---
title: Environment Setup
description: >-
  Configure dbt profiles and CI/CD environment variables for Recce data validation.
  Set up isolated schemas for base vs current comparison on pull requests.
---

!!! tip "Following the onboarding guide?"
    Return to [Get Started with Recce Cloud](../getting-started/start-free-with-cloud.md#3-add-recce-to-cicd) after completing this page.

# Environment Setup

Configure your dbt profiles and CI/CD environment variables for Recce data validation.

## Goal

Set up isolated schemas for base vs current comparison. After completing this guide, your CI/CD workflows automatically create per-PR schemas and compare them against production.

## Prerequisites

- [x] **dbt project**: A working dbt project with `profiles.yml` configured
- [x] **CI/CD platform**: GitHub Actions, GitLab CI, or similar
- [x] **Warehouse access**: Credentials with permissions to create schemas dynamically

## Why separate schemas matter

Recce compares two sets of data to validate changes:

- **Base**: The production state (main branch)
- **Current**: The PR branch with your changes

For accurate validation, these must point to different schemas in your warehouse. Without separation, you would compare identical data and miss meaningful differences.

## How CI/CD works with Recce

Recce uses both continuous delivery (CD) and continuous integration (CI) to automate data validation:

- **CD (Continuous Delivery)**: Runs after merge to main. Updates baseline artifacts with latest production state.
- **CI (Continuous Integration)**: Runs on PR. Validates proposed changes against baseline.

**Set up CD first**, then CI. CD establishes your baseline (production artifacts), which CI uses for comparison.

## Configure profiles.yml

Your `profiles.yml` file defines how dbt connects to your warehouse. Add a `ci` target with a dynamic schema for PR isolation.

```yaml
jaffle_shop:
  target: dev
  outputs:
    dev:
      type: snowflake
      account: "{{ env_var('SNOWFLAKE_ACCOUNT') }}"
      user: "{{ env_var('SNOWFLAKE_USER') }}"
      password: "{{ env_var('SNOWFLAKE_PASSWORD') }}"
      database: analytics
      warehouse: COMPUTE_WH
      schema: dev
      threads: 4

    # CI environment with dynamic schema per PR
    ci:
      type: snowflake
      account: "{{ env_var('SNOWFLAKE_ACCOUNT') }}"
      user: "{{ env_var('SNOWFLAKE_USER') }}"
      password: "{{ env_var('SNOWFLAKE_PASSWORD') }}"
      database: analytics
      warehouse: COMPUTE_WH
      schema: "{{ env_var('SNOWFLAKE_SCHEMA') }}"
      threads: 4

    prod:
      type: snowflake
      account: "{{ env_var('SNOWFLAKE_ACCOUNT') }}"
      user: "{{ env_var('SNOWFLAKE_USER') }}"
      password: "{{ env_var('SNOWFLAKE_PASSWORD') }}"
      database: analytics
      warehouse: COMPUTE_WH
      schema: public
      threads: 4
```

After saving, your profile supports three targets: `dev` for local development, `ci` for PR validation, and `prod` for production.

Key points:

- The `ci` target uses `env_var('SNOWFLAKE_SCHEMA')` for dynamic schema assignment (other warehouses use their own variable name)
- The `prod` target uses a fixed schema (`public`) for consistency
- Adapt this pattern for other warehouses (BigQuery uses `dataset` instead of `schema`)

## Set CI/CD environment variables

Your CI/CD workflow sets the schema dynamically for each PR. The key configuration:

**GitHub Actions:**

```yaml
env:
  SNOWFLAKE_SCHEMA: "PR_${{ github.event.pull_request.number }}"
```

**GitLab CI:**

```yaml
variables:
  SNOWFLAKE_SCHEMA: "MR_${CI_MERGE_REQUEST_IID}"
```

This creates schemas like `PR_123`, `PR_456` for each PR automatically. When a PR opens, the workflow sets `SNOWFLAKE_SCHEMA` and dbt writes to that isolated schema.

For complete workflow examples, see [Setup CD](setup-cd.md) and [Setup CI](setup-ci.md).

## Recommended pattern: Schema-per-PR

Create an isolated schema for each PR. This is the recommended approach for teams.

| Base Schema | Current Schema | Example |
|-------------|----------------|---------|
| `public` (prod) | `pr_123` | PR #123 gets its own schema |

**Why this pattern:**

- Complete isolation between PRs
- Multiple PRs can run validation in parallel without conflicts
- Easy cleanup by dropping the schema when PR closes
- Clear audit trail of what data each PR produced

## Alternative patterns

### Using staging as base

Instead of comparing against production, compare against a staging environment with limited data.

| Base Schema | Current Schema | Use Case |
|-------------|----------------|----------|
| `staging` | `pr_123` | Teams wanting faster comparisons |

**Pros:**

- Faster diffs with limited data ranges
- Consistent source data between base and current
- Reduced warehouse costs

**Cons:**

- Staging may drift from production
- Issues caught in staging might not reflect production behavior
- Requires maintaining an additional environment

See [Environment Best Practices](environment-best-practices.md) for strategies on limiting data ranges.

### Shared development schema (not recommended)

Using a single `dev` schema for all development work.

| Base Schema | Current Schema | Use Case |
|-------------|----------------|----------|
| `public` (prod) | `dev` | Solo developers only |

**Why this is not recommended:**

- Multiple PRs overwrite each other's data
- Cannot run parallel validations
- Comparison results may include changes from other work
- Difficult to isolate issues to specific PRs

Only use this pattern for individual local development, not for CI/CD automation.

## Verification

After configuring your setup, verify that both base and current schemas are accessible.

### Check configuration locally

```shell
dbt debug --target ci
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

## Next steps

- [Get Started with Recce Cloud](../getting-started/start-free-with-cloud.md) - Complete onboarding guide
- [Environment Best Practices](environment-best-practices.md) - Strategies for source data and schema management
- [Setup CD](setup-cd.md) - CD workflow for GitHub Actions and GitLab CI
- [Setup CI](setup-ci.md) - CI workflow for GitHub Actions and GitLab CI
