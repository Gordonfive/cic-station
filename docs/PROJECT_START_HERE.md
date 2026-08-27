# Project Start Here

This file is retained as a compatibility entry point. New contributors and agents should use `docs/README.md` as the documentation index.

## Start sequence

1. Read `AGENTS.md`.
2. Read `docs/README.md` and `docs/STATUS.md`.
3. Read `docs/ROADMAP.md`, `MISSION_CONTROL.md`, and `docs/coordination/decisions.md` as needed for the task.
4. Inspect current branches, issues, and pull requests before acting.
5. Read the corresponding current documentation in `Gordonfive/vincent` when work crosses the public/private boundary.

## Repository roles

- Mission Control is PRIVATE and owns fleet enrollment approval, authorization, inventory, roles, repository scopes, assignments, private coordination, and fleet-level reporting.
- Vincent is PUBLIC and owns the generic worker platform, Debian installer/ISO tooling, first boot, runtime, public-safe documentation, tests, and releases.
- Individual project repositories own their source, requirements, tests, and project-specific work history.

## Security boundary

Never place raw secrets, passwords, private keys, access tokens, authentication caches, reusable enrollment credentials, or production data in Git. A new Vincent worker starts without private project authority and receives only explicitly approved scope.

## Recovery principle

Normal project recovery depends only on the current Vincent and Mission Control repositories plus their active issues, pull requests, branches, and release evidence. Historical migration repositories and chat history are not operational dependencies.
