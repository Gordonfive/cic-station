# ADR-0003: Outbound authenticated worker protocol

**Status:** Accepted
**Decision date:** 2026-08-27

## Context

Workers may sit behind NAT and ordinary firewalls. Mission Control needs bounded fleet operations, not arbitrary host administration.

## Decision

Routine Vincent-to-Mission-Control communication will be initiated outbound by Vincent over an authenticated protocol. Mission Control will expose bounded fleet operations/state transitions and will not require general inbound worker management ports for normal operation.

Mission Control is not a remote shell; SSH and standard Linux administration remain separate.

## Rationale

Outbound connections simplify deployment and reduce attack surface while preserving clear control-plane semantics.

## Consequences

- Worker protocol design must support registration, heartbeat, assignments/leases, policy, approvals/results, and health over authenticated channels.
- General shell access is outside the product API.
