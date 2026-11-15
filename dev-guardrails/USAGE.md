# Using Dev Guardrails (revised separation)

This is one model-neutral development skill. Its references are loaded only for
the current phase. It includes no routing table, dispatcher, provider binding,
agent-count policy or automatic schedule. The separate daily workflow owns those.

Copy the entire folder, not only SKILL.md:
- Codex project: `.agents/skills/dev-guardrails/`
- Claude Code project: `.claude/skills/dev-guardrails/`
- Other hosts: use the supported skill directory or ask the agent to read
  SKILL.md explicitly and follow its relative reference links.

Do not overwrite custom edits in an older installation. Back them up outside the
host's skill-discovery paths, then deliberately replace/merge the full folder.
Remove the old routing.md and old routing pointers when upgrading this skill;
otherwise stale delegation policy can conflict with the new external workflow.
Do not replace AGENTS.md or CLAUDE.md. Refresh skills using the host's supported
mechanism or a new session, without discarding a useful work checkpoint.

In Codex chat use `$dev-guardrails`; in Claude Code chat use `/dev-guardrails`.
These are chat invocations, not PowerShell commands. Plain-language examples:

- "Plan this feature. Explain material choices and recommend an option. Stop
  after a compact spec and vertical-task plan if approval is still needed."
- "Build approved task T1 at <record path>. Use TDD; return READY_FOR_REVIEW with
  candidate and evidence. Do not choose agents or publish anything."
- "Verify-only this candidate against <record>. Inspect fresh evidence and run
  missing safe checks. Return the gate; do not edit the product."
- "Recheck findings F-01/F-02 on the repaired candidate. Include affected paths;
  reuse only evidence whose relevant inputs remain unchanged."

The owner approves product outcomes, consequential architecture tradeoffs and
material risk, not indexes, mocking syntax, or routine technical test boundaries.

Use the daily workflow to coordinate an actual agent pool. The skill alone is
also usable with one agent; record self-review and any unmet independent-review
requirement. No model is automatically changed by a label in instructions.

The reverify-project skill remains a separate one-time retrospective audit.
This skill only imports relevant approved findings into the current change.

Validation is structural, not an empirical benchmark or a real project run.
No enforced compliance or token savings are claimed. See the release validation
note for what was actually checked.

## Workspace / release separation

Provision or resume a dedicated change worktree through the daily workflow before
editing. Keep operational state outside that disposable worktree. At readiness,
return a release handoff; do not publish, migrate, deploy or clean up automatically.
Use the separately installed release-housekeeping skill only under release scope.
