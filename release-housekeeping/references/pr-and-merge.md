# Preflight, publication and merge

## Resolve the target and effects

Inspect repo instructions, current Git state and all worktrees. Verify origin's
actual URL/owner/repository, target main branch and PR host; do not trust CWD or a
branch name alone. Preserve dirty/staged/untracked files and any local commits.
Read CI and deployment triggers before pushing: PR previews, main deploys and
migrations are externally consequential side effects, not harmless metadata.
Use configured host connectors/CLI, do not install a new integration implicitly.

Ensure the release ledger/evidence destination survives cleanup. Know how to
recover the prior deployed artifact and database state before risking them.
A backup reference should include time, scope and actual verification evidence;
'we probably have backups' is not a verified recovery plan.

## Candidate and PR

- Require an applicable READY_FOR_PR result for the selected change, not a generic
  promise. Record approved spec/revision, base SHA, reviewed candidate commit SHA,
  author/reviewer, relevant checks and actual publishing authority.
- The change is normally already committed on its branch. Inspect the full diff
  from base to the reviewed SHA for unrelated changes, secrets, test artifacts
  and generated junk before pushing. If anything reviewed still needs
  committing, stage exact files; do not default to `git add .` or amend
  unrelated commits. A commit hook changing code invalidates affected prior evidence.
- Before pushing, inspect whether the branch already exists remotely and whether
  somebody else advanced it. Never force-push or overwrite that work by default.
- Query for an existing open/merged PR for this repo/base/head. Reuse or report it;
  retries must not create duplicate PRs. Use explicit repo/base/head when creating.
- The PR body is concise: outcome, AC/evidence links, exact checks and pending CI,
  risk/compatibility, deploy components, migration plan and rollback pointer.
  Private logs and secrets stay out of public artifacts.

Example CLI forms only; substitute inspected values and the repo's approved
method. These are not unattended scripts or commands to run against placeholders:

```text
git -C <CHANGE_WORKTREE> status --short --untracked-files=all
git -C <CHANGE_WORKTREE> diff --cached
gh pr create --repo <OWNER/REPO> --base main --head <OWNER:BRANCH> --title <TITLE> --body-file <FILE>
gh pr checks <PR> --repo <OWNER/REPO>
gh pr view <PR> --repo <OWNER/REPO> --json state,baseRefName,headRefOid,mergeCommit,mergedAt,statusCheckRollup
```

## Merge gate

Required CI, review and branch rules must actually be satisfied for the selected
head or merge-queue candidate. Resolve failures through normal development and
focused review; do not edit checks to make a release pass. Low-risk docs-only
changes still honor repo policy. Don't call skipped/cancelled jobs green.

Select the repo-approved merge method. With GitHub CLI, a head-matching guard is
available, for example `gh pr merge <PR> --repo <OWNER/REPO> --squash
--match-head-commit <REVIEWED_HEAD_SHA>` (use one command in the actual shell).
Do not copy `--squash` if the repo requires another method. Never use `--admin`
to bypass policy. Do not add `--delete-branch`: retain branch/worktree until the
release is healthy and housekeeping has verified ownership and merge proof.

The platform may require a merge queue or auto-merge. Record WAITING_MERGE until
mergedAt/state and the merge result are real. Do not promise asynchronous
monitoring unless the host actually provides it. On resume query the platform,
not the previous assistant narrative. Capture PR head SHA and actual merged SHA
separately; they may differ after squash/rebase/queue integration.

Before deployment, establish that the merged commit is on the intended remote
main and identify which build it produced. If the service only deploys 'latest',
resolve intervening commits explicitly; don't silently widen the approved release.
Remote main changing during synchronization is a race to observe, not permission
to overwrite it or indefinitely retry.

Confirm the result of an outward step before running the step that depends on
it. Do not chain "merge" with "move the checkout to the merged main" in one
command: a merge that fails transiently leaves the checkout on the old main.
Read the PR state and the merge commit first, then continue.

## Failures and branch retention

Merge/push/PR failures do not authorize deletion, force actions or remote-main
rewrites. Retain the worktree and source branch while a release is blocked. If
branch auto-deletion is configured on the platform, record that fact and protect
local recovery/evidence instead of recreating it automatically.
