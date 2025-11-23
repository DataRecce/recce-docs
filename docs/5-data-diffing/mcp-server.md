---
title: MCP Server
---

Recce exposes its tools to AI agents, enabling integration with tools like Claude Code. This allows you to interact with Recce analysis through natural language queries directly in your Claude Code sessions.


## Installation

1. Install Recce with the MCP extra dependency:

   ```shell
   pip install 'recce[mcp]'
   ```

2. Verify the MCP server works by starting it in your dbt project:

   ```shell
   cd my-dbt-project/
   recce mcp-server
   ```

   You should see the message: `Starting Recce MCP Server in stdio mode...` Stop the server with `Ctrl+C` once confirmed.

## Method 1: MCP Server (stdio)

Configure Recce as an MCP server with stdio transport. Claude Code will automatically launch the MCP server when you start a session.

1. Configure the MCP server for your dbt project:

    ```shell
    claude mcp add --scope project recce -- recce mcp-server
    ```

2. Run Claude Code

    ```shell
    claude
    ```

3. Ask Claude Code about your changes

    ```shell
    > Understand changes from Recce.
    ```

## Method 2: MCP Server (SSE)

Alternatively, launch a standalone MCP server that Claude Code connects to via HTTP-SSE. This requires running the server in a separate terminal.

1. Configure the MCP server for your dbt project:

    ```shell
    claude mcp add --transport sse --scope project recce http://localhost:8000/sse
    ```

2. In a separate terminal, start the standalone MCP server:

    ```shell
    cd my-dbt-project/
    recce mcp-server --sse
    ```

3. In your original terminal, run Claude Code:

    ```shell
    claude
    ```

4. Ask Claude Code about your changes:

    ```shell
    > Understand changes from Recce.
    ```
