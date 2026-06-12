---
title: Setup CD
description: >-
  Automate baseline updates for Recce Cloud with a continuous deployment workflow.
  Keep your dbt validation baseline current after every merge to main.
---

!!! tip "Following the onboarding guide?"
    Return to [Get Started with Recce Cloud](../getting-started/start-free-with-cloud.md#3-add-recce-to-cicd) after completing this page.

# Setup CD - Auto-Update Baseline

Manually updating your Recce Cloud baseline after every merge is tedious and error-prone. This guide shows you how to automate baseline updates so your data comparison stays current without manual intervention.

After completing this guide, your continuous deployment (CD) workflow automatically uploads dbt artifacts to Cloud whenever code merges to main.

## What This Does

**Automated Base Session Management** eliminates manual baseline maintenance:

- **Triggers**: Merge to main + scheduled updates + manual runs
- **Action**: Auto-update base Recce session with latest production artifacts
- **Benefit**: Current comparison baseline for all future PRs

## Prerequisites

Before setting up CD, ensure you have:

- [x] **Cloud account** - [Start free trial](https://cloud.reccehq.com/)
- [x] **Repository connected** to Cloud - [Connect Git Provider](../getting-started/start-free-with-cloud.md#2-connect-git-provider)
- [x] **dbt artifacts** - Know how to generate `manifest.json` and `catalog.json` from your dbt project
- [x] **Environment configured** - [Environment Setup](environment-setup.md) with `prod` target for base artifacts

## Environment strategy

This workflow uses the **main branch** with the `prod` target as the base environment. The base artifacts represent your production state, which PRs compare against.

See [Environment Setup](environment-setup.md) for profiles.yml configuration.

## Setup

### GitHub Actions

Create `.github/workflows/base-workflow.yml`:

```yaml linenums="1"
name: Update Base Metadata

on:
  push:
    branches: ["main"]
  schedule:
    - cron: "0 2 * * *"
  workflow_dispatch:

concurrency:
  group: ${{ github.workflow }}
  cancel-in-progress: true

jobs:
  update-base-session:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    permissions:
      contents: read

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Prepare dbt artifacts
        run: |
          dbt deps
          dbt build --target prod
          dbt docs generate --target prod
        env:
          SNOWFLAKE_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
          SNOWFLAKE_USER: ${{ secrets.SNOWFLAKE_USER }}
          SNOWFLAKE_PASSWORD: ${{ secrets.SNOWFLAKE_PASSWORD }}
          SNOWFLAKE_DATABASE: ${{ secrets.SNOWFLAKE_DATABASE }}
          SNOWFLAKE_WAREHOUSE: ${{ secrets.SNOWFLAKE_WAREHOUSE }}

      - name: Upload to Recce Cloud
        run: |
          pip install recce-cloud
          recce-cloud upload --type prod
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

**Key points:**

- `dbt build` and `dbt docs generate` create the required artifacts (`manifest.json` and `catalog.json`)
- `recce-cloud upload --type prod` uploads the Base metadata to Cloud
- [`GITHUB_TOKEN`](https://docs.github.com/en/actions/concepts/security/github_token) authenticates with Cloud

### GitLab CI/CD

Add to your `.gitlab-ci.yml`:

```yaml linenums="1" hl_lines="30-31"
stages:
  - build
  - upload

variables:
  DBT_TARGET_PROD: "prod"

# Production build - runs on schedule or main branch push
prod-build:
  stage: build
  image: python:3.11-slim
  script:
    - pip install -r requirements.txt
    - dbt deps
    # Optional: dbt build --target $DBT_TARGET_PROD
    - dbt docs generate --target $DBT_TARGET_PROD
  artifacts:
    paths:
      - target/
    expire_in: 7 days
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"
    - if: $CI_PIPELINE_SOURCE == "push" && $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH

# Upload to Recce Cloud
recce-upload-prod:
  stage: upload
  image: python:3.11-slim
  script:
    - pip install recce-cloud
    - recce-cloud upload --type prod
  dependencies:
    - prod-build
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"
    - if: $CI_PIPELINE_SOURCE == "push" && $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
```

**Key points:**

- Authentication is automatic via `CI_JOB_TOKEN`
- Configure schedule in **CI/CD → Schedules** (e.g., `0 2 * * *` for daily at 2 AM UTC)
- `recce-cloud upload --type prod` tells Recce this is a baseline session

### Platform Comparison

| Aspect               | GitHub Actions                      | GitLab CI/CD                                                                   |
| -------------------- | ----------------------------------- | ------------------------------------------------------------------------------ |
| **Config file**      | `.github/workflows/base-workflow.yml` | `.gitlab-ci.yml`                                                               |
| **Trigger on merge** | `on: push: branches: ["main"]`      | `if: $CI_PIPELINE_SOURCE == "push" && $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH` |
| **Schedule setup**   | In workflow YAML (`schedule:`)      | In UI: **CI/CD → Schedules**                                                   |
| **Authentication**   | Explicit (`GITHUB_TOKEN`)           | Automatic (`CI_JOB_TOKEN`)                                                     |
| **Manual trigger**   | `workflow_dispatch:`                | Pipeline run from UI                                                           |

## Verification

### Test the Workflow

**GitHub:**

1. Go to **Actions** tab → Select "Update Base Metadata"
2. Click **Run workflow** → Monitor for completion

**GitLab:**

1. Go to **CI/CD → Pipelines** → Click **Run pipeline**
2. Select **main** branch → Monitor for completion

### Verify Success

Look for these indicators:

- [x] **Workflow/Pipeline completes** without errors
- [x] **Base session updated** in [Cloud](https://cloud.reccehq.com)

**GitHub:**

![Recce Cloud Sessions page displaying a successfully uploaded production baseline from GitHub Actions](../assets/images/setup-guides/verify-setup-github-cd.png){: .shadow}

**GitLab:**

![Recce Cloud Sessions page displaying a successfully uploaded production baseline from GitLab CI](../assets/images/setup-guides/verify-setup-gitlab-cd.png){: .shadow}

### Expected Output

When the upload succeeds, you'll see output like this in your workflow logs:

**GitHub:**

```hl_lines="2 3 13"
─────────────────────────── CI Environment Detection ───────────────────────────
Platform: github-actions
Session Type: prod
Commit SHA: def456ab...
Source Branch: main
Repository: your-org/your-repo
Info: Using GITHUB_TOKEN for platform-specific authentication
────────────────────────── Creating/touching session ───────────────────────────
Session ID: abc123-def456-ghi789
Uploading manifest from path "target/manifest.json"
Uploading catalog from path "target/catalog.json"
Notifying upload completion...
──────────────────────────── Uploaded Successfully ─────────────────────────────
Uploaded dbt artifacts to Recce Cloud for session ID "abc123-def456-ghi789"
Artifacts from: "/home/runner/work/your-repo/your-repo/target"
```

**GitLab:**

```hl_lines="2 3 13"
─────────────────────────── CI Environment Detection ───────────────────────────
Platform: gitlab-ci
Session Type: prod
Commit SHA: a1b2c3d4...
Source Branch: main
Repository: your-org/your-project
Info: Using CI_JOB_TOKEN for platform-specific authentication
────────────────────────── Creating/touching session ───────────────────────────
Session ID: abc123-def456-ghi789
Uploading manifest from path "target/manifest.json"
Uploading catalog from path "target/catalog.json"
Notifying upload completion...
──────────────────────────── Uploaded Successfully ─────────────────────────────
Uploaded dbt artifacts to Recce Cloud for session ID "abc123-def456-ghi789"
Artifacts from: "/builds/your-org/your-project/target"
```

## Advanced Options

### Custom Artifact Path

If your dbt artifacts are in a non-standard location:

```bash
recce-cloud upload --type prod --target-path custom-target
```

### External Artifact Sources

You can download artifacts from external sources before uploading:

```yaml
# GitHub example
- name: Download from dbt Cloud
  run: |
    # Your download logic here
    # Artifacts should end up in target/ directory

- name: Upload to Recce Cloud
  run: |
    pip install recce-cloud
    recce-cloud upload --type prod
```

### Dry Run Testing

Test your configuration without actually uploading:

```bash
recce-cloud upload --type prod --dry-run
```

## Troubleshooting

### Missing dbt artifacts

**Error**: `Missing manifest.json` or `Missing catalog.json`

**Solution**: Ensure `dbt docs generate` runs successfully before upload:

**GitHub:**

```yaml
- name: Prepare dbt artifacts
  run: |
    dbt deps
    dbt docs generate --target prod  # Required
```

**GitLab:**

```yaml
prod-build:
  script:
    - dbt deps
    - dbt docs generate --target $DBT_TARGET_PROD # Required
  artifacts:
    paths:
      - target/
```

### Authentication issues

**Error**: `Failed to create session: 401 Unauthorized`

**Solutions**:

1. Verify your repository is connected in [Cloud settings](https://cloud.reccehq.com/settings)
2. **For GitHub**: Ensure `GITHUB_TOKEN` is passed explicitly to the upload step and the job has `contents: read` permission
3. **For GitLab**: Verify project has GitLab integration configured
   - Check that you've created a [Personal Access Token](connect-git.md#connect-gitlab)
   - Ensure the token has appropriate scope (`api` or `read_api`)
   - Verify the project is connected in Cloud settings

### Upload failures

**Error**: `Failed to upload manifest/catalog`

**Solutions**:

1. Check network connectivity to Cloud
2. Verify artifact files exist in `target/` directory
3. Review workflow/pipeline logs for detailed error messages
4. **For GitLab**: Ensure artifacts are passed between jobs:

   ```yaml
   prod-build:
     artifacts:
       paths:
         - target/ # Must include dbt artifacts

   recce-upload-prod:
     dependencies:
       - prod-build # Required to access artifacts
   ```

### Session not appearing

**Issue**: Upload succeeds but session doesn't appear in Cloud

**Solutions**:

1. Check you're viewing the correct repository in Cloud
2. Verify you're looking at the production/base sessions (not PR/MR sessions)
3. Check session filters in Cloud (may be hidden by filters)
4. Refresh the Cloud page

### Schedule not triggering (GitLab only)

**Issue**: Scheduled pipeline doesn't run

**Solutions**:

1. Verify schedule is **Active** in CI/CD → Schedules
2. Check schedule timezone settings (UTC by default)
3. Ensure target branch (`main`) exists
4. Review project's CI/CD minutes quota
5. Verify schedule owner has appropriate permissions

## Next Steps

**[Setup CI](setup-ci.md)** to automatically validate PR/MR changes against your updated base session. This completes your CI/CD pipeline by adding automated data validation for every pull request or merge request.
