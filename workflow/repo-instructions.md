# Optional repo instruction block

This is a block to MERGE into existing AGENTS.md / CLAUDE.md under installation
authorization, not a replacement file. Resolve the installed skill path and keep
only one canonical daily workflow policy. Existing higher-priority rules win;
report actual conflicts rather than silently weakening them.

---

## Development method and orchestration

- For daily feature/bug work, the lead follows `docs/agent-workflow/daily-workflow.md`
  and the verified facts in `docs/agent-workflow/project-setup.md`.
- Use the installed `dev-guardrails` skill for the current phase. Delegatees must
  read its entrypoint and applicable references explicitly; inheritance is not assumed.
- Ask the owner only consequential product/operational decisions, with context,
  options, tradeoffs, risks and a recommendation. Discover repo facts yourself.
- Preserve approved ACs and focused TDD. Before readiness, reconcile the candidate
  with the spec and real evidence. Never turn unknown/skipped checks into PASS.
- Keep skill methodology separate from workflow routing. Default to main review
  plus the same builder's fixes, one writer per worktree, no automatic review
  swarm. Run changes in parallel when they do not affect each other.
- Respect the recorded authority, unrelated edits, safe environments and repo CI.
  Local commits on the change branch are part of building. A ready local gate
  does not grant push/PR/merge/deploy permission.
- Before READY_FOR_PR on a change the owner can see or use, show the owner the
  candidate running (steps plus screenshots) and record their OK.
- Resume from the active change record. Do not run the full reverify-project audit
  after each feature or restart all discovery each day.

---

This block guides agents, not runtime permissions or branch protection. Do not
install hooks, paid services or a dispatcher just to use it.

## Version 3 lifecycle addition (merge into the same canonical block)

- Before development writes, follow `docs/agent-workflow/worktree-lifecycle.md`:
  create or resume the change's dedicated Git worktree, never edit product work
  directly on main. Use explicit workspace paths for all agents and checks.
  A no-logic QUICK_FIX edit (wording, docs, spacing) may use a short branch.
- Maintain a small durable resource/evidence ledger outside retiring worktrees;
  do not share test databases/ports/volumes accidentally across worktrees.
- After readiness, release only under explicit authority. Follow
  `docs/agent-workflow/release-workflow.md` and the installed release-housekeeping
  skill for PR, merge, necessary deploy/migrations, local-main sync and retirement.
- Preserve user changes and tracked tests. No reset-to-main shortcut or broad
  Docker pruning. Unknown/shared resources are retained and reported.

Entry: /dev uses the installed host adapter and `docs/agent-workflow/dev-router.md`
to choose QUICK_FIX, STANDARD or LARGE independently of risk/tier. Keep one active
session scope; do not ask the owner to choose a lane. No-logic edits use a short
branch and a commit message only. Other tiny clear fixes use a micro record, not
a full spec ceremony; mandatory tests/review/worktrees still apply to them.
Reuse existing safe test environments. Clean run data, not the reusable baseline;
remove only eligible containers and KEEP volumes/config by default. Never delete
worktree paths still needed by retained environments. Release authority is separate.
