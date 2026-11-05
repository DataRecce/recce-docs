---
title: Configuration
description: >-
  Reference for the recce.yml configuration file. Define preset checks and
  parameters for automated dbt data validation.
---

# Configuration

This reference documents the `recce.yml` configuration file, which defines preset checks and their parameters for automated data validation.

## Overview

The config file for Recce is located in `recce.yml` in your dbt project root. Use this file to define preset checks that run automatically with `recce server` or `recce run`.

## File Location

| Path | Description |
|------|-------------|
| `recce.yml` | Main configuration file in dbt project root |

## Preset Checks

Preset checks define automated validations that execute when you run `recce server` or `recce run`. Each check specifies a type of comparison and its parameters.

### Check Structure

```yaml
# recce.yml
checks:
  - name: Query diff of customers
    description: |
        This is the demo preset check.

        Please run the query and paste the screenshot to the PR comment.
    type: query_diff
    params:
        sql_template: select * from {{ ref("customers") }}
    view_options:
        primary_keys:
        - customer_id
```

### Check Fields

| Field | Description | Type | Required |
|-------|-------------|------|----------|
| `name` | The title of the check | string | Yes |
| `description` | The description of the check | string | |
| `type` | The type of the check (see types below) | string | Yes |
| `params` | The parameters for running the check | object | Yes |
| `view_options` | The options for presenting the run result | object | |

## Check Types

### Row Count Diff

Compares row counts between base and current environments.

**Type:** `row_count_diff`

**Parameters:**

| Field | Description | Type | Required |
|-------|-------------|------|----------|
| `node_names` | List of node names | `string[]` | *1 |
| `node_ids` | List of node IDs | `string[]` | *1 |
| `select` | Node selection syntax. See [dbt docs](https://docs.getdbt.com/reference/node-selection/syntax) | `string` | |
| `exclude` | Node exclusion syntax. See [dbt docs](https://docs.getdbt.com/reference/node-selection/syntax) | `string` | |
| `packages` | Package filter | `string[]` | |
| `view_mode` | Quick filter for changed models | `all`, `changed_models` | |

**Notes:**

*1: If `node_ids` or `node_names` is specified, it will be used; otherwise, nodes will be selected using the criteria defined by `select`, `exclude`, `packages`, and `view_mode`.

**Examples:**

Using node selector:

```yaml
checks:
  - name: Row count for modified tables
    description: Check row counts for all modified table models
    type: row_count_diff
    params:
       select: state:modified,config.materialized:table
       exclude: tag:dev
```

Using node names:

```yaml
checks:
  - name: Row count for key models
    description: Check row counts for customers and orders
    type: row_count_diff
    params:
      node_names: ['customers', 'orders']
```

### Schema Diff

Compares schema structure between base and current environments.

**Type:** `schema_diff`

**Parameters:**

| Field | Description | Type | Required |
|-------|-------------|------|----------|
| `node_id` | The node ID or list of node IDs to check | `string[]` | *1 |
| `select` | Node selection syntax. See [dbt docs](https://docs.getdbt.com/reference/node-selection/syntax) | `string` | |
| `exclude` | Node exclusion syntax. See [dbt docs](https://docs.getdbt.com/reference/node-selection/syntax) | `string` | |
| `packages` | Package filter | `string[]` | |
| `view_mode` | Quick filter for changed models | `all`, `changed_models` | |

**Notes:**

*1: If `node_id` is specified, it will be used; otherwise, nodes will be selected using the criteria defined by `select`, `exclude`, `packages`, and `view_mode`.

**Examples:**

Using node selector:

```yaml
checks:
  - name: Schema diff for modified models
    description: Check schema changes for modified models and downstream
    type: schema_diff
    params:
       select: state:modified+
       exclude: tag:dev
```

Using node ID:

```yaml
checks:
  - name: Schema diff for customers
    description: Check schema for customers model
    type: schema_diff
    params:
      node_id: model.jaffle_shop.customers
```

### Lineage Diff

Compares lineage structure between base and current environments.

**Type:** `lineage_diff`

**Parameters:**

| Field | Description | Type | Required |
|-------|-------------|------|----------|
| `select` | Node selection syntax. See [dbt docs](https://docs.getdbt.com/reference/node-selection/syntax) | `string` | |
| `exclude` | Node exclusion syntax. See [dbt docs](https://docs.getdbt.com/reference/node-selection/syntax) | `string` | |
| `packages` | Package filter | `string[]` | |
| `view_mode` | Quick filter for changed models | `all`, `changed_models` | |

**Examples:**

```yaml
checks:
  - name: Lineage diff for modified models
    description: Check lineage changes for modified models and downstream
    type: lineage_diff
    params:
       select: state:modified+
       exclude: tag:dev
```

### Query

Executes a custom SQL query in the current environment.

**Type:** `query`

**Parameters:**

| Field | Description | Type | Required |
|-------|-------------|------|----------|
| `sql_template` | SQL statement using Jinja templating | `string` | Yes |

**Examples:**

```yaml
checks:
  - name: Customer count
    description: Get total customer count
    type: query
    params:
       sql_template: select count(*) from {{ ref("customers") }}
```

### Query Diff

Compares query results between base and current environments.

**Type:** `query_diff`

**Parameters:**

| Field | Description | Type | Required |
|-------|-------------|------|----------|
| `sql_template` | SQL statement using Jinja templating | `string` | Yes |
| `base_sql_template` | SQL statement for base environment (if different) | `string` | |
| `primary_keys` | Primary keys for record identification | `string[]` | *1 |

**Notes:**

*1: If `primary_keys` is specified, the query diff is performed in the warehouse. Otherwise, the query result (up to the first 2000 records) is returned, and the diff is executed on the client side.

**Examples:**

```yaml
checks:
  - name: Customer data diff
    description: Compare customer data between environments
    type: query_diff
    params:
      sql_template: select * from {{ ref("customers") }}
      primary_keys:
      - customer_id
```

### Value Diff

Compares values for a specific model between environments.

**Type:** `value_diff` or `value_diff_detail`

**Parameters:**

| Field | Description | Type | Required |
|-------|-------------|------|----------|
| `model` | The name of the model | `string` | Yes |
| `primary_key` | Primary key(s) for record identification | `string` or `string[]` | Yes |
| `columns` | List of columns to include in diff | `string[]` | |

**Examples:**

Value diff summary:

```yaml
checks:
  - name: Customer value diff
    description: Compare customer values
    type: value_diff
    params:
      model: customers
      primary_key: customer_id
```

Value diff with detailed rows:

```yaml
checks:
  - name: Customer value diff (detailed)
    description: Compare customer values with row details
    type: value_diff_detail
    params:
      model: customers
      primary_key: customer_id
```

### Profile Diff

Compares statistical profiles of a model between environments.

**Type:** `profile_diff`

**Parameters:**

| Field | Description | Type | Required |
|-------|-------------|------|----------|
| `model` | The name of the model | `string` | Yes |

**Examples:**

```yaml
checks:
  - name: Customer profile diff
    description: Compare statistical profile of customers
    type: profile_diff
    params:
      model: customers
```

### Histogram Diff

Compares histogram distributions for a column between environments.

**Type:** `histogram_diff`

**Parameters:**

| Field | Description | Type | Required |
|-------|-------------|------|----------|
| `model` | The name of the model | `string` | Yes |
| `column_name` | The name of the column | `string` | Yes |
| `column_type` | The type of the column | `string` | Yes |

**Examples:**

```yaml
checks:
  - name: CLV histogram diff
    description: Compare customer lifetime value distribution
    type: histogram_diff
    params:
      model: customers
      column_name: customer_lifetime_value
      column_type: BIGINT
```

### Top-K Diff

Compares top-K values for a column between environments.

**Type:** `top_k_diff`

**Parameters:**

| Field | Description | Type | Required |
|-------|-------------|------|----------|
| `model` | The name of the model | `string` | Yes |
| `column_name` | The name of the column | `string` | Yes |
| `k` | Number of top items to include | `number` | Default: 50 |

**Examples:**

```yaml
checks:
  - name: Top 50 customer values
    description: Compare top 50 customer lifetime values
    type: top_k_diff
    params:
      model: customers
      column_name: customer_lifetime_value
      k: 50
```

## Default Behavior

- Preset checks are loaded from `recce.yml` when Recce starts
- Checks execute automatically with `recce run`
- Results are stored in the state file
- View options control how results are displayed in the UI

## Related

- [Preset Checks Guide](../collaboration/preset-checks.md) - How to use preset checks in workflows
- [State File](./state-file.md) - Understanding the state file format
- [CLI Commands](../using-recce/cli-commands.md) - Command-line options for running checks
