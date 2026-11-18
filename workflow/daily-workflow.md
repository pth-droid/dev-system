# Daily Development Workflow

Version: 4.1 / 2026-11-14. This file is an instruction runbook for the lead agent,
NOT another skill, an executable dispatcher, or a scheduled automation.
Read it at session entry or when orchestration policy changes. Workers receive
only their assignment and relevant skill sections, not the whole lead history.

## Entry: one /dev workflow, three proportional lanes

Start with [dev-router.md](dev-router.md): resolve intent/checkpoint, inspect only
relevant context, choose QUICK_FIX / STANDARD / LARGE independently of risk and
model tier, and state the current session scope. A no-logic QUICK_FIX edit
(wording, docs, spacing) is handled entirely by dev-router.md section 3a and
needs nothing from this file. For any other QUICK_FIX the micro-contract path
replaces unnecessary discovery/full planning below; it does not waive tests,
review, worktrees or authority. For LARGE these steps apply to ONE selected
approved milestone, not the whole initiative. Do not restart this router for each
builder feedback round. Native invocation varies by host; verify its adapter.

## 1. The operating model

- Lead/main: Tier 1, normally High. Own owner-facing decisions, scope, assignment,
  spec-first review, final local gate and a small persistent checkpoint.
- Builder: one existing Tier 3 or Tier 2 worker as the task requires. Own TDD,
  implementation, ordinary test failures, in-scope repairs and execution evidence.
- Extra verifier: absent by default. Add one only for a clear need: the lead
  authored high-risk implementation, separate specialist tools are needed, or a
  bounded high-volume verification job is cheaper to isolate.
- Scripts/CI: perform mechanical checks using existing project tooling. An LLM
  need not narrate every command or ingest every passing test log.

Use one code writer per worktree and no review swarm, model contest, nested
worker delegation or mandatory tier ladder. The lead stays read/review-oriented
while a builder writes. Do not start concurrent writers in the same workspace.

Run changes in parallel when they do not affect each other; this needs no
separate owner approval. Changes are independent when they touch different
files or modules, write to no shared test database, container or port, have no
ordering dependency and share no deploy step. Give each parallel change its own
worktree, branch, builder and test data, and tell the owner which changes run
in parallel and why. If any condition fails or cannot be established, run the
changes one after another and say why. When parallel changes must ship
together, verify the integrated candidate, not each branch alone.

The skill defines HOW to develop; this workflow defines WHO does what and WHEN;
the runtime actually launches tools/models. Do not claim the runtime did an
operation merely because this document requested it.

Shared log files collide when changes run in parallel. Reserve the decision or
ticket number when the change is opened. A shared progress or log file is
written by main only, once, right before the PR and after merging the current
main into the branch; builders do not edit it.

## 2. The user's three resource pools

These are user-provided preference labels, NOT verified provider IDs, rankings,
prices, supported effort enums, or a promise of model availability.

| Pool | User-provided labels | Use |
| --- | --- | --- |
| Tier 1 | Opus High; Opus xHigh | Lead, consequential design, deep investigation, difficult final judgment |
| Tier 2 | Opus Medium; Sonnet Xhigh; Sol 6.2 Extra High | Difficult implementation or a bounded quick investigation |
| Tier 3 | Sonnet High; Sol 6.2 High; Sol 6.2 Medium; Terra 6.1 xHigh; Deepseek 4.1 Flash High; GLM 5.3 Flash Max | Clear, routine implementation and deterministic check execution |

Do not hardcode labels into API/CLI arguments. Resolve actual model IDs, effort
support, permitted tools and cost constraints from the installed host once in
[project-setup.md](project-setup.md). Record the real selected settings when the
host exposes them; otherwise write UNKNOWN. A label alone changes nothing.

Use Tier 3 for a well-specified task in known code patterns; Tier 2 for a concrete
but difficult build or narrow investigation. Use Tier 1 for material ambiguity,
cross-module decisions or high-consequence reasoning. Risk and complexity are
separate: a small permission edit can still need careful non-author review.
Do not switch providers to save money without considering re-reading context,
failed attempts and the owner's allowed pool. No automatic fallback outside it.

A list price holds only for a short context. Some models charge more once a
request passes a context threshold, and a long-running agent sits above it on
almost every request. Pick the model for a role by the context that role will
reach, not only by difficulty, and record the thresholds in project-setup.md.

## 3. One-time project bootstrap

Read repo instructions, existing specs, package manifests, scripts, test and CI
configuration. Discover technical facts yourself. Complete the small setup record
using actual evidence: skill path, source of truth, safe test environment,
commands, runtime capabilities, available worker profiles and action permissions.
Do not ask the owner to supply build commands that the repo already documents.

Ask only material product/cost/security choices or missing authorization, with
context, options, tradeoffs, risks and a reasoned recommendation. Never invent
credentials or assume test data is safe just from a variable name.

Use tools already installed. Do not install a dispatcher, new paid service,
agent plugin, CI integration or dependency without applicable authorization.
If the host cannot launch the preferred worker/model, report the capability gap
once. Use a supported authorized route or a manual handoff. Low-risk work can
continue as explicitly labeled single-agent work if permitted; high-risk
independent-review requirements remain unmet until a non-author reviews.

## 3a. Provision the change workspace before development

Follow [worktree-lifecycle.md](worktree-lifecycle.md). At the first write for a new
change, provision one dedicated registered worktree on its owned non-main branch,
from an inspected fetched base. On resume validate and reuse the SAME worktree.
The only exception is the no-logic edit in dev-router.md section 3a.
Do not create a new worktree every day, per tier, or per feedback round.

All builders, review commands and fixes use that exact path. Read-only discovery
may start in the primary checkout. Do not edit product code, tests or the change's
repo documents directly on local main. If worktree creation is unavailable, report
BLOCKED rather than silently using the original checkout. Never carry uncommitted
primary-worktree changes across without an explicit scoped transfer decision.

Record the workspace, base, canonical installed skill/workflow paths and resource
ledger. Reuse an approved existing test environment when it can safely isolate this
run's data; allocate new ports/projects only where needed. Worktree separation
alone is insufficient. Record DATA_ONLY / CONTAINERS_KEEP_VOLUMES / disposable
runtime policy, exact storage identities, data boundary and restart recipe in
release-setup/resource ledger. Preserve runtime state outside retiring trees.

The task table says where each task's evidence runs. If a task needs an
environment that is not running (a test stack for the change's worktree, a
fixture, a service), provision and smoke-test it before dispatching the first
task, and note setup steps that a fresh environment lacks compared with the
real one.

## 4. Start or resume the daily session

Read project-setup.md, the active change record and its latest checkpoint, then
verify current branch, workspace, dirty/untracked state and actual worker status.
Do not assume yesterday's worker is running or that its patch is integrated.
Do not restart interviews, plans or reviews just because the calendar changed.

Choose the current approved change/session milestone under dev-router.md, or ask
one priority question if no priority exists. Select one task whose dependencies are done. Briefly state current phase,
task, assignment and the next useful step. Do not silently work through an entire
backlog or the old reverify-project report.

Prefer continuing the useful current session. When a fresh session is needed,
load a compact checkpoint plus pointers, not the entire prior conversation.

## 5. Plan only when needed

Use dev-guardrails discovery/planning sections. Investigate facts, explain only
consequential owner decisions, record compact ACs and vertical tasks, and obtain
one combined approval unless equivalent scope/authority already exists.

Assign an appropriate worker in this workflow, not in the skill. Start directly
at BUILDING for an approved task or VERIFYING for a verify-only request. Keep
unresolved material decisions out of implementation.

State progression (skip already-satisfied gates, never their evidence):
TRIAGE -> DISCOVERY -> AWAITING_APPROVAL -> WORKSPACE_READY -> READY_TO_BUILD -> BUILDING
-> READY_FOR_REVIEW -> VERIFYING -> OWNER_CHECK -> READY_FOR_PR

OWNER_CHECK applies to changes the owner can see or use (section 11); other
changes go from VERIFYING straight to READY_FOR_PR. A verified defect follows VERIFYING -> NEEDS_WORK -> FIXING -> READY_FOR_REVIEW
-> VERIFYING. BLOCKED is a side state: preserve the suspended phase and reason.
Never upgrade a state merely because the time/token budget ended.

## 6. Dispatch one bounded assignment

For a trivial low-risk change where delegation adds more overhead than work,
main may implement and self-review within authority; label it honestly. Do not
apply that exception to high-risk paths requiring non-author review.

Use the same builder for a coherent task and its fixes when context remains
useful. Resume its actual session/agent ID if supported; otherwise use a handoff.
Do not claim context continuity that the runtime does not provide.

Send the worker:
- Task ID, outcome, approved spec/revision and relevant AC IDs.
- Absolute assigned worktree, branch, repo/common Git identity, base/candidate,
  canonical skill path, resource-ledger path, owned scope and unrelated edits.
- Confirm the worker will actually run tools with that working directory and safe
  test environment, not the primary checkout or a previous session's CWD.
- Installed dev-guardrails path; instruct it to read SKILL.md and the relevant
  TDD/planning sections. Do not assume it inherited skill contents.
- Required behavior and failure cases, safe checks, authority and non-goals.
- Commit rule: commit each completed task on the assigned branch, staging exact
  files. No commits on main, no push, no amend or rebase of reviewed commits.
- Return format: READY_FOR_REVIEW or BLOCKED; candidate commit SHA, changed files, AC results,
  exact commands/results, evidence pointers, limitations, next useful question.

Do not send a confident implementation narrative as the only source of truth.
Give source pointers; let the worker read the actual contract and relevant code.
Keep raw logs in accessible files. If files are not shared, transfer through an
actual supported channel and record patch/commit provenance.

## 7. Keep the ordinary development loop local to the builder

Builder uses incremental TDD, commits each completed task on the change branch
and fixes routine in-scope failures before asking for review. Do not wake the lead for every RED, type error or unambiguous test
failure. Do not create a separate test-writing agent for each slice.

Use focused checks during development, plus project-required checks at their
specified stage. No universal six-command or one-test-run budget applies. Store
full evidence locally; send concise summaries including failure/skip counts,
exit status and artifact pointers. A small fast suite may be better than many
agent turns selecting individual tests. Never hide failed or skipped checks.

The lead does not read the worker's entire transcript or continuously poll it.
Use supported completion events/status tools; if manual, resume when its result
is supplied. No implied background/scheduled work is created by this runbook,
except the owner-enabled keep-warm wake-up in section 7a.

## 7a. Keep the lead session warm while it waits (owner-enabled)

This is an owner instruction, not a host default. On a host whose prompt cache
expires (about one hour in Claude Code), a lead that resumes after the expiry
writes its whole context again at the full write price; one request before the
expiry costs a cache read, a small fraction of that. It applies only when
project-setup.md records keep-warm as enabled or the owner turns it on, and the
host has a wake-up tool. Otherwise skip this section.

When the lead ends a turn to wait, it arms ONE wake-up shortly before the cache
expires (50 minutes in Claude Code), and each wake-up arms the next one. This
fixed cadence keeps any two requests closer together than the cache lifetime,
so real turns in between need no re-arming. Never keep two wake-ups.

A wake-up is also the progress check. Do exactly this, then stop:
- Read the cheap signals of work in flight: the builder's newest commit, the
  last lines of its log or report file, the host's status of the agent. Never
  read its transcript.
- Send the checks and the next wake-up in one message, then answer in one line
  (time, what was checked, what changed). Every extra request and every word
  written here is read again on all later steps.
- Act only when the work finished (start the review), stood still across two
  consecutive checks or asked a question (report it, stop watching), or a usage
  limit was hit (save state, section 10).

What ends keep-warm depends on what the lead waits for. Do not count wake-ups.

| Waiting for | Keep warm until |
| --- | --- |
| A builder or runner in flight | It finishes, stands still across two checks, or the watch ceiling passes (default 5 hours). Quiet hours do not end this. |
| The owner | Quiet hours begin (default 23:00-07:00 local), or the owner turns it off. |

It also ends when the change is released or the session is about to be replaced
by a new one.

The owner controls it in plain words, in any language, or with the host's short
command when one is installed:
- on: "keep warm", "keep the session warm", "bật giữ ấm";
- off: "stop keep-warm", "stop warming", "let it go cold", "tắt giữ ấm";
- until a time: "keep warm until 22:00", "giữ ấm tới 22:00";
- status: "is keep-warm on?", "giữ ấm đang bật không?".

An override lasts for the session. A bare "stop", "pause" or "nghỉ" is not a
keep-warm command; ask when unsure. Say in one line every time the state
changes and why ("keep-warm on until 23:00", "keep-warm off: builder finished").

Changing the model or the effort level in the middle of a lead session starts
the cache over (on the Claude API either one does), so do not change them for
no reason, and keep the wake-up prompt to one short line. Saving the cache is
never a reason to keep an unsuitable model or effort: when the work needs more
capability, quality comes first; switch now, or at a session boundary if the
change can wait without harming the result. Keep-warm also never outranks a
stop instruction from the owner.

## 8. Main performs the default post-development review

Receive one candidate with evidence. The Tier 1 main uses dev-guardrails
verification.md to reconcile EVERY in-scope AC, inspect material code paths and
assertions, check provenance and review relevant standards/risk.

If main did not write the implementation, it can provide the non-author review;
no third agent is needed merely to rename this role. Shared design assumptions
still need critical examination. If main materially authored a high-risk path,
assign ONE suitable non-author reviewer. That reviewer need not be Tier 3.

Reuse authentic evidence whose relevant inputs remain unchanged. Request a
missing focused check from the same builder or an existing runner. Main may run
a short decisive check itself if doing so is simpler; avoid relaying tiny tasks.
Do not rerun all tests, all browsers, or the full retrospective audit for comfort.
Do not accept a PASS sentence without underlying evidence and assertions.

Batch findings into one review packet: F-ID, AC/source, expected/actual, path,
proof, impact, correction objective, and whether blocking. Group one root cause.
Keep unsupported suggestions separate from actual failures. Stop/reject
immediately for a serious safety issue rather than waiting to finish the batch.

## 9. Feedback -> fix -> delta recheck

This loop applies only to authorized build/repair work. A verify-only request
ends after reporting findings; do not dispatch a fixer until repair is authorized.

Return the packet to the original builder, not a newly initialized fixer.
Builder repairs approved defects with TDD as new commits and returns
finding-by-finding resolution, the new candidate SHA and affected evidence, so
main rechecks only the diff between the two SHAs. Do not silently change accepted product
behavior. Send disputed requirements back as a decision, not a guessing contest.

Main rechecks the findings, repair diff and affected transitive dependencies.
Reopen an earlier conclusion only when the repair or new evidence invalidates
it. Reuse still-applicable evidence. After integration, use the actual combined
candidate, not separate worker branches, for the final gate.

Do not let a third verifier become a permanent feedback relay. Add one only for
the bounded need in section 1; let it preserve context through rechecks. Main
assesses its scope/evidence and unresolved risk rather than repeating its entire
job. A verifier that repairs product code is an author of those repairs; record
that and satisfy non-author review where required.

Main may make a micro-fix itself instead of another builder round when the
change is about five lines or fewer, involves no new behavior decision, and
main re-runs the related check (including a syntax check) afterwards. The
report says main made it. Anything larger goes back to the same builder.

## 10. Stop unproductive loops and route the actual blocker

Proposed default: after TWO attempts on the SAME blocker with no new useful
evidence, pause and triage. This is not two test runs, two expected REDs, or two
productive fixes. Record attempts rather than guessing at a counter.

| Blocker | Action |
| --- | --- |
| Product rule/spec ambiguity | Main explains decision and asks owner; no model escalation solves missing authority |
| Missing data, credentials, environment or permission | Resolve capability/authorization; do not retry smarter models blindly |
| Task too broad / dependency missing | Re-scope or reorder within approval, otherwise seek approval |
| Clear but hard technical build | Give a bounded problem to Tier 2 if useful |
| Deep cross-module uncertainty or two unproductive repairs | Main Tier 1 investigates, using stronger configured effort only if justified |
| Provider unavailable or exhausted allowance | Save state; use only an authorized supported alternative, or BLOCKED |

Do not force Tier 3 -> Tier 2 -> Tier 1 for every issue. The main can solve a
specific reasoning question and return a concrete constraint to the same builder.
After a directed repair that still provides no progress, preserve BLOCKED and a
next diagnostic/decision; do not silently start an unbounded repair swarm.

## 11. Owner check, final gate and explicit release handoff

When verification passes for a change the owner can see or use, main prepares
the owner check described in the dev-guardrails verification.md: a plain summary,
steps to see the candidate running, and screenshots of the changed screens.
The change stays in OWNER_CHECK until the owner answers. The owner's OK moves it
to READY_FOR_PR; a reported problem returns it to NEEDS_WORK or to a scope
decision. Silence is not an OK. Independent work may continue meanwhile under
section 1.

Main reports READY_FOR_PR, NEEDS_WORK or BLOCKED under the dev skill's evidence
rules. Local commits on the change branch are part of building. READY_FOR_PR is
not permission to push, publish, merge, migrate, deploy or delete.
Prepare one release handoff: approved change/spec, reviewed candidate, evidence,
worktree/branch, affected components/migration proposal and resource ledger.
Keep the same context; don't redo discovery or the whole verification pass.

When the user requests a release or standing release authority applies, follow
[release-workflow.md](release-workflow.md) and the separately installed
release-housekeeping skill. A PR-only request may stop after publication; do not
widen it to deployment. Release planning must inspect automatic push/merge deploy
triggers BEFORE those actions. Unknown authority stays blocked/plan-only.

Do not remove worktrees, branches or test resources just because READY_FOR_PR was
reached. Keep the complete lifecycle bound to this change's exact recorded IDs.

## 12. End the session / start tomorrow

Update the existing durable runtime checkpoint OUTSIDE retiring worktrees, linking
the SAME change record rather than making a new document. Preserve current
phase/task, approved decisions,
actual workspace/candidate, worker identity or manual route, unresolved findings,
commands/evidence, stale results, blocker and one concrete next action. Redact
secrets. Do not manufacture a daily duplicate spec or huge transcript summary.
Commit unfinished work on the change branch with a `wip:` message, so the next
session resumes from a commit SHA and nothing lives only in the working tree.

State what is done, what is not verified, and what must happen next. Do not leave
shared UI/DB sessions or writing agents running unintentionally. Stop only
resources you own when safe; never kill unknown processes. Report any known
running work honestly. On resume, validate these facts before continuing.

When the session is left to go cold (night, between changes, keep-warm off),
bring the change record up to date first. The next day, prefer a new session
that starts from the record when the old context is large: a new session writes
only its fixed overhead, a resumed one writes its whole context again.
Compacting lowers that cost only while the cache is still warm; the compacted
context is itself written anew on the next request and grows again with review.

## 13. Observe cost without inventing a benchmark

When the host exposes them, record per-task model/effort, uncached/cache/output
usage (including reasoning according to the provider), cost or subscription
usage, number of repair rounds and defects discovered after readiness. Otherwise
mark usage unavailable. Do not convert labels, log size or test count to dollars.

Optimize completed, verified outcomes rather than cheapest token price. Start
with the main-review/same-builder-fix design; change it based on your own traces.
Prompt caching and cheaper models are not a guarantee of lower total usage.

## 14. Owner status report

The owner is often away for long stretches and catches up without rereading the
conversation. Every report to the owner covers every change this session runs,
not only the one that just moved. Put decisions that block progress first. For
each change give a short block in the owner's language:

- What it is: one plain sentence on the goal and why the owner asked for it.
- Where it stands: state, commit or PR, deploy state, what was verified and
  what was not.
- Decisions taken: what was chosen, what was given up, and who decided.
- What the owner must decide or do: each open question with its options and a
  recommendation, marked when it blocks progress.
- Links: change record, PR and key document.

A change that has passed its whole finish line (merged, deployed and migrated
where applicable, housekeeping complete) is reported as DONE once, in one line
with its PR and what was verified, then left out of later reports.

Open the report with the decisions waiting for the owner. Each has an id, the
date it was asked and a recommendation. Whether main may continue on its own
default depends on who owns the choice, not on whether the code can be undone:

| The open decision is | Main does |
| --- | --- |
| A low-risk implementation detail inside the approved scope | Continues on the more cautious default, marked "running on the default, can be changed" |
| Covered by a fallback the owner approved in advance | Continues on that fallback and names the approval |
| About money, access, data integrity, product policy, an outside effect or material scope | Marks it "recommended, waiting for approval" and continues only the work that does not depend on it |

Reverting code does not revert its effects: a rounding rule, a refund
condition or a permission already applied to real records stays applied.
Silence is never consent to the third row.

## Files used by this workflow

- [project-setup.md](project-setup.md): fill technical facts once, maintain on change.
- [prompts.md](prompts.md): owner-facing start/resume/verify/wrap-up prompts.
- [repo-instructions.md](repo-instructions.md): optional small repo instruction block.
- Installed dev-guardrails: method, templates and phase-specific references.

These files do not launch agents, enforce budgets, automatically schedule daily
runs or bypass host restrictions. Actual orchestration uses your configured host.

## Lifecycle companions

- [worktree-lifecycle.md](worktree-lifecycle.md): provision/resume the isolated
  change workspace and resource ledger. It is not a separate skill.
- [release-workflow.md](release-workflow.md): orchestrate the separately authorized
  PR/merge/deploy/migration/sync/retirement phase without a new swarm.
- [release-setup.md](release-setup.md): verified project-specific targets, commands,
  trigger behavior and cleanup policy, not executable configuration.
- [resource-ledger.md](resource-ledger.md): a small template instantiated in the
  configured durable runtime state root; don't load it unless allocating resources.
