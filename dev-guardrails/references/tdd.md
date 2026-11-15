# Lean TDD: real feedback, not a test campaign

## Select observable boundaries

Use the project's existing test tools and documented commands. Test a public
behavior at a boundary that is stable and cheap enough for frequent feedback:
a domain operation, service/API boundary, or a browser flow when UI behavior is
itself the requirement. The agent proposes boundaries; the owner approves the
business scenarios and material coverage limits, not framework minutiae.

Prefer a real integration through the relevant production path. A small public
pure function can be the right boundary for complex calculations. Browser tests
are not mandatory for every rule; a pure unit test does not prove UI wiring,
authorization middleware, database concurrency, or a real external integration.
Choose additional evidence for those risks explicitly.

Derive expected values from approved scenarios, independently worked examples,
or a trusted external contract. Never copy the implementation's calculation into
the expected result. Do not assert only that the app starts or returns success
when the requirement concerns persisted data, access, or a side effect.

Mock unavailable external boundaries (payments, email, time) when necessary;
keep the business logic under test real. Prefer an isolated test database when
real storage constraints matter. Label what mocks cannot prove. Do not mock your
own core behavior into returning the expected answer. Read effects back through
public interfaces where practical. An explicit storage invariant may justify a
focused DB assertion; explain that exception instead of coupling every test to
private tables and call order.

## Execute a vertical RED -> GREEN cycle

For each behavior:
1. Pick the acceptance criterion and one scenario. Write its focused test first.
   When an existing test already fails on exactly the assigned bug, that test
   is the RED: record its failing line and go to step 3 without writing a copy.
2. Run that test and preserve the expected failure. Confirm failure is caused by
   the missing/wrong behavior, not missing credentials, a broken runner, or a typo.
   A valid unimplemented public interface can fail; a random compile error is
   not meaningful evidence about the acceptance criterion.
3. Implement the smallest coherent change that delivers this behavior on the real
   path. Do not hardcode examples or add future features to satisfy the test.
4. Rerun the focused test and observe GREEN. Inspect assertions and relevant side
   effects. Run nearby affected tests when the change could invalidate them.
5. Record the result, then select the next behavior. Do not batch all tests first.

When a task's behaviors are GREEN, commit them on the change branch with the
task and AC IDs in the message. Stage exact files; keep secrets, local
environment files and generated junk out. A local commit is private and can be
undone; pushing is not part of development. Repairs after review are new
commits, so the reviewer can compare two SHAs; do not amend or rebase commits
that were already reviewed.

Keep required negative/security cases in the same delivery scope. A working happy
path alone is not completion. Do not move required integrity checks to a later
unapproved release just because smaller tasks are easier.

Do not rewrite correct expected behavior to get GREEN. A genuinely wrong test
may be corrected with a recorded reason grounded in the approved spec; changing
the product contract needs owner approval. Do not delete, skip, broaden, or mock
away failing assertions without a justified, visible reason.

For a bug fix, first reproduce the bug in a regression test when feasible. For
existing behavior that already passes, record characterization/verification;
do not deliberately break the product or pretend it was developed test-first.
If a test cannot express the behavior, agree a minimal alternative evidence plan.
Docs-only/cosmetic changes may justify non-TDD checks, recorded before editing.
Visual-only claims require visual evidence when automated checks cannot prove them.

## Keep test effort proportionate

Plan a small set of representative approved behaviors, not a fixed coverage
percentage or every imaginable edge case. Choose high-impact failure cases from
actual requirements and reachable code paths. Never drop a required risk check
merely to meet a numeric test limit.

Run focused commands in bounded non-watch mode and capture concise output. Use
one result for multiple ACs only if its assertions actually support each one.
Distinguish runtime/compute cost from LLM tokens; repeated log/context ingestion
and agent calls add model work, but test-case count is not a token meter.
Do not impose a universal command-count limit: meaningful RED/GREEN cycles
are necessary. Honor the actual caller budget and disclose any unfinished work.

Do not perform broad refactors during the loop. At review, make only justified
local cleanup within approved scope and rerun affected checks. Larger cleanup is
separate work. The inspected Matt TDD skill places refactoring in review; this
workflow also does not require refactoring after every GREEN.

When stuck or reaching the caller's stop condition, stop random edits and return
a blocker with evidence, attempted hypotheses and what is needed next. Expected
RED followed by an informed implementation is progress, not a failed retry.
If the runner/environment is unavailable, record BLOCKED; do not label
unexecuted tests as TDD or install new infrastructure silently.
