# Cleanup TODO

Tracks follow-up cleanup tasks for documentation migrations. Remove entries once verified post-deploy.

## DRC-3554 — Change Classification page rename (2026-06-09)

<!-- legacy-feature-name --> Formerly the "Breaking Change Analysis" page/feature.

Terminology sweep + page rename. See `claude/URL_CHANGES_TRACKING.md` for the full URL/redirect record.

- [x] Rename `docs/what-you-can-explore/breaking-change-analysis.md` → `change-classification.md` (`git mv`)
- [x] Add 301 redirect `/what-you-can-explore/breaking-change-analysis/` → `/what-you-can-explore/change-classification/` in `mkdocs.yml`
- [x] Update nav label to "Change Classification"
- [x] Sweep doc bodies to new vocabulary (model-wide change / column change / additive change)
- [x] Update AI-guidance: `claude/terminology.md`, `claude/KNOWLEDGE_BASE.md`, `claude/URL_CHANGES_TRACKING.md`
- [ ] **After deploy:** verify the 301 redirect resolves on docs.reccehq.com (old URL → new URL)
- [ ] **After deploy:** confirm `llms-full.txt` and `sitemap.md` regenerated with the new slug (build artifacts in `site/`)
- [ ] Update the "Universal Terms" Notion page (AC#7) — owned by the commander, tracked separately
- [ ] Audit external inbound links (blog, landing, third-party) for the old slug; the redirect covers them but high-traffic links should be updated at source
