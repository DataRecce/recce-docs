---
title: Refresh Base
description: >-
  Recce Cloud's auto-snapshot freezes a per-PR snapshot baseline at upload time
  so PR comparisons stay clean. If the shared base drifts afterwards, a
  staleness banner lets you refresh the snapshot baseline in place.
---

# Refresh Base

Recce Cloud captures a snapshot of your production baseline when your PR is uploaded. Comparisons in that PR's session run against that frozen snapshot, so the diff stays focused on **only what this PR changed** — even when other PRs merge to `main` afterwards.

When production moves on, the PR session detects that its snapshot is behind, and a yellow banner offers a one-click **Refresh base** action.

## How Auto-Snapshot Keeps Diffs Clean

Without a frozen baseline, every comparison runs against whichever production state is live at the moment you open the UI. If `main` has merged ten times since CI ran, those merges leak into your PR diff as phantom changes — modified models you never touched, removed models that are simply newer in production.

Auto-Snapshot fixes this by copying the project's shared base into the PR session at upload time. The PR diff stays anchored to the production state that existed when the PR was first validated, so the only changes you see are the ones from your branch.

!!! info "Example: clean diff vs. phantom diff"
    Before Auto-Snapshot, a 1-model PR could surface as **2 modified + 13 removed** entries because production had drifted between CI and review. After Auto-Snapshot, the same PR surfaces as **1 modified, 0 removed** — matching what the developer actually changed.

## When the Staleness Banner Appears

The banner appears at the top of the session view (lineage, diff, or detail) when the project's shared base has been refreshed since this PR's snapshot was captured.

![Staleness banner at the top of a Recce Cloud session, prompting the reviewer to refresh the base](../assets/images/using-recce/staleness-banner-placeholder.png){: .shadow}

> **Production data has changed since this PR's base was captured. Comparisons may not reflect current state.** **\[Refresh base\]**

The banner signals a real risk to the comparison, so it is **not dismissible**. It clears automatically once you refresh, or once the snapshot matches the current shared base again.

First-time viewers see a one-shot popover that introduces the feature. After dismissing it, the banner alone communicates staleness.

## What Refresh Base Does

Clicking **Refresh base** re-clones the latest shared-base artifacts into this PR's session:

1. The button shows a spinner while the refresh runs.
2. Recce pulls the current shared-base `manifest.json`, `catalog.json`, and lineage cache into the session.
3. The lineage and diff views re-render against the new baseline within about 30 seconds.
4. A toast confirms the refresh:

    > Base refreshed. If you've saved checks in this session, you may want to re-run them against the new base.

5. The banner clears.

If the refresh fails, the banner stays visible and an error toast appears:

> Refresh failed — try again.

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
- The PR session was created after Auto-Snapshot was enabled in your Recce Cloud project. New PR sessions automatically capture a frozen snapshot at upload; older sessions created before the rollout continue to compare against the live shared base and won't show the staleness banner.

## Related Reading

- [Environment Best Practices](../setup-guides/environment-best-practices.md): How the shared base is built and kept current.
- [Data Reviewer Workflow](data-reviewer.md): The full review flow this banner appears in.
- [Data Developer Workflow](data-developer.md): How PR uploads pick up the snapshot in CI.
