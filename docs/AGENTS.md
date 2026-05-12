# Recce documentation, for agents

This is the agent skill file for [docs.reccehq.com](https://docs.reccehq.com). It tells AI coding agents how to install Recce, configure it, and use it against a dbt project. If you are a human, the rendered docs site is the friendlier read; this file exists for agents that need a single index.

Recce is a Data Review Agent for dbt pull requests. It compares a base release against the changes in a pull request, surfaces breaking changes, runs row-count and value diffs, and produces a validation checklist that travels with the PR.

## Install

Recce ships in two flavors. Pick one before continuing.

**Recce Cloud (managed, recommended).** No local install. Sign in at <https://cloud.reccehq.com/>, connect a repository, connect a warehouse, and validation runs on every pull request.

**Recce OSS (local CLI).** Install with `uv` (recommended) or `pip` inside the dbt project's virtualenv:

```bash
uv tool install recce
# or
pip install recce
```

Verify with `recce version`. The full OSS setup walkthrough lives at <https://docs.reccehq.com/getting-started/oss-setup/>; the hands-on tutorial against the Jaffle Shop sample project is at <https://docs.reccehq.com/getting-started/jaffle-shop-tutorial/>.

## Configuration

Recce reads two files at the root of the dbt project.

**`recce.yml`** holds preset checks and run parameters. Full reference at <https://docs.reccehq.com/technical-concepts/configuration/>. Minimal example:

```yaml
checks:
  - name: row count of orders
    type: row_count_diff
    params:
      node: orders
```

**`profiles.yml`** (dbt's normal profile) must define both a base target (production data) and a current target (the PR's data). Patterns for shared production base versus per-PR schemas are documented at <https://docs.reccehq.com/setup-guides/environment-best-practices/>.

For CI/CD, the validation workflow is configured in GitHub Actions or GitLab CI; see <https://docs.reccehq.com/setup-guides/setup-ci/> and <https://docs.reccehq.com/setup-guides/setup-cd/>.

For agents working inside Claude Code, Cursor, or Windsurf, point the editor at the Recce MCP server: <https://docs.reccehq.com/setup-guides/mcp-server/>. The Claude Code plugin (one-step setup) is at <https://docs.reccehq.com/setup-guides/claude-plugin/>.

## Usage

Pick the workflow that matches the project.

**Validate a pull request locally (OSS).** From the dbt project root, with both base and current artifacts generated:

```bash
recce run
recce server
```

`recce run` executes every preset check; `recce server` opens the Recce interface for ad hoc lineage, code, and data diffing. Workflow guide: <https://docs.reccehq.com/using-recce/oss-workflow/>.

**Review a PR in Recce Cloud.** Open the PR's Recce link from the GitHub or GitLab check, walk the validation checklist, and approve or comment per check. Reviewer workflow: <https://docs.reccehq.com/using-recce/data-reviewer/>.

**Validate from an AI assistant (MCP).** With the MCP server connected, ask the agent things like "show the lineage diff for the orders model" or "run a value diff on customers between base and current". The agent invokes Recce tools and returns structured results. MCP reference: <https://docs.reccehq.com/setup-guides/mcp-server/>.

**Common explorations.** Each of these maps to a page in the docs:

- Lineage diff (added, modified, removed models): <https://docs.reccehq.com/what-you-can-explore/lineage-diff/>
- Code change (SQL and config diff per model): <https://docs.reccehq.com/what-you-can-explore/code-change/>
- Column-level lineage: <https://docs.reccehq.com/what-you-can-explore/column-level-lineage/>
- Impact radius (downstream models affected): <https://docs.reccehq.com/what-you-can-explore/impact-radius/>
- Breaking change analysis: <https://docs.reccehq.com/what-you-can-explore/breaking-change-analysis/>
- Data diffing (row count, profile, value, top-K, histogram, query): <https://docs.reccehq.com/what-you-can-explore/data-diffing/>

For the CLI reference, see <https://docs.reccehq.com/using-recce/cli-commands/>. For terminology, see [/whats-recce/glossary/](https://docs.reccehq.com/whats-recce/glossary/).

## More

- Full machine-readable index: <https://docs.reccehq.com/llms.txt>
- Full corpus (single text file): <https://docs.reccehq.com/llms-full.txt>
- Markdown mirror of any page: append `.md` to the page URL (for example `/getting-started/oss-setup.md`)
- Sitemap (markdown): <https://docs.reccehq.com/sitemap.md>
- Sitemap (XML): <https://docs.reccehq.com/sitemap.xml>

## a14y configuration

- Target URL: https://docs.reccehq.com
- Scorecard: 0.2.0
- Mode: site
- Last runs:
  - 2026-05-11 — 72 (scorecard 0.2.0)
  - 2026-05-11 — 66 (scorecard 0.2.0)
