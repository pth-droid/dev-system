---
name: release-housekeeping
description: "Release an approved change through PR creation, policy-compliant merge to origin/main, necessary deployments and ordered migrations, deployment verification, safe local-main synchronization, and cleanup of change-owned worktrees and disposable test resources. Use only when asked to plan, execute, resume or finish a release/housekeeping operation; never auto-release merely because development is ready."
---

# Release and Housekeeping

Keep the release reproducible and the cleanup narrower than the resources created.
Use existing repo tooling. This skill defines release method and safety gates;
the external workflow assigns agents/models and the runtime executes operations.
Do not create a swarm, dispatcher, scheduler, provider binding or new CI system.

## Modes and authority

Accept plan-only, execute, resume or cleanup-only as natural-language intents,
not magic CLI flags. Default to plan-only if execution authority is absent.
The request to install this skill is NOT authority to publish, merge, deploy,
migrate, delete branches or remove data in any repository.

For execution, record exact repo/remote, branch/PR, environments, components,
migration IDs/order, cleanup allowlist and authorization source. A single explicit
approval or valid standing policy may authorize the whole disclosed sequence;
do not ask again at every already-covered step. Ask only for missing material
scope, destructive exceptions, ambiguous targets or new risk. Explain business
context, options, tradeoffs, risks and recommendation before asking the owner.
Never infer permission from tool credentials or from READY_FOR_PR.

## Non-negotiable boundaries

- Respect branch protection, required checks, approvals, secrets, existing edits
  and host permissions. Do not bypass CI/review, force-push main, reset/stash user
  work, silently widen the release, or claim success from a pending job.
- Verify upstream identity and deployment side effects BEFORE push/merge. A
  push/merge may trigger automatic deployment or migrations. Include those in
  the approved plan before taking the triggering action; do not duplicate them.
- Pin the reviewed head, actual merged commit and deployed artifact separately.
  A queue/squash/rebase can change commit identity. Never deploy a moving main
  tip without establishing the exact intended artifact and its checks.
- Make migrations dependency-ordered, not blindly 'after deploy'. Never reset a
  live database, use a development schema-sync shortcut, guess SQL rollback,
  edit applied migration history, or rerun an uncertain non-idempotent job.
- Separate data cleanup from runtime lifecycle and storage retention. Preserve
  pre-existing reusable test infrastructure and KEEP volumes by default, even
  after removing eligible containers. Never delete source tests, baseline fixtures,
  snapshots, migration history or retained bind data as cleanup. A resource used
  or created for testing is not automatically disposable. Never use broad Docker
  prune, reset the daemon or shut down the shared server to reclaim memory.
- Keep the live execution ledger and install/rollback artifacts outside any
  retiring worktree. Re-read actual state on resume; don't replay commands just
  because a checkbox or previous assistant message says they are unfinished.

## Load references only when needed

| Step | Reference |
| --- | --- |
| Preflight, PR and merge | [pr-and-merge.md](references/pr-and-merge.md) |
| Component impact, migrations, rollout and smoke | [deploy-and-migrate.md](references/deploy-and-migrate.md) |
| Local main and resource retirement | [cleanup.md](references/cleanup.md) |
| Existing/reusable test environment and data | [test-environment-policy.md](references/test-environment-policy.md) |

Use [release-record.md](assets/release-record.md) selectively in the durable runtime
ledger, with links to the existing spec and evidence. Do not create a duplicate
engineering document tree or commit every operational status change.

## 0. Preflight and resumable release plan

Read the repo's instructions and verified release setup. Locate the approved
change, exact candidate and pre-PR evidence; check current head/dirty state and
open PRs, existing deployments/migration histories and owned test resources.
Identify the actual primary checkout, common Git directory and main worktree.
Default remote/target is origin/main as requested, but verify the repository's
real convention; report a mismatch instead of renaming branches or remotes.

Build a concise plan: what will change where, PR/merge policy, artifact identities,
component impact and dependencies, migration sequence, rollback/roll-forward,
production smoke plan and exact cleanup targets. Use repo-tested commands, not
invented package-manager or cloud commands. Classify no-deploy/no-migration paths
with evidence (for example docs-only); do not skip a needed downstream service.

Resolve authority once for the known plan. Stop before irreversible/external
steps if a prerequisite is missing. Record checkpoints so failure can resume.

## 1. Create or reuse PR

Read pr-and-merge.md. Work from the approved change branch/worktree. The change
is normally already committed there: inspect the full diff from base to the
reviewed candidate SHA and push only as allowed. Stage exact files if anything
reviewed still needs committing.
Bind checks to the resulting commit; run affected checks if hooks changed it.
Reuse a matching PR or create one with explicit repository, base and head, ACs,
real check evidence, deployment/migration impact and remaining CI status.
Do not invoke branch deletion as part of the merge command.

## 2. Merge to the actual remote main

Wait/check for actual required checks and review policy, using bounded foreground
status checks or return WAITING_CI/WAITING_MERGE. Merge through the hosting service,
not by pushing a local unreviewed merge to main. Match the expected PR head where
supported. An accepted auto-merge/queue request is NOT proof of merge.
Verify merged state and capture merge SHA. If conflicts/new commits change the
candidate, return to targeted development verification before proceeding.

## 3. Deploy only the necessary release unit and migrations

Read deploy-and-migrate.md. Compare the target artifact with the last deployed
version of each component, not merely the last local commit. Include dependency,
config, API and schema consumers. Use the approved single executor (CI or manual)
for each action, and the compatible migration/deploy order. Capture migration
history and artifact IDs; don't invent a generic deploy command.
Observe automated deploys instead of duplicating them. If main has advanced, pin
or resolve the intended release, rather than silently deploying unrelated work.

## 4. Verify deployment before retirement

Check real job completion, desired artifact identity, health/readiness and a small
representative smoke path plus migration/backfill checks where applicable. Prefer
read-only/synthetic safe production checks. Do not rerun the whole dev audit.
A healthy old version or a 200 response alone does not establish new-code rollout.

On failure, preserve diagnostics, halt destructive cleanup and follow only the
approved rollback/roll-forward procedure. Report partial success honestly (for
example merged but migration failed). A code rollback may not undo data changes.

## 5. Synchronize local main safely

Read cleanup.md. Fetch origin and update the correct clean, unlocked main worktree
only by fast-forward; confirm its HEAD and refs/heads/main equal the freshly
observed origin/main. Protect unrelated changes, local-only commits and other
agents. Never hard-reset to manufacture parity. Report BLOCKED or cleanup-pending
when main cannot be safely synchronized. Deployment SHA may differ from a later
main SHA; record both. Do not redeploy just because the remote advanced.

## 6. Retire change-owned resources

After successful rollout (or approved no-deploy path) and main synchronization,
archive evidence OUTSIDE retiring worktrees and read test-environment-policy.md.
Freeze only this run's writers, identify the exact safe data boundary and clean
its approved run data while required services remain available. Preserve schema,
seeds and baseline accounts. A retained volume does not clean its records for you.

Apply the verified per-environment policy: DATA_ONLY for shared/always-on systems;
CONTAINERS_KEEP_VOLUMES for an eligible idle dedicated stack; scoped disposable
runtime retirement for per-change infrastructure, also KEEP volumes by default.
Preserve exact volume IDs, bind data, stable project identity and a surviving
startup recipe. Never delete a worktree containing the only reusable config/data.
Remove only eligible containers after cleanup, without volume deletion. Unknown
ownership, active consumers or an unverified recreation path block that action.
Then retire safe generated artifacts/worktree/branch under cleanup.md. Deliberate
storage/environment decommission is a separate explicitly scoped operation.
Measure only actual observations; do not invent disk/RAM reclaimed.

## 7. Close with independent outcomes

Report PR URL/state, reviewed and merged SHAs, per-component deployment/artifact,
migration state, smoke evidence, local-main parity, removed/retained resources,
measured disk/memory observations and follow-up blockers. Keep per-step status;
never call the release wholly failed merely because cleanup is pending, or call
housekeeping complete when required actions are blocked. Expected assets retained
by policy are successful outcomes, not leftover failures.

Use: PLAN_READY, WAITING_CI, WAITING_MERGE, RELEASE_BLOCKED, RELEASE_FAILED,
RELEASED_CLEANUP_PENDING, COMPLETE, or CLEANUP_COMPLETE for a separately scoped
cleanup-only job. COMPLETE requires the selected release and cleanup scope to be
satisfied, each retained/skipped action justified. RETAINED_BY_POLICY is compatible
with COMPLETE; required unsafe/unavailable data cleanup is cleanup-pending. This skill neither enforces permissions
nor guarantees deployment safety; verified repo setup and host controls do that.
