# Mission Control and Vincent Roadmap

**Roadmap updated:** 2026-08-27T08:18:00-08:00

This is the private recovery mirror and Mission Control product roadmap. Git is authoritative; Vincent remains the public worker platform.

## Repository authority and product direction

| Repository | Current visibility | Authority |
|---|---|---|
| `Gordonfive/vincent` | Public | Generic Vincent worker platform, Debian ISO/installer, first boot, diagnostics, maintenance/update client, Mission Control client/protocol implementation, runtime, tests, public-safe documentation, releases |
| `Gordonfive/mission-control` | Private today | Our private coordination/control repository and future Mission Control control-plane implementation area: enrollment approval, authorization, inventory, capabilities, roles, repository scopes, assignments, leases, approvals, reports, and control-plane design |

Mission Control is planned as a **self-hostable server application with a web interface and authenticated API**. It is not planned as a desktop application and will not require users to depend exclusively on a Gordonfive-hosted service. A future hosted service may be offered as an option.

If Mission Control becomes a distributable Vincent product, its reusable application source should become public/open. Gordonfive's actual fleet/deployment state, assignments, authorization information, infrastructure metadata, and other private operational material must remain in a separate private deployment/state location. Application source and deployment state are separate concerns.

## Architectural boundary

Vincent must remain independently functional. It can boot, diagnose itself, maintain Debian and its own software, update from its trusted public upstream, and remain healthy without Mission Control.

Mission Control is the managed-fleet control plane. Conceptually, Vincent defines what a worker **can** do; Mission Control determines what an enrolled worker **may** do, what it **should** do, and records what it **is doing**.

A fresh Vincent installation begins untrusted. Enrollment into Mission Control is explicit, scoped, and revocable. Normal Vincent-to-Mission-Control communication should be outbound from the worker over an authenticated protocol so ordinary deployments do not require inbound worker management ports.

Mission Control is not a general-purpose remote shell and does not replace SSH or standard Linux administration.

## Current work

The immediate Vincent priority remains installer/worker proof. Mission Control implementation must not unnecessarily delay a stable generic Vincent worker. Early coordination may remain Git-backed while workflows and data structures are proven.

The current private repository also remains responsible for preserving project recovery and coordination state during consolidation of the historical worker-platform repositories.

## Mission Control product track

1. **Prove the model with Git-backed coordination.** Define durable structures for worker identity, capabilities, assignments, claims/leases, results, and authorization without prematurely building a server.
2. **Enrollment and trust.** Define worker-generated identity, enrollment request, operator approval, scoped authorization, revocation, and credential lifecycle.
3. **Inventory and capabilities.** Record worker identity, Vincent version, installer provenance, hardware/resources, installed AI agents/providers, health, and last contact.
4. **Assignments and leases.** Mission Control creates bounded assignments; workers accept time-bounded leases, renew active work, and allow expired/abandoned work to become eligible for reassignment without stale results superseding newer leases.
5. **Authorization.** Associate workers/roles/assignments with least-privileged repository and project scopes rather than distributing broad credentials.
6. **Results and audit.** Receive structured state transitions and outcomes such as assignment accepted, work started, blocked, validation passed/failed, commit produced, approval requested, completed, or lease expired.
7. **Human approval gates.** Provide explicit approval for destructive operations, production actions, credential expansion, protected merges, releases, and other sensitive operations.
8. **Fleet policy.** Represent minimum Vincent versions, update channels, staged/canary adoption, maintenance windows, and temporary pins without replacing Vincent's own trusted-upstream update mechanism.
9. **Service/API/database.** Once the Git-backed workflow is proven, implement the persistent Mission Control service with authenticated API and database.
10. **Web interface.** Implement a responsive browser UI for enrollment, fleet status, worker details, assignments, approvals, failures, and reports. Phone-first operation remains a milestone.
11. **Self-hosted packaging.** Support straightforward deployment on Linux servers, VMs/VPSs and, where appropriate, containers/NAS environments.
12. **Public product separation.** Before public distribution, move reusable Mission Control application source into a public-safe codebase/repository boundary while keeping Gordonfive deployment state private.
13. **Optional hosted service.** Evaluate a managed Mission Control offering only after self-hosting is established as a first-class supported model.
14. **Multi-agent scheduling.** As Vincent gains Codex/Gemini/Copilot/Ollama/custom-agent adapters, Mission Control may select appropriate worker/agent combinations from reported capabilities and assignment requirements.

## Product milestones

| Milestone | Outcome | Status |
|---|---|---|
| M0 | Architecture and Project DNA accepted | Complete |
| M1 | One disposable generic Vincent worker completes a bounded task | In progress |
| M2 | Worker recovery proven | Not started |
| M3 | Universal installer proven | Prototype / in progress |
| M4 | Two-worker Git coordination and assignment leasing proven | Not started |
| M5 | Phone-first Mission Control control proven | Not started |
| M6 | Self-hostable Mission Control service/API/database proven | Planned |
| M7 | Multi-project operation proven | Not started |
| M8 | Full operation recovery proven | Not started |

## Permanent principles

- Git restores durable technical/project work; Project DNA restores intent; Mission Control restores managed-fleet operational state.
- Vincent workers perform bounded work; Mission Control authorizes, dispatches/leases, observes, and records managed-fleet work.
- Vincent does not depend on Mission Control for basic health, diagnostics, maintenance, or trusted-upstream software updates.
- Mission Control never replaces human judgment for high-impact approval gates.
- Workers are replaceable and least-privileged.
- Public application source and private fleet/deployment state must remain explicitly separated.
- No raw secret belongs in Git.
- Mission Control should use standard authenticated network protocols and avoid unnecessary inbound worker exposure.
- Mission Control is a control plane, not a generic remote-administration shell.
- Durable Git evidence and explicit owner decisions override stale chat summaries.
