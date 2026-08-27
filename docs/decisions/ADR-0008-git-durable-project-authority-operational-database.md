# ADR-0008: Git for durable project authority; database for operational fleet state

**Status:** Accepted
**Decision date:** 2026-08-27

## Context

Early coordination can use Git, but high-frequency heartbeats, leases, and live fleet state are a poor fit for commit-based storage. At the same time, Mission Control must not become the sole authority for source or product intent.

## Decision

Git remains authoritative for durable project/source/product artifacts. The Mission Control service/database owns operational fleet state such as enrollment status, worker registry, heartbeats, leases, health, notification state, and operational audit where appropriate.

Mission Control records references/results needed for fleet coordination but does not replace project Git as source authority.

## Rationale

The split uses each storage system for the semantics it handles well and keeps the control plane replaceable.

## Consequences

- Early Git-backed prototypes must preserve a migration path to the service/database.
- Control-plane recovery must reconcile operational state from backups plus fresh worker/project state.
