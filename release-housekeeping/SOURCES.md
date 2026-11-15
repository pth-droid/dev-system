# Sources and adaptation boundaries

Version 4.0, checked 2026-11-14. This is an original project-neutral runbook, not
an official Git/Docker/hosting plugin. It supplies no provider-specific deployment
command. Follow the installed tools and repository runbooks over generic examples.

- Git worktree: https://git-scm.com/docs/git-worktree
- Git merge / fast-forward: https://git-scm.com/docs/git-merge
- Git status / ignored files: https://git-scm.com/docs/git-status
- GitHub PR create: https://cli.github.com/manual/gh_pr_create
- GitHub PR merge / match-head / queue: https://cli.github.com/manual/gh_pr_merge
- Docker Compose down / volume behavior: https://docs.docker.com/reference/cli/docker/compose/down/
- Docker pruning scope: https://docs.docker.com/engine/manage-resources/pruning/
- Docker disk usage: https://docs.docker.com/reference/cli/docker/system/df/
- Docker runtime memory observations: https://docs.docker.com/reference/cli/docker/container/stats/
- Expand/contract illustration, NOT a Prisma dependency or command prescription:
  https://www.prisma.io/docs/guides/database/data-migration

The exact permission gates, ownership ledger, separate outcomes and no-global-prune
policy are design choices for this user's system. They are not a claim that a
Markdown skill technically enforces permissions or transactionality.

## Reusable environment amendment, checked 2026-11-14
- https://docs.docker.com/reference/cli/docker/compose/rm/ : stopped container removal;
  non-volume writable-layer data is lost; -v changes anonymous-volume retention.
- https://docs.docker.com/reference/cli/docker/compose/down/ : project teardown,
  volume options and anonymous-volume reattachment limitation.
- https://docs.docker.com/engine/storage/volumes/ : retained volume lifecycle.
Policy is owner-specific: preserve reusable test environments, baseline and volume
identity. No Docker/server operation was performed while authoring these files.
