# Contributing to CIC Station

## Current contribution policy

Outside pull requests are not accepted yet. Revisit external contribution policy at 1.0 or later.

## Internal workflow

- `main` is the only permanent branch.
- Create a short-lived branch for each bounded change.
- Open a pull request; do not integrate ordinary work directly into `main`.
- Required CI/status checks must pass before merge.
- Resolve review conversations before merge.
- Squash merge accepted pull requests.
- Delete merged/superseded branches after useful work is preserved.
- Do not force-push or delete `main`.

The repository is public during pre-release development. The workflow above should therefore be enforced with GitHub repository rules when available rather than relying only on procedure. Until those rules are configured, the same PR + CI + squash + no-force-push requirements remain mandatory project policy.

## Documentation changes

Update the canonical document for the type of change:

- product intent/boundary → `docs/PRODUCT.md`;
- stable requirement → `docs/REQUIREMENTS.md` with the next unused `MC-REQ-####`;
- consequential architecture/policy decision → new ADR;
- implementation architecture → `docs/ARCHITECTURE.md`;
- cross-product milestone → `docs/PROGRAM_ROADMAP.md`;
- CIC Station release outcome → `docs/ROADMAP.md`;
- current implementation/test state → `docs/STATUS.md`;
- unscheduled idea/work → GitHub issue.

Do not recreate permanent handoff, Project Start, or planned-feature backlog documents.

## Security

Never commit raw secrets, credentials, authentication caches, production data, private keys, or reusable enrollment/provider credentials. Public repository visibility reinforces rather than replaces this source/operational-data boundary.

## Releases

CIC Station versions independently using SemVer. Pre-1.0 versions use `0.x.y`; the first accepted 1.0 release is `1.0.0`. Update `CHANGELOG.md` at release boundaries and use Git tags/GitHub Releases for exact release commits and fuller release notes.
