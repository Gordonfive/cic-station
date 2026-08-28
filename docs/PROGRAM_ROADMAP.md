# Vincent + CIC Station Program Roadmap

This is the canonical cross-product roadmap. Product-specific implementation details belong in the Vincent and CIC Station product roadmaps.

## Program principles

- Vincent remains a useful standalone worker platform.
- CIC Station governs managed-fleet enrollment, authorization, assignments, leases, approvals, health, operational configuration, and coordination.
- Git preserves durable technical/project work; product/requirements/ADRs preserve intent; CIC Station restores managed-fleet operation.
- Workers and the control plane are replaceable; durable authoritative work must not depend on one machine or chat thread.
- Product/release evidence is required before declaring milestones complete.
- Generic Vincent and CIC Station releases must support independent self-hosted deployments without requiring a Gordonfive-operated rendezvous, registry, pairing, or relay service.
- Public Internet access is not a prerequisite for Vincent/CIC Station enrollment when the two products have a mutually reachable private network path.

## Milestones

| Milestone | Outcome | Current state |
|---|---|---|
| M0 | Canonical product, requirements, ADR, roadmap, status, and governance model established in both repositories | Complete |
| M1 | Vincent installer and standalone READY path physically proven on heterogeneous hardware; large workstation usable as persistent worker | In progress |
| M2 | Vincent completes bounded real work from an operator-selected source, publishes verified results, maintains itself, and preserves installer/software version separation | Not complete |
| M3 | First managed-worker CIC Station model proven through the persistent operational service/database with explicit decentralized enrollment, scoped authorization, inventory, bounded work-item/attempt execution, result reporting, revocation, and managed operational configuration | Planned |
| M4 | Two-worker coordination proves persistent lease ownership, liveness/grace behavior, stale-result protection, replacement, and recovery | Planned |
| M5 | CIC Station service/database operational hardening plus responsive phone-capable web UI, deployment/recovery workflows, and supported direct/private/tunneled connectivity modes proven | Planned |
| M6 | CIC Station passes its public-release audit and the existing application repository is published under AGPLv3 with self-hosted packaging and a release process | Planned |
| M7 | Multi-project and multi-agent/provider scheduling/identity policy proven with project isolation, capability matching, centrally assigned worker network/egress policy, and managed software/source delivery where required | Planned |
| M8 | Full destructive recovery proves workers and CIC Station can be reconstructed from durable/protected external state; 1.0 acceptance criteria satisfied | Planned |

## Current execution strategy

- Complete Vincent post-consolidation QA and physical installer verification from exact accepted `main` source.
- Keep the large workstation online as the first useful persistent Vincent worker and use it for real development work when practical.
- Use the old laptop as the expendable physical installer/recovery test target for repeated clean installs and failure-path tests.
- Do not destroy the productive workstation merely for symmetry; deliberately rebuild it later at the worker-impermanence/recovery acceptance gate.
- Begin CIC Station `0.1.0` application/domain-model work with the minimum persistent service/API/database foundation from the start; do not make Git the authoritative live lease/heartbeat database.
- Resolve CIC Station work-item/attempt/lease/result modeling and multidimensional worker-state semantics before database schemas harden.
- Implement managed enrollment from the accepted decentralized model: CIC Station supplies its reachable endpoint plus a single-use bootstrap authorization; Vincent initiates the connection and binds its worker-generated asymmetric identity to that CIC Station.
- Preserve same-subnet/private-address enrollment and make CIC Station reachability independent from public Internet/provider/package-source availability.
- Treat CIC Station as the managed operational-policy authority after enrollment, including direct/proxied/restricted network mode and future managed software/source delivery.

## Enrollment and connectivity direction

The accepted cross-product design is recorded in `docs/decisions/ADR-0019-decentralized-enrollment-and-worker-egress-policy.md` and the corresponding Vincent ADR.

Key program constraints:

- generic Vincent installer and generic CIC Station application;
- no mandatory central pairing/rendezvous service;
- CIC Station enrollment remains optional for Vincent standalone operation;
- CIC Station must complete its administrator/security bootstrap before it can issue worker enrollment material;
- bootstrap input consists of a reachable CIC Station endpoint plus a one-time, expiring, case-insensitive 16-character alphanumeric key presented as `XXXX-XXXX-XXXX-XXXX`;
- bootstrap material is invalidated after successful enrollment and never becomes the permanent worker credential;
- Vincent initiates normal control-plane connections, so workers require no inbound management exposure;
- CIC Station may be public, port-forwarded, reachable through an operator-chosen reverse tunnel/VPN/overlay, or private/local-only;
- private IP and private DNS endpoints are valid, including networks with no public Internet access;
- CIC Station may assign worker network mode as direct, CIC-proxied, external-proxy, or restricted/offline;
- CIC Station may cache/deliver approved software and act as a policy-controlled worker egress gateway, but should not become an unrestricted transparent proxy by default.

## Program planning structure

Vincent and CIC Station remain two separate products and two separate repositories with independent SemVer/release lifecycles. Program planning should be unified above the repository boundary.

A separate project-management thread is expected to create a single GitHub Project spanning both repositories. That GitHub Project should become the shared planning/triage view for cross-product work while repository-local issues, PRs, code, product requirements, ADRs, releases, and histories remain authoritative in their respective repositories.

Recommended project setup notes for that thread:

- include issues and pull requests from both `Gordonfive/vincent` and `Gordonfive/cic-station`;
- distinguish `Vincent`, `CIC Station`, and `Cross-product` work with a Product field rather than merging repositories;
- include Status, Priority, Target release/milestone, Work type, and Dependency/blocked state fields;
- use the program milestones M0-M8 as the cross-product planning layer while preserving each product's own SemVer roadmap;
- do not duplicate requirement or ADR authority into Project fields; link to the authoritative repository documents/issues instead;
- use the GitHub Project for planning visibility, not as an operational CIC Station database or replacement for Git history;
- preserve the trunk-based rule that `main` is the only permanent branch in each repository.

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
