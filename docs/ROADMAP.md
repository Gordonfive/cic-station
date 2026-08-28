# CIC Station Product Roadmap

This roadmap contains CIC Station product/release outcomes only. The cross-product Vincent + CIC Station roadmap is `PROGRAM_ROADMAP.md`.

CIC Station versions independently using Semantic Versioning. Pre-1.0 development uses `0.x.y`; the first release satisfying accepted 1.0 criteria becomes `1.0.0`.

## 0.1.0 — Product, domain-model, and persistence foundation

- canonical product, requirements, ADR, architecture, status, and release documentation;
- worker/enrollment/authorization/inventory/work-item/assignment/attempt/lease/result/audit domain models;
- minimum persistent application service/API/database foundation for operational fleet state;
- operator/actor identity, authorization, session, bootstrap, and recovery model;
- worker-generated asymmetric installation identity, proof-of-possession, replay-resistant enrollment/bootstrap, credential lifecycle, and server-trust model;
- explicitly versioned worker protocol with declared compatibility, retry/idempotency identifiers, and stale/conflicting transition protection;
- authenticated encrypted outbound worker protocol definition;
- encrypted operator/API transport boundary;
- explicit durable/ephemeral data authority model;
- multidimensional worker state model separating scheduling/availability, liveness/health, execution, and power state; simple Working/Available/Offline/Standby labels may be derived for UI use;
- AI-provider identity-profile model;
- protected-secret boundary definition.

## 0.2.0 — First managed-worker proof through persistent operational authority

- explicit Vincent enrollment and approval by an authenticated authorized operator;
- approval bound to the exact worker public identity with proof-of-possession on subsequent connections;
- replay-resistant enrollment/bootstrap behavior and independent worker credential revocation;
- declared Vincent/CIC Station protocol compatibility with visible incompatibility failure;
- retry-safe assignment/acknowledgement/result state transitions without exactly-once delivery assumptions;
- scoped authorization and independent revocation;
- worker inventory, version/provenance, capabilities, multidimensional health/availability/execution visibility, and protocol-compatibility visibility;
- bounded work item and execution-attempt lifecycle with structured result reporting;
- operational enrollment/authorization/assignment/attempt/result state persisted through the CIC Station service/database rather than using Git as the live control-plane database;
- Git retained for durable project artifacts and conservative transitional coordination where appropriate;
- human approval gate round-trip with attributable operator audit;
- AI-provider intended/effective identity mismatch reporting.

## 0.3.0 — Leases and multi-worker coordination

- time-bounded assignment/attempt leases backed by persistent CIC Station operational state;
- heartbeat/liveness with grace states distinct from scheduling and execution state;
- explicit lease clock-authority/skew/restart semantics;
- stale-result protection across expired/superseded attempts;
- explicit assignment precedence and capability matching;
- second-worker coordination;
- worker retirement/replacement;
- coordinator restart/reconciliation semantics.

## 0.4.0 — Service/database operational hardening

- hardened self-hostable application service and authenticated authorized API;
- production-shaped database migrations/schema lifecycle;
- backup/restore, upgrade, rollback/recovery, and reconciliation procedures;
- observability and operational failure handling for service/database state;
- deployment hardening across supported Linux server/VM/VPS/container environments;
- protected secret-delivery integration only if unattended credential use is actually required.

## 0.5.0 — Web UI and packaging

- responsive browser UI suitable for phone/desktop use;
- operator login/session/revocation workflows;
- enrollment approval, worker details, assignment state, approvals, failures, reports, and fleet policy;
- notification routing/deduplication;
- straightforward self-hosted deployment on supported Linux server/VM/VPS/container environments with documented TLS termination/trust boundaries;
- documented backup/recovery and upgrade procedures, including operator-authentication and worker-credential recovery/replacement semantics.

## 0.6.0 — Public application ecosystem

- complete Git-history and release-content audit for privacy, secrets, infrastructure, and production configuration;
- publish the existing reusable application repository under AGPLv3;
- public-safe configuration examples and schemas;
- release tags/GitHub Releases and `CHANGELOG.md`;
- package/container distribution as appropriate;
- dependency/license/security review;
- no Gordonfive operational data, secrets, or private production configuration in the published source.

## 0.7.0 and later — Multi-project and multi-agent maturity

- multiple active projects with independent scopes/policies;
- multiple repositories per project where required;
- project activation and priority policy;
- provider-neutral scheduling across Codex, Gemini, Copilot, Ollama/local models, and custom agents as Vincent support matures;
- fleet update policy, maintenance/drain workflows, and recovery exercises.

## 1.0.0 acceptance

CIC Station 1.0 must be operationally trustworthy rather than merely feature-rich. At minimum it must prove:

- self-hosted API/database/web UI;
- distinct authenticated operators, least-privileged authorization, secure session lifecycle, first-admin bootstrap, and administrative recovery;
- encrypted operator/API and worker/control-plane transport;
- worker-generated asymmetric identity, proof-of-possession, replay-resistant enrollment/bootstrap, credential rotation/revocation, and fail-closed server trust;
- explicit worker-protocol compatibility/versioning and retry-safe/idempotent state transitions;
- explicit enrollment, least-privileged worker authorization, revocation, and audit;
- multiple workers and projects;
- correct work-item/attempt/lease/reassignment semantics;
- multidimensional worker scheduling/liveness/execution/power state with safe derived operator statuses;
- human approval gates;
- worker replacement and control-plane recovery;
- provider identity-policy handling without Git-based secret storage;
- release/upgrade/recovery documentation;
- full program recovery acceptance defined by `PROGRAM_ROADMAP.md`.

Unscheduled feature ideas remain GitHub issues until assigned to a release milestone.
