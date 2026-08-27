# Mission Control Roadmap

**Updated:** 2026-08-27T08:17:00-08:00

Mission Control is the private control plane for Vincent deployments. This roadmap tracks control-plane outcomes, not day-to-day task state. Active implementation work should be represented by GitHub issues, pull requests, and milestones.

## Current dependency

Vincent 1.0 must first prove that a generic worker can install cleanly, reach an unassigned READY state, connect to an operator-selected Git repository, complete one bounded task, and report results without requiring Mission Control.

Mission Control should remain intentionally small until that proof establishes which control-plane functions are actually required.

## M1 — Private fleet records

**Goal:** define durable private fleet state without storing secrets.

- Worker inventory and public identity fingerprints.
- Enrollment approval, suspension, revocation, and retirement state.
- Roles, capabilities, resource limits, and repository scopes.
- Project registrations and assignment metadata.
- Safe references to externally protected credentials.

**Status:** design/documentation.

## M2 — Assignment coordination

**Goal:** coordinate multiple Vincent workers without ambiguous ownership.

- Machine-readable assignment records.
- Explicit claiming/ownership semantics.
- Isolated worker workspaces.
- Durable completion/failure reporting.
- Clear separation between task completion, review, integration, and production authority.

**Status:** deferred until Vincent 1.0 worker proof.

## M3 — Liveness and leases

**Goal:** distinguish an active worker from abandoned work and allow safe reassignment.

- Worker liveness/heartbeat model.
- Time-bounded assignment leases.
- Grace periods for temporary connectivity loss.
- Expiration/reassignment semantics that reject stale results.

**Status:** planned; unscheduled.

## M4 — Operational service

**Goal:** determine whether a dedicated Mission Control service/backend provides enough value over Git-backed coordination to justify its complexity.

Potential capabilities include enrollment workflow, inventory API, assignment dispatch, fleet health, notifications, and operator UI.

**Status:** deferred.

## M5 — Multi-project and recovery proof

**Goal:** restore and operate a multi-project worker fleet from durable state after loss of workers or the control-plane service.

- Reconstruct fleet policy and project registrations.
- Re-enroll replacement workers safely.
- Reconcile active assignments and incomplete work.
- Prove no worker-local or chat-only state is required for recovery.

**Status:** not started.

## Permanent constraints

- Mission Control never replaces human judgment for product direction, production actions, destructive actions, credential scope, or major architecture.
- Fresh Vincent does not automatically depend on Mission Control.
- Public Vincent must never contain private fleet state or reusable private credentials.
- Git stores durable policy and coordination evidence; secret values remain outside Git.
- Prefer standard GitHub issues, pull requests, milestones, releases, and ADRs over custom parallel tracking systems when those tools meet the requirement.
