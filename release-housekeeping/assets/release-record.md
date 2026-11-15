# Release record: <change-id>

Store in durable authorized state outside retiring worktrees. Reuse existing
release records by pointer. UNKNOWN / NOT RUN / NOT APPLICABLE are distinct.

## Authority and identity
Mode / requested scope / actual permission source:
Origin repository identity / target branch / primary and main worktree:
Change worktree / branch / original reviewed candidate / PR head SHA:
Spec + READY_FOR_PR evidence / CI + required reviews:
PR URL / mergedAt / actual merged SHA:
Deployment triggers on push/merge / executor for each action:

## Plan and results
| Component/environment | Previous artifact | Intended artifact | Impact/reason | Executor/command pointer | Status + evidence |
| --- | --- | --- | --- | --- | --- |
| <component> | <actual> | <pinned> | <why or NO_DEPLOY> | <actual repo mechanism> | NOT RUN |

| Migration ID/checksum | Target database identity (no secrets) | Applied history | Order/compatibility | Recovery prerequisite | Actual result |
| --- | --- | --- | --- | --- | --- |
| <ID or N/A> | <environment> | <evidence> | <expand/backfill/contract> | <verified plan> | NOT RUN |

Smoke / artifact identity / observation results:
Failures / partial application / rollback or roll-forward action:
Local main before / fetched origin/main / local main after / timestamp:

## Resource retirement
Archive/evidence root outside worktree:
| Exact path/ID | Host/context/project | Ownership/proof | Disposable + approval | Retention/consumers | Removed/retained + result |
| --- | --- | --- | --- | --- | --- |
| <resource> | <identity> | <ledger proof> | <yes/no + source> | <reason> | NOT RUN |

Disk before/after (same host/scope, observed, not guessed):
Owned workload RAM before/after / host RAM if available / attribution limits:
Protected tests/fixtures/migrations / backups / retained shared resources:

## Resume checkpoint and final result
Per-stage actual statuses (publication / merge / deploy / migration / smoke / sync / cleanup):
Outcome:
Next concrete action and unmet authority/prerequisite:

## Test environment preservation
Lifecycle / policy / exact run-data selector / reviewed cleanup recipe:
Data cleanup outcome and baseline/schema/seed validation:
Eligible containers removed or shared services intentionally retained:
Retained exact volume IDs, durable bind/config/image references:
Surviving startup/reattachment recipe and readiness evidence:
Each resource: REMOVED / DATA_CLEANED / RETAINED_BY_POLICY / BLOCKED / NOT_IN_SCOPE.
Do not mark expected retained assets as unfinished housekeeping.
