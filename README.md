# Mission Control

Mission Control is the private control plane for Vincent worker deployments.

Vincent builds and operates generic workers. Mission Control owns private fleet enrollment approval, authorization, inventory, roles, repository scopes, assignments, and fleet-level reporting. Individual project repositories remain authoritative for their own source, requirements, rules, tests, and work history.

## Documentation

- `docs/README.md` — documentation index and maintenance rules.
- `docs/STATUS.md` — current state and immediate priorities.
- `docs/ROADMAP.md` — strategic milestones.
- `MISSION_CONTROL.md` — operating model.
- `docs/coordination/decisions.md` — accepted decisions.

## Authority

- The owner controls mission, security, production access, enrollment, and major architecture.
- ChatGPT may provide planning, review, and bounded task direction.
- Mission Control records and coordinates authorized fleet work.
- Vincent workers implement, validate, publish, report, and stop at task boundaries.
- Git is the durable technical authority.

## Repository boundary

This repository may contain:

- approved worker inventory and public identity fingerprints;
- worker roles, capabilities, resource limits, and repository scopes;
- project registrations and assignment records;
- enrollment, suspension, revocation, and recovery policy;
- fleet-level reports and private infrastructure references that are safe to keep in Git.

This repository must not contain raw passwords, access tokens, private keys, authentication caches, reusable enrollment credentials, or production data. Store only safe identifiers, public keys/fingerprints, policy, and references to separately protected secrets.

A fresh Vincent installation is generic and does not automatically contact Mission Control. Private control-plane authority is granted only through explicit operator-approved configuration and enrollment.
