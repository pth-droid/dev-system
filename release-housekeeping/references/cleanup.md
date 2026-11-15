# Safe local synchronization and owned-resource retirement

Contents: [Main](#1-synchronize-local-main) | [Plan](#2-plan-and-preserve) |
[Docker](#3-retire-test-services-and-docker-resources) | [Files](#4-worktree-files-and-branches) |
[Report](#5-measure-and-report)

## 1. Synchronize local main

After a verified deployment or justified no-deploy path, find the actual main
worktree from `git worktree list --porcelain`. The original clone may have a
feature branch checked out; do not switch it blindly. Inspect status, staged and
untracked files, active Git operations, locks and known active writers. Ignored
files that could be overwritten also need care. Never stash/reset/clean user work.

Verify origin identity; fetch main without changing the checked-out files.
Compare local main to the fetched origin/main. If main is clean and strictly
behind (or equal), run `git -C <MAIN_WORKTREE> merge --ff-only origin/main`.
Record exit status; confirm both refs and main worktree HEAD equal the freshly
fetched SHA. --ff-only can report success when local main is already ahead, so
an exit code alone is not proof of parity. Check ancestry/divergence and equality.

If main is ahead, diverged, dirty, locked, absent, checked out by another active
writer, or origin/main cannot be fetched reliably, preserve it and report the
exact blocker. Do not use reset --hard, auto-stash, a force ref update, or create
a main merge commit. An unused/main worktree can be provisioned only within
explicit authorization. Do not force-checkout the same branch twice.

Main parity is at a recorded fetch/time, not a guarantee the remote cannot advance
later. If it advances during this run, re-fetch/recheck once and explain ongoing
movement. Do not deploy unrelated newer commits to 'match main'. Store deployed
SHA and final observed main SHA separately. Retain retiring resources if required
main synchronization is blocked unless a separate scoped cleanup is authorized.

## 2. Plan and preserve

Read the change's resource ledger. For each target require exact absolute path
or resource ID, repo/change ownership, host/context, purpose, disposable status,
retention dependencies and permission. A name containing 'test' is not proof.
Identify references by other worktrees, running/stopped containers or release
rollback processes. Unknown/shared resources are retained and reported.

Pause or stop only owned writers/services; verify no further writes can happen.
Archive the necessary redacted logs, minimal repro, release record, PR/commit
proofs and rollback references in the durable state root OUTSIDE the deleting
tree. Never delete the only copy of a database, .env, user file or uncommitted
artifact. Do not store secrets in the report or upload them with a PR.

Show the exact deletion list, what is retained and why. Existing approval of a
known disposable-resource policy may cover this list; unknown data/destructive
exceptions need a specific decision. Do not turn this into a global cleanup job.
Use a reviewed removal plan; many tools have no safe automatic dry-run.

Before retiring a test environment, check whether a follow-up change on the
same area has already been requested. If so, keep the environment and its
worktree, record in the resource ledger that they pass to that change, and
still delete the merged branches.

## 3. Retire test services without destroying reusable environments

Read [test-environment-policy.md](test-environment-policy.md) before changing data
or containers. It governs reusable environments and supersedes a vague old label
such as 'disposable volume'. Identify the actual TEST host/context, project and
active consumers; never assume the daemon is local or a test name makes it safe.

Classify data, runtime and storage independently. DATA_ONLY keeps shared/always-on
services intact. CONTAINERS_KEEP_VOLUMES removes eligible idle containers only
AFTER scoped data cleanup and durable recreation checks. Even per-change runtime
cleanup keeps volumes by default. Unknown ownership means retain and report.

Clean only authorized run data through a reviewed scoped recipe while needed
services are available. Preserve baseline rows, schema/migration history, test
accounts and fixtures. Do not truncate/drop/reset shared data, flush entire queues
or remove volume files to manufacture a clean test state. Container removal is
not logical data cleanup. Verify both deletion scope and retained baseline.

Keep exact named/external volume identities or a verified explicit reattachment
recipe for anonymous mounts. Preserve durable bind data, Compose config, required
image/build inputs and secret-store references OUTSIDE retiring worktrees. A new
worktree name must not silently create an empty replacement volume next session.
No removal when persistent state may exist only in the container writable layer.

Prefer targeted stop/remove of eligible container IDs or services. A full scoped
Compose down WITHOUT volume deletion is allowed only for an entirely eligible
idle stack with no shared/always-on services/networks affected and a safe surviving
startup recipe. No rm -v, down --volumes, volume rm/prune, system prune or renewal
of anonymous volumes in ordinary housekeeping. Storage decommission is separate.
No --remove-orphans or --rmi all by default. Keep reusable images/shared cache;
only explicitly disposable, unneeded per-run artifacts may be removed.

Measure scoped workload and Docker/host disk before/after when available. Do not
confuse logical record deletion, volume bytes, image sizes, host free disk and
workload RAM. Do not compact a database/VHD, restart Docker, reboot or shut down
WSL to improve a metric. Report unknown metrics honestly.

## 4. Worktree, files and branches

Finish eligible scoped data/runtime cleanup BEFORE deleting the worktree. Check
that no retained environment, container or bind mount depends on this directory;
never delete its only Compose/startup recipe or reusable data. Keep evidence safely archived first. Preserve tracked product tests,
fixtures, snapshots and migrations in the merged repository. 'Test cleanup' means
owned generated reports, scoped disposable run-data and runtime files, not the
test suite or reusable database/baseline. Verify durable content is in the merged artifact or retained backup.

Check status including staged, unstaged, untracked AND ignored contents. Use
`git status --short --untracked-files=all`, `git status --short --ignored`, and
bounded inspection of ignored directories. A normal clean status can hide .env,
local databases and precious untracked ignored files. Resolve symlinks/junctions;
do not traverse outside an allowlisted owned root. Never delete a source-root,
home directory, shared Git directory, other worktree or arbitrary temp folder.

Confirm the PR is actually merged into the expected main, the recorded PR head
matches the retired branch tip, and the worktree has no newer work. Leave it if
another PR/worker depends on the branch. Archive branch recovery evidence where
required. Use `git worktree remove <EXACT_WORKTREE>` from a surviving directory;
do not `rm -rf` it and do not use --force to bypass dirty/submodule protections.
If removal refuses, inspect and preserve the cause. Do not force completion.

Delete only the associated local branch AFTER worktree removal. `git branch -d`
is the normal path. A squash/rebase merge may not satisfy Git's ancestry test.
Never interpret that refusal as blanket permission for -D: verify the host's
merged PR, exact retired head, equivalent integrated content and absence of later
commits, and require an explicitly authorized exact-branch deletion exception.
If that exception isn't already in the approved plan, retain the branch and report
cleanup pending. Retention is safer than losing unknown work. An approved exact
exception must still not delete main, a shared branch or another checked-out branch.

Remote branch deletion is separately scoped: confirm no newer remote tip,
reuse by collaborators or dependent open PRs. Do not delete it merely because
local cleanup was requested. Respect platform auto-deletion if already done.
Worktree metadata pruning is not disk cleanup; review `git worktree prune --dry-run`
only for stale owned entries and preserve unavailable/removable-drive worktrees.
Do not prune all metadata blindly or run aggressive repository GC as housekeeping.

## 5. Measure and report

Re-list worktrees/branches and targeted Docker resources. Confirm main parity and
any remaining running test workload. Compare exact host/context disk and memory
observations with timestamps; mark unavailable readings UNKNOWN. Shared concurrent
activity and image layer sharing limit attribution; do not sum image sizes as
'reclaimed disk'. List removed IDs/paths, retained assets and reasons.

Return COMPLETE only when the approved release and all required cleanup are done.
Otherwise RELEASED_CLEANUP_PENDING with deployment success preserved and explicit
blockers. Expected retained volumes/config/shared services count as RETAINED_BY_POLICY,
not a cleanup failure. Report a genuinely blocked required action as pending.
Never hide a dirty main, uncleaned required run data or lost restart recipe.
