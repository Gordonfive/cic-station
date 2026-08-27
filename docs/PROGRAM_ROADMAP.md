# Vincent + Mission Control Program Roadmap

This is the canonical cross-product roadmap. Product-specific implementation details belong in the Vincent and Mission Control product roadmaps.

## Program principles

- Vincent remains a useful standalone worker platform.
- Mission Control governs managed-fleet enrollment, authorization, assignments, leases, approvals, health, and operational coordination.
- Git preserves durable technical/project work; product/requirements/ADRs preserve intent; Mission Control restores managed-fleet operation.
- Workers and the control plane are replaceable; durable authoritative work must not depend on one machine or chat thread.
- Product/release evidence is required before declaring milestones complete.

## Milestones

| Milestone | Outcome | Current state |
|---|---|---|
| M0 | Canonical product, requirements, ADR, roadmap, status, and governance model established in both repositories | In progress — documentation reset underway |
| M1 | Vincent installer and standalone READY path physically proven on heterogeneous hardware; large workstation usable as persistent worker | In progress |
| M2 | Vincent completes bounded real work from an operator-selected source, publishes verified results, maintains itself, and preserves installer/software version separation | Not complete |
| M3 | First managed-worker Mission Control model proven with explicit enrollment, scoped authorization, inventory, bounded assignment, result reporting, and revocation | Planned |
| M4 | Two-worker coordination proves lease ownership, liveness/grace behavior, stale-result protection, replacement, and recovery | Planned |
| M5 | Self-hostable Mission Control API/database plus responsive phone-capable web UI proven | Planned |
| M6 | Reusable Mission Control application lives in a separate public AGPLv3 repository with self-hosted packaging and release process | Planned |
| M7 | Multi-project and multi-agent/provider scheduling/identity policy proven with project isolation and capability matching | Planned |
| M8 | Full destructive recovery proves workers and Mission Control can be reconstructed from durable/protected external state; 1.0 acceptance criteria satisfied | Planned |

## Current execution strategy

- Keep the large workstation online as the first useful persistent Vincent worker and use it for real development work when practical.
- Use the old laptop as the expendable physical installer/recovery test target for repeated clean installs and failure-path tests.
- Do not destroy the productive workstation merely for symmetry; deliberately rebuild it later at the worker-impermanence/recovery acceptance gate.
- Finish the Vincent documentation/installer decision reconciliation before resuming normal ISO development from a clean branch model.
- Begin reusable Mission Control application coding only after the public AGPL application repository boundary is created.

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
