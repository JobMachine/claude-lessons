---
name: add-lesson
description: Pull a Claude lesson meeting from Granola and save its transcript and summary to this repo, then commit and push. Use when the user says /add-lesson, "save today's lesson", or "add the Claude session".
---

# Add a lesson from Granola

1. **Find the meeting** with the Granola MCP tools (server `granola`). Default: the most recent meeting today where Ion explains Claude. If the user gave a title or date, use that. If more than one meeting could match, ask which.
2. **Get Granola's notes** with `get_meetings`, then try `get_meeting_transcript`. Transcripts need a paid Granola plan: if it errors, don't retry. Skip `transcript.md` and tell the user.
3. **Pick a folder**: `lessons/YYYY-MM-DD-<short-kebab-topic>/` (meeting date, not today's date). If it exists, update it instead of making a new one.
4. **Write `transcript.md`** (only if step 2 returned a transcript):
   - Header: title, date, attendees (first names only).
   - The transcript as `**Speaker:** text` lines, unchanged except for redactions.
5. **Write `summary.md`** in plain words for non-engineers. Use only what's in the notes or transcript; don't add anything that wasn't said. Link the Granola note at the top.
   - `# <Topic>` and the date
   - **In one line**
   - **What we covered** (bullets)
   - **Key ideas** (the 3 to 5 things to remember)
   - **Try this** (small things people can do with Claude this week)
   - **Questions asked** (with answers, if given)
   - **Links** mentioned
6. **Redact** before saving: API keys, tokens, passwords, URLs with secrets, and any candidate's personal data (names, emails, phones). Replace with `[redacted]`. Tell the user what you redacted.
7. **Update the index** in `README.md`: add a row right under the `lessons-index` comment, newest first, in the same format as the rows below it.
   **Slides (when the user asks):** copy the previous lesson's `deck/build.py`, rewrite the slides (one idea each: short headline, one drawing, at most one line), run it, then `python3 tools/render.py lessons/<folder>/deck` and add a `## Slides` section to the summary.
   **This repo is public:** double-check step 6 before committing.
8. **Commit and push** to `main`: `git add -A && git commit -m "Add lesson: <topic> (YYYY-MM-DD)"` then `git push`.
9. Reply with the GitHub link to the summary.
