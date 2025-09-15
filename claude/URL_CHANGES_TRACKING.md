# URL Changes Tracking for Guides Restructure

This document tracks all URL changes that will occur when the new "Guides (New)" structure replaces the current "Guides" structure.

## Current URL Structure (Before Restructure)

### Overview Section
- `/overview/` → `index.md`
- `/demo/` → `demo.md`

### Getting Started Section
- `/getting-started/` → `get-started.md`
- `/configure-diff/` → `configure-diff.md`
- `/get-started-jaffle-shop/` → `get-started-jaffle-shop.md`
- `/start-with-dbt-cloud/` → `start-with-dbt-cloud.md`

### Web UI Section
- `/web-ui/` → `features/lineage.md`
- `/web-ui/` → `features/query.md`
- `/web-ui/` → `features/checklist.md`

### Command Line Interface Section
- `/command-line-interface/` → `features/recce-debug.md`
- `/command-line-interface/` → `features/recce-run.md`
- `/command-line-interface/` → `features/recce-summary.md`

### Advanced Features Section
- `/advanced-features/` → `features/state-file.md`
- `/advanced-features/` → `features/preset-checks.md`
- `/advanced-features/` → `features/node-selection.md`
- `/advanced-features/` → `features/impact-radius.md`
- `/advanced-features/` → `features/breaking-change-analysis.md`
- `/advanced-features/` → `features/column-level-lineage.md`
- `/advanced-features/` → `reference/configuration.md`

### Scenarios Section
- `/scenarios/` → `guides/scenario-dev.md`
- `/scenarios/` → `guides/scenario-pr-review.md`
- `/scenarios/` → `guides/scenario-ci.md`
- `/scenarios/` → `guides/best-practices-prep-env.md`

### Architecture Section
- `/architecture/` → `architecture/overview.md`
- `/changelog/` → External link to blog

### Privacy & Terms Section
- `/privacy-policy/` → External link
- `/cookie-policy/` → External link
- `/terms-of-use/` → External link
- `/accessibility-statement/` → External link

## New URL Structure (After Restructure)

**TODO: Update this section as you restructure the "Guides (New)" tab**

### [New Section Name]
- `[new-url]/` → `[file-path]`

## Redirect Mapping (To Be Implemented)

**TODO: Fill in the redirect mappings once the new structure is finalized**

```yaml
# Example redirect structure for mkdocs-redirects plugin
redirect_maps:
  # Old URL: New URL
  "/old-path/": "/new-path/"
  "/another-old-path/": "/another-new-path/"
```

## Notes

- All external links (Privacy Policy, Terms, etc.) will remain unchanged
- The Changelog link will remain unchanged
- Only internal documentation structure will change
- This tracking document should be updated as you make changes to the "Guides (New)" structure

## Implementation Steps

1. ✅ Create "Guides (New)" tab with current structure
2. 🔄 Restructure the "Guides (New)" tab (2 days of work)
3. ⏳ Document all URL changes in this file
4. ⏳ Test new structure thoroughly
5. ⏳ Replace original "Guides" with "Guides (New)"
6. ⏳ Implement redirects using mkdocs-redirects plugin
7. ⏳ Remove "Guides (New)" tab
8. ⏳ Deploy and verify redirects work correctly
