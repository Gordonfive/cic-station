# Project Start Here

Use this file to recover Mission Control and Vincent in a completely new ChatGPT/Codex project. The previous ChatGPT project is intentionally disposable.

## First actions

1. Connect to and fetch both:
   - `Gordonfive/mission-control`
   - `Gordonfive/vincent`
2. Read `AGENTS.md`, this file, `docs/ROADMAP.md`, and `docs/CONTINUATION_HANDOFF.md` in both repositories.
3. Fetch all branches and tags before making assumptions about current migration or ISO state.
4. Treat Git state and explicit owner decisions as authoritative.

## Repository roles

- Mission Control is PRIVATE. It owns fleet enrollment approval, authorization, inventory, roles, repository scopes, assignments, private coordination, private reports, and safe private infrastructure metadata.
- Vincent is PUBLIC. It owns the generic worker platform, Debian ISO/install/bootstrap, enrollment client, runtime, tests, public-safe documentation, and releases.
- `Gordonfive/codex-worker-platform` and `Gordonfive/GitBoy` are legacy migration sources. The owner has directed their deletion after verified consolidation into the new repositories.

## Current shared state

Vincent refs that matter at this handoff:

- accepted migration source for ISO testing: `fc032f8df1c0abde295122a8a515e9cdcf7c7b70`
- acceptance record: `d6fb92a6a07905dc29a1431b17d2a953abd5fbc8`
- ISO correction code: `3a6abb330fb11faffbd638b101ed11dca47f4216`
- ISO correction/report branch tip: `4edd5e95a403d605664402a7b1dc2d5c4f53b71b`
- branch: `workstream/ws2-iso-corrections`

The first Vincent ISO from the accepted source was rejected by the obsolete-name scan and must not be flashed.

## Two active workstreams

### A. Consolidation and retirement

Make Vincent and Mission Control fully authoritative and self-sufficient. Verify all useful legacy code/history/docs/control-plane state has been preserved in the correct public/private repository. Then delete the two legacy repositories only after that preservation proof.

### B. ISO creation and physical testing

Resume from the Vincent Workstream 2 correction, establish one exact reviewed/authorized source commit, rebuild and fully inspect the image, then proceed through the separately gated physical test.

These workstreams may run in separate ChatGPT threads. Git is their coordination mechanism.

## Mission Control security boundary

- Never place raw secrets, passwords, private keys, tokens, authentication caches, reusable enrollment credentials, or production data in Git.
- Public Vincent must never contain private fleet authorization, inventory, repository scopes, assignments, or private reports.
- A new Vincent worker begins untrusted and gains only explicit scoped authority after enrollment approval.
- Preserve unexpected state until understood; do not erase conflicting Git evidence to make the project appear clean.

## Recovery goal

A fresh ChatGPT project connected only to `Gordonfive/vincent` and `Gordonfive/mission-control` must be able to determine the product intent, architecture, authority boundaries, current work, failures, exact important refs, and next actions without the old ChatGPT project.
