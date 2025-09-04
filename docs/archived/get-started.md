---
title: Getting Started
icon: material/rocket-launch-outline
---

# Getting Started
This guide outlines how to launch Recce, whether evaluating it for the first time or expanding usage with Recce Cloud.

Recce supports data validation by:

- Explore what changed
- Validate downstream impacts
- Collaborate through shareable checklists

For a hands-on example, refer to the [5-Minute Tutorial](./get-started-jaffle-shop.md).

Currently, **Recce supports dbt projects**. For teams using other tools, [feature requests are welcomed](mailto:product@datarecce.io) and may be considered for the product roadmap.


## Install

From within a dbt project directory:
```shell
cd your-dbt-project/  # if you're not already there
pip install -U recce
```


## Launch
To start Recce in the current environment:
```shell
recce server
```
Launching Recce enables:

- **Lineage clarity**: Trace changes down to the column level

- **Query insights**: Explore logic and run custom queries

- **Live diffing**: Reload and inspect changes as you iterate

Best suited for quick exploration before moving to structured validation using Diff.

<!-- <insert the gif of sign in flow step 2>  -->

## Next: Diff

Tests may pass, but business logic or edge cases can still cause unexpected results. Comparing **before and after** helps confirm impact, validate intent, and catch issues early.

👉 See [Configure Diff](./configure-diff.md)

