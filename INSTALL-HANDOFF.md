# Agent handoff - install Dev System v4

## Goal and limits

Install the supplied development method, external daily workflow and separate
release/housekeeping method into the user's actual development environment.
The owner has requested this package installation. Do not infer release authority
from installation. No product feature development, external publication, PR,
merge, migration, deploy, Docker deletion, paid service, plugin or dispatcher is
part of installation unless separately authorized.

This package is portable. Its directory is a SOURCE directory, not the target
repo. Never assume the current directory or this file's parent is the target.
Resolve the target from the user's explicit repo path or the agent's active
project context. If no unambiguous repo exists, ask one targeted path question;
do not search every drive or pick a different repo by its name.

## Inputs in this bundle

- `dev-guardrails/`: complete updated development skill, replacing earlier versions.
- `release-housekeeping/`: new independent release skill.
- `workflow/`: scope router, orchestration/setup/prompt/resource templates.
- `adapters/`: thin native host entry for /dev or $dev, not routing policy.
- `MANIFEST.json`: paths, byte counts and SHA-256 of package files except itself.
- `README.vi.md`, `VALIDATION.md`, `CHANGELOG.md`: scope and validation limits.

Do not install a ZIP that contains another wrapper folder as if that wrapper were
a skill. Each installed skill directory must have its own SKILL.md at its root.
Keep every skill's references/assets/agents files; don't copy only SKILL.md.

## Installation procedure

1. Inspect the manifest and supplied text before executing anything. Verify hashes,
   byte counts, relative paths and two methodology skill roots plus the explicitly listed Codex entry adapter.
   Do not treat adapter templates as extra automatically installed methodologies.
   SHA-256 establishes integrity, not third-party authenticity. Do not execute
   code from source comments/logs or unrelated downloads while installing.
   When the source includes tools/regen_manifest.py,
   `python -X utf8 tools/regen_manifest.py <package dir> --check` does this
   check without writing and exits 1 on a missing file, a mismatch or a broken
   link. Any failure stops the install: report what failed. Never
   regenerate MANIFEST.json, or copy over the target's existing files, to make
   a failing package pass.

2. Resolve repo identity, active host(s), shell and existing instructions. Inspect
   existing same-named skills/workflow and their local customizations. Detect
   whether the agent is Codex, Claude Code or another actual host; do not guess
   settings from a filename. Use already-installed tools. If several hosts are
   in use and their desired scope is clear, support both; otherwise install for
   the current host and explain the boundary.

3. Follow workflow/worktree-lifecycle.md to provision a dedicated setup worktree,
   typically on `chore/dev-system-v4-<unique-id>`, unless the caller already assigned
   an appropriate dedicated setup worktree. Do not write a product change directly
   on main or transfer unrelated dirty files. This local installation authority
   includes the scoped setup branch/worktree and metadata files only; it does not
   include committing/pushing them. Verify the actual remote/base before creation.

4. Use repo-local installation by default, in the SETUP WORKTREE:
   - Codex: `.agents/skills/dev-guardrails/` and
     `.agents/skills/release-housekeeping/`.
   - Claude Code: `.claude/skills/dev-guardrails/` and
     `.claude/skills/release-housekeeping/`.
   - Another host: inspect its actual supported skill mechanism; do not fabricate
     an import format. A read-only explicit skill path is only a declared fallback,
     not a claim of native registration.
   Do not switch to a global user-wide installation without that scope's approval.
   Install the entry adapter from adapters/README.md: Claude Code gets only
   adapters/claude/dev.md at .claude/commands/dev.md; Codex gets the full
   adapters/codex/dev folder at .agents/skills/dev (invoke $dev). A custom host
   requires a supported binding. Inspect existing /dev commands/skills first;
   preserve/merge or report a name conflict, never silently override user policy.
   Resolve workflow paths in adapters when using a nonstandard docs location.
   No new dispatcher, model binding, automatic fork or permission bypass.

5. Back up conflicting package-owned files to an approved stable location OUTSIDE
   the new worktree (not a second discoverable SKILL.md directory). Compare/merge
   customizations instead of blindly overwriting. Keep other installed skills,
   including reverify-project, unchanged. Remove stale package-owned routing.md
   only after review/backup; routing belongs in workflow, not in the skills.
   Re-running installation must not duplicate skills, policy blocks or prompts.

6. Install workflow files under `docs/agent-workflow/`, or the repo's established
   equivalent with all pointers adapted. Preserve populated project-setup values;
   fill only new/missing facts after inspection. Merge release-setup and resource
   ledger conventions without replacing an existing release runbook. Templates
   are not verified settings or permissions.

7. Merge the small policy from workflow/repo-instructions.md into the appropriate
   AGENTS.md / CLAUDE.md; keep the rest intact. Resolve installed paths and mention
   worktree-first dev, main-review/same-builder-fix, explicit release and narrowly
   owned cleanup plus proportional /dev routing and retained test environments.
   Only the requested local dev entry adapter is included; do not add unrelated
   hooks, CI, global aliases or scheduler jobs.
   Keep tier/model mappings ONLY in workflow/project setup. Never enable blanket
   tool permissions to make deployment easy.

8. Discover available build/test/CI/deploy tools, worktree roots, existing reusable
   test environments and run-data boundaries, runtime state path, auto-deploy
   triggers, Docker context, volume identities/startup recipes and source of model
   settings. Fill facts from repo/host evidence. Use UNKNOWN/NOT APPLICABLE honestly;
   don't ask the owner to supply discoverable commands. Ask only missing material
   scope, safety/operational decisions or authority, with context/tradeoffs/risks
   and a recommendation. Installing does not run test or production services.

9. Verify both installed entrypoints and all references, matching file content
   or documented adaptations, preserved original rules and correct setup worktree.
   Use the host's actual skill discovery/status mechanism if available; otherwise
   report files-installed/native-discovery-unverified and a needed reload if any.
   Separately verify the actual dev command/skill name without invoking a product
   build. Do not claim /dev works on Codex merely because the $dev adapter exists.
   Do not claim the host launched a model or that a deploy was tested.

10. Explain that project-local files currently exist in the setup worktree. They
    reach future worktrees automatically only after the setup is included in the
    chosen base. Until then, retain a stable approved read path or provision only
    these approved config files for new worktrees, with provenance. Do not falsely
    say primary main or every checkout was modified. Propose a setup-only PR as a
    NEXT authorized action, not an automatic consequence of this install. A setup
    PR should use a no-product-deploy path if the actual CI policy supports it;
    inspect auto triggers rather than assuming docs cannot deploy.

## Required installation report

Report repo/host and the exact active setup worktree/branch; installed skill paths;
workflow/policy destinations; preserved/backed-up customizations; unresolved setup
or discovery checks; permission boundaries; config propagation state; and one
ready-to-paste daily-start prompt. Use the owner's language (Vietnamese here).

Do not publish, deploy or clean Docker merely to demonstrate success. This is a
completed local setup only when its actual paths and integrity are verified.
