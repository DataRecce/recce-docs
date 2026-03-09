---
title: Recce MCP Server — Data Validation for AI Agents
description: >-
  Connect the Recce MCP server to Claude Code, Cursor, or Windsurf to validate
  data changes through natural language. Supports Schema Diff, Row Count Diff,
  Value Diff, and more via the Model Context Protocol (MCP).
---

# Recce MCP Server

When data models change, downstream dashboards and reports can break without warning. The Recce MCP server lets your AI agent validate those changes before they reach production — directly from your editor, through natural language.

[MCP (Model Context Protocol)](https://modelcontextprotocol.io) is an open standard that lets AI assistants call external tools. Recce implements an MCP server so your AI agent can run data diffs against your warehouse on your behalf.

Unlike general-purpose database tools, Recce's MCP server is purpose-built for branch comparison. It reads dbt artifacts (`manifest.json`, `catalog.json`) to understand your model graph, so your AI agent can reason about lineage, column-level changes, and statistical differences — not just raw SQL.

!!! tip "Claude Code users: skip to the easy path"
    The [Recce Claude Plugin](../2-getting-started/claude-plugin.md) handles all setup automatically — prerequisites, artifact generation, and server startup — in two commands. If you use Claude Code, start there.

## What you can do

Once connected, ask your AI agent questions like:

- "What schema changes happened in this branch?"
- "Show me the Row Count Diff for all modified models"
- "Are there any breaking column changes in this PR?"
- "Profile the orders table and compare it against production"
- "Run a custom SQL query against both dev and prod and show the differences"

Your agent translates these into the appropriate Recce tool calls and returns the results directly in your conversation.

## How it works

Recce compares your current branch against a baseline from your main branch. It needs two sets of dbt artifacts — one representing your current work and one representing your base branch. The MCP server reads both artifact sets and runs diffs against your warehouse when your AI agent requests them.

## Prerequisites

Before starting the MCP server, you need dbt artifacts for your current branch. Base artifacts are recommended for full diffing but not required.

### Generate development artifacts

Run dbt in your current working branch:

```shell
dbt docs generate
```

This creates `target/manifest.json` and `target/catalog.json`.

### Generate base artifacts

Generate artifacts from your base branch to a separate directory:

```shell
dbt docs generate --target-path target-base
```

This creates `target-base/manifest.json` and `target-base/catalog.json`. The MCP server compares these two artifact sets to produce diffs.

!!! note
    If `target-base/` is missing, the MCP server starts in **single-environment mode** — all tools remain available, but diff results show no changes because both sides reference the same data. Generate base artifacts to enable real comparisons.

## Installation

Install Recce with the MCP extra dependency:

```shell
pip install 'recce[mcp]'
```

Recce works with all major dbt adapters, including Snowflake, BigQuery, Redshift, Databricks, DuckDB, and others.

## Configuration

Choose the tab for your AI agent. **stdio** is simpler (no separate process to manage) and works for most setups. Use **SSE** only if you need to share a single Recce server across multiple tools simultaneously.

=== "Claude Code"

    ### Option A: Recce plugin (recommended)

    The [Recce Claude Plugin](../2-getting-started/claude-plugin.md) provides guided setup, handles prerequisite checks, generates artifacts, and starts the MCP server — all through interactive commands.

    ```
    /plugin marketplace add DataRecce/recce-claude-plugin
    /plugin install recce-quickstart@recce-claude-plugin
    /recce-setup
    ```

    See the [Claude Plugin guide](../2-getting-started/claude-plugin.md) for full details.

    ### Option B: Stdio

    Configure Recce as an MCP server with stdio transport. Claude Code automatically launches the server when you start a session.

    ```shell
    cd my-dbt-project/
    claude mcp add --scope project recce -- recce mcp-server
    ```

    Then start Claude Code and verify the connection:

    ```shell
    claude
    ```

    ```
    > /mcp
    ╭────────────────────────────────────────────────────────────╮
    │ Manage MCP servers                                         │
    │                                                            │
    │ ❯ 1. recce            ✔ connected · Enter to view details  │
    ```

    ### Option C: SSE

    Launch a standalone MCP server that Claude Code connects to via HTTP. Use this if you want to keep the server running independently or share it across tools.

    Start the server in a separate terminal:

    ```shell
    cd my-dbt-project/
    recce mcp-server --sse
    ```

    In another terminal, configure Claude Code:

    ```shell
    cd my-dbt-project/
    claude mcp add --transport sse --scope project recce http://localhost:8000/sse
    ```

=== "Cursor"

    Add to `.cursor/mcp.json` in your dbt project:

    ```json
    {
      "mcpServers": {
        "recce": {
          "command": "recce",
          "args": ["mcp-server"]
        }
      }
    }
    ```

    Or use SSE mode:

    ```json
    {
      "mcpServers": {
        "recce": {
          "url": "http://localhost:8000/sse"
        }
      }
    }
    ```

=== "Windsurf"

    Add to `~/.codeium/windsurf/mcp_config.json`:

    ```json
    {
      "mcpServers": {
        "recce": {
          "command": "recce",
          "args": ["mcp-server"]
        }
      }
    }
    ```

=== "Generic (stdio)"

    Any MCP-compatible client can use stdio transport:

    ```json
    {
      "command": "recce",
      "args": ["mcp-server"],
      "transport": "stdio"
    }
    ```

=== "Generic (SSE)"

    Start the server:

    ```shell
    recce mcp-server --sse --host localhost --port 8000
    ```

    Connect your client to: `http://localhost:8000/sse`

## Available tools

The MCP server exposes these tools to your AI agent:

| Tool | Description |
|------|-------------|
| `lineage_diff` | Compare data lineage between base and current branches |
| `schema_diff` | Detect schema changes (added, removed, or modified columns and type changes) |
| `row_count_diff` | Compare row counts between branches |
| `profile_diff` | Statistical profiling comparison (min, max, avg, nulls, and more) |
| `query` | Run arbitrary SQL against your warehouse |
| `query_diff` | Run the same SQL against both branches and compare results |
| `list_checks` | List all validation checks in the current session with their status |
| `run_check` | Run a specific validation check by ID |

### Check types available through `run_check`

These check types are accessible as preset checks configured in `recce.yml` or created in the Recce instance. Your AI agent runs them with the `run_check` tool:

| Check type | Description |
|------------|-------------|
| `value_diff` | Compare actual data values row by row between branches |
| `top_k_diff` | Compare top-K value distributions |
| `histogram_diff` | Compare value distributions as histograms |

See [Preset checks](../7-cicd/preset-checks.md) for how to configure these check types.

!!! note
    If base artifacts (`target-base/`) are not present, the server starts in **single-environment mode** — all tools remain available, but diff results show no changes. Generate base artifacts to enable real comparisons.

## Troubleshooting

### MCP server fails to start

The most common cause is missing dbt artifacts. Check that your dbt artifacts exist:

```shell
ls target/manifest.json
```

If missing, run `dbt docs generate` in your current branch. See [Prerequisites](#prerequisites).

### Diff results show no changes

If the server starts but all diffs return empty results, you are likely in single-environment mode (missing base artifacts). Follow the [Generate base artifacts](#generate-base-artifacts) steps to enable real comparisons.

### Port already in use (SSE mode)

```shell
# Check what's using port 8000
lsof -i :8000

# Use a different port
recce mcp-server --sse --port 8001
```

### Warehouse connection errors

The MCP server uses your `profiles.yml` to connect to your warehouse. Verify your connection:

```shell
dbt debug
```

### Prefer guided setup over manual configuration

If you're using Claude Code and running into issues, the [Recce Claude Plugin](../2-getting-started/claude-plugin.md) handles prerequisite checks and provides actionable error messages:

```
/plugin install recce-quickstart@recce-claude-plugin
/recce-setup
```

See the [Claude Plugin guide](../2-getting-started/claude-plugin.md) for full setup instructions.

## FAQ

**"How do I validate data changes in my PR using an AI agent?"**

Connect Recce's MCP server to your AI agent (Claude Code, Cursor, or Windsurf), then ask questions in natural language. Your agent calls the appropriate validation tools and returns the results.

**"Which dbt adapters work with Recce MCP?"**

Recce works with all major dbt adapters: Snowflake, BigQuery, Redshift, Databricks, DuckDB, and others.

**"Do I need Recce Cloud to use the MCP server?"**

No. The MCP server is part of Recce OSS and free to use. [Recce Cloud](https://cloud.reccehq.com/) adds automated PR review, team collaboration, and persistent validation history.

**"What is MCP and how does Recce use it?"**

[MCP (Model Context Protocol)](https://modelcontextprotocol.io) is an open standard that allows AI agents to call external tools. Recce implements an MCP server so AI agents can run data diffs against your warehouse on demand.

## What's next

- [Recce Claude Plugin](../2-getting-started/claude-plugin.md) — guided setup for Claude Code users with interactive commands
- [Row Count Diff](row-count-diff.md) — understand row count validation
- [Profile Diff](profile-diff.md) — statistical profiling comparisons
- [Value Diff](value-diff.md) — row-by-row data validation
- [CI/CD Setup](../7-cicd/ci-cd-getting-started.md) — automate validation in your workflow
