---
title: Change Classification
---

**Change Classification** examines each modified model and categorizes the change into one of three types:

- Additive changes
- Column changes
- Model-wide changes

Without classification, you have to assume that any change to a model's SQL affects every downstream model. In practice, changes differ in impact: a formatting adjustment or a new column shouldn't disrupt downstream dependencies, while a new filter condition can change every downstream result. Change Classification tells you whether a change affects downstream models and, if so, to what extent.


## Usage
Use the [Impact Radius](./impact-radius.md#usage) view to analyze changed models and see their impacted downstream models.

## Categories of change
### Additive change

No downstream models are affected. Common cases include adding a new column, adding comments, or reformatting SQL without altering logic.

**Example: Adding a new column**

Adding a new column such as `status` doesn't affect downstream models that don't reference it.

```diff
select
    user_id,
    user_name,
++  status,
from
    {{ ref("orders") }}

```




### Column change

Only downstream models that reference the changed columns are affected. Common cases include removing, renaming, or redefining a column.

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


### Model-wide change

All downstream models are affected. Common cases include adding a filter condition or adding a `GROUP BY` column.

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

This changes the granularity of the result set, which affects every dependent model.

```diff
select
    user_id,
++  order_date,
    count(*) as total_orders
from
    {{ ref("orders") }}
-- group by user_id
++ group by user_id, order_date
```


## Limitations

Change Classification is intentionally conservative to prioritize safety. As a result, a modified model may be classified as a model-wide change when it is actually an additive or column change. Common cases include:

1. Logically equivalent rewrites, such as changing `a + b` to `b + a`.
1. Adding a `LEFT JOIN` and selecting columns from the joined table. This pattern is often used to enrich a model with dimension data without affecting existing downstream models.
1. Modified Python models and seeds, which are always treated as model-wide changes.

## When to Use

- Determine which downstream models need validation after a change
- Prioritize review effort based on impact severity
- Understand whether a refactor affects dependent models
- Assess risk before merging model changes

## Technology

Change Classification uses the SQL parsing and AST diff capabilities of [SQLGlot](https://github.com/tobymao/sqlglot) to compare the semantic trees of the base and current SQL.

## Related

- [Impact Radius](impact-radius.md) - Visualize affected downstream models
- [Column-Level Lineage](column-level-lineage.md) - Trace column dependencies
- [Code Change](code-change.md) - Review the actual SQL modifications
