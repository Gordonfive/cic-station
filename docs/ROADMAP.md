# CIC Station Product Roadmap

This roadmap contains CIC Station product/release outcomes only. The cross-product Vincent + CIC Station roadmap is `PROGRAM_ROADMAP.md`.

CIC Station versions independently using Semantic Versioning. Pre-1.0 development uses `0.x.y`; the first release satisfying accepted 1.0 criteria becomes `1.0.0`.

## 0.1.0 — Product and data-model foundation

- canonical product, requirements, ADR, architecture, status, and release documentation;
- worker/enrollment/authorization/inventory/assignment/lease/result/audit data models;
- authenticated outbound worker protocol definition;
- explicit durable/ephemeral data authority model;
- AI-provider identity-profile model;
- protected-secret boundary definition.

## 0.2.0 — First managed-worker proof

- explicit Vincent enrollment and approval;
- scoped authorization and independent revocation;
- worker inventory, version/provenance, capabilities, and health;
- bounded assignment and structured result reporting;
- conservative Git-backed coordination where useful for the first proof;
- human approval gate round-trip;
- AI-provider intended/effective identity mismatch reporting.

## 0.3.0 — Leases and multi-worker coordination

- time-bounded assignment leases;
- heartbeat/liveness with grace states;
- stale-result protection;
- explicit assignment precedence and capability matching;
- second-worker coordination;
- worker retirement/replacement;
- coordinator restart/reconciliation semantics.

## 0.4.0 — Persistent service/API/database

- self-hostable application service;
- authenticated API;
- persistent operational database;
- enrollment/inventory/assignment/lease/audit operations moved from Git-backed prototype state into the service where appropriate;
- protected secret-delivery integration only if unattended credential use is actually required.

## 0.5.0 — Web UI and packaging

- responsive browser UI suitable for phone/desktop use;
- enrollment approval, worker details, assignment state, approvals, failures, reports, and fleet policy;
- notification routing/deduplication;
- straightforward self-hosted deployment on supported Linux server/VM/VPS/container environments;
- documented backup/recovery and upgrade procedures.

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
- explicit enrollment, least-privileged authorization, revocation, and audit;
- multiple workers and projects;
- correct assignment/lease/reassignment semantics;
- human approval gates;
- worker replacement and control-plane recovery;
- provider identity-policy handling without Git-based secret storage;
- release/upgrade/recovery documentation;
- full program recovery acceptance defined by `PROGRAM_ROADMAP.md`.

Unscheduled feature ideas remain GitHub issues until assigned to a release milestone.
