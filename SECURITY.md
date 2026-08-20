# Security policy

## Prohibited content

**DO NOT COMMIT, UPLOAD OR PROCESS FILES CONTAINING API CREDENTIALS, CLIENT SECRETS, PASSWORDS, ACCESS TOKENS, BEARER TOKENS, CERTIFICATES, SIGNED URLS OR OTHER LIVE SECRETS.**

Also do not commit:

- client or employee personal data;
- unapproved Power BI Service extracts;
- tenant identifiers where restricted;
- screenshots showing credentials or sensitive records;
- `.env`, credential cache or local authentication files;
- unredacted Power Query containing secrets.

## Required controls

- Use an organisation-approved commercial GPT or Claude environment.
- Sanitise Power BI Service definitions locally before AI processing.
- Run `scripts/scan_secrets.py` against candidate text artefacts.
- Stop if a suspected secret is detected.
- Rotate any live credential discovered in source code or an exported definition.
- Keep client review artefacts outside this repository.

## Reporting a security issue

Do not open a public issue containing sensitive details. Contact the repository owner privately and provide only the minimum information needed to locate the problem. Never paste the secret itself.
