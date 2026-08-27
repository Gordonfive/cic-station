# Mission Control Decision Register

**Updated:** 2026-08-27T08:17:00-08:00

This register contains concise accepted decisions that currently affect Mission Control. New consequential architecture decisions should preferably be recorded as numbered ADRs and indexed here.

## MC-DEC-001 — Separate public worker software from private fleet control

**Accepted:** 2026-08-25  
**Status:** Accepted

- `Gordonfive/vincent` is the public generic worker platform.
- `Gordonfive/mission-control` is the private fleet control plane.
- Individual project repositories retain project-specific authority, source, requirements, tests, and work history.
- Previous prototype names and repositories are retired and are not part of the active architecture.
- VS Code is optional and is not a control-plane dependency.
- Installer media contains no permanent worker identity or reusable private credential.
- Enrollment is explicit, scoped, unique per worker, and revocable.

## MC-DEC-002 — Keep operational repositories current

**Accepted:** 2026-08-26T09:49:00-08:00  
**Status:** Accepted

- Mission Control and Vincent are operational sources of truth, not archives of abandoned implementation.
- Before obsolete Git state is deleted, inspect it and distill still-useful rationale, requirements, or lessons into current documentation.
- Remove superseded experiments, migration-only material, and obsolete branches after useful information is captured.
- Use temporary task branches only while work is active; delete them after integration or supersession.
- Explicitly recorded accepted decisions outrank stale handoffs or chat summaries.

## MC-DEC-003 — Fresh Vincent does not depend on Mission Control

**Accepted:** 2026-08-26T13:22:00-08:00  
**Status:** Accepted

A fresh Vincent installation reaches an unassigned READY state independently. Mission Control is an optional private control source selected and authorized after installation; Vincent must not automatically contact it or require private Mission Control configuration to boot, self-test, update, or become operational.

## Decision practice

For new decisions, use a numbered ADR under `docs/decisions/` when the choice affects architecture, security boundaries, persistent interfaces, or long-term maintenance. Each ADR should record context, decision, alternatives considered, consequences, status, and any superseded ADR.
