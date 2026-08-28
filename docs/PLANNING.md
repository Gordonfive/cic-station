# Planning and Work Tracking

GitHub issues are the active planning system for the Vincent + CIC Station product family.

## Authority

- GitHub issues: active work, defects, verification work, blockers, follow-ups, and unscheduled ideas.
- Pull requests: implementation/review state and change-specific evidence.
- Repository milestones: target product releases.
- Repository labels: lightweight priority, workstream, and cross-product classification where useful.
- `docs/PROGRAM_ROADMAP.md`: cross-product milestone outcomes.
- Each repository's `docs/ROADMAP.md`: product/release outcomes.
- `docs/REQUIREMENTS.md`: stable requirements.
- ADRs: consequential accepted decisions.
- `docs/STATUS.md`: concise current implementation/test state.

A separate GitHub Projects v2 board is intentionally not part of the authoritative workflow. The connected GitHub automation used for routine project management can directly maintain repository issues, PRs, branches, and issue metadata but cannot reliably maintain Projects v2 fields/views/statuses. Requiring a manually synchronized project board would create a second source of truth and unnecessary maintenance burden.

## Cross-repository planning

Use organization-scoped GitHub issue search across `logrusbox/vincent` and `logrusbox/cic-station` rather than duplicating issues across repositories.

Cross-product work should have one primary issue in the repository that owns the implementation or decision. Link the counterpart repository issue only when there is genuinely distinct work that must be tracked independently. Do not create duplicate mirror issues for visibility.

## Lightweight metadata

Prefer native GitHub metadata over custom documents:

- issue state for open/completed work;
- milestone for target release;
- labels for priority/workstream/cross-product classification;
- assignee only when ownership needs to be explicit;
- linked PRs and issue dependencies for implementation/blocking relationships.

Avoid story points, sprint fields, estimates, duplicated release fields, permanent handoff documents, and other metadata that requires continual manual synchronization without demonstrated value.
