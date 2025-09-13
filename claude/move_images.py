#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

def move_images():
    """Move images to their appropriate section folders based on usage analysis."""
    
    base_path = Path("docs/assets/images")
    
    # Define the moves based on our analysis
    moves = {
        # 1-whats-recce
        "home/checklist-readme3.png": "1-whats-recce/checklist-readme3.png",
        "home/diff-readme2.png": "1-whats-recce/diff-readme2.png", 
        "home/lineage-readme1.png": "1-whats-recce/lineage-readme1.png",
        
        # 2-getting-started
        "jaffle-shop/jaffle_shop_check.png": "2-getting-started/jaffle_shop_check.png",
        "jaffle-shop/jaffle_shop_lineage.png": "2-getting-started/jaffle_shop_lineage.png",
        "jaffle-shop/jaffle_shop_query.png": "2-getting-started/jaffle_shop_query.png",
        
        # 3-view-modified (already exists, but move more features there)
        "features/actions-dropdown.png": "3-view-modified/actions-dropdown.png",
        "features/actions-menu.png": "3-view-modified/actions-menu.png",
        "features/add-to-checklist-button.png": "3-view-modified/add-to-checklist-button.png",
        "features/add-to-checklist.gif": "3-view-modified/add-to-checklist.gif",
        "features/clipboard-to-github.gif": "3-view-modified/clipboard-to-github.gif",
        "features/cll-1.png": "3-view-modified/cll-1.png",
        "features/cll-2.png": "3-view-modified/cll-2.png",
        "features/cll-3.png": "3-view-modified/cll-3.png",
        "features/code-diff.png": "3-view-modified/code-diff.png",
        "features/histogram-diff.gif": "3-view-modified/histogram-diff.gif",
        "features/histogram-diff.png": "3-view-modified/histogram-diff.png",
        "features/lineage-diff.gif": "3-view-modified/lineage-diff.gif",
        "features/model-schema-change-detected.png": "3-view-modified/model-schema-change-detected.png",
        "features/multi-node-row-count-diff.gif": "3-view-modified/multi-node-row-count-diff.gif",
        "features/multi-node-selection.gif": "3-view-modified/multi-node-selection.gif",
        "features/multi-node-value-diff.gif": "3-view-modified/multi-node-value-diff.gif",
        "features/node-details-panel.gif": "3-view-modified/node-details-panel.gif",
        "features/profile-diff.png": "3-view-modified/profile-diff.png",
        "features/row-count-diff-selector.gif": "3-view-modified/row-count-diff-selector.gif",
        "features/row-count-diff-single.gif": "3-view-modified/row-count-diff-single.gif",
        "features/schema-diff.gif": "3-view-modified/schema-diff.gif",
        "features/schema-diff.png": "3-view-modified/schema-diff.png",
        "features/select-node-children.gif": "3-view-modified/select-node-children.gif",
        "features/top-k-diff.gif": "3-view-modified/top-k-diff.gif",
        "features/top-k-diff.png": "3-view-modified/top-k-diff.png",
        "features/value-diff-detail.gif": "3-view-modified/value-diff-detail.gif",
        "features/value-diff.png": "3-view-modified/value-diff.png",
        
        # 4-downstream-impacts
        "features/cll-example.png": "4-downstream-impacts/cll-example.png",
        "features/impact-radius-1.png": "4-downstream-impacts/impact-radius-1.png",
        "features/impact-radius-2.png": "4-downstream-impacts/impact-radius-2.png",
        "features/impact-radius-3.png": "4-downstream-impacts/impact-radius-3.png",
        "features/impact-radius-legacy.png": "4-downstream-impacts/impact-radius-legacy.png",
        "features/impact-radius-single-1.png": "4-downstream-impacts/impact-radius-single-1.png",
        "features/impact-radius-single-2.png": "4-downstream-impacts/impact-radius-single-2.png",
        "features/impact-radius-single-3.png": "4-downstream-impacts/impact-radius-single-3.png",
        "features/impact-radius.png": "4-downstream-impacts/impact-radius.png",
        
        # 5-data-diffing
        "features/query-diff.gif": "5-data-diffing/query-diff.gif",
        "features/query-diff.png": "5-data-diffing/query-diff.png",
        
        # 6-collaboration
        "features/checklist.png": "6-collaboration/checklist.png",
        "recce-cloud/recce-cloud-connection-request-approved.png": "6-collaboration/recce-cloud-connection-request-approved.png",
        "recce-cloud/recce-server-use-recce-cloud-for-free.png": "6-collaboration/recce-server-use-recce-cloud-for-free.png",
        "recce-cloud/recce-share-from-cli.png": "6-collaboration/recce-share-from-cli.png",
        "recce-cloud/recce-share-from-server-fs8.png": "6-collaboration/recce-share-from-server-fs8.png",
        "recce-cloud/setting-page-api-token-fs8.png": "6-collaboration/setting-page-api-token-fs8.png",
        
        # 7-workflow-integration
        "env-prep/prep-env-clone-source.png": "7-workflow-integration/prep-env-clone-source.png",
        "env-prep/prep-env-github-pr-outdated.png": "7-workflow-integration/prep-env-github-pr-outdated.png",
        "env-prep/prep-env-limit-data-range.png": "7-workflow-integration/prep-env-limit-data-range.png",
        "env-prep/prep-env-pr-outdated.png": "7-workflow-integration/prep-env-pr-outdated.png",
        "features/preset-checks-prep.png": "7-workflow-integration/preset-checks-prep.png",
        "features/preset-checks-template.png": "7-workflow-integration/preset-checks-template.png",
        "features/preset-checks.png": "7-workflow-integration/preset-checks.png",
        "pr/ci-cd.png": "7-workflow-integration/ci-cd.png",
        "pr/copy-markdown-pr-comment.png": "7-workflow-integration/copy-markdown-pr-comment.png",
        "pr/copy-markdown.png": "7-workflow-integration/copy-markdown.png",
        "pr/lineage-dbt.png": "7-workflow-integration/lineage-dbt.png",
        "pr/lineage-diff.png": "7-workflow-integration/lineage-diff.png",
        "recce-cloud/dbt-cloud-api-trigger.png": "7-workflow-integration/dbt-cloud-api-trigger.png",
        "recce-cloud/dbt-cloud-deploy-generate-docs.png": "7-workflow-integration/dbt-cloud-deploy-generate-docs.png",
        "recce-cloud/setup-architecture.png": "7-workflow-integration/setup-architecture.png",
        
        # 8-lots-models
        "features/node-selection.png": "8-lots-models/node-selection.png",
        
        # 9-technical-concepts
        "features/state-file-dev.png": "9-technical-concepts/state-file-dev.png",
        "features/state-file-pr.png": "9-technical-concepts/state-file-pr.png",
        "recce-cloud/sse-c.png": "9-technical-concepts/sse-c.png",
        
        # archived
        "demo/clv-profile-diff-fs8.png": "archived/clv-profile-diff-fs8.png",
        "demo/clv-query-diff-fs8.png": "archived/clv-query-diff-fs8.png",
        "demo/clv-value-diff-fs8.png": "archived/clv-value-diff-fs8.png",
    }
    
    # Images used in multiple sections - keep in shared
    shared_images = {
        "configure-diff/environment-info.png": "shared/environment-info.png",
        "dbt-cloud/dev-artifacts.png": "shared/dev-artifacts.png",
        "dbt-cloud/login-dbt-cloud.png": "shared/login-dbt-cloud.png",
        "dbt-cloud/prod-artifacts.png": "shared/prod-artifacts.png",
        "dbt-cloud/select-run-job.png": "shared/select-run-job.png",
        "features/node.png": "shared/node.png",
        "features/state-file-save.png": "shared/state-file-save.png",
        "recce-cloud/pr-checks-all-approved.png": "shared/pr-checks-all-approved.png",
    }
    
    # Move archived recce-cloud images
    archived_recce_cloud = [
        "recce-cloud/app-install-authorize.png",
        "recce-cloud/app-install.png", 
        "recce-cloud/branch-merged-delete-codespace.png",
        "recce-cloud/check-codespace-in-github.png",
        "recce-cloud/checks.png",
        "recce-cloud/codespace-troubleshoot-1.png",
        "recce-cloud/codespace-troubleshoot-2.png",
        "recce-cloud/codespaces-queued.png",
        "recce-cloud/create-in-codespace.png",
        "recce-cloud/delete-codespace-in-github.png",
        "recce-cloud/github-token.png",
        "recce-cloud/ngrok-expose.png",
        "recce-cloud/open-codespace-in-browser.png",
        "recce-cloud/pr-checks-wo-approved.png",
        "recce-cloud/query-diff.png",
        "recce-cloud/recce-active.png",
        "recce-cloud/recce-cloud-home.png",
        "recce-cloud/recce-cloud-open-pr.png",
        "recce-cloud/repo-list.png",
        "recce-cloud/self-hosted-architecture.png",
        "recce-cloud/self-hosted-instance-lifecycle.png",
        "recce-cloud/set-prebuild-specific-regions.png",
        "recce-cloud/sign-in-authorize.png",
        "recce-cloud/sign-in.png",
        "recce-cloud/tailscale-dashboard-fs8.png",
        "recce-cloud/tailscale-expose.png",
    ]
    
    for img in archived_recce_cloud:
        filename = os.path.basename(img)
        moves[img] = f"archived/{filename}"
    
    # Perform moves
    moves.update(shared_images)
    
    total_moves = 0
    successful_moves = 0
    
    for source_path, dest_path in moves.items():
        source_full = base_path / source_path
        dest_full = base_path / dest_path
        
        total_moves += 1
        
        if source_full.exists():
            # Create destination directory if it doesn't exist
            dest_full.parent.mkdir(parents=True, exist_ok=True)
            
            try:
                shutil.move(str(source_full), str(dest_full))
                print(f"✅ Moved: {source_path} → {dest_path}")
                successful_moves += 1
            except Exception as e:
                print(f"❌ Error moving {source_path}: {e}")
        else:
            print(f"⚠️ Source not found: {source_path}")
    
    print(f"\n📊 Summary: {successful_moves}/{total_moves} images moved successfully")

if __name__ == "__main__":
    move_images()