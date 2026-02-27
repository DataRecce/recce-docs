---
title: Environment Setup
---

# Environment Setup

This guide covers advanced configuration for data teams with complex setups—multiple schemas, separate development warehouses, or CI/CD automation requirements.

## Goal

Configure your dbt targets and CI/CD environment variables to support base vs current comparison in Recce. After completing this guide, your CI/CD workflows can automatically create isolated schemas for each PR and compare them against production.

## Prerequisites

- [x] **dbt project**: A working dbt project with `profiles.yml` configured
- [x] **CI/CD platform**: GitHub Actions, GitLab CI, or similar
- [x] **Warehouse access**: Credentials with permissions to create schemas dynamically

## How CI/CD works with Recce

Recce uses both continuous delivery (CD) and continuous integration (CI) to automate data validation:

- **CD (Continuous Delivery)**: Runs after merge to main. Updates baseline artifacts with latest production state.
- **CI (Continuous Integration)**: Runs on PR/MR. Validates proposed changes against baseline.

**Set up CD first**, then CI. CD establishes your baseline (production artifacts), which CI uses for comparison.

## Why separate schemas matter

Recce compares two sets of data to validate changes:

- **Base**: The production state (main branch)
- **Current**: The PR branch with your changes

For accurate validation, these must point to different schemas in your warehouse. Without separation, you would compare identical data and miss meaningful differences.

Common patterns include:

| Pattern | Base Schema | Current Schema | Best For |
|---------|-------------|----------------|----------|
| Shared dev | `public` (prod) | `dev` | Solo developers or small teams |
| Schema-per-PR | `public` (prod) | `pr_123` | Teams with many concurrent PRs |
| Staging-based | `staging` | `pr_123` | Teams wanting consistent source data |

## Configure profiles.yml

Your `profiles.yml` file defines how dbt connects to your warehouse. Add separate targets for production, development, and CI.

### Example: Snowflake with dynamic CI schema

```yaml
jaffle_shop:
  target: dev
  outputs:
    # Local development
    dev:
      type: snowflake
      account: "{{ env_var('SNOWFLAKE_ACCOUNT') }}"
      user: "{{ env_var('SNOWFLAKE_USER') }}"
      password: "{{ env_var('SNOWFLAKE_PASSWORD') }}"
      role: DEVELOPER
      database: analytics
      warehouse: COMPUTE_WH
      schema: "{{ env_var('DEV_SCHEMA', 'dev_' ~ env_var('USER', 'default')) }}"
      threads: 4

    # CI environment with dynamic schema
    ci:
      type: snowflake
      account: "{{ env_var('SNOWFLAKE_ACCOUNT') }}"
      user: "{{ env_var('SNOWFLAKE_USER') }}"
      password: "{{ env_var('SNOWFLAKE_PASSWORD') }}"
      role: DEVELOPER
      database: analytics
      warehouse: COMPUTE_WH
      schema: "{{ env_var('CI_SCHEMA') }}"
      threads: 4

    # Production
    prod:
      type: snowflake
      account: "{{ env_var('SNOWFLAKE_ACCOUNT') }}"
      user: "{{ env_var('SNOWFLAKE_USER') }}"
      password: "{{ env_var('SNOWFLAKE_PASSWORD') }}"
      role: DEVELOPER
      database: analytics
      warehouse: COMPUTE_WH
      schema: public
      threads: 4
```

Key points:

- The `ci` target uses `env_var('CI_SCHEMA')` for dynamic schema assignment
- The `prod` target uses a fixed schema (`public`) for consistency
- The `dev` target can use a developer-specific schema or a shared one

### Example: BigQuery with dataset separation

```yaml
jaffle_shop:
  target: dev
  outputs:
    dev:
      type: bigquery
      method: service-account
      project: "{{ env_var('GCP_PROJECT') }}"
      dataset: "{{ env_var('DEV_DATASET', 'dev') }}"
      threads: 4
      keyfile: "{{ env_var('GOOGLE_APPLICATION_CREDENTIALS') }}"

    ci:
      type: bigquery
      method: service-account
      project: "{{ env_var('GCP_PROJECT') }}"
      dataset: "{{ env_var('CI_DATASET') }}"
      threads: 4
      keyfile: "{{ env_var('GOOGLE_APPLICATION_CREDENTIALS') }}"

    prod:
      type: bigquery
      method: service-account
      project: "{{ env_var('GCP_PROJECT') }}"
      dataset: production
      threads: 4
      keyfile: "{{ env_var('GOOGLE_APPLICATION_CREDENTIALS') }}"
```

## Set CI/CD environment variables

Your CI/CD workflow sets the schema dynamically for each PR. This creates isolated data for validation.

### GitHub Actions example

In your PR workflow file (`.github/workflows/pr-recce.yml`):

```yaml
name: PR Validation

on:
  pull_request:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest
    env:
      # Dynamic schema based on PR number
      CI_SCHEMA: "pr_${{ github.event.pull_request.number }}"

      # Warehouse credentials from secrets
      SNOWFLAKE_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
      SNOWFLAKE_USER: ${{ secrets.SNOWFLAKE_USER }}
      SNOWFLAKE_PASSWORD: ${{ secrets.SNOWFLAKE_PASSWORD }}

    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Build current branch
        run: |
          dbt deps
          dbt build --target ci
          dbt docs generate --target ci
```

This creates schemas like `pr_123`, `pr_456` for each PR automatically.

### GitLab CI example

In your `.gitlab-ci.yml`:

```yaml
variables:
  CI_SCHEMA: "mr_${CI_MERGE_REQUEST_IID}"

validate_pr:
  stage: test
  script:
    - pip install -r requirements.txt
    - dbt deps
    - dbt build --target ci
    - dbt docs generate --target ci
  rules:
    - if: $CI_MERGE_REQUEST_IID
```

## Common patterns

### Pattern 1: Schema-per-PR

Creates an isolated schema for each PR. Ideal for teams with multiple concurrent PRs.

```yaml
# profiles.yml
ci:
  schema: "{{ env_var('CI_SCHEMA') }}"

# GitHub Actions
env:
  CI_SCHEMA: "pr_${{ github.event.pull_request.number }}"
```

Benefits:

- Complete isolation between PRs
- Parallel PR validation without conflicts
- Easy cleanup by dropping the schema

### Pattern 2: Shared development schema

Uses a single `dev` schema for all development work. Simpler but requires coordination.

```yaml
# profiles.yml
dev:
  schema: dev

# No dynamic schema needed
```

Benefits:

- Simpler configuration
- Faster iteration for solo developers
- Lower warehouse storage usage

### Pattern 3: Staging as base

Uses a staging schema (with limited data) as the base for faster comparisons.

```yaml
# profiles.yml
staging:
  schema: staging  # Base for comparison

ci:
  schema: "{{ env_var('CI_SCHEMA') }}"  # Current PR schema
```

Benefits:

- Consistent source data between base and current
- Faster diffs with limited data ranges
- Reduced warehouse costs

See [Environment Best Practices](environment-best-practices.md) for detailed strategies on limiting data ranges and managing source data consistency.

## Verification

After configuring your setup, verify that both base and current schemas are accessible.

### Check configuration locally

Run the debug command to verify your profile configuration:

```shell
recce debug
```

This checks artifacts, directories, and warehouse connections.

### Verify in CI

Add a verification step to your workflow:

```yaml
- name: Verify schema access
  run: |
    dbt debug --target ci
    echo "CI_SCHEMA is set to: $CI_SCHEMA"
```

### Verify in Recce interface

Launch Recce and check **Environment Info** in the top-right corner. You should see:

- **Base**: Your production schema (e.g., `public`)
- **Current**: Your PR-specific schema (e.g., `pr_123`)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Schema creation fails | Verify your CI credentials have `CREATE SCHEMA` permissions |
| Environment variable not found | Check that secrets are configured in your CI/CD platform settings |
| Base and current show same schema | Ensure `--target ci` is used in CI, not `--target dev` |
| Profile not found | Verify `profiles.yml` is accessible in CI (check path or use `DBT_PROFILES_DIR`) |
| Connection timeout | Check warehouse IP allowlists include CI runner IP ranges |

### Debugging environment variables

If schemas are not resolving correctly, add debugging to your workflow:

```yaml
- name: Debug environment
  run: |
    echo "CI_SCHEMA: $CI_SCHEMA"
    dbt debug --target ci 2>&1 | grep -i schema
```

## Related

- [Get Started with Recce Cloud](start-free-with-cloud.md) - Complete onboarding guide
- [Environment Best Practices](environment-best-practices.md) - Strategies for source data and schema management
- [Setup CD](setup-cd.md) - CD workflow for GitHub Actions and GitLab CI
- [Setup CI](setup-ci.md) - CI workflow for GitHub Actions and GitLab CI
