# goal-md

Goal Markdown experiments and notes.

## Status

Active seed repository. This repo is intentionally small and should stay focused until its scope is finalized.

## Purpose

`goal-md` is a lightweight place to collect and refine Markdown-based goal, planning, and progress-tracking formats.

## Current scope

- Draft simple goal documents in Markdown.
- Keep examples small and easy to review.
- Keep product repositories free of long-running goal ledgers when their scope
  needs to stay product-only.
- Store external project goals under `goals/<repo>-goal.md` when the goal is
  useful but should not live in the target repository.
- Avoid adding runtime dependencies until the repository has a concrete tool or workflow.

## Usage

There is no required build step yet. Add Markdown documents or examples directly to the repository.

For product repositories that should not contain goal ledgers, keep the goal in
this repository instead:

```text
goals/<repo>-goal.md
```

Register reusable goals in `goals/index.json` so agents can use short names
instead of full paths. The first registered alias is `codex`, which tracks
follow-up hardening for `humtr/codex` while keeping that repository product-only.

Human-friendly forms supported by the skill:

```text
/goal codex
/goal resume codex
goal codex
```

Resolver utility:

```bash
python3 scripts/resolve_goal.py codex
python3 scripts/resolve_goal.py codex --field resume-prompt
```

## Validation

There is no automated validation yet. For now, keep Markdown files simple, readable on GitHub, and free of private credentials or personal secrets.

## Next steps

1. Decide whether this repository is a document template library, a CLI/tooling project, or an archive candidate.
2. Add one canonical example document.
3. Add a minimal validation rule if the format becomes stable.
