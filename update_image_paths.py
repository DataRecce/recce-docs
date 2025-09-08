#!/usr/bin/env python3
import os
import re
from pathlib import Path

def update_image_paths():
    """Update all image paths in markdown files based on the reorganization."""
    
    # Define path mappings based on the moves we did
    path_mappings = {
        # 1-whats-recce
        "../assets/images/home/checklist-readme3.png": "../assets/images/1-whats-recce/checklist-readme3.png",
        "../assets/images/home/diff-readme2.png": "../assets/images/1-whats-recce/diff-readme2.png",
        "../assets/images/home/lineage-readme1.png": "../assets/images/1-whats-recce/lineage-readme1.png",
        
        # 2-getting-started
        "../assets/images/jaffle-shop/jaffle_shop_check.png": "../assets/images/2-getting-started/jaffle_shop_check.png",
        "../assets/images/jaffle-shop/jaffle_shop_lineage.png": "../assets/images/2-getting-started/jaffle_shop_lineage.png",
        "../assets/images/jaffle-shop/jaffle_shop_query.png": "../assets/images/2-getting-started/jaffle_shop_query.png",
        
        # 3-view-modified
        "../assets/images/features/actions-dropdown.png": "../assets/images/3-view-modified/actions-dropdown.png",
        "../assets/images/features/actions-menu.png": "../assets/images/3-view-modified/actions-menu.png",
        "../assets/images/features/add-to-checklist-button.png": "../assets/images/3-view-modified/add-to-checklist-button.png",
        "../assets/images/features/add-to-checklist.gif": "../assets/images/3-view-modified/add-to-checklist.gif",
        "../assets/images/features/clipboard-to-github.gif": "../assets/images/3-view-modified/clipboard-to-github.gif",
        "../assets/images/features/cll-1.png": "../assets/images/3-view-modified/cll-1.png",
        "../assets/images/features/cll-2.png": "../assets/images/3-view-modified/cll-2.png",
        "../assets/images/features/cll-3.png": "../assets/images/3-view-modified/cll-3.png",
        "../assets/images/features/code-diff.png": "../assets/images/3-view-modified/code-diff.png",
        "../assets/images/features/histogram-diff.gif": "../assets/images/3-view-modified/histogram-diff.gif",
        "../assets/images/features/histogram-diff.png": "../assets/images/3-view-modified/histogram-diff.png",
        "../assets/images/features/lineage-diff.gif": "../assets/images/3-view-modified/lineage-diff.gif",
        "../assets/images/features/model-schema-change-detected.png": "../assets/images/3-view-modified/model-schema-change-detected.png",
        "../assets/images/features/multi-node-row-count-diff.gif": "../assets/images/3-view-modified/multi-node-row-count-diff.gif",
        "../assets/images/features/multi-node-selection.gif": "../assets/images/3-view-modified/multi-node-selection.gif",
        "../assets/images/features/multi-node-value-diff.gif": "../assets/images/3-view-modified/multi-node-value-diff.gif",
        "../assets/images/features/node-details-panel.gif": "../assets/images/3-view-modified/node-details-panel.gif",
        "../assets/images/features/profile-diff.png": "../assets/images/3-view-modified/profile-diff.png",
        "../assets/images/features/row-count-diff-selector.gif": "../assets/images/3-view-modified/row-count-diff-selector.gif",
        "../assets/images/features/row-count-diff-single.gif": "../assets/images/3-view-modified/row-count-diff-single.gif",
        "../assets/images/features/schema-diff.gif": "../assets/images/3-view-modified/schema-diff.gif",
        "../assets/images/features/schema-diff.png": "../assets/images/3-view-modified/schema-diff.png",
        "../assets/images/features/select-node-children.gif": "../assets/images/3-view-modified/select-node-children.gif",
        "../assets/images/features/top-k-diff.gif": "../assets/images/3-view-modified/top-k-diff.gif",
        "../assets/images/features/top-k-diff.png": "../assets/images/3-view-modified/top-k-diff.png",
        "../assets/images/features/value-diff-detail.gif": "../assets/images/3-view-modified/value-diff-detail.gif",
        "../assets/images/features/value-diff.png": "../assets/images/3-view-modified/value-diff.png",
        
        # 4-downstream-impacts
        "../assets/images/features/cll-example.png": "../assets/images/4-downstream-impacts/cll-example.png",
        "../assets/images/features/impact-radius-1.png": "../assets/images/4-downstream-impacts/impact-radius-1.png",
        "../assets/images/features/impact-radius-2.png": "../assets/images/4-downstream-impacts/impact-radius-2.png",
        "../assets/images/features/impact-radius-3.png": "../assets/images/4-downstream-impacts/impact-radius-3.png",
        "../assets/images/features/impact-radius-legacy.png": "../assets/images/4-downstream-impacts/impact-radius-legacy.png",
        "../assets/images/features/impact-radius-single-1.png": "../assets/images/4-downstream-impacts/impact-radius-single-1.png",
        "../assets/images/features/impact-radius-single-2.png": "../assets/images/4-downstream-impacts/impact-radius-single-2.png",
        "../assets/images/features/impact-radius-single-3.png": "../assets/images/4-downstream-impacts/impact-radius-single-3.png",
        "../assets/images/features/impact-radius.png": "../assets/images/4-downstream-impacts/impact-radius.png",
        
        # 5-data-diffing
        "../assets/images/features/query-diff.gif": "../assets/images/5-data-diffing/query-diff.gif",
        "../assets/images/features/query-diff.png": "../assets/images/5-data-diffing/query-diff.png",
        
        # 6-collaboration
        "../assets/images/features/checklist.png": "../assets/images/6-collaboration/checklist.png",
        "../assets/images/recce-cloud/recce-cloud-connection-request-approved.png": "../assets/images/6-collaboration/recce-cloud-connection-request-approved.png",
        "../assets/images/recce-cloud/recce-server-use-recce-cloud-for-free.png": "../assets/images/6-collaboration/recce-server-use-recce-cloud-for-free.png",
        "../assets/images/recce-cloud/recce-share-from-cli.png": "../assets/images/6-collaboration/recce-share-from-cli.png",
        "../assets/images/recce-cloud/recce-share-from-server-fs8.png": "../assets/images/6-collaboration/recce-share-from-server-fs8.png",
        "../assets/images/recce-cloud/setting-page-api-token-fs8.png": "../assets/images/6-collaboration/setting-page-api-token-fs8.png",
        
        # 7-workflow-integration
        "../assets/images/env-prep/prep-env-clone-source.png": "../assets/images/7-workflow-integration/prep-env-clone-source.png",
        "../assets/images/env-prep/prep-env-github-pr-outdated.png": "../assets/images/7-workflow-integration/prep-env-github-pr-outdated.png",
        "../assets/images/env-prep/prep-env-limit-data-range.png": "../assets/images/7-workflow-integration/prep-env-limit-data-range.png",
        "../assets/images/env-prep/prep-env-pr-outdated.png": "../assets/images/7-workflow-integration/prep-env-pr-outdated.png",
        "../assets/images/features/preset-checks-prep.png": "../assets/images/7-workflow-integration/preset-checks-prep.png",
        "../assets/images/features/preset-checks-template.png": "../assets/images/7-workflow-integration/preset-checks-template.png",
        "../assets/images/features/preset-checks.png": "../assets/images/7-workflow-integration/preset-checks.png",
        "../assets/images/pr/ci-cd.png": "../assets/images/7-workflow-integration/ci-cd.png",
        "../assets/images/pr/copy-markdown-pr-comment.png": "../assets/images/7-workflow-integration/copy-markdown-pr-comment.png",
        "../assets/images/pr/copy-markdown.png": "../assets/images/7-workflow-integration/copy-markdown.png",
        "../assets/images/pr/lineage-dbt.png": "../assets/images/7-workflow-integration/lineage-dbt.png",
        "../assets/images/pr/lineage-diff.png": "../assets/images/7-workflow-integration/lineage-diff.png",
        "../assets/images/recce-cloud/dbt-cloud-api-trigger.png": "../assets/images/7-workflow-integration/dbt-cloud-api-trigger.png",
        "../assets/images/recce-cloud/dbt-cloud-deploy-generate-docs.png": "../assets/images/7-workflow-integration/dbt-cloud-deploy-generate-docs.png",
        "../assets/images/recce-cloud/setup-architecture.png": "../assets/images/7-workflow-integration/setup-architecture.png",
        
        # 8-lots-models
        "../assets/images/features/node-selection.png": "../assets/images/8-lots-models/node-selection.png",
        
        # 9-technical-concepts
        "../assets/images/features/state-file-dev.png": "../assets/images/9-technical-concepts/state-file-dev.png",
        "../assets/images/features/state-file-pr.png": "../assets/images/9-technical-concepts/state-file-pr.png",
        "../../assets/images/recce-cloud/sse-c.png": "../../assets/images/9-technical-concepts/sse-c.png",
        
        # Shared images (used across multiple sections)
        "../assets/images/configure-diff/environment-info.png": "../assets/images/shared/environment-info.png",
        "../assets/images/dbt-cloud/dev-artifacts.png": "../assets/images/shared/dev-artifacts.png",
        "../assets/images/dbt-cloud/login-dbt-cloud.png": "../assets/images/shared/login-dbt-cloud.png",
        "../assets/images/dbt-cloud/prod-artifacts.png": "../assets/images/shared/prod-artifacts.png",
        "../assets/images/dbt-cloud/select-run-job.png": "../assets/images/shared/select-run-job.png",
        "../assets/images/features/node.png": "../assets/images/shared/node.png",
        "../assets/images/features/state-file-save.png": "../assets/images/shared/state-file-save.png",
        "../assets/images/recce-cloud/pr-checks-all-approved.png": "../assets/images/shared/pr-checks-all-approved.png",
        
        # Archived images - different paths due to deeper nesting
        "assets/images/demo/clv-profile-diff-fs8.png": "assets/images/archived/clv-profile-diff-fs8.png",
        "assets/images/demo/clv-query-diff-fs8.png": "assets/images/archived/clv-query-diff-fs8.png",
        "assets/images/demo/clv-value-diff-fs8.png": "assets/images/archived/clv-value-diff-fs8.png",
        "assets/images/configure-diff/environment-info.png": "assets/images/shared/environment-info.png",
        "assets/images/dbt-cloud/dev-artifacts.png": "assets/images/shared/dev-artifacts.png",
        "assets/images/dbt-cloud/login-dbt-cloud.png": "assets/images/shared/login-dbt-cloud.png",
        "assets/images/dbt-cloud/prod-artifacts.png": "assets/images/shared/prod-artifacts.png",
        "assets/images/dbt-cloud/select-run-job.png": "assets/images/shared/select-run-job.png",
        "../../assets/images/recce-cloud/self-hosted-architecture.png": "../../assets/images/archived/self-hosted-architecture.png",
        "../../assets/images/recce-cloud/self-hosted-instance-lifecycle.png": "../../assets/images/archived/self-hosted-instance-lifecycle.png",
        "../assets/images/recce-cloud/app-install-authorize.png": "../assets/images/archived/app-install-authorize.png",
        "../assets/images/recce-cloud/app-install.png": "../assets/images/archived/app-install.png",
        "../assets/images/recce-cloud/branch-merged-delete-codespace.png": "../assets/images/archived/branch-merged-delete-codespace.png",
        "../assets/images/recce-cloud/check-codespace-in-github.png": "../assets/images/archived/check-codespace-in-github.png",
        "../assets/images/recce-cloud/checks.png": "../assets/images/archived/checks.png",
        "../assets/images/recce-cloud/codespace-troubleshoot-1.png": "../assets/images/archived/codespace-troubleshoot-1.png",
        "../assets/images/recce-cloud/codespace-troubleshoot-2.png": "../assets/images/archived/codespace-troubleshoot-2.png",
        "../assets/images/recce-cloud/codespaces-queued.png": "../assets/images/archived/codespaces-queued.png",
        "../assets/images/recce-cloud/create-in-codespace.png": "../assets/images/archived/create-in-codespace.png",
        "../assets/images/recce-cloud/delete-codespace-in-github.png": "../assets/images/archived/delete-codespace-in-github.png",
        "../assets/images/recce-cloud/github-token.png": "../assets/images/archived/github-token.png",
        "../assets/images/recce-cloud/ngrok-expose.png": "../assets/images/archived/ngrok-expose.png",
        "../assets/images/recce-cloud/open-codespace-in-browser.png": "../assets/images/archived/open-codespace-in-browser.png",
        "../assets/images/recce-cloud/pr-checks-wo-approved.png": "../assets/images/archived/pr-checks-wo-approved.png",
        "../assets/images/recce-cloud/query-diff.png": "../assets/images/archived/query-diff.png",
        "../assets/images/recce-cloud/recce-active.png": "../assets/images/archived/recce-active.png",
        "../assets/images/recce-cloud/recce-cloud-home.png": "../assets/images/archived/recce-cloud-home.png",
        "../assets/images/recce-cloud/recce-cloud-open-pr.png": "../assets/images/archived/recce-cloud-open-pr.png",
        "../assets/images/recce-cloud/repo-list.png": "../assets/images/archived/repo-list.png",
        "../assets/images/recce-cloud/set-prebuild-specific-regions.png": "../assets/images/archived/set-prebuild-specific-regions.png",
        "../assets/images/recce-cloud/sign-in-authorize.png": "../assets/images/archived/sign-in-authorize.png",
        "../assets/images/recce-cloud/sign-in.png": "../assets/images/archived/sign-in.png",
        "../assets/images/recce-cloud/tailscale-dashboard-fs8.png": "../assets/images/archived/tailscale-dashboard-fs8.png",
        "../assets/images/recce-cloud/tailscale-expose.png": "../assets/images/archived/tailscale-expose.png",
    }
    
    # Process all markdown files in the docs directory
    docs_path = Path("docs")
    updated_files = 0
    total_replacements = 0
    
    for md_file in docs_path.rglob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        file_replacements = 0
        
        for old_path, new_path in path_mappings.items():
            if old_path in content:
                content = content.replace(old_path, new_path)
                count = original_content.count(old_path)
                file_replacements += count
                print(f"  ✅ {md_file.relative_to(docs_path)}: {old_path} → {new_path} ({count} times)")
        
        if content != original_content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_files += 1
            total_replacements += file_replacements
            print(f"📝 Updated {md_file.relative_to(docs_path)} ({file_replacements} replacements)")
    
    print(f"\n📊 Summary: {updated_files} files updated with {total_replacements} path replacements")

if __name__ == "__main__":
    update_image_paths()