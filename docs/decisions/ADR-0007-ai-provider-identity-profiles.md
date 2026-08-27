# ADR-0007: AI provider identity profiles

**Status:** Accepted
**Decision date:** 2026-08-27

## Context

Vincent is intended to support Codex first and later additional AI providers/agents. Managed workers need to use the intended provider identity/account/project without putting reusable credentials in Git.

## Decision

CIC Station may assign a worker's desired AI provider plus non-secret account/organization/tenant/project context and authentication policy. Vincent performs provider-specific installation and enrollment locally through its adapter, verifies effective non-secret identity/scope where possible, and reports enrollment/health/mismatch state.

Provider mismatch must block or surface clearly rather than silently use an unintended identity.

Reusable AI credentials never belong in Git. Any future unattended credential delivery must use authenticated protected delivery with unique/scoped/rotatable/revocable credentials. Shared fleet-wide AI credentials are prohibited.

## Rationale

This keeps provider-specific authentication logic on the worker while allowing CIC Station to manage intended identity/policy in a provider-neutral way.

## Consequences

- Codex begins with supported device/ChatGPT interactive authorization where available.
- Future adapters may support other interactive, OAuth/device, SSO, scoped service/API, or local-model mechanisms without changing the core fleet model.
