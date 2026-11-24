---
title: Data Developer Workflow (OSS)
description: >-
  Validate dbt data changes locally with Recce OSS. Save state files, manage
  checklists, and share results with reviewers.
---

# Data Workflow in OSS

Validate data changes locally using Recce open source (OSS). This guide covers saving your work, managing checklists, and sharing results with reviewers.

**Goal:** Validate data changes locally and share evidence with PR reviewers.

## Prerequisites

- [x] Recce OSS installed
- [x] dbt project with base and current environments configured
- [x] Access to your data warehouse

## Development Workflow

### 1. Run Validation Checks

Start the Recce server and validate your changes:

```bash
recce server
```

Use [lineage diff](../what-you-can-explore/lineage-diff.md), schema diff, and [data diffs](../what-you-can-explore/data-diffing.md) to validate your changes. Add important checks to your [checklist](../collaboration/checklist.md) with descriptions explaining what reviewers should verify.

### 2. Iterate as You Develop

When you update your dbt models locally, Recce automatically detects changes to your `target/` artifacts. The lineage diff updates to reflect your latest changes, so you can keep validating as you develop.

1. Make changes to your dbt models
2. Run `dbt build` or `dbt run` to update artifacts
3. Recce refreshes automatically—check the updated lineage and re-run validations

### 3. Save Your State

Switching branches is often unavoidable during development. Save your current state for future use:

1. Click **Export** in the Recce UI
2. Save the [state file](../technical-concepts/state-file.md) (e.g., `recce_issue_123.json`)

To resume later, start Recce with the state file:

```bash
recce server recce_issue_123.json
```

![Save state file](../assets/images/using-recce/state-file-save.png){: .shadow}

### 4. Import Checklist

Reuse checks from previous sessions:

1. Go to the **Checklist** page
2. Click the **Import** icon
3. Select a state file to import checks from

This preserves your favorite checks across branches.

### 5. Share with Reviewers

When ready for PR review, share your validation results.

**As the submitter:**

1. Export your state file
2. Attach the state file to your PR comment
3. Use **Copy to Clipboard** to paste screenshots in PR comments

**As the reviewer:**

1. Download the state file from the PR
2. Run Recce in review mode:

```bash
recce server --review <state_file>
```

The `--review` option uses artifacts from the state file to connect to both base and PR environments.

!!! note "Required files"
    You still need `profiles.yml` and `dbt_project.yml` so Recce knows which credentials to use for the data warehouse connection.

## Validation Techniques

See [Data Diffing](../what-you-can-explore/data-diffing.md) for available validation methods:

- **Schema diff** - Column additions, removals, type changes
- **Row count diff** - Record count comparison
- **Value diff** - Column-level match percentage
- **Profile diff** - Statistical comparison
- **Query diff** - Custom SQL validation

## Verification

Confirm your workflow works:

1. Make a model change and run `dbt build && dbt docs generate`
2. Start Recce: `recce server`
3. Add a validation check to your checklist
4. Export the state file
5. Start a new Recce session and import the checklist
6. Verify checks imported correctly

## Next Steps

- [Share](../collaboration/share.md) - More sharing options including Cloud upload
- [Checklist](../collaboration/checklist.md) - Managing validation checks
- [State File](../technical-concepts/state-file.md) - State file reference
