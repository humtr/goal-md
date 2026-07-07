# Goal: Codex Wrapper Purity and Final Refactor Hardening

## Objective

Raise the current `main` branch into a near-ideal thin, product-only Termux
Codex wrapper.

This goal intentionally lives outside `humtr/codex` as
`/data/data/com.termux/files/home/prj/goal-md/goals/codex-goal.md`. The codex product
repo must not carry long-running goal ledgers, generic automation plans,
handoff material, or operations framework documents.

Target score improvements now use the strictest rule so far: remove at least
95% of each dimension's distance from 100. The previous draft used a 90%
reduction threshold; this goal deliberately raises the bar again.

| Dimension | Current | Current Gap | 95% Gap Reduction Target | Reason |
| --- | ---: | ---: | ---: | --- |
| Goal record hygiene | 98 | 2 | 99.9+ | Externalize the goal ledger and keep codex product-only. |
| Thin wrapper philosophy | 89 | 11 | 99.45+ | Leave shell as Termux glue, not policy or parsing logic. |
| Refactor quality | 92 | 8 | 99.6+ | Prevent Python CLI monolith growth and tighten ownership. |
| Product validation confidence | 96 | 4 | 99.8+ | Add mismatch, tuple, network-disabled, and doctor-field proof. |
| Merge candidate maturity | 93 | 7 | 99.65+ | Remove non-product artifacts and leave a clean, reviewable stack. |

The final state should feel like a completed product wrapper, not an
automation experiment: small shell entrypoints, explicit contracts, Python
decision modules, strong product-local tests, and no generic orchestration.

The 95% target is intentionally hard. It means the branch should not merely be
mergeable; it should be difficult to improve without changing product scope,
and any remaining imperfection must be explicitly justified by Termux runtime
constraints or reviewability.

## Current Evidence

Baseline branch:

- `main`
- Latest pushed main commit at this goal lift: `56d6704 Read auto-update state through Python plans`
- Main merge proof:
  - `refactor/wrapper-purity-hardening` fast-forwarded into `main`
  - `main` pushed to `origin/main` through `56d6704`
  - product goal ledger kept outside `humtr/codex`
  - external goal stored in `humtr/goal-md`
- Post-merge product proof on `main`:
  - installed wrapper: `260702-72 (56d6704fd99d)`
  - `bash -n` protected shell/scripts: pass
  - `validate --root .`: pass
  - `canon-audit --strict`: pass, findings `[]`
  - `tests/run-portable.sh`: pass
  - `tests/run-termux.sh`: pass
  - cached rebuild smoke: pass
  - `tests/run-all.sh`: pass

The final product proof for this lifted goal should be rerun after the next
hardening commits.

Current measured structure:

- `lib/codex-termux.sh`: 87 lines
- `bin/install-runtime.sh`: 626 lines
- domain shell total: 2621 lines
- shell functions in protected wrapper shell: 175
- `lib/codex-termux/runtime.sh`: 960 lines
- `lib/codex-termux/state.sh`: 493 lines
- `lib/codex-termux/profile.sh`: 434 lines
- `lib/codex-termux/notify.sh`: 405 lines
- `tools/codex_termux/cli.py`: 927 lines

These are strong enough to merge, but still not fully at the strict thin-wrapper standard.

## Hard Boundaries

### Product Repo Boundary

`humtr/codex` is the Termux Codex wrapper product repo.

Allowed in `humtr/codex`:

- wrapper source
- installer/runtime scripts
- product-local Python helpers
- product-local tests
- product manifest/audit rules
- concise product docs if directly needed

Forbidden in `humtr/codex`:

- `GOAL.md` or other long-running goal ledgers
- generic PR loop material
- handoff prompts or `NEXT_AGENT_PROMPT`
- merge-readiness workflows
- GitHub/OpenAI API orchestration
- local-server automation framework material
- branch archive mining docs
- reusable agent ops playbooks, schemas, or templates

### Behavior Boundary

Preserve:

- public `codex` launcher behavior
- `codex termux` compatibility
- Termux install, support, rebuild, repair, rollback, registry, profile, and
  runtime contracts
- default profile behavior: do not force `CODEX_HOME`
- custom profile isolation
- managed launcher and runtime artifact paths

### Shell/Python Boundary

Shell owns:

- `exec`
- file mutation with `cp`, `mv`, `chmod`, `ln`
- locks, traps, temp files, fd wiring
- public shell dispatch
- Termux process environment setup

Python owns:

- diagnosis
- planning
- validation
- policy decisions
- structured state interpretation
- source resolution
- JSON/TOML-like rendering or parsing
- reusable action vocabulary


### Shell Domain Purification Completion Boundary

Shell-domain purification is a completion requirement, not an optional cleanup.
The goal is not aggressive line-count compression. The goal is a thin,
structured, maintainable wrapper where shell remains the Termux execution
substrate and Python owns reusable decisions.

A shell domain is complete only when all of the following are true:

- every public shell path still preserves existing `codex` and `codex termux`
  behavior.
- every shell function in `lib/codex-termux/*.sh` and `bin/install-runtime.sh`
  is classified as one of: dispatch, prompt/input collection, exec/fd wiring,
  file mutation, lock/trap/temp management, environment setup, or justified
  Termux glue.
- option parsing, profile/session/runtime/source selection, hook selection,
  doctor field derivation, install/rebuild planning, status rendering, JSON/TOML
  rendering, and reusable validation live in Python wherever practical.
- interactive shell may collect raw input and print menus, but Python must own
  interpreting selections whenever the interpretation is reusable policy rather
  than terminal I/O.
- non-interactive wrapper commands delegate command parsing and validation to
  Python command modules unless doing so would make shell execution less clear
  or less reliable.
- shell does not duplicate Python-owned vocabularies such as notify hooks,
  profile identifiers, runtime selection fields, install-plan actions, repair
  actions, or doctor critical fields.
- every remaining shell-side `case`, numeric selection, field extraction, or
  derived decision has a named exception explaining why it is irreducible
  shell glue.
- every exception has focused test coverage or is covered by a final Termux
  smoke gate.
- line-count budgets are treated as pressure metrics and regression guards, not
  a license to make shell terse, cryptic, or harder to maintain.

Domain-specific completion requirements:

- `notify.sh`: hook vocabulary, hook selection parsing, non-interactive option
  parsing, config-env rendering, and system-config rendering are Python-owned;
  shell keeps only prompt display, file writes, and provider/script invocation.
- `profile.sh`: profile validation, display names, default/custom semantics,
  recent profile state, menu-choice interpretation, and runtime selection
  interpretation are Python-owned; shell keeps terminal prompting, `CODEX_HOME`
  export/unset boundaries, and final runtime exec.
- `session.sh`: session selection result parsing, profile-aware resume plan
  interpretation, and recent-session policy are Python-owned; shell keeps temp
  file lifecycle and final `exec`/`cd` behavior.
- `state.sh`: structured path validation, product status fields, UI text,
  derived status values, and reusable safety decisions are Python-owned; shell
  keeps safe file mutation wrappers, locks, temp paths, and subprocess bridge.
- `runtime.sh`: repair/readiness/rebuild action selection, runtime metadata
  interpretation, tuple/status derivation, and display summaries are
  Python-owned; shell keeps fd remap, activation probes, binary execution,
  symlink/copy/chmod mutation, and rollback file operations.
- `bin/install-runtime.sh`: source resolution, install-plan decisions, option
  validation, package metadata interpretation, and reusable error/success
  messages are Python-owned; shell keeps local file operations, builder
  invocation, launcher install, chmod, symlink, and activation calls.

This gate is not complete if a shell domain is merely smaller. It is complete
only when the remaining shell is plainly execution glue, with any residual
policy documented as a deliberate exception.

### Network Boundary

Do not use network-dependent commands while implementing unless the user
explicitly authorizes a final push or remote check.

Do not run by default:

- `git fetch`
- `git pull`
- `git push`
- `gh`
- `curl`
- `wget`
- OpenAI API
- GitHub API
- npm registry queries

Allowed by default:

- local git status/diff/log/add/commit
- local tests
- local support install
- cached raw rebuild smoke

## Execution Strategy

This is a hardening goal, not a feature goal. Work in small local checkpoints,
but evaluate progress against the 95% gap-reduction targets. Do not accept a
change merely because tests pass; accept it only if it materially makes the wrapper
thinner, clearer, more product-local, or better proven.

Recommended branch policy:

1. Work on a fresh branch created from `main`.
2. Keep `main` stable while hardening proceeds on the branch.
3. Do not merge to `main` until the remaining hardening phases are complete and verified.
4. Do not push unless the user explicitly asks.

Recommended model operating structure:

Use exactly one primary frontier model and, when delegation is useful, exactly
one low-cost implementation subagent.

- Primary frontier model owns orchestration, goal interpretation, branch/commit
  policy, product-boundary enforcement, hard architectural judgment, acceptance
  gates, final smoke/merge/push decisions, and any work estimated above 7.5/10
  difficulty.
- The 5.4 mini high subagent may be used for bounded implementation work at or
  below 7.5/10 difficulty, such as focused test fixes, narrow shell-to-Python
  plan moves, small module extraction, invariant updates, and local checkpoint
  preparation.
- Do not run multiple implementation subagents in parallel for this repo.
- Do not invoke a separate frontier review subagent by default. The primary
  frontier model performs the acceptance gate instead.
- The mini subagent must receive a narrow task, explicit forbidden actions,
  required focused tests, and a "no push" constraint.
- Any mini-produced patch must be accepted only after the primary model checks
  `git diff --check`, focused tests, `canon-audit --strict`, product-boundary
  constraints, and the relevant portable/Termux gate for the risk level.
- If a task is above 7.5/10 difficulty, the primary frontier model should do it
  directly instead of paying delegation, re-explanation, and re-review overhead.

Scoring rule:

- A phase is not complete because files changed.
- A phase is complete when the acceptance checks prove the relevant score gap
  was reduced to the 95% target or an explicit exception is justified.
- If a metric target is unreachable without harming clarity, document the
  exception and compensate with stronger tests or audit coverage.

## Execution Plan

### Phase 0: Externalize Goal Ledger

Remove goal-ledger material from the codex product repo and keep this file as
the canonical goal outside the repo.

Acceptance:

- `humtr/codex/GOAL.md` is deleted.
- `/data/data/com.termux/files/home/prj/goal-md/goals/codex-goal.md` exists.
- `humtr/goal-md` records the external-goal convention.
- The codex repo has no goal ledger or generic operations material.
- Goal record hygiene score is at least 99.9.

### Phase 1: Product Purity Cleanup

Remove or tighten any non-product residue introduced during the iterative
automation and refactor process.

Acceptance:

- `.github/workflows` remains empty or absent.
- no handoff, merge-readiness, agent-loop, GitHub API, or OpenAI API material
  exists outside product tests/docs.
- release package checks prove goal/ops files are excluded.
- `AGENTS.md` remains concise and product-local.

### Phase 2: Shell Budget Tightening

Make the thin-wrapper philosophy measurable with stricter budgets.

Target budgets for the 95% goal:

- `lib_lines` <= 80 unless loader clarity would suffer.
- `install_runtime_lines` <= 375.
- `domain_shell_lines` <= 1450.
- `lib_shell_functions` <= 85.
- `runtime_shell_lines` <= 450.
- `state_shell_lines` <= 220.
- `notify_shell_lines` <= 180.
- `profile_shell_lines` <= 220.
- `notify_shell_functions` <= 8.
- `profile_shell_functions` <= 7.
- `cli_py_lines` <= 250 for `tools/codex_termux/cli.py` after command-group split.

These are aggressive targets. Do not hit them by making shell obscure. If a
shell area remains above target, the exception must identify exactly which
Termux glue operation justifies it and what Python-owned logic has already been
removed.

Acceptance:

- `canon-audit --strict` enforces the new budgets as regression guards.
- Audit reports per-file shell line counts for runtime/state/profile/notify.
- Audit reports `cli.py` line count and fails if it regresses into a monolith.
- Every shell domain has a completed classification ledger: dispatch, prompt,
  exec/fd, file mutation, lock/trap/temp, env setup, or justified Termux glue.
- Any remaining over-budget shell area has an explicit exception with function
  names, reason, test coverage, and a follow-up target if the exception is not
  permanent.
- No movable shell-side parsing, policy decision, structured rendering, or
  reusable vocabulary remains in shell.
- Shell remains execution glue; policy does not move back into shell.
- Thin wrapper philosophy score is at least 99.45.

### Phase 3: Runtime and State Shell Reduction

Reduce `runtime.sh` and `state.sh` without changing behavior.

Preferred moves:

- move runtime action selection, state interpretation, and display summaries
  into Python modules.
- move structured state formatting, field extraction, and derived status values
  into Python.
- convert repeated shell `case` blocks into Python-selected actions with small
  shell executors.
- keep fd wiring, process launch, activation shell calls, and managed file
  mutation in shell.

Detailed work items:

1. Inventory every function in `runtime.sh` and classify it as execute, mutate,
   parse, decide, render, or dispatch.
2. Move parse/decide/render functions first.
3. Collapse duplicated repair/readiness/rebuild action handling.
4. Inventory `state.sh` and move non-shell-safe path calculations, derived
   fields, and renderable output into Python.
5. Add tests before deleting shell branches whenever behavior is not already
   covered.

Acceptance:

- runtime install/rebuild/repair/rollback behavior remains unchanged.
- `tests/repair-diagnosis.sh`, `tests/store-rollback.sh`,
  `tests/runtime-build.sh`, and live rebuild smoke pass.
- `runtime.sh` and `state.sh` meet or have documented exceptions against Phase
  2 budgets.
- No shell-side JSON parsing or policy action selection remains.

### Phase 4: Install Runtime Slimming

Reduce `bin/install-runtime.sh` toward a pure installer/executor.

Preferred moves:

- move remaining source planning, validation, option parsing, and package
  metadata decisions into Python helpers.
- move install mode summaries and reusable error messages into Python where
  they encode policy.
- keep local copy, chmod, symlink, activation, and process calls in shell.

Detailed work items:

1. Map every branch in `bin/install-runtime.sh` to an install-plan field.
2. Add missing install-plan fields before shrinking shell.
3. Move release/local/git source validation messages into Python.
4. Preserve direct shell execution for builder invocation and support file copy.
5. Re-run branch smoke with explicit local source after every substantial
   deletion.

Acceptance:

- `bin/install-runtime.sh` <= 450 lines, or any remaining excess is justified
  by irreducible Termux file/process glue.
- install support and cached rebuild smoke pass from a local checkout.
- branch-local rebuild cannot silently resolve to `main`.

### Phase 5: Python CLI De-Monolith

Prevent the current Python CLI from becoming the new monolith.

Expected shape:

- keep `tools/codex_termux/cli.py` as a thin command dispatcher.
- move command group registration/handlers into focused modules, for example:
  - `cli_source.py`
  - `cli_install.py`
  - `cli_runtime.py`
  - `cli_notify.py`
  - `cli_profile.py`
  - `cli_session.py`
  - `cli_doctor.py`
  - `cli_audit.py`
- keep shared parser helpers small and local.

Detailed work items:

1. Freeze CLI behavior with focused tests around shell-called commands.
2. Extract one command group at a time, starting with notify/profile/source.
3. Keep each extracted module responsible for parser registration and handler
   implementation for its domain only.
4. Leave `cli.py` with parser construction, shared primitives, and group
   registration calls.
5. Add audit ownership for CLI modules so the monolith cannot grow back.

Acceptance:

- `tools/codex_termux/cli.py` <= 250 lines, or any remaining excess is
  explicitly justified as parser/dispatch glue after domain command extraction.
- command behavior remains unchanged.
- existing shell callers do not need broad rewrites.
- Python module ownership is clear enough to audit.
- Refactor quality score is at least 99.6.

### Phase 6: Manifest and Audit Upgrade

Extend the manifest/audit from shell ownership to full product ownership.

Expected additions:

- Python module ownership map.
- stricter shell budget checks.
- forbidden product-repo patterns for goal/handoff/automation material.
- release leak checks for external goal files.
- shell-to-Python command surface sanity checks.

Acceptance:

- `canon-audit --strict` fails on:
  - reintroduced `GOAL.md`
  - workflow files
  - handoff/merge-readiness markers
  - inline `python3 -c`
  - shell-side JSON parsing
  - over-budget shell files
  - over-budget `cli.py`
  - unknown Python CLI ownership
  - protected shell calling unregistered Python helper commands
- audit still allows legitimate product-local tests and docs.

### Phase 7: Validation Confidence Upgrade

Raise product proof from "works now" to "catches drift."

Add focused tests for:

- installed wrapper commit/version mismatch.
- rebuild smoke tuple updates to the final wrapper tuple.
- `doctor --json` critical fields:
  - `overallStatus`
  - `wrapper.version`
  - `wrapper.commit`
  - `verifiedTupleId`
  - `activeTupleId`
  - hash checks
- network-disabled smoke invariants.
- release package exclusion of goal/ops artifacts.

Acceptance:

- tests fail on old wrapper tuple mismatch.
- tests fail if support install does not update manager metadata.
- tests fail if rebuild resolves to non-local source during branch smoke.
- tests fail if `doctor --json` omits critical status/hash/wrapper fields.
- tests prove auto-update and network checks are disabled during final smoke.
- `tests/run-all.sh` remains the final local gate.
- Product validation confidence score is at least 99.8.

### Phase 8: Commit Stack and Merge Hygiene

Leave a branch that is easy to review and merge.

Acceptance:

- no in-repo goal ledger remains.
- product changes are grouped into coherent commits or a squash-ready stack.
- final diff is product-local and reviewable.
- final PR summary can be written from code/tests, not from long operational
  notes.
- final branch can be merged without carrying temporary proof-only commits if
  the user chooses squash.
- no direct push or PR action happens unless the user explicitly asks.
- Merge candidate maturity score is at least 99.65.

## Implementation Order

Use this order unless current code evidence contradicts it:

1. Phase 6 first, in a non-destructive way: extend audit metrics to report the
   new 95% targets before making large reductions. Initial failures are allowed
   only while local work is in progress.
2. Phase 5 second: split `cli.py` into command-group modules so Python does not
   become the new monolith.
3. Phase 7 early: add drift tests for installed wrapper metadata, tuple update,
   doctor fields, and network-disabled smoke invariants before aggressive
   deletion.
4. Phase 3 next: shrink `runtime.sh` and `state.sh` by moving parse/decide/render
   logic to Python.
5. Phase 4 next: slim `bin/install-runtime.sh` after install-plan coverage is
   strong enough.
6. Phase 2 becomes final enforcement: tighten budgets only after the preceding
   work proves the targets or documented exceptions.
7. Phase 8 closes the branch with merge hygiene, final proof, and a concise
   PR-ready summary.

## Phase-by-Phase Checkpoints

Each phase should end with a local checkpoint summary containing:

- files changed
- shell/Python line-count deltas
- audit metric deltas
- focused tests run
- remaining score gap
- whether the next phase should continue, split, or stop for review

Do not rely on `tests/run-all.sh` alone as proof for score improvement. It is a
product gate, not a design-quality metric.

## Required Validation

Run after focused changes:

```bash
bash -n install.sh bin/install-local.sh bin/install-runtime.sh \
  lib/codex-termux.sh lib/codex-termux/*.sh \
  tools/smoke-termux-wrapper.sh tools/package-release.sh tests/*.sh

PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools \
  python3 -B -m codex_termux.cli validate --root .

PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools \
  python3 -B -m codex_termux.cli canon-audit --root . --strict

PYTHONDONTWRITEBYTECODE=1 bash tests/run-portable.sh
```

Final local product proof:

```bash
CODEX_TERMUX_AUTO_UPDATE=0 bash bin/install-local.sh support
CODEX_TERMUX_AUTO_UPDATE=0 PYTHONDONTWRITEBYTECODE=1 bash tests/run-termux.sh
CODEX_TERMUX_AUTO_UPDATE=0 CODEX_TERMUX_RUN_REBUILD_SMOKE=1 \
  PYTHONDONTWRITEBYTECODE=1 bash tests/run-termux.sh
CODEX_TERMUX_AUTO_UPDATE=0 PYTHONDONTWRITEBYTECODE=1 bash tests/run-all.sh
```

Completion audit:

```bash
git status --short --branch
find .github -maxdepth 3 -type f 2>/dev/null | sort
rg -n "GOAL.md|merge-readiness|handoff|NEXT_AGENT_PROMPT|OpenAI API|GitHub API|workflow_dispatch|agent loop" \
  . --glob '!.git/**'
wc -l lib/codex-termux.sh bin/install-runtime.sh lib/codex-termux/*.sh tools/codex_termux/cli.py
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools \
  python3 -B -m codex_termux.cli canon-audit --root . --strict
```

The final `rg` command should return no product-repo contamination except
explicitly allowed product-local references, if any. The final audit output
should prove the 95% metrics or list explicit, narrow Termux-glue exceptions.

## Acceptance Ledger

- [x] Phase 0 external goal ledger complete.
- [x] Phase 1 product purity cleanup complete.
- [ ] Phase 2 95%-target shell budgets and shell-domain classification gate implemented.
- [ ] Phase 3 runtime/state shell reduction complete.
- [ ] Phase 4 install runtime slimming complete.
- [ ] notify shell domain purified: Python owns hook/option/config decisions.
- [ ] profile shell domain purified: Python owns validation/menu/runtime-selection decisions.
- [ ] session shell domain purified: Python owns resume-plan/session-state decisions.
- [ ] state shell domain purified: Python owns derived status/safety/render decisions.
- [ ] runtime shell domain purified: Python owns readiness/repair/rebuild metadata decisions.
- [ ] install-runtime shell domain purified: Python owns source/install-plan decisions.
- [ ] every remaining shell policy exception is named, justified, and test-covered.
- [ ] Phase 5 Python CLI de-monolith complete.
- [ ] Phase 6 manifest/audit upgrade complete.
- [ ] Phase 7 validation confidence upgrade complete.
- [ ] Phase 8 merge hygiene complete.
- [x] `humtr/codex` has no in-repo `GOAL.md`.
- [x] `humtr/codex` remains product-only.
- [x] public `codex` behavior preserved.
- [x] `codex termux` compatibility preserved.
- [x] installed wrapper matches final local commit.
- [x] final validation passes.
- [x] goal record hygiene score is at least 99.9.
- [ ] thin wrapper philosophy score is at least 99.45.
- [ ] refactor quality score is at least 99.6.
- [ ] product validation confidence score is at least 99.8.
- [ ] merge candidate maturity score is at least 99.65.
- [ ] no network-dependent command used unless explicitly authorized.
- [x] no branch pushed unless explicitly authorized.

## Not Proven Yet

- Whether the 95%-target shell budgets can all be reached without making the
  wrapper less clear; if not, the completion gate requires named shell-glue
  exceptions rather than obscure compression.
- Whether `cli.py` can be reduced to <= 250 lines without excessive import
  complexity.
- Whether all tuple/mismatch tests can be made stable across local Termux
  environments.
- Whether a squash-ready final branch is preferable to preserving the local
  checkpoint history.
- Whether the 95% line-count budgets should be treated as strict merge blockers
  or as hard targets with documented Termux-glue exceptions.

## Resume Notes

Start from the current `main` branch in `humtr/codex`. Treat this external
file as the canonical goal.

The current product branch is `refactor/wrapper-final-hardening`, cut from
`main` to finish the remaining hardening phases as product-only commits. Keep
`legacy/monolith-maintained` separate as a maintained side line, not the
primary target.

2026-07-03 current goal alignment:

- active product baseline is `main` at `56d6704 Read auto-update state through Python plans`.
- `legacy/monolith-maintained` remains a separate maintained line for backports
  that fit the monolith shape.
- the current working branch is `refactor/wrapper-final-hardening`, cut from
  `main` to finish the remaining hardening phases.
- external goal storage remains in `humtr/goal-md`.
- current product proof on `main` remains the latest validated proof set:
  - installed wrapper: `260702-72 (56d6704fd99d)`
  - `bash -n` protected shell/scripts: pass
  - `validate --root .`: pass
  - `canon-audit --strict`: pass, findings `[]`
  - `tests/run-portable.sh`: pass
  - `tests/run-termux.sh`: pass
  - cached rebuild smoke: pass
  - `tests/run-all.sh`: pass
- the remaining hardening phases still need to be rerun on the new branch
  after any fresh structural edits.

Current measured structure from the latest validated `main` state:

- `lib/codex-termux.sh`: 87 lines
- `bin/install-runtime.sh`: 626 lines
- domain shell total: 2621 lines
- shell functions in protected wrapper shell: 175
- `lib/codex-termux/runtime.sh`: 960 lines
- `lib/codex-termux/state.sh`: 493 lines
- `lib/codex-termux/profile.sh`: 434 lines
- `lib/codex-termux/notify.sh`: 405 lines
- `tools/codex_termux/cli.py`: 927 lines

These are strong enough to merge, but still not fully at the strict thin-wrapper standard.
  - `notify_shell_lines`: 142
  - `profile_shell_lines`: 341
  - `lib_shell_functions`: 135
  - `cli_registered_command_count`: 82
- goal remains incomplete:
  - `runtime.sh`, `state.sh`, `profile.sh`, and `bin/install-runtime.sh` remain
    above the aggressive 95% line budgets.
  - explicit shell-domain exception/classification proof is still required.
  - final live Termux proof has not been rerun after the latest commits.

## Historical Checkpoints

Recent hardening checkpoints on the branch that led to the current `main`
baseline were progressively folded into the validated product state:

- checkpoint 3: shell classification became a strict audit contract; 167 shell
  functions were classified and the portable gate passed.
- checkpoint 4: profile/use planning moved further into Python; `cli.py`
  shrank to 62 lines and the profile, session, and CLI surface tests passed.
- checkpoint 5: status/version text normalization moved to Python; portable
  validation and runtime-date checks passed while shell budget pressure stayed
  concentrated in runtime, install, profile, and state.
- checkpoint 6: auto-update state planning moved to Python; the latest portable
  gate passed, and the remaining large shell blocks were still in
  `runtime.sh` and `bin/install-runtime.sh`.

Current validated product evidence on `main` remains:

- installed wrapper: `260702-72 (56d6704fd99d)`
- `bash -n` protected shell/scripts: pass
- `validate --root .`: pass
- `canon-audit --strict`: pass, findings `[]`
- `tests/run-portable.sh`: pass
- `tests/run-termux.sh`: pass
- cached rebuild smoke: pass
- `tests/run-all.sh`: pass

The remaining hardening work is still expected to focus on the same areas
listed above: `runtime.sh`, `state.sh`, `profile.sh`, and
`bin/install-runtime.sh`.

