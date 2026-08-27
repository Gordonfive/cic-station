# Mission Control and Vincent Roadmap

**Roadmap updated:** 2026-08-27T11:49:00-08:00

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

## Current physical-development strategy

The large workstation is the first persistent Vincent worker and the first real Mission Control development subject. Bring it fully online as a worker now and use it together with ChatGPT/GitHub to begin implementing and exercising Mission Control concepts.

The old laptop is the disposable Vincent/installer test target. Repeated clean installs, installer changes, networking/first-boot tests, destructive failure-path tests, and other high-churn physical validation should occur there whenever possible so the large workstation remains available for productive development.

The large workstation should not be reinstalled merely for routine installer regression testing. Its deliberate destruction/rebuild is reserved for the later worker-impermanence/recovery acceptance gate, or another test that specifically requires proving clean reconstruction of a previously useful worker.

This gives Mission Control development a stable first worker to manage while Vincent installer development proceeds independently on expendable hardware.

## Current work

Immediate priorities are now parallel rather than serial:

1. Bring the large workstation online as a useful persistent Vincent worker.
2. Begin Mission Control development using that worker as the first real managed-worker subject, initially with Git-backed coordination where practical.
3. Continue Vincent/installer physical testing on the laptop without destabilizing the large workstation.
4. Preserve the eventual requirement to prove worker impermanence by intentionally rebuilding the large workstation only when the recovery milestone is ready for acceptance testing.

The current private repository also remains responsible for preserving project recovery and coordination state during consolidation of the historical worker-platform repositories.

## Mission Control product track

1. **First real worker.** Use the large workstation as the initial persistent Vincent worker and development target for Mission Control behavior.
2. **Prove the model with Git-backed coordination.** Define durable structures for worker identity, capabilities, assignments, claims/leases, results, and authorization without prematurely building a server.
3. **Enrollment and trust.** Define worker-generated identity, enrollment request, operator approval, scoped authorization, revocation, and credential lifecycle.
4. **Inventory and capabilities.** Record worker identity, Vincent version, installer provenance, hardware/resources, installed AI agents/providers, health, and last contact.
5. **Assignments and leases.** Mission Control creates bounded assignments; workers accept time-bounded leases, renew active work, and allow expired/abandoned work to become eligible for reassignment without stale results superseding newer leases.
6. **Authorization.** Associate workers/roles/assignments with least-privileged repository and project scopes rather than distributing broad credentials.
7. **AI identity profiles and agent enrollment.** Let Mission Control assign a worker's AI provider plus intended account/organization/tenant/project context and authentication policy. Vincent performs provider-specific enrollment locally through an adapter, verifies non-secret effective identity/scope where possible, and reports enrollment/health state. Begin with Codex device/ChatGPT authorization where supported; keep the design provider-neutral for future agents.
8. **Protected secret delivery.** Keep reusable AI credentials out of Git. If unattended provider enrollment is later required, define a protected secret broker/backend or one-time delivery mechanism using authenticated transport, unique least-privileged worker/provider credentials, rotation, and revocation. Never introduce a shared fleet-wide AI credential.
9. **Results and audit.** Receive structured state transitions and outcomes such as assignment accepted, work started, blocked, validation passed/failed, commit produced, approval requested, completed, or lease expired.
10. **Human approval gates.** Provide explicit approval for destructive operations, production actions, credential expansion, protected merges, releases, and other sensitive operations.
11. **Fleet policy.** Represent minimum Vincent versions, update channels, staged/canary adoption, maintenance windows, and temporary pins without replacing Vincent's own trusted-upstream update mechanism.
12. **Second worker and leases.** Use the laptop as a second worker when appropriate to prove multi-worker coordination, lease expiration/reassignment, and replacement behavior.
13. **Service/API/database.** Once the Git-backed workflow is proven, implement the persistent Mission Control service with authenticated API and database.
14. **Web interface.** Implement a responsive browser UI for enrollment, fleet status, worker details, assignments, approvals, failures, and reports. Phone-first operation remains a milestone.
15. **Self-hosted packaging.** Support straightforward deployment on Linux servers, VMs/VPSs and, where appropriate, containers/NAS environments.
16. **Public product separation.** Before public distribution, move reusable Mission Control application source into a public-safe codebase/repository boundary while keeping Gordonfive deployment state private.
17. **Optional hosted service.** Evaluate a managed Mission Control offering only after self-hosting is established as a first-class supported model.
18. **Multi-agent scheduling.** As Vincent gains Codex/Gemini/Copilot/Ollama/custom-agent adapters, Mission Control may select appropriate worker/agent combinations from reported capabilities and assignment requirements.

## Worker impermanence and recovery acceptance

Worker replaceability is a required property, but it should be tested deliberately rather than by repeatedly destroying productive hardware.

The laptop provides routine reinstall/recovery evidence during development. Later, after the large workstation has performed useful work and Mission Control/Git hold the required durable state, deliberately wipe/reinstall or otherwise invalidate that workstation's local Vincent state and prove that:

- authoritative project work was not trapped on the worker;
- the worker can be reconstructed from supported Vincent installation/update paths;
- identity/enrollment replacement or recovery behaves according to the final security model;
- stale leases/credentials/state cannot silently regain authority;
- Mission Control can recognize the loss/replacement and restore appropriate assignments or capabilities;
- normal operation resumes without relying on undocumented local state.

That test is the meaningful proof of worker impermanence.

## Product milestones

| Milestone | Outcome | Status |
|---|---|---|
| M0 | Architecture and Project DNA accepted | Complete |
| M1 | Large workstation online as persistent Vincent worker and completing bounded work | In progress |
| M2 | Laptop clean-install/recovery cycle proven; later large-workstation impermanence/rebuild proven | Not started |
| M3 | Universal installer proven through repeated laptop testing | Prototype / in progress |
| M4 | Two-worker Git coordination and assignment leasing proven | Not started |
| M5 | Phone-first Mission Control control proven | Not started |
| M6 | Self-hostable Mission Control service/API/database proven | Planned |
| M7 | Multi-project operation proven | Not started |
| M8 | Full operation recovery proven | Not started |

## Permanent principles

- Git restores durable technical/project work; Project DNA restores intent; Mission Control restores managed-fleet operational state.
- Vincent workers perform bounded work; Mission Control authorizes, dispatches/leases, observes, and records managed-fleet work.
- Vincent does not depend on Mission Control for basic health, diagnostics, maintenance, or trusted-upstream software updates.
- Mission Control may assign AI-provider identity/profile policy, but Vincent performs provider-specific enrollment and reports only non-secret identity/status data.
- AI-provider credentials are unique/scoped/revocable where applicable and never stored in Git; shared fleet-wide AI credentials are prohibited.
- Mission Control never replaces human judgment for high-impact approval gates.
- Workers are replaceable and least-privileged, but productive workers are not destroyed unnecessarily merely to exercise that principle.
- Destructive worker-recovery testing occurs at an explicit acceptance gate with durable state already preserved elsewhere.
- Public application source and private fleet/deployment state must remain explicitly separated.
- No raw secret belongs in Git.
- Mission Control should use standard authenticated network protocols and avoid unnecessary inbound worker exposure.
- Mission Control is a control plane, not a generic remote-administration shell.
- Durable Git evidence and explicit owner decisions override stale chat summaries.
