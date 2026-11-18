# Dev System

Version 4.8.1. A set of written rules and runbooks for AI coding agents (Claude Code, Codex)
that do day-to-day software changes: how to size a request, who does what, how to prove the
work, and how to release and clean up afterwards.

This is instructions for agents. It is not a dispatcher, a scheduler or a permission
sandbox, and it does not launch models by itself. The host (Claude Code, Codex) runs the
agents; this package tells them how to behave. A Vietnamese overview is in
[README.vi.md](README.vi.md).

## What is in the package

| Path | What it is |
| --- | --- |
| `dev-guardrails/` | Skill: the development method. Discovery, planning hand-off, TDD, worktree rules, verification. |
| `release-housekeeping/` | Skill: the release method. PR, merge, deploy, ordered migrations, cleanup of test resources. |
| `workflow/` | Runbooks for the lead agent: scope router, daily workflow, project setup, release workflow, worktree lifecycle, resource ledger. |
| `adapters/` | Thin entry points for `/dev` (Claude Code) and `$dev` (Codex). They only point at the router. |
| `validation/` | 20 authored scenarios (expected behaviour, not measured results) and older check fixtures. |
| `tools/` | `regen_manifest.py` rebuilds `MANIFEST.json`. `watch-codex-job.sh` watches a running Codex builder by event (see below). `tools/usage/` holds token-usage measurement scripts. None of them is part of the package manifest. |
| `MANIFEST.json` | Byte count and SHA-256 of every package file (except itself). |

The method lives in the two skills. Routing and delegation live in `workflow/`, so the
skills stay free of model names and tiers.

## How a change flows

`/dev <request>` starts at [workflow/dev-router.md](workflow/dev-router.md). The lead agent
reads the repository instructions, then classifies the request on three separate axes: size,
risk and uncertainty. The classification picks the smallest safe lane.

| Lane | Use for | Short form |
| --- | --- | --- |
| QUICK_FIX | One bounded correction with a clear cause and low risk | 3a no-logic edit: short branch, one check, commit. 3b small behaviour fix: worktree, regression test, one builder. 3c may hand a qualifying fix to a fresh low-cost session that reports back. |
| STANDARD | A feature, a bug with unknown cause, or any small fix with high risk | Compact contract, vertical tasks, one builder per worktree, main review, same-builder fix, delta recheck. |
| LARGE | Several milestones or a staged rollout | Plan first, then run one approved milestone as STANDARD. |

Every lane except the no-logic edit works in its own worktree. A change the owner can see or
use waits for the owner's check before it is ready for a PR. A change ends at
`READY_FOR_PR`, `NEEDS_WORK` or `BLOCKED`. Push, merge, deploy and cleanup need a separate
authorization and run under the release skill and
[workflow/release-workflow.md](workflow/release-workflow.md).

State progression:

```
TRIAGE -> DISCOVERY -> AWAITING_APPROVAL -> WORKSPACE_READY -> READY_TO_BUILD -> BUILDING
-> READY_FOR_REVIEW -> VERIFYING -> OWNER_CHECK -> READY_FOR_PR
```

## Agent roles

- **Lead (main)**: Tier 1. Owns owner decisions, scope, assignment, review and the final gate.
- **Builder**: Tier 3 or Tier 2 as the task needs. One builder per worktree. Does TDD,
  commits each task and fixes its own findings.
- **Reviewer who did not write the code**: required for high-risk work.
- **Scripts and CI**: mechanical checks only.

A Claude sub-agent brief always requires the `/dev` workflow. A builder on a lower model tier
than the lead messages the lead before it settles a decision or an uncertainty the spec does
not cover: context, question, options and its recommendation, under 400 words.

## While the builder works, and the review

- **Watch by event, not by clock.** Most of the cost of a progress check is the lead reading its
  whole context again. For a Codex builder launched through the Claude Code plugin,
  `tools/watch-codex-job.sh` runs as a background command and polls every 5 minutes without the
  model. It wakes the lead only on a new commit, the job finishing or failing, a usage-limit or
  sign-in error, or a 40-minute heartbeat that also keeps the prompt cache warm. It prints only
  what is new since the last wake-up. A Claude sub-agent needs no watcher: it messages the lead.
- **Name the source.** Each progress line says where a claim comes from ("the builder's log
  says ...", "commit ...") and marks what the lead has not checked itself.
- **Independent checks in review.** Rerunning the builder's own tests only shows that its
  evidence exists and passes. For a change that produces or moves figures the lead (a) reconciles
  the key totals by a separate computation, every difference explained to the unit, and (b) reads
  the assertions against the acceptance criteria. For a key rule it (c) breaks the rule in a
  scratch copy and confirms a test goes red. The lead also reads the builder's whole progress log
  once and compares it with the final report.

Details: [workflow/daily-workflow.md](workflow/daily-workflow.md) sections 6, 7a and 8, and
[dev-guardrails/references/verification.md](dev-guardrails/references/verification.md).

The tier labels in [workflow/daily-workflow.md](workflow/daily-workflow.md) section 2 are the
owner's preference labels, not verified model IDs. Resolve real IDs once in
`workflow/project-setup.md`.

## Install

The package is a source directory. Do not copy it as one folder into a repository.

1. Read [INSTALL-HANDOFF.md](INSTALL-HANDOFF.md). It describes the repository-local install,
   the backup rules and the report an installing agent must give.
2. Install each skill folder whole, with its own `SKILL.md` at the root and all
   `references/`, `assets/` and `agents/` files.
3. Install only the adapter for the host in use. Claude Code: copy `adapters/claude/dev.md`
   to `.claude/commands/dev.md`. Codex: copy `adapters/codex/dev/` to
   `.agents/skills/dev/`. Details are in [adapters/README.md](adapters/README.md).
4. Point the adapter at the real location of `workflow/dev-router.md` if it is not
   `docs/agent-workflow/`.

Check package integrity before installing:

```bash
python -X utf8 tools/regen_manifest.py . 4.8.1
git diff --stat MANIFEST.json
```

An unchanged `MANIFEST.json` means the files match their recorded hashes. Hashes show
integrity, not who published the files.

## Status and limits

- Checked: internal Markdown links resolve and `MANIFEST.json` matches the files.
- Exercised in a pilot on a real repository: QUICK_FIX 3b, STANDARD, the owner check and
  release-housekeeping.
- Not exercised: QUICK_FIX 3a, LARGE, QUICK_FIX 3c (hand-off to a fresh low-cost session) and a
  full keep-warm cycle over several hours.
- The event watcher ran once, on one Codex job (LH-ERP, 19/11/2026), in an earlier form; the
  final 5-minute / 40-minute form and the lower-tier "ask the lead" rule have not run yet.
- The 20 scenarios in `validation/agent-scenarios.json` are expected behaviour. No routing
  accuracy, compliance or token saving has been measured against them.

See [VALIDATION.md](VALIDATION.md) and [CHANGELOG.md](CHANGELOG.md) for the full record.

## Notes and measurements

- `PILOT-REVIEW-2026-11-14.vi.md`: review of the first real-repository pilot (Vietnamese).
- `POOR-MAN-MODE-ANALYSIS-2026-11-15.vi.md`: where the tokens went and what it led to
  (Vietnamese). It is not part of the package manifest.
