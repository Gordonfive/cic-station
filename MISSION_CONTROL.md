# Mission Control

## Mission

Restore and coordinate a reproducible software-development operation while preserving human judgment, project intent, and Git authority.

Mission Control does not replace developers and does not autonomously choose product direction. It reduces repetitive coordination so the owner can concentrate on decisions.

## Roles

- **Owner:** final mission, security, production, enrollment, and architecture authority.
- **ChatGPT:** product direction, planning, review, and worker assignment.
- **Mission Control:** durable dispatch, claiming, state tracking, and fleet reporting.
- **Vincent worker:** bounded implementation, validation, publication, reporting, and stop.
- **Project repository:** authoritative Product DNA, source, rules, tests, and work history.

## Recovery principle

Git restores the work. Project DNA restores the intent. Mission Control restores the operation.

## Initial coordination model

Use simple Git-backed polling and machine-readable task records. Assignments require explicit ownership. Workers operate in isolated workspaces and publish commits and reports. Failures remain visible and recoverable.
