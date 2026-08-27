# ADR-0011: Versioning and Build Identifiers

- Status: Accepted
- Date: 2026-08-27

## Context

Mission Control is a distinct application from Vincent. Vincent is the worker environment/platform; Mission Control is the control application that manages workers. Both products, and the Vincent installer, will undergo many small prototype-stage iterations.

Semantic versions are needed to describe meaningful product/release state. Independent monotonic build numbers are needed to identify exact test iterations without changing the semantic version for every small change.

## Decision

Use Semantic Versioning for all three components:

- Vincent: `0.1.0`
- Vincent installer: `0.1.0`
- Mission Control: `0.1.0`

Each component has an independent build counter:

- Vincent build number: starts at `0001`
- Vincent installer build number: retains its existing sequence, currently `0022`
- Mission Control build number: starts at `0001`

Semantic versions change at meaningful product/release boundaries. Build numbers may increment for small implementation and test iterations while the semantic version stays unchanged.

The three build counters are independent and must not be synchronized or inferred from one another.

## Repository representation

In `Gordonfive/mission-control`:

- `/VERSION` is the Mission Control semantic version.
- `/BUILD_NUMBER` is the Mission Control build number.

Vincent and the Vincent installer maintain their own equivalent identifiers in `Gordonfive/vincent`.

## Consequences

Current identifiers are:

- `Vincent 0.1.0 build 0001`
- `Vincent Installer 0.1.0 build 0022`
- `Mission Control 0.1.0 build 0001`

Independent versioning does not change repository boundaries: Mission Control remains its own control-plane application, while Vincent and its installer remain together in the Vincent repository.
