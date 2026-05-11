---
title: Glossary
description: >-
  Definitions for the Recce, dbt, and data validation terms used throughout this
  documentation, written for data teams.
---

# Glossary

Quick definitions for the terms used across the Recce docs. Where a concept has its own page, the entry links there.

## Recce concepts

**Recce Cloud.** The managed version of Recce. Connects to a Git repository and warehouse, runs validation automatically on every pull request, and posts a summary to the PR. See [Cloud vs Open Source](cloud-vs-oss.md).

**Recce OSS.** The open source CLI you run locally against a dbt project. Same validation engine as Cloud, manual orchestration. See [OSS Setup](../getting-started/oss-setup.md).

**Recce interface.** The web UI Recce serves (locally via `recce server`, in the cloud via the Cloud app) for browsing lineage, code, and data diffs. Sometimes called "Recce" alone in conversational context.

**Data Review Agent.** What Recce is. An agent that performs validation on dbt data changes the way a code review agent reviews code: examines the diff, runs checks, summarizes findings.

**Validation.** Running checks that confirm a data change is correct and intended. Recce's primary verb. Use in place of "testing" when describing what Recce does.

**Validation check.** A single comparison between base and current data (a row count diff, a value diff, a query) that returns a result the reviewer can approve.

**Preset check.** A validation check defined in `recce.yml` so it runs automatically on every PR for the project. See [Preset Checks](../collaboration/preset-checks.md).

**Checklist.** The collection of validation checks saved against a PR. Travels with the PR as proof-of-correctness. See [Checklist](../collaboration/checklist.md).

**State file.** The on-disk file that holds the checklist, run history, and validation results for a Recce session. Format reference: [State File](../technical-concepts/state-file.md).

**Recce instance.** A running Recce server (local `recce server` or a Cloud session) that holds a single state file.

## Validation comparisons

**Base.** The reference side of the comparison. Usually the production warehouse, or whatever the team treats as the source of truth for the PR.

**Current.** The PR's side of the comparison. Usually a per-PR schema in the warehouse with the PR's models built into it.

**Lineage diff.** Visualization of which dbt models were added, modified, or removed between base and current. See [Lineage Diff](../what-you-can-explore/lineage-diff.md).

**Code change.** The SQL and config diff for a single modified model. See [Code Change](../what-you-can-explore/code-change.md).

**Column-level lineage.** A lineage view that traces relationships at the column level, not just the model level. See [Column-Level Lineage](../what-you-can-explore/column-level-lineage.md).

**Impact radius.** The set of downstream models and columns affected by a change. See [Impact Radius](../what-you-can-explore/impact-radius.md).

**Breaking change analysis.** Automated categorization of a modified model as breaking, non-breaking, or partial breaking. See [Breaking Change Analysis](../what-you-can-explore/breaking-change-analysis.md).

**Row count diff.** Compares the number of rows in a model between base and current. Fastest sanity check.

**Profile diff.** Column-level statistical comparison (min, max, distinct, null counts) between base and current.

**Value diff.** Row-by-row comparison of values for a primary-key join between base and current.

**Top-K diff.** Comparison of the most frequent values in a categorical column.

**Histogram diff.** Comparison of the distribution of a numeric column.

**Query diff.** A custom SQL query run against both base and current with results compared. The full data-diffing toolkit lives on the [Data Diffing](../what-you-can-explore/data-diffing.md) page.

## dbt and warehouse terms

**dbt.** The data transformation tool Recce wraps validation around. Always lowercased.

**dbt model.** A SQL transformation defined in a dbt project. The unit of change Recce validates.

**dbt target.** The named warehouse connection defined in `profiles.yml` (for example `dev` or `prod`). Recce uses two targets per PR: one for base, one for current.

**dbt artifacts.** The `manifest.json` and `catalog.json` files dbt produces. Recce reads them to understand the model graph and column types.

**Data warehouse.** Snowflake, BigQuery, Databricks, Redshift, or another analytical warehouse. Where Recce queries actually run.

**Warehouse connection.** Credentials and configuration that point Recce at a specific warehouse. Configured via dbt's `profiles.yml`.

**Development stage.** The phase of work a change is in (development, review, release). Use this in place of "environment" when "environment" might be misread as "warehouse".

**Release.** Making data changes live in the production warehouse. Use in place of "deploy" when talking about data changes (deploy is reserved for infrastructure).

## Workflow roles

**Data developer.** The author of a dbt PR. Runs Recce locally or watches Cloud-generated validation results. Reviewer workflow: [Data Developer](../using-recce/data-developer.md).

**Data reviewer.** The teammate who reviews the PR. Walks the Recce checklist, approves checks, leaves comments. Reviewer workflow: [Data Reviewer](../using-recce/data-reviewer.md).

**Admin.** The person who connects Recce Cloud to the repo and warehouse and manages organization access. Setup guide: [Admin Setup](../using-recce/admin-setup.md).

## Automation

**CI (continuous integration).** Recce's per-PR automation: runs preset checks when a PR opens or updates and posts the result. Setup: [Setup CI](../setup-guides/setup-ci.md).

**CD (continuous delivery).** Recce's post-merge automation: refreshes the base state after merges so the next PR has an up-to-date reference. Setup: [Setup CD](../setup-guides/setup-cd.md).

**MCP server.** Recce's Model Context Protocol server, used by AI coding agents (Claude Code, Cursor, Windsurf) to call Recce tools through natural language. Setup: [MCP Server](../setup-guides/mcp-server.md).
