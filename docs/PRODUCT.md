# Mission Control Product Definition

## Product

Mission Control is the control plane for fleets of Vincent workers.

It coordinates enrollment, identity, authorization, worker inventory, capabilities, assignments, leases, approvals, health, results, audit history, fleet policy, and recovery without turning workers into general-purpose remotely controlled shells.

Mission Control is designed as a self-hostable server application with a responsive browser UI and authenticated API. Self-hosting is first-class; an optional hosted service may be evaluated later.

## Users

Primary users are operators who manage one or more Vincent workers and software projects. The initial deployment is Gordonfive's own fleet; the reusable application is intended to become a public AGPLv3 product when reusable application coding begins.

## Product boundary

Mission Control owns managed-fleet policy and operational coordination. Vincent owns the generic worker: installation, boot, local diagnostics, system/toolchain maintenance, trusted Vincent updates, AI-provider adapters, and bounded task execution.

A fresh Vincent installation must remain useful without Mission Control. Joining Mission Control is explicit enrollment, not a boot dependency.

Project repositories remain authoritative for their own source, product requirements, repository instructions, tests, integration policy, and durable development artifacts. Mission Control coordinates work; it does not replace project authority.

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
- Mission Control is not a remote shell. SSH and normal Linux administration remain separate.
- Raw credentials never belong in Git.
- Reusable AI/provider credentials are never shared fleet-wide.
- High-impact destructive, production, credential-expansion, protected-integration, and release actions retain explicit human approval unless a later ADR deliberately changes the boundary.

## AI-provider boundary

Mission Control may assign the desired AI provider and non-secret identity context such as account, organization, tenant, project, or policy. Vincent performs provider-specific installation/enrollment locally, verifies effective non-secret identity/scope where possible, and reports health/mismatch state.

If unattended provider enrollment is later required, Mission Control must use a separately protected secret-delivery mechanism with unique, scoped, rotatable, revocable credentials. Git is never the secret transport.

## Public application and private deployment separation

The current `Gordonfive/mission-control` repository is private because it contains Gordonfive-specific program planning and may contain private fleet/deployment state.

When reusable Mission Control application coding begins, the reusable application source will be established in a separate public AGPLv3 repository from the start. Private fleet state, assignments, authorization records, infrastructure metadata, and secrets/references remain outside that public source repository.

## Non-goals

Mission Control is not intended to be:

- a general remote administration shell;
- a replacement for Git or project repositories;
- a requirement for standalone Vincent health or maintenance;
- an autonomous production authority by default;
- a massive distributed scheduler before a smaller design proves insufficient;
- tied exclusively to Codex, GitHub, one operating system for the server, or a Gordonfive-hosted service.

## Success

Mission Control succeeds when an operator can safely manage a fleet from a browser, assign bounded development work, understand worker and task state, approve consequential actions, recover from failures, replace workers, and preserve durable results without depending on physical access to individual workers or transient conversations.
