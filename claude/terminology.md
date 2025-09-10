# Recce Documentation Terminology Guide

This guide helps maintain consistent, data-team-friendly language across all Recce documentation.

## Core Philosophy

**Data teams think data-first, code-second.** Our terminology should reflect their mental models and avoid software engineering jargon that creates confusion.

## Preferred Terminology

### Recce-Specific Terms

| **Use This** | **Not This** | **Context** |
|-------------|-------------|-------------|
| **Recce instance** | Recce server, Recce app | The UI launched by `recce server` |
| **data validation** | data testing, data quality checks | Primary concept for what Recce does |
| **validation results** | diff output, comparison data | What users see in Recce |
| **impact analysis** | dependency analysis, lineage | Understanding downstream effects |
| **data changes** | code changes, model changes | What users are validating |
| **code change** | code modification | Specific term for data team workflows |
| **validation workflow** | testing workflow, QA process | How teams use Recce |
| **diff** | comparison, delta | Data teams familiar with git diff, use freely |
| **state file** | session file, cache | Stores validation results and checks for later use |
| **preset checks** | default tests, template checks | Pre-configured validation rules for projects |
| **lineage diff** | dependency comparison | Visual comparison of model relationships |
| **breaking change analysis** | impact assessment | Automated detection of schema changes |
| **value diff** | data comparison | Row-by-row data validation between environments |
| **profile diff** | summary statistics | Column-level statistical comparisons |
| **histogram diff** | distribution analysis | Numeric data distribution comparisons |
| **top-K diff** | frequency analysis | Categorical data frequency comparisons |
| **row count diff** | record count validation | Quick data volume verification |
| **Recce**| recce | this is the brand name, should always use "Recce" | 
| **dbt** | DBT | this is the brand name, should always use lower cases| 


### Data vs Software Terms

| **Data Team Friendly** | **Software Term** | **Why Different** |
|------------------------|-------------------|-------------------|
| **data warehouse** | database | Data teams distinguish warehouses from operational databases |
| **development stage** | environment | "Environment" confuses (warehouse vs dev/prod) |
| **data models** | components | dbt models vs software components |
| **model** | node | Data teams think "model", software teams think "node" |
| **release changes** | deploy | Data teams "release" changes, don't "deploy" infrastructure |
| **validation checks** | unit tests | Data quality checks vs code functionality tests |
| **automated validation** | CI/CD pipeline | Data processing vs deployment automation |
| **change review** | code review | Reviewing data changes vs code changes |
| **diff** | comparison | Data teams understand diff from git/version control |
| **artifacts** | build outputs | dbt manifest.json, catalog.json files |
| **run dbt** | execute dbt, build models | Preferred: "run dbt" not "execute" or "build" |
| **materialization** | table creation strategy | How dbt creates tables (table, view, incremental) |
| **dbt target** | environment config | profiles.yml target configuration |
| **warehouse connection** | database connection | Data team context for connecting to warehouse |
| **development workspace** | dev environment | Where data analysts work on models |
| **production workspace** | prod environment | Live data warehouse with production data |

### Business Impact Language

| **Business Focused** | **Technical Focused** | **Impact** |
|---------------------|----------------------|------------|
| **build trust** | ensure quality | Emphasizes outcome over process |
| **catch issues early** | prevent bugs | Prevention focus, business consequences |
| **confident releases** | successful deployments | User empowerment over technical success |
| **team collaboration** | workflow integration | People-first over tool-first |
| **validate changes** | test modifications | Active validation vs passive testing |
| **validation checklist** | test suite | Collaborative validation workflow for teams |
| **share findings** | distribute results | Team collaboration on validation results |
| **review together** | collaborate on validation | Team-based change review process |
| **check status** | test results | Current state of validation checks |
| **approve changes** | sign off on deployment | Business approval vs technical deployment |

## Terms That Confuse Data Teams

### 🚨 High Confusion Terms

**Environment**
- **Data team thinks**: Snowflake vs BigQuery warehouse
- **Software team thinks**: dev/staging/prod deployment target
- **✅ Use instead**: "development stage" or "dbt target"

**Deploy**
- **Data team thinks**: Infrastructure deployment (not their job)
- **Software team thinks**: Release code changes
- **✅ Use instead**: "release changes" or "make live"

**Pipeline**
- **Data team thinks**: Data transformation workflow (dbt run)
- **Software team thinks**: CI/CD automation workflow
- **✅ Use instead**: "data pipeline" vs "automation workflow"

**Testing**
- **Data team thinks**: Data quality validation
- **Software team thinks**: Unit/integration tests for code
- **✅ Use instead**: "validation" or "data quality checks"

**Build**
- **Data team thinks**: "dbt run" - executing transformations
- **Software team thinks**: Compile/package application
- **✅ Use instead**: "run models" or "execute transformations"

**Server**
- **Data team thinks**: Database server (Snowflake, BigQuery)
- **Software team thinks**: Web server or application server
- **✅ Use instead**: "Recce UI" or "Recce interface" for the tool

### ⚠️ Medium Confusion Terms

**Model**
- **Data context**: dbt data model (SQL transformation)
- **Software context**: Software component or data structure
- **✅ Clarify**: Always use "dbt model" or "data model"

**Schema** 
- **Data context**: Database schema (namespace for tables)
- **Software context**: Data structure definition
- **✅ Clarify**: "database schema" vs "data structure"

**Target**
- **Data context**: dbt profile target (dev/prod warehouse config)
- **Software context**: Deployment target or goal
- **✅ Clarify**: "dbt target" when referring to profiles.yml

**Artifacts**
- **Data context**: dbt-generated metadata files (manifest.json, catalog.json)
- **Software context**: Build outputs, compiled binaries
- **✅ Clarify**: "dbt artifacts" or "metadata files"

**Workspace**
- **Data context**: Development area in data warehouse
- **Software context**: IDE or development environment
- **✅ Clarify**: "development workspace" vs "local workspace"

**Instance**
- **Data context**: Recce UI session or warehouse instance
- **Software context**: Running application or server
- **✅ Clarify**: "Recce session" or "warehouse connection"

## Terminology Alert System

When reviewing documentation, flag confusing terms with this format:

```
⚠️ **Terminology Alert**: [TERM]
- **Confusion risk**: [Why data teams might misunderstand]
- **Current usage**: [How it appears in content]
- **Suggested clarification**: [Better phrasing or explanation]
- **Context needed**: [When to add explanation]
```

### Examples

```
⚠️ **Terminology Alert**: "Deploy your changes"
- **Confusion risk**: Data teams think infrastructure deployment
- **Current usage**: "Deploy your dbt changes to production"
- **Suggested clarification**: "Release your data changes to production"
- **Context needed**: Always in data change contexts
```

```
⚠️ **Terminology Alert**: "Test environment" 
- **Confusion risk**: Could mean test warehouse vs test deployment stage
- **Current usage**: "Run Recce in your test environment"
- **Suggested clarification**: "Run Recce against your development data warehouse"
- **Context needed**: When referring to data warehouse setup
```

## Clarification Patterns

### Pattern 1: Define on First Use
```markdown
Recce validates your **data changes** (modifications to dbt models, seeds, or configurations) before they impact production.
```

### Pattern 2: Use Data Analogies
```markdown
Just like code reviews catch bugs before production, data validation catches issues before they affect business metrics.
```

### Pattern 3: Contrast Software vs Data
```markdown
While software teams deploy applications, data teams release model changes to their warehouse.
```

### Pattern 4: Add Contextual Clarifiers
```markdown
Configure your dbt target (the warehouse connection in profiles.yml) to point to your development environment.
```

## Conflicting Usage Patterns

These terms are used inconsistently across the documentation, creating potential confusion. Document conflicts here without changing the content immediately.

### 🔀 Terms Used Inconsistently

**"Environment" vs "Target" vs "Workspace"**
- **Data team perspective**: "Target" refers to dbt profiles.yml config, "Environment" means warehouse type (Snowflake vs BigQuery)
- **Software team perspective**: "Environment" means dev/staging/prod deployment context
- **Current usage in docs**: Mixed usage - sometimes "environment" for dbt targets, sometimes for deployment stages
- **Recommendation**: Use "dbt target" for profiles.yml, "development workspace" for where analysts work

**"Check" vs "Validation" vs "Test"**
- **Data team perspective**: "Validation" sounds more professional than "testing", "checks" are specific validations
- **Software team perspective**: "Tests" are automated code verification, "checks" are CI/CD gates
- **Current usage in docs**: Mixed - "preset checks", "validation workflow", "test your models"
- **Recommendation**: Standardize on "validation" for data quality, "checks" for specific validation rules

**"Build" vs "Run" vs "Execute"**
- **Data team perspective**: "Run dbt" is the standard command, "build" sounds like compiling code
- **Software team perspective**: "Build" means compile/package, "execute" means run program
- **Current usage in docs**: Mixed usage - "build your models", "run dbt", "execute transformations"
- **Recommendation**: Use "run" for dbt operations, avoid "build" and "execute"

**"Review" vs "Audit" vs "Validation"**
- **Data team perspective**: "Review" is collaborative, "audit" is formal compliance checking
- **Software team perspective**: "Review" is code review process, "audit" is security scanning
- **Current usage in docs**: "Review mode", "change review", "validation workflow"
- **Recommendation**: Use "review" for collaborative processes, "validation" for automated checks

**"Pipeline" vs "Workflow"**
- **Data team perspective**: "Pipeline" means data transformation flow (dbt models)
- **Software team perspective**: "Pipeline" means CI/CD automation pipeline
- **Current usage in docs**: "CI/CD pipeline", "validation workflow", "automation workflow"
- **Recommendation**: "Data pipeline" for transformations, "automation workflow" for CI/CD

**"Deploy" vs "Release" vs "Publish"**
- **Data team perspective**: "Release" means making changes live, "deploy" sounds like infrastructure
- **Software team perspective**: "Deploy" means publish application, "release" means version release
- **Current usage in docs**: Mixed - "deploy changes", "release changes", "publish results"
- **Recommendation**: Use "release" for data changes, "deploy" only for infrastructure

## Maintenance Guidelines

### Adding New Terms
When introducing new terminology:
1. **Check for confusion potential** - Could data teams misunderstand?
2. **Define immediately** - Explain on first use
3. **Use consistently** - Same term for same concept throughout
4. **Add to this guide** - Update the preferred terminology table

### Regular Reviews
- **Monthly**: Review user questions for terminology confusion
- **Quarterly**: Update based on support feedback and user research
- **Major releases**: Ensure new features use data-team-friendly language

### Quality Checks
Before publishing, verify:
- [ ] **No undefined jargon** - All technical terms explained
- [ ] **Consistent usage** - Same term used throughout
- [ ] **Data team perspective** - Language matches their mental models
- [ ] **Context provided** - Clarification when terms could be ambiguous

## Quick Reference: Common Replacements

| **Instead of...** | **Use...** | **Context** |
|------------------|------------|-------------|
| "Deploy changes" | "Release changes" | Data modifications |
| "Test your models" | "Validate your models" | Data quality checking |
| "Environment setup" | "Warehouse connection setup" | Database configuration |
| "CI/CD pipeline" | "Automated validation workflow" | Recce automation |
| "Unit tests" | "Model validation checks" | dbt testing |
| "Production deployment" | "Production release" | Making changes live |
| "Development environment" | "Development warehouse" | Where you develop |
| "Code review" | "Change review" | Reviewing data modifications |
| "Build models" | "Run models" | dbt model execution |
| "Execute dbt" | "Run dbt" | Standard dbt command usage |
| "Check results" | "Validation status" | Status of data validation |
| "Recce server" | "Recce interface" | The UI tool itself |
| "Database connection" | "Warehouse connection" | Data team context |

---

**Remember**: When in doubt, choose the term that a data analyst (not a software engineer) would immediately understand. Clarity builds trust and reduces barriers to adoption.