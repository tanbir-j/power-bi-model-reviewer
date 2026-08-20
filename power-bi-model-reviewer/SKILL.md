---
name: power-bi-model-reviewer
description: Review, document and improve Power BI solutions from PBIP/TMDL/PBIR/.bim artefacts or sanitised Power BI Service extracts. Use when assessing data sources, Power Query, semantic models, relationships, hierarchies, dimensions, DAX measures, report design, security, domain coverage, best-practice dashboards, or enhancement roadmaps. Supports both ChatGPT and Claude workflows. Refuse to process files containing credentials or secrets and require an approved business-grade AI environment before starting.
---

# Power BI Model Reviewer

## Mandatory warning before any work

Display this warning verbatim before opening, reading, extracting or analysing any supplied Power BI artefact or service definition:

> **DO NOT USE THIS SKILL IF THE FILES CONTAIN API CREDENTIALS, CLIENT SECRETS, PASSWORDS, ACCESS TOKENS, BEARER TOKENS, CERTIFICATES, SIGNED URLS OR OTHER LIVE SECRETS. REMOVE OR REDACT THEM BEFORE CONTINUING.**

Then require the user to confirm both statements:

1. The supplied files or extracted definitions contain no live credentials or secrets.
2. The work is being performed in an organisation-approved ChatGPT Business/Enterprise/Edu workspace, Claude Team/Enterprise workspace, or another formally approved commercial environment with suitable data controls.

Do not proceed if either confirmation is absent, unknown or negative. Do not accept a personal plan, ordinary browser incognito mode, temporary chat, private project, or disabled history as a substitute for organisational approval.

## Security fail-safe

Before semantic review:

1. Run `scripts/scan_secrets.py` against the input folder when code execution is available.
2. Stop if the scanner reports a suspected secret with medium or high confidence.
3. Never print, quote, summarise or preserve the suspected value.
4. Ask the user to create a sanitised copy and rotate any exposed live credential.
5. Record only the file, line, suspected secret type and redacted preview.

When code execution is unavailable, inspect filenames and visible snippets cautiously, do not expand suspicious credential-bearing content, and require the user to attest that sanitisation was completed locally.

Read `references/security-and-platform-gate.md` for the complete control.

## Runtime selection

Use one methodology with two runtime adapters.

- For ChatGPT, read `references/runtime-chatgpt.md`.
- For Claude, read `references/runtime-claude.md`.
- For Power BI Service without a PBIX/PBIT/PBIP file, read `references/power-bi-service-acquisition.md`.

Do not claim that browser-only Power BI Service inspection provides complete Power Query, model or DAX coverage. Prefer a sanitised TMDL/TMSL and PBIR extraction.

## Inputs

Accept any combination of:

- PBIP, TMDL, TMSL, `.bim` or model-documentation exports;
- PBIR or report-definition JSON;
- sanitised Power BI Service semantic-model and report definitions;
- Tabular Editor BPA results;
- DAX Studio, DMV, Performance Analyzer or refresh-history exports;
- screenshots or exported PDF for rendered-report behaviour;
- row-count profiles, control totals and reconciliation outputs;
- business decision lists, KPI definitions and source-system documentation.

State the evidence available and unavailable before reviewing.

## Review workflow

### 1. Document the solution

Produce structured inventories for:

- data sources and authentication method, without credentials;
- Power Query queries, dependencies and transformation logic;
- semantic-model tables, columns, relationships and partitions;
- explicit and inferred hierarchies;
- dimensions, facts, bridges and helper tables;
- DAX measures, calculated columns and calculated tables;
- report pages, visuals, filters, bookmarks and navigation;
- refresh, gateway and operational dependencies where evidence exists.

Read `references/documentation-contract.md`.

### 2. Visualise the model

Create:

- model topology map;
- filter-path map;
- fact and dimension map;
- hierarchy trees;
- date-role map;
- grain matrix;
- measure dependency map where practical.

Visually distinguish bidirectional relationships, many-to-many relationships, inactive relationships, fact-to-fact joins and ambiguous routes. Link each material issue to a finding ID.

Read `references/visualisation-contract.md`.

### 3. Critique the data model

Keep model critique central. Assess against dimensional-modelling and Power BI best practice, including:

- bidirectional joins and cross-filter direction;
- many-to-many relationships and bridge design;
- ambiguous filter paths and loops;
- fact-to-fact and dimension-to-dimension relationships;
- star-schema quality and avoidable snowflaking;
- mixed grain and duplicate-key risk;
- conformed dimensions;
- role-playing dates and inactive relationships;
- effective dating and slowly changing dimensions;
- snapshot facts and semi-additive behaviour;
- surrogate and natural keys;
- RLS propagation;
- calculated columns, calculated tables and implicit measures;
- naming, descriptions, display folders and usability;
- performance and maintainability risks.

Do not label a pattern bad merely because it is unusual. For each finding provide evidence, consequence, falsification test and recommended target pattern.

Read `references/model-and-dax-tests.md`.

### 4. Review DAX and semantic definitions

For each material measure document:

- business meaning;
- expression and dependencies;
- grain and filter context;
- date context;
- blank, zero and total behaviour;
- formatting and unit;
- repeated logic;
- correctness and performance risks;
- validation required.

Test or flag common issues involving `CALCULATE`, `FILTER`, iterators, `ALL`, `REMOVEFILTERS`, `USERELATIONSHIP`, context transition, distinct counts, ratios, semi-additive measures and totals.

### 5. Classify the business domain

Infer the primary and secondary domains from tables, fields, measures, source names and report pages. State confidence and supporting evidence.

Examples include HR, AP, AR, GL, procurement, projects, grants, sales, service, operations and inventory.

### 6. Research domain dashboard practice

Use current authoritative sources when web research is available. Identify:

- executive, management, operational, diagnostic and control reporting;
- standard and emerging KPIs;
- regulatory or statutory requirements;
- common dimensions and drill paths;
- control and exception reporting;
- advanced analytics that are realistic for the available data.

Separate statutory requirements, established practice, vendor marketing and speculative ideas.

### 7. Compare coverage and feasibility

Create a matrix showing:

- analytical requirement;
- current report coverage;
- data availability;
- model readiness;
- trust status;
- source or model gap;
- recommendation;
- priority and dependency.

### 8. Design improvements

Recommend:

- immediate remediation;
- target semantic model;
- governed measure catalogue;
- report-page redesign;
- data-quality controls;
- security and sensitivity controls;
- performance improvements;
- phased enhancement roadmap.

Use the sequence: Stabilise, Standardise, Enhance, Extend.

## Evidence and findings

For every material finding record:

- finding ID;
- category;
- hypothesis;
- supporting evidence;
- evidence strength;
- business and technical consequence;
- falsification test;
- test result or untested status;
- recommendation;
- priority;
- dependency;
- disposition: retain, refine, remodel, rebuild or retire.

Never call a figure reconciled without a supplied control total and successful comparison.

## Required outputs

Produce, where evidence permits:

1. Security and evidence statement.
2. Data-source inventory.
3. Power Query catalogue and dependency map.
4. Semantic-model inventory.
5. Fact, dimension and hierarchy catalogue.
6. Model topology and filter-path diagrams.
7. Grain and date-role matrices.
8. DAX and semantic-layer catalogue.
9. Model and DAX critique.
10. Report-page inventory and decision coverage.
11. Domain best-practice benchmark.
12. Coverage and feasibility matrix.
13. Target-state model and measure catalogue.
14. Prioritised enhancement backlog.
15. Executive disposition and evidence limits.

## Boundaries

- Remain read-only unless the user separately requests an implementation task.
- Do not retrieve or expose credential values.
- Do not use live organisational data on an unapproved personal account.
- Do not infer row-level defects from metadata alone.
- Do not treat hidden fields as security.
- Do not overstate browser-only evidence.
- Keep parser outputs factual; reserve interpretation for the review stage.
