# Change: <business outcome>

Use only needed sections; prefer existing repo records. Placeholders are not
approval or execution evidence. Assignment metadata is maintained by the workflow.

## Scope and authority
Goal / users:
Non-goals:
Approved source/revision and actual approval pointer:
Allowed build/test/external actions and boundaries:
Accepted decisions, reasons and material residual risks:
Unresolved decisions / assumptions:

## Contract and evidence
| ID | Observable outcome / independent expected result | Required failure case | Method / evidence / candidate | Status |
| --- | --- | --- | --- | --- |
| AC-01 | <outcome> | <case or justified N/A> | <not yet collected> | UNREVIEWED |

Owner-facing test proposal / what is not established:
Agent-owned implementation notes (not authority to change the contract):

## Vertical tasks
| ID | Outcome / AC IDs | Blocked by | Complexity / risk | Status |
| --- | --- | --- | --- | --- |
| T1 | <one result> | <real blockers or none> | <why> | PLANNED |

## Evidence ledger
Repo/workspace, base SHA, candidate commit SHA:
Safe environment, config, dependencies and fixtures (no secrets):

| Task / AC | RED / GREEN / CHECK | Exact command + directory | Actual exit/result + counts/skips | Evidence pointer / target |
| --- | --- | --- | --- | --- |
| <ID> | <stage> | <command actually executed> | <actual> | <log or artifact> |

Reused evidence and why still applicable:
Mocks, limitations, stale results and checks not run:

## Review / repairs
Reviewer, authorship and self/non-author status:
| Finding | AC / source | Expected vs actual / proof | Impact | Repair objective | Status / resolution evidence |
| --- | --- | --- | --- | --- | --- |
| F-01 | <ID> | <path + proof> | <impact> | <minimum fix> | <open/resolved/needs decision> |

Final candidate / affected ACs rechecked:
Owner check: what was shown, the owner's answer and its source (or not applicable and why):
Local mandatory gates:
Later CI requirements (not yet passed):
Outcome: <READY_FOR_REVIEW / READY_FOR_PR / NEEDS_WORK / BLOCKED>
Next action and required authority:

## Session checkpoint (maintained only when needed by the workflow)
Current phase/task; actual worker/session ID or none:
Files/workspaces owned; unrelated changes to preserve:
Facts learned, failed hypotheses, evidence pointers:
Concrete next action; blocker; stop conditions:

## Workspace and resource pointers
Primary/main worktree and common Git identity:
Change worktree absolute path / branch / fetched base SHA:
Durable runtime checkpoint and resource-ledger location (outside retiring tree):
Isolated test endpoints / Docker context and project (no secrets):
Release handoff: candidate, evidence, migration proposal, affected deploy components:

## Optional workflow classification (filled by the lead, not the skill)
Lane / risk / uncertainty / concise evidence:
Parent initiative / selected milestone and current session boundary:
Approval source (including clear direct repair instruction when applicable):
Classification change and scope delta, if any:
For a tiny change keep only applicable fields; this is not a required full form.
