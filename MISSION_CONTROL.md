# Mission Control

## Mission

Coordinate a reproducible software-development worker fleet while preserving human judgment, project authority, and Git-based provenance.

Mission Control does not choose product direction. It reduces repetitive fleet coordination so the owner can concentrate on decisions, risk, and acceptance.

## Roles

- **Owner:** final mission, security, production, enrollment, and architecture authority.
- **ChatGPT:** planning, review, and bounded task direction when authorized.
- **Mission Control:** private enrollment, authorization, dispatch, state tracking, and fleet reporting.
- **Vincent worker:** bounded implementation, validation, publication, reporting, and stop.
- **Project repository:** authoritative source, requirements, project rules, tests, and work history.

## Recovery principle

Git restores durable work and policy. Project documentation restores intent. Mission Control restores private fleet coordination.

## Initial coordination model

Prefer simple Git-backed task records and explicit ownership before building a dedicated distributed service. Workers operate in isolated workspaces, publish commits and reports, surface conflicts, and stop at assignment boundaries.

A fresh Vincent worker is operational without Mission Control and connects to private control sources only after explicit operator configuration and authorization.
