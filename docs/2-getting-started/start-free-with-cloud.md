---
title: Start free with Cloud
---

# Start Free with Recce Cloud

**Launch Recce in under 2 minutes** to validate your data changes. We offer two paths to getting started.

👉 **[Start Free →](https://cloud.reccehq.com)**

## Understanding Recce Sessions

A session captures a snapshot of your dbt project, storing artifacts (`manifest.json` and `catalog.json`) that enable data comparison and validation.

### Session Types

- **Base Session**: Your production baseline - what you compare changes against
- **Dev Session**: For ad-hoc exploration and validation during development
- **PR Session**: Automated sessions created for pull requests

### How Sessions Work

Launch Recce from your current session (PR or Dev) against the base to:

- **Compare data** between your changes and the baseline
- **Validate changes** before merging to UAT/PROD
- **Track impact** on downstream models

Later, CI/CD automation ([Setup CI](../7-cicd/setup-ci.md) and [Setup CD](../7-cicd/setup-cd.md)) will manage sessions automatically - keeping base sessions current and creating PR sessions on every push.

## Step 1: Get Ready to Launch Recce

### Upload your artifacts

- **Best if**: You want to try without GitHub permissions
- **You get**: Launch Recce with your actual dbt project
- **Setup**: Upload your development and production artifacts locally
- **Immediate value**: See your real project lineage and metadata diffs
- ✨ **You'll know it's working when**: Your models appear in the lineage graph

<br>
If you don't have a dbt project, you can just click "Launch" to see the Jaffle Shop sample project loaded.

### Connect to view all your PRs

- **Best if**: You have a current PR and GitHub permissions
- **You get**: List all your PRs and validate any of them
- **Setup**: Connect GitHub (installs Recce app) and upload your PR snapshots
- **Immediate value**: See all opened PRs and do validation
- ✨ **You'll know it's working when**: Your PRs appear in the project

## Step 2: Launch Recce → See Metadata Diffing

**What you just unlocked**:

- ✅ **Lineage visualization** of your models
- ✅ **Metadata comparison** between changes and production
- ✅ **Change detection** automatically highlighted
- ✅ **Column-level impact analysis**

**You can now**: Explore which models changed and understand downstream impact

✨ **You'll know it's working when**: You see colored nodes showing changed models in the lineage view

## Step 3: Unlock Data Diffing → Real Data Validation

- **What you'll unlock**: Compare actual data between development and production
- **Setup needed**: Configure your data warehouse connection (1 action)
- **New value**:
    - ✅ **Value diff** - see row count changes
    - ✅ **Profile diff** - compare data distributions
    - ✅ **Schema diff** - spot structure changes
    - ✅ **Custom query comparisons** - run any SQL side-by-side

**You can now**: Validate that your data changes work correctly

✨ **You'll know it's working when**: You can run "Value Diff" and see actual row count comparisons

## Step 4: Automate Everything → CI/CD Integration

- **What you'll unlock**: Automatic session management for every PR
- **Setup needed**: [Set up automated workflows](../7-cicd/scenario-ci.md)
- **How it works**:
    - **Base sessions** auto-update when you merge to main ([Setup CD](../7-cicd/setup-cd.md))
    - **PR sessions** auto-create for validation on every push ([Setup CI](../7-cicd/setup-ci.md))
- **Ultimate value**:
    - ✅ **Automatic PR validation** - sessions created and updated on every push
    - ✅ **Team workflows** - standardized validation across team
    - ✅ **Current baselines** - your base sessions stay up-to-date automatically

## What's Next?

After launching Recce, explore:

- [View modified](../3-visualized-change/lineage.md)
- [View downstream impacts](../4-downstream-impacts/impact-radius.md)
- [Data diffing](../5-data-diffing/query.md)

**Questions?** [Join our Discord](../1-whats-recce/community-support.md) - we're here to help!
