---
title: Start free with Cloud
---

# Start Free with Recce Cloud

**Get started in 3 simple steps**. After signing up, you'll be guided through connecting your GitHub repository and automating your PR validation workflow.

👉 **[Start Free →](https://cloud.reccehq.com){target="\_blank"}**

## Step 1: Connect Your GitHub Repository {#github-integration}

After signing up, you'll enter your default project. The first step is connecting your GitHub organization and repository to enable PR tracking and validation.

### What You'll Get

Once connected, you can:

- View all open and draft PRs in your Recce dashboard
- See limited PR summaries showing model changes
- Track which PRs need validation

### Setup Requirements

- GitHub repository with dbt project
- Repository admin access for initial setup
- Active PRs with model changes

!!!Note
You'll need administrative access to the GitHub organization you want to connect. Please ensure you have the necessary permissions for **GitHub App installations**.

### Connection Steps

Follow the guidance to connect your GitHub organization and link your repository:

![Connect GitHub](../assets/images/2-getting-started/connect_github.png)

![Link Repository](../assets/images/2-getting-started/link_repository.png)

Once connected, your PRs will appear in the dashboard with basic change summaries:

![Connected Projects](../assets/images/2-getting-started/connected_projects.png)

## Step 2: Automate Metadata with CI/CD {#cicd-automation}

To unlock full-featured PR summaries and easy validation with Recce, configure CI/CD automation to automatically prepare metadata for every PR.

### What You'll Get

With CI/CD configured, you get:

- **Full-featured PR summaries** with comprehensive model impact analysis
- **One-click "Launch Recce"** to validate changes interactively
- Automatic metadata upload on every PR
- Consistent validation across all PRs
- Integrated PR status checks
- Validation results directly in PR comments

### Setup Requirements

- GitHub integration completed (Step 1)
- CI/CD platform access (GitHub Actions, GitLab CI, etc.)
- Team plan subscription or free trial

!!!Note
Available with Team plan (free trial included).

### How It Works

The CI/CD integration automates the metadata preparation process:

1. **On PR creation/update**: CI workflow generates dbt artifacts (`manifest.json`, `catalog.json`)
2. **Automatic upload**: Metadata is uploaded to Recce Cloud for both base and current environments
3. **Ready to validate**: PR appears in your dashboard with full summary and "Launch Recce" button

### Setup Guides

Follow the detailed setup guides for your CI/CD platform:

- [Setup CD](/7-cicd/setup-cd/) - Configure continuous deployment for base environment metadata
- [Setup CI](/7-cicd/setup-ci/) - Configure CI pipeline for PR environment metadata

<!-- insert a video -->

## Advanced Features

### Data Warehouse Diffing {#data-diffing}

Go beyond metadata to see how changes affect your actual data. Configure your data warehouse connection to compare query results and catch issues before they impact production.

#### Why Use Data Diffing?

While metadata comparison shows structural changes, data diffing reveals:

- Unexpected changes in row counts or data distributions
- Breaking changes in downstream transformations
- Data quality issues before production deployment

#### Setup Requirements

- Data warehouse credentials with read access
- Network connectivity to your warehouse
- CI/CD automation configured (Step 2 recommended)

#### Supported Warehouses

- Snowflake
- Databricks
- Others coming in future releases

#### Configure Warehouse Connection

**Connection setup:**

1. Navigate to [organization settings](https://cloud.reccehq.com/settings#organization){target="\_blank"}
2. Click "Add Connection" and enter your warehouse credentials
3. Go to your [project home](https://cloud.reccehq.com/) and click the gear icon
4. Link the newly added connection to your project

Your connection credentials are secure. See our [security practices](https://reccehq.com/security/){target="\_blank"} for details.

For detailed connection settings, see [Connect to Warehouse](../5-data-diffing/connect-to-warehouse.md).

<!-- insert a video -->

#### Available Diffing Methods

Recce supports multiple data diffing approaches:

- [Row Count Diff](/5-data-diffing/row-count-diff) - Compare total row counts
- [Profile Diff](/5-data-diffing/profile-diff/) - Statistical profiling of columns
- [Value Diff](/5-data-diffing/value-diff/) - Detailed value-level comparison
- [Top-K Diff](/5-data-diffing/topK-diff/) - Compare top values and frequencies
- [Histogram Diff](/5-data-diffing/histogram-diff/) - Distribution analysis
- [Query](/5-data-diffing/query/) - Custom SQL queries for validation
