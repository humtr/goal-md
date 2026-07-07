# Goal: Termux Codeplane Full Architecture

## Objective

Create `humtr/termux-codeplane` as the Termux-specific full-code cognition and execution plane for ChatGPT-led development, then integrate it with `humtr/termux-mcp` and the existing Worker/tunnel path until the full architecture is proven end to end.

`termux-codeplane` must become the local engine that owns:

- repository mirror and sync
- canonical repository registry
- full-code indexing
- context capsule generation
- change bundle application
- recipe execution for deterministic jobs
- git worktree sandboxing
- validation tiers
- commit
- push
- structured observation/result reporting
- job/session state
- audit and replay material
- integration contracts for MCP and Worker frontends

`humtr/loop` remains the generic PR-ops, handoff, readiness, schema, and workflow-pattern framework. `termux-codeplane` is a Termux-specific implementation derived from those concepts, not a replacement for `humtr/loop`.

`humtr/termux-mcp` remains the ChatGPT-facing MCP bridge. Its long-term role is to become a thin facade that delegates code cognition and execution work to `termux-codeplane`.

## Current Repositories

### Generic framework

```text
humtr/loop
```

### Goal registry

```text
humtr/goal-md
```

### Termux-specific execution engine

```text
humtr/termux-codeplane
```

Canonical local path:

```text
/data/data/com.termux/files/home/prj/termux-codeplane
```

Remote target:

```text
git@github.com:humtr/termux-codeplane.git
```

### MCP bridge

```text
humtr/termux-mcp
```

Canonical source checkout:

```text
/data/data/com.termux/files/home/prj/termux-mcp
```

Current live runtime checkout:

```text
/data/data/com.termux/files/home/work/termux-mcp
```

The live runtime must remain stable until explicit migration.

## Goal-Led Agent Loop

This goal is not a passive plan. It is the controlling objective ledger for Agent work.

For any Agent run that acts on this goal:

1. Resolve the goal by alias `termux-codeplane` or by this file path.
2. Read the goal before planning edits.
3. Create or update the target repository `GOAL.md` from this goal.
4. Treat the target repository `GOAL.md` as the live execution contract after the repository exists.
5. At the start of each phase, update `GOAL.md` with the current phase, intended checkpoint, and first incomplete acceptance item.
6. At the end of each phase, update `GOAL.md` with actual results, validation evidence, pushed commit, blockers, and the next phase.
7. If implementation evidence changes the plan, update `GOAL.md` first or in the same commit as the implementation that changes the plan.
8. Never replace the goal with hidden reasoning. Store only public, reviewable facts: decisions, evidence, blockers, result summaries, and next actions.
9. On resume, read `GOAL.md`, locate the first incomplete acceptance item, and continue from there.
10. Do not stop simply because a checkpoint was pushed. Stop only under the stop conditions below.
11. If an Agent invocation cannot finish all remaining phases, it must update `GOAL.md` with exact resume instructions before stopping.
12. If the user asks `/goal termux-codeplane`, the next agent must use this file as the single source of durable objective state.

The purpose of this protocol is to increase work persistence across Agent invocations. `GOAL.md` is the single durable objective state, not merely documentation.

## Operating Rule

This goal is not complete after the first successful bootstrap.

A successful Phase 1 push is a checkpoint, not a final answer.

A successful Phase 2 push is a checkpoint, not a final answer.

A successful Phase 3 push is a checkpoint, not a final answer.

The full architecture is not complete until Phase 12 is complete, unless the user explicitly narrows scope.

For the first Agent run, the minimum target is Phase 3 unless blocked. If Phase 3 completes and time/tooling remains available, continue to Phase 4 and beyond.

Only stop when one of these is true:

1. All phases through Phase 12 are completed, validated, committed, pushed, and final status is clean.
2. A platform, authentication, repository-creation, validation, push, or runtime blocker prevents further safe progress.
3. The user explicitly cancels or narrows the task.
4. Continuing would require a destructive operation forbidden by this goal.
5. Continuing would require live runtime migration without explicit approval.

## Hard Boundaries

### Preserve `humtr/loop`

Do not modify `humtr/loop`.

Allowed:

- read it as reference
- copy suitable seed concepts into `termux-codeplane`
- cite it in provenance docs

Forbidden:

- changing `humtr/loop`
- pushing to `humtr/loop`
- converting `humtr/loop` into Termux-specific code

### Preserve Existing MCP Runtime

Do not move, delete, or rewrite the live runtime checkout during bootstrap and codeplane development:

```text
/data/data/com.termux/files/home/work/termux-mcp
```

Do not change the current Cloudflare Worker, tunnel, or live MCP registration before the dedicated migration phase.

### Prepare Canonical MCP Checkout

A canonical source checkout is required:

```text
/data/data/com.termux/files/home/prj/termux-mcp
```

This checkout may be created, updated, validated, and pushed. It must not replace the live runtime until explicit migration.

### Push Policy

Push is included in this goal.

Allowed:

```text
git push origin main
git push -u origin main
gh repo create humtr/termux-codeplane --private --source . --remote origin --push
```

Forbidden unless explicitly authorized later:

```text
git push --force
git push --force-with-lease
git push --mirror
git push --tags
remote branch deletion
remote tag deletion
```

### Secrets

Do not print, store, or commit secrets.

Do not commit:

```text
.env
tokens
private keys
GitHub tokens
OpenAI keys
Cloudflare keys
SSH private keys
```

### Safety of Live Service

Any live service change must have a rollback path.

Before modifying live MCP or Worker routing, record:

- current running path
- current commit
- current process/session status
- current Worker backend target
- rollback command or manual rollback steps

## Execution Strategy

Work in phases, but do not treat phase boundaries as stopping points.

Each phase must end with:

- `GOAL.md` progress update
- local validation
- git status
- commit
- push
- remote verification where practical
- short checkpoint note

Then continue to the next phase immediately when safe.

If validation fails:

- diagnose the failure
- repair if the cause is clear
- update `GOAL.md` with the blocker and next action if repair is not immediately possible
- rerun validation
- do not commit or push broken code unless the phase explicitly records a non-executable design-only artifact and validation still passes for repository integrity

If push fails:

- keep the local commit
- update `GOAL.md` with the local commit and exact remote failure
- report the local commit hash
- report the exact push failure
- do not force push

## Phase 0: Preflight and Repository Placement

### Goal

Solidify repository placement and remote availability without disrupting the live MCP runtime.

### Required Work

- Verify `git`, `python3`, and `gh` are available.
- Verify GitHub CLI authentication.
- Verify `~/prj` exists.
- Verify `~/prj/goal-md` exists and can resolve alias `termux-codeplane`.
- Verify `humtr/termux-codeplane` exists remotely.
- Verify `humtr/termux-mcp` exists remotely.
- Verify `~/prj/termux-mcp` exists as a non-live source checkout.
- Verify `~/prj/termux-codeplane` exists as a local checkout or empty initialized repo.
- Verify `~/work/termux-mcp` remains unchanged and live.
- Record the preflight report path in `GOAL.md`.

### Current Evidence

- [x] `humtr/termux-codeplane` exists as a private repository.
- [x] `humtr/termux-mcp` exists as a private repository.
- [x] `humtr/goal-md` contains alias `termux-codeplane`.
- [x] User reported repository preflight was completed.
- [ ] Agent must still verify local paths and statuses at run start.

### Acceptance

- [ ] Tooling verified.
- [ ] `~/prj` exists.
- [ ] external goal is readable locally or from GitHub.
- [ ] `~/prj/termux-mcp` is present as a non-live checkout.
- [ ] `~/prj/termux-codeplane` is present.
- [ ] `~/work/termux-mcp` remains unchanged and live.
- [ ] Phase 0 result is recorded in target repo `GOAL.md`.

## Phase 1: Bootstrap `termux-codeplane` Repository Identity

### Goal

Create a pushed repository with clear project identity, architecture docs, schemas, examples, Python skeleton, and minimal validation tooling.

### Required Files

```text
README.md
GOAL.md
Makefile
codeplane/__init__.py
codeplane/cli.py
codeplane/config.py
codeplane/repo.py
codeplane/indexer.py
codeplane/context.py
codeplane/bundle.py
codeplane/worktree.py
codeplane/validation.py
codeplane/gitops.py
codeplane/result.py
tools/codeplane_validate.py
docs/architecture.md
docs/runtime-model.md
docs/push-policy.md
docs/derived-from-loop.md
docs/goal-loop.md
schemas/project-manifest.schema.json
schemas/repo-registry.schema.json
schemas/context-request.schema.json
schemas/context-capsule.schema.json
schemas/change-bundle.schema.json
schemas/execution-observation.schema.json
schemas/job-result.schema.json
schemas/codeplane-session.schema.json
examples/context-request.sample.json
examples/context-capsule.sample.json
examples/change-bundle.sample.json
examples/job-result.sample.json
```

### Required Validation

```text
python3 -m py_compile all Python files
python3 tools/codeplane_validate.py
git status --short --branch
```

### Commit

```text
Initialize termux-codeplane
```

### Acceptance

- [ ] Repository identity files exist.
- [ ] `GOAL.md` exists as live progress ledger.
- [ ] Architecture docs exist.
- [ ] All required schemas exist.
- [ ] All required examples exist.
- [ ] Python files compile.
- [ ] Validation tool passes.
- [ ] Commit is pushed.
- [ ] Local status is clean.

## Phase 2: Code Cognition MVP

### Goal

Implement the minimum useful local code cognition engine.

### Required Commands

```text
python3 -m codeplane.cli inspect-project --repo <path>
python3 -m codeplane.cli build-index --repo <path> --out <path>
python3 -m codeplane.cli prepare-context --request <json> --out <json>
python3 -m codeplane.cli validate-self
```

### MVP Capabilities

`inspect-project` reports:

- repo path
- git repo status
- current branch
- current HEAD
- clean/dirty status
- remote URL
- package manager hints
- known validation scripts

`build-index` generates:

- file manifest
- file sizes
- sha256 hashes
- basic language classification
- package scripts when `package.json` exists
- recent commit summary
- ignored file awareness

`prepare-context` generates:

- base HEAD
- repo cleanliness
- relevant file list
- relevant search matches
- selected slices or small full files
- sha guards
- context completeness status

### Commit

```text
Add code cognition MVP
```

### Acceptance

- [ ] `inspect-project` works on `termux-codeplane`.
- [ ] `build-index` works on `termux-codeplane`.
- [ ] `prepare-context` produces valid capsule.
- [ ] Context capsule has base/head/hash guards.
- [ ] `GOAL.md` records Phase 2 result.
- [ ] Commit is pushed.

## Phase 3: Change Bundle Execution MVP

### Goal

Implement deterministic execution of ChatGPT-generated change bundles.

### Required Commands

```text
python3 -m codeplane.cli execute-bundle --bundle <json>
python3 -m codeplane.cli read-result --result <json>
python3 -m codeplane.cli validate-self
```

### Required Capabilities

- edit operations: create, append, replace
- base HEAD guard
- file hash guard
- optional dry-run mode
- validation tiers: none, self, standard
- result JSON
- commit policy
- push policy
- refusal on force push/tag push/remote deletion

### Commit

```text
Add change bundle execution MVP
```

### Acceptance

- [ ] `execute-bundle` exists.
- [ ] create/append/replace operations work or are clearly guarded.
- [ ] base HEAD guard exists.
- [ ] file hash guard exists or has explicit TODO and refusal semantics.
- [ ] validation tiers exist.
- [ ] result JSON is emitted.
- [ ] commit/push policy is implemented or explicitly gated.
- [ ] safe self-proof is performed.
- [ ] Commit is pushed.

## Phase 4: Repository Registry, Mirror, and Sync

### Goal

Move from ad hoc repo paths to a durable registry and mirror/sync model.

### Required Work

- Add repo registry schema and storage.
- Support registering repos under `~/prj`.
- Track repo name, full_name, local_path, default_branch, remote URL, safe execution policy, validation profile.
- Implement sync command.
- Implement clean/dirty/ref mismatch checks.
- Implement base ref drift detection.
- Support `termux-codeplane` and `termux-mcp` as first-class registered projects.

### Required Commands

```text
python3 -m codeplane.cli register-repo --name <name> --path <path>
python3 -m codeplane.cli list-repos
python3 -m codeplane.cli sync-repo --name <name>
python3 -m codeplane.cli inspect-project --name <name>
```

### Acceptance

- [ ] Registry exists.
- [ ] `termux-codeplane` registered.
- [ ] `termux-mcp` registered.
- [ ] Sync does not run destructive operations.
- [ ] Dirty repo refuses unsafe execution.
- [ ] Base ref drift is reported.

## Phase 5: Worktree Isolation and Promotion

### Goal

Make bundle execution safe by default using isolated worktrees.

### Required Work

- Create temporary worktree for execution.
- Apply bundle in worktree.
- Validate in worktree.
- Commit in worktree or promote patch back to canonical branch safely.
- Push only after validation.
- Keep main working tree clean on failure.
- Store execution artifacts.
- Add cleanup policy for old worktrees.

### Acceptance

- [ ] Worktree execution path exists.
- [ ] Validation failure leaves canonical checkout clean.
- [ ] Successful execution can commit and push.
- [ ] Failed execution produces observation JSON.
- [ ] Worktree cleanup is implemented.

## Phase 6: Observation, Failure Analysis, and Repair Loop

### Goal

Return structured observations that ChatGPT can use to repair failed changes.

### Required Work

- Normalize failure categories:
  - context_incomplete
  - base_head_mismatch
  - file_hash_mismatch
  - apply_failed
  - validation_failed
  - commit_failed
  - push_failed
  - remote_verify_failed
- Extract diagnostics from Python, Node, shell, git, and generic test output.
- Emit repair hints without hidden reasoning.
- Store observations under ignored artifact path.

### Acceptance

- [ ] Observation schema is enforced.
- [ ] Failed validation emits structured diagnostics.
- [ ] Push failure preserves local commit and reports exact failure.
- [ ] Repair loop input can be produced from a failed result.

## Phase 7: Recipe Layer for Deterministic Jobs

### Goal

Add recipes for common deterministic operations while keeping creative coding based on context capsule plus change bundle.

### Required Work

- Define recipe schema.
- Add recipes for safe common tasks:
  - append gitignore entry
  - update docs section
  - bump version metadata
  - create example file
  - cleanup ignored artifacts
  - run validation only
- Add recipe dry-run and execution modes.
- Keep recipe layer subordinate to change-bundle architecture.

### Acceptance

- [ ] Recipe schema exists.
- [ ] At least three safe recipes exist.
- [ ] Recipe execution uses same validation/commit/push policy.
- [ ] Recipe cannot bypass guardrails.

## Phase 8: `termux-mcp` Thin Wrapper Integration

### Goal

Expose codeplane capabilities through `termux-mcp` while keeping MCP thin.

### Required Work

In `humtr/termux-mcp`, add wrapper tools that call `termux-codeplane`:

```text
prepare_coding_context
execute_change_bundle
run_recipe_job
read_job_result
cancel_job
inspect_codeplane
```

The wrappers must:

- validate inputs
- call codeplane CLI or local API
- return structured JSON
- avoid duplicating codeplane business logic
- preserve existing p4 transaction tools until replacement is proven
- not change live runtime until migration phase

### Acceptance

- [ ] `~/prj/termux-mcp` has wrapper implementation.
- [ ] Existing p4 behavior remains intact.
- [ ] Wrappers call codeplane rather than duplicating logic.
- [ ] Wrapper validation passes.
- [ ] Commit is pushed.

## Phase 9: End-to-End Local Proof

### Goal

Prove the non-live source path end to end before live migration.

### Required Proofs

- Agent/terminal calls codeplane directly for context capsule.
- Agent/terminal calls codeplane directly for change bundle execution.
- `termux-mcp` wrapper calls codeplane for context capsule.
- `termux-mcp` wrapper calls codeplane for change bundle execution.
- A harmless test change validates, commits, pushes, and emits result JSON.

### Acceptance

- [ ] Direct codeplane proof exists.
- [ ] MCP wrapper proof exists in non-live checkout.
- [ ] Remote verification succeeds.
- [ ] Rollback path documented.

## Phase 10: Live Runtime Migration Plan

### Goal

Prepare but do not blindly execute migration from `~/work/termux-mcp` to `~/prj/termux-mcp`.

### Required Work

- Document current live runtime path.
- Document current live commit.
- Document current server start command.
- Document current Cloudflare/Worker/tunnel relation.
- Add rollback plan.
- Add migration checklist.
- Add post-migration health checks.

### Acceptance

- [ ] Migration doc exists.
- [ ] Rollback doc exists.
- [ ] User explicit approval required for live switch.
- [ ] No live switch happens during planning only.

## Phase 11: Live MCP Migration and Proof

### Goal

After explicit approval, switch live MCP runtime to the canonical `~/prj/termux-mcp` path or otherwise make `~/prj` the source of truth while preserving service availability.

### Required Work

- Stop or quiesce live MCP safely.
- Record previous live path/commit.
- Start MCP from approved path.
- Verify health endpoint.
- Verify `server_info`.
- Verify Worker backend connectivity.
- Run one read-only wrapper proof.
- Run one safe write proof if authorized.
- Keep rollback ready.

### Acceptance

- [ ] User explicit approval recorded.
- [ ] Live server path is correct.
- [ ] Health checks pass.
- [ ] Worker route works.
- [ ] Rollback remains possible.
- [ ] Final status recorded in `GOAL.md`.

## Phase 12: Production Hardening and Operating Model

### Goal

Make the architecture durable enough for repeated ChatGPT/Agent development work.

### Required Work

- Add job/session store.
- Add artifact retention policy.
- Add audit log.
- Add config file and defaults.
- Add schema validation to all public commands.
- Add security guardrails:
  - safe roots
  - forbidden path patterns
  - secret scanning before commit
  - no force push
  - no tag push by default
  - no remote branch deletion
- Add validation profiles per project.
- Add regression tests.
- Add docs for normal operation, failure recovery, and manual override.
- Decide whether Worker queue/Durable Object/KV is needed now or later.
- If Worker queue is implemented, document control-plane/data-plane split.

### Acceptance

- [ ] Job/session store exists or deliberate deferral is documented.
- [ ] Audit log exists.
- [ ] Artifact retention policy exists.
- [ ] Security guardrails are enforced.
- [ ] Secret scan or equivalent pre-commit guard exists.
- [ ] Validation profiles exist.
- [ ] Regression tests exist.
- [ ] Operating docs exist.
- [ ] Final architecture proof is recorded.

## Full Architecture Completion Checklist

The architecture is not complete until all of the following are true:

- [ ] `termux-codeplane` repository exists and is pushed.
- [ ] `termux-mcp` repository exists and is pushed.
- [ ] `goal-md` alias `termux-codeplane` exists.
- [ ] `termux-codeplane/GOAL.md` exists and is updated as live ledger.
- [ ] `termux-codeplane` owns mirror/sync.
- [ ] `termux-codeplane` owns repo registry.
- [ ] `termux-codeplane` owns repo indexing.
- [ ] `termux-codeplane` owns context capsule generation.
- [ ] `termux-codeplane` owns change bundle execution.
- [ ] `termux-codeplane` owns recipe execution for deterministic jobs.
- [ ] `termux-codeplane` owns worktree isolation.
- [ ] `termux-codeplane` owns validation tiers.
- [ ] `termux-codeplane` owns commit and push policy.
- [ ] `termux-codeplane` emits structured observations and result JSON.
- [ ] `termux-codeplane` stores job/session state or documents a deliberate deferred design.
- [ ] `~/prj/termux-mcp` exists as canonical source checkout.
- [ ] live `~/work/termux-mcp` remains stable until explicit migration.
- [ ] `termux-mcp` exposes thin wrappers for codeplane context and bundle operations.
- [ ] Worker/tunnel/MCP integration path is documented.
- [ ] force push, tag push, branch deletion, unsafe paths, and secret leakage are guarded.
- [ ] end-to-end proof exists: ChatGPT/Agent -> MCP or terminal -> codeplane -> validate -> commit -> push -> result.
- [ ] live migration plan exists.
- [ ] live migration is performed only after explicit approval.
- [ ] production hardening checklist is complete or explicitly deferred with rationale.

## Required Final Report

When stopping, report:

```text
Outcome:
Completed phases:
Current phase:
Local path:
Remote:
Commits:
Validation:
Push:
Final status:
Blockers:
Next required action:
GOAL.md updates:
```

If stopped before Phase 12, explain why and identify the exact first incomplete acceptance item.

Do not describe Phase 1, Phase 2, or Phase 3 as final completion.

## Live Progress Ledger

Initial state:

- [x] external goal created in `humtr/goal-md`.
- [x] `goals/index.json` registered alias `termux-codeplane`.
- [x] `humtr/termux-codeplane` exists as a private repository.
- [x] `humtr/termux-mcp` exists as a private repository.
- [x] User reported repository preflight completed.
- [ ] Agent must verify local `~/prj` status at start.
- [ ] target repository `GOAL.md` created.
- [ ] Phase 0 complete.
- [ ] Phase 1 complete.
- [ ] Phase 2 complete.
- [ ] Phase 3 complete.
- [ ] Phase 4 complete.
- [ ] Phase 5 complete.
- [ ] Phase 6 complete.
- [ ] Phase 7 complete.
- [ ] Phase 8 complete.
- [ ] Phase 9 complete.
- [ ] Phase 10 complete.
- [ ] Phase 11 complete.
- [ ] Phase 12 complete.

Current phase:

```text
Phase 0 consolidation pending: Agent must verify local prepared repos and write target repo GOAL.md.
```

Next action:

```text
Run Agent with this goal. Agent must verify Phase 0, create/update ~/prj/termux-codeplane/GOAL.md, then proceed through Phase 1, Phase 2, and Phase 3 at minimum. If Phase 3 completes safely, continue into Phase 4+.
```

## Not Proven Yet

- Whether `~/prj/termux-codeplane` local checkout is clean and ready.
- Whether `~/prj/termux-mcp` local checkout is clean and pushed.
- Whether worktree execution can be fully implemented in the first Agent invocation.
- Whether Phase 3 real self-proof should commit a harmless example change or stay dry-run only.
- Whether future `termux-mcp` wrappers should be added as a separate app name or under a later p5/p6 surface.
- Whether Worker queue is required before live migration or can be deferred until after local MCP wrapper proof.
