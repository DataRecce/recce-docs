---
title: How Diff Works
icon: material/school
---

## Understand How Diff Works

The following steps provide a quick way to explore how Recce detects changes and why both artifacts and schemas are required for meaningful comparisons.

### 1. Start with identical artifacts

At first launch, Recce reads the latest dbt artifacts from the `target/` folder. All models will appear in gray since no differences are detected yet.
<!-- <insert the signel env screenshot>  -->

To simulate a comparison, create a baseline by copying the current artifacts:

```bash
cp -r target/ target-base/
```

Recce now reads from both `target/` and `target-base/`. Because these artifacts are identical, no differences appear in the lineage.

In most cases, artifacts in `target-base/` should come from the main branch or a stable baseline.

### 2. Modify a model to trigger lineage diff

With identical artifacts in place, make a change to a model, e.g., adding a `WHERE` clause to adjust row output. Recce would auto detect the updated artifacts in `target/`.

- Modified models will be highlighted in the lineage graph
- Downstream impacts would also reflect the change
  
<!-- <insert modified lineage>  -->

### 3. Run a Row Count Diff

Open the modified model and use the row count diff feature.

- Since both environments point to the same schema (e.g., `dev`), query results will be identical, no differences will appear
- In this setup, only metadata and lineage differences are surfaced

### 4. Configure another schema for data diff

Set up a second schema (e.g., production or staging) and ensure both schemas are available in your dbt profiles.

After configuring Recce to reference both schemas:

- The **Base** and **Current** environments will point to different schemas
- Running a row count diff now reveals data differences between environments

This setup enables full diffing, covering lineage, logic, metadata, and data output.

Recce requires two sets of artifacts and two schemas to perform a complete diff.

To complete the setup, see [Configure Diff](./configure-diff.md)