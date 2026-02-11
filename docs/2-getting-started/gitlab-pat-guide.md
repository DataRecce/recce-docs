---
title: GitLab Personal Access Token
---

# GitLab Personal Access Token Setup

To integrate Recce with your GitLab project, you'll need to create a Personal Access Token (PAT) with appropriate
permissions.

## Token Scope Requirements

Recce supports two different permission levels depending on your needs:

| Scope      | Permissions                      | Features Available                                                                                                                  |
|------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `api`      | Full API access (read and write) | • View and track merge requests<br>• **Receive generated summaries and notes on MRs from Recce**<br>• Full integration capabilities |
| `read_api` | Read-only API access             | • View and track merge requests<br>• **Cannot receive generated summaries and notes on MRs from Recce**                             |

!!!warning "Important: Choose the Right Scope"
    If you want Recce to automatically post validation summaries and notes directly to your merge requests, you **must** use
    the `api` scope. The `read_api` scope only allows Recce to read merge request information but cannot write comments or
    summaries back to GitLab.

## How to Create a Personal Access Token

Follow these steps to create a Personal Access Token in GitLab:

1. **Navigate to [Personal Access Token Settings in GitLab](https://gitlab.com/-/user_settings/personal_access_tokens)**

2. **Create New Token**
    - Click **Add new token** button
    - Enter a descriptive **Token name** (e.g., "Recce Integration")
    - Set an **Expiration date**

3. **Select Scopes**

    Choose one of the following based on your needs:

    **Option A: Full Integration (Recommended)**<br>
    - ✅ `api` scope<br>
    - This enables Recce to post validation summaries and notes to your merge requests

    **Option B: Read-Only Access**<br>
    - ✅ `read_api` scope<br>
    - ⚠️ You will **not** receive generated PR summaries and notes on your MRs from Recce

4. **Generate Token**
    - Click **Create personal access token**
    - **Important**: Copy the token immediately - you won't be able to see it again!

5. **Save Token Securely**
    - Store the token in a secure location


## Using Your Token with Recce

Once you have your Personal Access Token:

1. Navigate to Recce settings
2. Select GitLab integration
3. Paste your Personal Access Token
4. Complete the connection setup

## Troubleshooting

**Token not working?**

- Verify you've selected the correct scope (`api` or `read_api`)
- Check that the token hasn't expired
- Ensure you have appropriate project permissions (Maintainer or Owner role)

**Not receiving summaries on merge requests?**

- Verify your token uses the `api` scope (not just `read_api`)
- Check that Recce has write permissions to your project

**Still having issues?**

- Please reach out to us on [our Discord](https://discord.gg/HUUx9fyphJ) or via email at `help@reccehq.com`

## Related Documentation

- [Connect Git Provider](./start-free-with-cloud.md#2-connect-git-provider)
- [CI/CD Getting Started](../7-cicd/ci-cd-getting-started.md)
