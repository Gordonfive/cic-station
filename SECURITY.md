# Security Policy

CIC Station is pre-release software and is not yet supported for production security-sensitive deployment.

## Reporting a vulnerability

Do not publish credentials, private keys, tokens, production data, exploit details that would create immediate risk, or other sensitive information in a public GitHub issue.

Report suspected security vulnerabilities privately to the repository owner through GitHub's private vulnerability reporting feature when available. If private vulnerability reporting is unavailable, contact the Logrus Box maintainers through a private channel rather than opening a public issue containing sensitive details.

For non-sensitive security hardening, design questions, or publicly safe defects, use a normal GitHub issue.

## Scope

Security boundaries and accepted decisions are defined by `docs/REQUIREMENTS.md`, `docs/ARCHITECTURE.md`, and `docs/decisions/`.

Raw secrets, production credentials/configuration, worker private credentials, authentication caches, reusable enrollment material, and operational fleet data must remain outside Git.

## Supported versions

No stable release is currently supported. Security support policy will be defined before the first formal release.
