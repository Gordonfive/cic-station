# ADR-0020: Develop CIC Station in a public repository before release

**Status:** Accepted
**Decision date:** 2026-08-28

## Context

ADR-0010 selected one CIC Station application repository and required it to remain private until a later public-release gate. The owner subsequently decided that public development is preferable now. The repository is already public, while CIC Station remains pre-release software.

Repository visibility and product release readiness are separate concerns. Public source visibility does not make operational fleet data, credentials, private keys, authentication state, production configuration, or protected deployment information appropriate for Git.

## Decision

Develop `logrusbox/cic-station` publicly before the first stable release.

Public repository visibility does not constitute a stable product release, waive acceptance criteria, open external contribution policy, or remove security/release audit requirements. CIC Station operational data and secrets remain outside Git under the existing source/operational-data boundary.

The formal release gate still requires the applicable repository-history, secret, privacy, infrastructure, dependency, configuration, packaging, and release-content review.

This ADR changes repository visibility only. It does not modify the separately recorded CIC Station license decision.

## Rationale

Public development makes the evolving architecture and implementation inspectable, avoids an unnecessary later publication event, and aligns repository visibility with the intended reusable product while preserving the actual security boundary around operational data and secrets.

## Consequences

- `logrusbox/cic-station` is public during pre-1.0 development.
- Public visibility must not be described as equivalent to release readiness or support status.
- Public-safe source, documentation, examples, tests, and configuration practices apply continuously rather than only immediately before release.
- Operational fleet data, credentials, production configuration, and protected deployment state remain outside Git.
- The formal release audit remains required.
- External pull requests remain intentionally deferred unless a later owner decision changes contribution policy.

## Supersedes

- The **private-until-release visibility requirement only** in `ADR-0010-single-application-repository-private-until-release.md`.

ADR-0010 remains authoritative for the single-application-repository and source/operational-data separation decisions.
