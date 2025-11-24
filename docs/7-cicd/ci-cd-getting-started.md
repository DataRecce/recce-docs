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

Recce currently integrates with both GitHub Actions and GitLab CI/CD. If you use another CI/CD product and interested in Recce, [let us know](https://cal.com/team/recce/chat).

## Prerequisites

Before setting up, ensure you have:

- **Recce Cloud account** You can signup and start your free trial [here](https://cloud.reccehq.com/)
- **Repository connected** to Recce Cloud ([setup guide](../2-getting-started/start-free-with-cloud.md#git-integration))
- **dbt artifacts generated** (`manifest.json` and `catalog.json`) from your project

### GitHub
If your dbt project uses GitHub:

1. [Setup CD](./github/setup-cd.md) - Auto-update baseline on merge to main
2. [Setup CI](./github/setup-ci.md) - Auto-validate changes in every PR

### GitLab
If your dbt project uses GitLab:

1. [Setup CD](./gitlab/setup-cd.md) - Auto-update baseline on merge to main
2. [Setup CI](./gitlab/setup-ci.md) - Auto-validate changes in every MR
3. [GitLab Personal Access Token Guide](./gitlab/gitlab-pat-guide.md) - Required for GitLab integration

## Next steps

1. Start with relevant CD setup ([GitLab](./gitlab/setup-cd.md) or [GitHub](./github/setup-cd.md)) to establish automatic baseline (production artifacts) updates.
2. Configure CI setup ([GitLab](./gitlab/setup-ci.md) or [GitHub](./github/setup-ci.md)) to enable PR/MR validation
3. Review [best practices](./best-practices-prep-env.md) for environment preparation

## Related workflows

After setting up CI/CD automation, explore these workflow guides:

- [Development workflow](./scenario-dev.md) - How to validate data impact during development (pre-PR/MR)
- [PR/MR review workflow](./scenario-pr-review.md) - How to collaborate with teammates using Recce in PRs/MRs
- [Preset checks](./preset-checks.md) - How to configure automatic validation checks
