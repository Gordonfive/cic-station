# ADR-0013: Operator identity and access-control baseline

**Status:** Accepted
**Decision date:** 2026-08-27

## Context

CIC Station already requires authenticated APIs, authorized enrollment approval, human approval gates, and actor-attributed audit history. Those requirements did not define how human operators are identified, authenticated, authorized, session-scoped, bootstrapped, or recovered.

The initial product is self-hosted. Its security model must therefore work without requiring an external identity provider, while leaving room for optional OIDC/SSO integration later. The baseline should be deliberately small and auditable rather than importing enterprise IAM complexity before it is needed.

## Decision

CIC Station uses distinct human operator identities and supports application-local operator authentication as the baseline self-hosted mechanism.

Authentication establishes identity. Authorization is a separate explicit least-privilege decision; an authenticated operator does not automatically receive unrestricted administrative authority.

The first administrator is established through a one-time bootstrap path. CIC Station does not ship with a reusable default administrator credential. After successful administrator establishment, ordinary bootstrap is disabled or restricted to an explicit administrative recovery procedure.

Interactive browser access uses secure server-side session state with expiration and explicit logout/revocation. High-impact actions may require reauthentication according to policy.

Non-human API/service identities are separate from human operator identities and receive independently scoped, attributable, revocable authority.

CIC Station provides a documented self-hosted recovery path for loss of operator-authentication state. Recovery establishes fresh authority rather than silently restoring prior credentials and preserves attributable recovery evidence where operationally possible.

External OIDC/SSO may be added later as an optional authentication source, but the local self-hosted control/recovery path remains available unless a later ADR deliberately changes that boundary.

## Rationale

A built-in baseline preserves self-hostability and recovery independence. Distinct identities, explicit authorization, revocable sessions, and separate service identities provide a conventional least-privilege security boundary without requiring external infrastructure for the first deployment.

## Consequences

- The 0.1.0 data model must include operator/actor identity, authorization, and session concepts.
- Initial implementation needs a safe first-administrator bootstrap flow and documented administrative recovery procedure.
- Passwords or equivalent reusable operator secrets are never stored in Git; application authentication storage must use appropriate protected credential-verifier mechanisms.
- High-impact approval actions can be attributed to a concrete authenticated operator and can require reauthentication where policy demands it.
- Service/API automation does not impersonate a human operator by reusing browser sessions or shared administrator credentials.
- Optional external identity-provider integration is additive rather than required for baseline operation.

## Related requirements

- `MC-REQ-0061` through `MC-REQ-0067`
