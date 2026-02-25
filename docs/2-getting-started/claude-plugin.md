---
title: Recce Claude Plugin — AI-Assisted dbt Data Validation in Claude Code
description: >-
  Install and use the Recce Claude Plugin to validate dbt data changes
  directly in Claude Code. Automates MCP server setup, artifact generation,
  and provides slash commands for schema diff, row count diff, and PR review.
---

# Recce Claude Plugin for Claude Code

Recce is a dbt data validation tool that compares your development branch against your base branch and surfaces schema changes, row count differences, and data diffs before you merge. The Recce Claude Plugin brings this capability into Claude Code, making it accessible through natural language and interactive slash commands.

If you're reviewing dbt pull requests with Claude Code, the plugin connects Claude directly to your data warehouse so you can ask questions like "What changed in the orders model?" and get validated answers — without writing a single query by hand.

## Why use the plugin?

Without Recce, reviewing data changes in a dbt PR means manually querying your warehouse, comparing results across branches, and hoping you've checked the right models. With the Recce Claude Plugin, Claude does this for you — it runs schema diffs, row count comparisons, and statistical profiles across your modified models and reports back in plain language.

The plugin also handles all of the setup that the [MCP server](../5-data-diffing/mcp-server.md) requires manually:

- Checks prerequisites (Python, dbt, Git)
- Installs Recce if needed
- Generates base and current dbt artifacts (the `manifest.json` and `catalog.json` metadata files that Recce needs)
- Starts the MCP server automatically
- Provides slash commands for common validation workflows

!!! note
    If you use Cursor, Windsurf, or another AI agent, see the [MCP Server page](../5-data-diffing/mcp-server.md) for direct configuration instructions.

## Requirements

- Claude Code 1.0.33 or higher
- Python 3.8+
- dbt (any adapter — Snowflake, BigQuery, Redshift, Databricks, DuckDB, and others)
- Git

## Installation

### Step 1: Add the Recce marketplace

In Claude Code, run:

```
/plugin marketplace add DataRecce/recce-claude-plugin
```

### Step 2: Install the plugin

```
/plugin install recce-quickstart@recce-claude-plugin
```

Or use the interactive installer:

```
/plugin
```

Navigate to the **Discover** tab, find `recce-quickstart`, and press Enter to install.

### Step 3: Verify installation

```
/plugin
```

Navigate to the **Installed** tab to confirm `recce-quickstart` appears.

!!! tip "Installation scopes"
    By default, the plugin installs at user scope (available across all projects). You can also install at project scope (`--scope project`) to share with your team, or local scope (`--scope local`) for just the current repository.

## Getting started

Make sure you're on your feature branch — Recce compares your current branch against main. Then navigate to your dbt project and run the setup command:

```
/recce-setup
```

This walks you through:

1. Verifying your dbt project and warehouse connection
2. Generating development dbt artifacts (`target/manifest.json`)
3. Generating base dbt artifacts (`target-base/manifest.json`)
4. Starting the Recce MCP server

When setup completes, you'll see confirmation that the MCP server is running and connected.

Once connected, Claude has access to all of Recce's validation tools. Try asking a question about your data changes:

```
You: What schema changes happened in my current branch?
```

Claude calls Recce's `schema_diff` tool behind the scenes and responds with a summary of added, removed, or modified columns across your changed models.

## Available commands

| Command | Description |
|---------|-------------|
| `/recce-setup` | Guided setup — installs dependencies, generates artifacts, starts the MCP server |
| `/recce-pr [url]` | Analyze data impact of a pull request (auto-detects PR from current branch) |
| `/recce-check [type] [model]` | Run validation checks (row-count, schema, profile, query-diff) |
| `/recce-ci` | Generate GitHub Actions workflows for Recce Cloud CI/CD |

## Example workflows

### Analyze a pull request

```
/recce-pr https://github.com/your-org/your-repo/pull/123
```

Or if you're already on the PR branch:

```
/recce-pr
```

### Run specific validation checks

```
/recce-check row-count orders
/recce-check schema customers
/recce-check profile payments
```

## Managing the plugin

Disable the plugin:

```
/plugin disable recce-quickstart@recce-claude-plugin
```

Re-enable:

```
/plugin enable recce-quickstart@recce-claude-plugin
```

Uninstall:

```
/plugin uninstall recce-quickstart@recce-claude-plugin
```

Update to latest version:

```
/plugin marketplace update recce-claude-plugin
```

## Troubleshooting

### Plugin not loading

1. Verify Claude Code version is 1.0.33 or higher: `claude --version`
2. Check the plugin is installed: `/plugin` → **Installed** tab
3. Check for errors: `/plugin` → **Errors** tab

### MCP server not starting

1. Make sure you're in a dbt project directory (has `dbt_project.yml`)
2. Verify Recce is installed: `pip install 'recce[mcp]'`
3. Check if port 8081 is available, or set a custom port: `RECCE_MCP_PORT=8085`
4. Re-run the setup: `/recce-setup`

### Commands not recognized

1. Confirm the plugin is enabled: `/plugin` → **Installed** tab → check status
2. Restart Claude Code to reload plugins

## FAQ

**Does the Recce Claude Plugin work with Cursor or Windsurf?**

The plugin is specific to Claude Code. For Cursor and Windsurf, configure Recce using the [MCP server](../5-data-diffing/mcp-server.md) directly.

**What dbt adapters does Recce support?**

Recce works with any dbt adapter, including Snowflake, BigQuery, Redshift, Databricks, DuckDB, and others.

**What is the Model Context Protocol (MCP)?**

[MCP](https://modelcontextprotocol.io) is an open standard that lets AI agents like Claude Code call external tools. Recce implements an MCP server so Claude can run data diffs against your warehouse on demand.

**Can I use the plugin without Recce Cloud?**

Yes. The plugin works with Recce OSS for local validation. [Recce Cloud](https://cloud.reccehq.com/) adds automated PR review, team collaboration, and persistent validation history.

## What's next

- [Recce MCP Server](../5-data-diffing/mcp-server.md) — configure Recce with Cursor, Windsurf, and other AI agents, or explore advanced MCP options
- [Row Count Diff](../5-data-diffing/row-count-diff.md) — understand row count validation
- [Profile Diff](../5-data-diffing/profile-diff.md) — statistical profiling comparisons
- [CI/CD Setup](../7-cicd/ci-cd-getting-started.md) — automate validation in your workflow
