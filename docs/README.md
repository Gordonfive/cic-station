# Mission Control Documentation

This directory contains the canonical Mission Control and cross-product program documentation.

## Canonical documents

- `PRODUCT.md` — Mission Control purpose, users, goals, non-goals, and product boundaries.
- `REQUIREMENTS.md` — stable `MC-REQ-####` functional and non-functional requirements.
- `ARCHITECTURE.md` — control-plane architecture and Vincent integration boundary.
- `PROGRAM_ROADMAP.md` — canonical Vincent + Mission Control cross-product roadmap.
- `ROADMAP.md` — Mission Control product/release roadmap only.
- `STATUS.md` — current implementation, proof, and blocker state.
- `decisions/README.md` — ADR index.

## Supporting material

- GitHub issues — unscheduled feature backlog, active work, blockers, and follow-ups.
- Pull requests — integration/review state and change-specific evidence.
- `CHANGELOG.md` — concise release history.
- `CONTRIBUTING.md` — repository workflow and contribution policy.

## Lifecycle rules

- Do not recreate permanent handoff, Project Start, or planned-feature backlog documents.
- Consequential accepted decisions become ADRs.
- Requirements retain their IDs permanently; superseded requirements keep their identifiers and status.
- Completed migration/project-reset material belongs in Git history, not the active documentation tree.
- Large raw logs, screenshots, generated builds, and CI bundles belong in Actions/release artifacts rather than ordinary Git history.
- Documentation and source change through the same pull-request/CI workflow.
