# Mission Control

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

Raw secrets, private keys, passwords, tokens, and authentication caches must not be committed. Store only public keys, fingerprints, credential identifiers, and references to separately protected secrets.

## Canonical task flow

`pending → claimed → completed | failed`

Workers must use isolated workspaces, surface Git conflicts, preserve unexpected dirty work, publish verified results, and stop at the task boundary.
