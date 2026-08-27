# Mission Control

Mission Control is the private program and fleet-control repository for Vincent.

The long-term Mission Control product is a self-hostable server application with a responsive web UI and authenticated API for enrollment, authorization, worker inventory, assignments, leases, approvals, health, results, and audit history.

Vincent remains independently functional for installation, boot, diagnostics, maintenance, updates, and standalone work. Mission Control applies only after a worker is explicitly enrolled into a managed fleet.

## Repository boundary

This private repository currently owns:

- the canonical Vincent + Mission Control program roadmap;
- Mission Control product planning, requirements, architecture, and ADRs;
- Gordonfive-specific fleet/deployment planning and operational state;
- private enrollment, authorization, assignment, policy, inventory, and recovery design;
- private infrastructure references that do not belong in public Vincent.

When reusable Mission Control application coding begins, that reusable AGPLv3 application source will move into a separate public repository from the start. Gordonfive-specific fleet/deployment state will remain private here or in another private operational repository.

Raw secrets, private keys, passwords, tokens, authentication caches, reusable enrollment credentials, and production data must never be committed.

## Documentation

Start with:

1. `docs/README.md`
2. `docs/PRODUCT.md`
3. `docs/REQUIREMENTS.md`
4. `docs/ARCHITECTURE.md`
5. `docs/PROGRAM_ROADMAP.md`
6. `docs/ROADMAP.md`
7. `docs/STATUS.md`
8. `docs/decisions/README.md`

Active work and unscheduled feature ideas belong in GitHub issues; implementation/review state belongs in pull requests.
