# Contributing

This is a private, controlled repository. Access does not imply permission to reuse client data or redistribute the skill.

## Branching

- `main`: validated release-ready source
- `feature/<short-description>`: enhancements
- `fix/<short-description>`: corrections

## Pull request requirements

Include:

- purpose of the change;
- files changed;
- expected behaviour;
- evidence used for testing;
- confirmation that no secrets or client data are included;
- whether `skill.zip` was rebuilt.

## Design principles

- Keep the core methodology platform-neutral.
- Keep GPT- and Claude-specific instructions in runtime adapters.
- Prefer deterministic extraction for inventories.
- Separate extracted facts from AI interpretation.
- State evidence limitations.
- Preserve model critique, falsification tests and domain benchmarking.
- Do not duplicate canonical reference models where exchange packs can be used.
