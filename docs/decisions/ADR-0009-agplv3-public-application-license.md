# ADR-0009: AGPLv3 for reusable CIC Station application source

**Status:** Accepted — repository-visibility clause superseded by ADR-0020
**Decision date:** 2026-08-27

## Context

CIC Station is planned as a self-hostable server application. The owner wants distributed and network-hosted modified versions of the reusable application to preserve source availability.

## Decision

The reusable public CIC Station application source will use the GNU Affero General Public License v3.0 (AGPLv3).

The original decision also kept `Gordonfive/cic-station` private during development until an owner-approved release gate. ADR-0020 supersedes that visibility clause: the repository is public during pre-release development. This does not change the license decision recorded here.

## Rationale

AGPLv3 extends strong copyleft obligations to modified versions offered over a network, matching the server/SaaS nature of CIC Station.

## Consequences

- At formal release, this repository must include the canonical AGPLv3 license and compatible dependency choices.
- Reusable application coding proceeds in the public development repository before formal release readiness.
- Private Gordonfive operational data remains in the deployed database and protected systems and is not made public by repository visibility or the application license.
- Formal release requires a complete Git-history and release-content audit.
