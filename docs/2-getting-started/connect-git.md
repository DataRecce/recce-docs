# Connect Git Provider

**Goal:** Connect your GitHub or GitLab repository to Recce Cloud for automated PR data review.

Recce Cloud supports GitHub and GitLab. Using a different provider? Contact us at support@reccehq.com.

## Prerequisites

- [ ] Recce Cloud account (free trial at cloud.reccehq.com)
- [ ] Repository admin access (required to authorize app installation)
- [ ] dbt project in the repository

## How It Works

When you connect a Git provider, Recce Cloud maps your setup:

| Git Provider | Recce Cloud |
|--------------|-------------|
| Organization | Organization |
| Repository | Project |

Every Recce Cloud account starts with one organization and one project. When you connect your Git provider, you select which organization and repository to link.

**Monorepo support:** If you have multiple dbt projects in one repository, you can create multiple Recce Cloud projects that connect to the same repo.
<!-- TODO: add link to monorepo section -->

## Connect GitHub

### 1. Authorize the Recce GitHub App

Navigate to Settings → Git Provider in Recce Cloud. Click **Connect GitHub**.

**Expected result:** GitHub authorization page opens.

### 2. Select Organization and Repository

Choose which GitHub organization to connect. This becomes your Recce Cloud organization.

Then select the repository containing your dbt project. This becomes your Recce Cloud project.

**Expected result:** Repository connected. Your Recce Cloud project is ready to use.

<!-- TODO: add screenshot -->

## Connect GitLab

GitLab uses Personal Access Tokens (PAT) instead of OAuth.

### 1. Create a Personal Access Token

In GitLab: User Settings → Access Tokens → Add new token.

**Required scopes:**

- `api` - Full access (required for PR comments)
- `read_api` - Read-only alternative (limited functionality)

**Expected result:** Token string displayed (copy immediately).

### 2. Add Token to Recce Cloud

Navigate to Settings → Git Provider. Select GitLab, paste token.

## Verify Success

In Recce Cloud, navigate to your repository. You should see:

- Connection status: "Connected"
- Repository branches visible

## Troubleshooting

### Error: "Repository not found"

**Cause:** Token lacks access to the repository (GitLab) or app not authorized for repo (GitHub).
**Solution:** Ensure proper permissions are granted.

### Error: "Invalid token" (GitLab)

**Cause:** Token expired or incorrect scope.
**Solution:** Generate new token with `api` scope.

### Error: "Cannot post PR comments" (GitLab)

**Cause:** Using `read_api` instead of `api` scope.
**Solution:** Regenerate token with `api` scope.

## Next Steps

- [Connect Data Warehouse](../5-data-diffing/connect-to-warehouse.md)
- [Add Recce to CI/CD](../7-cicd/setup-ci.md)
