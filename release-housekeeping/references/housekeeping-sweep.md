# Housekeeping sweep: cleanup without a release

The owner starts this when they want to find and clean leftovers of work that
never went through a release's cleanup: a small job finished but not cleaned,
a session closed midway, a worktree a builder made in a scratch folder. The
cleanup itself is the same as step 6 of this skill and cleanup.md; what this
reference adds is finding the leftovers, proving what each is, and asking the
owner part by part. There is no PR, merge, deploy or migration here.

It never runs on a schedule or as a side effect of another command. Running it
authorizes the read-only plan only; nothing is removed until the owner approves
that part.

## 1. Scope: the repository of the open folder

Resolve the repository the session's working folder belongs to (its common Git
directory), and sweep only that repository: its worktrees wherever they live,
its local branches, its branches on origin, and Docker resources whose Compose
working directory label (`com.docker.compose.project.working_dir`) points into
the repository or one of its worktrees. Nothing in another repository or
elsewhere on the disk is touched; something noticed there is mentioned, not
planned.

## 2. Find (read-only)

Fetch origin first (`git fetch origin`), so "merged" is judged against the
current remote. Then collect facts with commands:

| Kind | Facts |
| --- | --- |
| Worktree (`git worktree list --porcelain`) | Path, branch or detached HEAD, locked/prunable flags, last commit date, `git status --short --untracked-files=all`, ignored files of value from `git status --short --ignored` (.env, local databases, data/ or upload folders), commits not in origin/main (`git log --oneline origin/main..HEAD`), PR of its branch (`gh pr list --head <branch> --state all`), who made it (host session, Codex/Orca task, scratch folder) |
| Host-managed worktree | The owning session in the host's session list, and whether it is archived. Idle is not archived |
| Local branch without a worktree | Commits not in origin/main, PR state and whether the merged PR's head equals the branch tip, whether a host session names it |
| Remote branch on origin | Same merged proof, and no open PR from it |
| Docker (this repo only) | Stopped containers and their networks by Compose project; volumes listed, never planned for removal |
| Local main | Clean? Behind origin/main? (cleanup.md section 1) |
| Stale worktree metadata | `git worktree prune --dry-run` |

Record free disk on the repository's drive before anything.

## 3. Classify

Two conditions make a leftover cleanable. Both must be proved; neither is ever
waived by the owner's approval of a part:

1. Every commit it holds is in origin/main: by ancestry, or by a merged PR whose
   head equals the branch tip (squash merge).
2. It is not the main worktree.

| Group | Means |
| --- | --- |
| READY | Both conditions hold and nothing below stands in the way |
| NEEDS_STEPS | Both conditions hold, but something stands in the way (table below); each is resolved with the owner one step at a time |
| NOT_MERGED | Condition 1 fails. Not finished work: reported and kept |
| KEPT | The main worktree, the folder this session runs in, volumes and their data, anything shared or owned by another tool |

What stands in the way, and the step offered for it:

| Obstacle | Options put to the owner (recommendation first when clear) |
| --- | --- |
| Uncommitted or untracked files | Show the list; discard them, or keep the item |
| Ignored files of value (.env, local DB, data/) | Show what they are and their size; delete with the item, copy them somewhere the owner names first, or keep the item |
| An open PR from the branch | Show the PR; close it, or keep the item |
| The folder this session runs in | Cannot remove itself: detach it at origin/main so the branch can go, and say the host removes the folder when the session is archived |
| Locked worktree | Show the lock reason; unlock, or keep |

A host session that owns a cleanable worktree or local branch is not an
obstacle and is not asked about (owner decision 15/11): archiving it is part of
cleaning that item, and the owner's approval of the part covers it. The plan
names each such session with its last activity. Archiving is always the last
step of the item, after any obstacle above is resolved. Two limits stay: never
archive the session this sweep runs in (its row above), and never archive a
session that is mid-turn or owns an item that is NOT_MERGED or KEPT. Report
those and keep them.

## 4. Plan, then ask part by part

Show the plan before changing anything, in the owner's language, grouped into
parts. Each line: what it is, its proof in a few words, its size.

- A. READY worktrees, and READY local branches that have no worktree, each with
  the host session that owns it, which is archived with the item
- B. READY merged branches on origin (their proof does not depend on the local
  branch, so A and B can be approved in either order)
- C. NEEDS_STEPS items whose obstacles include anything other than a host
  session, each with its obstacles in the order they will be asked
- D. (no separate part: owning host sessions are archived with their item in
  A and C)
- E. Stopped test containers and networks of this repo (volumes kept)
- F. Local main fast-forward and stale worktree metadata
- NOT_MERGED and KEPT: listed with the reason (and the owning session, if
  any, for information), never part of an approval

Each item appears in exactly one part. An item with a host session AND another
obstacle is in C, never also in A: archiving a session lets the host delete its
worktree with everything in it, so its uncommitted or ignored files are asked
about first and archiving comes last. The folder this session runs in is the
session's own working directory; compare paths, do not guess.

Then ask the owner which parts to clean, one part at a time. An answer covers
exactly the items listed in that part. Silence or an unclear answer is no.
Do not remember earlier answers between sweeps: every sweep asks again.

## 5. Clean what was approved

Before each action, re-check that item's facts; if anything changed, show it
and ask again instead of acting. Then:

- A: a worktree owned by a host session: archive that session with the host's
  own tool, confirm the host removed the folder, and do not remove it with Git.
  A worktree no host session owns: `git worktree remove <exact path>` from
  outside it (no --force). Then `git branch -d <exact branch>` (-D only under
  cleanup.md's exact-branch exception, for a squash merge proved in section 3).
  For a local branch with no worktree, delete it the same way, then archive
  any host session that names it. Archive only after re-checking the session
  is not mid-turn and is not the session this sweep runs in.
- B: `git push origin --delete <exact branch>`, one by one, after confirming
  the remote tip still equals the proved tip.
- C: walk each item's obstacles in order, one prompt per obstacle, acting only
  on the answer. When none remain, clean it as in A, including archiving its
  host session as the last step. A "keep" on any obstacle ends that item: it
  is kept, and its session is not archived.
- D: nothing separate; see A and C.
- E: remove the named stopped containers and their project networks without
  volumes, only when test-environment-policy.md section 3 holds.
- F: fast-forward local main only if clean (cleanup.md section 1); run
  `git worktree prune` only for entries the dry run listed.

Never in this sweep: volume removal or prune, `docker system prune`, image
prune -a, `git clean -x`, reset, stash, --force, or any change in the main
worktree beyond a clean fast-forward.

## 6. Report

Close like a release report without the release: what was removed (paths,
branches, IDs), what was kept and why (NOT_MERGED, KEPT, and what the owner
declined), what a re-check changed, and free disk before and after measured the
same way. Status: CLEANUP_COMPLETE when every approved part is done, or
CLEANUP_PENDING with the approved items that could not be done and why.
