# Mission Control Documentation

This directory contains the current operational documentation for Mission Control.

## Start here

1. `../AGENTS.md` — repository rules for automated contributors.
2. `STATUS.md` — current project state and immediate priorities.
3. `ROADMAP.md` — strategic milestones and planned work.
4. `../MISSION_CONTROL.md` — product role and operating model.
5. `coordination/decisions.md` — accepted project/control-plane decisions.

## Documentation classes

- **Current guidance:** `README.md`, `STATUS.md`, `ROADMAP.md`, `MISSION_CONTROL.md`, and accepted decision records.
- **Configuration examples:** `../config/`.
- **Evidence:** current validation or operational reports only when they remain useful to ongoing work.

Completed migration/consolidation material does not remain in the active documentation tree merely for history; Git history provides provenance.

## Maintenance rules

- Keep active documentation consistent with the current implementation and accepted decisions.
- Do not duplicate the same authority or status information across multiple files.
- Put durable architecture choices in decision records rather than handoff prose.
- Put volatile task state in issues, pull requests, or `STATUS.md`, not in the roadmap.
- Remove superseded operational instructions after useful rationale has been captured.
- Do not commit secrets, credentials, private keys, authentication caches, or production data.
