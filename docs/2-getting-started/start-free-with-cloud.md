---
title: Start free with Cloud
---

# Start Free with Recce Cloud

**Launch Recce in under 2 minutes**. Each following feature provides additional value. The progressive features help you get more value from Recce over time.

👉 **[Start Free →](https://cloud.reccehq.com){target="_blank"}**

## Model Changes and Impact Analysis

Recce shows what changed between **base** and **current** environments and helps assess potential impact. The most common case is comparing your development branch against your production or main branch to see what your changes will impact. 

You can: 

- Explore with the pre-loaded Jaffle Shop data
- Upload your metadata (see below)
- **Skip manual upload go directly to [CI/CD automation](#cicd-automation)** 

<!-- insert a video -->

### Upload Metadata
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


## Data Warehouse Diffing {#data-diffing}

Go beyond metadata to see how changes affect your actual data. Configure your data warehouse connection to compare query results and catch issues before they impact production.

### Setup Requirements

- Data warehouse credentials with read access
- Network connectivity to your warehouse
- Base and current environments configured in previous step

### Supported Warehouses

- Snowflake
- Databricks
- Others coming in future releases

### Warehouse Connection

Configure connection to your data warehouse to enable query result comparisons. For detailed connection settings, see [Connect to Warehouse](../5-data-diffing/connect-to-warehouse.md).

**Connection setup:**

1. Navigate to your [project home](https://cloud.datarecce.io/)
2. Find the **Warehouse Connection** section and click the gear icon
3. Choose one of the following options:
   - **Create new connection**: Click "Create New Connection" to set up a new warehouse connection and link it to your project
   - **Select existing**: If your organization already has warehouse connections, select one from the dropdown and click "Save"
4. Your connection is now linked and ready to use

**Managing connections:**

To update or change your project's warehouse connection:

1. Click the gear icon next to **Warehouse Connection** in your project home
2. In the connection management dialog:
   - **Switch connection**: Select a different connection from the dropdown and click "Save"
   - **Create new**: Click "Create New Connection" to add and link a new warehouse connection
   - **Remove connection**: Select "No Connection" from the dropdown and click "Save"

**Quick tips:**

- New connections are automatically linked to your project when created from project home
- You can manage all organization warehouse connections from [settings](https://cloud.reccehq.com/settings#organization){target="_blank"}
- Connection credentials are encrypted and secure. See our [security practices](https://reccehq.com/security/){target="_blank"} for details

<!-- insert a video -->

### How to Use Data Diffing

Recce supports several data diffing methods. See Data Diffing sections for details:

- [Row Count Diff](/5-data-diffing/row-count-diff)
- [Profile Diff](/5-data-diffing/profile-diff/)
- [Value Diff](/5-data-diffing/value-diff/)
- [Top-K Diff](/5-data-diffing/topK-diff/)
- [Histogram Diff](/5-data-diffing/histogram-diff/)
- [Query](/5-data-diffing/query/)

## GitHub Integration {#github-integration}

Connect your GitHub repo to see all PRs in one place and validate changes before they hit production.

### Setup Requirements

- GitHub repository with dbt project
- Repository admin access for initial setup
- Active PRs with model changes

!!!Note
    You'll need administrative access to the GitHub organization you want to connect. Please ensure you have the necessary permissions for **GitHub App installations**.

### GitHub Connection

Connect your repository to track pull requests and validate changes.

**Connection setup:**

1. Navigate to settings
2. Connect GitHub repository
3. Authorize Recce access
4. Select repository

<!-- insert a video -->

### How to Use PR Tracking

Once connected, Recce displays all open and draft PRs in your dashboard.

### PR Validation Workflow

- View open/draft PRs in dashboard
- Select PR to validate
- Upload PR metadata (until CI/CD is configured)
- Launch Recce to analyze changes


## CI/CD Automation {#cicd-automation}

Set up CI/CD to automatically upload metadata and run validation checks on every PR. 

!!!Note
    Available with Team plan (free trial included).

### Setup Requirements
See the CI/CD sections for complete setup guides:

- [Setup CD](/7-cicd/setup-cd/)
- [Setup CI](/7-cicd/setup-ci/)

- GitHub integration configured
- Team plan subscription or free trial

### Automation Benefits

- Automatic metadata upload on every PR
- Consistent validation across all PRs
- Reduced manual setup steps
- Integrated PR status checks
- Validation results directly in PR




