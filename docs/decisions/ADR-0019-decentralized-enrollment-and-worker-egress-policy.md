# ADR-0019: Decentralized enrollment and worker egress policy

**Status:** Accepted  
**Decision date:** 2026-08-28

## Context

Vincent and CIC Station are intended for many independent self-hosted deployments. A universal Vincent installer and generic CIC Station application must not depend on a Gordonfive-operated rendezvous, registry, pairing, or relay service in order to establish trust. Deployments must also support workers and CIC Station behind NAT, private-only networks, and networks with no public Internet access.

The existing architecture already requires explicit enrollment, worker-generated asymmetric identity, replay-resistant bootstrap material, authenticated encrypted transport, and routine worker-initiated control-plane communication. This decision specifies how peers locate one another, how bootstrap authorization works, and how CIC Station governs worker network egress after enrollment.

## Decision

### Generic products and no central rendezvous dependency

Vincent installation media and CIC Station releases remain generic. CIC Station enrollment must not require a central Gordonfive discovery, pairing, SSO, rendezvous, or relay service.

A short code cannot by itself identify an arbitrary network location without a registry. Therefore the enrollment bootstrap must convey a CIC Station endpoint directly to Vincent. The endpoint may be a public DNS name, private DNS name, routable IP address, or same-subnet private IP address.

### CIC Station security gate before enrollment

A newly deployed CIC Station instance must not issue worker enrollment material until required administrative and transport-security bootstrap steps are complete. At minimum the implementation must establish administrator authority, installation identity/secrets, authenticated encrypted transport or an explicitly safe local bootstrap trust mechanism, and required security self-tests before worker enrollment is enabled.

### Single-use human-readable bootstrap key

CIC Station may generate a human-enterable bootstrap key formatted as four groups of four case-insensitive alphanumeric characters, for example `7K3M-P9XR-2WQF-8DNT`.

The key is bootstrap authorization only. It must be random, bounded in lifetime, single-use, invalidated after successful enrollment, protected from replay, and must never become the worker's permanent credential. Hyphens are presentation separators and are not part of the entropy calculation.

Equivalent QR encoding may be provided as a convenience, but QR is only another representation of the endpoint plus bootstrap material and does not define a separate trust model.

### Worker-initiated enrollment and permanent identity

Vincent generates and protects its asymmetric installation credential locally as already required by ADR-0015. The operator supplies Vincent with the CIC Station endpoint and one-time bootstrap key. Vincent initiates the network connection to CIC Station, presents the bootstrap authorization and worker public identity, proves possession as required by the protocol, and completes an explicit approval/binding flow.

After successful enrollment, CIC Station invalidates the bootstrap key. The durable relationship is based on the worker-generated asymmetric identity and authenticated CIC Station identity, not the bootstrap key.

### NAT and reachability

Routine worker/control-plane communication remains worker-initiated. Workers therefore require no general inbound port exposure and may operate behind ordinary NAT or CGNAT as long as they can reach the configured CIC Station endpoint.

CIC Station may be reachable through any deployment-owned method that preserves authenticated end-to-end semantics, including direct public HTTPS, operator-managed port forwarding, reverse tunnels, VPN/overlay networks, or private routing. CIC Station does not require one specific tunnel or VPN provider.

If neither side has a mutually reachable path, communication is impossible without an intermediary; the product must not hide that constraint by introducing a mandatory shared relay.

### Offline and isolated-network enrollment

Enrollment requires network reachability between Vincent and CIC Station, not public Internet access. A worker and CIC Station on the same isolated subnet may enroll using a private IP address or private DNS endpoint.

Internet, Git hosting, package repositories, AI-provider endpoints, and other external capabilities are evaluated separately. Their absence may limit useful work but must not prevent a valid Vincent/CIC Station trust relationship from being established or maintained.

### CIC Station as operational configuration authority

After enrollment, CIC Station is authoritative for managed-worker operational policy. Vincent retains only the local bootstrap/recovery information necessary to locate and authenticate CIC Station and enforce received policy safely.

CIC Station must be able to assign worker connectivity policy at least conceptually as:

- **direct** — worker accesses approved external services directly;
- **CIC-proxied** — worker uses CIC Station as its controlled egress path where supported;
- **external-proxy** — CIC Station supplies policy/configuration for an operator-selected proxy or gateway;
- **restricted/offline** — worker is limited to CIC Station and explicitly permitted internal resources.

Policies may be assigned per worker, group, role, enrollment profile, or later equivalent policy object.

### CIC Station software distribution and egress gateway role

CIC Station may distribute or cache approved Vincent updates, packages, agent/provider components, assignment payloads, container artifacts, and other software required by managed workers. This enables deployments where only CIC Station has approved Internet egress.

If CIC Station provides worker Internet egress, it should be an authenticated policy-controlled worker gateway rather than an unrestricted general-purpose transparent proxy. Access should be limited by worker identity and explicit policy, with destination/service restrictions and auditable outcomes where practical.

CIC Station may instead configure workers to use a separate proxy or gateway. Vincent should obtain these operational settings from CIC Station rather than requiring independent manual configuration on each managed worker.

## Rationale

This design keeps Vincent and CIC Station self-hostable and decentralized, eliminates a mandatory global pairing service as a high-value attack and availability target, works naturally with worker-side NAT, supports air-gapped and same-subnet deployments, and allows organizations to centralize worker egress through a hardened CIC Station or separate proxy.

It also preserves the existing separation between bootstrap authorization and permanent worker identity: short human-entered material authorizes a one-time binding operation while long-lived authentication uses independently revocable asymmetric credentials.

## Consequences

- Vincent enrollment UX must accept a CIC Station endpoint plus one-time bootstrap key; QR may encode the same information.
- CIC Station must issue and invalidate single-use bootstrap keys only after its enrollment security gate is satisfied.
- Vincent must support CIC Station endpoints expressed as public/private DNS names and routable IP addresses, including same-subnet private addresses.
- Public Internet access is not an enrollment prerequisite.
- Worker inbound management ports are not part of the normal architecture.
- CIC Station deployment documentation must distinguish direct, tunneled, VPN/private, and local-only reachability without making one provider mandatory.
- Managed worker networking becomes centrally policy-driven through CIC Station.
- CIC Station proxy/software-distribution capability must be designed with least privilege and must not silently become unrestricted network transit.
- Standalone Vincent operation remains valid and CIC Station enrollment remains optional.

## Related decisions and requirements

- ADR-0003 — outbound authenticated worker protocol
- ADR-0004 — explicit enrollment and revocation
- ADR-0014 — encrypted transport baseline
- ADR-0015 — worker-generated asymmetric identity and bootstrap
- ADR-0016 — explicitly versioned, retry-safe worker protocol
- `MC-REQ-0007` through `MC-REQ-0010`
- `MC-REQ-0068` through `MC-REQ-0082`
