# Contributing to Mission Control

## Before starting

Read `AGENTS.md`, `docs/README.md`, `docs/STATUS.md`, `docs/ROADMAP.md`, and `MISSION_CONTROL.md`. Inspect open issues, pull requests, and branches before changing shared coordination state.

## Work tracking

- Use GitHub issues for non-trivial defects, features, refactors, or documentation work.
- Use milestones for release or capability goals.
- Keep `docs/ROADMAP.md` at milestone/outcome level rather than using it as a task queue.
- Record consequential architecture, security, or authority changes as ADRs/decision records.

## Branches and pull requests

- Use short-lived descriptive branches such as `fix/...`, `feature/...`, or `docs/...`.
- Keep one logical change per pull request when practical.
- Preserve unexpected active work and surface conflicts rather than destructively resolving them.
- Delete temporary branches after merge or supersession.
- Pull-request approval does not grant production, credential, enrollment, destructive, or repository-deletion authority unless explicitly stated.

## Validation

Run the repository validation appropriate to the change before requesting review. Long-running commands should display progress while saving complete output with `tee`, preserve pipeline status, and print an explicit final status.

## Documentation

Update documentation with behavior, policy, schema, authority, or operating-procedure changes. Use issues/pull requests for volatile work state; keep `docs/STATUS.md` concise and cross-cutting.

## Security

Never commit passwords, tokens, private keys, authentication caches, reusable enrollment credentials, or production data. Store safe identifiers, public keys/fingerprints, policy, and references to separately protected secrets only.
