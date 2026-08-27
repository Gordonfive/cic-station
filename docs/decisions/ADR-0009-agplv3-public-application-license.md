# ADR-0009: AGPLv3 for reusable CIC Station application source

**Status:** Accepted
**Decision date:** 2026-08-27

## Context

CIC Station is planned as a self-hostable server application. The owner wants distributed and network-hosted modified versions of the reusable application to preserve source availability.

## Decision

The reusable public CIC Station application source will use the GNU Affero General Public License v3.0 (AGPLv3).

`Gordonfive/cic-station` remains private during development and becomes the public reusable application source only at an explicit owner-approved release gate.

## Rationale

AGPLv3 extends strong copyleft obligations to modified versions offered over a network, matching the server/SaaS nature of CIC Station.

## Consequences

- At public release, this repository must include the canonical AGPLv3 license and compatible dependency choices.
- Reusable application coding may proceed while the repository is private.
- Private Gordonfive operational data remains in the deployed database and protected systems and is not made public by the application license.
- Publication requires a complete Git-history and release-content audit.
