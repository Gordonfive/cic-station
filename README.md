# CIC Station

CIC Station is the reusable fleet-control application for Vincent. The repository remains private during development and is intended to become public under AGPLv3 at an explicit release gate.

The long-term CIC Station product is a self-hostable server application with a responsive web UI and authenticated API for enrollment, authorization, worker inventory, assignments, leases, approvals, health, results, and audit history.

Vincent remains independently functional for installation, boot, diagnostics, maintenance, updates, and standalone work. CIC Station applies only after a worker is explicitly enrolled into a managed fleet.

## Repository boundary

This repository owns:

- the reusable CIC Station web application, API, database schema/migrations, tests, and packaging;
- the canonical Vincent + CIC Station program roadmap;
- CIC Station product planning, requirements, architecture, and ADRs;
- safe deployment templates and operational documentation.

Gordonfive-specific worker inventory, enrollment and authorization state, assignments, results, audit records, and other operational data belong in the deployed CIC Station database and protected backups. Production secrets and private deployment configuration remain outside Git. Before public release, the entire Git history and release contents must pass a privacy, secret, infrastructure, and configuration audit.

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
