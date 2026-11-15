# Necessary deployment and migration ordering

## Discover the actual release unit

Read existing deployment configuration/runbooks and migration tooling. Determine
which environment is approved, who executes each action (CI, platform or manual),
what triggers it, and where authoritative job/artifact/migration status lives.
Do not invent commands or install a deployment framework to fill a table.

For each component compare its last actually deployed SHA/artifact/config with
the intended release. A PR diff alone can miss earlier undeployed changes.
Include shared packages, lockfiles/build inputs, API consumers, workers/schedules,
configuration and schema compatibility. Select the smallest justified release
unit: frontend-only, backend/worker, database, static assets, or coupled services.
Docs-only may be NO_DEPLOY with evidence. Record unknown impact as a blocker.

Use immutable image digests/build IDs/commit references where supported. Record
old and new artifact identity per component, environment and intended smoke test.
Do not rebuild/redeploy every service by reflex; do not omit coupled consumers
just to make the change look small. A later main tip is not automatically the
same approved release.

## Migration plan BEFORE merge/deploy triggers

Discover pending migration IDs/checksums and applied history in the actual target.
Never infer production state from a dev schema or just from filenames. Resolve
drift/failed or partially applied jobs using the project's documented procedure.
Record locks/concurrency control, old/new application compatibility, expected lock
or downtime impact, backfill duration bounds and recovery mechanism.

Classify each change: additive compatible schema, data backfill, constraint/index,
or breaking/removal. Preserve applied migration history. Do not run dev reset,
force schema synchronization, or arbitrary production SQL under housekeeping.

Ordering is dependency-driven. A common safe pattern, when the repo supports it:
1. Apply compatible additive schema needed by the new app (expand).
2. Deploy an app compatible with both transition states.
3. Backfill/verify data according to the approved resumable plan; this may precede
   or follow the app rollout depending on what the new code requires.
4. Remove old schema only in a separately approved contract step after old
   consumers/rollback versions are no longer dependent on it.

This is NOT a fixed recipe for every framework. Some transactional/maintenance
window releases require another tested sequence. Explain consequential downtime
or data-loss tradeoffs to the owner; don't ask them to design the migration SQL.

Verify the required backup/recovery prerequisites for material data changes.
Reuse existing infrastructure; do not launch surprise paid backups or services.
A migration can be additive yet operationally risky on a large table. Plan and
verify locks/index creation/backfill against repo practices.

## Execute once, prove actual results

Assign exactly one executor per deploy/migration. If CI/platform performs it,
observe the real run and capture evidence; do not invoke the same job manually.
Use migration runner locking/history and stable deployment IDs where available.
On timeout, loss of connection or ambiguous exit, query actual state before any
retry. Non-idempotent operations must not be replayed blindly.

Record actual start/result, migration version/checksum and artifact identity.
A job submission is not completion. Failed or partially applied migrations block
dependent services and destructive housekeeping. Do not assume all DDL rolls
back transactionally or that code rollback reverses persisted data.

## Focused post-deploy verification

Check readiness/health, actual desired build/digest/version, a representative
changed user/API path, observable persistence effects, and migration/backfill
completion. Select checks needed to establish deployment, not repeat every TDD
step. Use read-only endpoints or isolated synthetic accounts/data. A real payment,
email or destructive transaction is not authorized by the word 'smoke'.

A 200 response from an old version is insufficient. For rollout strategies check
all relevant instances/traffic/version policy, not one lucky request. Honor the
repo's required observation/rollback window without inventing a universal delay.
If a required window hasn't completed, record pending and retain rollback assets.

A deploy script's success line is not the deployed state. After it returns,
check the thing that changed with a command independent of the script: the
version the server reports, the changed file or image actually being served,
one real run of the changed path. A rollback path that has never been executed
is reported as not verified.

This deployment check runs on every release. There is no click-through of the
screens on production after a deploy: clicking happens before release, in the
owner check of a change with a user interface (dev-guardrails verification.md).

## Failure / resume / cleanup-only

Record merged/deployed/migrated stages independently. Stop, retain diagnosis,
and use only an approved rollback/roll-forward plan. A repair after merge uses a
new tracked change/worktree unless the repo's emergency process says otherwise;
do not patch production or rewrite main to hide the failed release.

On resume query PR, CI, deployment and migration history before continuing.
Cleanup-only needs no repeat deployment: verify the original release gate and
remaining owned resources from its ledger. If fresh emergency teardown is needed
after a failed release, obtain a separately scoped cleanup decision and preserve
necessary evidence; routine successful-release cleanup does not imply that right.
