# CIC Station Architecture

## Product boundary

CIC Station is the managed-fleet control plane. Vincent is the worker platform. Project repositories remain authoritative for project source, requirements, tests, repository-local instructions, and durable development artifacts.

A fresh Vincent worker does not require CIC Station. CIC Station authority begins after explicit enrollment.

## Logical layers

1. **Web UI** — responsive authenticated operator interface for enrollment, fleet status, worker details, assignments, approvals, failures, reports, and policy.
2. **Authenticated API/application service** — authenticates operator/service identities and worker identities, enforces authorization, workflow/state transitions, leases, approval gates, session lifecycle, and audit recording.
3. **Persistent operational database** — stores operator/role state, worker registry, enrollment state, capabilities, leases, health, policy, audit events, notification state, and other operational data that is not appropriate for Git.
4. **Worker protocol** — authenticated encrypted outbound Vincent connections for registration, heartbeat, assignment/lease exchange, provider-profile policy, results, and health.
5. **Durable project authorities** — Git repositories containing source, product/requirements, ADRs, tasks where applicable, commits, reports, and project-specific rules.
6. **Protected secret system** — separate mechanism for any future unattended credential delivery; raw secrets do not live in Git or ordinary fleet records.

## Data authority

| Data | Canonical authority |
|---|---|
| Project source, product requirements, repository instructions, commits | Project Git repository |
| CIC Station product requirements/ADRs/program roadmap | CIC Station Git repository |
| Operator identities, roles/permissions, and session state | CIC Station service/database once implemented |
| Worker identity/enrollment/authorization state | CIC Station service/database once implemented |
| Worker heartbeat and current liveness | CIC Station operational state |
| Assignment lease ownership | CIC Station operational state |
| Durable task result/source changes | Project Git plus CIC Station audit/reference |
| Installer provenance and current Vincent version | Reported by Vincent; recorded by CIC Station |
| Raw credentials | Protected secret store/local protected worker storage, never Git |

Early Git-backed coordination is permitted while the model is being proven, but the data model must not assume Git remains the high-frequency operational database.

## Operator identity and access control

The baseline self-hosted deployment supports application-local operator accounts so CIC Station does not depend on an external identity provider to remain operable. External OIDC/SSO integration may be added later without replacing the local recovery/control boundary.

Each human operator has a distinct identity. Authentication establishes identity; authorization separately determines which fleet-control operations that identity may perform. The initial model should remain small and explicit rather than importing enterprise IAM complexity before it is needed, but it must preserve least privilege and avoid treating every authenticated operator as an unrestricted administrator.

The first administrator is established through an explicit one-time bootstrap path. CIC Station must not ship with a reusable default administrator credential. After the first administrator is created, bootstrap capability is disabled or restricted to an explicit recovery procedure.

Interactive browser access uses secure server-side session state. Sessions expire and support explicit logout/revocation. High-impact actions may require reauthentication according to policy. Browser session cookies and equivalent credentials must receive the normal protections appropriate to their transport and client context.

Non-human API/service identities are separate from interactive human operators. They receive their own bounded scope, lifecycle, revocation, and audit attribution rather than borrowing a human session or shared administrator identity.

Operator-authentication recovery is an explicit self-hosted administrative procedure. Recovery may rely on trusted local host administration, but it must establish fresh authority rather than silently resurrecting old credentials and must preserve an attributable recovery/audit record where operationally possible.

## Transport security

Real operator/API and routine Vincent-to-CIC-Station communication is encrypted in transit using TLS or equivalent authenticated encryption. Plaintext communication is limited to explicitly local non-production development that carries no real credentials or operational data.

TLS termination may occur in CIC Station itself or at a trusted deployment boundary such as a reverse proxy. A deployment must not introduce an unprotected network hop across a trust boundary merely because TLS terminates upstream.

This baseline does not require mutual TLS. Worker authentication credentials, certificate/bootstrap mechanics, reverse-proxy choice, and certificate-authority strategy remain implementation decisions to be defined by the worker-protocol and deployment design while satisfying the authenticated-encrypted transport requirement.

## Worker connection model

Normal worker communication is initiated outbound by Vincent over an authenticated encrypted protocol. This allows workers behind NAT and ordinary firewalls to participate without inbound management ports.

CIC Station exposes bounded operations and state transitions, not arbitrary shell execution. SSH remains an independent administrative fallback.

## Enrollment and trust

1. Vincent generates a unique installation identity.
2. The worker presents a non-secret enrollment request.
3. An authenticated and authorized operator verifies and approves the request.
4. CIC Station grants scoped, revocable authority.
5. The worker registers capabilities and health.
6. Reinstallation normally creates a new identity unless an explicit recovery path restores the old one.

## Assignments and leases

Assignments describe bounded work and hard requirements. CIC Station may explicitly select a worker or choose one by capabilities.

Exclusive managed work uses time-bounded leases. Heartbeats show liveness but do not replace lease ownership. A worker that loses or cannot verify its lease must not continue publishing exclusive results indefinitely. Reassignment is conservative when network state is uncertain.

Lease clock authority and skew/restart semantics are intentionally deferred to the 0.3.0 lease-design gate tracked separately; implementations must not infer unsafe ownership merely from synchronized wall-clock assumptions.

## AI-provider identity boundary

CIC Station may assign the desired provider and non-secret identity context. Vincent owns provider installation, provider-specific enrollment, local credential storage, and effective-identity/health verification.

CIC Station receives only non-secret effective identity/scope/status information needed to detect mismatches and enforce policy.

If unattended provider credentials are required later, a protected secret broker or one-time delivery mechanism must provide unique/scoped/rotatable/revocable credentials over authenticated encrypted transport. Shared fleet-wide AI credentials are prohibited.

## Recovery

The CIC Station service is replaceable. Recovery should reconstruct durable product/project knowledge from Git, restore private deployment configuration from protected operational backups, start the service/database, restore or deliberately recover operator access, request fresh worker registrations/heartbeats, expire or reconcile uncertain leases conservatively, and resume dispatch only after ownership is safe.

Loss of CIC Station must not destroy project source, product intent, completed work, or the ability to rebuild workers.

## Repository and operational-data boundary

`Gordonfive/cic-station` contains the reusable application code, schemas, safe examples, tests, packaging, and product documentation. It remains private during development and may become the public AGPLv3 source repository at an explicit owner-approved release gate.

Gordonfive fleet data is application data: operator identities/authorization state, worker identities, enrollment and authorization state, assignments, results, leases, and audit history belong in the deployed operational database and protected backups. Raw secrets and private production configuration remain outside Git. Publication requires an audit of the complete Git history and proposed release contents.
