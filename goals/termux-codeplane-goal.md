# Goal: Termux Codeplane Bootstrap and Full-Code Execution Plane

## Objective

Create `humtr/termux-codeplane` as the Termux-specific full-code cognition and execution plane for ChatGPT-led development.

`termux-codeplane` must become the local engine that owns:

- repository mirror and sync
- full-code indexing
- context capsule generation
- change bundle application
- git worktree sandboxing
- validation
- commit
- push
- structured result and observation reporting

`humtr/loop` remains the generic PR-ops, handoff, readiness, schema, and workflow-pattern framework. `termux-codeplane` is a Termux-specific implementation derived from those concepts, not a replacement for `humtr/loop`.

`humtr/termux-mcp` remains the ChatGPT-facing MCP bridge. It should eventually become a thin facade that delegates code cognition and execution work to `termux-codeplane`.

## Canonical Local Path

```text
/data/data/com.termux/files/home/prj/termux-codeplane
```

## Remote Target

```text
git@github.com:humtr/termux-codeplane.git
```

## Operating Rule

This goal is not complete after the first successful bootstrap.

Do not stop after Phase 1 unless a hard blocker occurs.

After completing and pushing Phase 1, continue to Phase 2 in the same working session if possible.

After completing and pushing Phase 2, continue to Phase 3 in the same working session if possible.

Only stop when one of these is true:

1. Phase 3 is completed, validated, committed, pushed, and final status is clean.
2. A platform, authentication, repository-creation, validation, or push blocker prevents further safe progress.
3. The user explicitly cancels the task.
4. Continuing would require a destructive operation forbidden by this goal.

A successful Phase 1 push is a checkpoint, not a final answer.

A successful Phase 2 push is a checkpoint, not a final answer.

The final target for the first agent run is Phase 3 unless blocked.

## Repository Roles

### `humtr/loop`

Generic framework repository.

Owns:

- reusable PR-loop patterns
- generic handoff/readiness concepts
- generic schemas and examples
- cross-repo operation philosophy
- reference material only

Must remain unchanged during this task.

### `humtr/termux-codeplane`

New Termux-specific implementation repository.

Owns:

- Termux local repo mirror
- code index
- context capsule builder
- change bundle executor
- worktree sandbox
- validation runner
- commit and push execution
- result and observation artifacts

### `humtr/termux-mcp`

Existing MCP bridge.

Do not move or refactor `~/work/termux-mcp` during Phase 1.

Do not migrate `termux-mcp` from `~/work` to `~/prj` during this goal unless a later explicit task says so.

During this goal, `termux-mcp` is referenced only as the future integration target.

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

Do not move, delete, or rewrite:

```text
/data/data/com.termux/files/home/work/termux-mcp
```

Do not change the current Cloudflare Worker, tunnel, or MCP registration during Phase 1 or Phase 2.

### Push Policy

Push is included in this task.

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

## Execution Strategy

Work in phases, but do not treat phase boundaries as stopping points.

Each phase must end with:

- local validation
- git status
- commit
- push
- remote verification where practical
- short checkpoint note

Then continue to the next phase immediately.

If validation fails:

- diagnose the failure
- repair if the cause is clear
- rerun validation
- do not commit or push broken code unless the phase explicitly records a non-executable design-only artifact and validation still passes for repository integrity

If push fails:

- keep the local commit
- report the local commit hash
- report the exact push failure
- do not force push

## Phase 1: Bootstrap Repository and Project Identity

### Goal

Create `humtr/termux-codeplane` as a pushed GitHub repository with clear project identity, architecture docs, schemas, examples, and a minimal validation surface.

### Required Work

1. Verify Termux tools:

```bash
git --version
python3 --version
gh --version
gh auth status -h github.com
gh config set git_protocol ssh
```

2. Create local repository:

```text
~/prj/termux-codeplane
```

3. Create or connect remote repository:

```text
humtr/termux-codeplane
```

Use `gh repo create` if the remote does not exist.

4. Add project identity files:

```text
README.md
GOAL.md
docs/architecture.md
docs/runtime-model.md
docs/push-policy.md
docs/derived-from-loop.md
```

5. Add core schema files:

```text
schemas/project-manifest.schema.json
schemas/context-request.schema.json
schemas/context-capsule.schema.json
schemas/change-bundle.schema.json
schemas/execution-observation.schema.json
schemas/job-result.schema.json
schemas/codeplane-session.schema.json
```

6. Add example files:

```text
examples/context-request.sample.json
examples/context-capsule.sample.json
examples/change-bundle.sample.json
examples/job-result.sample.json
```

7. Add minimal validation tooling:

```text
tools/codeplane_validate.py
Makefile
```

8. Add initial Python package skeleton:

```text
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
```

At Phase 1, these modules may be skeletal, but they must be syntactically valid and must clearly state their responsibility.

### Phase 1 Validation

Run:

```bash
python3 -m py_compile $(find codeplane tools -name '*.py' | sort)
python3 tools/codeplane_validate.py
git status --short --branch
```

### Phase 1 Commit

Commit message:

```text
Initialize termux-codeplane
```

### Phase 1 Push

Push to:

```text
origin/main
```

### Phase 1 Acceptance

- [ ] `~/prj/termux-codeplane` exists.
- [ ] `humtr/termux-codeplane` exists.
- [ ] remote uses SSH.
- [ ] README explains the project.
- [ ] GOAL.md exists and says Phase 1 is not the final stop.
- [ ] architecture docs exist.
- [ ] all required schemas exist.
- [ ] all required examples exist.
- [ ] Python files compile.
- [ ] `tools/codeplane_validate.py` passes.
- [ ] commit is pushed to `origin/main`.
- [ ] final local status is clean.
- [ ] continue to Phase 2 unless blocked.

## Phase 2: Code Cognition MVP

### Goal

Implement the minimum useful local code cognition engine.

`termux-codeplane` must be able to inspect a local git repository and generate compact context capsules for ChatGPT coding work.

### Required Work

Implement or improve:

```text
codeplane/repo.py
codeplane/indexer.py
codeplane/context.py
codeplane/cli.py
codeplane/result.py
```

CLI commands required by the end of Phase 2:

```text
python3 -m codeplane.cli inspect-project --repo <path>
python3 -m codeplane.cli build-index --repo <path> --out <path>
python3 -m codeplane.cli prepare-context --request <json> --out <json>
python3 -m codeplane.cli validate-self
```

### Phase 2 MVP Capabilities

`inspect-project` should report:

- repo path
- whether it is a git repo
- current branch
- current HEAD
- clean/dirty status
- remote URL if available
- package manager hints if available
- known validation scripts if available

`build-index` should generate a JSON index with:

- file manifest
- file sizes
- sha256 hashes
- basic language classification
- package scripts when `package.json` exists
- recent commit summary when available

`prepare-context` should produce a context capsule with:

- base HEAD
- repo cleanliness
- relevant file list
- relevant search matches
- selected file slices or full small files
- sha guards
- context completeness status

This does not need tree-sitter or full symbol graph yet. Literal search and file slices are acceptable for MVP.

### Phase 2 Validation

Run:

```bash
python3 -m py_compile $(find codeplane tools -name '*.py' | sort)
python3 tools/codeplane_validate.py
python3 -m codeplane.cli validate-self
python3 -m codeplane.cli inspect-project --repo .
python3 -m codeplane.cli build-index --repo . --out .codeplane-index.sample.json
python3 -m codeplane.cli prepare-context --request examples/context-request.sample.json --out .context-capsule.sample.out.json
git status --short --branch
```

Generated sample output files may be removed before commit unless intentionally kept under `examples/`.

### Phase 2 Commit

Commit message:

```text
Add code cognition MVP
```

### Phase 2 Push

Push to:

```text
origin/main
```

### Phase 2 Acceptance

- [ ] `inspect-project` works on `termux-codeplane` itself.
- [ ] `build-index` works on `termux-codeplane` itself.
- [ ] `prepare-context` produces a valid context capsule.
- [ ] validation passes.
- [ ] commit is pushed.
- [ ] local status is clean.
- [ ] continue to Phase 3 unless blocked.

## Phase 3: Change Bundle Execution MVP

### Goal

Implement the minimum useful deterministic executor for ChatGPT-generated change bundles.

`termux-codeplane` must be able to apply a structured change bundle in a safe git worktree, validate it, commit it, push it, and report the result.

### Required Work

Implement or improve:

```text
codeplane/bundle.py
codeplane/worktree.py
codeplane/validation.py
codeplane/gitops.py
codeplane/result.py
codeplane/cli.py
```

CLI commands required by the end of Phase 3:

```text
python3 -m codeplane.cli execute-bundle --bundle <json>
python3 -m codeplane.cli read-result --result <json>
python3 -m codeplane.cli validate-self
```

### Change Bundle Requirements

A change bundle must support at least:

```text
operation: create
operation: append
operation: replace
```

Each edit must include:

- path
- operation
- content for create/append
- search and replace for replace
- optional expected sha256 guard

Bundle-level fields must include:

- project or repo path
- base HEAD
- validation tier or checks
- checkpoint policy
- commit message
- push flag

### Worktree Policy

Execution should use a temporary git worktree or an equivalent safe isolated path.

Main working tree must remain clean on validation failure.

If worktree implementation is not fully complete in Phase 3, the code must clearly mark the limitation and default to a non-destructive dry-run unless execution is explicitly requested.

### Validation Policy

At minimum support:

```text
validation tier: none
validation tier: self
validation tier: standard
```

For `termux-codeplane` itself:

```text
self:
  python compile
  tools/codeplane_validate.py

standard:
  self + CLI smoke commands
```

### Commit and Push Policy

If validation passes and the bundle requests commit/push:

1. commit the change
2. push to `origin/main`
3. verify remote main where practical

Do not force push.

### Phase 3 Validation

Run:

```bash
python3 -m py_compile $(find codeplane tools -name '*.py' | sort)
python3 tools/codeplane_validate.py
python3 -m codeplane.cli validate-self
python3 -m codeplane.cli inspect-project --repo .
python3 -m codeplane.cli build-index --repo . --out .codeplane-index.sample.json
python3 -m codeplane.cli prepare-context --request examples/context-request.sample.json --out .context-capsule.sample.out.json
```

Then perform one safe self-proof if practical:

- create a change bundle that appends a harmless ignored sample output path to `.gitignore`, or
- create/update a small example file under `examples/`, or
- run execute-bundle in dry-run mode if a real self-change is too risky.

The self-proof must not force push.

### Phase 3 Commit

Commit message:

```text
Add change bundle execution MVP
```

### Phase 3 Push

Push to:

```text
origin/main
```

### Phase 3 Acceptance

- [ ] `execute-bundle` exists.
- [ ] create/append/replace operations are represented.
- [ ] base HEAD guard is represented.
- [ ] file hash guard is represented or explicitly stubbed with a clear TODO.
- [ ] validation tiers exist.
- [ ] result JSON is produced.
- [ ] commit and push policy is implemented or clearly guarded behind explicit flags.
- [ ] validation passes.
- [ ] commit is pushed.
- [ ] local status is clean.
- [ ] final report is written.

## Phase 4: Future MCP Integration

Do not start Phase 4 unless Phase 3 is completed or the user explicitly asks.

Future goal:

- add `termux-mcp` wrappers for:
  - `prepare_coding_context`
  - `execute_change_bundle`
  - `read_job_result`
- keep `termux-mcp` thin
- do not migrate `~/work/termux-mcp` to `~/prj/termux-mcp` until explicitly approved

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
```

If stopped before Phase 3, explain why.

Do not describe Phase 1 as final completion unless Phase 2 and Phase 3 are explicitly blocked or cancelled.

## Acceptance Ledger

- [ ] Phase 1 repository bootstrap complete.
- [ ] Phase 1 commit pushed.
- [ ] Phase 2 code cognition MVP complete.
- [ ] Phase 2 commit pushed.
- [ ] Phase 3 change bundle execution MVP complete.
- [ ] Phase 3 commit pushed.
- [ ] `humtr/loop` unchanged.
- [ ] `~/work/termux-mcp` unchanged.
- [ ] no force push used.
- [ ] no secrets committed.
- [ ] final local status clean.
- [ ] final remote status verified where practical.

## Not Proven Yet

- Whether `gh repo create` is already authenticated on this Termux device.
- Whether `humtr/termux-codeplane` already exists remotely.
- Whether worktree execution can be fully implemented in the first Agent invocation.
- Whether Phase 3 real self-proof should commit a harmless example change or stay dry-run only.
- Whether future `termux-mcp` wrappers should be added as `termux-codeplane-p1` or as a later `termux-mcp-p5`.
