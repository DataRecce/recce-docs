---
title: Admin Setup
---

# Set Up Your Organization

After connecting your Git repo to Recce Cloud, you need to configure your organization so your team can collaborate on PR validation.

**Goal:** Configure your Recce Cloud organization for team collaboration.

When you sign up for Recce Cloud, you get one organization and one project. After connecting to Git, your organization and project names automatically map to your Git provider's names. You can rename them and invite team members.

## Prerequisites

- [ ] Recce Cloud account with owner/admin access
- [ ] Git repository connected to Recce Cloud
- [ ] Team members' email addresses

## Steps

### 1. Access organization settings

Navigate to your organization configuration.

1. Log in to [Recce Cloud](https://cloud.reccehq.com)
2. Click **Settings** → **Organization** in the side panel

**Expected result:** Organization settings page displays your current organization.

![Recce Cloud Organization Settings page showing organization name and members section](../assets/images/6-collaboration/recce-cloud-org-setting-fs8.png){: .shadow}

### 2. Rename your organization (optional)

Update the organization name to match your company or team.

1. In Organization Settings, find the **Organization Name** field
2. Enter your preferred name
3. Click **Save**

**Expected result:** Organization name updates across all Recce Cloud pages.

### 3. Set up additional projects (monorepo)

!!! note "For monorepo users"
    If your repository contains multiple dbt projects, set up additional projects before inviting team members. Skip this step if you have a single dbt project.

1. In Organization Settings, navigate to **Projects**
2. Click **Add Project**
3. Enter the project name and select the subdirectory path
4. Click **Create**

**Expected result:** New project appears in the project list and sidebar.

### 4. Invite team members

Add collaborators to your organization.

1. In Organization Settings, find the **Members** section
2. Click **Invite Members**
3. Enter email addresses (use SSO email if members use SSO login)
4. Select a role for each invitee:

| Role | Permissions |
|------|-------------|
| **Owner** | The one who created this organization. Full organization management: update info, manage roles, remove members |
| **Admin** | Same permissions as Owner |
| **Member** | Upload metadata, launch Recce instances, view organization info |

!!! tip "SSO login requires Team plan or above"
    SSO login is available on the Team plan and above. See [Pricing](https://www.reccehq.com/pricing) for plan details.

1. Click **Send Invitation**

**Expected result:** Invitees receive email invitations and see notifications when logged in.

![Invite Members dialog with email input field and role selection](../assets/images/6-collaboration/recce-cloud-org-invitation-fs8.png){: .shadow}

## Additional Settings

### Rename your project

Update the project name if needed.

1. Navigate to your project → click **Settings**
2. Enter the new project name
3. Click **Save**

**Expected result:** Project name updates in the sidebar and project list.

## Verify Success

Confirm your setup by checking:

1. Organization name displays correctly in the sidebar
2. Invited members appear in the Members list (pending or active)
3. All projects are listed under Settings → Projects

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Invitation not received | Check spam folder; verify email address matches SSO provider |
| Member sees their own org, not company org | They may have signed up with a different email than the one you invited; ask them to log in with the invited email |
| Cannot change organization name | Confirm you have Admin role |
| Project not appearing | Refresh the page; verify the subdirectory path is correct |

## For Invited Users

When you receive an invitation:

1. **Immediate response:** A notification modal appears on login — accept or decline directly
2. **Later:** Navigate to **Settings** → **Organization** to view pending invitations

![Recce Cloud home page showing pending invitation notification modal](../assets/images/6-collaboration/recce-cloud-org-pending-invitation-home-fs8.png){: .shadow}

## Next Steps

- [Data Developer Workflow](data-developer.md) — Learn how developers validate changes
- [Data Reviewer Workflow](data-reviewer.md) — Learn how reviewers approve PRs
