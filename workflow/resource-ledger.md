# Resource ledger: <change-id>

Instantiate only real resources in durable runtime state OUTSIDE retiring
worktrees. Do not inventory the whole host. Unknown identity means retain/report.

Repo/origin / main worktree / common Git directory:
Change worktree / branch / base / actual writer(s):
System/skill source path/version / evidence archive and retention authority:

## Environment and logical data
Environment identity / lifecycle / active users:
Policy: DATA_ONLY / CONTAINERS_KEEP_VOLUMES / scoped disposable runtime / UNKNOWN.
Non-production endpoint and exact run/tenant/record/object boundary:
Reviewed data-cleanup recipe / effect preview / baseline validation:
Schema, migration history, seeds and baseline accounts that MUST remain:
Stable startup recipe/config/secret-store references OUTSIDE retiring worktrees:
Exact existing volume IDs/mounts/bind paths needed on reuse:
Readiness: INSPECTED_ONLY / EXERCISED / BLOCKED, with actual evidence.

## Physical resources (separate policies, not a single disposable flag)
| Exact ID/path | Host/context/project | Ownership and current consumers | Data policy | Runtime action | Storage/config retention | Authority and dependencies | Outcome/evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <actual only> | <verified> | <current proof> | <scoped cleanup/retain> | <keep/stop/remove> | KEEP by default | <source; recreation checks> | ACTIVE |

Record source worktrees/branches, ports/processes, run-data, Compose inputs,
containers/networks, volume IDs/bind paths and image/cache references as relevant.
No source tests/fixtures/migrations are disposable. Record outcomes as DATA_CLEANED,
REMOVED, RETAINED_BY_POLICY, BLOCKED, NOT_IN_SCOPE or NOT_APPLICABLE. Expected
retention is success, not cleanup pending. A required unsafe cleanup remains
BLOCKED. Archive evidence before removal and report only measured disk/RAM changes.
