---
title: Start with Recce Cloud
---

# Start with Recce Cloud

Validate data changes and collaborate with your team with automation.

👉 **[Start with Recce Cloud](https://cloud.reccehq.com){target="_blank"}**

Setup steps:

1. [Git Platform Integration](#git-integration)
2. [Data Warehouse Diffing](#data-diffing)
3. [CI/CD Automation](#cicd-automation)

Fall back to [manual](#manual) if you unable to finish the setup. 


## Prerequisites
1. Admin access for git platform
2. Data warehouse credentials with read access
3. 


## Git Platform Integration {#git-integration}

Connect your GitHub or GitLab repository to see all PRs/MRs in one place and validate changes before they hit
production.

### Setup Requirements

| GitHub                                                                                                                 | GitLab                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| • GitHub repository with dbt project<br>• Repository admin access for initial setup<br>• Active PRs with model changes | • GitLab project with dbt project<br>• Project maintainer or owner access for initial setup<br>• Active merge requests with model changes |

!!!Note
    You'll need administrative access to the Organization/Group you want to connect. Please ensure you have the necessary
    permissions for **App installations** (GitHub) or **Providing a Personal Access Token** (GitLab).

### Connection

Connect your repository to track pull requests/merge requests and validate changes.

!!!Note
    Keep **Connection setup** note the same as before if there was one specific to this section.

**Connection setup:**

| GitHub                                                                                                       | GitLab                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Navigate to settings<br>2. Connect GitHub repository<br>3. Authorize Recce access<br>4. Select repository | 1. Navigate to settings<br>2. Connect GitLab by providing a Personal Access Token ([see our directions here](../7-cicd/gitlab-pat-guide.md))<br>3. Connect a project by adding a GitLab Project or URL to a Recce Project |


### How to Use PR/MR Tracking

Once connected, Recce displays all open and draft PRs/MRs in your Recce Cloud project.

### PR/MR Validation Workflow

- View open/draft PRs/MRs in dashboard
- Select PR/MR to validate
- Upload PR/MR metadata (until CI/CD is configured)
- Launch Recce to analyze changes

## Data Warehouse Diffing {#data-diffing}

Do data diffing to see how changes affect your actual data. Configure your data warehouse connection to compare query
results and catch issues before they impact production.

### Setup Requirements

- Data warehouse credentials with read access
- Network connectivity to your warehouse

### Supported Warehouses

- Snowflake
- Databricks
- Others coming in future releases

### Warehouse Connection

Configure connection to your data warehouse to enable query result comparisons.

**Quick setup:**

1. In your [project home](https://cloud.reccehq.com/), click the gear icon next to **Warehouse Connection**
2. Create a new connection or select an existing one from the dropdown
3. Your connection is linked and ready to use

For detailed connection settings, see [Connect to Warehouse](../5-data-diffing/connect-to-warehouse.md). Connection
credentials are encrypted and secure, see our [security practices](https://reccehq.com/security/).


## CI/CD Automation {#cicd-automation}

Set up CI/CD to automatically upload metadata and run validation checks on every PR.

!!!Note
    Available with Team plan (free trial included).

### Setup Requirements

See the CI/CD sections for complete setup guides:

- [Getting Started with CI/CD](../7-cicd/ci-cd-getting-started.md)
- GitHub CI/CD
    - [Setup CI for GitHub](../7-cicd/github/setup-ci.md)
    - [Setup CD for GitHub](../7-cicd/github/setup-cd.md)
- GitLab CI/CD
    - [Setup CI for Gitlab](../7-cicd/gitlab/setup-ci.md)
    - [Setup CD for Gitlab](../7-cicd/gitlab/setup-cd.md)

### Automation Benefits

- Automatic metadata upload on every PR
- Consistent validation across all PRs
- Reduced manual setup steps
- Integrated PR status checks
- Validation results directly in PR


## Manual Upload Metadata  {#manual}

Recce shows what changed between base and current environments and helps assess potential impact. The most common case is comparing your development branch against your production or main branch to see what your changes will impact.

If you don’t use the GitHub/GitLab or havn’t setup CI/CD yet, you can manual upload

- Web interface: Click "Update" on the session you want to update in Recce Cloud.
  1. Click "Update" in base session to upload baseline metadata
  2. Click "Update" in current session to upload comparison metadata
  3. Click "Launch" to compare current against base
- CLI command:

```
recce upload-session --session-id <your_session_id>
```

Find your session ID in Recce Cloud web interface when clicking "Update" on any session.

### Required Files

Recce needs `manifest.json` and `catalog.json` from both **base** and **current** environments for comparison.

#### Base Metadata

Production environment is commonly used as the baseline, but any environment can serve as the base.

Choose one method:

**Method 1: Generate locally**

```
dbt docs generate --target-path target-base --target <your_prod_target>
```

**Method 2: dbt Cloud**<br>
Deploy → Jobs → Production job → Recent run → Download artifacts

**Method 3: dbt Docs server**<br>
Download the artifacts directly from dbt docs server:

- `<dbt_docs_url>/manifest.json`
- `<dbt_docs_url>/catalog.json`

#### Current Metadata

Use development environment or PR branch as current to compare against the base.

Choose one method:

**Method 1: Generate locally**

```
dbt docs generate --target <your_dev_target>
```

**Method 2: dbt Cloud**<br>
Deploy → Jobs → CI job → Recent run → Download artifacts


