# ADR-0005: Assignment leases and conservative reassignment

**Status:** Accepted
**Decision date:** 2026-08-27

## Context

Multiple workers require explicit work ownership. Temporary network loss must not cause two workers to continue the same exclusive task.

## Decision

Managed exclusive assignments use time-bounded leases with explicit owner, duration, renewal, expiration, and stale-result semantics. Heartbeats report liveness but do not replace leases. Reassignment is conservative while ownership is uncertain, and stale results from expired/superseded leases may not silently supersede newer work.

## Rationale

Correctness and preservation of authoritative work matter more than immediate machine utilization.

## Consequences

- Lease state belongs in operational Mission Control state rather than high-frequency Git commits.
- Workers that cannot verify ownership must stop or checkpoint safely before publishing exclusive results.
