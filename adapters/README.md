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

Claude Code commands in `~/.claude/commands/` (`ship.md`, `warm.md`, and
`housekeeping.md`) have their source here in `claude/`. Prefer a symbolic link
from the command folder to the file in `claude/` so an update in this repo
takes effect at once. Creating a link on Windows needs Administrator rights or
Developer Mode; if the link cannot be made, copy the file again after each
change to the source. A file can be linked only if it has no machine-specific
paths: `ship.md` and `warm.md` currently contain `D:\Working\Dev system\...`
paths, so they are a copy until those paths are made relative.
`dev.md` is also still a copy: the installed version carries an absolute path
to the workflow router, and the repo version expects
`docs/agent-workflow/dev-router.md` in the project. Linking it would make `/dev`
fail in projects that lack that folder.

`codex/source-qualification.md` is a reference note, not an installable
skill: it says where Codex reports the model list and the credit state that
project-setup.md "Source qualification" needs. It names no account-switching
tool; each machine records its own in project-setup.md.

Read-only discovery/menu checks verify registration without starting product
work. Files installed and invocation verified are different statuses. If the host
cannot register a shortcut, report that and use an explicit runbook instruction.
The adapter, skill and workflow must remain discoverable inside new worktrees.
