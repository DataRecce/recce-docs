---
title: What the Agent Does
description: >-
  Learn how the Recce Agent automates dbt validation on pull requests, from
  impact analysis and data diffing to posting review summaries.
---

# What the Recce Agent Does

Data validation for pull requests is time-consuming. You need to understand what changed, identify downstream impacts, run the right checks, and communicate findings to reviewers. The agent automates this entire workflow.

## How It Works

The agent monitors your pull requests and acts as an automated data reviewer. When you open or update a PR that modifies dbt models, the agent:

1. **Analyzes your changes** - Reads dbt artifacts and compares your branch against the base branch
2. **Identifies impact** - Traces lineage to find all affected models and columns
3. **Runs validation checks** - Executes schema diffs, row count comparisons, and other relevant checks
4. **Generates insights** - Produces a data review summary with actionable findings
5. **Posts results** - Adds the summary directly to your PR for reviewers to see

This happens automatically in your CI/CD pipeline. No manual intervention required.

## When to Use

- **Every PR with data changes** - The agent runs automatically when dbt models are modified
- **Complex refactoring** - When changes affect many models, the agent maps the full impact radius
- **Critical model updates** - When validating changes to models that power dashboards or reports
- **Team collaboration** - When reviewers need context about data changes without running Recce locally

## Agent Capabilities

The agent provides three core capabilities:

### Automated Validation

The agent determines what needs validation based on your changes and runs appropriate checks automatically. It executes schema comparisons, row count diffs, and other validation queries against your warehouse.

[Learn more about Automated Validation](automated-validation.md)

### Impact Analysis

Before running checks, the agent analyzes your model changes to understand the scope of impact. It traces column-level lineage and categorizes changes as breaking, partial breaking, or non-breaking.

[Learn more about Impact Analysis](impact-analysis.md)

### Data Review Summary

After validation completes, the agent generates a comprehensive summary that explains what changed, what was validated, and whether the changes are safe to merge.

[Learn more about the Data Review Summary](../7-cicd/pr-mr-summary.md)

## Next Steps

- [Data Developer Workflow](../3-using-recce/data-developer.md) - How developers validate changes
- [Data Reviewer Workflow](../3-using-recce/data-reviewer.md) - How reviewers approve PRs
- [CI/CD Getting Started](../2-getting-started/environment-setup.md) - Set up automated validation
