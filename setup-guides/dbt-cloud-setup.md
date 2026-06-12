---
title: dbt Cloud Setup
description: >-
  Integrate Recce with dbt Cloud for automated pull request data validation.
  Retrieve dbt Cloud artifacts and compare PR changes against production.
---

# dbt Cloud Setup

When your dbt project runs on dbt Cloud, validating PR data changes requires retrieving artifacts from the dbt Cloud API rather than generating them locally.

## Goal

After completing this tutorial, every PR triggers automated data validation. Recce compares your PR changes against production, with results visible in Recce Cloud.

## Prerequisites

- [x] **Cloud account**: free trial at [cloud.reccehq.com](https://cloud.reccehq.com)
- [x] **dbt Cloud account**: with CI (continuous integration) and CD (continuous deployment) jobs configured
- [x] **dbt Cloud API token**: with read access to job artifacts
- [x] **GitHub repository**: with admin access to add workflows and secrets

## How Recce retrieves dbt Cloud artifacts

Recce needs both base (production) and current (PR) dbt artifacts to compare changes. When using dbt Cloud, these artifacts live in dbt Cloud's API rather than your local filesystem. Your GitHub Actions workflows retrieve them via API calls and upload to Cloud.

Two workflows handle this:

1. **Base workflow** (on merge to main): Downloads production artifacts from your CD job → uploads with `recce-cloud upload --type prod`
2. **PR workflow** (on pull request): Downloads PR artifacts from your CI job → uploads with `recce-cloud upload`

## Setup steps

### 1. Enable "Generate docs on run" in dbt Cloud

Recce requires `catalog.json` for schema comparisons. Enable documentation generation for both your CI and CD jobs in dbt Cloud.

**For CD jobs (production):**

1. Go to your CD job settings in dbt Cloud
2. Under **Execution settings**, enable **Generate docs on run**

**For CI jobs (pull requests):**

1. Go to your CI job settings in dbt Cloud
2. Under **Advanced settings**, enable **Generate docs on run**

!!! note
    Without this setting, dbt Cloud won't generate `catalog.json`, and Recce won't be able to compare schemas between environments.

### 2. Get your dbt Cloud credentials

Collect the following from your dbt Cloud account:

| Credential | Where to find it |
| --- | --- |
| **Account ID** | URL when viewing any job: `cloud.getdbt.com/deploy/{ACCOUNT_ID}/projects/...` |
| **CD Job ID** | URL of your production/CD job: `...jobs/{JOB_ID}` |
| **CI Job ID** | URL of your PR/CI job: `...jobs/{JOB_ID}` |
| **API Token** | Account Settings > API Tokens > Create Service Token |

!!! tip
    Create a service token with "Job Admin" or "Member" permissions. This allows read access to job artifacts.

### 3. Configure GitHub secrets

Add the following secrets to your GitHub repository (Settings > Secrets and variables > Actions):

**dbt Cloud secrets:**

- `DBT_CLOUD_API_TOKEN` - Your dbt Cloud API token
- `DBT_CLOUD_ACCOUNT_ID` - Your dbt Cloud account ID
- `DBT_CLOUD_CD_JOB_ID` - Your production/CD job ID
- `DBT_CLOUD_CI_JOB_ID` - Your PR/CI job ID

!!! note
    `GITHUB_TOKEN` is automatically provided by GitHub Actions, no configuration needed.

### 4. Create the base workflow (CD)

Create `.github/workflows/recce-base.yml` to update your production baseline when merging to main.

```yaml
name: Update Base Metadata (dbt Cloud)

on:
  push:
    branches: [main]
  workflow_dispatch:

env:
  DBT_CLOUD_API_BASE: "https://cloud.getdbt.com/api/v2/accounts/${{ secrets.DBT_CLOUD_ACCOUNT_ID }}"
  DBT_CLOUD_API_TOKEN: ${{ secrets.DBT_CLOUD_API_TOKEN }}

jobs:
  update-base:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install recce-cloud
        run: pip install recce-cloud

      - name: Retrieve artifacts from CD job
        env:
          DBT_CLOUD_CD_JOB_ID: ${{ secrets.DBT_CLOUD_CD_JOB_ID }}
        run: |
          set -eo pipefail
          CD_RUNS_URL="${DBT_CLOUD_API_BASE}/runs/?job_definition_id=${DBT_CLOUD_CD_JOB_ID}&order_by=-id&limit=1"
          CD_RUNS_RESPONSE=$(curl -sSf -H "Authorization: Bearer ${DBT_CLOUD_API_TOKEN}" "${CD_RUNS_URL}")
          DBT_CLOUD_CD_RUN_ID=$(echo "${CD_RUNS_RESPONSE}" | jq -r ".data[0].id")
          mkdir -p target
          for artifact in manifest.json catalog.json; do
            ARTIFACT_URL="${DBT_CLOUD_API_BASE}/runs/${DBT_CLOUD_CD_RUN_ID}/artifacts/${artifact}"
            curl -sSf -H "Authorization: Bearer ${DBT_CLOUD_API_TOKEN}" "${ARTIFACT_URL}" -o "target/${artifact}"
          done

      - name: Upload to Recce Cloud
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: recce-cloud upload --type prod
```

### 5. Create the PR workflow (CI)

Create `.github/workflows/recce-pr.yml` to validate PR changes.

```yaml
name: Validate PR (dbt Cloud)

on:
  pull_request:
    branches: [main]

env:
  DBT_CLOUD_API_BASE: "https://cloud.getdbt.com/api/v2/accounts/${{ secrets.DBT_CLOUD_ACCOUNT_ID }}"
  DBT_CLOUD_API_TOKEN: ${{ secrets.DBT_CLOUD_API_TOKEN }}

jobs:
  validate-pr:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install recce-cloud
        run: pip install recce-cloud

      - name: Wait for dbt Cloud CI job
        env:
          DBT_CLOUD_CI_JOB_ID: ${{ secrets.DBT_CLOUD_CI_JOB_ID }}
          CURRENT_GITHUB_SHA: ${{ github.event.pull_request.head.sha }}
        run: |
          set -eo pipefail
          CI_RUNS_URL="${DBT_CLOUD_API_BASE}/runs/?job_definition_id=${DBT_CLOUD_CI_JOB_ID}&order_by=-id"
          fetch_ci_run_id() {
            CI_RUNS_RESPONSE=$(curl -sSf -H "Authorization: Bearer ${DBT_CLOUD_API_TOKEN}" "${CI_RUNS_URL}")
            echo "${CI_RUNS_RESPONSE}" | jq -r ".data[] | select(.git_sha == \"${CURRENT_GITHUB_SHA}\") | .id" | head -n1
          }
          DBT_CLOUD_CI_RUN_ID=$(fetch_ci_run_id)
          while [ -z "$DBT_CLOUD_CI_RUN_ID" ]; do
            echo "Waiting for dbt Cloud CI job to start..."
            sleep 10
            DBT_CLOUD_CI_RUN_ID=$(fetch_ci_run_id)
          done
          echo "DBT_CLOUD_CI_RUN_ID=${DBT_CLOUD_CI_RUN_ID}" >> $GITHUB_ENV
          CI_RUN_URL="${DBT_CLOUD_API_BASE}/runs/${DBT_CLOUD_CI_RUN_ID}/"
          while true; do
            CI_RUN_RESPONSE=$(curl -sSf -H "Authorization: Bearer ${DBT_CLOUD_API_TOKEN}" "${CI_RUN_URL}")
            CI_RUN_SUCCESS=$(echo "${CI_RUN_RESPONSE}" | jq '.data.is_complete and .data.is_success')
            CI_RUN_FAILED=$(echo "${CI_RUN_RESPONSE}" | jq '.data.is_complete and (.data.is_error or .data.is_cancelled)')
            if $CI_RUN_SUCCESS; then
              echo "dbt Cloud CI job completed successfully."
              break
            elif $CI_RUN_FAILED; then
              status=$(echo ${CI_RUN_RESPONSE} | jq -r '.data.status_humanized')
              echo "dbt Cloud CI job failed or was cancelled. Status: $status"
              exit 1
            fi
            echo "Waiting for dbt Cloud CI job to complete..."
            sleep 10
          done

      - name: Retrieve artifacts from CI job
        run: |
          set -eo pipefail
          mkdir -p target
          for artifact in manifest.json catalog.json; do
            ARTIFACT_URL="${DBT_CLOUD_API_BASE}/runs/${DBT_CLOUD_CI_RUN_ID}/artifacts/${artifact}"
            curl -sSf -H "Authorization: Bearer ${DBT_CLOUD_API_TOKEN}" "${ARTIFACT_URL}" -o "target/${artifact}"
          done

      - name: Upload to Recce Cloud
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: recce-cloud upload
```

## Verification

After setting up:

1. **Trigger the base workflow** - Push to main or run manually to upload production baseline
2. **Create a test PR** with a small model change
3. **Wait for dbt Cloud CI job** to complete
4. **Check GitHub Actions** - the Recce PR workflow should run after dbt Cloud CI completes
5. **Open Cloud** - the PR session appears with validation results

!!! tip
    Run the base workflow first to establish your production baseline. The PR workflow compares against this baseline.

## Troubleshooting

| Issue | Solution |
| --- | --- |
| "CD run not found" | Ensure your CD job has run on the base branch commit. Try rebasing your PR to trigger a new CD run. |
| "CI job timeout" | The workflow waits for dbt Cloud CI to complete. Check if your CI job is stuck or taking longer than expected. |
| "Artifact not found" | Verify "Generate docs on run" is enabled for both CI and CD jobs. |
| "API authentication failed" | Check your `DBT_CLOUD_API_TOKEN` has correct permissions and is stored in GitHub secrets. |

### CD job timing considerations

The base workflow retrieves artifacts from the latest CD job run. For accurate comparisons, ensure your dbt Cloud CD job runs on every merge to main.

If your CD job runs on a schedule:

- The baseline may be outdated compared to the actual main branch
- Consider triggering the CD job manually before validating PRs

## Next steps

- [Get Started with Cloud](../getting-started/start-free-with-cloud.md) - Standard setup for self-hosted dbt
- [Configure CD to establish your production baseline](setup-cd.md)
- [Configure CI for automated PR validation](setup-ci.md)
- [Learn environment strategies for reliable comparisons](environment-best-practices.md)
