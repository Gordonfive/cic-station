# Agent Instructions

## Start here

Before changing this repository, read:

1. `README.md`
2. `docs/README.md`
3. `docs/PRODUCT.md`
4. `docs/REQUIREMENTS.md`
5. `docs/ARCHITECTURE.md`
6. `docs/ROADMAP.md`
7. `docs/STATUS.md`
8. `docs/decisions/README.md`
9. relevant active GitHub issues and pull requests
10. `logrusbox/vincent-program` when the task has cross-product implications

Check current remote state in both `logrusbox/cic-station` and `logrusbox/vincent` before assuming a branch is current. Git is the durable authority; chat history is not.

## Authority and safety

- The owner controls product direction, security, production access, destructive operations, enrollment policy, and major architecture.
- Durable consequential product decisions belong in CIC Station ADRs. Program-level decisions that genuinely span both products belong in `logrusbox/vincent-program`.
- Never commit raw secrets, passwords, tokens, private keys, authentication caches, reusable enrollment credentials, or production data.
- CIC Station must not become a general-purpose remote shell.
- Vincent workers are independently identifiable, revocable, and least-privileged.
- Human approval remains mandatory for high-impact production, destructive, credential-expansion, protected-integration, and release actions unless a later ADR explicitly changes the boundary.

## Repository boundary

`logrusbox/cic-station` owns the reusable CIC Station web application, API, database schema/migrations, tests, packaging, product documentation, product-specific issues, and product roadmap. Generic Vincent worker implementation belongs in `logrusbox/vincent`. Cross-product program roadmap, integration issues, and program governance belong in `logrusbox/vincent-program`.

Operational fleet data belongs in the deployed CIC Station database, protected backups, deployment configuration, and secret systems—not Git. The repository is public during pre-release development, so public-safe source, examples, tests, configuration, and documentation practices apply continuously. Public visibility does not remove the formal release audit or make operational data, credentials, private keys, authentication state, or production configuration appropriate for Git.

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

- `PRODUCT.md` defines CIC Station intent and boundaries.
- `REQUIREMENTS.md` defines stable `MC-REQ-####` requirements.
- `ARCHITECTURE.md` explains CIC Station implementation design.
- `docs/decisions/ADR-*.md` record consequential CIC Station decisions.
- `docs/ROADMAP.md` owns CIC Station product/release outcomes only.
- `docs/STATUS.md` records current CIC Station implementation/test state.
- `docs/PROGRAM_ROADMAP.md` is a migration pointer; the canonical program roadmap lives in `logrusbox/vincent-program`.
- CIC Station-specific GitHub issues are the local backlog; cross-product issues belong in `logrusbox/vincent-program`.
