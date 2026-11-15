# Preserve reusable test environments

Read before data cleanup, container removal or deletion of a worktree supporting
a test environment. Reuse existing tooling; this is not another skill or service.

## 1. Classify before acting

Separate DATA cleanup, CONTAINER lifecycle and STORAGE retention. Owning a
container does not imply ownership of its database or volume. A resource is not
disposable merely because the current change used or created it.

| Environment | Normal completion policy |
| --- | --- |
| Existing shared / always-on | DATA_ONLY: clean authorized run data; keep infrastructure and other users' runtime unchanged. |
| Reusable dedicated / idle | CONTAINERS_KEEP_VOLUMES when approved and no active users: clean scoped data, remove eligible containers, retain volumes and a usable recreation recipe. |
| Per-change disposable | Retire allowlisted runtime/generated artifacts; KEEP volumes by default. Storage decommission requires separate explicit scope. |
| Unknown lifecycle or data boundary | Retain it; report the missing fact, not permission to delete/reset. |

Select the policy once in verified setup and reuse it unless facts change. Removing
containers is conditional on safe recreation. Shared/always-on services stay up;
approved stop-but-retain exceptions remain valid. Do not create more infrastructure
when an existing authorized environment safely isolates this run's data.

## 2. Clean run data, not the reusable database

- Identify exact non-production endpoint/database/tenant and run boundary: run ID,
  dedicated tenant/schema, created-record IDs or another verified isolation key.
  Do not guess broad name/date filters. Names containing test do not prove safety.
- Preserve schema, migration history, baseline fixtures/seed data, standard test
  accounts and configuration. Keep fixture/test files in source control.
- Prefer the existing reviewed cleanup API/script. Inspect its actual effects;
  reset-test-db may erase the reusable environment despite its name.
- Pause only this run's writers/jobs as needed. Clean its rows, objects, uploads
  and queue messages while required services are still available. Use a safe
  preview/affected-count check or transaction where supported. Check cascades and
  dependency scope; make reruns idempotent. Do not consume another run's messages.
- Do not truncate shared tables, DROP the whole database, reset migrations, flush
  shared caches/queues or delete database-volume files as logical data cleanup.
  Removing a volume is not a data-reset shortcut in this workflow.
- Verify targeted data is gone AND the baseline remains using scoped counts/checks.
  Record command, safe target identity, selector and result, not secrets/records.
- If required cleanup has no safe recipe or boundary, keep data and mark that
  action BLOCKED. Ask only the consequential ownership/reset decision, not for
  technical commands discoverable in the repo. Never improvise a whole-DB reset.

Container removal does not clear records in a retained volume. Logical row
cleanup also does not prove physical disk was returned to the host. Do not run
compaction or destructive resets merely to claim storage savings.

## 3. Keep recreation possible

Before stopping/removing containers, record and verify:
- Host/context, stable Compose project, service identities, exact volume names/IDs,
  mount destinations and durable bind paths. Do not silently create a different
  empty volume by changing worktree/Compose project names on the next run.
- Compose files, overrides, image/build references and secret-store references in
  approved durable locations OUTSIDE retiring worktrees. No secrets in ledgers,
  source control or distributable files. Inspect config without exposing secrets.
- Existing startup recipe using the retained storage and compatible schema.
- Required state is in retained mounts, not only the container writable layer.
  If unknown, retain the container until resolved. Inspect auto-remove behavior
  before stopping a container with storage to preserve.
- Prefer named/external volumes or explicit durable bind paths. Anonymous volumes
  require saved exact IDs and a verified reattachment recipe; keeping an anonymous
  volume does not make a later Compose up automatically reuse it.

Do not delete a worktree containing the only reusable config, bind data or required
build input. Preserve/repoint under approval and verify first; otherwise retain
the worktree and report the blocker. Keeping a volume but losing its startup
recipe or bind directory is not successful preservation.

## 4. Container and storage actions

Use exact approved targets. Remove eligible idle/disposable runner containers
without volume deletion. Leave shared/always-on containers running. For a fully
eligible dedicated idle stack, scoped down WITHOUT volume deletion may stop/remove
containers and disposable project networks only when every affected service can
be stopped and the recreation recipe survives. Otherwise target eligible services
or IDs individually. Do not kill unowned processes or use name wildcards.

KEEP all named/anonymous volumes, retained bind data, baseline config, reusable
images, shared networks and caches in normal housekeeping. Do not run down
--volumes, rm -v, volume rm/prune, system prune, renew-anonymous-volumes or an
equivalent destructive startup/reset operation. Deliberate environment/storage
decommission is a separate explicit request with exact IDs and retention/recovery
checks; it is not implied by release or by an old disposable label.

Verify retained volume IDs and startup references still exist. Report readiness
as INSPECTED_ONLY, EXERCISED or BLOCKED, with actual evidence. Do not claim restart
was tested if it was not; do not restart a shared service or start an idle stack
solely to prove a point without authority.

## 5. Completion and measurement

Record each action/resource as DATA_CLEANED, REMOVED, RETAINED_BY_POLICY, BLOCKED,
NOT_IN_SCOPE or NOT_APPLICABLE. Expected kept volumes/config/shared services are
successful outcomes, not leftovers. COMPLETE is allowed when all required actions
and retention checks pass. Required data cleanup or safe worktree retirement that
cannot finish means RELEASED_CLEANUP_PENDING, even if deployment succeeded.

Report workload RAM, Docker disk and host free space separately only if measured.
Retained volume space is intentionally not reclaimed. Do not prune, compact,
restart Docker, reboot, shut down WSL or drop shared caches to improve the numbers.
A preserved reusable test environment is part of successful housekeeping.
