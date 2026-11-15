# Compact specs, vertical tasks, and handoffs

## One change record, not a document factory

Prefer existing specs and trackers. Otherwise keep the spec, task table, and
verification summary in one change record. Use the bundled template selectively.
Separate an accepted behavior contract from mutable implementation notes.

Capture the business goal, actors, non-goals, approved decisions and rationale,
and acceptance criteria with stable IDs such as AC-01. Include relevant negative
cases, state transitions, permissions, thresholds, and persisted effects. Preserve
exact agreed values. Define expected results independently of the implementation.
Record the test coverage proposal in observable behavior terms, including limits.

Keep conceptual architecture in the spec. Put current file paths, commands, and
snapshot details in task/handoff notes, where their revision can be checked.
Avoid an exhaustive list of speculative stories. Do not omit an important agreed
requirement to make the document shorter. Mark actual approval and its source;
never backfill fictional approval records.

## Divide by demonstrable outcome

Make each task a small end-to-end result, not a code layer. A task should fit one
focused working context and be verifiable without guessing what later tasks will
do. It need not touch UI, API, and database if the actual behavior needs only one.

For example, a goods-receipt feature might have these slices:
- T1: An authorized employee records a valid receipt for one store and reads it
  back with its stock effect. Include the required authorization in this slice.
- T2: A retry of the same submission does not create another receipt/stock effect.
  Blocked by T1. Keep the feature unshipped until this required safety property passes.
- T3: An authorized manager corrects an eligible receipt with an auditable effect,
  only if correction is part of the approved scope. Blocked by T1 and any actual
  integrity dependencies. Do not invent the correction policy yourself.

Show the owner the outcome order and any meaningful delivery tradeoff. The agent
owns the dependency graph and technical file division; do not ask the owner to
validate engineering minutiae. Work only on tasks whose real blockers are done.

For each task record: ID, outcome, AC IDs, blockers, scope boundaries, complexity,
risk, required evidence, and status. The external workflow assigns an implementer
and controls concurrency; this skill does not select resources.
Do not create remote tickets, branches, or PRs without authorization.

Only add a preparatory refactor or exploratory spike when a concrete obstacle
justifies it. Keep it bounded and do not let throwaway exploratory code silently
become production. For broad incompatible migrations, propose an explicit safe
sequence and approval rather than forcing independent slices that cannot work.

Trace a relaxed gate one step downstream. When a decision removes or loosens a
blocking condition (a line may be empty, a check no longer stops the flow),
follow the data one layer further before writing it into the behavior contract
and record which layer receives it and whether that layer accepts it. A decision
the next layer rejects is not deliverable; return it to the owner with that fact.

Give each task a line saying where its evidence runs (pure test on the dev
machine, integration test in which environment, real-click check on which
stack). An environment that cannot be started yet is provisioned before the
first task is dispatched, not discovered at the second.

## Transfer work only when useful

Prepare a handoff when the caller requests a transfer or the work cannot continue
with the current capabilities. Do not decide the recipient, create sessions, or
restart merely because a phase changed. Describe what context is needed. The portable
handoff is a pointer-rich delta, not a second copy of the spec or the whole chat.
Use an allowed scratch/temporary location and state where it is.

A handoff must include:
- Goal, task/AC IDs, approved spec pointer/revision, and accepted decisions.
- Repo/workspace, base SHA and current commit SHA, any work not yet committed,
  and existing user changes that must not be overwritten.
- Owned scope/current relevant paths and explicit non-goals.
- Checks already run, exact results and evidence locations, including failures,
  rejected hypotheses, stale evidence, and environmental limitations.
- One next concrete action, remaining blocker, required tool capabilities,
  stop conditions, and caller-supplied budget constraints.

Redact secrets and private customer data. The receiving agent verifies current
state before acting; a stale handoff is not permission to overwrite new work.
Its return message should normally be a few hundred words plus pointers: changed
files, AC status, tests/evidence, unresolved issues, and next action. Do not omit a
critical risk merely to fit a word target.

If workers do not share a filesystem, use only an explicitly supported transfer
mechanism and record the commit/patch. Never imply changes were integrated when
only a prose report was received. When the workflow runs independent changes in
parallel, each uses its own worktree and branch; reverify the combined candidate
if they ship together.

Tell the builder what to do when the assignment is wrong. A premise that turns
out false but does not touch business behavior, stored data or blocking rules:
follow the assignment's intent and report the deviation. Anything that would
change those, or that reaches outside the assigned scope: stop and report the
exact reason.

A baseline check that is not green before the first edit is classified, not
automatically a stop. Record the failing lines first either way, so old failures
are never mixed with new ones:

| The baseline fails because | Then |
| --- | --- |
| It reproduces exactly the bug this task was assigned to fix | Record it as the task's intended RED (tdd.md) and continue |
| An old failure unrelated to this task | Record it separately; continue only if it does not void the evidence for the part being changed |
| A broken environment, or a failing premise not yet understood | Stop the affected part and report the blocker |

"Exactly the assigned bug" means the failing assertion matches the reported
symptom; a failure that merely sits in the same file is the second row.

## Feedback is an evidence-backed work item

Group findings with one root cause and give stable IDs (F-01, F-02). Record the
AC/source, expected versus observed behavior, reachable path, proof type, impact,
evidence pointer and minimal correction objective. Keep confirmed defects,
unverified concerns, scope questions and nonblocking suggestions distinct.

A worker return should state the candidate, changed files, AC results, exact
check outcomes and unresolved items. Never report only "done" or "all tests pass".
For a repair, return each finding ID with its resolution evidence. Do not promise
that a repair is integrated if the receiver has only a patch or prose report.

## Workspace fields in every assignment / handoff

Include the absolute primary/main checkout, assigned development worktree, branch,
base SHA, common Git directory identity, and runtime/evidence ledger path. Specify
safe test endpoint/namespace, Docker context and Compose project when used.
The receiving agent must recheck these facts and use the assigned worktree as its
working directory. Keep operational checkpoints outside a worktree scheduled for
retirement. The external workflow, not this skill, provisions these resources.

## Minimal contracts and larger initiatives

Use an existing approved description as the source when it fully states the
intended behavior. A small repair needs a concise durable record, not a second
approval ceremony or full template. Keep stable AC references even if there is
only one task. For a milestone inside a larger initiative, cite the parent plan
but treat only the selected milestone as the current build contract. Do not infer
approval of future work. Report unexpected wider impact before broadening edits.
