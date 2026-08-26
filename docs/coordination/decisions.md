# Decisions

**Register updated:** 2026-08-26T09:49:00-08:00

## 2026-08-25 — Separate public workers from private fleet control

Accepted structure:

- `Gordonfive/vincent` is the public Vincent worker platform.
- `Gordonfive/mission-control` is the private fleet control plane.
- Individual project repositories retain project-specific authority and Product DNA.
- GitBoy is a retired prototype name.
- VS Code is optional and is not a control-plane dependency.
- The universal ISO contains no permanent identity or reusable credential.
- Enrollment is explicit, scoped, unique per worker, and revocable.

## 2026-08-26T09:49:00-08:00 — Repository hygiene and timestamp authority

Accepted policy:

- Mission Control and Vincent are operational sources of truth, not archives of abandoned implementation.
- Before obsolete Git state is deleted, inspect it once and distill any still-useful facts, rationale, lessons, or requirements into current timestamped documentation.
- After useful information is documented, obsolete branches, migration histories, abandoned code, superseded experiments, and archive-only tags may be deleted.
- Keep only the minimum temporary workstream branches needed for active work; delete them after integration or supersession.
- The stable target branch topology is `main` only. VINCENT 1.0 specifically targets `main` as the sole Vincent branch.
- For conflicting project direction, the newest applicable explicitly timestamped authoritative decision controls unless a later decision explicitly provides different precedence.
- Untimestamped material cannot override conflicting timestamped material. Git commit timestamps are provenance only and do not replace an authoritative decision or document timestamp.
