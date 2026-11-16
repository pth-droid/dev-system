# Codex: reading source evidence for project-setup.md "Source qualification"

Host notes only. The rules (QUALIFIED / SKIP / UNKNOWN, rotation order, no
fallback) are in workflow/project-setup.md. Paths below are relative to the
Codex home folder (`~/.codex`, or the folder `CODEX_HOME` points to).

## What the runtime reports

| Need | Where Codex reports it | Notes |
| --- | --- | --- |
| Models the signed-in source lists | `models_cache.json`, array `models` | Each entry has `slug`, `visibility` (`list` or `hide`), `priority` and `supported_reasoning_levels`. The file has `fetched_at` and an `identity` hash and describes only the source signed in when it was fetched. Treat it as stale if `fetched_at` is old or the source changed since; refresh it by running Codex once under that source. |
| Default model | `config.toml`, `model` and `model_reasoning_effort` | If this is below the pool, the brief must pass the model and effort explicitly. |
| Credit / quota now | Newest `sessions/YYYY/MM/DD/rollout-*.jsonl`, last `rate_limits` object | `primary` is the 5-hour window and `secondary` the weekly one (`used_percent`, `resets_at`). `rate_limit_reached_type` such as `workspace_member_credits_depleted` and `credits.has_credits=false` mean SKIP: no credit. A session written under another source says nothing about this one. |
| Plan type (context only) | Claims inside `auth.json` | Read only the plan and subscription end. It never decides qualification. |

Do not print `auth.json`, any `*auth*.json` or any token, key or email. When a
file mixes secrets with the fields you need, extract the named fields and
redact the rest.

## Switching source

How a machine switches Codex source differs (a manual `codex login`, an account
manager, an API key) and is written in this machine's project-setup.md line
"How this machine switches the model source". This adapter does not name or
depend on any particular tool. Do not decrypt a tool's stored account files to
read them; switch to the source through the tool's own supported action, with
the owner's recorded permission, then read the evidence above.

## Passing the model explicitly

Give the worker the model ID and effort from the pool row, for example
`codex exec -m <model-id> -c model_reasoning_effort=<effort> ...`. Check the
flag spelling with `codex exec --help` on this machine before relying on it.
