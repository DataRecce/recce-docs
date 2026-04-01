---
title: Connect Your Repository
description: >-
  Connect your GitHub or GitLab repository to Recce Cloud for automated
  pull request data review and dbt validation.
---

# Connect Your Repository

**Goal:** Connect your GitHub or GitLab repository to Recce Cloud for automated PR data review.

Cloud supports GitHub and GitLab. Using a different provider? Contact us at support@reccehq.com.

## Prerequisites

- [x] Cloud account (free trial at cloud.reccehq.com)
- [x] Repository admin access (required to authorize app installation)
- [x] dbt project in the repository

## How It Works

When you connect a Git provider, Cloud maps your setup:

| Git Provider | Cloud |
|--------------|-------------|
| Organization | Organization |
| Repository | Project |

Every Cloud account starts with one organization and one project. When you connect your Git provider, you select which organization and repository to link.

**Monorepo support:** If you have multiple dbt projects in one repository, you can create multiple Cloud projects that connect to the same repo.

## Connect GitHub

### 1. Authorize the Recce GitHub App

Navigate to Settings → Git Provider in Cloud. Click **Connect GitHub**.

**Expected result:** GitHub authorization page opens.

### 2. Select Organization and Repository

Choose which GitHub organization to connect. This becomes your Cloud organization.

Then select the repository containing your dbt project. This becomes your Cloud project.

**Expected result:** Repository connected. Your Cloud project is ready to use.

![alt text](../assets/images/setup-guides/connect-github.png){: .shadow}

## Connect GitLab

GitLab uses Personal Access Tokens (PAT) instead of OAuth. We recommend creating a dedicated service account so that Recce Cloud PR comments appear as a bot, not as your personal account.

### 1. Create a Dedicated Service Account (Recommended)

PR comments posted through the GitLab API appear as the token owner. If you use your personal token, your teammates see comments from *you* rather than from Recce Cloud.

To avoid this, create a **GitLab service account** for Recce Cloud:

1. In GitLab, navigate to your **group Settings > Service Accounts**
2. Click **Add service account**
3. Set the name to **Recce Cloud** (username auto-generates)
4. Click **Create service account**
5. (Optional) Edit the account to customize the username and upload a Recce avatar

**Expected result:** Service account appears in the group's member list with a "service account" badge.

Add the service account as a **Developer** member to the projects you want Recce Cloud to access.

!!! info "Availability"
    GitLab service accounts are available on GitLab.com Free (up to 100 per group), Premium, and Ultimate. For Self-Managed Free instances where service accounts are unavailable, create a dedicated GitLab user (e.g., `recce-cloud-bot`) instead.

### 2. Create a Personal Access Token

Generate a PAT for your service account (not your personal account):

1. In the service account's settings, click **Manage access tokens > Add new token**
2. Set a descriptive name (e.g., "Recce Cloud integration")
3. Select the **`api`** scope (required for PR comments)
4. Set an expiration date and click **Create**
5. Copy the token immediately (it cannot be viewed again)

### 3. Add Token to Cloud

Navigate to **Settings > Git Provider** in Recce Cloud. Select GitLab and paste the token.

## Verify Success

In Cloud, navigate to your repository. You should see:

- Connection status: "Connected"
- Organization Project is linked to a git repository

![alt text](../assets/images/setup-guides/connect-gitlab.png){: .shadow}
![alt text](../assets/images/setup-guides/org-projects.png){: .shadow}

## Troubleshooting

| Issue | Solution |
| --- | --- |
| Repository not found | Ensure proper permissions are granted (GitLab: token access, GitHub: app authorized) |
| Invalid token (GitLab) | Generate new token with `api` scope |
| Cannot post PR comments (GitLab) | Regenerate token with `api` scope instead of `read_api` |
| PR comments show as personal user (GitLab) | Create a [service account](#1-create-a-dedicated-service-account-recommended) and use its token instead of your personal token |

## Next Steps

- [Connect Data Warehouse](connect-to-warehouse.md)
- [Add Recce to CI/CD](environment-setup.md)
