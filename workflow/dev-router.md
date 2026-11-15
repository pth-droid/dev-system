# /dev - Scope-aware entry workflow

Version: 4.1 / 2026-11-14. Run this as the lead/main agent, not a new classifier
subagent. The native host adapter forwards the request here. This is orchestration
policy, not a third development skill or an executable agent dispatcher.

## 1. Resolve the current session before choosing a lane

Read the repo instructions, relevant project-setup facts and an existing active
checkpoint. Identify the actual intent: plan, implement/fix, verify-only, or
resume. An empty /dev resumes one unambiguous active change. If there is no goal,
ask for it; if several changes compete, ask one priority question. Do not pick a
random backlog item. The calendar or a new chat is not a reason to restart work.
A request to clean leftovers of finished work, with nothing to release, is not
a dev lane: it is the release-housekeeping skill's housekeeping sweep
(/housekeeping).

Inspect the affected entry points, tests, current behavior and relevant callers
only as needed to understand scope. Use a short targeted inspection, not a whole
repo audit, new agent swarm or exhaustive interview. Unknown root cause is not
proof of a quick fix. Read-only triage may occur in the primary checkout. Follow
worktree-lifecycle.md BEFORE the first repo write or mutating reproduction. The
no-logic edit path in section 3a is the only exception.

Classify three independent dimensions:
- SIZE: one bounded correction; one cohesive feature; or multiple milestones.
- RISK: low; ordinary/medium; high (access/security, money/inventory, cross-tenant
  data, concurrency/idempotency, irreversible data changes, deployment contracts).
- UNCERTAINTY: behavior and approach clear; needs bounded investigation; or
  consequential product/architecture decisions remain.

Use evidence, not line count, file count, guessed completion time, model tier or
whether the owner used the words 'quick', 'small', or 'just'. A one-line change can
be high risk. One large generated diff can still be mechanically simple.

## 2. Select the smallest safe lane

| Lane | Eligibility | Treatment |
| --- | --- | --- |
| QUICK_FIX | One bounded correction/minor adjustment with clear expected behavior, understood local cause/approach, low risk, existing patterns/checks, no consequential new decision, public/data contract, migration, permission or external-service change | No-logic edit (3a): short branch, commit message as the record, one fitting check. Small behavior fix (3b): micro contract, one task, targeted TDD/checks and focused review |
| STANDARD | One cohesive feature, a meaningful behavior change, an uncertain bug needing investigation, or ANY small high-risk fix | Compact approved contract, vertical tasks as needed, proportional risk-based verification |
| LARGE | Several independently useful outcomes/milestones, major architecture or multi-component rollout dependencies, or decisions whose effects require staged delivery | Plan first, resolve material decisions, milestone map, then implement ONLY the selected approved milestone via STANDARD |

Risk is an overlay, not a synonym for size. A small financial/security patch is
STANDARD + HIGH, not automatically a giant feature. A large low-risk interface
change still needs milestone/session scope if it cannot be verified coherently.
If evidence is insufficient, provisionally choose STANDARD / investigation-only,
state the uncertainty and inspect further. Never classify a mystery as QUICK_FIX.
A known unused parameter/UI wording bug can be QUICK_FIX even though a new small
regression test is needed; 'existing checks' means a usable test environment, not
that the bug already has a test.

Announce the decision in 2-4 lines in the owner's language, e.g. lane/risk, reason,
this session's outcome and next action. Classification itself requires no owner
approval. The owner can request more scrutiny or a smaller outcome. A request to
rush cannot waive required risk checks, authority or branch protection.

Match the builder to the lane. A QUICK_FIX and a STANDARD task whose design is
already decided in the assignment go to the lower-cost builder pool; main names
the pool or model explicitly on every dispatch instead of inheriting its own.
The strongest pool is for design-heavy or high-risk work and for main's review.

## 3. QUICK_FIX - remove ceremony, not safeguards

QUICK_FIX has two paths. Choose between them from the edit itself, not from the
owner's wording.

### 3a. No-logic edit (lightest path)

Use this path only when ALL of these hold: the edit changes wording, docs,
comments, spacing or another purely visual value; it touches no condition,
calculation, data, permission, money, migration, API contract or dependency;
and reverting one commit undoes it completely.

1. A clear instruction to make the edit is its approval. Ask nothing more.
2. No dedicated worktree is needed. Create a short branch from the fetched
   origin/main in the current checkout; never edit on main itself. Use a
   worktree instead when that checkout has uncommitted work or another change
   is active in it. A session that already runs in its own worktree uses that.
3. Main makes the edit itself. No builder, change record or resource ledger.
4. Run one check that fits the edit: a before/after screenshot for wording or
   visual changes, a build or lint run for docs and comments. Do not invent a
   failing unit test.
5. Commit on the branch, staging exact files. The commit message is the whole
   record: what changed, why, and how it was checked.
6. Report READY_FOR_PR with the commit SHA, the diff and the before/after
   evidence, so the owner sees the result at a glance. No push, merge or deploy.

If the edit turns out to need a logic change, stop and continue under 3b or
STANDARD on the same branch. This path needs nothing beyond sections 1-3a of
this file: do not load daily-workflow.md, the dev-guardrails references or
release material for it.

### 3b. Small behavior fix

1. Treat a clear explicit instruction to repair a stated existing behavior as its
   behavior approval; do not ask the owner to approve the same intent twice.
   Distinguish this from a question/plan-only request. Missing consequential
   behavior decisions or missing edit/worktree permission still block writes.
2. Create/reuse the change's dedicated worktree under the existing approved policy.
   Keep one micro record in the existing change/checkpoint system, not a new PRD,
   task board or architecture essay. Record goal/expected behavior, non-goal,
   1-3 representative ACs when sufficient, approval source, lane/risk, worktree/
   candidate, evidence and final state. No numeric AC cap may hide requirements.
3. Default to the available suitable builder with one task, main doing a short
   final review. For a truly trivial low-risk edit, main may perform and honestly
   self-review it if spawning a worker is more overhead; no mandatory third agent.
4. For a behavior bug, capture a focused meaningful regression RED, fix and observe
   GREEN; run affected checks plus repository-mandated gates. For pure wording,
   docs or visual-only edits, record the appropriate non-TDD evidence instead of
   inventing a fake failing unit test. A layout assertion needs visual evidence
   when code-level checks cannot establish it.
5. Review the ACs, actual candidate/diff and meaningful assertions. If a defect is
   found, send one focused feedback packet to the SAME builder. Recheck affected
   evidence only, including transitive callers when relevant.
6. Commit the fix on the change branch; the candidate is that commit SHA. For a
   fix the owner can see or use, run the owner check in the dev-guardrails
   verification.md before reporting readiness.
7. Finish at READY_FOR_PR / NEEDS_WORK / BLOCKED; no auto-push, merge or deploy.

Skip an additional brainstorming interview only when there is nothing material
to decide. Skip duplicate paperwork, not worktree isolation, provenance, TDD for
behavior changes, relevant tests, security checks or honest completion states.

### 3c. Where a QUICK_FIX runs: a fresh low-cost session that reports back

A QUICK_FIX done inside a long lead or orchestration session pays for that
session's whole context on every step; for a small fix that overhead costs more
than the fix. When the host can start a separate session and receive its
report, the orchestrating session hands the fix to a NEW session on the
low-cost model recorded in project-setup.md, and stays out of the loop until
the report arrives. 3a and 3b still say what the fix needs; this only says
where it runs.

A handed-off fix is a choice of who does the work, never a lower standard: the
same TDD, evidence and owner-check rules apply. Not every small fix is worth a
new session; when one word or one line would cost less to change here than to
brief, start and receive a worker, the lead does it itself under 3a/3b.

Hand it off only when ALL of these hold; otherwise run it as 3a/3b with the
lead's review:
1. Something to check against already exists: a test that covers the edited
   place, or a result that is visible at a glance.
2. The design fits in one sentence; nothing is left to decide.
3. It stays inside a few files of one module, listed in the assignment.
4. It writes no data and touches no ledger, permission, money or migration.
   This one is absolute; the new session never weighs it.
5. Reverting one commit undoes it.

The new session knows nothing the lead knows, so the assignment carries the
minimum it needs: the absolute worktree path, the branch, the base SHA, the
behavior to reach in one sentence, the files it may touch, the check to run
(exact command), where to write the report, "no push, merge, deploy or
production access", and this section. Two handed-off fixes never share a file.

The new session first re-checks the five conditions against the actual code.
If one fails it stops and says which, without editing. Otherwise it follows 3a
or 3b, commits on its assigned branch, and reports. The report opens with what
the orchestrating session needs, within the first 400 characters: one status,
the commit SHA, the check that ran and its result line, and what was not
checked. The detailed evidence (command, raw output, the SHA it ran on) goes to
the named report file and stays readable there.

| Status | Means |
| --- | --- |
| READY_FOR_REVIEW | Committed, the check ran on that commit, evidence in the file |
| BLOCKED | A condition failed or something prevents the fix; says which, nothing edited or what was left |
| NEEDS_OWNER_CHECK | Committed and checked, but the result is something the owner must look at |

On receiving the report the orchestrating session does not re-run a check that
is still valid just for reassurance. It does read the diff (for a small fix,
reading the small diff is the proportionate review; a correct file list does
not prove a correct edit), compares changed files with the assignment, and
reads the evidence file. It runs the affected check itself, or sends it back,
when the evidence is missing, ran on another SHA than the candidate, is
ambiguous, or does not show the assigned behavior. It then looks at the end
state when the change is visible and reports to the owner. Release and cleanup
follow the usual path.

## 4. STANDARD - the normal daily development loop

Use daily-workflow.md and dev-guardrails. If a sufficient approved spec exists,
start at its current phase without reopening settled decisions. Otherwise ask only
material owner questions with context, options, tradeoffs, risks and advice, then
obtain a combined behavior/coverage approval. Agent chooses technical details.

Implement one cohesive approved change using vertical slices, one builder per
worktree, a local commit per completed task, main-review/same-builder-fix and
delta rechecks. Changes that do not affect each other may run in parallel under
daily-workflow.md section 1. A change the owner can see or use passes the owner
check (verification.md) before READY_FOR_PR. Do not require a worker for each
layer, test or slice. High-risk paths require non-author review of the important
implementation; main qualifies when it did not author it. Preserve mandatory
negative/integrity cases; never treat happy-path success as feature completion.
A known difficult task may go straight to the suitable pool; no forced tier ladder.

## 5. LARGE - staged scope, not a bigger swarm

First create/reuse a compact overall intent, major decisions, dependencies and a
milestone map. Avoid specifying every future implementation detail now. Explain
material architecture choices by business/operational outcomes before approval.

Separate parent initiative from CURRENT SESSION/MILESTONE. Select the next useful
vertical milestone with explicit in/out scope, ACs and a standalone review/PR
boundary. Approval of a roadmap is not blanket permission to implement/release
all milestones. Use STANDARD for this milestone; keep its task/worktree/feedback
loop cohesive. New independently releasable milestones normally get their own
change/worktree, not one per worker or per day. If work depends on an unmerged
milestone, use an explicitly documented stacked base or wait; never guess origin/
main already contains it. Each release candidate must include its required safety
cases, not defer them to an optional future milestone.

End the session at the selected milestone's gate or a real blocker and checkpoint
what comes next. Continue another milestone only within explicit session scope.
Do not silently work through the whole initiative, create a swarm or auto-release.

## 6. Reclassify when evidence changes

Recheck classification when investigation finds a broader cause, a repair touches
shared behavior/data contracts, risk increases, or the same blocker stops making
progress. Do not keep expanding a QUICK_FIX to preserve its label. Announce the
new lane/risk and exact scope delta; preserve the existing valid worktree/context.
Do not create a fresh branch merely because a label changed.

If additional work changes owner-approved behavior, cost or risk, pause that work
for a decision card. Technical investigation within scope need not repeatedly ask
for approval. A later lower-risk classification may reduce ceremony with a recorded
reason, but cannot erase already-discovered mandatory requirements. Two attempts
without new useful evidence trigger workflow blocker triage, not a test-run quota.
A purposeful RED/GREEN iteration is progress, not a failed attempt.

A request that arrives mid-flight is routed, not argued. Same screen or module
and same deployment unit as the open change: add acceptance criteria to the open
record. A different deployment unit, or work that stands on its own: open a new
change and run it in parallel.

A pre-existing defect found while building is folded into the open change only
when that change makes the defect easier to hit; it then gets its own acceptance
criterion, a failing test first, and the owner's confirmation at the owner
check. Otherwise report it and open a separate change.

## 7. Routing, lifecycle and checkpoint contract

Use daily-workflow.md for model pools/delegation and dev-guardrails for method.
Load only the relevant phase/reference; do not load release material or the whole
project history for a quick correction. Do not send the entire router or lead
transcript to a worker when its bounded task/ACs and method references suffice.
Lanes do NOT map 1:1 to the three model tiers. Keep classification/delegation out
of the reusable dev skill and keep code review focused on evidence, not labels.

All lanes retain the reusable-test-environment policy, and every path except the
no-logic edit in 3a works in a dedicated worktree. Reuse
a safe existing environment when available. Data cleanup is separate from runtime
and volume retention; read release-setup and resource ledger before mutations.
Do not tear down shared test infrastructure or delete volumes to finish quickly.
Release remains a separately authorized release-housekeeping invocation.

Persist only: parent initiative if any; active change; lane/risk/uncertainty and
reason; approved scope source; selected milestone/task; actual worktree/candidate;
worker ID/route; evidence/finding pointers; phase/blocker; and one next action.
On resume validate actual state and continue; don't reclassify the entire project
or load unrelated history. No metrics/benchmark guarantees are implied by lanes.

Host invocation: Claude Code can use the supplied /dev command adapter. Codex uses
the supplied $dev adapter or its actual skill selector. A literal /dev in a custom
host requires a real configured binding, not a sentence claiming it exists.
