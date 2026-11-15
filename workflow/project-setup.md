# Project Setup (fill from evidence; keep small)

The lead populates this once from the repo/host, then updates only changed facts.
Placeholders mean UNKNOWN, never permission or verified configuration. Reuse an
existing equivalent file by pointer. Do not commit credentials or private logs.

If the repository already has an equivalent (agent instructions, a deploy
runbook, a decision log, a progress file), record the path to it here and stop;
do not fill a second copy of the same facts into these templates.

## Project and records
Repo/root and supported shell/OS:
Repo instructions and their scope:
Installed dev-guardrails path:
Spec/decision source(s) and authority:
Active change record or index (prefer existing convention):
Allowed evidence/scratch directory and retention:
Approved test environment / isolated data; production endpoints to avoid:

## Actual host capabilities
Host/version:
Can spawn workers? Can resume a worker? Actual supported tool/mechanism:
Do workers share a filesystem? How patches/commits are integrated:
Can choose provider/model/effort per worker? Actual supported configuration:
Allowed tools / MCP connections (no secret values):
Available usage telemetry / unknown limits:
Authorized fallback when delegation is unavailable:
Can start a separate session that reports back? Model for a handed-off QUICK_FIX (dev-router.md 3c):
Context threshold after which each configured model costs more (or none):
Prompt cache lifetime and wake-up tool on this host (or none):
Keep-warm for the lead session (daily-workflow.md 7a): on / off (owner's choice):
Quiet hours for keep-warm (default 23:00-07:00 local):
Watch ceiling for work in flight (default 5 hours):

## Resolve the user's pools, do not invent provider bindings

Copy candidate preference labels from daily-workflow.md only as needed. Inspect
what the configured runtime actually supports and select authorized bindings.
Do not configure unavailable IDs or assert two models have equivalent ability.

| Role / pool | User preference label | Actual provider + model ID | Actual effort setting | Verified via | Allowed / unavailable |
| --- | --- | --- | --- | --- | --- |
| Main / Tier 1 | <preference> | UNKNOWN | UNKNOWN | <runtime evidence> | UNKNOWN |
| Hard builder / Tier 2 | <preference> | UNKNOWN | UNKNOWN | <runtime evidence> | UNKNOWN |
| Builder / Tier 3 | <preference> | UNKNOWN | UNKNOWN | <runtime evidence> | UNKNOWN |

## Existing check commands (inspect scripts for effects)

| Purpose | Exact command + working directory | Environment/data effects | Required stage | Evidence source |
| --- | --- | --- | --- | --- |
| Focused test | <discover> | <inspect> | During TDD | <repo path> |
| Lint/typecheck/build | <discover> | <inspect> | <repo policy> | <repo path> |
| Integration / smoke | <discover> | <inspect> | When applicable | <repo path> |
| Full checks / CI | <discover> | <inspect> | <local/CI policy> | <config path> |

Do not invent commands to fill every row. Write NOT APPLICABLE or UNKNOWN and why.
A test command's name does not establish safety. Keep secrets in the existing
secret manager/environment, not here. Do not introduce new infrastructure merely
to make this table complete.

## Authorization (actual source required)

| Action | Allowed scope / denied / unknown | Source of authorization |
| --- | --- | --- |
| Read repo / write local records | <status> | <source> |
| Edit approved product/tests | <status> | <source> |
| Run isolated tests / start local services | <status> | <source> |
| Create branch/worktree / local commits | <status> | <source> |
| Install dependencies / change environment | <status> | <source> |
| Push / create PR / update remote issues | <status> | <source> |
| Merge / deploy / live migrations | Not granted by this workflow | <separate approval if any> |

Do not repeatedly ask for actions already authorized within these limits. A new
scope, destructive effect or external action needs the appropriate authority.

## Worktree-first setup
Primary checkout / actual main worktree / common Git directory identity:
Verified origin identity / base branch (expected main) / fetch policy:
Approved sibling worktree parent / branch naming convention:
Durable runtime state/evidence root OUTSIDE retiring worktrees:
How installed skills/workflow are available in fresh worktrees:
Existing unmerged installation / bootstrap copy or stable read path, if any:
Isolation strategy for ports, test database, secrets and Docker resources:
Ownership / one-writer-per-worktree and parallel-change policy / worktree creation permission source:
Resource ledger template: [resource-ledger.md](resource-ledger.md).
Release facts are in [release-setup.md](release-setup.md); do not duplicate them.

## /dev entry and proportional scope (version 4)
Actual installed command/adapter and host discovery evidence:
Actual invocation (/dev, $dev or verified custom-host binding):
Existing command/skill name conflicts and resolution:
Workflow router path and canonical dev skill path:
Policy for clear direct repair requests / authorized local edits and worktrees:
Active initiative/change/milestone index (reuse existing source):
Test-environment lifecycle/data cleanup/retention: link to release-setup.md.
Unknown command support is not permission to install a dispatcher or fake an alias.
