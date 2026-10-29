"""Lesson 1 deck: Context is everything (2026-10-28).

Run: python3 lessons/2026-10-28-claude-code-fundamentals/deck/build.py
Writes the Claude Slides files into ./project/ next to this script.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from sketch import *  # noqa: E402,F403

ROOT = Path(__file__).resolve().parent / "project"

slides: dict[str, str] = {}
NOTE = dict(font="Caveat", weight=700)

# 1. Cover
p = []
p += rect(1180, 250, 230, 70, fill=YELLOW)
p += rect(1180, 310, 580, 460, fill=YELLOW)
p += robot(1470, 360, scale=0.85, fill=LBLUE)
p += line(136, 652, 900, 646, color=ORANGE, w=8)
slides["cover"] = section("cover", "Sketch of a folder with a small robot inside it", p, [
    T(132, 240, 1000, "How Claude works · lesson 1", 52, color=BLUE, **NOTE),
    T(128, 310, 1040, "Context is<br>everything", 140, weight=700, lh=1.1).replace("'Nunito'", "'Fredoka'").replace("font-weight:800", "font-weight:600"),
    T(128, 980, 1200, "Job Machine · Oct 28, 2026 · with Ion", 28, color=GRAY),
], "Lesson 1 of the daily Claude sessions. Theme: an agent only knows what is in front of it.")

# 2. Folder
u, h = heading("It only knows what’s in its folder", 0)
p = list(u)
p += rect(560, 300, 300, 80, fill=YELLOW)
p += rect(560, 370, 800, 540, fill=YELLOW)
p += robot(960, 440, scale=1.0)
slides["folder"] = section("folder", "A big folder with Claude, drawn as a robot, inside it", p, [
    h, T(580, 312, 280, "your project", 36, weight=700),
], "Think of an agent as living inside a folder: CLAUDE.md, a context folder, skills. What's in there is all it knows. Missing context: it guesses. Leaked or wrong context: it gets confused. Protect the folder.")

# 3. People
u, h = heading("Agents think like people", 0)
p = list(u)
p += person(560, 330)
p += robot(1360, 320)
slides["people"] = section("people", "A stick person equals a robot", p, [
    h,
    T(860, 440, 200, "=", 180, weight=700, align="center").replace("'Nunito'", "'Fredoka'"),
    T(310, 770, 500, "you", 48, weight=700, align="center"),
    T(1110, 770, 500, "Claude", 48, weight=700, align="center"),
    T(128, 870, 1664, "both reason from whatever context they get", 60, color=BLUE, align="center", **NOTE),
], "Agents and humans share context-dependence: both reason continuously from incoming signals. Better input, better thinking.")

# 4. Lazy
u, h = heading("…and both are lazy", 0)
p = list(u)
for x in (300, 1060):
    p += rect(x, 380, 480, 240)
    p += rect(x + 480, 455, 40, 90, fill=INK)
    p += rect(x + 20, 400, 200, 200, fill=LGREEN, sw=2)
slides["lazy"] = section("lazy", "Two half-empty batteries, one for a person and one for Claude", p, [
    h,
    T(300, 660, 520, "you save time & calories", 40, weight=700, align="center"),
    T(1060, 660, 520, "Claude saves compute & tokens", 40, weight=700, align="center"),
    T(128, 860, 1664, "not a flaw: it’s how limited energy works", 60, color=RED, align="center", **NOTE),
], "Laziness by default comes from limited resources. Humans conserve calories, agents conserve tokens. Not a flaw, a feature of the constraints.")

# 5. One step at a time
u, h = heading("One step at a time", 0)
p = list(u)
p += rect(180, 320, 560, 420, fill=LRED)
p += line(220, 360, 700, 700, color=RED, w=7) + line(700, 360, 220, 700, color=RED, w=7)
for (x, y) in [(1000, 330), (1200, 510), (1400, 690)]:
    p += rect(x, y, 260, 140, fill=LGREEN)
p += arrow(1270, 475, 1330, 505, bend=-20)
p += arrow(1470, 655, 1530, 685, bend=-20)
slides["oneshot"] = section("oneshot", "A crossed-out giant box next to three small steps", p, [
    h,
    T(180, 490, 560, "the whole app", 64, weight=700, align="center"),
    label(1000, 330, 260, 140, "1", 80), label(1200, 510, 260, 140, "2", 80), label(1400, 690, 260, 140, "3", 80),
    T(128, 880, 1664, "give it a big goal, then small, clear tasks", 60, color=GREEN_S, align="center", **NOTE),
], "One-shotting a large project fights how Anthropic tuned the models: they take shortcuts. Make the agent ambitious, give it a clear purpose, and break the work into scoped tasks.")

# 6. Memory
u, h = heading("CLAUDE.md is its memory", 0)
p = list(u)
p += rect(380, 300, 480, 580, fill=PAPER)
p += line(800, 302, 858, 360, w=3)
for y, L in [(450, 340), (510, 390), (570, 310), (630, 370), (690, 280), (750, 340)]:
    p += line(430, y, 430 + L, y + j(3), color="#ADB5BD", w=5, passes=1)
p += arrow(900, 560, 1180, 560, bend=-40, color=BLUE, sw=4)
p += robot(1440, 330)
slides["memory"] = section("memory", "A CLAUDE.md page with an arrow to Claude", p, [
    h,
    T(420, 330, 420, "CLAUDE.md", 56, weight=700),
    T(870, 440, 380, "read first, every session", 46, color=BLUE, align="center", **NOTE),
], "CLAUDE.md in a project folder is the agent's working memory: what the project is, the rules, where things live. Put a context folder beside it, organized by topic. Start with Anthropic's defaults before adding memory tools like SuperMemory.")

# 7. Skills
u, h = heading("Skills are know-how in a file", 0)
p = list(u)
for x, w, c in [(130, 460, PAPER), (720, 460, LGREEN), (1310, 480, VIOLET)]:
    p += rect(x, 380, w, 240, fill=c)
p += line(560, 860, 1360, 854, color=ORANGE, w=7)
slides["skills"] = section("skills", "Best skill plus your context equals your know-how", p, [
    h,
    label(130, 380, 460, 240, "a good skill", 52), label(720, 380, 460, 240, "your context", 52),
    label(1310, 380, 480, 240, "your know-how", 52),
    T(600, 430, 110, "+", 110, weight=700, align="center").replace("'Nunito'", "'Fredoka'"),
    T(1190, 430, 110, "=", 110, weight=700, align="center").replace("'Nunito'", "'Fredoka'"),
    T(128, 730, 1664, "context, not code", 104, color=RED, align="center", **NOTE),
], "Skills (skills.sh) are markdown files that give the agent deep expertise in one area: Supabase, Vercel, UI, QA, browser automation. Start from the best default skill, then add your own context and edge cases. That version is your IP; no need to publish it.")

# 8. Tokens
u, h = heading("The first message costs the most", 0)
p = list(u)
p += line(560, 290, 560, 820) + line(560, 820, 1400, 820)
texts = [h]
for i, (x, y, c) in enumerate([(620, 320, LORANGE), (820, 730, LBLUE), (1020, 715, LBLUE), (1220, 740, LBLUE)]):
    p += rect(x, y, 140, 820 - y, fill=c)
p += arrow(1000, 420, 790, 450, bend=-20, color=RED, sw=4)
texts += [
    T(1010, 360, 600, "it loads all the context", 56, color=RED, **NOTE),
    T(128, 860, 1664, "then each message adds a little. output costs more than input.", 50, color=BLUE, align="center", **NOTE),
    T(128, 980, 1664, "Illustration of the pattern, not measured numbers.", 26, color=GRAY),
]
slides["tokens"] = section("tokens", "Hand-drawn bars: the first is tall, the rest are short", p, texts,
    "Tokens are the unit of AI information, built on bits. The first message in a session loads the full context so it's the most expensive; later ones add incrementally. You pay for input and output, output costs more. Default model in Claude Code: Opus 5.5.")

# 9. Try this
u, h = heading("Try this week", 0)
p = list(u)
texts = [h]
for i, (x, c, sc, rot, t1) in enumerate([(140, YELLOW, "#E8B500", -2, "Write a CLAUDE.md"),
        (700, LBLUE, "#4DABF7", 1.5, "Install one skill"), (1260, LGREEN, "#51CF66", -1, "Watch your tokens")]):
    p += rect(x, 300, 520, 480, fill=c, color=sc, sw=2, rot=rot)
    texts += [T(x + 40, 330, 440, str(i + 1), 140, color=INK, **NOTE), T(x + 40, 560, 440, t1, 56, weight=700)]
texts.append(T(128, 870, 1664, "a new session every day", 56, color=BLUE, align="center", **NOTE))
slides["trythis"] = section("trythis", "Three sticky notes with things to try this week", p, texts,
    "1. Add a CLAUDE.md to a folder you work in: what the project is and its rules. 2. Install a skill for a tool you use, like Supabase, and see how answers change. 3. In one session, compare the token count of the first message with the later ones. Daily sessions until everyone speaks the same language.")

# Write files
(ROOT / "slides").mkdir(parents=True, exist_ok=True)
for sid, html in slides.items():
    (ROOT / "slides" / f"{sid}.html").write_text(html)
    print(sid, len(html))
deck = json.loads((ROOT / "deck.json").read_text())
deck["faces"] = {
    "fredoka": {"family": "Fredoka", "href": "https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600&display=swap"},
    "nunito": {"family": "Nunito", "href": "https://fonts.googleapis.com/css2?family=Nunito:wght@500;800&display=swap"},
}
deck["order"] = list(slides)
(ROOT / "deck.json").write_text(json.dumps(deck))
