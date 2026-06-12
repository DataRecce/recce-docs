# Cleanup TODO

Tracks follow-up cleanup tasks for documentation migrations. Remove entries once verified post-deploy.

## DRC-3554 — Change Classification page rename (2026-06-09)

<!-- legacy-feature-name --> Formerly the "Breaking Change Analysis" page/feature.

Terminology sweep + page rename. See `claude/URL_CHANGES_TRACKING.md` for the full URL/redirect record.

- [x] Rename `docs/what-you-can-explore/breaking-change-analysis.md` → `change-classification.md` (`git mv`)
- [x] Add redirect `/what-you-can-explore/breaking-change-analysis/` → `/what-you-can-explore/change-classification/` in `mkdocs.yml` (mkdocs-redirects emits a client-side meta-refresh redirect, not an origin HTTP 301)
- [x] Update nav label to "Change Classification"
- [x] Sweep doc bodies to new vocabulary (model-wide change / column change / additive change)
- [x] Update AI-guidance: `claude/terminology.md`, `claude/KNOWLEDGE_BASE.md`, `claude/URL_CHANGES_TRACKING.md`
- [ ] **After deploy:** verify the redirect resolves on docs.reccehq.com (old URL → new URL) and record the actual HTTP response code (expect 200 + meta refresh unless the host adds a 301 rule)
- [ ] **After deploy:** confirm `llms-full.txt` and `sitemap.md` regenerated with the new slug (build artifacts in `site/`)
- [ ] Update the "Universal Terms" Notion page (AC#7) — owned by the commander, tracked separately
- [ ] Audit external inbound links (blog, landing, third-party) for the old slug; the redirect covers them but high-traffic links should be updated at source
