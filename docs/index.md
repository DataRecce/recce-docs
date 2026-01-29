# What is Recce (Data Review Agent)

Know exactly how code changes impact your data.

Recce is a Data Review Agent that automates data validation for pull requests. When you open a PR, it compares your dev environment against production and surfaces schema changes, data diffs, row counts, and downstream impacts. You see what changed, what it affects, and what passed, all before you merge.

No more merging PRs where the pipeline succeeded but the data is quietly wrong.

## How Recce Works

When you open a PR with data changes, Recce automatically:

1. **Runs data diffing:** The best practice to validate data changes
2. **Analyzes impact:** Identifies what changed down to the column level using Column-Level Lineage (CLL)
3. **Reviews first:** The agent provides a data review summary explaining the change and its impact
4. **Surfaces what matters:** Shows only impacted items, not every downstream table
5. **Opens exploration:** Spins up a Recce instance where you can run additional diffs, explore lineage, and investigate deeper

You review the agent's findings, add notes, and approve with confidence, not blind trust.

![How Recce Works](assets/images/1-whats-recce/how-recce-work.png)

1. PR Created
2. Recce Triggered
3. Agent Analyzes Production vs. Development Data 
4. Agent Generates Review Summary
5. Human Explore in Recce Instance
6. Human Reviews Approves
7. PR Merges


Example of Recce agent summary in a GitHub PR comment: 
![How Recce Works](assets/images/1-whats-recce/agent-data-review-example.png)

## Automate Agent Data Review with CI/CD

Recce delivers value through CI/CD integration. Without it, you waste time triaging false alerts from source data updates and manually comparing environments hoping you caught everything.

With CI/CD:

- Every PR gets automatic validation
- Base and current environments are set up automatically
- Agent reviews before you do
- Checks accumulate as organizational knowledge (preset checks)

## When to Use Recce

- **Business-critical data:** Data that's customer-facing or revenue-impacting
- **Team collaboration:** When reviewers need to understand impact, not just see code changes
- **Standardized validation:** When you need consistent review across senior and junior team members
- **Unknown unknowns:** When you can't predict what might break from a change

## When Not to Use

- Teams that accept errors on production and fix later
- Exploratory analysis that won't go to production

## FAQ

**Does Recce work without CI/CD?**
Yes, you can run Recce locally for dev sessions. But CI/CD unlocks the full value: automatic validation on every PR without manual setup.

**What data platforms does Recce support?**
Recce works with data warehouses like Snowflake, BigQuery, Redshift, and Databricks. See [Connect to Warehouse](5-data-diffing/connect-to-warehouse/) for setup.

## Related
- Interactive Demo: [Try the Data Review Agent](https://reccehq.com/demo/)
- Tutorial: [Get Started with Recce Cloud](2-getting-started/start-free-with-cloud/)
- Blog: [The Problem with Data PR Reviews: Where Do You Even Start?](https://blog.reccehq.com/guided-data-review)
