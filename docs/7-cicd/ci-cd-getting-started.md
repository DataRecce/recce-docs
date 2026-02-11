---
title: CI/CD Getting Started
---

# CI/CD Getting Started

Automate data validation in your development workflow. Catch data issues before they reach production with continuous integration and delivery built specifically for dbt projects.

## What you'll achieve

Set up automated workflows that:

- **Save time on reviews** - Eliminate manual validation steps for every change
- **Run data validations on every pull request/merge request** - Run data validation checks automatically when changes are proposed
- **Prevent regressions** - Catch data quality issues before they reach production

!!!note
    CI/CD automation requires a Cloud Plan. Get started for free [here](https://cloud.reccehq.com/).

## What is CI/CD? 

Recce uses both continuous integration (CI) and continuous delivery (CD) to automate data validation:

**Continuous Integration (CI)**

- **When**: Runs when you open a new or update a Pull Request/Merge Request 
- **Purpose**: Validates proposed changes against baseline (typically this mean production)
- **Benefit**: Catches issues before merge, with results in your PR/MR

**Continuous Delivery (CD)**

- **When**: Runs after merge to main branch
- **Purpose**: Updates baseline artifacts Recce uses to with latest production state
- **Benefit**: Ensures future comparisons use current baseline

## What does look like with Recce?

Both CI and CD workflows follow the same pattern:

1. **Trigger event** (merge to main, or PR/MR opened/updated)
2. **Generate dbt artifacts** (`dbt docs generate` or external source)
3. **Upload to Recce Cloud** (automatic via workflow action)
4. **Validation results** appear in Recce dashboard and PR/MR

<figure markdown>
  ![Recce CI/CD architecture](../assets/images/7-cicd/ci-cd.png){: .shadow}
  <figcaption>Automated validation workflow for pull requests</figcaption>
</figure>

## Getting Started with your CI/CD

Recce integrates with both GitHub Actions and GitLab CI/CD using the lightweight `recce-cloud` CLI. If you use another CI/CD platform and are interested in Recce, [let us know](https://cal.com/team/recce/chat).

## Prerequisites

Before setting up, ensure you have:

- ✅ **Recce Cloud account** - [Start free trial](https://cloud.reccehq.com/)
- ✅ **Repository connected** to Recce Cloud - [Connect Git Provider](../2-getting-started/start-free-with-cloud.md#2-connect-git-provider)
  - For GitLab: [Create a Personal Access Token](../2-getting-started/gitlab-pat-guide.md) if not already done
- ✅ **dbt artifacts** - Know how to generate `manifest.json` and `catalog.json` from your project

## Setup Steps

Both GitHub and GitLab follow the same simple pattern:

### 1. Setup CD - Auto-update baseline
[**Setup CD Guide**](./setup-cd.md) - Configure automatic baseline updates when you merge to main

- Updates your production baseline artifacts automatically
- Runs on merge to main + optional scheduled updates
- Works with both GitHub Actions and GitLab CI/CD

### 2. Setup CI - Auto-validate PRs/MRs
[**Setup CI Guide**](./setup-ci.md) - Enable automatic validation for every PR/MR

- Validates data changes in every pull request or merge request
- Catches issues before they reach production
- Works with both GitHub Actions and GitLab CI/CD

## Why This Order?

Start with **CD first** to establish your baseline (production artifacts), then add **CI** for PR/MR validation. CI validation compares your PR/MR changes against the baseline created by CD.

## Next Steps

1. **[Setup CD](./setup-cd.md)** - Establish automatic baseline updates
2. **[Setup CI](./setup-ci.md)** - Enable PR/MR validation
3. Review [best practices](./best-practices-prep-env.md) for environment preparation

## Related workflows

After setting up CI/CD automation, explore these workflow guides:

- [Development workflow](./scenario-dev.md) - How to validate data impact during development (pre-PR/MR)
- [PR/MR review workflow](./scenario-pr-review.md) - How to collaborate with teammates using Recce in PRs/MRs
- [Preset checks](./preset-checks.md) - How to configure automatic validation checks
