---
title: Setup CI for GitLab
---

# Setup CI

Automatically validate your data changes in every merge request using Recce Cloud. Catch data issues before they reach production, with validation results right in your MR.

## Purpose

**Automated MR Validation** prevents data regressions before merge.

- **Triggers**: MR opened/updated against main
- **Action**: Auto-update Recce session for MR validation
- **Benefit**: Automated data validation and comparison

## Prerequisites

You need `manifest.json` and `catalog.json` files (dbt artifacts) for Recce Cloud. See [Start Free with Cloud](../../2-getting-started/start-free-with-cloud.md) for instructions on preparing these files.

## Implementation

### 1. Core Workflow

Add to your `.gitlab-ci.yml`:
```yaml
include:
  - component: gitlab.com/recce/recce-cloud-cicd-component/recce-cloud@1.2.0
    inputs:
      stage: test

stages:
  - build
  - test

variables:
  DBT_TARGET: "ci"

dbt-build:
  stage: build
  image: python:3.11-slim
  script:
    - pip install -r requirements.txt

    # Install dbt packages
    - dbt deps

    # Optional: Build tables to ensure they're materialized
    # - dbt build --target $DBT_TARGET

    # Required: Generate artifacts for comparison
    - dbt docs generate --target $DBT_TARGET
  artifacts:
    paths:
      - target/
    expire_in: 1 week
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
```

The included Recce Cloud component automatically:

- Creates a session in Recce Cloud for the merge request
- Uploads your dbt artifacts (`manifest.json` and `catalog.json`)
- Provides session URL for validation review

### 2. Component Configuration Options

The component accepts optional inputs for customization:
```yaml
include:
  - component: gitlab.com/recce/recce-cloud-cicd-component/recce-cloud@1.2.0
    inputs:
      stage: test                        # Pipeline stage (default: test)
      dbt_target_path: target            # Path to dbt artifacts (default: target)
      base_branch: main                  # Base branch for comparison (default: main)
      gitlab_token: $CUSTOM_GITLAB_TOKEN # Custom GitLab token (default: $CI_JOB_TOKEN)
```

**Default Configuration** (shown in example above):

- Component uses `$CI_JOB_TOKEN` automatically (no manual token setup required)
- Uploads from `target/` directory by default
- Compares against `main` branch

**Custom Token** (optional):

If you need to use a custom GitLab token instead of the default `$CI_JOB_TOKEN`:

1. Create a [Project Access Token](../gitlab-pat-guide.md) with `api` scope
2. Add it as a [CI/CD variable](https://docs.gitlab.com/ee/ci/variables/) in your project
3. Reference it in the component inputs:
```yaml
include:
  - component: gitlab.com/recce/recce-cloud-cicd-component/recce-cloud@1.2.0
    inputs:
      gitlab_token: $CUSTOM_GITLAB_TOKEN
```

### 3. Artifact Preparation Options

**Default: Fresh Build** (shown in example above)

- `dbt docs generate` is required and provides all needed artifacts
- `dbt build` is optional but ensures tables are materialized and updated

**Alternative Methods:**

- **External Download**: Download from dbt Cloud, Paradime, or other platforms
- **Pipeline Integration**: Use existing dbt build workflows

### 4. Verification

#### Test with an MR

1. Create a test MR with small data changes
2. Check **CI/CD → Pipelines** for workflow execution
3. Verify validation runs successfully

#### Verify Success

- ✅ **Pipeline completes** without errors in CI/CD → Pipelines
- ✅ **MR session updated** in Recce Cloud
- ✅ **Session URL** appears in pipeline job output

![Recce Cloud showing MR validation session](../../assets/images/7-cicd/verify-setup-ci.png){: .shadow}

#### Review MR Session

To analyze the MR changes in detail:

- Go to your [Recce Cloud](https://cloud.reccehq.com)
- Find the MR session that was created
- Launch Recce instance to explore data differences

Or use the session launch URL from the pipeline output:
```bash
# Pipeline output example
RECCE_SESSION_LAUNCH_URL: https://cloud.reccehq.com/launch/abc123
```

## Troubleshooting

### Missing dbt files

**Error**: `Missing manifest.json` or `Missing catalog.json`

**Solution**: Ensure `dbt docs generate` runs successfully before the Recce component:
```yaml
dbt-build:
  script:
    - dbt build
    - dbt docs generate # Required
  artifacts:
    paths:
      - target/
```

### Authentication issues

**Error**: `Failed to create session: 401 Unauthorized`

**Solutions**:

1. Verify Recce Cloud GitLab integration is set up for your project
2. Check that your project is connected in [Recce Cloud settings](https://cloud.reccehq.com/settings)
3. For custom tokens, ensure the token has `api` scope ([setup guide](../gitlab-pat-guide.md))

### Upload failures

**Error**: `Failed to upload manifest/catalog`

**Solutions**:

1. Check network connectivity to Recce Cloud
2. Verify artifact files exist in `target/` directory
3. Review pipeline job logs for detailed error messages
4. Ensure artifacts are passed between jobs:
```yaml
dbt-build:
  artifacts:
    paths:
      - target/ # Must include dbt artifacts
```

## Complete Example

Here's a full working example combining dbt build and Recce validation:
```yaml
include:
  - component: gitlab.com/recce/recce-cloud-cicd-component/recce-cloud@1.2.0
    inputs:
      stage: test

stages:
  - build
  - test

variables:
  DBT_TARGET: "ci"

dbt-build:
  stage: build
  image: python:3.11-slim
  before_script:
    - pip install -r requirements.txt
  script:
    - dbt deps
    - dbt build --target $DBT_TARGET
    - dbt docs generate --target $DBT_TARGET
  artifacts:
    paths:
      - target/
    expire_in: 1 week
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
```

See the [complete example project](https://gitlab.com/recce/jaffle-shop-snowflake/-/blob/main/.gitlab-ci.yml) for a full working configuration.
