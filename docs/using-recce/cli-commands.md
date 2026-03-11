---
title: CLI Commands
description: >-
  Command-line reference for Recce Cloud and Recce OSS CLIs. Connect to Cloud
  sessions, upload artifacts, and run local data validation.
---

# CLI Commands

Reference for the Recce command-line tools.

## Overview

Recce provides two pip packages:

1. **recce-cloud** (`pip install recce-cloud`) - Lightweight library for Cloud operations. Cloud users only need this to connect to sessions.
    - Prerequisite: [Recce Cloud setup](../getting-started/start-free-with-cloud.md) completed

2. **recce** (`pip install recce`) - Full OSS library with local server for data validation and diffing.
    - Prerequisite: [OSS Setup](../getting-started/oss-setup.md) completed

## recce-cloud Commands

Connect to Cloud sessions locally or upload artifacts in CI/CD pipelines.

### Installation

```bash
pip install recce-cloud
```

### Connect to Cloud sessions

**Step 1: Authenticate**

```bash
# Check current auth status
recce-cloud login --status

# If not logged in:
recce-cloud login
```

**Step 2: Initialize the project**

Link your local project to your Cloud organization:

```bash
recce-cloud init
```

**Step 3: Find your session**

```bash
# List all sessions
recce-cloud list

# Filter by type
recce-cloud list --type pr
```

**Step 4: Launch the server**

```bash
recce server --session-id <SESSION_ID>
```

The server runs locally on `http://localhost:8000` but fetches state from Cloud. Your changes automatically sync back when you close the session.

### CI/CD integration

Upload dbt artifacts to Cloud in your pipelines:

```bash
# CD workflow: Upload baseline after merge to main
recce-cloud upload --type prod

# CI workflow: Upload PR artifacts (auto-detected)
recce-cloud upload
```

**Environment variables:**

| Platform | Variable | Description |
|----------|----------|-------------|
| GitHub | `GITHUB_TOKEN` | Authentication token (automatic in Actions) |
| GitLab | `CI_JOB_TOKEN` | Authentication token (automatic in CI/CD) |

See [Setup CI](../setup-guides/setup-ci.md) and [Setup CD](../setup-guides/setup-cd.md) for complete guides.

### Command reference

#### recce-cloud login

```bash
recce-cloud login [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--status` | Check current authentication status |

#### recce-cloud init

```bash
recce-cloud init
```

Links your local project to a Cloud organization and project.

#### recce-cloud list

```bash
recce-cloud list [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--type <type>` | Filter by session type: `pr`, `dev`, `prod` |

#### recce-cloud upload

```bash
recce-cloud upload [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--type <type>` | Session type: `prod` for baseline, omit for auto-detection |
| `--target-path <path>` | Path to dbt artifacts. Default: `target/` |
| `--dry-run` | Test configuration without uploading |

## recce Commands

Run data validation locally with the full OSS library.

### Installation

```bash
pip install recce
```

### Local development workflow

```bash
# Start interactive session
recce server

# Continue from saved state
recce server my_state.json

# Share with reviewer (they load in review mode)
recce server --review my_state.json
```

See [OSS Workflow](oss-workflow.md) for the complete guide.

### Command reference

#### recce server

```bash
recce server [OPTIONS] [STATE_FILE]
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `STATE_FILE` | Optional state file path. Loads if exists, creates if not. |

**Options:**

| Option | Description |
|--------|-------------|
| `--session-id <id>` | Connect to a Cloud session by ID |
| `--review` | Review mode. Uses artifacts from state file instead of `target/` |
| `--api-token <token>` | API token for Cloud connection |

**Notes:**

- Runs on `http://localhost:8000` by default
- For OSS usage, requires artifacts in `target/` and `target-base/` unless using `--review` mode

#### recce run

Executes preset checks and saves results to a state file.

```bash
recce run [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--state-file <file>` | Path to state file. Default: `recce_state.json` |
| `--github-pull-request-url <url>` | GitHub PR URL for CI context |

#### recce summary

Generates a summary report from a state file.

```bash
recce summary <STATE_FILE>
```

#### recce debug

Verifies configuration and environment setup.

```bash
recce debug
```

Checks for required artifacts and warehouse connection.

## Related

- [Configuration](../technical-concepts/configuration.md) - Preset check configuration
- [State File](../technical-concepts/state-file.md) - State file format
