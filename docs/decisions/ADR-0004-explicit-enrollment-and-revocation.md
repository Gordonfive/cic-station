# ADR-0004: Explicit enrollment and independent revocation

**Status:** Accepted
**Decision date:** 2026-08-27

## Context

A fresh Vincent installation must not automatically inherit fleet authority, and one compromised/replaced worker must not force fleet-wide credential rotation.

## Decision

Fresh workers begin untrusted. Each installation generates a unique identity, submits inspectable enrollment information, receives explicit authorized approval, and is granted scoped revocable authority. Reinstallation normally creates a new identity unless an explicit recovery path restores the previous one.

## Rationale

This separates installation from trust and makes worker replacement/revocation routine.

## Consequences

- Enrollment, suspension, revocation, and replacement are first-class lifecycle states.
- Credentials/authority are per-worker or appropriately scoped, never silently shared across the fleet.
