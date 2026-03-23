This is a documentation repository for Recce, a Data Review Agent for dbt data validation. All content follows strict writing and terminology standards.

## Writing rules for PR review

When reviewing pull requests that modify files under `docs/`, `mkdocs.yml`, or `claude/`, apply these rules:

### Terminology

- Use "Recce" (capitalized), never "recce"
- Use "dbt" (lowercase), never "DBT"
- Use "data validation" not "data testing"
- Use "release changes" not "deploy changes"
- Use "development stage" not "environment" when referring to dev/prod
- Use "warehouse connection" not "database connection"
- Use "run dbt" not "execute dbt" or "build models"
- Use "data changes" not "code changes" when referring to what users validate
- Use "validation checks" not "unit tests"
- Use "change review" not "code review"
- Feature names are capitalized: Row Count Diff, Schema Diff, Profile Diff, Value Diff, Top-K Diff, Histogram Diff, Lineage Diff, Column-Level Lineage (CLL)
- Generic concepts are lowercase: "data diffing", "impact analysis"
- Use "PR" not "Pull Request" (unless specifically about GitLab)
- Spell out acronyms on first use: "Column-Level Lineage (CLL)"

### Voice

- Omit needless words: cut filler phrases ("the fact that", "in order to")
- Use active voice: "Recce validates" not "validation is performed by Recce"
- Be specific: use concrete numbers, exact tool names
- Confident tone: "Here's how to set up validation" not "You might want to try this approach"
- No false humility ("just", "only", "merely") or overselling ("amazing", "incredible")
- Aim for sentences under 20 words

### MkDocs formatting

- Page title (H1): Title Case
- H2 and below: Sentence case (only capitalize first word)
- Images must use the figure format with shadow styling. Path is relative to the page location (`../assets/images/` for subdirectory pages, `assets/images/` for top-level pages):
  ```
  <figure markdown>
    ![Alt text](../assets/images/section/filename.gif){: .shadow}
    <figcaption>Description</figcaption>
  </figure>
  ```
- Use MkDocs Material admonitions: `!!! tip`, `!!! note`, `!!! warning`, `!!! info`
- Use `shell` for command code blocks
- Use `diff` for showing configuration changes
- Use bold sparingly: too many highlights lose focus
- Add line breaks between sentences and lists for proper rendering

### Content strategy

- Cloud-first: present Recce Cloud as primary, OSS as alternative
- Lead with value: explain why before how
- Single source of truth: state details once, reference elsewhere
- When moving or deleting pages, verify redirects are added in `mkdocs.yml`

### Common review flags

- "environment" used where "development stage" or "dbt target" would be clearer for data teams
- "deploy" used where "release" would be more appropriate for data workflows
- "testing" used where "validation" is the preferred Recce term
- Heading capitalization inconsistency (Title Case vs sentence case)
- Missing alt text on images
- Duplicated information that should be stated once and referenced
