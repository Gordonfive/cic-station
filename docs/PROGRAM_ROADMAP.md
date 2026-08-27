# Vincent + CIC Station Program Roadmap

This is the canonical cross-product roadmap. Product-specific implementation details belong in the Vincent and CIC Station product roadmaps.

## Program principles

- Vincent remains a useful standalone worker platform.
- CIC Station governs managed-fleet enrollment, authorization, assignments, leases, approvals, health, and operational coordination.
- Git preserves durable technical/project work; product/requirements/ADRs preserve intent; CIC Station restores managed-fleet operation.
- Workers and the control plane are replaceable; durable authoritative work must not depend on one machine or chat thread.
- Product/release evidence is required before declaring milestones complete.

## Milestones

| Milestone | Outcome | Current state |
|---|---|---|
| M0 | Canonical product, requirements, ADR, roadmap, status, and governance model established in both repositories | Complete |
| M1 | Vincent installer and standalone READY path physically proven on heterogeneous hardware; large workstation usable as persistent worker | In progress |
| M2 | Vincent completes bounded real work from an operator-selected source, publishes verified results, maintains itself, and preserves installer/software version separation | Not complete |
| M3 | First managed-worker CIC Station model proven with explicit enrollment, scoped authorization, inventory, bounded assignment, result reporting, and revocation | Planned |
| M4 | Two-worker coordination proves lease ownership, liveness/grace behavior, stale-result protection, replacement, and recovery | Planned |
| M5 | Self-hostable CIC Station API/database plus responsive phone-capable web UI proven | Planned |
| M6 | CIC Station passes its public-release audit and the existing application repository is published under AGPLv3 with self-hosted packaging and a release process | Planned |
| M7 | Multi-project and multi-agent/provider scheduling/identity policy proven with project isolation and capability matching | Planned |
| M8 | Full destructive recovery proves workers and CIC Station can be reconstructed from durable/protected external state; 1.0 acceptance criteria satisfied | Planned |

## Current execution strategy

- Complete Vincent post-consolidation QA, then build and physically verify Installer `0.1.0` build `0022` from the exact accepted `main` source.
- Keep the large workstation online as the first useful persistent Vincent worker and use it for real development work when practical.
- Use the old laptop as the expendable physical installer/recovery test target for repeated clean installs and failure-path tests.
- Do not destroy the productive workstation merely for symmetry; deliberately rebuild it later at the worker-impermanence/recovery acceptance gate.
- Begin CIC Station `0.1.0` application/data-model work in `Gordonfive/cic-station` while preserving the documented operational-data and secret boundaries.

## Cross-product acceptance rules

A milestone is complete only when:

1. required implementation exists;
2. automated validation passes;
3. applicable physical/integration proof has been performed;
4. authoritative results are durable outside the tested worker;
5. relevant requirements/ADRs/status/roadmaps are updated;
6. no unresolved safety or authority contradiction remains.

## Deferred capabilities

Unscheduled future ideas belong in GitHub issues, not this roadmap. Promotion into the roadmap occurs only when the capability is assigned to a concrete product/release milestone.
