---
title: Setup CD
---

# Setup CD

Set up automatic updates for your Recce Cloud base sessions. Keep your data comparison baseline current every time you merge to main, with no manual work required.

## Purpose

**Automated Base Session Management** eliminates manual baseline maintenance.

- **Triggers**: PR merge to main + scheduled updates
- **Action**: Auto-update base Recce session
- **Benefit**: Current comparison baseline for future PRs

## Prerequisites

You need `manifest.json` and `catalog.json` files (dbt artifacts) for Recce Cloud. See [Start Free with Cloud](../../2-getting-started/start-free-with-cloud.md) for instructions on preparing these files.

## Implementation

### 1. Core Workflow

Create `.github/workflows/cd-workflow.yml`:

```yaml
name: Update Base Recce Session

on:
  push:
    branches: ["main"]
  schedule:
    - cron: "0 2 * * *" # Daily at 2 AM UTC
  workflow_dispatch:

concurrency:
  group: ${{ github.workflow }}
  cancel-in-progress: true

jobs:
  update-base-session:
    runs-on: ubuntu-latest
    timeout-minutes: 30

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Prepare dbt artifacts
        run: |
          # Install dbt packages
          dbt deps

          # Optional: Build tables to ensure they're materialized and updated
          # dbt build --target prod

          # Required: Generate artifacts (provides all we need)
          dbt docs generate --target prod
        env:
          DBT_ENV_SECRET_KEY: ${{ secrets.DBT_ENV_SECRET_KEY }}

      - name: Update Recce Cloud Base Session
        uses: DataRecce/recce-cloud-cicd-action@v0.1
        # This action automatically uploads artifacts to Recce Cloud
```

### 2. Artifact Preparation Options

**Default: Fresh Build** (shown in example above)

- `dbt docs generate` is required and provides the needed `manifest.json` and `catalog.json` artifacts.
- `dbt build` is optional but ensures tables are materialized and updated.

**Alternative Methods:**

- **External Download**: Download from dbt Cloud, Paradime, or other platforms
- **Pipeline Integration**: Use existing dbt build workflows


### 3. Verification

#### Manual Trigger Test

1. Go to **Actions** tab in your repository
2. Select "Update Base Recce Session" workflow
3. Click **Run workflow** button
4. Monitor the run for successful completion

#### Verify Success

- ✅ **Workflow completes** without errors in Actions tab
- ✅ **Base session updated** in Recce Cloud dashboard

![Recce Cloud dashboard showing updated base sessions](/assets/images/7-cicd/verify-setup-cd.png){: .shadow}

## Next Steps

**[Setup CI](./setup-ci.md)** to automatically validate PR changes against your updated base session. This completes your CI/CD pipeline by adding automated data validation for every pull request.
