# Sources and adaptation notes

Revised 2026-11-14. Independently written adaptation of the user's prior
`dev-guardrails` and `reverify-project` design. Not an official Matt/Pstack plugin,
not a complete implementation of either stack. Upstream main URLs are mutable.

## Primary sources inspected for this release

- https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grilling/SKILL.md
  Retain informed recommendations and agent-owned fact finding. Replace exhaustive
  technical interviews with 1-3 consequential owner-friendly decision cards.
- https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/to-spec/SKILL.md
  Retain explicit behavior and testing intent. Replace extensive story lists,
  required tracker publication and owner approval of technical seams with one
  compact contract and business-scenario approval.
- https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/to-tickets/SKILL.md
  Retain vertical outcomes and real dependencies, without mandatory per-ticket
  files or a technical dependency quiz for the owner.
- https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/tdd/SKILL.md
  Retain incremental RED/GREEN, public boundaries and independent expected
  results. Do not force refactoring after every GREEN or invent TDD retrospectively.
- https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/code-review/SKILL.md
  Retain spec and documented-standards checks. Do not copy its parallel-review
  agent requirement; the external workflow chooses review assignment.
- https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/handoff/SKILL.md
  Retain artifact pointers and secret redaction; adapt to the approved repo or
  temporary checkpoint location rather than forcing a specific operating system.

## Host references

- https://developers.openai.com/api/reference/cli
- https://developers.openai.com/plugins/build/skills
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/sub-agents

Manual skill paths and invocation are host-dependent. Actual cross-provider
launching, permissions, resume and effort selection must be supported by the
installed runtime. A Markdown file is not a runtime integration.

## Deliberate separation from the previous package

Remove model/tier routing and retry thresholds from the skill. Keep task quality,
review authorship requirements, evidence labels, and a model-neutral blocker
report. The external daily workflow selects resources and handles the fix loop.
The skill has no required external skill or live connector dependency.

## Version 3 additions

Dedicated worktree invariant and separate release handoff are original workflow
adaptations. Git references: https://git-scm.com/docs/git-worktree and
https://git-scm.com/docs/git-status . Worktrees do not isolate databases or services.
The previously approved v2 owner-facing discovery, TDD, evidence and routing
separation remain intact. No model/tier routing was moved into either skill.
