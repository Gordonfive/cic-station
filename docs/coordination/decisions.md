# Decisions

## 2026-08-25 — Separate public workers from private fleet control

Accepted structure:

- `Gordonfive/vincent` is the public Vincent worker platform.
- `Gordonfive/mission-control` is the private fleet control plane.
- Individual project repositories retain project-specific authority and Product DNA.
- `Gordonfive/codex-worker-platform` and `Gordonfive/GitBoy` remain intact during verified migration.
- GitBoy is a retired prototype name.
- VS Code is optional and is not a control-plane dependency.
- The universal ISO contains no permanent identity or reusable credential.
- Enrollment is explicit, scoped, unique per worker, and revocable.
