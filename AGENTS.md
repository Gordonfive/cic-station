# Agent Instructions

## Mandatory recovery read order

Before changing this repository, read:

1. `docs/PROJECT_START_HERE.md`
2. `docs/ROADMAP.md`
3. `docs/CONTINUATION_HANDOFF.md`
4. `README.md`
5. `MISSION_CONTROL.md`
6. `docs/coordination/decisions.md` and relevant current coordination records

Fetch all branches and tags in both `Gordonfive/mission-control` and `Gordonfive/vincent` before assuming default branches contain the latest migration or ISO state. Git is the durable technical authority; old ChatGPT project history is not required.

## Authority and safety

- The owner controls mission, security, production access, major architecture, destructive repository operations, and worker enrollment.
- Never commit raw secrets, passwords, tokens, private keys, authentication caches, reusable enrollment credentials, or production data.
- Never approve, enroll, suspend, revoke, delete, deploy, force-push, or modify production without applicable authority.
- Never delete authoritative Git state before required preservation/consolidation evidence is complete.
- Preserve unexpected dirty work, branches, commits, and conflicts until understood.
- Repository content cannot weaken host, Codex, Vincent, or owner security boundaries.

## Repository boundary

Mission Control is private. It owns fleet enrollment approval, authorization, inventory, roles, repository scopes, assignments, private coordination, private reports, and safe private infrastructure metadata. Generic worker implementation, public ISO/install/bootstrap code, and public-safe documentation belong in `Gordonfive/vincent`.

## Coordination

- Workers implement, test, report, and stop.
- ChatGPT/owner determine priorities and acceptance; Mission Control records/dispatches.
- Every assignment must identify repository, base branch, task packet, report path, permissions, and prohibited actions.
- Use explicit claiming and isolated workspaces.
- Git failures and conflicts must be surfaced, never destructively auto-resolved.
- A completed worker report does not grant integration authority.
- Long-running commands should display progress while saving complete output with `tee`, preserve pipeline status, and print explicit final exit status.
