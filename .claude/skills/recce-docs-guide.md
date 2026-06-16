---
name: recce-docs-guide
description: >
  Use when writing, editing, or reviewing any documentation in this repo.
  Triggers on any work touching files under docs/, mkdocs.yml, or claude/.
  Handles MkDocs conventions, page structure, and formatting standards.
  Delegates voice, terminology, QA, and AISEO to the recce-team plugin.
---

# Recce Docs Guide

## Pre-flight: plugin check

Before any work, verify the `recce-team` plugin is available by checking if the `recce-team:writing-content` skill exists.

If the plugin is NOT installed, stop and show:

> The `recce-team` plugin is required for writing principles, terminology, QA, and AISEO reviews.
>
> Install it:
> ```
> claude plugin add https://github.com/DataRecce/recce-team
> ```
>
> Then retry your request.

Do not proceed without the plugin.

## Scope detection

Assess the scope of the documentation work to choose the right workflow:

**Lightweight path** — use when:
- Editing 1-2 existing pages
- No new pages created
- No navigation changes in `mkdocs.yml`

**Full path** — use when:
- Creating new pages
- Changing `mkdocs.yml` navigation
- Touching 3+ pages
- Restructuring or consolidating content

The user can override: request full workflow on a small edit, or lightweight on a large one.

## Lightweight path

1. Read local docs-specific context:
   - `claude/writing-principles.md` — ICP definitions, audience strategy, tone variants
   - `claude/terminology.md` — confusion risks, conflicting usage, clarification patterns
2. Invoke `recce-team:writing-content` for voice and formatting checks
3. Apply the MkDocs conventions below
4. Done — no QA/AISEO required

## Full path

1. Read local docs-specific context:
   - `claude/writing-principles.md` — ICP definitions, audience strategy, tone variants
   - `claude/terminology.md` — confusion risks, conflicting usage, clarification patterns
   - `claude/KNOWLEDGE_BASE.md` — site map / section index
2. Delegate to `recce-team:writing-content` which handles:
   - Planning (action types, doc types, source materials)
   - Structure approval
   - Drafting content under `docs/` in the appropriate section
   - QA review (`/recce-team:qa`)
   - AISEO review (`/recce-team:aiseo-review`)
3. Apply MkDocs conventions below on top of the drafted content
4. Handle nav updates and redirects in `mkdocs.yml`

## MkDocs conventions

### Page structure template

Every documentation page should follow this structure:

```markdown
---
title: [Descriptive Title]
---

# [H1 Title - Title Case, matches page title]

[Brief introduction — what this page covers and why it matters]

## [Value-first conceptual overview]
[Explain the concept, especially why and what value it provides, before implementation]

## [Step-by-step guide]
[Numbered steps with code examples or screenshots]

## [Common scenarios/use cases]
[Real-world applications and variations]

## [Troubleshooting] (if applicable)
[Common issues and solutions]

## [What's next]
[Links to related topics and logical next steps]
```

### Heading capitalization

- **Page title (H1):** Title Case — capitalize every word
- **H2 and below:** Sentence case — only capitalize the first word

### Image format

Use the standardized figure format with shadow styling. The image path is relative to the current page location:

For pages in subdirectories (e.g., `docs/setup-guides/connect-git.md`):

```markdown
<figure markdown>
  ![Alt text](../assets/images/section/filename.gif){: .shadow}
  <figcaption>Description of what the image shows</figcaption>
</figure>
```

For top-level pages (e.g., `docs/index.md`):

```markdown
<figure markdown>
  ![Alt text](assets/images/section/filename.gif){: .shadow}
  <figcaption>Description of what the image shows</figcaption>
</figure>
```

- Use consistent naming: `section-feature-description.png`
- Include meaningful alt text
- Keep screenshots current

### Admonitions

Use MkDocs Material admonition syntax:

```markdown
!!! tip
    Use for helpful suggestions and best practices

!!! note
    Use for important information and context

!!! warning
    Use for potential issues or important caveats

!!! info
    Use for additional context or background information
```

### Code blocks

- Use `shell` for commands
- Show expected output when helpful
- Use `diff` for configuration changes

```shell
pip install recce
recce server
```

```diff
  existing_line
- removed_line
+ added_line
```

### Bold usage

Use bold sparingly. Too many highlights lose focus and make content harder to read.

### Navigation updates

When adding or moving pages:
1. Update `mkdocs.yml` nav section
2. Add redirects under `plugins > redirects > redirect_maps` for moved/deleted pages:

```yaml
plugins:
  - redirects:
      redirect_maps:
        'old-path/file.md': 'new-path/file.md'
```

### File and path conventions

- Use `./` for relative paths: `./models/staging/stg_payments.sql`
- Highlight important files with code formatting: `profiles.yml`, `dbt_project.yml`
- Use consistent file extensions: `.sql`, `.yml`, `.md`
