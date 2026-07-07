---
name: goal-md
description: "Use when a project needs a GOAL.md-centered workflow: analyze the project, shape user intent into a durable living objective, keep an acceptance ledger, raise the goal threshold from current evidence, and prepare a resumable /goal entrypoint without storing reusable /goal prompts in GOAL.md."
---

# Goal-md

Use this skill when a project needs a durable GOAL.md workflow that can be
started, revised, resumed, and handed off across sessions.

## Core Rule

`GOAL.md` is the canonical living objective and acceptance ledger for the
current project. Do not store a reusable `/goal` prompt inside `GOAL.md`.
Treat `/goal` as an entrypoint derived from the current `GOAL.md` at resume or
start time.

When a target repository must remain product-only or otherwise should not carry
a long-running goal ledger, keep the canonical goal outside that repository as
`goals/<repo>-goal.md` in this repo or another explicit goal store. In that
case, treat the external goal file as canonical and keep only product-local
material in the target repository.

Human-friendly goal references are file-based. If the user writes
`/goal codex-goal.md`, `/goal resume codex-goal.md`, `goal codex-goal.md`, or
otherwise provides a goal file name instead of a path, resolve it with
`scripts/resolve_goal.py codex-goal.md` and then read the returned goal file as
canonical. If the file is unknown, list the available goal files from the index
instead of asking the user to remember a path.

Keep user-facing goal commands file-based when a specific goal file is known. Use absolute goal paths only for
internal file reads or when the user explicitly asks for the path. When
offering a resume command, prefer `/goal resume codex-goal.md` over expanding the
command to an abstract alias.

## Workflow

1. Analyze the current project and identify the public surface, risks,
   existing strengths, and missing proof.
2. Report the current state and the most important development insights to the
   user.
3. Use short, focused questions to clarify the goal, safety boundaries,
   success criteria, and proof gaps.
4. Draft or repair `GOAL.md` as the project's living objective and acceptance
   ledger.
5. Review the draft with the user and either improve it or confirm it.
6. Prefer `/goal resume` when available. If resume is unavailable or
   insufficient, derive a fresh `/goal` entrypoint from the current `GOAL.md`,
   present it to the user for approval, and only then start.

## Goal Lift Rule

Do not only ask whether the current goal is satisfied. Also ask whether the
current evidence, implementation shape, user-facing behavior, or risk analysis
justifies raising the goal threshold. When it does, update `GOAL.md` first,
then plan and execute against the lifted goal.

## What To Keep In `GOAL.md`

- Public contract and protected surfaces
- Current success threshold
- Project analysis and user decisions
- Execution plan
- Acceptance ledger
- Goal lifts and lifted thresholds
- Not proven items
- Blocked or resume conditions
- Working notes and handoff

## What Not To Put In `GOAL.md`

- A reusable `/goal` prompt block
- A question bank that freezes the workflow
- Project-agnostic boilerplate that does not affect execution or handoff

## Questions

Ask only the smallest set of questions that materially affect the goal,
constraints, success criteria, or proof boundary. Use questions to narrow the
objective, not to lock the implementation path.
