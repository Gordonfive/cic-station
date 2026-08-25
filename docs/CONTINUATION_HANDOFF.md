# Continuation Handoff — Mission Control Project Reset

Date: 2026-08-25 (America/Sitka)

Purpose: preserve enough durable state in Git that the current ChatGPT project can be deleted and a new project can resume without loss of intent or coordination context.

## Mission

Mission Control is the private fleet control plane for Vincent workers. It coordinates operation; it does not replace human judgment or choose product direction. Vincent is the public replaceable worker platform.

## Immediate owner priorities

1. **Consolidate all required state into `Gordonfive/vincent` and `Gordonfive/mission-control`, verify preservation, then delete `Gordonfive/codex-worker-platform` and `Gordonfive/GitBoy`.**
2. **Resume Vincent ISO creation/testing from the corrected Workstream 2 state.**

These may be separate ChatGPT threads, but Git must be the only coordination authority between them.

## New-session procedure

1. Fetch both new repositories plus all branches/tags.
2. Read `AGENTS.md`, `docs/PROJECT_START_HERE.md`, `docs/ROADMAP.md`, and this file in both repositories.
3. Inspect all Vincent migration/legacy/Workstream 2 branches before altering default branches.
4. Reconcile newer Git commits if branch tips have advanced since this handoff.
5. Keep private control-plane state here and generic/public worker implementation in Vincent.
6. Push all material decisions, reports, and continuation state back into Git before ending a thread.

## Consolidation handoff

The Vincent migration already preserved complete native history for the known legacy branch tips, including:

- `codex-worker-platform` main `0f6e93bb8cccc26edf8887eb50641ae0fe1495a2`
- `codex-worker-platform` checkpoint `5521b3fc1fd273ffc71e47c344d6bb9083cfdb3f`
- `GitBoy` main `191f21a30ddf94d6181cbfbee1206c3fc5029c66`

Before deleting either legacy repository, fetch them again and verify there are no later/unpreserved branches, tags, commits, reports, configuration, or coordination records.

Mission Control should receive any legacy material that represents private fleet/control-plane state rather than generic worker implementation, including:

- enrollment approval/authorization policy and durable approval state;
- fleet/worker inventory and role definitions;
- repository/project scopes;
- assignments, claims, dispatch state, and private coordination records;
- private reports and recovery state;
- private infrastructure metadata that is safe and useful to keep in Git.

Do not migrate raw secrets into Git. Passwords, access tokens, private keys, authentication caches, reusable enrollment credentials, and production data must remain outside repository history.

Before legacy deletion, record:

- complete source ref inventory;
- exact destination preservation evidence;
- public/private boundary review;
- secret scan results;
- active legacy-reference scan results;
- a clean recovery test using only Vincent and Mission Control;
- exact final consolidation commits in both repositories.

The owner's 2026-08-25 directive is to delete both legacy repositories after that proof is complete. This supersedes the earlier planning rule that linked deletion to later ISO acceptance. The preservation proof remains mandatory.

## ISO handoff relevant to Mission Control

Vincent accepted Workstream 1 source:

`fc032f8df1c0abde295122a8a515e9cdcf7c7b70`

Acceptance record:

`d6fb92a6a07905dc29a1431b17d2a953abd5fbc8`

The first ISO built from that source was rejected by the obsolete-name scan; rejected image SHA-256:

`bcebd5fed3c82f86c7259b8dd71297e99057f630698c1742e4461265b78842a2`

It must not be flashed.

Correction state in Vincent:

- branch `workstream/ws2-iso-corrections`
- correction code `3a6abb330fb11faffbd638b101ed11dca47f4216`
- report branch tip `4edd5e95a403d605664402a7b1dc2d5c4f53b71b`
- report `docs/reports/VINCENT_WS2_ISO_VALIDATION.md`

Mission Control must not weaken the ISO trust model. A new worker must:

- generate its identity locally;
- start with no private/project authority;
- request enrollment;
- receive explicit scoped authorization;
- support revocation/recovery;
- never depend on a reusable fleet credential embedded in the public ISO.

No USB had been identified/flashed and no release or production/project authority had been granted at handoff time.

## Operating rules

- Git wins over chat summaries.
- Project DNA records why; roadmap records order; handoff records current state.
- Fetch before deciding what is current.
- Preserve conflicting/unexpected Git state until understood.
- Long-running commands should show output and save complete timestamped logs with `tee`; preserve pipeline status and report explicit exit status.
- Never infer success from truncated terminal output.
- Mission Control dispatches/records; workers implement/test/report; ChatGPT/owner provide direction and acceptance.

## Recovery success criterion

The old ChatGPT project is no longer needed once a fresh project connected to only the two new repositories can recover the system, current blockers, accepted/rejected artifacts, authority boundaries, and next work solely from Git.
