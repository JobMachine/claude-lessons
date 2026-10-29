# Claude lessons

Short daily sessions where Ion explains how Claude (and Claude Code) works to the Job Machine team.
Each session is recorded in Granola. This repo keeps the transcript and a summary of each one so anyone can catch up.

## How it's organized

```
lessons/
  2026-10-29-<topic>/
    summary.md      # what we covered, key ideas, things to try
    transcript.md   # full transcript (only when Granola provides one, which needs its paid plan)
```

## Lessons

| Date | Topic | Summary | Slides |
|------|-------|---------|--------|
<!-- lessons-index: new rows go below this line, newest first -->
| 2026-10-28 | Claude Code fundamentals and managing context | [summary](lessons/2026-10-28-claude-code-fundamentals/summary.md) | [deck](https://claude.ai/artifact/85rWeDt3pnbxQJBYHKuuXc) |

## Adding a lesson (for Ion)

After a session, open Claude Code in this folder and run `/add-lesson` (optionally with the meeting title or date).
It finds the meeting in Granola, writes `summary.md` and `transcript.md`, adds a row above, and commits and pushes.

## Rules

- Private repo, Job Machine team only.
- No secrets (API keys, tokens, passwords) and no candidate personal data. Redact them if they come up in a session.
