# Owner-friendly discovery

## First obtain facts yourself

Inspect the relevant code, existing workflows, approved specs, and current test
setup. Use bounded searches with the available tools. Report an unavailable
capability to the caller instead of arranging delegation yourself. Mark inaccessible information honestly. Do not ask the
owner to explain their own code or repeat a settled decision.

Distinguish three kinds of questions:

| Kind | Who handles it |
| --- | --- |
| Product policy: who may act, expected outcome, limits, priorities | Owner decides, with your recommendation |
| Consequential architecture: offline behavior, data ownership, reliability, costs, reversibility | Agent translates options into consequences; owner approves the material tradeoff |
| Implementation detail: function names, indexes, internal interfaces, test tools | Agent follows repo conventions and explains only when consequential |

Do not present a data-security baseline as an optional inconvenience to remove.
For example, investigate how to enforce isolation; ask who is authorized, not
whether it is acceptable to omit authorization checks to save development time.

## Use one decision card per consequential question

Write the card in the owner's conversational language:

1. **Decision and context:** explain the user situation and what current evidence
   establishes; separate assumptions. Explain unfamiliar terms in plain language.
2. **Options:** give two or three realistic choices and concrete behavior for each.
3. **Tradeoffs:** state what improves and what gets harder: workflow disruption,
   maintenance, cost, latency, data integrity, reversibility, and what is deferred.
   Do not invent numerical costs, reliability, or delivery-time estimates.
4. **Risks:** explain important failure modes and mitigations; do not bury caveats.
5. **Recommendation:** recommend one choice based on the stated needs, with a
   reason and the circumstance that would make a different option preferable.
6. **Decision request:** ask a clear business question; allow an alternative.

Offer at most three independent cards per round. A question dependent on an
unanswered choice waits for the next round. Do not use leading wording that
hides costs or pretends there is no legitimate alternative.

State current behavior only with a source. Every sentence in a decision card or
proposal that describes what the system does today carries its evidence: a
`file:line`, or the command that was run and what it printed. If it was not
checked, write "not checked" instead of a confident sentence. The owner decides
from these sentences; a wrong one produces a wrong decision that surfaces tasks
later.

## Example: unstable store internet

Do not ask: "Should we implement optimistic replication with an outbox?"
Ask about whether a staff member may keep entering a goods receipt while offline.
Explain the difference between (A) blocking submission until connection returns,
(B) storing an explicitly unsent draft without updating stock, and (C) accepting
real offline transactions and reconciling later. Explain that C also needs rules
for conflicting edits, duplicate submission, and what counts as accepted.
Recommend the simplest option meeting the owner's actual continuity needs.
State whether device-local drafts can be lost or accessed on a shared device;
do not invent secure persistence that has not been designed.

Translate the chosen behavior into implementation decisions yourself. Record a
short rationale so the next worker does not reopen the choice or silently alter it.

## Avoid interview overhead

A precise bug report or approved spec may need no interview. For a tiny change,
one short paragraph can contain the whole decision card. Do not generate a long
requirements questionnaire, glossary, or ADR library by default. Introduce a
shared domain term or a durable architectural decision only when it resolves real
ambiguity. Capture it in existing repo docs when available.

Review proposed acceptance criteria with the owner once as observable scenarios,
not as internal API boundaries. They approve what must work and the important
risks left out; the agent selects the technical seams and tools. Reopen approval
only when a discovery changes scope, cost, data handling, or expected behavior.

Record unresolved low-risk implementation assumptions transparently. Do not let
an assumption settle a material product policy without authorization. Stop when
key outcomes, failure behavior, scope, and success criteria are clear enough to
implement; park unrelated future ideas under non-goals.
