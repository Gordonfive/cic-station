# ADR-0015: Worker-generated asymmetric identity and bootstrap

**Status:** Accepted
**Decision date:** 2026-08-28

## Context

CIC Station requires unique worker identities, explicit enrollment, independent revocation, encrypted transport, and an authenticated outbound worker protocol. Those properties are insufficient unless CIC Station can distinguish a worker that merely claims an identifier from the exact Vincent installation whose enrollment was approved.

A fleet-wide shared secret would couple compromise and rotation across workers. Issuing reusable worker private credentials from CIC Station would also make the control plane a repository of worker authentication secrets and weaken worker replacement/recovery isolation.

## Decision

Each Vincent installation generates its own asymmetric installation credential before enrollment. The private credential remains protected on that Vincent worker. The enrollment request exposes only the corresponding public identity/fingerprint and other non-secret enrollment information.

Operator approval binds CIC Station authority to that exact public identity. Subsequent authenticated worker connections must prove possession of the corresponding private credential; a claimed worker ID by itself is never sufficient authentication.

Any additional enrollment/bootstrap token or challenge used to connect the untrusted worker request with operator approval is bounded, expires, and is single-use wherever reuse could confer authority. Enrollment and credential-transition flows must resist replay and credential substitution.

CIC Station stores the worker public/verifier material and authorization state needed to authenticate the worker, but not the worker private credential.

Worker credential rotation, suspension, revocation, replacement, and recovery are explicit auditable state transitions. A credential may be replaced while preserving an existing worker record only through an authorized transition that binds the new credential. Reinstallation otherwise creates fresh worker authority rather than silently inheriting the previous installation credential.

Vincent verifies CIC Station's authenticated transport identity and fails closed on invalid or untrusted server identity. A deliberately defined bootstrap/recovery mechanism may establish initial trust, but it may not silently weaken established server trust.

This ADR does not choose a key algorithm, key container, TPM requirement, certificate authority, or mutual-TLS design. mTLS remains one possible implementation of the proof-of-possession contract rather than a requirement.

## Rationale

A worker-generated asymmetric identity gives each installation an independently revocable credential, allows CIC Station to authenticate proof of possession without holding the worker's private secret, and lets operator approval bind to an inspectable public identity. It also reduces fleet-wide blast radius and makes replacement/recovery transitions explicit.

## Consequences

- Vincent must generate and protect a private installation credential and expose only its public identity/fingerprint for enrollment.
- CIC Station's worker data model must distinguish worker records, current authentication credential/public identity, lifecycle state, and authorization state.
- Enrollment approval must be bound to the exact presented public identity rather than only hostname, hardware metadata, or a user-entered worker name.
- Worker authentication and bootstrap flows require replay/substitution resistance.
- Credential lifecycle events must be auditable and independently revocable.
- CIC Station does not store reusable worker private credentials.
- Vincent server-trust verification is part of the worker security boundary.

## Related requirements

- `MC-REQ-0011` through `MC-REQ-0016`
- `MC-REQ-0052`
- `MC-REQ-0068`
- `MC-REQ-0069` through `MC-REQ-0076`
