# Worktree-first development lifecycle

This is lead/orchestrator policy. Dev-guardrails checks the workspace invariant;
this workflow decides when to provision or resume it. Use the installed host's
actual tools, permissions and OS shell. No automatic model/tier routing is added
inside either skill.

## 1. Resolve identity and scope

Resolve the target repository from the user's nominated path or active session,
NOT the installer/handoff file's directory. Read repo instructions and inspect
remote URLs, current branches, dirty/untracked state, ongoing operations and
`git worktree list --porcelain`. Resolve the actual common Git directory and the
worktree that checks out main; the initial clone is not necessarily on main.

An authorized 'start development in its own worktree' includes scoped branch and
worktree creation, not publication or deployment. Respect any narrower host/user
permissions. Leave unrelated dirty files and branches untouched. Read-only planning
may precede creation; all change-specific repo writes require the worktree,
except the no-logic edit path in dev-router.md section 3a.

Choose a sanitized unique change ID and branch, such as `work/<change-id>` under
repo conventions. Choose an absolute absent destination outside the primary
checkout, for example a sibling `<repo-name>-worktrees/<change-id>` directory.
Do not nest another Git worktree in a source tree, reuse a nonempty directory,
follow a path outside the approved parent, or force an existing branch checkout.
An already dedicated active change worktree can be reused after identity checks.

## 2. Select a real base and create once

For a NEW feature, fetch the verified origin and resolve a pinned origin/main SHA
unless a different base is explicitly approved. If remote access is unavailable,
record the blocker; don't silently pretend a stale local base is current. A
separately approved cached base must be labeled with its provenance.

For EXISTING in-progress work, reuse its recorded branch/worktree. Do not start
again from main and lose its modifications, nor copy uncommitted changes from a
primary clone without a scoped transfer plan.

Illustrative commands, with inspected absolute paths, no unexpanded placeholders:

```text
git -C <REPO> remote -v
git -C <REPO> worktree list --porcelain
git -C <REPO> fetch origin
git -C <REPO> rev-parse refs/remotes/origin/main
git -C <REPO> check-ref-format --branch <NEW_BRANCH>
git -C <REPO> worktree add --no-track -b <NEW_BRANCH> <ABSENT_ABSOLUTE_PATH> <PINNED_BASE_SHA>
git -C <NEW_WORKTREE> status --short --untracked-files=all
git -C <NEW_WORKTREE> branch --show-current
```

Do not set the feature's upstream to main by accident, use -B/--force, reset local
main, or commit unrelated work just to make workspace setup convenient. Freeze
base SHA, branch and path in the runtime checkpoint; creation alone starts no tests.

## 3. Make instructions and test resources available

Verify skills/workflow/repo policy are readable from the new worktree. Prefer
tracked repo installation already present at the pinned base. If system files
are installed but uncommitted/unmerged, use the approved stable absolute source
read-only or copy ONLY the explicitly approved system/config paths with provenance
and inspect the resulting diff. Report this bootstrap gap; do not silently carry
product modifications, production secrets or arbitrary home configuration.

Do not blindly copy .env from primary. Use approved test credentials and data.
Prefer a safe authorized existing test environment and isolate run data rather
than automatically create a new stack. Allocate unique ports/database/schema/
Compose project only where needed. Inspect explicit names, binds, volumes and
consumers; do not change the stable project/volume identity of a reusable stack.
Record data scope, retention and durable recreation recipe before using it.
The presence of a separate worktree is not proof of runtime isolation.

Use project-setup's configured durable state root outside all disposable checkouts.
One option is `<resolved-common-git-dir>/agent-workflow-state/<change-id>/`;
resolve a relative --git-common-dir result correctly for the current CWD/version.
This operational directory is not Git's own worktrees/objects/refs directory and
must never be removed with a broad cleanup command. Do not persist secrets there.

Create a small resource ledger only for resources actually allocated. Record
worktree/branch/base, main checkout, exact IDs/paths, context/host/project, ownership,
disposability, dependencies, required retention and cleanup authority. Reuse the
template [resource-ledger.md](resource-ledger.md), not a sprawling asset database.
Keep state/evidence out of the retiring worktree; approved spec and source tests
remain normal versioned repo content.

## 4. Dispatch and resume

Pass explicit worktree and skill paths in every assignment. Check real CWD before
each command; tool calls must set it or use explicit -C/path flags. Default one
writer per change worktree. Main reads/reviews; the builder performs TDD/fixes.
Changes that do not affect each other may run in parallel under
daily-workflow.md section 1: use distinct branches/worktrees and resource
names, then verify the combined candidate when they ship together. No shared mutable dependency directory
or database should defeat the separation.

Resume the same worktree through feedback loops and the next day. A missing or
moved worktree is a reconciliation problem, not permission to delete metadata or
recreate it on top of another folder. Record operational ownership and halt stale
writers before reassignment. Avoid polling idle workers continuously.

## 5. Retire only at the approved end

READY_FOR_REVIEW/READY_FOR_PR and session wrap-up do not authorize worktree removal.
Transfer its ledger to release-housekeeping when release is requested. Retain
source/test code and evidence; final housekeeping deletes only verified disposable
artifacts. Cancellation/abandonment needs its own explicit scope and preservation
check, rather than masquerading as a successful deployed release.
