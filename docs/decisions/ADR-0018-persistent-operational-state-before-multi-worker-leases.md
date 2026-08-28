# ADR-0018: Persistent operational state precedes multi-worker lease coordination

**Status:** Accepted
**Decision date:** 2026-08-28

## Context

ADR-0008 establishes that high-frequency fleet state such as enrollment status, heartbeats, leases, health, and operational audit belongs in CIC Station's operational service/database rather than Git. The initial product roadmap scheduled multi-worker lease coordination in 0.3.0 and the persistent service/API/database in 0.4.0. That sequencing would require proving the hardest ownership/recovery semantics against a temporary Git-backed operational model and then replacing the authority mechanism immediately afterward.

## Decision

CIC Station introduces the minimum persistent application service/API/database foundation before the multi-worker lease proof.

The 0.1.0/0.2.0 path establishes enough transactional operational storage and service behavior to support the first managed-worker proof. Multi-worker lease ownership, renewal, expiration, stale-result protection, and reconciliation in 0.3.0 are proven against that operational authority rather than against Git as the live lease database.

Git-backed coordination may still be used for durable project artifacts, fixtures, migration/prototype evidence, or bounded transitional mechanisms, but it is not the authoritative runtime store for multi-worker lease ownership.

The later service/database milestone becomes operational hardening: migrations, backup/restore, upgrades, deployment, reconciliation, observability, and recovery rather than introducing the operational authority for the first time.

## Rationale

Lease ownership and reassignment are distributed-systems correctness boundaries. Proving them once against the intended authoritative persistence model avoids throwaway semantics, reduces migration risk, and aligns roadmap sequencing with ADR-0008.

## Consequences

- CIC Station 0.1.0 includes the minimum persistent data/service foundation needed for the domain model.
- CIC Station 0.2.0 proves the first managed worker through that service/database path.
- CIC Station 0.3.0 proves multi-worker leases, liveness, stale-result handling, and recovery against persistent operational authority.
- CIC Station 0.4.0 focuses on hardening persistence/service operations rather than first introducing them.
- The program roadmap must no longer imply that a production-shaped API/database appears only after the multi-worker proof.

## Relationship

This refines roadmap sequencing under ADR-0001 and ADR-0008. It does not change Git's role as durable project/source authority.

## Owner approval

Approved 2026-08-28 during the Vincent/CIC architecture review.
