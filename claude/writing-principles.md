# Writing Principles for Recce Documentation

This guide establishes strategic writing standards for Recce documentation.

## Documentation Goals

The Recce Documentation guides data practitioners from understanding the value of systematic data validation to successfully implementing confident, collaborative workflows.

## Writing Principles

### 1. User Outcomes
Help users succeed quickly, master workflows that fit their team, and scale from individual to team adoption—always focusing on business value over technical complexity.

### 2. Core Principles
Every page should reinforce that Recce enables **collaboration**, keeps **humans in the loop**, streamlines **efficiency**, builds **transparency**, and **prevents issues** early in the development workflow to build **trust**.

### 3. Audience-First 

Data practitioners care about data first, code is just their tool. 

We consider three types of audiences:
1. **ICP (Ideal Customer Profiles)** - Business segments by company needs and budget
2. **Data Roles** - Job functions (analysts, engineers, stakeholders) regardless of exact titles
3. **Review Process Roles** - Whether someone authors or reviews data changes

**Writing Focus**: Based on our ICPs, we write primarily for analysts and engineers. For review processes, we assume authors (not reviewers) read our documentation, though often the same person plays both roles.

Our documentation prioritizes three ICPs:
1. Cloud-Native Users (Primary Focus)**
   - **Choose the Right Path**: Understand OSS vs Cloud options and migrate seamlessly when ready
   **Profile**: Data teams who use Recce Cloud directly without OSS experience
   - **Background**: Data-focused professionals, not software engineers
   - **Characteristics**: 
     - Data is core to their business (financial services, healthcare, e-commerce)
     - Have budget and prefer SaaS solutions
     - Want easy team adoption without setup complexity
     - Expect product + support to handle implementation challenges
   - **Documentation Needs**: 
     - Start with Cloud features and benefits
     - Minimize technical complexity
     - Focus on business outcomes and team collaboration
     - Clear, simple onboarding paths
2. OSS-to-Cloud Migration (Secondary Focus)**
  **Profile**: Teams who started with OSS but now need Cloud features
  - **Background**: Initially technical enough for OSS, but situations changed
  - **Characteristics**:
    - Lost technical team members or capability
    - Strategy shift toward core business focus
    - Hit feature limitations requiring Cloud
    - Now have budget for premium tools
  - **Documentation Needs**:
    - Smooth migration paths from OSS workflows
    - Clear Cloud upgrade benefits
    - Preserve existing knowledge while adding capabilities
1. OSS-Only Users (Tertiary Focus)
  **Profile**: Technical teams committed to open source solutions
  - **Background**: Strong software engineering or technical ops experience
  - **Characteristics**:
    - Data validation supports engineering best practices
    - Need customization and control
    - Active in open source communities
    - No budget for premium tools
  - **Documentation Needs**:
    - Self-service technical documentation
    - Advanced configuration and customization guides
    - Community contribution pathways

### 4. Cloud-Native First Strategy
- **Default Path**: Always present Cloud as primary solution. Since cloud is simple setup and team collaboration

### 5. Bridge Software Engineering & Data
**Translate software practices using data team language**
- Use data team vocabulary, explain software engineering terms
- Connect validation to data quality and business trust
- Use data workflow analogies (data testing, quality checks, impact analysis)
- Position as natural evolution for growing data teams
- Prioritize data concepts over software engineering terminology
- Explain technical terms when necessary
- Use business impact language (trust, confidence, risk reduction)
- Focus on workflow integration, not tool complexity
- **Technical Depth**: Link to advanced topics rather than inline complexity


### 6. Clear & Concise
Write everything as clearly and briefly as possible. Simplicity builds trust and reduces barriers to adoption. 

### 7. Consistent Terminology
Use data-team-friendly language and maintain consistency. See [terminology.md](./terminology.md) for complete guidance.

**Key principles**:
- Use "Recce instance" for the UI launched by `recce server`
- Prefer "data validation" over "data testing"
- Use "development stage" instead of "environment" when referring to dev/prod
- Choose terms data analysts understand immediately

## Tone & Voice Guidelines

Our voice embodies the five strategic principles through confident, practical communication:

### **Lower Barriers to Entry Voice**
- **Welcoming**: "You're in the right place" rather than "This might be complex"
- **Accessible**: Use common data concepts and familiar dbt concepts to explain new validation ideas
- **Supportive**: Multiple pathways without overwhelming choice
- **Encouraging**: "You've got this" messaging throughout

### **Confidence & Authority**
Always use positive and condidnece tone. 
```markdown
✅ "Here's how to set up systematic validation for your team"
✅ "This approach catches 90% of downstream issues before production"
✅ "You'll have validation results in under 5 minutes"
✅ "Your team will see immediate benefits from this workflow"
```

Avoid Uncertainty Language, like: 
```markdown
❌ "You might want to try this approach if you think it could work"
❌ "This should probably work in most cases"
❌ "Advanced users might be able to figure this out"
❌ "If you're comfortable with technical concepts..."
```

### **Bridge Software Engineering & Data Voice**
- **Translational**: "Just like PR reviews for code, Recce reviews for data"
- **Familiar**: Use software development analogies data teams already understand
- **Evolutionary**: Position as natural next step, not radical change
- **Professional**: Match the sophistication of software engineering tools

### **Shift-Left Philosophy Voice**
- **Prevention-focused**: "Catch issues early" rather than "fix problems later"
- **Confidence-building**: Validation as empowerment, not extra burden
- **Workflow-integrated**: "Built into your development process"
- **Value-oriented**: Emphasize time and trust savings

### **Collaborative Workflows Voice**
- **Team-centric**: "Your team" and "together" language
- **Role-inclusive**: Acknowledge different perspectives and expertise
- **Trust-building**: Shared understanding and confidence
- **Scaling-aware**: Individual success → team success progression


## Navigation 
Maintain consistency with the 9-section structure:
1. **What's Recce** - Introduction, value proposition, use cases
2. **Getting Started** - Installation, tutorials, first steps
3. **Visualized Change** - Core functionality, diff analysis
4. **Downstream Impacts** - Impact analysis, dependency mapping
5. **Data Diffing** - Query comparison, validation techniques
6. **Collaborate Validation** - Team workflows, checklist management
7. **CI/CD** - CI/CD, automation, best practices
8. **Technical Concepts** - Architecture, configuration

These structure is to align users adoption process. Start from using in PR, colloaborate with team, and using in dev time. And know more technical behind it. 



## Content format guide

1. **Use markdown** for all content formatting
2. **Add line breaks** between sentences and bullet points or numbered lists to ensure proper rendering
3. **Page title capitalization**: Capitalize every word in the main page title (Title Case)
4. **Heading capitalization**: For H2 headings and below, only capitalize the first word (Sentence case)
5. **Image format**: Use the standardized figure format with shadow styling:

```markdown
<figure markdown>
  ![Recce Lineage Diff](../assets/images/3-view-modified/lineage-diff.gif){: .shadow}
  <figcaption>Interactive lineage graph showing modified models</figcaption>
</figure>
```
6. Use bold only when it's neccessary. Too many highlight will lose focus and not easy to read. 

### Page Structure Template
```markdown
---
title: [Descriptive Title]
---

# [H1 Title - matches page title]

[Brief introduction paragraph - what this page covers and why it matters]

## [Conceptual Overview with value first] 
[Explain the concept, esp. why, what's the value first, before diving into implementation]

## [Step-by-Step Guide]
[Numbered steps with code examples or screenshots if applicable]
- use list or numaric list if applicable
- 

## [Common Scenarios/Use Cases]
[Real-world applications and variations]

## [Troubleshooting] (if applicable)
[Common issues and solutions]

## [What's Next]
[Links to related topics and logical next steps]
```

### Code Examples and Commands

```markdown
# Use descriptive context before code blocks
Edit the `profiles.yml` file to add a production target:

```yaml
# profiles.yml
jaffle_shop:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: 'jaffle_shop.duckdb'
    prod:
      type: duckdb
      path: 'jaffle_shop.duckdb'
      schema: prod
``` 

# Use shell prompts consistently
```shell
pip install recce
recce server
```

# Show expected output when helpful
```shell
$ recce server
Server running at: http://0.0.0.0:8000
```

```


### File and Path Conventions
- Use `./` for relative paths: `./models/staging/stg_payments.sql`
- Use absolute paths sparingly: `/path/to/file`
- Highlight important files: **profiles.yml**, **dbt_project.yml**
- Use consistent file extensions: `.sql`, `.yml`, `.md`

### Screenshot and Media Guidelines
- Use consistent naming: `section-feature-description.png`
- Include alt text: `![Lineage diff view showing model dependencies](../assets/images/lineage-diff.png)`
- Keep screenshots current and relevant
- Use callouts and annotations when needed
- Maintain consistent browser/interface styling


## 6. Content Quality & Maintenance

### Before Publishing Checklist
- [ ] **Accuracy**: All code examples tested and working
- [ ] **Completeness**: All steps included, no assumptions
- [ ] **Clarity**: Technical concepts explained for target audience
- [ ] **Consistency**: Follows style guide and terminology
- [ ] **Links**: All internal and external links working
- [ ] **Images**: Screenshots current and properly formatted
- [ ] **Grammar**: Proofread for spelling and grammar errors

### Version Synchronization
- Update screenshots when UI changes
- Verify code examples against latest Recce version
- Update version-specific instructions
- Check compatibility notes for dbt versions
- Review external link validity

### User Feedback Integration
- Monitor user questions and pain points
- Update documentation based on common issues
- Add FAQ sections for repeated questions
- Improve unclear sections based on user feedback

### Terminology Management
See [terminology.md](./terminology.md) for comprehensive terminology guidance including:
- Preferred terms for data teams
- Common confusion points
- Terminology alert system
- Clarification patterns

**Quick reference**: Always flag terms that might confuse data teams and provide immediate clarification.

### Regular Review Process
- **Monthly**: Review Cloud onboarding and key user journeys
- **Quarterly**: Update terminology and glossary alignment
- **Major releases**: Prioritize Cloud features in documentation updates
- **Continuous**: Monitor user questions for terminology confusion

## 7. Style Guidelines

### Formatting
- **Bold** for UI elements, file names, important terms
- *Italics* for emphasis (use sparingly)  
- `Code` for inline code, commands, file names
- Use numbered lists for sequential steps
- Use bullet points for non-sequential items
- Use tables for comparison or reference information

### Headings
- Use H1 only for page title
- Use H2 for main sections
- Use H3 for subsections  
- Use H4 sparingly, only for detailed breakdowns
- Make headings descriptive and action-oriented

### Admonitions (Callouts)
```markdown
!!! tip
    Use for helpful suggestions and best practices

!!! note  
    Use for important information and context

!!! warning
    Use for potential issues or important caveats

!!! info
    Use for additional context or background information
```

### Code Diffs

Use diffs to clearly show what changes in configuration files or code examples.
```markdown
```diff
  existing_line
- removed_line
+ added_line
```
```


## Content Quality Framework

Before publishing any content, verify it supports and follows these writing principles.

### Terminology Review Checklist
- [ ] **Terminology alerts flagged**: Confusing terms identified and clarified
- [ ] **Data-team language**: Preferred terms used consistently
- [ ] **Technical terms defined**: Software concepts explained in data context
- [ ] **Consistent usage**: Same terms used throughout document
- [ ] **Terminology guide updated**: New terms added to terminology.md
- [ ] Consistent, when refrering to same thing, use the same term

### Real-Time Terminology Alerts
When reviewing content, use this format to flag confusing terms:

```
⚠️ **Terminology Alert**: [TERM]
- **Confusion risk**: [Why data teams might misunderstand]
- **Suggested fix**: [Better phrasing or explanation]
```

**Example**:
```
⚠️ **Terminology Alert**: "Deploy your changes"
- **Confusion risk**: Data teams think infrastructure deployment
- **Suggested fix**: "Release your data changes to production"
```  