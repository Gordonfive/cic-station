# ADR-0017: Multidimensional worker state model

**Status:** Accepted
**Decision date:** 2026-08-28

## Context

Early planning used a single managed-worker state list such as Working, Available, Offline, and later Standby. A single mutually exclusive enum cannot accurately represent combinations such as an online but administratively drained worker, a working but degraded worker, an available worker with provider authentication blocked, or a suspended worker with a validated wake path.

## Decision

Canonical managed-worker state is multidimensional rather than one exclusive status enum.

At minimum, CIC Station and Vincent-side managed reporting distinguish:

- **scheduling/availability state** — whether new work may be assigned, including available, drained/maintenance, disabled, or equivalent policy states;
- **liveness/health state** — observed reachability and health, including online/healthy, degraded, stale, unreachable, or equivalent observations;
- **execution state** — whether the worker is idle, preparing, working, blocked/waiting, or otherwise executing an attempt;
- **power state** — awake, suspended/standby, powered off, unknown, or equivalent where supported.

Simple labels such as **Working**, **Available**, **Offline**, or **Standby** may remain as derived UI summaries, but they are not the canonical authority model and must not collapse independent scheduling, liveness, execution, or power facts.

## Rationale

Independent dimensions prevent state explosion and preserve truthful scheduling and recovery behavior as workers gain maintenance/drain modes, degraded health, provider-specific blocks, remote wake, and multi-worker scheduling.

## Consequences

- CIC Station data models should store independent worker state dimensions or equivalent normalized facts.
- Scheduling decisions must use authoritative scheduling/health/capability inputs rather than a display badge alone.
- Vincent reports the facts it can observe locally; CIC Station derives fleet-level liveness and scheduling interpretation where appropriate.
- Existing Working/Available/Offline wording in the Vincent roadmap must be revised to describe derived operator-facing status rather than a canonical state machine.
- Future Standby support remains conditional on a validated remote-wake mechanism.

## Owner approval

Approved 2026-08-28 during the Vincent/CIC architecture review.
