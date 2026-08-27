# ADR-0002: Separate public application source from private deployment state

**Status:** Superseded by ADR-0010
**Decision date:** 2026-08-27

## Context

The current repository contains private Gordonfive program/deployment concerns, while the reusable Mission Control application is intended to become a public open-source product.

## Decision

When reusable Mission Control application coding begins, create a separate public application repository immediately. Keep Gordonfive fleet state, assignments, authorization records, infrastructure metadata, and private deployment configuration out of that public source repository.

This decision was superseded after confirming that no current Git content requires a third repository and that future private fleet information is application data belonging in the deployed database and protected systems.

## Rationale

Splitting at the beginning avoids later secret/history cleanup and makes the public/private boundary architectural rather than procedural.

## Consequences

- This private repository remains authoritative for program planning and private deployment/fleet state.
- Reusable application source, tests, schemas, packaging, and public docs will live in the future public AGPLv3 repository.

## Superseded by

- `ADR-0010-single-application-repository-private-until-release.md`
