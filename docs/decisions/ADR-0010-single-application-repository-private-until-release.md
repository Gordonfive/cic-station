# ADR-0010: Use one CIC Station application repository, private until release

**Status:** Accepted — visibility portion superseded by ADR-0020
**Decision date:** 2026-08-27

## Context

The earlier repository boundary assumed that the control-plane repository would store private operational state in Git and that reusable application code therefore required a third repository. Review found no current need for that split. CIC Station is itself a reusable web application, and its private fleet information is application data that belongs in the deployed database and protected operational systems.

## Decision

Use two product repositories:

- `logrusbox/vincent` for the worker installer, operating environment, runtime, diagnostics, updates, provider adapters, and CIC Station client.
- `logrusbox/cic-station` for the reusable CIC Station web application, API, database schema and migrations, tests, packaging, and product/program documentation.

The original decision kept the CIC Station repository private during development until an explicit release gate. ADR-0020 supersedes that visibility requirement: `logrusbox/cic-station` is public during pre-release development. The two-repository and source/operational-data separation decisions remain current.

Do not commit private operational data. Worker identities, inventory, enrollment and authorization state, assignments, leases, results, and audit history belong in the deployed CIC Station database and protected backups. Raw secrets and private production configuration belong in protected secret and deployment systems outside Git.

## Rationale

A third application repository would add coordination and documentation overhead without protecting data that should not be committed to source control in the first place. Keeping application source together also avoids a later code migration. Separating source from runtime data and secrets is the conventional application boundary.

## Consequences

- CIC Station implementation proceeds in the existing public application repository.
- No separate application repository is required.
- Public-safe practices apply continuously.
- Deleting files immediately before a formal release is insufficient because Git retains history.
- The formal-release gate must audit the complete Git history, dependencies, secrets, privacy-sensitive content, infrastructure references, production configuration, documentation, and release artifacts.
- Any credential ever committed must be removed from history where appropriate and rotated before release.

## Supersedes

- `ADR-0002-public-application-private-deployment-split.md`

## Superseded by

- `ADR-0020-public-development-visibility.md` supersedes only the private-until-release visibility requirement. The single-repository and source/operational-data separation decisions remain current.
