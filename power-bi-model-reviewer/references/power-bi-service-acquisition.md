# Power BI Service acquisition

Treat Power BI Service as a first-class source when PBIX, PBIT or PBIP is unavailable.

Preferred evidence order:

1. Sanitised semantic-model definition in TMDL or TMSL.
2. Sanitised report definition in PBIR or legacy JSON.
3. Tabular Editor BPA and XMLA/DMV extracts.
4. Data-source, refresh, gateway and lineage metadata.
5. Rendered-report screenshots or PDF.
6. Browser-only observation as a degraded fallback.

Use read-only Microsoft Fabric/Power BI APIs, XMLA, Tabular Editor, DAX Studio, PowerShell or an approved connector to create a local review pack. Never retrieve credential values.

Important: Power Query expressions embedded in model definitions may contain hard-coded secrets. Extract locally, scan immediately, redact before AI analysis, and rotate any exposed credential.

A browser-only review may assess visible pages, navigation and interactions, but must not claim complete Power Query, relationship, hierarchy or DAX coverage.
