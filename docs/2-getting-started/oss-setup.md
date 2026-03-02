---
title: OSS Setup
---

# Set Up Recce OSS

When you change data models, you need to compare the data before and after to catch unintended impacts. Recce OSS lets you run this validation locally.

**Goal:** Install and run Recce locally for manual data validation.

Recce OSS gives you the core validation engine to run locally. For the full experience with Recce Agent assistance on PRs and during development, see [Cloud vs Open Source](../1-whats-recce/cloud-vs-oss.md).

## Prerequisites

- [x] Python 3.9+ installed
- [x] A dbt project with at least one model
- [x] Git installed (for version comparison)

## Steps

### 1. Install Recce

Install Recce in your dbt project's virtual environment.

```shell
pip install recce
```

**Expected result:** Installation completes without errors.

### 2. Generate base environment artifacts

Recce compares two states of your dbt project. First, generate artifacts for your base (production) state.

```shell
git checkout main
dbt docs generate --target-path ./target-base
```

**Expected result:** `target-base/` folder contains `manifest.json` and `catalog.json`.

!!! note "Different approaches by environment"
    - **File-based (DuckDB):** Run `dbt build` first to create data. See [Jaffle Shop Tutorial](jaffle-shop-tutorial.md).
    - **Cloud warehouses with dbt Cloud:** Download artifacts from dbt Cloud API. See [For dbt Cloud Users](#for-dbt-cloud-users) below.

### 3. Generate current environment artifacts

Switch to your development branch and generate artifacts for comparison.

```shell
git checkout your-feature-branch
dbt run
dbt docs generate
```

**Expected result:** `target/` folder contains updated `manifest.json` and `catalog.json`.

### 4. Start Recce server

Launch the Recce web interface.

```shell
recce server
```

**Expected result:** Server starts and displays:

```
Recce server is running at http://0.0.0.0:8000
```

### 5. Explore changes in the UI

Open http://localhost:8000 in your browser.

- **Lineage tab:** See which models changed and their downstream impact
- **Query tab:** Run SQL queries to compare data between base and current states

**Expected result:** Lineage Diff shows your modified models highlighted.

### 6. Add validation checks to checklist

After running a query or diff:

1. Review the results
2. Click **Add to Checklist** to save the validation
3. Repeat for each check you want to track

**Expected result:** Checklist shows your saved validations.

## Verify Success

Run `recce server` and confirm you can:

1. See Lineage Diff between base and current
2. Run a Query Diff on a modified model
3. Add the result to your checklist

## Try It: Jaffle Shop Tutorial

Want a hands-on walkthrough with DuckDB? The [Jaffle Shop Tutorial](jaffle-shop-tutorial.md) guides you through making a model change, comparing data, and validating the impact.

## For dbt Cloud Users

If you use dbt Cloud for CI/CD, download production artifacts instead of generating them locally.

**Get artifacts from dbt Cloud API:**

```shell
# Set your dbt Cloud credentials
export DBT_CLOUD_API_TOKEN="your-token"
export DBT_CLOUD_ACCOUNT_ID="your-account-id"
export DBT_CLOUD_JOB_ID="your-production-job-id"

# Download artifacts from your production job
curl -H "Authorization: Token $DBT_CLOUD_API_TOKEN" \
  "https://cloud.getdbt.com/api/v2/accounts/$DBT_CLOUD_ACCOUNT_ID/jobs/$DBT_CLOUD_JOB_ID/artifacts/manifest.json" \
  -o target-base/manifest.json

curl -H "Authorization: Token $DBT_CLOUD_API_TOKEN" \
  "https://cloud.getdbt.com/api/v2/accounts/$DBT_CLOUD_ACCOUNT_ID/jobs/$DBT_CLOUD_JOB_ID/artifacts/catalog.json" \
  -o target-base/catalog.json
```

Then generate current artifacts locally (`dbt docs generate`) and run `recce server` as usual.

!!! tip "Recce Cloud automates this"
    With Recce Cloud, the Agent retrieves artifacts automatically — no manual downloads. See [Start Free with Cloud](start-free-with-cloud.md).

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "No artifacts found" error | Run `dbt docs generate` for both base and current states |
| Empty Lineage Diff | Ensure you have uncommitted model changes vs the base branch |
| Port 8000 already in use | Use `recce server --port 8001` to specify a different port |

## Next Steps

- [Cloud vs Open Source](../1-whats-recce/cloud-vs-oss.md) — Compare OSS and Cloud features
- [Start Free with Cloud](start-free-with-cloud.md) — Get Recce Agent on your PRs and CLI
