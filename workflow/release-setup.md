# Release setup - discover once, update changed facts

A factual runbook record, NOT an executable config or authorization by itself.
Use actual repo tools; UNKNOWN is not permission or a value to guess.
Store secrets only in existing approved stores; record references, not values.

## Repository and authority
Canonical origin URL / host / owner/repo:
Target remote branch (expected origin/main) / main worktree:
Actual merge method / required reviews / CI / queue:
Push, PR, merge, deploy, migration, local cleanup authorization and source:
Approved environments / production boundaries / synthetic smoke data:
Remote branch deletion policy (separate from local branch retirement):
Exact-branch squash/rebase cleanup exception authorized? Scope/source or NO:

## Automatic side effects BEFORE publication
What push / PR / merge triggers deploys, previews or migrations?
Who owns each action (CI / platform / manual)?
How to query job completion, artifact identity and applied migration history?
How to prevent duplicate manual runs / concurrent releases?

## Deploy only the required unit
| Component + environment | Current artifact query | Deploy/observe command + CWD | Dependencies/shared inputs | Smoke/version proof | Rollback/roll-forward |
| --- | --- | --- | --- | --- | --- |
| <discover> | <actual tool> | <actual repo mechanism> | <actual> | <actual> | <verified> |

## Database / data changes
Migration tool and production-safe command (never dev reset/sync shortcut):
Migration history/checksum query / lock and retry semantics:
Compatibility order: expand / deploy / backfill / deferred contract:
Backup/recovery prerequisites / how verified / retention:
Downtime/lock risks and owner-approved limits:
CI automatic executor vs manual executor:

## Cleanup / test server
Durable evidence and release ledger path (outside retiring worktree):
Test server identity / Docker context endpoint / project naming and labels:
Compose files / overrides / env-file references (NO secret contents):
Environment lifecycle / data-cleanup / container policy / KEEP-volume policy:
Protected shared/production resources / rollback assets / retention:
Dedicated builder cache policy (shared caches retained by default):
Generated artifact paths / never-delete source-test paths:
Allowed measurement commands / host access / actual metrics available:

## Missing setup
List the small set of blockers that prevents release. If there is no Docker use,
mark NOT APPLICABLE. Do not install a provider, service, migration runner or CI
system just to populate this file. Explain material choices to the owner.

## Reusable test environments (required before housekeeping)

| Environment identity | Lifecycle | Data boundary and reviewed cleanup recipe | Container policy | Retained storage/config + startup recipe | Active users / authority |
| --- | --- | --- | --- | --- | --- |
| <actual endpoint/context/project> | shared-always-on / reusable-dedicated / per-change / unknown | <run/tenant IDs; baseline checks> | DATA_ONLY / CONTAINERS_KEEP_VOLUMES / scoped runtime retirement | <exact volume IDs; durable bind/config/image references> | <actual> |

Default KEEP volumes, seeds, schema/migration history, baseline users and reusable
configuration. No service stop if shared/active without explicit coordination.
No whole-database reset as a cleanup shortcut. Do not infer permission to destroy
storage from an old disposable label. Define reusable startup independently of a
retiring worktree and retain the SAME volume identity across worktree names.
Set readiness verification to INSPECTED_ONLY / EXERCISED / BLOCKED with evidence.
