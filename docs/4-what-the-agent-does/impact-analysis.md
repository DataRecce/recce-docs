---
title: Impact Analysis
description: >-
  Understand how the Recce Agent maps the full downstream impact of your dbt
  model changes using data lineage and column-level analysis.
---

# Impact Analysis

A single column change can break dashboards, reports, and downstream models you never intended to affect. Impact analysis maps the full scope of your changes before they reach production, helping you understand exactly what will be affected.

## How It Works

The Recce Agent analyzes your changes at multiple levels to determine their true impact.

### Lineage Analysis

The agent traces dependencies through your dbt project to identify all models affected by your changes. It builds a graph of:

- **Direct dependencies** - Models that reference your modified model
- **Transitive dependencies** - Models further downstream in the lineage
- **Column-level dependencies** - Specific columns that reference modified columns

### Schema Comparison

The agent compares schemas between your base and PR branches to detect:

- Added columns
- Removed columns
- Renamed columns
- Data type changes

### Change Classification

The agent categorizes each change based on its downstream impact:

| Type | Description | Example |
|------|-------------|---------|
| **Breaking** | Affects all downstream models | Adding a filter condition, changing GROUP BY |
| **Partial breaking** | Affects only models that reference specific modified columns | Removing or renaming a column |
| **Non-breaking** | Does not affect downstream models | Adding a new column, formatting changes |

### Downstream Effects

For each modified model, the agent identifies:

- Which downstream models are affected
- Which specific columns in those models are impacted
- Whether the impact is direct or indirect

## When to Use

- **Before merging any PR** - Understand the full scope of your changes
- **During development** - Validate that changes are isolated to intended models
- **Code review** - Help reviewers understand what will be affected
- **Breaking change assessment** - Determine if coordination with downstream consumers is needed

## Example: Column Change Impact

When you modify a column like `stg_orders.status`:

1. The agent identifies that `orders` model selects this column directly (partial impact)
2. The agent detects that `customers` model uses `status` in a WHERE clause (full impact)
3. The agent traces that `customer_segments` depends on `customers` (indirect impact)

This lets you know that your seemingly simple column change affects models you may not have considered.

## Next Steps

- [Impact Radius](../4-downstream-impacts/impact-radius.md) - Visualize affected models
- [Breaking Change Analysis](../4-downstream-impacts/breaking-change-analysis.md) - Understand change types
- [Lineage Diff](../3-visualized-change/lineage.md) - See lineage changes
- [Column-Level Lineage](../3-visualized-change/column-level-lineage.md) - Trace column dependencies
