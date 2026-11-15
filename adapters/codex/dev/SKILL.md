---
name: dev
description: "Enter or resume the project's external development workflow when the owner invokes $dev or asks to start the dev router. This is a thin command adapter; scope classification and delegation live in docs/agent-workflow/dev-router.md and daily-workflow.md."
---

# Dev entry adapter

Find the actual project root and read `docs/agent-workflow/dev-router.md`, or the
explicit installed workflow path in the repo instructions. Follow that runbook
using the owner's request and current approved checkpoint. Do not recursively
invoke this adapter or duplicate the router's policy here.

If the runbook is missing, explain the missing installation; do not invent a
workflow or silently install into another repo. If no new request is supplied,
resume the unambiguous active change; otherwise ask for the goal/priority.
Use the installed dev-guardrails skill as directed by the router. Do not force a
model, fork a new agent, change tool permissions, or publish/merge/deploy merely
because this entry was invoked. Report the actually selected route and scope.
