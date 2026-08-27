# Agent Instructions

## Start here

Before changing this repository, read:

1. `README.md`
2. `docs/README.md`
3. `docs/PRODUCT.md`
4. `docs/REQUIREMENTS.md`
5. `docs/ARCHITECTURE.md`
6. `docs/PROGRAM_ROADMAP.md`
7. `docs/ROADMAP.md`
8. `docs/STATUS.md`
9. `docs/decisions/README.md`
10. relevant active GitHub issues and pull requests

Check current remote state in both `Gordonfive/cic-station` and `Gordonfive/vincent` before assuming a branch is current. Git is the durable authority; chat history is not.

## Authority and safety

- The owner controls product direction, security, production access, destructive operations, enrollment policy, and major architecture.
- Durable consequential decisions belong in ADRs. ADR identifiers are immutable once merged.
- Never commit raw secrets, passwords, tokens, private keys, authentication caches, reusable enrollment credentials, or production data.
- CIC Station must not become a general-purpose remote shell.
- Vincent workers are independently identifiable, revocable, and least-privileged.
- Human approval remains mandatory for high-impact production, destructive, credential-expansion, protected-integration, and release actions unless a later ADR explicitly changes the boundary.

## Repository boundary

`Gordonfive/cic-station` owns the reusable CIC Station web application, API, database schema/migrations, tests, packaging, product documentation, and program roadmap. Generic Vincent worker implementation belongs in `Gordonfive/vincent`.

Private operational data belongs in the deployed CIC Station database, protected backups, deployment configuration, and secret systems—not Git. This repository remains private during development and may become public under AGPLv3 only after an explicit owner-approved release gate and complete history, secret, privacy, and configuration audit.

## Development workflow

- `main` is the only permanent branch.
- Use short-lived task branches and pull requests.
- Squash merge accepted PRs.
- Delete merged or superseded branches after useful work is preserved.
- Do not accept outside pull requests yet; revisit at 1.0 or later.
- Keep changes bounded, tested, documented, and recoverable.
- Git failures and conflicts must be surfaced, never destructively auto-resolved.
- Long-running commands should display progress while saving complete output with `tee`, preserve pipeline status, and print an explicit final exit status.

## Documentation model

- `PRODUCT.md` defines intent and boundaries.
- `REQUIREMENTS.md` defines stable `MC-REQ-####` requirements.
- `ARCHITECTURE.md` explains implementation design.
- `docs/decisions/ADR-*.md` record consequential decisions.
- `PROGRAM_ROADMAP.md` owns cross-product Vincent + CIC Station milestones.
- `ROADMAP.md` owns CIC Station product/release outcomes only.
- `STATUS.md` records current implementation/test state.
- GitHub issues are the unscheduled backlog; do not recreate `PLANNED_FEATURES.md`.
