# Contributing to Mission Control

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
- Force pushes to protected `main` are prohibited.

## Documentation changes

Update the canonical document for the type of change:

- product intent/boundary → `docs/PRODUCT.md`;
- stable requirement → `docs/REQUIREMENTS.md` with the next unused `MC-REQ-####`;
- consequential architecture/policy decision → new ADR;
- implementation architecture → `docs/ARCHITECTURE.md`;
- cross-product milestone → `docs/PROGRAM_ROADMAP.md`;
- Mission Control release outcome → `docs/ROADMAP.md`;
- current implementation/test state → `docs/STATUS.md`;
- unscheduled idea/work → GitHub issue.

Do not recreate permanent handoff, Project Start, or planned-feature backlog documents.

## Security

Never commit raw secrets, credentials, authentication caches, production data, private keys, or reusable enrollment/provider credentials. Private repository visibility does not make secret storage in Git acceptable.

## Releases

Mission Control versions independently using SemVer. Pre-1.0 versions use `0.x.y`; the first accepted 1.0 release is `1.0.0`. Update `CHANGELOG.md` at release boundaries and use Git tags/GitHub Releases for exact release commits and fuller release notes.
