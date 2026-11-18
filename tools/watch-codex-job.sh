#!/usr/bin/env bash
# Event-driven watch of a background Codex job launched through the Claude Code plugin (daily-workflow.md 7a).
# Run it as a background command; it costs no model tokens while it waits. It exits - which wakes the lead - on:
#   a new commit in the builder's worktree, the job finished/failed, a usage-limit or sign-in error line,
#   or a heartbeat (default 40 min, under the ~1 h prompt-cache lifetime, so it also keeps the cache warm).
# It prints only what is NEW since the previous wake-up (cursor in the state file) plus the latest rate-limit line.
#
# Usage: watch-codex-job.sh <job> <worktree> <state-file> [heartbeat-min=40] [poll-min=20]
#   <job>: path of the plugin job without extension, e.g.
#          ~/.claude/plugins/data/codex-openai-codex/state/<worktree>-<hash>/jobs/task-xxxx   (reads <job>.json and <job>.log)
# First run: write the cursor with the current counts, so old lines are not reported:
#   printf 'PROG=%s\nSHA=%s\nFAIL=%s\nERR=%s\n' "$(grep -c 'Assistant message captured' <job>.log)" \
#     "$(git -C <worktree> rev-parse HEAD)" "$(grep -c 'Command failed' <job>.log)" 0 > <state-file>
set -u
J="$1"; WT="$2"; ST="$3"; HB="${4:-40}"; POLL="${5:-20}"
ERR_RE='Turn failed|usage_limit|credits_depleted|unauthorized|exited with'
touch "$ST"; . "$ST"
P0="${PROG:-0}"; C0="${SHA:-$(git -C "$WT" rev-parse HEAD)}"; F0="${FAIL:-0}"; E0="${ERR:-0}"
status() { python -X utf8 -c "import json,sys;print(json.load(open(sys.argv[1],encoding='utf-8')).get('status',''))" "$J.json" 2>/dev/null; }
t0=$(date +%s); ev=""
while :; do
  s=$(status); head=$(git -C "$WT" rev-parse HEAD)
  e=$(grep -cE "$ERR_RE" "$J.log" 2>/dev/null)
  [ "$s" != "running" ] && ev="FINISHED ($s)" && break
  [ "$head" != "$C0" ] && ev="NEW COMMIT" && break
  [ "${e:-0}" -gt "$E0" ] && ev="ERROR / LIMIT" && break
  [ $(( $(date +%s) - t0 )) -ge $(( HB * 60 )) ] && ev="HEARTBEAT ${HB} MIN" && break
  sleep $(( POLL * 60 ))
done
p=$(grep -c "Assistant message captured" "$J.log"); f=$(grep -c "Command failed" "$J.log")
echo "EVENT: $ev | status: $(status) | new failed commands: $(( f - F0 ))"
echo "-- new progress lines (builder's job log, unverified):"
grep "Assistant message captured" "$J.log" | tail -n +$(( P0 + 1 )) | sed -E 's/^\[([^]]*)\] Assistant message captured: /\1 /' | cut -c1-300
echo "-- new commits:"; git -C "$WT" log --oneline "$C0..HEAD" 2>/dev/null
R=$(ls -t ~/.codex/sessions/*/*/*/rollout-*.jsonl 2>/dev/null | head -1)
echo "-- rate limit (latest):"
grep -o '"primary":{"used_percent":[0-9.]*\|"secondary":{"used_percent":[0-9.]*\|"rate_limit_reached_type":"[a-z_]*"' "$R" 2>/dev/null | tail -3 | tr '\n' ' '; echo
printf 'PROG=%s\nSHA=%s\nFAIL=%s\nERR=%s\n' "$p" "$(git -C "$WT" rev-parse HEAD)" "$f" "${e:-0}" > "$ST"
