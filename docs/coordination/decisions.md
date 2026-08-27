# Decisions

**Register updated:** 2026-08-27T11:49:00-08:00

## 2026-08-25 — Separate public workers from private fleet control

Accepted structure:

- `Gordonfive/vincent` is the public Vincent worker platform.
- `Gordonfive/mission-control` is the private fleet control plane.
- Individual project repositories retain project-specific authority and Product DNA.
- GitBoy is a retired prototype name.
- VS Code is optional and is not a control-plane dependency.
- The universal ISO contains no permanent identity or reusable credential.
- Enrollment is explicit, scoped, unique per worker, and revocable.

## 2026-08-26T09:49:00-08:00 — Repository hygiene and timestamp authority

Accepted policy:

- Mission Control and Vincent are operational sources of truth, not archives of abandoned implementation.
- Before obsolete Git state is deleted, inspect it once and distill any still-useful facts, rationale, lessons, or requirements into current timestamped documentation.
- After useful information is documented, obsolete branches, migration histories, abandoned code, superseded experiments, and archive-only tags may be deleted.
- Keep only the minimum temporary workstream branches needed for active work; delete them after integration or supersession.
- The stable target branch topology is `main` only. VINCENT 1.0 specifically targets `main` as the sole Vincent branch.
- For conflicting project direction, the newest applicable explicitly timestamped authoritative decision controls unless a later decision explicitly provides different precedence.
- Untimestamped material cannot override conflicting timestamped material. Git commit timestamps are provenance only and do not replace an authoritative decision or document timestamp.

## 2026-08-27T11:49:00-08:00 — Mission Control assigns AI identity profiles; Vincent performs enrollment

Accepted architecture:

- Mission Control may assign each enrolled Vincent worker an AI provider identity profile defining the desired provider plus account, organization, tenant, project, or equivalent provider context and authentication policy.
- Vincent executes the provider-specific enrollment flow locally through an agent/provider adapter, verifies the effective non-secret identity/scope where the provider permits it, and reports enrollment/health state back to Mission Control.
- Codex should initially prefer supported ChatGPT/device authorization where available so a human can authorize the worker from another browser/device without embedding permanent credentials in Vincent.
- If a provider cannot enforce the assigned account/project automatically, Vincent must surface a mismatch or blocked state rather than silently operate under an unintended identity.
- Future provider adapters may use OAuth/device authorization, browser/SSO authorization, scoped API or service-account credentials, or no remote account for local-model agents.
- Raw tokens, cookies, API keys, passwords, private keys, authentication caches, and reusable credentials never belong in Git. Mission Control may store only non-secret identity/profile metadata, credential identifiers, and references to protected secret material.
- Future unattended enrollment must use a protected secret broker/backend or one-time delivery mechanism with authenticated transport, unique least-privileged worker/provider credentials, and revocation. Shared fleet-wide AI credentials are prohibited.
- The architecture is provider-neutral and must support future Codex, Gemini, Copilot, Ollama/local-model, and custom-agent integrations without redesigning worker enrollment.
