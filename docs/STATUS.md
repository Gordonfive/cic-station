# Mission Control Status

**Updated:** 2026-08-27T08:17:00-08:00

## Current state

Mission Control is the private control-plane repository for Vincent deployments. Repository consolidation is complete; Vincent and Mission Control are the only repositories required for normal project recovery and ongoing development.

Vincent 1.0 installer and worker proof remains the current product priority. Mission Control development should stay minimal until Vincent can independently reach an unassigned READY state and complete a bounded Git-driven task.

## Current Mission Control priorities

1. Maintain the private/public boundary between Mission Control and Vincent.
2. Keep enrollment, authorization, inventory, repository scopes, and assignment concepts documented without embedding secrets.
3. Avoid building a dedicated service/backend before Vincent 1.0 proves the simpler operator-selected Git workflow.
4. Use issues and pull requests for active implementation work and `docs/ROADMAP.md` for milestone-level planning.

## Authority boundary

Mission Control may record and coordinate private fleet state, but a fresh Vincent installation does not require or automatically contact this repository. Vincent is generic by default and receives project/control configuration only after explicit operator action.

## Recovery

A new contributor or agent should read `AGENTS.md`, `docs/README.md`, this file, `docs/ROADMAP.md`, and `MISSION_CONTROL.md`, then inspect current issues, pull requests, and branches before acting.
