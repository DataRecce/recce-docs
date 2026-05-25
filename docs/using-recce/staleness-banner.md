---
title: Refresh Base
description: >-
  Recce Cloud freezes a per-PR baseline at upload time so PR comparisons stay
  clean. If production moves on after that, a banner lets you refresh the
  baseline in place.
---

# Refresh Base

Recce Cloud captures a snapshot of your production baseline when your PR is uploaded. Comparisons in that PR's session run against that frozen snapshot, so the diff stays focused on **only what this PR changed** — even when other PRs merge to `main` afterwards.

When production moves on, the PR session detects that its snapshot is behind, and a yellow banner offers a one-click **Refresh base** action.

## Why a Frozen Snapshot

Without a frozen baseline, every comparison runs against whichever production state is live at the moment you open the UI. If `main` has merged ten times since CI ran, those merges leak into your PR diff as phantom changes — modified models you never touched, removed models that are simply newer in production.

Auto-Snapshot fixes this by copying the project's shared base into the PR session at upload time. The PR diff stays anchored to the production state that existed when the PR was first validated, so the only changes you see are the ones from your branch.

!!! info "Example: 205datalab acid test"
    A customer PR that touched **one** model used to display **2 modified + 13 removed** because production had drifted between CI and review. With Auto-Snapshot, the same PR now shows **1 modified, 0 removed** — matching what the developer actually changed.

## When the Staleness Banner Appears

The banner appears at the top of the session view (lineage, diff, or detail) when the project's shared base has been refreshed since this PR's snapshot was captured.

> **Production data has changed since this PR's base was captured. Comparisons may not reflect current state.** **\[Refresh base\]**

The banner is correctness-critical, so it is **not dismissible**. It clears automatically once you refresh, or once the snapshot matches the current shared base again.

First-time viewers see a one-shot popover that introduces the feature. After dismissing it, the banner alone communicates staleness.

## What Refresh Base Does

Clicking **Refresh base** re-clones the latest shared-base artifacts into this PR's session:

1. The button shows a spinner while the refresh runs.
2. Recce pulls the current shared-base `manifest.json`, `catalog.json`, and lineage cache into the session.
3. The lineage and diff views re-render against the new baseline within about 30 seconds.
4. A toast confirms: *"Base refreshed. If you've saved checks in this session, you may want to re-run them against the new base."*
5. The banner clears.

If the refresh fails, the banner stays visible and an error toast appears: *"Refresh failed — try again."*

!!! tip "Re-run saved checks after a refresh"
    Checks you added to the session before the refresh still reference the previous baseline. Re-run them so the recorded results reflect the new comparison.

## When to Refresh

| Situation | Recommended action |
|-----------|---------------------|
| Banner appears, you want the most current comparison | Click **Refresh base** |
| Banner appears, you only care about what this PR changed | Leave it; the frozen snapshot is already correct for this PR |
| You merged from `main` into the PR branch | Push and let CI re-upload; the new upload captures a fresh snapshot |
| You are reviewing a stale PR alongside a newer one | Refresh both sessions so they share the same baseline reference |

For most PR reviews, the frozen snapshot is the right default — it answers the question *"what does this PR change?"* without interference from unrelated merges. Refresh when you specifically want to validate the PR against the **current** production state, for example before merge.

## Requirements

- The project has a shared base configured (`recce-cloud upload --type prod` runs on `main`). Refresh is disabled when no shared base exists.
- The PR session was created after Auto-Snapshot was enabled in your Recce Cloud project. Older sessions continue to compare against the live shared base.

## Related Reading

- [Environment Best Practices](../setup-guides/environment-best-practices.md): How the shared base is built and kept current.
- [Data Reviewer Workflow](data-reviewer.md): The full review flow this banner appears in.
- [Data Developer Workflow](data-developer.md): How PR uploads pick up the snapshot in CI.
