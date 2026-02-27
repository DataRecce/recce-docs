---
title: dbt Cloud Setup
---

# dbt Cloud Setup

This guide helps you set up Recce Cloud when your dbt project runs on dbt Cloud. Since dbt Cloud manages your dbt runs, you'll retrieve artifacts via the dbt Cloud API instead of generating them locally.

## Goal

After completing this setup, you'll have automated data validation on every pull request, with Recce comparing your PR changes against production. The workflow retrieves dbt artifacts directly from dbt Cloud and uploads them to Recce Cloud for validation.

## Prerequisites

- [x] **Recce Cloud account**: free trial at [cloud.reccehq.com](https://cloud.reccehq.com)
- [x] **dbt Cloud account**: with CI and CD jobs configured
- [x] **dbt Cloud API token**: with read access to job artifacts
- [x] **GitHub repository**: with admin access to add workflows and secrets
- [x] **Data warehouse**: read access for data diffing

## How it works

When your dbt project runs on dbt Cloud, the artifacts (`manifest.json`, `catalog.json`) are stored in dbt Cloud rather than your local environment. To use Recce, you'll:

1. Retrieve Base artifacts from your CD job (production runs)
2. Retrieve Current artifacts from your CI job (PR runs)
3. Upload both to Recce Cloud for validation

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

**Recce Cloud secrets:**

- `RECCE_STATE_PASSWORD` - Password to encrypt state files (create any secure string)

**Data warehouse secrets** (for data diffing):

Add your warehouse credentials based on your adapter. For Snowflake:

- `SNOWFLAKE_ACCOUNT`
- `SNOWFLAKE_USER`
- `SNOWFLAKE_PASSWORD`
- `SNOWFLAKE_SCHEMA`

!!! note
    `GITHUB_TOKEN` is automatically provided by GitHub Actions, no configuration needed.

### 4. Create the GitHub Actions workflow

Create `.github/workflows/recce-dbt-cloud.yml` with the workflow configuration. The workflow:

1. **Retrieves Base artifacts** from your CD job run matching the PR's base commit
2. **Retrieves Current artifacts** from your CI job run for the PR's head commit
3. **Runs Recce validation** and uploads results to Recce Cloud
4. **Posts a summary comment** on the pull request

```yaml
name: Recce with dbt Cloud

on:
  pull_request:
    branches: [main]

env:
  DBT_CLOUD_API_BASE: "https://cloud.getdbt.com/api/v2/accounts/${{ secrets.DBT_CLOUD_ACCOUNT_ID }}"
  DBT_CLOUD_API_TOKEN: ${{ secrets.DBT_CLOUD_API_TOKEN }}

jobs:
  recce-validation:
    name: Validate PR with Recce
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"
          cache: "pip"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Retrieve Base artifacts (CD job)
        env:
          DBT_CLOUD_CD_JOB_ID: ${{ secrets.DBT_CLOUD_CD_JOB_ID }}
          BASE_GITHUB_SHA: ${{ github.event.pull_request.base.sha }}
        run: |
          set -eo pipefail
          CD_RUNS_URL="${DBT_CLOUD_API_BASE}/runs/?job_definition_id=${DBT_CLOUD_CD_JOB_ID}&order_by=-id"
          CD_RUNS_RESPONSE=$(curl -sSf -H "Authorization: Bearer ${DBT_CLOUD_API_TOKEN}" "${CD_RUNS_URL}")
          DBT_CLOUD_CD_RUN_ID=$(echo "${CD_RUNS_RESPONSE}" | jq -r ".data[] | select(.git_sha == \"${BASE_GITHUB_SHA}\") | .id" | head -n1)
          echo "DBT_CLOUD_CD_RUN_ID=${DBT_CLOUD_CD_RUN_ID}" >> $GITHUB_ENV
          mkdir -p target-base
          for artifact in manifest.json catalog.json; do
            ARTIFACT_URL="${DBT_CLOUD_API_BASE}/runs/${DBT_CLOUD_CD_RUN_ID}/artifacts/${artifact}"
            curl -sSf -H "Authorization: Bearer ${DBT_CLOUD_API_TOKEN}" "${ARTIFACT_URL}" -o "target-base/${artifact}"
          done

      - name: Retrieve Current artifacts (CI job)
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
            sleep 5
            DBT_CLOUD_CI_RUN_ID=$(fetch_ci_run_id)
          done
          echo "DBT_CLOUD_CI_RUN_ID=${DBT_CLOUD_CI_RUN_ID}" >> $GITHUB_ENV
          CI_RUN_URL="${DBT_CLOUD_API_BASE}/runs/${DBT_CLOUD_CI_RUN_ID}/"
          while true; do
            CI_RUN_RESPONSE=$(curl -sSf -H "Authorization: Bearer ${DBT_CLOUD_API_TOKEN}" "${CI_RUN_URL}")
            CI_RUN_SUCCESS=$(echo "${CI_RUN_RESPONSE}" | jq '.data.is_complete and .data.is_success')
            CI_RUN_FAILED=$(echo "${CI_RUN_RESPONSE}" | jq '.data.is_complete and (.data.is_error or .data.is_cancelled)')
            if $CI_RUN_SUCCESS; then
              echo "CI job completed successfully."
              break
            elif $CI_RUN_FAILED; then
              status=$(echo ${CI_RUN_RESPONSE} | jq -r '.data.status_humanized')
              echo "CI job failed or was cancelled. Status: $status"
              exit 1
            fi
            sleep 5
          done
          mkdir -p target
          for artifact in manifest.json catalog.json; do
            ARTIFACT_URL="${DBT_CLOUD_API_BASE}/runs/${DBT_CLOUD_CI_RUN_ID}/artifacts/${artifact}"
            curl -sSf -H "Authorization: Bearer ${DBT_CLOUD_API_TOKEN}" "${ARTIFACT_URL}" -o "target/${artifact}"
          done

      - name: Run Recce validation
        env:
          SNOWFLAKE_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
          SNOWFLAKE_USER: ${{ secrets.SNOWFLAKE_USER }}
          SNOWFLAKE_PASSWORD: ${{ secrets.SNOWFLAKE_PASSWORD }}
          SNOWFLAKE_SCHEMA: "PR_${{ github.event.pull_request.number }}"
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          RECCE_STATE_PASSWORD: ${{ secrets.RECCE_STATE_PASSWORD }}
        run: recce run --cloud

      - name: Generate Recce summary
        id: recce-summary
        env:
          SNOWFLAKE_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
          SNOWFLAKE_USER: ${{ secrets.SNOWFLAKE_USER }}
          SNOWFLAKE_PASSWORD: ${{ secrets.SNOWFLAKE_PASSWORD }}
          SNOWFLAKE_SCHEMA: "PR_${{ github.event.pull_request.number }}"
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          RECCE_STATE_PASSWORD: ${{ secrets.RECCE_STATE_PASSWORD }}
        run: |
          set -eo pipefail
          recce summary --cloud > recce_summary.md
          cat recce_summary.md >> $GITHUB_STEP_SUMMARY

      - name: Comment on pull request
        uses: thollander/actions-comment-pull-request@v2
        with:
          filePath: recce_summary.md
          comment_tag: recce
```

### 5. Adapt for your data warehouse

The workflow above uses Snowflake. Update the environment variables in the "Run Recce validation" and "Generate Recce summary" steps to match your warehouse configuration.

For other warehouses, replace the Snowflake variables with your adapter's required credentials. See [Connect to Warehouse](../5-data-diffing/connect-to-warehouse.md) for adapter-specific configuration.

## Verification

After setting up:

1. **Create a test PR** with a small model change
2. **Wait for dbt Cloud CI job** to complete
3. **Check GitHub Actions** - the Recce workflow should run
4. **Review the PR comment** - Recce validation summary appears
5. **Launch Recce instance** - from Recce Cloud dashboard, open the PR session

!!! tip
    If the workflow fails on the first run, check that your CD job has run on the base commit. The workflow looks for artifacts from a specific git SHA.

## Troubleshooting

| Issue | Solution |
| --- | --- |
| "CD run not found" | Ensure your CD job has run on the base branch commit. Try rebasing your PR to trigger a new CD run. |
| "CI job timeout" | The workflow waits for dbt Cloud CI to complete. Check if your CI job is stuck or taking longer than expected. |
| "Artifact not found" | Verify "Generate docs on run" is enabled for both CI and CD jobs. |
| "API authentication failed" | Check your `DBT_CLOUD_API_TOKEN` has correct permissions and is stored in GitHub secrets. |
| "Warehouse connection failed" | Verify warehouse credentials in GitHub secrets. Check IP whitelisting if applicable. |
| No PR comment appears | Ensure `GITHUB_TOKEN` has write permissions for pull requests. Check workflow permissions. |

### CD job timing considerations

The workflow retrieves Base artifacts from the CD job run that matches the PR's base commit SHA. If your CD job runs on a schedule (not on every merge), the base commit might not have artifacts available.

**Solutions:**

- Configure CD to run on merge to main (recommended)
- Rebase your PR to a commit that has CD artifacts
- Modify the workflow to use the latest CD run instead of commit-matched artifacts

## Related

- [Get Started with Recce Cloud](./start-free-with-cloud.md) - Standard setup for self-hosted dbt
- [Setup CD](../7-cicd/setup-cd.md) - CD workflow configuration
- [Setup CI](../7-cicd/setup-ci.md) - CI workflow configuration
- [Best Practices for Preparing Environments](../7-cicd/best-practices-prep-env.md) - Environment strategy guidance
