---
name: add-lesson
description: Pull a Claude lesson meeting from Granola and save its transcript and summary to this repo, then commit and push. Use when the user says /add-lesson, "save today's lesson", or "add the Claude session".
---

# Add a lesson from Granola

1. **Find the meeting** with the Granola MCP tools (server `granola`). Default: the most recent meeting today where Ion explains Claude. If the user gave a title or date, use that. If more than one meeting could match, ask which.
2. **Get the full transcript** and Granola's notes for that meeting.
3. **Pick a folder**: `lessons/YYYY-MM-DD-<short-kebab-topic>/` (meeting date, not today's date). If it exists, update it instead of making a new one.
4. **Write `transcript.md`**:
   - Header: title, date, attendees (first names only).
   - The transcript as `**Speaker:** text` lines, unchanged except for redactions.
5. **Write `summary.md`** in plain words for non-engineers:
   - `# <Topic>` and the date
   - **In one line**
   - **What we covered** (bullets)
   - **Key ideas** (the 3 to 5 things to remember)
   - **Try this** (small things people can do with Claude this week)
   - **Questions asked** (with answers, if given)
   - **Links** mentioned
6. **Redact** before saving: API keys, tokens, passwords, URLs with secrets, and any candidate's personal data (names, emails, phones). Replace with `[redacted]`. Tell the user what you redacted.
7. **Update the index** in `README.md`: add a row right under the `lessons-index` comment, newest first: `| YYYY-MM-DD | Topic | [summary](lessons/<folder>/summary.md) |`.
8. **Commit and push** to `main`: `git add -A && git commit -m "Add lesson: <topic> (YYYY-MM-DD)"` then `git push`.
9. Reply with the GitHub link to the summary.
