# Mission Control Requirements

Requirement identifiers are permanent once merged to `main`. Superseded or withdrawn requirements retain their IDs and history; IDs are never reused.

## Product and deployment

- **MC-REQ-0001 — Self-hostable control plane.** Mission Control must be deployable as a self-hosted server application.
- **MC-REQ-0002 — Browser UI.** Mission Control must provide a responsive web interface suitable for desktop, tablet, and phone operation.
- **MC-REQ-0003 — Authenticated API.** Mission Control must expose authenticated programmatic operations for supported fleet-management workflows.
- **MC-REQ-0004 — Optional hosted service.** Any future hosted service must not weaken self-hosting as a first-class deployment model.
- **MC-REQ-0005 — Independent versioning.** Mission Control uses its own Semantic Versioning lifecycle, independent of Vincent and installer builds.
- **MC-REQ-0006 — Public/private separation.** Reusable Mission Control application source must remain separate from private deployment/fleet state.

## Vincent independence and network boundary

- **MC-REQ-0007 — Vincent independence.** Vincent must remain capable of installation, boot, diagnostics, maintenance, trusted updates, and standalone operation without Mission Control.
- **MC-REQ-0008 — Explicit enrollment.** Mission Control authority begins only after explicit worker enrollment.
- **MC-REQ-0009 — Outbound worker connection.** Routine worker/control-plane communication must be initiated outbound by Vincent where practical.
- **MC-REQ-0010 — No general remote shell.** Mission Control must not expose arbitrary shell execution as its ordinary fleet-control interface.

## Identity, enrollment, and authorization

- **MC-REQ-0011 — Unique worker identity.** Every installation enrolled into Mission Control must have a distinct durable security identity.
- **MC-REQ-0012 — Enrollment request.** A fresh worker must present inspectable non-secret enrollment information before authorization.
- **MC-REQ-0013 — Explicit approval.** Enrollment must require an authorized approval action.
- **MC-REQ-0014 — Revocation.** One worker's authority must be revocable without disabling unrelated workers.
- **MC-REQ-0015 — Least privilege.** Repository/project/operation scope must be limited to what the worker or assignment requires.
- **MC-REQ-0016 — Reinstallation identity safety.** Reinstallation must not silently regain the previous installation's authority unless an explicit recovery mechanism permits it.
- **MC-REQ-0017 — Role separation.** Worker identity, hardware identity, role, and current assignment must be distinct concepts.

## Inventory and health

- **MC-REQ-0018 — Fleet inventory.** Mission Control must track enrolled worker identities and lifecycle state.
- **MC-REQ-0019 — Software inventory.** Mission Control must record current Vincent version and immutable installer provenance where reported.
- **MC-REQ-0020 — Capability inventory.** Mission Control must record relevant worker capabilities, hardware/resources, and installed AI-provider support.
- **MC-REQ-0021 — Health state.** Mission Control must represent worker health and last-contact state without treating intentional idleness as failure.
- **MC-REQ-0022 — Version policy visibility.** Mission Control must be able to express and report fleet version/update policy without replacing Vincent's trusted update mechanism.

## Assignments, leases, and liveness

- **MC-REQ-0023 — Bounded assignments.** Work assignments must specify objective, scope, authority, constraints, and acceptance expectations.
- **MC-REQ-0024 — Explicit ownership.** Exclusive work must have unambiguous ownership.
- **MC-REQ-0025 — Time-bounded leases.** Managed assignments must support leases with explicit owner, duration, renewal, and expiration semantics.
- **MC-REQ-0026 — Conservative reassignment.** Temporary loss of connectivity must not immediately cause unsafe duplicate execution.
- **MC-REQ-0027 — Stale-result protection.** Results from expired or superseded leases must not silently supersede newer authoritative work.
- **MC-REQ-0028 — Heartbeats distinct from leases.** Liveness signals may inform worker state but do not by themselves define task ownership.
- **MC-REQ-0029 — Explicit assignment precedence.** A valid explicit worker assignment must not be silently rerouted by ordinary capability scheduling.
- **MC-REQ-0030 — Capability matching.** When no explicit worker is selected, scheduling may use declared hard requirements and worker capabilities.

## Results, audit, and approvals

- **MC-REQ-0031 — Structured task state.** Mission Control must represent meaningful assignment states such as queued, active, blocked, approval-required, completed, failed, expired, cancelled, and superseded.
- **MC-REQ-0032 — Durable result references.** Mission Control must record structured results and references to durable project artifacts/commits without replacing Git as source authority.
- **MC-REQ-0033 — Audit history.** Important fleet-control changes must record actor, action, time, and resulting state.
- **MC-REQ-0034 — Human approval gates.** Consequential destructive, production, credential-expansion, protected-integration, and release actions require explicit approval unless later policy deliberately changes the boundary.
- **MC-REQ-0035 — Decision durability.** Decisions that affect continuing work must be durable and auditable rather than existing only in chat.
- **MC-REQ-0036 — Emergency pause.** The operator must have a fleet-level mechanism to stop new ordinary work without destroying existing work.

## AI-provider identity and credentials

- **MC-REQ-0037 — Provider profile assignment.** Mission Control may assign desired AI provider plus non-secret account/organization/tenant/project context and authentication policy.
- **MC-REQ-0038 — Vincent-owned provider enrollment.** Provider-specific installation, enrollment, and local credential-health checks remain Vincent responsibilities.
- **MC-REQ-0039 — Provider mismatch visibility.** A mismatch between intended and effective provider identity/scope must block or surface clearly rather than silently proceed.
- **MC-REQ-0040 — No reusable AI credentials in Git.** Reusable provider credentials must never be stored in Git.
- **MC-REQ-0041 — No fleet-wide shared AI credential.** Unattended provider access must use unique or appropriately scoped revocable credentials rather than a single shared fleet credential.
- **MC-REQ-0042 — Protected secret delivery.** Any unattended credential delivery must use an authenticated protected mechanism supporting scope, rotation, and revocation.

## Data, architecture, and recovery

- **MC-REQ-0043 — Durable/ephemeral separation.** Git remains authoritative for durable project artifacts while high-frequency fleet state may live in the Mission Control database/service.
- **MC-REQ-0044 — Replaceable control plane.** Loss of a Mission Control instance must not destroy source history, product intent, or completed project artifacts.
- **MC-REQ-0045 — Recovery reconciliation.** On control-plane restart, uncertain leases/worker state must be reconciled conservatively before dispatch resumes.
- **MC-REQ-0046 — Multi-project support.** Mission Control must support multiple projects without allowing one project's rules to become unintended global policy.
- **MC-REQ-0047 — Multiple repositories per project.** Projects may reference multiple repositories with explicit modification scope.
- **MC-REQ-0048 — Project activation state.** Projects may be active, paused, under maintenance, or archived without losing durable state.
- **MC-REQ-0049 — Worker replacement.** Retired/replaced workers must retain historical identity for audit while replacement identities receive fresh authority.
- **MC-REQ-0050 — Full recovery.** The program must eventually prove recovery after loss/replacement of workers and the control plane using durable external state.

## Operations, security, and release

- **MC-REQ-0051 — Secret minimization.** Private fleet state may contain secret references/identifiers but raw secrets must remain in a protected secret system.
- **MC-REQ-0052 — Credential rotation.** Worker/control-plane credentials must support documented rotation and emergency revocation.
- **MC-REQ-0053 — Production boundary.** Ordinary development workers must not receive broad production authority merely for convenience.
- **MC-REQ-0054 — Observable failure.** Failures and blocked states must expose meaningful operational context and preserved-state information.
- **MC-REQ-0055 — Notification deduplication.** Notification adapters must avoid repeated identical alerts for unchanged state.
- **MC-REQ-0056 — Maintenance/drain state.** Workers undergoing planned maintenance must stop receiving new assignments and preserve active work according to policy.
- **MC-REQ-0057 — Release traceability.** Mission Control releases must identify exact source, version, relevant protocol compatibility, known limitations, and validation evidence.
- **MC-REQ-0058 — Release changelog.** A concise `CHANGELOG.md` must be maintained at release boundaries.
- **MC-REQ-0059 — AGPLv3 application license.** Reusable public Mission Control application source must use AGPLv3.
- **MC-REQ-0060 — External contributions deferred.** Outside pull requests are not accepted until the owner intentionally reopens contribution policy at 1.0 or later.

## Requirement maintenance

New requirements receive the next unused `MC-REQ-####` identifier through normal pull-request review. Requirements are implementation-neutral statements of what must be true; implementation choices belong in architecture documents and ADRs.
