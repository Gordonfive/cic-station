# ADR-0003: Outbound authenticated worker protocol

**Status:** Accepted
**Decision date:** 2026-08-27

## Context

Workers may sit behind NAT and ordinary firewalls. CIC Station needs bounded fleet operations, not arbitrary host administration.

## Decision

Routine Vincent-to-CIC-Station communication will be initiated outbound by Vincent over an authenticated protocol. CIC Station will expose bounded fleet operations/state transitions and will not require general inbound worker management ports for normal operation.

CIC Station is not a remote shell; SSH and standard Linux administration remain separate.

## Rationale

Outbound connections simplify deployment and reduce attack surface while preserving clear control-plane semantics.

## Consequences

- Worker protocol design must support registration, heartbeat, assignments/leases, policy, approvals/results, and health over authenticated channels.
- General shell access is outside the product API.
