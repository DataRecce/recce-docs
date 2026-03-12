---
title: Column-Level Lineage
---

Column-Level Lineage provides visibility into the upstream and downstream relationships of a column.

Common use-cases for column-level lineage are:

1. **Source Exploration**: During development, column-level lineage helps you understand how a column is derived.
2. **Impact Analysis**: When modifying the logic of a column, column-level lineage enables you to assess the potential impact across the entire DAG.
3. **Root Cause Analysis**: Column-level lineage helps identify the possible source of errors by tracing data lineage at the column level.

## Usage

1. Select a node in the lineage DAG, then click the column you want to view.

    ![alt text](../assets/images/what-you-can-explore/cll-1.png){: .shadow}

1. The column-level lineage for the selected column will be displayed.

    ![alt text](../assets/images/what-you-can-explore/cll-2.png){: .shadow}

1. To exit column-level lineage view, click the close button in the upper-left corner.

    ![alt text](../assets/images/what-you-can-explore/cll-3.png){: .shadow}

## Transformation Types

The transformation type is also displayed for each column, which will help you understand how the column was generated or modified.

| Type | Description  |
|------|--------------|
| Pass-through  |The column is directly selected from the upstream table. |
| Renamed | The column is selected from the upstream table but with a different name. |
| Derived | The column is created through transformations applied to upstream columns, such as calculations, conditions, functions, or aggregations. |
| Source | The column is not derived from any upstream data. It may originate from a seed/source node, literal value or data generation function. |
| Unknown | We have no information about the transformation type. This could be due to a parse error or other unknown reason. |

## When to Use

- Trace where a column's data originates
- Understand which downstream columns depend on a specific column
- Assess the impact of modifying a column's logic
- Debug data quality issues by following the transformation chain

## Related

- [Impact Radius](impact-radius.md) - See column-level impact on downstream models
- [Breaking Change Analysis](breaking-change-analysis.md) - Classify change severity
- [Data Diffing](data-diffing.md) - Validate column-level data changes


