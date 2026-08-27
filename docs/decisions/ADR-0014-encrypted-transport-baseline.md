# ADR-0014: Encrypted transport baseline

**Status:** Accepted
**Decision date:** 2026-08-27

## Context

CIC Station already requires authenticated operator/API operations and authenticated outbound Vincent communication. Authentication alone does not provide confidentiality or integrity for fleet metadata, assignments, results, authorization state, session credentials, or worker-control traffic while crossing a network.

CIC Station must remain practical to self-host across direct application, reverse-proxy, VM/VPS, and container deployments without hard-coding one certificate authority or network topology.

## Decision

Real operator browser/API traffic and routine Vincent-to-CIC-Station communication use TLS or equivalent authenticated encryption in transit.

Plaintext transport is permitted only for explicitly local non-production development that carries no real credentials or operational data.

TLS termination may occur in CIC Station itself or at a trusted deployment boundary such as a reverse proxy. Deployments must not introduce an unprotected network hop across a trust boundary merely because encryption terminates upstream.

This baseline does not require mutual TLS. Worker authentication/bootstrap credential mechanics, certificate-authority choice, reverse-proxy choice, and certificate automation remain later implementation/deployment decisions provided they satisfy authenticated encrypted transport requirements.

## Rationale

Encryption in transit is a baseline control-plane safety property. Requiring the property while leaving termination and certificate-management topology flexible preserves self-hostability and avoids prematurely coupling the product to one proxy, CA, VPN, or hosting model.

## Consequences

- Operator login/session credentials and fleet-management API traffic may not traverse untrusted networks in plaintext.
- Routine worker enrollment, heartbeats, assignments, results, health, and authorization traffic require encrypted transport when carrying real fleet state.
- Deployment documentation must make TLS termination and any internal trust boundary explicit.
- A trusted reverse proxy is supported, but any downstream network hop that crosses a trust boundary must remain protected.
- mTLS may be adopted later if worker identity/bootstrap design warrants it; it is not a 0.1.0 requirement.

## Related requirements

- `MC-REQ-0003`
- `MC-REQ-0009`
- `MC-REQ-0068`
