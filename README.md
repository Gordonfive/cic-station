# Mission Control

> **Project recovery:** a fresh ChatGPT/Codex project should begin with `docs/PROJECT_START_HERE.md`, then read `docs/ROADMAP.md` and `docs/CONTINUATION_HANDOFF.md` in this repository and in `Gordonfive/vincent`.

Mission Control is the private control plane for the owner's Vincent worker fleet.

Vincent builds and operates generic workers. Mission Control enrolls, authorizes, assigns, observes, suspends, and retires those workers. Individual project repositories remain authoritative for their own Product DNA, source, commands, tests, tasks, and reports.

## Authority

- The owner controls mission, security, production access, and major architecture.
- ChatGPT provides product direction and bounded assignments.
- Mission Control dispatches and tracks work.
- Vincent workers implement, test, report, and stop.
- Git is the durable technical authority.

## Repository boundary

This repository owns:

- approved worker inventory and public identity fingerprints;
- worker roles, capabilities, resource limits, and repository scopes;
- project registrations;
- durable task assignments and fleet-level reports;
- enrollment, suspension, revocation, and recovery policy;
- private infrastructure references that do not belong in public Vincent.

Raw secrets, private keys, passwords, tokens, authentication caches, reusable enrollment credentials, and production data must not be committed. Store only safe public keys, fingerprints, credential identifiers, and references to separately protected secrets.

## Canonical task flow

`pending → claimed → completed | failed`

Workers must use isolated workspaces, surface Git conflicts, preserve unexpected dirty work, publish verified results, and stop at the task boundary.

## Current project reset

The owner is replacing the current ChatGPT project with a clean one. The durable roadmap and continuation state are stored in `docs/`. The two active priorities are: complete consolidation into Vincent/Mission Control and then delete the legacy repositories after preservation proof; and resume corrected Vincent ISO creation/testing. See `docs/ROADMAP.md`.
