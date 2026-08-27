# ADR-0009: AGPLv3 for reusable Mission Control application source

**Status:** Accepted
**Decision date:** 2026-08-27

## Context

Mission Control is planned as a self-hostable server application. The owner wants distributed and network-hosted modified versions of the reusable application to preserve source availability.

## Decision

The reusable public Mission Control application source will use the GNU Affero General Public License v3.0 (AGPLv3).

The current private program/deployment repository is not itself the public reusable application source and does not need to become public merely to carry planning/state.

## Rationale

AGPLv3 extends strong copyleft obligations to modified versions offered over a network, matching the server/SaaS nature of Mission Control.

## Consequences

- The future public application repository must include the canonical AGPLv3 license and compatible dependency choices.
- Reusable application coding begins only after that public repository boundary exists.
- Private Gordonfive fleet/deployment state remains separate and is not made public by the application license.
