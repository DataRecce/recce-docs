---
title: Recce MCP Server — dbt Data Validation for AI Agents
description: >-
  Connect the Recce MCP server to Claude Code, Cursor, or Windsurf to validate
  dbt data changes through natural language. Supports schema diff, row count diff,
  value diff, and more via the Model Context Protocol (MCP).
---

# Recce MCP Server for dbt

Recce is a dbt data validation tool that compares your development branch against your base branch (typically main) and surfaces schema changes, row count differences, and data diffs. Its MCP server makes these capabilities available to any AI code agent — including Claude Code, Cursor, and Windsurf — so you can validate data changes through natural language without leaving your editor.

[MCP (Model Context Protocol)](https://modelcontextprotocol.io) is an open standard that lets AI assistants call external tools directly. Recce implements an MCP server so your AI agent can run data diffs against your warehouse on your behalf.

Unlike general-purpose database tools, Recce's MCP server is built specifically for dbt branch comparison. It reads dbt artifacts (`manifest.json`, `catalog.json`) to understand your model graph, so your AI agent can reason about lineage, column-level changes, and statistical differences — not just raw SQL.

!!! tip "Claude Code users: skip to the easy path"
    The [Recce Claude Plugin](../2-getting-started/claude-plugin.md) handles all of the setup below automatically — prerequisites, artifact generation, and server startup — in two commands. If you use Claude Code, start there.

## What you can do with Recce MCP

Once connected, you can ask your AI agent questions like:

- "What schema changes happened in this branch?"
- "Show me the row count diff for all modified models"
- "Are there any breaking column changes in this PR?"
- "Profile the orders table and compare it against production"
- "Run a custom SQL query against both dev and prod and show the differences"

Your agent translates these into the appropriate Recce tool calls and returns the results directly in your conversation.

## How it works

Recce compares your current branch's dbt models against a baseline from your main branch. To do this, it needs two sets of dbt artifacts (the `manifest.json` and `catalog.json` metadata files that dbt generates) — one representing your current work and one representing your base branch. The MCP server reads both artifact sets and runs diffs against your warehouse when your AI agent requests them.

## Prerequisites

Before starting the MCP server, generate both artifact sets.

### Generate development artifacts

Run dbt in your current working branch:

```shell
dbt docs generate
```

This creates `target/manifest.json` and `target/catalog.json`.

### Generate base artifacts

Switch to your base branch and generate artifacts to a separate directory:

```shell
git stash                                # save uncommitted changes
git checkout main                        # switch to base branch
dbt docs generate --target-path target-base  # generate base artifacts
git checkout <your-branch>                # switch back
git stash pop                            # restore changes
```

This creates `target-base/manifest.json` and `target-base/catalog.json`. The MCP server compares these two artifact sets to produce diffs.

!!! warning
    The MCP server will not start if either `target/manifest.json` or `target-base/manifest.json` is missing.

## Installation

Install Recce with the MCP extra dependency:

```shell
pip install 'recce[mcp]'
```

Recce works with all major dbt adapters, including Snowflake, BigQuery, Redshift, Databricks, DuckDB, and others.

## Configuration

Choose the tab for your AI agent. If you're unsure which transport to use: **stdio** is simpler (no separate process to manage) and works for most setups. Use **SSE** only if you need to share a single Recce server across multiple tools simultaneously.

=== "Claude Code"

    ### Option A: Recce plugin (recommended)

    The [Recce Claude Plugin](../2-getting-started/claude-plugin.md) is the easiest way to get started. Unlike manual MCP configuration, the plugin provides guided setup, handles prerequisite checks, generates artifacts, and starts the MCP server for you — all through interactive commands.

    ```
    /plugin marketplace add DataRecce/recce-claude-plugin
    /plugin install recce-quickstart@recce-claude-plugin
    /recce-setup
    ```

    See the [Claude Plugin guide](../2-getting-started/claude-plugin.md) for full details.

    ### Option B: Stdio

    Configure Recce as an MCP server with stdio transport. Claude Code automatically launches the server when you start a session — no separate process to manage.

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

When connected, the MCP server exposes these tools to your AI agent:

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

!!! note "MCP server modes"
    The MCP server supports three modes: **server** (default), **preview**, and **read-only**. In preview and read-only modes, only `lineage_diff` and `schema_diff` are available — tools that query your warehouse are disabled.

## Troubleshooting

### MCP server fails to start

The most common cause is missing dbt artifacts. Check that both artifact directories exist:

```shell
ls target/manifest.json target-base/manifest.json
```

If either file is missing, follow the [Prerequisites](#prerequisites) section above.

### "No such file or directory: target-base/manifest.json"

You need to generate base artifacts. See [Prerequisites](#prerequisites).

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

**Which AI agents does Recce MCP support?**

Recce MCP works with any MCP-compatible AI agent, including Claude Code, Cursor, and Windsurf. It supports both stdio and SSE transport modes.

**What dbt adapters are supported?**

Recce works with all major dbt adapters: Snowflake, BigQuery, Redshift, Databricks, DuckDB, and others.

**Do I need Recce Cloud to use the MCP server?**

No. The MCP server is part of Recce OSS and is free to use. [Recce Cloud](https://cloud.reccehq.com/) adds automated PR review, team collaboration, and persistent validation history.

**What is the Model Context Protocol?**

[MCP (Model Context Protocol)](https://modelcontextprotocol.io) is an open standard that allows AI agents to call external tools. Recce implements an MCP server so AI agents can run data diffs against your warehouse on demand.

## What's next

- [Recce Claude Plugin](../2-getting-started/claude-plugin.md) — guided setup for Claude Code users with interactive commands
- [Row Count Diff](row-count-diff.md) — understand row count validation
- [Profile Diff](profile-diff.md) — statistical profiling comparisons
- [Value Diff](value-diff.md) — row-by-row data validation
- [CI/CD Setup](../7-cicd/ci-cd-getting-started.md) — automate validation in your workflow
