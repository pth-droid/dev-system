---
description: Release the finished change (PR, merge, deploy, verify) and then clean up its leftovers, following the Dev System release-housekeeping skill. Use when the owner types /ship or says in plain words "ship", "ship đi", "phát hành đi", "release đi", "lên prod đi", "đưa lên máy chủ" about work that is finished in this session.
argument-hint: "[plan | cleanup | <change name>]"
---

Run the release-housekeeping workflow for the change this session is working on.
Arguments: $ARGUMENTS

1. Read `D:\Working\Dev system\release-housekeeping\SKILL.md` and follow it; load its
   references only when a step needs them. Read the repository's own instructions and
   deploy runbook first; they win over the skill's templates.
2. Mode from the arguments:
   - empty or a change name: execute. The owner typing this command (or saying "ship đi")
     is the single approval for the whole standard sequence: push the branch, open the PR,
     merge to origin/main under the repo's policy, deploy and migrate the affected components
     per the runbook, verify the real deployed state, sync local main, then clean up (step 4).
     Verifying always means the deployment check (version the server reports, service up,
     one read-only run of the changed path, independent of the deploy script). Do not
     click through screens on production after the deploy.
   - `plan`: show the plan only, change nothing.
   - `cleanup`: only step 4, for work already released.
3. Before the first outward step, show the plan in at most ten lines: change, candidate
   commit, components affected, migrations, expected downtime, rollback path, and the
   cleanup list. Then continue without waiting, unless the plan contains something beyond
   the standard sequence (an unclear target, a failed check, a change that is not
   READY_FOR_PR). In that case stop and ask one question with options and a recommendation.
4. Cleanup, only after the release is verified, and only for what this change owns
   (its resource ledger, or resources this session created for it):
   - remove: the change's local and remote branches once merged, its worktree, its test
     containers and network, its temp files and fixtures;
   - keep: volumes and data, anything shared or created before the change, anything not
     merged, anything whose owner is unclear. List these and ask once instead of removing.
   - the session's own folder: a session cannot remove the worktree it runs in. If this
     session runs inside the change's worktree, detach it at origin/main, delete the branch,
     leave the folder, and say that the app removes it when the session is archived.
5. Finish with one short report: what was released (PR, merge commit, deployed version),
   what was verified and how, what was not verified, what was removed, what is left and why.
