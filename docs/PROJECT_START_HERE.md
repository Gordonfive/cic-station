# Project Start Here

Use this file to recover Mission Control and Vincent in a completely new ChatGPT/Codex project. Prior ChatGPT history and legacy repositories are not required for normal recovery.

## First actions

1. Connect to and fetch both authoritative repositories:
   - `Gordonfive/mission-control`
   - `Gordonfive/vincent`
2. Read `AGENTS.md`, this file, `docs/ROADMAP.md`, and `docs/CONTINUATION_HANDOFF.md` in both repositories.
3. Treat Git state and explicit owner decisions as authoritative.
4. Inspect current reports before beginning a new workstream.

## Repository roles

- Mission Control is PRIVATE. It owns fleet enrollment approval, authorization, inventory, roles, repository scopes, assignments, private coordination, private reports, and safe private infrastructure metadata.
- Vincent is PUBLIC. It owns the generic worker platform, Debian ISO/install/bootstrap, enrollment client, runtime, tests, public-safe documentation, and releases.
- Historical worker-platform and bootstrap repositories were migration sources only. Their known Git histories are preserved by Vincent `legacy/*` refs and are not required for project recovery.

## Current shared state

Vincent durable history records:

- accepted Workstream 1 source for ISO testing: `fc032f8df1c0abde295122a8a515e9cdcf7c7b70`;
- owner acceptance record: `d6fb92a6a07905dc29a1431b17d2a953abd5fbc8`;
- Workstream 2 correction code: `3a6abb330fb11faffbd638b101ed11dca47f4216`;
- correction/report tip: `4edd5e95a403d605664402a7b1dc2d5c4f53b71b`.

The first ISO built from the accepted source was rejected by validation. Rejected SHA-256:

`bcebd5fed3c82f86c7259b8dd71297e99057f630698c1742e4461265b78842a2`

It must never be flashed. Migration consolidation does not itself authorize a replacement ISO source.

## Mission Control security boundary

- Never place raw secrets, passwords, private keys, tokens, authentication caches, reusable enrollment credentials, or production data in Git.
- Public Vincent must never contain private fleet authorization, inventory, repository scopes, assignments, or private reports.
- A new Vincent worker begins untrusted and gains only explicit scoped authority after enrollment approval.

## Recovery goal

A fresh project connected only to Vincent and Mission Control must be able to determine product intent, architecture, authority boundaries, important accepted/rejected states, current work, and next actions. Migration validation reports in `docs/reports/` record the preservation proof.
