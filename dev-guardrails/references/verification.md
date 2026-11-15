# Pre-PR verification: reconcile the promise and the evidence

Contents: [Scope](#scope-and-provenance) | [Review](#perform-one-focused-review-pass) |
[Evidence](#choose-evidence-with-the-least-duplicate-work) | [Reviewer](#review-authorship-and-requirements) |
[Corrections](#findings-and-corrective-work) | [Gate](#evidence-ledger-and-gate) |
[Owner check](#owner-check)

## Scope and provenance

Verify the selected change against its approved spec, plus affected integration
and regression paths. Do not run reverify-project's whole-repository retrospective
pass. Reuse its principles: requirement authority, honest evidence labels, a
pinned target, disconfirming evidence, and targeted checks.

Pin the base revision and the candidate commit SHA on the change branch. The
candidate is a commit: review the diff from the base to that SHA. If the
worktree still holds uncommitted or untracked changes that belong to the
change, return it to be committed before verifying; do not verify a moving
working tree. List leftover files that are not part of the change instead of
reviewing them. Do not claim coverage of another developer's uninspected
changes or a deployment. If the candidate changes, recheck the diff between the
old and new SHA before making a final readiness claim. Record relevant config,
dependency/lockfile versions, fixtures and environment, without secrets.

## Perform one focused review pass

Start from the approved acceptance criteria, not just the changed files or test
names. Account for every in-scope criterion, including required failure paths.
Trace relevant production entry points, shared middleware, data constraints,
configuration, and callers to check the change is actually reachable and wired.

Check for omitted/partial/wrong behavior, unauthorized scope expansion, and
regressions caused by touched shared paths. Inspect assertions: a test that
only verifies a helper cannot establish that the real handler uses that helper.
Do not run a general code-smell or full-codebase cleanup campaign.

Search for contrary evidence before reporting a defect: another active route,
an existing shared guard, a database constraint, or an approved scope change may
invalidate the suspicion. A failed text search does not prove a feature absent.
Group findings with a shared root cause. Distinguish a confirmed bug from an
unverified concern, a spec ambiguity, and a risk without an approved requirement.

Review documented standards when material. Let existing automated formatting
and lint tools do mechanical checks; do not create a second standards-review team.

## Choose evidence with the least duplicate work

Reuse authentic test results for the exact relevant candidate, configuration,
test data, and dependencies. Record where they came from. A worker's `PASS`
sentence is not test evidence. Inspect the supporting output and test assertions.
A change to relevant code/tests/config invalidates that evidence. If unaffected
inputs cannot be established reliably, rerun the small affected check. Treat CI
results for another commit, an older test version, or a different configuration
as historical, not current proof.

Run missing focused checks. Use a UI/API smoke flow for user-visible wiring or
integration that lower-level tests do not demonstrate; do not launch a browser
for a pure backend change unless it answers a relevant uncertainty. Prefer safe
read-back through public interfaces for persisted effects. Keep customer data,
external emails, payments, and production mutations out of the test environment.

Honor every required repo check at the required stage. Run a small, fast full
suite once at the end when that is practical or prescribed. If broad tests are
expensive and policy allows them in CI, use focused local evidence and explicitly
list the mandatory CI checks still needed. Do not run the same broad suite both
locally and in CI just for reassurance, but never disable a required gate to
save tokens. Do not mislabel pending CI as passed or READY_FOR_PR as merge-ready.

One clear observation is sufficient for a deterministic targeted claim. Re-run
only for changed inputs, ambiguous/flaky output, or a concrete new hypothesis.
Concurrency and timing claims may need a controlled race test or repeated trials;
a single lucky run cannot prove them. Plan the smallest justified test and record
its limits. Do not impose a universal one-run rule on nondeterministic behavior.

For a change someone can see, look at the end state, not only the pass line:
main views the final screenshot of the flow. A value that must not change
(a unit, a quantity, a price) is asserted again after every step of the flow,
not once after the first step.

Checks the repository's own runbook requires before a deployment are run on
the candidate before READY_FOR_PR, with the raw output kept, not left as
"builder reported" until release time. Running a check needs no judgment: the
builder or a low-cost runner runs it and writes the raw output with the commit
SHA to a file; main reads the summary line and the failures, and does not
repeat a run whose inputs are unchanged. Whoever runs it records the exact
command of each piece of evidence, including environment variables, so anyone
can run it again.

## Review authorship and requirements

The external workflow assigns the reviewer. Record the author and reviewer,
whether they are different acting agents, and what context each received. A
fresh prompt to the same author is not independent review. A non-author lead
can supply a separate review perspective, but sharing design assumptions is
not a guarantee of independent judgment; actively seek contradictory evidence.

For high-risk changes (permissions, store/tenant isolation, financial/stock
integrity, destructive migrations, retries/concurrency or shared critical
paths), require a reviewer who did not author the relevant implementation.
For a low-risk change self-review may be sufficient, clearly labeled. If the
required review is unavailable, report the unmet requirement to the caller;
do not spawn an agent, choose a model, or silently waive the requirement.

Obtain approved spec, base/candidate, the risk question, relevant source and raw
evidence pointers. Treat the builder's conclusion as a claim to inspect. A
reviewer may request a focused check without repeating the entire test suite.
If the reviewer materially implements a high-risk repair, that repair still
needs a non-author review. The workflow arranges it.

## Findings and corrective work

For each finding give AC/source, expected vs actual behavior, impact, reachable
path, proof type (runtime or source), evidence pointer, and smallest correction.
A complete source proof may confirm a defect without an expensive end-to-end
reproducer. Lack of a runtime failure does not excuse a decisive source defect.
Do not certify required runtime behavior on source review alone.

In a verification assignment, report findings without product edits; let the
caller assign repairs. When explicitly assigned an in-scope repair, use the
same TDD rules and rerun affected checks. In verify-only mode, report and stop. Request approval for new product decisions or broadened scope. Keep known pre-existing failures
separate, with evidence; do not assert `pre-existing` without support.
Do not re-audit the whole repo after every correction. Reconcile the final diff,
revisit affected criteria, and preserve unchanged valid evidence. If a repair/
review loop produces no new information, report the unresolved blocker and evidence to the caller. Do not choose the escalation recipient.

## Evidence ledger and gate

For each criterion record ID, approved source, implementation pointer, boundary,
test/evidence pointer, target/config, actual result, and one status:

| Status | Meaning |
| --- | --- |
| VERIFIED | Executed evidence supports the stated scenario at its declared boundary; not universal correctness |
| NON_BEHAVIOR_CHECKED | An explicitly justified docs/config/static criterion was checked by the specified method |
| SUPPORTED_BY_CODE | Source suggests the behavior, but required execution evidence is absent |
| GAP_CONFIRMED | A runtime observation or decisive source proof contradicts the requirement |
| SUSPECTED_GAP | A concrete concern still lacks decisive evidence |
| NEEDS_SPEC_DECISION | Behavior or scope lacks an authoritative decision |
| BLOCKED | Environment, access, or a required prerequisite prevents verification |
| UNREVIEWED | No adequate review/evidence yet |
| EXCLUDED | Not applicable to this change, with actual approved scope authority |

Record mocks/limitations even for VERIFIED. Do not give an acceptance criterion
broader credit than the checked boundary supports. A simulated payment is not
proof that the live payment provider integration works.

READY_FOR_PR requires all in-scope criteria to have suitable VERIFIED or justified
NON_BEHAVIOR_CHECKED evidence, relevant local mandatory checks passed, required
independent review completed, the owner check recorded as OK for a change the
owner can see or use, and no unresolved material discrepancy. Record
nonblocking residual risks visibly. Unverified required behavior is not a pass.
An approved scope change may exclude an item; a risk note alone cannot delete it.
Use NEEDS_WORK for known deficits and BLOCKED for missing prerequisites/decisions.
Publishing a clearly labeled draft with gaps is separate, explicitly authorized
work. Never claim merge/deploy readiness from the pre-PR gate alone.

## Owner check

The owner does not read code, so agent evidence alone cannot tell them whether
the result is the product they asked for. After every in-scope criterion is
verified, and before reporting READY_FOR_PR, prepare an owner check for any
change the owner can see or use:

- Say in plain words, in the owner's language, what now works differently.
- Give a way to see the candidate running: a local or preview address and the
  exact steps to click through, using test data only.
- Attach screenshots or a short recording of each changed screen, taken from
  the candidate, covering the main path and one important failure case.
- List what the owner should look at and what is deliberately not included.

The owner answers OK or says what is wrong. Record an OK with its source;
silence is not an OK. A reported problem is a finding: classify it as a defect
against an existing criterion or as a new request that changes scope.

A change with no visible effect (an internal refactor, a backend-only rule)
gets the same plain summary with one observable before/after result and does
not wait for an answer. A no-logic edit needs only its before/after evidence
in the report.

Before inviting the owner, main walks the owner's own click path once (from the
real entry screen, not a test shortcut). The invitation states: the address,
the login name, where the password is found (never the password itself), the
steps in order, what each coloured or new area of the screen means, and the
decisions the owner is asked to confirm.

Owner feedback after the check is routed like a new request. A QUICK_FIX on the
same screen is done on the open branch before release. Anything larger: release
the current candidate if it is no worse than what runs today, and open a new
change for the rest.

## Workspace and release handoff

Verify the integrated candidate in the assigned change worktree, not whichever
checkout the terminal happened to open. Record its branch and absolute path.
Source tests and reviewed migrations are durable code, not disposable cleanup.
Return READY_FOR_PR with candidate/evidence/worktree/resource-ledger pointers;
release-housekeeping performs the separately authorized release. Its smoke checks
validate deployment, not a reason to repeat this entire pre-PR review.
