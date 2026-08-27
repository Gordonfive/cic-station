# CIC Station Product Definition

## Product

CIC Station is the control plane for fleets of Vincent workers.

It coordinates enrollment, identity, authorization, worker inventory, capabilities, assignments, leases, approvals, health, results, audit history, fleet policy, and recovery without turning workers into general-purpose remotely controlled shells.

CIC Station is designed as a self-hostable server application with a responsive browser UI and authenticated API. Self-hosting is first-class; an optional hosted service may be evaluated later.

## Users

Primary users are operators who manage one or more Vincent workers and software projects. The initial deployment is Gordonfive's own fleet. The repository remains private during development and is intended to become a public AGPLv3 product at an explicit owner-approved release gate.

## Product boundary

CIC Station owns managed-fleet policy and operational coordination. Vincent owns the generic worker: installation, boot, local diagnostics, system/toolchain maintenance, trusted Vincent updates, AI-provider adapters, and bounded task execution.

A fresh Vincent installation must remain useful without CIC Station. Joining CIC Station is explicit enrollment, not a boot dependency.

Project repositories remain authoritative for their own source, product requirements, repository instructions, tests, integration policy, and durable development artifacts. CIC Station coordinates work; it does not replace project authority.

## Core goals

1. Let an operator enroll and revoke workers without rebuilding the fleet.
2. Represent worker identity, health, resources, capabilities, software versions, and AI-provider capability accurately.
3. Dispatch bounded work with explicit ownership and time-bounded leases.
4. Prevent stale or duplicate workers from silently superseding newer authoritative work.
5. Preserve human approval for consequential actions while automating routine coordination.
6. Support phone-first operation through a responsive web interface.
7. Recover operational control after worker or control-plane loss without depending on chat history or undocumented local state.
8. Support multiple workers, projects, and AI providers without hard-coding one vendor or project.

## Security principles

- Fresh workers begin untrusted.
- Enrollment is explicit, authenticated, scoped, and revocable.
- Normal worker/control-plane communication is initiated outbound by Vincent; inbound worker management ports are not required for routine fleet operation.
- CIC Station is not a remote shell. SSH and normal Linux administration remain separate.
- Raw credentials never belong in Git.
- Reusable AI/provider credentials are never shared fleet-wide.
- High-impact destructive, production, credential-expansion, protected-integration, and release actions retain explicit human approval unless a later ADR deliberately changes the boundary.

## AI-provider boundary

CIC Station may assign the desired AI provider and non-secret identity context such as account, organization, tenant, project, or policy. Vincent performs provider-specific installation/enrollment locally, verifies effective non-secret identity/scope where possible, and reports health/mismatch state.

If unattended provider enrollment is later required, CIC Station must use a separately protected secret-delivery mechanism with unique, scoped, rotatable, revocable credentials. Git is never the secret transport.

## Application source and operational-data separation

`Gordonfive/cic-station` is the reusable application repository. It remains private during development and may become the public AGPLv3 source repository at an explicit release gate.

Private worker inventory, fleet state, assignments, authorization records, results, and audit history belong in the deployed database and protected backups rather than Git. Secrets and private production configuration remain in protected deployment and secret systems. Publication requires a complete repository-history and release-content audit.

## Non-goals

CIC Station is not intended to be:

- a general remote administration shell;
- a replacement for Git or project repositories;
- a requirement for standalone Vincent health or maintenance;
- an autonomous production authority by default;
- a massive distributed scheduler before a smaller design proves insufficient;
- tied exclusively to Codex, GitHub, one operating system for the server, or a Gordonfive-hosted service.

## Success

CIC Station succeeds when an operator can safely manage a fleet from a browser, assign bounded development work, understand worker and task state, approve consequential actions, recover from failures, replace workers, and preserve durable results without depending on physical access to individual workers or transient conversations.
