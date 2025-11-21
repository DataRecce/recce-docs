---
title: MCP Server
---

Recce allows you to expose its tools to AI agents for integration. Here's how to use Claude Code to integrate with Recce.


## Method 1: MCP Server

To use Recce in Claude Code, add an MCP server to your project. Claude Code will launch the MCP server when the session starts.

1. Add Recce to your dbt project

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

Alternatively, you can launch a standalone MCP server. Claude Code will connect to it using HTTP-SSE.

1. Add Recce to your dbt project

    ```shell
    claude mcp add --transport sse --scope project recce http://localhost:8000/sse
    ```

2. Launch the standalone MCP server with HTTP-SSE

    ```shell
    cd my-dbt-project/
    recce mcp-server --sse
    ```

3. Run Claude Code

    ```shell
    claude
    ```

4. Ask Claude Code about your changes

    ```shell
    > Understand changes from Recce.
    ```
