# Mission Control Planned Features

This document records agreed Mission Control product directions and features that are not yet scheduled for implementation.

## Self-hostable web control plane

Mission Control will be a self-hostable server application with a responsive web interface and authenticated API. Expected deployments include Linux servers, VMs/VPSs, and suitable container/NAS environments. Browser administration avoids platform-specific desktop clients and supports desktop, tablet, and phone operation.

A future hosted Mission Control service may be offered, but self-hosting remains first-class.

## Vincent independence

Vincent remains functional without Mission Control for boot, diagnostics, Debian/system maintenance, Vincent updates, and local health. Mission Control is used when a Vincent worker joins a managed fleet.

## Enrollment, identity, and authorization

Planned features include worker-generated durable identity, explicit enrollment requests, operator approval, revocation, roles, repository/project scopes, and least-privileged assignment-specific authority. Fresh workers begin untrusted.

## Fleet inventory and health

Mission Control should track worker identity, installer provenance, Vincent version, hardware/resources, capabilities, installed AI-agent providers, health, last contact, active assignment, update/policy state, and relevant failures.

## Assignment leasing and liveness

Assignments should use time-bounded leases. Workers renew leases while active; abandoned/expired assignments become eligible for reassignment. Heartbeats indicate worker liveness while leases define work ownership. Temporary connectivity failures should have a grace period, and stale results from expired leases must not silently supersede newer work.

## Results and audit history

Workers should report structured state transitions and outcomes including accepted, started, blocked, approval requested, validation passed/failed, commit/result produced, completed, failed, and lease expired. Mission Control maintains operational/audit history while Git remains authoritative for source and durable project artifacts.

## Human approval gates

Mission Control should support explicit approval gates for destructive hardware actions, production actions, credential expansion, protected merges, releases, and other high-impact operations. Mission Control does not replace human judgment.

## Fleet policy

Mission Control may express fleet policy such as minimum Vincent versions, update channels, staged/canary adoption, maintenance windows, and temporary version pins. Vincent remains responsible for obtaining and applying its software from its trusted upstream.

## Multi-agent scheduling

As Vincent gains support for Codex, Gemini, Copilot, Ollama/local models, and custom agents, Mission Control should understand reported agent capabilities and may select an appropriate worker/agent combination for an assignment.

## Service architecture

Early coordination may remain Git-backed while workflows are proven. The eventual product should separate a browser frontend, authenticated API/application service, persistent database, and worker protocol. Data models should be designed early so Git-backed state can migrate cleanly.

## Network model

Normal worker communication should be initiated outbound by Vincent over an authenticated protocol, allowing workers behind NAT and ordinary firewalls to participate without exposing inbound management ports. Mission Control is not intended to provide an arbitrary remote shell; SSH and standard Linux administration remain separate.

## Public product and private deployment separation

The current Mission Control repository remains private while it contains Gordonfive-specific planning and operational material. If Mission Control becomes a public product, reusable application source should become public/open, while Gordonfive's real fleet state, assignments, authorization information, infrastructure metadata, and deployment configuration remain private and separate from application source.
