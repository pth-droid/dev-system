# Dedicated development workspace

## Invariant

Develop in one registered Git worktree for this change, on an owned non-main
branch. Planning, TDD, implementation, fixes and review use that same workspace.
A worktree is NOT an isolated database, Docker daemon, secret store, or permission
sandbox. The workflow must also allocate separate test data and services.

One exception: a no-logic edit (wording, docs, spacing) assigned by the caller
may use a short non-main branch in the current checkout, provided that checkout
has no uncommitted work and no other active change.

The external workflow creates/resumes the workspace; this reference defines the
checks every acting developer/reviewer must perform. Do not select a model or
create a worker here. Report missing workspace capability to the lead.

## Before any writes

1. Resolve the assigned absolute worktree path and Git repository identity.
   Check `git worktree list --porcelain`, current branch and HEAD, common Git
   directory, tracked/untracked state and concurrent ownership. Reject an
   unrelated checkout, main branch, detached work without an explicit approved
   purpose, or an existing workspace belonging to someone else.
2. Match the change/task, branch, base SHA, worktree path and approved spec to the
   assignment. On resume, revalidate; do not assume last session's CWD persists.
3. Read applicable repo instructions from this worktree, plus the installed skill
   path supplied by the workflow. An untracked installation in the primary clone
   does not automatically appear in a newly created worktree. Use an authorized
   verified read-only skill path or provision only the approved config files;
   never copy the entire primary checkout or its secrets into the new worktree.
4. Use explicit tool working directories or `git -C <WORKTREE>` for every command.
   Reject a command whose resolved write target is outside owned scope. Record
   the shell/OS; do not assume POSIX syntax works in Windows PowerShell.
5. Confirm test endpoints, database/schema, ports, Docker context and Compose
   project name. Check for fixed shared names, external volumes, host binds and
   production credentials. Merely setting a new Compose project name is not
   enough if the config explicitly shares those resources.

Where the worktree lives follows the repository's existing convention when it
has one.

## Preserve continuity and data

Keep the same branch/worktree for a coherent change and its repairs. Commit
completed tasks on that branch so every review and resume starts from a commit
SHA; committing is local, pushing is not part of development. Rebase or
update the base only under repo policy; re-evaluate affected evidence afterward.
Do not stash/reset/clean unrelated changes, force-add a worktree, force-switch a
checked-out branch, symlink writable dependency folders across active worktrees,
or run tests against a shared production database.

Record durable operational checkpoints and a resource ledger OUTSIDE the
worktree that will later be deleted. A configured location under the common Git
directory (for example `agent-workflow-state/<change-id>/`) is an option; this is
not committed product code. The workflow resolves the actual absolute path.
Keep approved specs/tests in the project convention; do not move business intent
solely into ephemeral logs. Redact secrets and preserve necessary evidence before
teardown. Do not keep the only copy of the install bundle inside a disposable tree.

For every created test resource record: absolute path or exact resource ID,
host/context/project, ownership, purpose, disposable yes/no, dependencies,
retention and cleanup authority. Unknown ownership means retain, not delete.

## Completion

Return worktree/branch, candidate and resource-ledger pointers with the normal
handoff. Do not delete this worktree when returning READY_FOR_REVIEW or
READY_FOR_PR. Retire it only through an authorized release/housekeeping operation
or a separately authorized cancellation. Keep source tests, migrations, fixtures
and snapshots; do not mistake the repo's test suite for test-run litter.

## Existing reusable test environments

A dedicated code worktree does not require a new test stack. Reuse an existing
approved environment if it safely isolates this run's data. Record its lifecycle,
scoped cleanup recipe, retained volumes/bind mounts and stable startup identity.
Never attach unknown production data or delete baseline fixtures. Retained test
config/data must not depend solely on a disposable worktree. Report missing
isolation or recreation facts instead of improvising a new environment/reset.
