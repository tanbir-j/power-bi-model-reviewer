# Power BI Model Reviewer

A cross-platform skill for GPT and Claude that documents, critiques and improves Power BI solutions from project artefacts or sanitised Power BI Service extracts.

## Security warning

> **DO NOT USE THIS SKILL IF THE FILES CONTAIN API CREDENTIALS, CLIENT SECRETS, PASSWORDS, ACCESS TOKENS, BEARER TOKENS, CERTIFICATES, SIGNED URLS OR OTHER LIVE SECRETS. REMOVE OR REDACT THEM BEFORE CONTINUING.**

Use only in an organisation-approved commercial AI environment. Do not treat incognito mode, temporary chat or disabled history as substitutes for organisational approval.

## What it reviews

- Data sources and refresh dependencies
- Power Query scripts and query dependencies
- Data model structure, grain and relationships
- Bidirectional, many-to-many and ambiguous filter paths
- Dimensions, hierarchies and date roles
- Semantic layer and DAX measures
- Report pages, visuals and decision coverage
- Domain-specific dashboard coverage and target-state improvements

## Repository structure

```text
power-bi-model-reviewer/
├── SKILL.md
├── agents/
├── references/
└── scripts/
skill.zip
```

`power-bi-model-reviewer/` is the editable source. `skill.zip` is the packaged upload artefact.

## Supported evidence routes

1. PBIP, TMDL, PBIR or BIM artefacts
2. Sanitised Power BI Service definitions and metadata
3. Tabular Editor BPA, XMLA, DMV or Performance Analyzer outputs
4. Browser-only evidence as a declared lower-confidence fallback

PBIX and PBIT files are not required. Claude should normally consume sanitised TMDL, PBIR, JSON, CSV and rendered evidence rather than a PBIX file.

## Installation

### ChatGPT

Upload `skill.zip` through the Skills interface.

### Claude

Add the `power-bi-model-reviewer` folder to the approved working directory or skill/plugin workflow used by your Claude environment. Follow `references/runtime-claude.md`.

## Development workflow

1. Create a feature branch.
2. Edit files inside `power-bi-model-reviewer/`.
3. Run the secret scanner against test inputs.
4. Validate the skill.
5. Repackage it as `skill.zip`.
6. Submit a pull request describing the change and test evidence.

Do not commit client Power BI extracts, screenshots, data, credentials or generated review outputs.

## Status

Enhancement-stage private pilot; the current focus is broader documentation, semantic-model critique, domain benchmarking and GPT/Claude portability.
