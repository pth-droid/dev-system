---
description: Keep the lead session's prompt cache warm while it waits, and check work in flight at each wake-up (Dev System daily-workflow.md section 7a). Use when the owner types /warm or says in plain words "keep warm", "keep the session warm", "keep warm until 22:00", "stop keep-warm", "stop warming", "let it go cold", "is keep-warm on?", "bật giữ ấm", "giữ ấm tới 22:00", "tắt giữ ấm", "giữ ấm đang bật không", or when a message is exactly a keep-warm tick.
argument-hint: "[on | off | until HH:MM | status | tick]"
---

Keep-warm for this session. Arguments: $ARGUMENTS

Read `D:\Working\Dev system\workflow\daily-workflow.md` section 7a once per session and
follow it. This file only says how to do it in Claude Code.

Tools: `CronCreate`, `CronDelete`, `CronList` (load them with ToolSearch if they are
deferred). Jobs are session-only and fire only while the session is idle.

Settings: the project's setup record if it has them; otherwise quiet hours 23:00-07:00
local and a 5-hour watch ceiling. An argument or the owner's words override them for
this session.

- `on` (or no argument), `until HH:MM`:
  1. Get the local time with one shell command.
  2. `CronList`; delete any earlier keep-warm job with `CronDelete`.
  3. `CronCreate` a ONE-SHOT job (`recurring: false`) pinned to the minute 50 minutes
     from now, with the prompt
     `keep-warm tick - Dev System daily-workflow.md 7a (check work in flight, one line, re-arm or stop)`.
     Do not use a recurring job: it may start up to 30 minutes late, past the cache lifetime.
  4. Say one line: on, until when, next wake-up time as the tool reports it.
- `tick` (the job fired):
  1. Decide from the time the job was pinned to, without a clock call: if nothing is in
     flight and quiet hours have begun or the owner's end time has passed, or the watch
     ceiling has passed, do not re-arm; say one line why and stop.
  2. Otherwise send ONE message with, in parallel: the checks of work in flight (newest
     commit in the builder's worktree, last lines of its log or report file) and the next
     one-shot `CronCreate`, pinned 50 minutes after this tick's time.
  3. Answer in one line. Act further only in the three cases section 7a lists.
- While a Codex builder launched through the plugin is in flight, watch by event instead
  of ticks (section 7a): delete the keep-warm job, then run
  `D:\Working\Dev system\tools\watch-codex-job.sh <job> <worktree> <state-file>` as ONE
  `Bash` background command (`run_in_background: true`; set the cursor first, see the
  script header). When it ends, answer in one line naming the source ("the builder's log
  says ...", "commit ..."), then re-arm the watcher, or start the review if the job
  finished. When nothing is in flight any more and keep-warm is still wanted, go back to
  the 50-minute one-shot job.
- Ordinary turns in between need no re-arming: the ticks keep a fixed 50-minute cadence,
  so two requests are never more than 50 minutes apart. Only when a turn ran across the
  pinned minute, check `CronList` at its end and re-arm if the job is gone.
- `off`: `CronList`, delete the keep-warm job, say one line.
- `status`: `CronList`; say whether it is on, the next wake-up, and what ends it.

Never keep two keep-warm jobs. Do not change the model or the effort level of this
session without a reason while keep-warm is on, but saving the cache is never a
reason to keep an unsuitable model or effort: when the work needs more capability,
switch. A bare "stop", "pause" or "nghỉ" is not a keep-warm command; still obey it
as a stop of the work, and ask whether keep-warm should end too when unsure.
