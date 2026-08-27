# ADR-0006: Human approval gates for consequential actions

**Status:** Accepted
**Decision date:** 2026-08-27

## Context

CIC Station exists to remove repetitive coordination, not to eliminate human authority over high-impact actions.

## Decision

Explicit human approval remains required for consequential destructive actions, production actions, credential expansion, protected integration/merge actions, releases, and comparable high-impact operations unless a later ADR deliberately changes a specific boundary.

Routine bounded development coordination may be automated within previously approved scope.

## Rationale

The platform should concentrate human attention on judgment rather than operational repetition while preserving clear blast-radius controls.

## Consequences

- Approval requests and answers are durable/auditable workflow objects.
- Workers must stop safely at approval boundaries rather than repeatedly invoking an AI agent against an unresolved decision.
