# CIC Station

CIC Station is the reusable fleet-control application for Vincent. The repository is public during pre-release development; public visibility is not equivalent to stable release readiness or support status.

The long-term CIC Station product is a self-hostable server application with a responsive web UI and authenticated API for enrollment, authorization, worker inventory, assignments, leases, approvals, health, results, and audit history.

Vincent remains independently functional for installation, boot, diagnostics, maintenance, updates, and standalone work. CIC Station applies only after a worker is explicitly enrolled into a managed fleet.

## Repository boundary

This repository owns:

- the reusable CIC Station web application, API, database schema/migrations, tests, and packaging;
- CIC Station product planning, requirements, architecture, ADRs, issues, and releases;
- safe deployment templates and operational documentation.

The cross-product VINCENT program roadmap, integration issues, and program-level governance are owned by [`logrusbox/vincent-program`](https://github.com/logrusbox/vincent-program).

Logrus Box-specific worker inventory, enrollment and authorization state, assignments, results, audit records, and other operational data belong in the deployed CIC Station database and protected backups. Production secrets and private deployment configuration remain outside Git. Before a formal release, the complete Git history and release contents must pass the applicable privacy, secret, infrastructure, dependency, configuration, and release-content audit.

Raw secrets, private keys, passwords, tokens, authentication caches, reusable enrollment credentials, and production data must never be committed.

## Documentation

Start with:

1. `docs/README.md`
2. `docs/PRODUCT.md`
3. `docs/REQUIREMENTS.md`
4. `docs/ARCHITECTURE.md`
5. `docs/ROADMAP.md`
6. `docs/STATUS.md`
7. `docs/decisions/README.md`
8. `docs/PROGRAM_ROADMAP.md` — migration pointer to the program repository

Active CIC Station work and unscheduled feature ideas belong in this repository's GitHub issues; cross-product work belongs in `logrusbox/vincent-program`; implementation/review state belongs in pull requests.
