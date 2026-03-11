---
title: CLI Reference
description: >-
  Command-line reference for the open source and Recce Cloud CLIs. Run dbt validation,
  data diffing, and artifact uploads from your terminal.
---

# CLI Reference

This reference documents the command-line interfaces for the open source CLI (`recce`) and the Recce Cloud CLI (`recce-cloud`).

## Overview

Recce provides two CLI tools:

- **`recce`** - The open source CLI for local data validation and diffing
- **`recce-cloud`** - The cloud CLI for uploading artifacts to Cloud in CI/CD workflows

## recce Commands

### recce server

Starts the Recce web server for interactive data validation.

**Syntax:**

```bash
recce server [OPTIONS] [STATE_FILE]
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `STATE_FILE` | Optional path to a state file. If specified and exists, loads the state. If specified and does not exist, creates a new state file at that path. |

**Options:**

| Option | Description |
|--------|-------------|
| `--review` | Enable review mode. Uses dbt artifacts from the state file instead of `target/` and `target-base/` directories. |
| `--api-token <token>` | API token for Cloud connection. |

**Examples:**

Start server with default settings:

```bash
recce server
```

Start server with a state file:

```bash
recce server my_recce_state.json
```

Start server in review mode (uses artifacts from state file):

```bash
recce server --review my_recce_state.json
```

Start server with Cloud connection:

```bash
recce server --api-token <your_api_token>
```

**Notes:**

- The server runs on `http://localhost:8000` by default
- Requires dbt artifacts in `target/` (current) and `target-base/` (base) directories unless using `--review` mode
- State is auto-saved when the Save button is clicked in the UI

### recce run

Executes preset checks and saves results to a state file.

**Syntax:**

```bash
recce run [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--state-file <file>` | Path to state file. Default: `recce_state.json` |
| `--github-pull-request-url <url>` | GitHub PR URL for CI context |

**Examples:**

Run all preset checks:

```bash
recce run
```

Run checks and save to specific state file:

```bash
recce run --state-file my_state.json
```

Run checks with GitHub PR context:

```bash
recce run --github-pull-request-url ${{ github.event.pull_request.html_url }}
```

**Notes:**

- Executes all checks defined in `recce.yml`
- Outputs results to the state file (default: `recce_state.json`)
- Used primarily in CI/CD pipelines for automated validation

### recce summary

Generates a summary report from a state file.

**Syntax:**

```bash
recce summary <STATE_FILE>
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `STATE_FILE` | Path to the state file to summarize |

**Examples:**

Generate summary from state file:

```bash
recce summary recce_state.json
```

Generate summary and save to file:

```bash
recce summary recce_state.json > recce_summary.md
```

**Notes:**

- Outputs summary in Markdown format
- Useful for generating PR comments in CI/CD workflows

### recce debug

Verifies Recce configuration and environment setup.

**Syntax:**

```bash
recce debug
```

**Examples:**

```bash
recce debug
```

**Notes:**

- Checks for required artifacts in `target/` and `target-base/` directories
- Verifies warehouse connection
- Useful for troubleshooting setup issues before launching the server

## recce-cloud Commands

The `recce-cloud` CLI is a lightweight tool for uploading dbt artifacts to Cloud in CI/CD pipelines.

### Installation

```bash
pip install recce-cloud
```

### recce-cloud upload

Uploads dbt artifacts to Cloud.

**Syntax:**

```bash
recce-cloud upload [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--type <type>` | Session type: `prod` for baseline, omit for PR/MR auto-detection |
| `--target-path <path>` | Path to dbt artifacts directory. Default: `target/` |
| `--dry-run` | Test configuration without uploading |

**Examples:**

Upload baseline artifacts (for CD workflow):

```bash
recce-cloud upload --type prod
```

Upload PR/MR artifacts (auto-detected):

```bash
recce-cloud upload
```

Upload from custom artifact path:

```bash
recce-cloud upload --target-path custom-target
```

Test configuration without uploading:

```bash
recce-cloud upload --dry-run
```

**Notes:**

- Automatically detects CI platform (GitHub Actions, GitLab CI)
- Uses `GITHUB_TOKEN` for GitHub authentication
- Uses `CI_JOB_TOKEN` for GitLab authentication
- Session type is auto-detected from PR/MR context when `--type` is omitted

**Environment Variables:**

| Platform | Variable | Description |
|----------|----------|-------------|
| GitHub | `GITHUB_TOKEN` | Authentication token (automatically available in Actions) |
| GitLab | `CI_JOB_TOKEN` | Authentication token (automatically available in CI/CD) |

### Expected Output

Successful upload displays:

```
─────────────────────────── CI Environment Detection ───────────────────────────
Platform: github-actions
Session Type: prod
Commit SHA: abc123de...
Source Branch: main
Repository: your-org/your-repo
Info: Using GITHUB_TOKEN for platform-specific authentication
────────────────────────── Creating/touching session ───────────────────────────
Session ID: f8b0f7ca-ea59-411d-abd8-88b80b9f87ad
Uploading manifest from path "target/manifest.json"
Uploading catalog from path "target/catalog.json"
Notifying upload completion...
──────────────────────────── Uploaded Successfully ─────────────────────────────
Uploaded dbt artifacts to Cloud for session ID "f8b0f7ca-ea59-411d-abd8-88b80b9f87ad"
```

## Common Workflows

### Local Development

```bash
# Start interactive session
recce server

# Or continue from saved state
recce server my_state.json
```

### CI/CD Pipeline

```bash
# CD: Update baseline after merge to main
recce-cloud upload --type prod

# CI: Upload PR artifacts for validation
recce-cloud upload
```

### Review Workflow

```bash
# Reviewer loads state file in review mode
recce server --review recce_state.json
```

## Related

- [Configuration](./configuration.md) - Preset check configuration in `recce.yml`
- [State File](./state-file.md) - State file format and usage
- [Setup CI](../2-getting-started/setup-ci.md) - CI/CD integration guide
- [Setup CD](../2-getting-started/setup-cd.md) - CD workflow setup
