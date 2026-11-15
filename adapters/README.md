# Host entry adapters (not routing policy)

Install only the adapter for the actual host; do not install every variant.

- Claude Code: copy `claude/dev.md` to `.claude/commands/dev.md` for `/dev`.
  This supported command-file format is deliberately a thin pointer, not another
  copy of the workflow. Check existing commands/skills named dev before replacing;
  a same-named skill can take precedence. No model/effort/fork/tool preapproval.
- Codex: copy the entire `codex/dev/` directory to `.agents/skills/dev/` and use
  `$dev` (or the actual host skill selector). It is a native skill-shaped adapter,
  not another methodology. Do not claim a bare `/dev` is universally supported.
- Another runtime / custom coding system: bind its supported `/dev` command to
  `docs/agent-workflow/dev-router.md`, forwarding request and active context.
  Verify the actual command registration; do not install a new dispatcher or
  remap unknown global shortcuts without permission.

The optional housekeeping entry follows the same pattern: Claude Code copies
`claude/housekeeping.md` to `.claude/commands/housekeeping.md` for
`/housekeeping`; Codex copies `codex/housekeeping/` to
`.agents/skills/housekeeping/` for `$housekeeping`. Both point to the
release-housekeeping skill's housekeeping-sweep.md and authorize only its plan.

Read-only discovery/menu checks verify registration without starting product
work. Files installed and invocation verified are different statuses. If the host
cannot register a shortcut, report that and use an explicit runbook instruction.
The adapter, skill and workflow must remain discoverable inside new worktrees.
