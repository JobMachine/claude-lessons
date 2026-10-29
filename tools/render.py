"""Render lesson slides (and the README banner) to PNG with headless Chrome.

Run: python3 tools/render.py lessons/<folder>/deck
Writes lessons/<folder>/slides/NN-<id>.png, in deck order.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FONTS = (
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    'family=Fredoka:wght@500;600&family=Nunito:wght@500;800&display=swap">'
)
PAGE = (
    "<!doctype html><html><head><meta charset='utf-8'>" + FONTS
    + "<style>html,body{margin:0}p{margin:0}section{position:relative;box-sizing:border-box;"
    "width:{w}px;height:{h}px;overflow:hidden}aside{display:none}</style></head><body>{body}</body></html>"
)


def shoot(html: str, out: Path, w: int = 1920, h: int = 1080) -> None:
    """Screenshot one page of HTML at w x h into out."""
    page = PAGE.replace("{w}", str(w)).replace("{h}", str(h)).replace("{body}", html)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(page)
    subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={w},{h}",
         "--virtual-time-budget=8000", f"--screenshot={out}", f"file://{f.name}"],
        check=True, capture_output=True,
    )
    Path(f.name).unlink()


def main(deck_dir: Path) -> None:
    project = deck_dir / "project"
    order = json.loads((project / "deck.json").read_text())["order"]
    out_dir = deck_dir.parent / "slides"
    out_dir.mkdir(exist_ok=True)
    for i, sid in enumerate(order, 1):
        out = out_dir / f"{i:02d}-{sid}.png"
        shoot((project / "slides" / f"{sid}.html").read_text(), out)
        print(out.name)


if __name__ == "__main__":
    main(Path(sys.argv[1]))
