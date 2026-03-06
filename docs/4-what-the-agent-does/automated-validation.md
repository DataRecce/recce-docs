---
title: Automated Validation
---

# Automated Validation

Manual data validation slows down every pull request. Developers must remember which checks to run, execute them correctly, and communicate results to reviewers. The Recce Agent automates this process, running the right validation checks based on what changed in your PR.

## How It Works

When a PR is opened or updated, the Recce Agent analyzes your changes and determines what needs validation.

### 1. PR Triggers the Agent

Your CI/CD pipeline runs `recce-cloud upload` when dbt metadata is updated. This triggers the agent to analyze the changes.

### 2. Agent Analyzes Changes

The agent reads dbt artifacts from both your base branch and PR branch. It identifies:

- Which models were modified
- What schema changes occurred
- Which downstream models are affected

### 3. Agent Runs Validation

Based on the analysis, the agent executes appropriate validation checks against your warehouse:

- **Schema diff** - Detects added, removed, or modified columns
- **Row count diff** - Compares record counts between branches
- **Profile diff** - Analyzes statistical changes in column values
- **Breaking change analysis** - Identifies changes that affect downstream models

### 4. Agent Posts Summary

The agent generates a data review summary and posts it directly to your PR. Reviewers see:

- What changed and why it matters
- Validation results with pass/fail status
- Recommended actions for review

## When to Use

- **Every PR that modifies dbt models** - The agent runs automatically for all data changes
- **Large-scale refactoring** - When many models change, automated validation catches issues you might miss
- **Critical path changes** - When modifying models that power dashboards or reports
- **Continuous integration** - As part of your CI pipeline to validate every change

## Triggering Validation

You can trigger the data review summary in three ways:

1. **Automatic trigger** - Runs when `recce-cloud upload` executes in CI
2. **Manual trigger from UI** - Click the Data Review button in a PR/MR session
3. **GitHub comment** - Comment `/recce` on your GitHub PR to generate a new summary

## Related

- [Impact Analysis](impact-analysis.md) - How the agent analyzes change scope
- [PR/MR Data Review Summary](../7-cicd/pr-mr-summary.md) - Understanding the summary output
- [Setup CI](../7-cicd/setup-ci.md) - Configure automated validation
