# ADR-0012: Rename the control-plane product to CIC Station

- Status: Accepted
- Date: 2026-08-27

## Context

The control-plane application and repository were previously named Mission Control. The owner selected **CIC Station** as the product name and `cic-station` as the repository name.

## Decision

Rename the control-plane product to **CIC Station** and rename the GitHub repository from `Gordonfive/mission-control` to `Gordonfive/cic-station`.

Use **CIC Station** for the application, service, web UI, API, documentation, roadmap, architecture, and fleet-control references. Vincent remains the worker platform.

Existing `MC-REQ-####` requirement identifiers remain unchanged because they are permanent identifiers, not product branding. Renumbering them would break durable references and violate the requirement-ID stability rule.

Historical Git commit messages and immutable Git history are not rewritten. Current source and documentation should use CIC Station except where explicitly describing the former name for historical context.

## Consequences

- `Gordonfive/cic-station` becomes the canonical control-plane repository after the GitHub repository rename.
- New branches, issues, pull requests, documentation, package names, deployment identifiers, URLs, and configuration should use `cic-station` rather than `mission-control`.
- Vincent documentation and integration references must be updated to point to CIC Station.
- Existing clones should update their `origin` URL after the repository rename.
