---
title: Breaking Change Analysis
---

**Breaking Change Analysis** examines modified models and categorizes changes into three types:

- Breaking changes
- Partial breaking changes
- Non-breaking changes

It's generally assumed that any modification to a model’s SQL will affect all downstream models. However, not all changes have the same level of impact. For example, formatting adjustments or the addition of a new column should not break downstream dependencies. Breaking change analysis helps you assess whether a change affects downstream models and, if so, to what extent.


## Usage
Use the [impact radius](./impact-radius.md#usage) view to analyze changed and see the impacted downstream.

## Categories of change
### Non-breaking change

No downstream models are affected. Common cases are adding new columns, comments, or formatting changes that don't alter logic.

**Example: Add new columns**
Adding a new column like status doesn't affect models that don't reference it.

```diff
select
    user_id,
    user_name,
++  status,
from
    {{ ref("orders") }}

```




### Partial breaking change

Only downstream models that reference specific columns are affected. Common cases are removing, renaming, or redefining a column.

**Example: Removing a column**

```diff
select
    user_id,
--  status,
    order_date,
from
    {{ ref("orders") }}
```

**Example: Renaming a column**

```diff
select
    user_id,
--  status
++  order_status
from
    {{ ref("orders") }}
```


**Example: Redefining a column**
```diff
select
    user_id,
--  discount
++  coalesce(discount, 0) as discount
from
    {{ ref("orders") }}
```


### Breaking change

All downstream models are affected. Common case are changes adding a filter condition or adding group by columns.

**Example: Adding a filter condition**
This may reduce the number of rows, affecting all downstream logic that depends on the original row set.

```diff
select
    user_id,
    order_date
from
    {{ ref("orders") }}
++ where status = 'completed'
```


**Example: Adding a GROUP BY column**
Changes the granularity of the result set, which can break all dependent models.

```diff
select
    user_id,
++  order_data,
    count(*) as total_orders
from
    {{ ref("orders") }}
-- group by user_id
++ group by user_id, order_date
```


## Limitations

Our breaking change analysis is intentionally conservative to prioritize safety. As a result, a modified model may be classified as a breaking change when it is actually non-breaking or partial breaking changes. Common cases include:

1. Logical equivalence in operations, such as changing `a + b` to `b + a`.
1. Adding a `LEFT JOIN` to a table and selecting columns from it. This is often used to enrich the current model with additional dimension table data without affecting existing downstream tables.
1. All modified python models or seeds are treated as breaking change.

## Technology

Breaking Change Analysis is powered by the SQL analysis and AST diff capabilities of [SQLGlot](https://github.com/tobymao/sqlglot) to  compare two SQL semantic trees.
