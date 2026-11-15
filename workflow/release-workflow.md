# Release orchestration (separate from the development method)

Use this only for an explicit release/PR/cleanup request or valid recorded standing
authority. Reading this file or installing a skill does not authorize production
changes. A single scoped authorization can cover the disclosed normal sequence;
ask again only when scope/risk changes or a destructive exception wasn't covered.

## Assignment and context

Keep the existing main/lead, normally Tier 1, responsible for release decisions
and interpreting gates. Use the existing builder or runner for a bounded command
when worthwhile. The lead may execute a short mechanical step directly; don't
spawn a third agent just to call Git. Any assigned operator must read the
release-housekeeping skill and relevant reference. Maintain one release executor
per environment/change and one migration executor; CI ownership takes precedence
when the approved runbook makes CI responsible.

Do not create another verification panel. Reuse development evidence for unchanged
inputs; deploy smoke checks prove the rolled-out artifact, not the whole product.
Keep PR/merge/deploy jobs and runtime ledger in the existing context where useful.
Raw logs stay in accessible files; return actual exit states, IDs and short evidence.

## Transition and actions

| Stage | Action / actual gate |
| --- | --- |
| RELEASE_PLANNING | Inspect setup, candidate, auto triggers, component impact, migration history and cleanup allowlist; resolve authority |
| PR_OPEN / WAITING_CI | Push the reviewed candidate commits if authorized; reuse/create PR; observe actual required checks |
| WAITING_MERGE | Apply platform policy/queue; pending acceptance is not merged |
| MERGED | Record actual merged commit and intended artifact; don't follow a moving main implicitly |
| RELEASING | Execute/observe the approved migration and deploy dependency plan once |
| VERIFYING_DEPLOY | Verify artifact, readiness, changed smoke path and data/migration result |
| SYNCING_MAIN | Fetch and fast-forward only a safe main checkout; prove equality to observed origin/main |
| CLEANING | Archive evidence; clean scoped run data; apply runtime/volume retention; remove only eligible artifacts/worktree/branch |
| COMPLETE | All selected gates satisfied; report partial results separately otherwise |

Migration ordering is part of RELEASING, not a mandatory step after deploy. If
merging itself triggers rollout, all prerequisites must be ready before MERGED.
A docs-only change can skip deploy/migration with a recorded reason, not a fake
success. A PR-only request stops at the authorized PR state. Cleanup-only reuses
verified release facts and does not recreate a PR or redeploy.

## Blockers and repairs

On required CI failure or a pre-merge defect, send one focused packet to the same
builder in the same change worktree. Use TDD/delta review, not a whole new audit.
Changes to the reviewed candidate invalidate affected evidence and head guards.

On deployment/migration failure, record partial states, preserve worktree/logs/
rollback artifacts and stop destructive housekeeping. Investigate the exact
failure with the existing lead. Follow the approved rollback/roll-forward plan;
a new code repair after merge normally gets a new tracked change and worktree.
Do not patch production outside policy, rerun non-idempotent migrations blindly,
or delete the evidence that would explain the failure.

When CI/queue/platform actions remain pending, save WAITING_* and a next concrete
status query. Do not claim work will continue in the background unless the host
actually supports and starts it. Resume by inspecting the service's real state.

If deployment succeeded but a required action is blocked (dirty main, unsafe
required data cleanup, missing recreation proof), report RELEASED_CLEANUP_PENDING.
A shared resource retained by policy is not a blocker by itself. No amount of
token pressure warrants deleting unowned data. Ask the owner only the consequential unresolved decision with
context, options, risks and recommendation, not low-level technical trivia.

## End

Persist the release record and resource disposition in the durable state root,
not inside the folder about to be removed and not as a new main commit just to
record that main was synchronized. Return PR/artifact/SHAs, real migration/smoke
outcomes, main parity, cleanup results and honest resource measurements.

## Reusable-environment policy applies to every release path

Before retiring resources, require the verified environment classification and
resource ledger. Clean scoped run data first; keep shared/always-on runtime or
remove eligible idle containers while retaining volumes/config and startup recipe.
Do not delete a worktree still needed by retained bind mounts or Compose inputs.
Read release-housekeeping/references/test-environment-policy.md from the actual
installed skill path. Expected retention is COMPLETE-compatible, not a reason to
retry cleanup. Missing required data cleanup/retirement proof is pending, not a
reason to destroy the environment. Deliberate decommission is separately scoped.
