# Goal: Codex Wrapper Purity and Final Refactor Hardening

## Objective

Raise the completed Python boundary expansion branch from a strong merge
candidate into a near-ideal thin, product-only Termux Codex wrapper.

This goal intentionally lives outside `humtr/codex` as
`/data/data/com.termux/files/home/prj/goal-md/goals/codex-goal.md`. The codex product
repo must not carry long-running goal ledgers, generic automation plans,
handoff material, or operations framework documents.

Target score improvements now use a stricter rule: remove at least 90% of
each dimension's distance from 100. The previous draft used an 80% reduction
threshold; this goal deliberately raises the bar.

| Dimension | Current | Current Gap | 90% Gap Reduction Target | Reason |
| --- | ---: | ---: | ---: | --- |
| Goal record hygiene | 98 | 2 | 99.8+ | Externalize the goal ledger and keep codex product-only. |
| Thin wrapper philosophy | 89 | 11 | 98.9+ | Leave shell as Termux glue, not policy or parsing logic. |
| Refactor quality | 92 | 8 | 99.2+ | Prevent Python CLI monolith growth and tighten ownership. |
| Product validation confidence | 96 | 4 | 99.6+ | Add mismatch, tuple, network-disabled, and doctor-field proof. |
| Merge candidate maturity | 93 | 7 | 99.3+ | Remove non-product artifacts and leave a clean, reviewable stack. |

The final state should feel like a completed product wrapper, not an
automation experiment: small shell entrypoints, explicit contracts, Python
decision modules, strong product-local tests, and no generic orchestration.

The 90% target is intentionally hard. It means the branch should not merely be
mergeable; it should be difficult to improve without changing product scope.

## Current Evidence

Baseline branch:

- `refactor/python-boundary-expansion`
- Latest pushed commit at 90% goal lift: `80f7d8c Externalize codex goal ledger`
- Product code proof from the prior Python boundary goal:
  - installed wrapper: `260702-11 (dbbabbd86348)`
  - `tests/run-portable.sh`: pass
  - `tests/run-termux.sh`: pass
  - rebuild smoke: pass
  - `tests/run-all.sh`: pass
  - `canon-audit --strict`: pass, findings `[]`
- Externalization proof after that product proof:
  - `GOAL.md` removed from `humtr/codex`
  - external goal stored in `humtr/goal-md`
  - codex branch pushed through `80f7d8c`

The final product proof for this lifted goal must be rerun after the next
refactor commits, because `80f7d8c` intentionally changed repository hygiene
and wrapper version metadata after the previous installed-wrapper proof.

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

These are good enough to merge as a strong branch, but not yet good enough for
the stricter "thin, pure, finished wrapper" standard.

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
but evaluate progress against the 90% gap-reduction targets. Do not accept a
change merely because tests pass; accept it only if it makes the wrapper
thinner, clearer, more product-local, or better proven.

Recommended branch policy:

1. Continue from `refactor/python-boundary-expansion` only if the user wants to
   keep the existing branch stack.
2. Otherwise create a follow-up branch such as
   `refactor/wrapper-purity-hardening` from the current local state.
3. Do not merge to `main` until Phase 8 proves the stack is clean.
4. Do not push unless the user explicitly asks.

Scoring rule:

- A phase is not complete because files changed.
- A phase is complete when the acceptance checks prove the relevant score gap
  was reduced.
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
- Goal record hygiene score is at least 99.8.

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

Target budgets for the 90% goal:

- `lib_lines` <= 85 unless loader clarity would suffer.
- `install_runtime_lines` <= 450.
- `domain_shell_lines` <= 1800.
- `lib_shell_functions` <= 110.
- `runtime_shell_lines` <= 575.
- `state_shell_lines` <= 275.
- `notify_shell_lines` <= 260.
- `profile_shell_lines` <= 300.
- `notify_shell_functions` <= 12.
- `profile_shell_functions` <= 10.
- `cli_py_lines` <= 350 for `tools/codex_termux/cli.py` after command-group split.

These are aggressive targets. Do not hit them by making shell obscure. If a
shell area remains above target, the exception must identify exactly which
Termux glue operation justifies it and what Python-owned logic has already been
removed.

Acceptance:

- `canon-audit --strict` enforces the new budgets.
- Audit reports per-file shell line counts for runtime/state/profile/notify.
- Audit reports `cli.py` line count and fails if it regresses into a monolith.
- Any remaining over-budget shell area has an explicit short-term exception
  with a reason and a follow-up target.
- Shell remains execution glue; policy does not move back into shell.
- Thin wrapper philosophy score is at least 98.9.

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

- `tools/codex_termux/cli.py` <= 350 lines.
- command behavior remains unchanged.
- existing shell callers do not need broad rewrites.
- Python module ownership is clear enough to audit.
- Refactor quality score is at least 99.2.

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
- Product validation confidence score is at least 99.6.

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
- Merge candidate maturity score is at least 99.3.

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
```

The final `rg` command should return no product-repo contamination except
explicitly allowed product-local references, if any.

## Acceptance Ledger

- [x] Phase 0 external goal ledger complete.
- [ ] Phase 1 product purity cleanup complete.
- [ ] Phase 2 90%-target shell budgets implemented.
- [ ] Phase 3 runtime/state shell reduction complete.
- [ ] Phase 4 install runtime slimming complete.
- [ ] Phase 5 Python CLI de-monolith complete.
- [ ] Phase 6 manifest/audit upgrade complete.
- [ ] Phase 7 validation confidence upgrade complete.
- [ ] Phase 8 merge hygiene complete.
- [x] `humtr/codex` has no in-repo `GOAL.md`.
- [ ] `humtr/codex` remains product-only.
- [ ] public `codex` behavior preserved.
- [ ] `codex termux` compatibility preserved.
- [ ] installed wrapper matches final local commit.
- [ ] final validation passes.
- [ ] goal record hygiene score is at least 99.8.
- [ ] thin wrapper philosophy score is at least 98.9.
- [ ] refactor quality score is at least 99.2.
- [ ] product validation confidence score is at least 99.6.
- [ ] merge candidate maturity score is at least 99.3.
- [ ] no network-dependent command used unless explicitly authorized.
- [x] no branch pushed unless explicitly authorized.

## Not Proven Yet

- Whether the 90%-target shell budgets can all be reached without making the
  wrapper less clear.
- Whether `cli.py` can be reduced to <= 350 lines without excessive import
  complexity.
- Whether all tuple/mismatch tests can be made stable across local Termux
  environments.
- Whether a squash-ready final branch is preferable to preserving the local
  checkpoint history.

## Resume Notes

Start from `humtr/codex` branch `refactor/python-boundary-expansion` unless the
user chooses a new branch. Treat this external file as the canonical goal.

First action inside the product repo should be deleting `GOAL.md` and proving
that no generic automation material remains.
