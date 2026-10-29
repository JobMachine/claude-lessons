"""Draw the README banner (assets/banner.png) in the same whiteboard style as the decks."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render import shoot  # noqa: E402
from sketch import (  # noqa: E402
    BLUE, GRAY, LBLUE, LGREEN, ORANGE, RED, YELLOW, T, arrow, line, rect, robot,
)

W, H = 1600, 600

p: list[str] = []
p += line(84, 268, 760, 262, color=ORANGE, w=8)
p += rect(1060, 120, 200, 60, fill=YELLOW)
p += rect(1060, 170, 460, 360, fill=YELLOW)
p += robot(1290, 205, scale=0.7, fill=LBLUE)
p += rect(830, 330, 250, 170, fill=LGREEN, color="#51CF66", sw=2, rot=-4)
p += arrow(960, 320, 1050, 250, bend=-30, color=BLUE)

svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
    'style="position:absolute;left:0;top:0">'
    '<defs><pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse">'
    '<path d="M40 0H0V40" fill="none" stroke="#E9ECEF" stroke-width="1.5"/></pattern></defs>'
    f'<rect width="{W}" height="{H}" fill="#FCFCFA"/><rect width="{W}" height="{H}" fill="url(#g)"/>'
    + "".join(p) + "</svg>"
)
texts = [
    T(80, 90, 800, "how Claude works", 56, font="Caveat", weight=700, color=BLUE),
    T(76, 140, 900, "Claude lessons", 120, weight=700).replace("'Nunito'", "'Fredoka'").replace("font-weight:800", "font-weight:600"),
    T(80, 300, 720, "Short daily whiteboard lessons on Claude and Claude Code, for people who don’t write code.", 36),
    T(845, 375, 220, "context is everything", 34, font="Caveat", weight=700, color=RED, align="center", lh=1.1),
    T(80, 520, 900, "transcripts · summaries · slides", 30, color=GRAY),
]
html = f'<section style="background:#FCFCFA;font-family:Nunito, sans-serif">{svg}{"".join(texts)}</section>'
out = Path(__file__).resolve().parent.parent / "assets" / "banner.png"
out.parent.mkdir(exist_ok=True)
shoot(html, out, W, H)
print(out)
