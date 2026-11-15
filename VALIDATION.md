# Validation - Dev System v4.5

## Revision 4.5

The 4.5 edits (see CHANGELOG.md) were made by hand. Six targeted scenarios
were run on 2026-11-15, only where the text had a conflict; this was not a full
re-run of the system. Results are in validation/agent-scenarios.json (the six
cases with a `run_2026_11_15` field).

- Four decision cases (assigned bug already red at baseline, owner finds a
  missing approved criterion, unanswered money decision, quick-fix evidence on
  the wrong SHA): each given to one fresh Claude Sonnet agent that read only the
  edited files and did not see the expected answer. All four chose the
  expected action. One run per case: this shows the text can be read the
  intended way, not that every model always will.
- Kept worktree: a real Git fixture on Windows. Deleting the branch the kept
  worktree has checked out is refused (exit 1); switching it to the new branch
  first lets the delete succeed (exit 0) and keeps ignored test data.
- Broken installer path: tools/regen_manifest.py run on copies with a missing
  file, a broken link and a tampered file. 4.5 `--check` exits 1 in all three
  and never writes; regeneration refuses to write. The 4.4 script exited 0 and
  rewrote MANIFEST.json when a link was broken.

Not checked: a handed-off QUICK_FIX session end to end, keep-warm over hours,
and the scenarios on Codex or on other models.

## Revision 4.4

The 4.4 edits (dev-router.md 3c, Tier 3 label, context thresholds) were made by
hand. Checked: internal Markdown links resolve and MANIFEST.json was regenerated.
Not checked: a QUICK_FIX handed to a fresh low-cost session has never been run.

## Revision 4.3

The 4.3 addition (keep-warm, daily-workflow.md 7a) was made by hand. Checked for
4.3: internal Markdown links resolve, MANIFEST.json was regenerated, and the
Claude Code wake-up mechanism was tried once with a one-shot job (result in
CHANGELOG.md if it differs from the description there). Not checked: a full
keep-warm cycle on a lead session over several hours, cache hits at a wake-up,
and how a subscription plan counts cached tokens.

## Revision 4.2

The 4.2 edits were made by hand after a pilot on a real repository. Checked for
4.2: internal Markdown links resolve, and MANIFEST.json was regenerated from the
edited files. Nothing else was rerun; the notes below describe 4.1 and 4.0.
The pilot itself exercised QUICK_FIX 3b, STANDARD, the owner check and
release-housekeeping end to end; QUICK_FIX 3a and LARGE were not exercised.

## Revision 4.1

The 4.1 edits were made by hand. For 4.1 only two things were checked: internal
Markdown links resolve, and MANIFEST.json was regenerated from the edited files.
The skill-creator validator, the 81 structural checks in
validation/current-checks.json and the extraction tests were NOT rerun; that
file describes 4.0. The single-file installer and ZIP archives were not rebuilt.
Everything below describes 4.0.

## Checks performed for 4.0

- Inspected the earlier complete v3 distribution and the pending reusable-test
  amendment; integrated the new /dev scope router and retention policy.
- Ran the installed skill-creator validator for dev-guardrails,
  release-housekeeping, and the thin Codex dev entry adapter.
- Checked internal Markdown file links, YAML entry metadata, skill length,
  complete resources, separation of model routing from method skills and presence
  of required scope/retention rules. These are structural/content checks, not
  proof that a model will follow the instructions.
- Rebuilt each single-skill archive as skill.zip, the complete distribution ZIP,
  SHA-256/byte manifest and the self-contained Markdown installer.
- Tested extraction and integrity with a fresh staging directory, a path with
  spaces, UTF-8 BOM, archive corruption, traversal, Windows reserved names,
  symlink entries, case-insensitive collisions and altered per-file metadata.
  See validation/current-checks.json for actual results and scope.

## Evaluation scenarios supplied, not run against agents

validation/agent-scenarios.json contains 20 authored examples (16 from 4.0, four
added in 4.1) covering scope/risk routing, quick/large session boundaries,
automatic promotion, reusable test retention, parallel changes, local commits
and the owner check. They are expected-behavior fixtures for a future host evaluation.
No LLM routing accuracy, behavior compliance or token savings has been measured.

## Previous validation retained as historical evidence

validation/git-fixtures.json and validation/portable-extraction.json originate
from the v3 artifact and are carried forward for provenance. They were NOT rerun
as part of v4. They do not establish current host, GitHub, Docker or agent behavior.

## Not performed

No user repository was modified. No actual Claude/Codex command registration,
Windows/PowerShell run, provider routing, PR/merge, cloud deploy, migration, Docker
server cleanup, logical database reset, runtime restart or RAM/disk reclamation
was performed. No real credentials, shared services or production data were used.

The extractor was exercised in this Linux container. Its Windows-aware path
checks are not a native Windows integration test. The workflow is instructions,
not an automatic dispatcher, scheduler, permission sandbox or enforcement system.
Hashes verify package integrity, not third-party publisher authenticity.
