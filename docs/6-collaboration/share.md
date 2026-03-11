---
title: Share
description: >-
  Share Recce validation results securely with team members and stakeholders
  for collaborative dbt pull request review.
---

# Share

Share your validation results with team members and stakeholders.

**Goal:** Give reviewers access to your Recce session so they can explore validation results.

## Recce Cloud

Share your session by copying the URL directly from your browser. Team members with organization access can view any session immediately.

To invite team members to your organization, see [Admin Setup](../3-using-recce/admin-setup.md#5-invite-team-members).

## Recce OSS

For local Recce sessions, use these sharing methods:

| Method | Best For | Requires |
|--------|----------|----------|
| **Copy to Clipboard** | Quick screenshots in PR comments | Nothing |
| **Upload to Recce Cloud** | Full interactive session access | Recce Cloud account |

### Copy to Clipboard

For quick sharing of specific results, use **Copy to Clipboard** in any diff result. Paste the screenshot directly into PR comments, Slack, or other channels.

<figure markdown>
  ![Copy a diff screenshot to the clipboard - Multiple models](../assets/images/6-collaboration/clipboard-to-github.gif){: .shadow}
  <figcaption>Copy diff result and paste to GitHub</figcaption>
</figure>

!!! note "Browser Compatibility"
    Firefox does not support copying images to the clipboard. Recce displays a modal where you can download or right-click to copy the image.

### Upload to Recce Cloud

When reviewers need full context, upload your session to Recce Cloud. This creates a shareable link with complete access to your validation results.

**Benefits:**

- No setup required for viewers
- Full lineage exploration, query results, and checklists
- Read-only access (secure viewing)
- Simple link sharing via any channel

!!! warning "Access Control"
    Anyone with the link can view your session after signing into Recce Cloud. For restricted access, [contact our team](https://cal.com/team/recce/chat).

#### First-time setup

1. Launch Recce server and click **Use Recce Cloud** if not already connected

    ![Recce Server](../assets/images/6-collaboration/recce-server-use-recce-cloud-for-free.png){: .shadow}

2. Sign in and authorize your local Recce to connect with Recce Cloud

    ![Request Approved](../assets/images/6-collaboration/recce-cloud-connection-request-approved.png){: .shadow}

3. Refresh the page to activate the connection. The **Share** button is now available.

    ![Recce Share From Server](../assets/images/6-collaboration/recce-share-from-server-fs8.png){: .shadow}

!!! tip "Alternative: CLI Setup"
    ```bash
    recce connect-to-cloud
    ```

#### Manual configuration (advanced)

For containerized environments or manual setup:

1. Get your API token from [Recce Cloud settings](https://cloud.reccehq.com/settings#tokens)

    ![Recce API Token](../assets/images/6-collaboration/setting-page-api-token-fs8.png){: .shadow}

2. Configure using one of these methods:

    **Option A: Command line flag**
    ```bash
    recce server --api-token <your_api_token>
    ```

    **Option B: Profile configuration**
    ```yaml
    # ~/.recce/profile.yml
    api_token: <your_api_token>
    ```

#### Share from UI or CLI

**From UI:** Click the **Share** button and select Recce Cloud.

<figure markdown>
  ![Click Share](../assets/images/6-collaboration/share-button.png){: .shadow}
  <figcaption>Access sharing options from the Share button</figcaption>
</figure>

Choose the sharing method that best fits your collaboration needs:

1. **Copy to Clipboard** - Quick screenshot sharing for PR comments and discussions
2. **Recce Cloud Sharing** - Full interactive session sharing with complete context

## Method 1: Copy to Clipboard

For quick sharing of specific results, use the **Copy to Clipboard** button found in diff results. This feature captures a screenshot image that you can paste directly into PR comments, Slack messages, or other communication channels.

<figure markdown>
  ![Copy a diff screenshot to the clipboard - Multiple models](../assets/images/6-collaboration/clipboard-to-github.gif){: .shadow}
  <figcaption>Copy a diff result screenshot to the clipboard and paste to GitHub</figcaption>
</figure>

!!! note "Browser Compatibility"
    Firefox does not support copying images to the clipboard. Instead, Recce displays a modal where you can download the image locally or right-click to copy the image.

## Method 2: Recce Cloud Sharing

When stakeholders need full context but don't have the environment to run Recce locally, use Cloud sharing. This method creates a read-only link that provides complete access to your validation results.

### Benefits of Cloud Sharing

- **No Setup Required** - Stakeholders access results instantly in their browser
- **Full Context** - Complete lineage exploration, query results, and validation checklists
- **Read-Only Access** - Secure viewing without ability to modify your work
- **Simple Link Sharing** - Share via any communication channel

!!! warning "Access Control"
    Anyone with the shared link can view your Recce session after signing into Cloud. For restricted access requirements, [contact our team](https://cal.com/team/recce/chat).

## Setting Up Cloud Sharing

The first time you share via Cloud, you'll need to associate your local Recce with your cloud account. This one-time setup enables secure hosting of your state files.

### Step 1: Enable Cloud Connection

Launch the Recce server and click the **Use Recce Cloud** button if your local installation isn't already connected to Cloud.

![Recce Server](../assets/images/6-collaboration/recce-server-use-recce-cloud-for-free.png){: .shadow}

### Step 2: Sign In and Grant Access

After successful login, authorize your local Recce to connect with Cloud. This authorization enables the sharing functionality and secure state file hosting.

![Request Approved](../assets/images/6-collaboration/recce-cloud-connection-request-approved.png){: .shadow}

### Step 3: Complete the Setup

Refresh the Recce page to activate the cloud connection. Once connected, the **Share** button will be available, allowing you to generate shareable links.

![Recce Share From Server](../assets/images/6-collaboration/recce-share-from-server-fs8.png){: .shadow}

!!! tip "Alternative Setup Method"
    You can also connect to Cloud using the command line:
    
    ```bash
    recce connect-to-cloud
    ```
    
    This command handles the sign-in and authorization process directly from your terminal.

## Manual Configuration (Advanced)

For containerized environments or when you prefer manual setup, you can configure the Cloud connection directly using your API token.

### Step 1: Retrieve Your API Token

Sign in to Cloud and copy your API token from the [personal settings page](https://cloud.reccehq.com/settings#tokens).

![Recce API Token](../assets/images/6-collaboration/setting-page-api-token-fs8.png){: .shadow}

### Step 2: Configure Local Connection

Choose one of the following methods to configure your local Recce:

#### Option A: Command Line Flag

Launch Recce server with your API token. The token will be saved to your profile for future use:

```bash
recce server --api-token <your_api_token>
```

#### Option B: Profile Configuration

Edit your `~/.recce/profile.yml` file to include the API token:

```yaml
api_token: <your_api_token>
```

!!! info "Configuration File Location"
    **Mac/Linux:**
    ```shell
    cd ~/.recce
    ```
    
    **Windows:**
    ```powershell
    cd ~\.recce
    ```
    
    Navigate to `C:\Users\<your_username>\.recce` or use the PowerShell command above.

## Command Line Sharing

For automated workflows or when working with existing state files, use the `recce share` command to generate shareable links directly from the terminal.

### Basic Sharing

If your Recce is already connected to Cloud:

```bash
# If already connected to Recce Cloud
recce share <your_state_file>

# With API token
recce share --api-token <your_api_token> <your_state_file>
```

![Recce Share From CLI](../assets/images/6-collaboration/recce-share-from-cli.png){: .shadow}

## Verification

Confirm sharing works:

1. Add a check to your checklist
2. Share via your preferred method (URL for Cloud, Share button for OSS)
3. Open the link in an incognito window
4. Verify you can view the session

## Related

- [Admin Setup](../3-using-recce/admin-setup.md) - Invite team members to your organization
- [Checklist](checklist.md) - Save validation checks to share
- [Preset Checks](preset-checks.md) - Automate recurring checks
