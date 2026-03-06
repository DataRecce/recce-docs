# Post-Merge Cleanup Tasks

This document tracks files to delete after all documentation restructuring PRs (6-9) are merged into `docs-v3`.

## Important

- Do NOT delete these files until all PRs are merged
- The redirects plugin in `mkdocs.yml` handles URL redirections automatically
- Delete this file after cleanup is complete

## Files to Delete

### From PR 6 - Lineage and Data Diffing Consolidation

**Old Visualized Change section:**

- `docs/3-visualized-change/lineage.md` → Moved to `5-what-you-can-explore/lineage-diff.md`

**Old Downstream Impacts section:**

- `docs/4-downstream-impacts/impact-radius.md` → Moved to `5-what-you-can-explore/impact-radius.md`
- `docs/4-downstream-impacts/breaking-change-analysis.md` → Moved to `5-what-you-can-explore/breaking-change-analysis.md`
- `docs/4-downstream-impacts/metadata-first.md` → Deprecated (if exists)
- `docs/4-downstream-impacts/transformation-types.md` → Deprecated (if exists)

**Old Data Diffing section:**

- `docs/5-data-diffing/row-count-diff.md` → Consolidated into `5-what-you-can-explore/data-diffing.md`
- `docs/5-data-diffing/profile-diff.md` → Consolidated into `5-what-you-can-explore/data-diffing.md`
- `docs/5-data-diffing/value-diff.md` → Consolidated into `5-what-you-can-explore/data-diffing.md`
- `docs/5-data-diffing/topK-diff.md` → Consolidated into `5-what-you-can-explore/data-diffing.md`
- `docs/5-data-diffing/histogram-diff.md` → Consolidated into `5-what-you-can-explore/data-diffing.md`
- `docs/5-data-diffing/query.md` → Consolidated into `5-what-you-can-explore/data-diffing.md`

### From PR 7 - CI/CD Reorganization

- `docs/7-cicd/preset-checks.md` → Moved to `6-collaboration/preset-checks.md`

### From PR 8 - Reference Section

- `docs/8-technical-concepts/configuration.md` → Moved to `7-reference/configuration.md`
- `docs/8-technical-concepts/state-file.md` → Moved to `7-reference/state-file.md`

### From PR 9 - Community Section

- `docs/1-whats-recce/community-support.md` → Moved to `8-community/support.md`

## Empty Directories to Remove

After deleting files, remove these directories if empty:

- `docs/4-downstream-impacts/`
- `docs/5-data-diffing/`
- `docs/8-technical-concepts/`

## Cleanup Command

After all PRs are merged, run this to delete old files:

```bash
# Delete old files (run from repository root)
rm -f docs/3-visualized-change/lineage.md
rm -f docs/4-downstream-impacts/impact-radius.md
rm -f docs/4-downstream-impacts/breaking-change-analysis.md
rm -f docs/4-downstream-impacts/metadata-first.md
rm -f docs/4-downstream-impacts/transformation-types.md
rm -f docs/5-data-diffing/row-count-diff.md
rm -f docs/5-data-diffing/profile-diff.md
rm -f docs/5-data-diffing/value-diff.md
rm -f docs/5-data-diffing/topK-diff.md
rm -f docs/5-data-diffing/histogram-diff.md
rm -f docs/5-data-diffing/query.md
rm -f docs/7-cicd/preset-checks.md
rm -f docs/8-technical-concepts/configuration.md
rm -f docs/8-technical-concepts/state-file.md
rm -f docs/1-whats-recce/community-support.md

# Remove empty directories
rmdir docs/4-downstream-impacts/ 2>/dev/null || true
rmdir docs/5-data-diffing/ 2>/dev/null || true
rmdir docs/8-technical-concepts/ 2>/dev/null || true

# Remove this file
rm -f docs/CLEANUP-TODO.md
```
