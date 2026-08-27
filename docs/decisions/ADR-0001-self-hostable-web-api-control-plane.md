# ADR-0001: Self-hostable web/API control plane

**Status:** Accepted
**Decision date:** 2026-08-27

## Context

CIC Station must support routine fleet operation from desktop and phone without requiring a platform-specific desktop client or dependence on a Gordonfive-hosted service.

## Decision

CIC Station will be a self-hostable server application with a responsive browser UI, authenticated API/application service, and persistent operational database.

Self-hosting is first-class. A hosted service may be evaluated later as an optional deployment model.

## Rationale

A browser/server architecture is portable, remotely accessible, compatible with phone-first operation, and naturally supports authenticated worker/API communication.

## Consequences

- Product architecture targets server deployment rather than desktop packaging.
- API and data models must remain usable independently of the UI.
- Packaging must eventually support practical Linux server/VM/VPS/container deployment.
