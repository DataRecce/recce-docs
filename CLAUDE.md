# Recce Documentation Site

Documentation for Recce, a Data Review Agent that automates data validation for dbt pull requests. Built with MkDocs Material theme.

## Tech Stack

- MkDocs + Material theme (Python)
- Node.js (Sass/Bootstrap)
- GitHub Actions (CI/CD)

## Commands

```shell
pip install -r requirements.txt  # Install Python deps
npm install                       # Install Node deps
mkdocs serve                      # Local dev server (localhost:8000)
mkdocs build                      # Build static site to /site
```

## Key Patterns

1. **Cloud-first**: Present Recce Cloud as primary, OSS as alternative
2. **Data-team language**: Use "validation" not "testing", "release" not "deploy", "development stage" not "environment"
3. **8-section structure**: What's Recce → Getting Started → Visualized Change → Downstream Impacts → Data Diffing → Collaboration → CI/CD → Technical Concepts

## File Structure

| Path | Purpose |
|------|---------|
| `docs/` | Markdown source files |
| `mkdocs.yml` | Site config and nav structure |
| `claude/` | Docs-specific writing principles, terminology, and site map |
| `.claude/skills/` | Local Claude Code skills (docs guide) |
| `docs/assets/images/` | Screenshots and diagrams |
| `site/` | Built output (git-ignored) |

## Plugin Dependency

Voice, formatting, QA, and AISEO reviews are provided by the `recce-team` plugin. Install it:

```
claude plugin add https://github.com/DataRecce/recce-team
```
