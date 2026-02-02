# Knowledge Base

## Documentation Structure
8 numbered sections mirror user adoption flow: understand → get started → use features → collaborate → automate → technical details.
→ `mkdocs.yml` (nav section)

## Writing Standards
Cloud-first, data-team-friendly language. Avoid software engineering jargon. Use "validation" not "testing", "release" not "deploy".
→ `claude/writing-principles.md`

## Terminology
Preferred terms for Recce features and data team concepts. Includes confusion alert patterns.
→ `claude/terminology.md`

## Content Sections

### What's Recce (Section 1)
Value proposition and how the Data Review Agent automates PR validation.
→ `docs/1-whats-recce/`

### Getting Started (Section 2)
OSS vs Cloud comparison, installation, Jaffle Shop tutorial.
→ `docs/2-getting-started/`

### Visualized Change (Section 3)
Lineage diffs, code changes, column-level lineage, multi-model views.
→ `docs/3-visualized-change/`

### Downstream Impacts (Section 4)
Impact radius analysis and breaking change detection.
→ `docs/4-downstream-impacts/`

### Data Diffing (Section 5)
Row count, profile, value, top-K, histogram diffs, custom queries, warehouse connections.
→ `docs/5-data-diffing/`

### Collaboration (Section 6)
Team invitations, validation checklists, sharing findings.
→ `docs/6-collaboration/`

### CI/CD (Section 7)
GitHub/GitLab integration, PR summaries, preset checks, best practices.
→ `docs/7-cicd/`

### Technical Concepts (Section 8)
State files and configuration reference.
→ `docs/8-technical-concepts/`

## Site Configuration
MkDocs Material theme config, nav structure, plugins, extensions.
→ `mkdocs.yml`

## Styling
Custom CSS in `docs/styles/extra.css`, theme overrides in `docs/overrides/`.

## Images
Optimize PNGs with pngquant. Keep animated GIFs under 1MB.
→ `readme.md` (Images section)
