# Security and platform gate

## Mandatory pre-flight sequence

Before reading input content, display:

**DO NOT USE THIS SKILL IF THE FILES CONTAIN API CREDENTIALS, CLIENT SECRETS, PASSWORDS, ACCESS TOKENS, BEARER TOKENS, CERTIFICATES, SIGNED URLS OR OTHER LIVE SECRETS. REMOVE OR REDACT THEM BEFORE CONTINUING.**

Require explicit confirmation that:

- all inputs are sanitised and secret-free; and
- the work is taking place in an organisation-approved commercial AI environment.

Stop if the user cannot confirm either condition.

## Accepted environment assertion

Accept a user or administrator assertion that the environment is one of:

- ChatGPT Business, Enterprise or Edu workspace approved by the organisation;
- Claude Team or Enterprise workspace approved by the organisation;
- another commercial deployment formally approved for the data concerned.

A skill cannot reliably detect the subscription tier or verify contractual settings. Therefore use an attestation gate, not a technical claim that the plan was detected.

## Not acceptable as a substitute

Do not treat any of the following as equivalent to organisational approval:

- ChatGPT Free, Plus or Pro personal workspace;
- Claude Free, Pro or Max personal account;
- browser incognito/private browsing;
- temporary chat;
- deleted chat history;
- a private Claude project;
- disabling model-training controls alone.

These may reduce some persistence or sharing risks, but do not establish organisational authorisation, contractual protection, retention policy or data-governance approval.

## Secret response

If a live or suspected secret appears:

1. Stop processing the affected file.
2. Do not reproduce the value.
3. Report a redacted location only.
4. Recommend local sanitisation and credential rotation.
5. Restart only from a new sanitised copy.

## Sensitive but non-secret data

For HR, payroll, customer, supplier or financial data, minimise row-level content. Prefer metadata, aggregates, masked samples and control totals. Record sensitivity, permitted detail and retention instructions in the evidence statement.
