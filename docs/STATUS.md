# CIC Station Status

**Updated:** 2026-08-28

## Repository state

- The repository rename from `Gordonfive/mission-control` to `Gordonfive/cic-station` is complete; `Gordonfive/cic-station` is the canonical control-plane repository.
- `Gordonfive/cic-station` remains private during development and is the canonical home for the reusable CIC Station application plus its product/program documentation.
- A third application repository is not planned. Private fleet information will be stored as deployed application data, with secrets and production configuration outside Git.
- CIC Station is currently `0.1.0` build `0001`.
- No CIC Station service, API, database schema, or web UI implementation has started yet; the repository currently contains the canonical product/governance/security/protocol model and validation scaffolding.
- `main` is the only permanent branch; automatic deletion of merged temporary branches is enabled.
- GitHub branch-protection/ruleset enforcement is intentionally deferred until the public-release gate on the current repository plan. PR, CI, squash-merge, no-force-push, and branch-cleanup rules remain procedural requirements while private.

## Current program state

- The canonical documentation/governance reset is complete in both CIC Station and Vincent.
- Vincent's ISO consolidation is integrated on `main`; Vincent remains in post-consolidation QA before physical Installer `0.1.0` build `0022` verification.
- Vincent QA/fix activity remains separate from CIC Station implementation and is tracked in the Vincent repository rather than duplicated here.
- The large workstation is intended to remain the first useful persistent Vincent worker and future first managed-worker CIC Station subject.
- The old laptop remains the expendable installer/recovery test target.
- CIC Station's first implementation proof may use conservative Git-backed coordination, but the product architecture is a self-hosted API/database/web application.
- The 0.1.0 operator-security baseline includes distinct operator identities, self-hostable local authentication, explicit least-privilege authorization, one-time first-admin bootstrap, revocable server-side sessions, separate service identities, administrative authentication recovery, and encrypted real operator/worker transport.
- The approved worker-trust baseline uses a worker-generated asymmetric installation credential, operator approval bound to the exact public identity, proof-of-possession on subsequent connections, replay-resistant enrollment/bootstrap, explicit credential rotation/revocation/recovery transitions, and fail-closed CIC Station server-trust verification.
- The approved worker-protocol baseline is explicitly versioned independently of product SemVer, declares compatibility rather than guessing, assumes network retries/duplicates can occur, uses stable idempotency identity for retryable state changes, and rejects stale/conflicting/out-of-order state transitions rather than relying on arrival order.
- External OIDC/SSO, mTLS, asymmetric algorithm choice, hardware-backed keys, certificate-authority selection, reverse-proxy choice, REST/WebSocket/gRPC selection, and serialization format remain optional/later implementation decisions rather than baseline dependencies.
- Reusable CIC Station application coding may begin in this repository under the documented source/operational-data, worker-trust, protocol, and security boundaries.

## Current blockers / gates

- Vincent post-consolidation QA and physical build-0022 verification remain incomplete.
- The large workstation has not yet completed the persistent bounded-work worker proof required before the first managed-worker integration proof.
- CIC Station implementation must keep operational data, worker private credentials, secrets, and private production configuration out of Git.
- Vincent client requirements/implementation must be aligned with the approved CIC Station worker-trust and protocol contract before the first managed-worker proof.
- Lease clock authority/skew/restart semantics remain to be defined before the 0.3.0 multi-worker lease implementation.

## Next actions

1. Complete Vincent post-consolidation QA and physical Installer `0.1.0` build `0022` verification.
2. Bring the large workstation fully online as a bounded-work Vincent worker.
3. Align Vincent with the approved asymmetric worker identity, proof-of-possession, server-trust, protocol-versioning, and retry/idempotency contract.
4. Define and begin the CIC Station `0.1.0` application structure and data models for operators, workers/public identities, enrollment/authorization, protocol compatibility, assignments, results, and audit state.
5. Preserve the documented security/protocol boundaries without treating early Git-backed coordination as the permanent operational architecture.
