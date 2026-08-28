# ADR-0016: Explicitly versioned, retry-safe worker protocol

**Status:** Accepted
**Decision date:** 2026-08-28

## Context

Vincent and CIC Station will evolve independently and communicate across networks that may disconnect, duplicate requests, delay messages, or cause callers to retry after uncertain outcomes. Product Semantic Versions alone do not define the exact logical worker/control-plane protocol contract.

Assuming exactly-once delivery or silently accepting incompatible messages could duplicate state changes, regress authoritative assignment state, or make mixed-version failures ambiguous.

## Decision

The Vincent/CIC Station worker protocol is explicitly versioned independently of product Semantic Versions. Exchanges carry enough protocol/schema-version information to determine whether the sender and receiver have a declared compatible interpretation.

Compatibility is explicit through supported versions/ranges or equivalent declared rules. If the peers cannot establish a compatible interpretation, the operation fails visibly and safely rather than guessing, silently ignoring incompatible behavior, or applying unknown state transitions.

The protocol does not assume exactly-once network delivery. Operations that may be retried after timeout, reconnect, or uncertain response use stable operation/request/event/assignment identifiers or equivalent idempotency identity so duplicate delivery can be detected and handled safely.

State transitions must include sufficient identity/version/generation/precondition information to detect stale, superseded, conflicting, or out-of-order updates. Older messages may not silently overwrite newer authoritative state.

Protocol compatibility information is exposed in diagnostics, worker inventory, and release metadata sufficiently to identify why a Vincent/CIC Station pairing is compatible or incompatible.

The logical protocol contract remains independent of transport selection. This ADR does not choose REST, WebSocket, SSE, gRPC, message queues, serialization format, or database concurrency primitives.

## Rationale

Explicit compatibility prevents ambiguous mixed-version behavior. Idempotent retry semantics reflect ordinary distributed-system failure modes and avoid relying on impossible exactly-once network guarantees. Separating logical protocol semantics from transport keeps implementation choices open while making correctness requirements durable.

## Consequences

- CIC Station and Vincent must maintain a protocol/schema version identity distinct from their product SemVer values.
- Release metadata must map product versions to supported worker-protocol versions/ranges.
- Retryable state-changing operations need stable idempotency identity.
- Assignment delivery, acknowledgements, results, approvals, enrollment-state transitions, and similar operations must define duplicate/stale handling where applicable.
- State machines require explicit stale/conflict detection rather than last-write-wins by arrival order.
- Incompatible peers fail visibly and expose diagnostic compatibility information.

## Related requirements

- `MC-REQ-0031` through `MC-REQ-0033`
- `MC-REQ-0057`
- `MC-REQ-0077` through `MC-REQ-0082`
