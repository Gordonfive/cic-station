# Mission Control and Vincent Roadmap

This is the private recovery mirror of the shared Vincent / Mission Control roadmap. It exists so the project can be reconstructed from Git without access to the previous ChatGPT project.

## Repository authority

| Repository | Visibility | Authority |
|---|---|---|
| `Gordonfive/vincent` | Public | Generic Vincent worker platform, Debian ISO, installer, bootstrap/first boot, enrollment client, worker runtime, tests, public-safe documentation, releases, preserved public legacy history |
| `Gordonfive/mission-control` | Private | Fleet enrollment approval, authorization, inventory, roles, repository scopes, assignments, private coordination, private reports, private control-plane configuration |
| `Gordonfive/codex-worker-platform` | Private legacy | Migration source only; scheduled for deletion after verified consolidation |
| `Gordonfive/GitBoy` | Public legacy | Migration/provenance source only; scheduled for deletion after verified consolidation |

Git is authoritative. Project DNA records intent. Chat history is disposable.

## Current shared state — 2026-08-25

Vincent migration and ISO evidence currently live on non-default Vincent branches and must be inspected before consolidation:

- accepted migration/ISO-testing source: `fc032f8df1c0abde295122a8a515e9cdcf7c7b70`
- durable owner acceptance record: `d6fb92a6a07905dc29a1431b17d2a953abd5fbc8`
- Workstream 2 correction code: `3a6abb330fb11faffbd638b101ed11dca47f4216`
- Workstream 2 correction/report branch tip: `4edd5e95a403d605664402a7b1dc2d5c4f53b71b`
- Workstream 2 branch: `workstream/ws2-iso-corrections`

The first Vincent ISO built from the accepted source was rejected by the obsolete-name gate because stale generated GitBoy package metadata remained embedded. The rejected image must not be flashed. The correction removes that material, fixes script executable bits, and strengthens the ISO validation workflow.

Complete native legacy histories were already copied into Vincent under `legacy/*`, but final consolidation still requires checking all current legacy refs and moving any private control-plane material that belongs here rather than in the public repository.

## Primary Workstream A — Consolidate and retire legacy repositories

This is the first primary task.

1. Fetch all refs from Vincent, Mission Control, `codex-worker-platform`, and `GitBoy`.
2. Inventory every branch, tag, report, Project DNA/architecture document, workflow, configuration, task/coordination record, and unresolved change.
3. Re-verify native Git history preservation instead of assuming file-level copies are sufficient.
4. Move/merge generic worker implementation and public-safe history into Vincent.
5. Move/merge private control-plane information into Mission Control, including:
   - enrollment approval records and policy;
   - worker/fleet inventory and roles;
   - repository/project scopes;
   - assignment/claim coordination records;
   - private infrastructure metadata that is appropriate for Git;
   - private fleet reports and recovery state.
6. Never commit raw secrets, passwords, tokens, private keys, authentication caches, reusable enrollment credentials, or production data. Store only safe configuration/references needed to reconstruct authority.
7. Reconcile duplicate architecture, authority, security, Project DNA, and roadmap material so the new repositories do not drift into contradictory sources of truth.
8. Remove active dependencies on legacy repository URLs/names and obsolete GitBoy identifiers, preserving them only where historical provenance requires them.
9. Run tests, secret scans, public/private-boundary scans, obsolete-name scans, link/reference checks, and source/destination ref comparisons.
10. Prove a clean ChatGPT/Codex environment connected only to the two new repositories can recover the system and continue work.
11. Record exact consolidation commits in both repositories.
12. **Owner directive dated 2026-08-25:** once preservation/consolidation is proven, delete `Gordonfive/codex-worker-platform` and `Gordonfive/GitBoy`. This supersedes the older planning dependency that postponed deletion until ISO acceptance. Never delete them before preservation proof completes.
13. After deletion, verify no active recovery, bootstrap, workflow, documentation, or coordination path requires either old repository.

Acceptance: Vincent and Mission Control alone contain all required code, history, intent, public/private state, reports, and recovery instructions.

## Primary Workstream B — Resume Vincent ISO creation and testing

This is the second primary task and may run in a separate ChatGPT thread.

Mission Control's role is to preserve the authority boundary around the public worker:

1. A fresh Vincent installation creates its own local identity/request.
2. It has no private/project authority before explicit approval.
3. Enrollment/authorization must be scoped and revocable.
4. Public Vincent must not contain Mission Control inventory, authorization state, private assignments, credentials, or reusable fleet secrets.
5. ISO validation and physical-install work must not require embedding Mission Control secrets into the image.

Vincent ISO recovery state:

- accepted source `fc032f8df1c0abde295122a8a515e9cdcf7c7b70` produced a rejected ISO because of obsolete GitBoy metadata;
- rejected ISO SHA-256: `bcebd5fed3c82f86c7259b8dd71297e99057f630698c1742e4461265b78842a2`;
- correction code: `3a6abb330fb11faffbd638b101ed11dca47f4216`;
- correction/report tip: `4edd5e95a403d605664402a7b1dc2d5c4f53b71b`;
- no USB had been identified or flashed at handoff time;
- no release or production/project authority had been granted.

The replacement image must be built from one exact reviewed/authorized source commit and must pass repository tests, Debian source verification, payload inspection, manifest/checksum verification, embedded-commit verification, credential/identity scans, and active obsolete-name scanning before flashing is considered.

Physical testing then requires exact target-device identification and authorization, fresh whole-disk guided-LVM install, persistent networking, `vincent-worker-NNNNNN`, local login, SSH, Git, GitHub CLI, Docker, DDEV, Codex, Vincent, local identity generation, scoped enrollment/revocation, one harmless real task, and a second clean install for reproducibility.

## Product milestones

| Milestone | Outcome | Status |
|---|---|---|
| M0 | Architecture and Project DNA accepted | Complete |
| M1 | One disposable Vincent worker completes a bounded task | In progress |
| M2 | Worker recovery proven | Not started |
| M3 | Universal installer proven | Prototype / in progress |
| M4 | Two-worker coordination proven | Not started |
| M5 | Phone-first control proven | Not started |
| M6 | Mission Control proven | Not started |
| M7 | Multi-project operation proven | Not started |
| M8 | Full operation recovery proven | Not started |

## Permanent principles

- Git restores work; Project DNA restores intent; Mission Control restores operation.
- ChatGPT selects priorities and worker assignment; Mission Control dispatches/records; Vincent workers perform bounded work and report.
- Mission Control never replaces human judgment.
- Workers are replaceable and least-privileged.
- Public and private authority boundaries must remain explicit.
- No raw secret belongs in Git.
- Durable Git evidence and explicit owner decisions override stale chat summaries.
