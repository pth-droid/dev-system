# Version 4.8 - 2026-11-19

Owner-requested changes, discussed with the owner before writing (lead session on
LH-ERP J206, after a Codex run whose progress checks cost mostly context re-reads):

- daily-workflow.md 7a: while a builder is in flight, watch by event. A watcher
  script polls the cheap signals every 5 minutes without the model and wakes the
  lead only on a new commit, job finished/failed, a limit or sign-in error, or a
  40-minute heartbeat (replaces the 50-minute tick while it runs). It prints only
  what is new since the last wake-up. Each progress line names its source
  ("the builder's log says ...", "commit ...") and marks unverified claims.
- tools/watch-codex-job.sh: the watcher for Codex jobs launched through the
  Claude Code plugin.
- adapters/claude/warm.md: use the watcher instead of ticks while a Codex builder runs.
- dev-guardrails references/verification.md: "Independent checks". Rerunning the
  builder's tests is a provenance check only. Changes that produce or move figures
  need (a) a reconciliation of key totals by a separate computation and (b) a read
  of the assertions against the ACs; key rules need (c) a mutation spot check.
- daily-workflow.md 8: points to those checks, and main reads the builder's whole
  progress log once and compares it with the final report.

# Version 4.7.1 - 2026-11-18

Owner-requested label update:

- daily-workflow.md 2: Sol 6.1 labels in Tier 2 and Tier 3 now read Sol 6.2
  (gpt-6.2-sol is listed by the active Codex account). Labels only; the
  actual model ID is still resolved per run under project-setup.md.

# Version 4.7 - 2026-11-16

Owner-requested addition, designed with the owner before writing:

- workflow/project-setup.md: "Source qualification". When a pool can be served
  by several sources (accounts, keys, providers), each is checked from evidence
  the runtime reports on that machine: QUALIFIED only if it lists the exact
  model ID bound to the pool at the requested effort; otherwise SKIP (no model
  or no credit) or UNKNOWN, which does not qualify. The brief names model and
  effort explicitly so a weaker host default cannot be used. If no source
  qualifies, stop and report; no lowering of the tier. Switching the signed-in
  source needs the owner's one-time permission recorded on that machine. New
  host-capability line: how this machine switches the model source, or none.
- adapters/codex/source-qualification.md: where Codex reports the model list,
  default model and credit state, and what never to print. Machine-neutral: no
  account-switching tool is named in the shared files.

# Version 4.6 - 2026-11-15

Owner-requested addition, designed with the owner before writing:

- release-housekeeping/references/housekeeping-sweep.md: the cleanup part of a
  release with no release, started by the owner (/housekeeping) for the open
  folder's repository only. Read-only plan first, grouped into parts; the owner
  approves part by part. Cleanable only when every commit is in origin/main
  (ancestry, or a merged PR whose head is the branch tip) and it is not the
  main worktree. Other obstacles (uncommitted files, ignored data, an open PR)
  are resolved with the owner one step at a time. The host session that owns a
  cleaned worktree or local branch is archived with it, without a separate
  question (not the running session, not one mid-turn). Branches on origin stay
  their own part B, never deleted as a side effect. No memory of earlier answers
  between sweeps.
- release-housekeeping SKILL.md: mode and reference row. dev-router.md points
  to it. Optional adapters: /housekeeping (Claude Code), $housekeeping (Codex).
- Clicking through screens happens only for a change with a user interface,
  and only before release in the owner check (verification.md). After deploy
  only the deployment check runs (deploy-and-migrate.md); no click-through on
  production.

# Version 4.5 - 2026-11-15

Owner-requested edits from a review of 4.4, made by hand:

- Who may run on a default (dev-guardrails SKILL.md card 4, daily-workflow.md
  14): only a low-risk detail inside approved scope or a fallback approved in
  advance. Money, access, data integrity, product policy, outside effects and
  material scope stay "recommended, waiting for approval" even when the code is
  reversible; only independent work continues.
- Owner feedback (verification.md): a missing approved criterion is NEEDS_WORK,
  never deferred because the candidate is "no worse than today". Table of four
  feedback kinds.
- Baseline not green (planning-handoff.md, tdd.md): three cases instead of an
  automatic stop; a test already failing on the assigned bug is the RED.
- QUICK_FIX hand-off (dev-router.md 3c): same standard as 3a/3b, the minimum
  the new session must be told, statuses READY_FOR_REVIEW / BLOCKED /
  NEEDS_OWNER_CHECK, and the lead reads the diff and evidence instead of
  "re-runs nothing"; tiny edits may stay with the lead.
- Kept worktree (cleanup.md): switch it to the next branch before deleting
  the old one, or keep the old branch on purpose.
- Keep-warm (daily-workflow.md 7a): saving the cache never keeps an unsuitable
  model or effort, and never outranks a stop.
- tools/regen_manifest.py: `--check` verifies without writing; regeneration
  refuses to write on a missing file or broken link. INSTALL-HANDOFF.md step 1
  says a failed check stops the install.

Six scenarios were run; see VALIDATION.md.

# Version 4.4 - 2026-11-15

Owner-requested edits, made by hand, after measuring where the pilot's tokens
went (POOR-MAN-MODE-ANALYSIS-2026-11-15.vi.md, not part of the package):

- dev-router.md 3c: a QUICK_FIX that meets five conditions runs in a fresh
  low-cost session that reports back to the orchestrating session, with the
  result in the first 400 characters of its report. 3a and 3b are unchanged.
- daily-workflow.md 2: Terra 6.1 xHigh added to the Tier 3 labels; pick the
  model for a role by the context it will reach, because some models cost more
  past a context threshold.
- project-setup.md: lines for the hand-off model and the context thresholds.

Internal links were checked and MANIFEST.json regenerated. Section 3c has not
been run. The measurement scripts are in tools/usage/, outside the manifest.

# Version 4.3 - 2026-11-15

Owner-requested addition, made by hand:

- daily-workflow.md 7a: owner-enabled keep-warm for the lead session. One
  wake-up shortly before the prompt cache expires, which is also the progress
  check of work in flight; it ends by what the lead waits for (work finished or
  a watch ceiling; quiet hours or the owner's word), not by a count. The owner
  turns it on and off in plain words in any language. Section 7 now names this
  as the one scheduled activity the runbook creates.
- daily-workflow.md 12: what to do when the session is left to go cold.
- project-setup.md: four lines for the cache lifetime, the wake-up tool,
  quiet hours and the watch ceiling.

Correction to 4.2, same day:

- dev-guardrails/SKILL.md core card item 8 said "Main re-runs the evidence
  itself", which contradicted "Reuse authentic evidence" in verification.md and
  daily-workflow.md 8. It now says main inspects the evidence (assertions, raw
  output, end state) and re-runs only when the candidate or environment
  changed, no raw output exists, or nobody ran the check.
- verification.md: the repository's mandatory pre-deploy checks need a recorded
  run on the candidate before READY_FOR_PR; the builder or a low-cost runner
  may run them, main reads the output.

The Claude Code command that implements keep-warm (`/warm`) lives in the user's
commands folder, not in this package. Internal links were checked and
MANIFEST.json regenerated; structural checks, installer and ZIP archives were
not rerun or rebuilt. The cost reasoning behind the rule is an estimate from
list prices; how a subscription plan counts cached tokens was not measured.

# Version 4.2 - 2026-11-15

Edits from the pilot on LH-ERP (four real changes and one quick fix, see
PILOT-REVIEW-2026-11-14.vi.md, which is not part of the package). All are short
paragraphs in existing files; none adds a mechanical gate.

- dev-guardrails/SKILL.md: a 13-line core card at the top; numbers in reports
  are copied from command output.
- discovery.md: a sentence about current behavior carries its source.
- planning-handoff.md: trace a relaxed gate one step downstream; each task says
  where its evidence runs; what the builder does when the assignment is wrong,
  and a non-green baseline is a stop.
- verification.md: look at the end state and re-assert fixed values after every
  step; repository-mandated pre-deploy checks run by main before READY_FOR_PR
  with the exact command recorded; contents of the owner-check invitation; main
  walks the click path first; owner feedback is routed like a new request.
- daily-workflow.md: shared log files written once by main; environments ready
  before the first task; main micro-fix of about five lines; owner report opens
  with pending decisions and their defaults.
- dev-router.md: builder pool matched to the lane; routing of mid-flight
  requests and of pre-existing defects found while building.
- deploy-and-migrate.md: verify the deployed state independently of the script.
- pr-and-merge.md: confirm an outward step before the step that depends on it.
- project-setup.md, worktree.md: link the repository's own runbook and follow
  its worktree convention instead of filling templates.
- cleanup.md: keep the test environment when a follow-up on the same area has
  been requested.

Made by hand. Internal links were checked and MANIFEST.json regenerated; the
structural checks, extraction tests, installer and ZIP archives were not rerun
or rebuilt. No scenario was added to validation/agent-scenarios.json.

# Version 4.1 - 2026-11-14

Owner-requested edits to 4.0, made by hand in this folder:

- QUICK_FIX gains a no-logic edit path (dev-router.md 3a) for wording, docs and
  spacing: a short branch instead of a worktree, the commit message as the only
  record, one fitting check, and no need to load other workflow files.
- Local commits on the change branch are part of building. The candidate is a
  commit SHA; the dirty-tree hash fingerprint is removed. Push, PR, merge and
  deploy still need separate authority.
- Changes that do not affect each other may run in parallel without separate
  approval, each in its own worktree (daily-workflow.md section 1).
- Owner check: a change the owner can see or use needs the owner's recorded OK,
  after seeing the candidate running, before READY_FOR_PR (verification.md).
- Adds the owner status report (daily-workflow.md section 14).
- Adds four authored scenarios (20 in total). None has been run with a model.

The single-file installer and ZIP archives built for 4.0 were not rebuilt.
The 4.0 folder is kept as dev-system-v4.0-original.zip, outside the manifest.

# Version 4.0 - 2026-11-14

Updates the complete v3 distribution with two related owner requests:

- Adds the external /dev scope router: QUICK_FIX / STANDARD / LARGE, with risk and
  uncertainty independent of size and model tier. Adds promotion rules, micro
  contracts, session/milestone boundaries and checkpoint resume semantics.
- Adds thin host adapters: Claude Code /dev command; Codex $dev skill entry.
  All actual lane/delegation policy remains in workflow, not dev-guardrails.
- Avoids duplicate approval for explicit, clear authorized fixes. Keeps worktrees,
  meaningful TDD/evidence, required checks and risk review in every lane.
- Separates logical test data cleanup, container lifecycle and storage retention.
  Keeps reusable environments, volumes, schema/history/seed data and startup
  recipes. Preserves active shared services and blocks unsafe broad resets.
- Records exact retention identities and readiness; allows COMPLETE when expected
  retained assets remain. Genuine unmet required cleanup is still pending.
- Rebuilds both method skills, thin Codex adapter, complete archive and one-file
  portable installer. No user repo, real deployment, database or Docker is touched.

Earlier v3 introduced dedicated worktrees, release-housekeeping, safe main parity,
scoped cleanup and the self-contained installer. Those safeguards remain unless
explicitly tightened above. The retrospective reverify-project skill is unchanged.
