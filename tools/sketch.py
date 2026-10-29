"""Whiteboard (Excalidraw-style) drawing helpers for the lesson decks.

A slide = one full-bleed SVG drawing (grid + sketchy shapes) with rounded-sans
text pinned on top, in the Claude Slides format (1920x1080).
"""
from __future__ import annotations

import math
import random

R = random.Random(11)

INK = "#1E1E1E"
GRAY = "#6B7076"
BLUE = "#1971C2"
RED = "#E03131"
ORANGE = "#F08C00"
GREEN_S = "#2F9E44"
YELLOW = "#FFEC99"
LBLUE = "#A5D8FF"
LGREEN = "#B2F2BB"
LRED = "#FFC9C9"
VIOLET = "#D0BFFF"
LORANGE = "#FFD8A8"
PAPER = "#FFFFFF"


def j(a: float = 2.5) -> float:
    return R.uniform(-a, a)


def f(v: float) -> str:
    return f"{v:.1f}"


def line(x1, y1, x2, y2, color=INK, w=3.0, passes=2, dash=False) -> list[str]:
    out = []
    da = ' stroke-dasharray="14 12"' if dash else ""
    for _ in range(passes):
        mx = (x1 + x2) / 2 + j(3)
        my = (y1 + y2) / 2 + j(3)
        out.append(
            f'<path d="M{f(x1 + j())} {f(y1 + j())} Q{f(mx)} {f(my)} {f(x2 + j())} {f(y2 + j())}" '
            f'fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round"{da}/>'
        )
    return out


def rect(x, y, w, h, fill=None, color=INK, sw=3.0, rot=0.0) -> list[str]:
    out = []
    if fill:
        k = 3
        out.append(
            f'<path d="M{f(x + 6 + j(k))} {f(y + j(k))} L{f(x + w - 6 + j(k))} {f(y + j(k))} '
            f'Q{f(x + w)} {f(y)} {f(x + w + j(k))} {f(y + 6)} L{f(x + w + j(k))} {f(y + h - 6)} '
            f'Q{f(x + w)} {f(y + h)} {f(x + w - 6)} {f(y + h + j(k))} L{f(x + 6)} {f(y + h + j(k))} '
            f'Q{f(x)} {f(y + h)} {f(x + j(k))} {f(y + h - 6)} L{f(x + j(k))} {f(y + 6)} Z" fill="{fill}"/>'
        )
    pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    for i in range(4):
        a, b = pts[i], pts[(i + 1) % 4]
        out += line(*a, *b, color=color, w=sw)
    if rot:
        cx, cy = x + w / 2, y + h / 2
        return [f'<g transform="rotate({rot} {f(cx)} {f(cy)})">' + "".join(out) + "</g>"]
    return out


def ellipse(cx, cy, rx, ry, fill=None, color=INK, sw=3.0) -> list[str]:
    out = []
    if fill:
        out.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="{fill}"/>')
    for _ in range(2):
        n = 14
        s = R.uniform(0, 2 * math.pi)
        pts = [
            (cx + (rx + j(3)) * math.cos(s + 2 * math.pi * i / n), cy + (ry + j(3)) * math.sin(s + 2 * math.pi * i / n))
            for i in range(n + 3)
        ]
        d = f"M{f((pts[0][0] + pts[1][0]) / 2)} {f((pts[0][1] + pts[1][1]) / 2)}"
        for i in range(1, len(pts) - 1):
            mx = (pts[i][0] + pts[i + 1][0]) / 2
            my = (pts[i][1] + pts[i + 1][1]) / 2
            d += f" Q{f(pts[i][0])} {f(pts[i][1])} {f(mx)} {f(my)}"
        out.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>')
    return out


def arrow(x1, y1, x2, y2, bend=0.0, color=INK, sw=3.0, dash=False) -> list[str]:
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    nx, ny = -dy / L, dx / L
    cx, cy = (x1 + x2) / 2 + nx * bend, (y1 + y2) / 2 + ny * bend
    da = ' stroke-dasharray="14 12"' if dash else ""
    out = [
        f'<path d="M{f(x1)} {f(y1)} Q{f(cx + j(2))} {f(cy + j(2))} {f(x2)} {f(y2)}" fill="none" '
        f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round"{da}/>'
    ]
    ang = math.atan2(y2 - cy, x2 - cx)
    for s in (1, -1):
        a = ang + math.pi - s * 0.45
        out += line(x2, y2, x2 + 26 * math.cos(a), y2 + 26 * math.sin(a), color=color, w=sw, passes=1)
    return out


def robot(cx, top, scale=1.0, fill=LBLUE) -> list[str]:
    s = scale
    out = []
    out += line(cx, top + 10 * s, cx, top + 45 * s)
    out += ellipse(cx, top, 12 * s, 12 * s, fill=LRED)
    out += rect(cx - 80 * s, top + 45 * s, 160 * s, 125 * s, fill=PAPER)
    out += ellipse(cx - 35 * s, top + 100 * s, 11 * s, 11 * s, fill=INK)
    out += ellipse(cx + 35 * s, top + 100 * s, 11 * s, 11 * s, fill=INK)
    out += line(cx - 30 * s, top + 140 * s, cx + 30 * s, top + 140 * s)
    out += rect(cx - 100 * s, top + 185 * s, 200 * s, 160 * s, fill=fill)
    out += line(cx - 100 * s, top + 220 * s, cx - 160 * s, top + 300 * s)
    out += line(cx + 100 * s, top + 220 * s, cx + 160 * s, top + 300 * s)
    out += line(cx - 50 * s, top + 345 * s, cx - 50 * s, top + 410 * s)
    out += line(cx + 50 * s, top + 345 * s, cx + 50 * s, top + 410 * s)
    return out


def person(cx, top) -> list[str]:
    out = ellipse(cx, top + 55, 55, 55, fill=LORANGE)
    out += line(cx, top + 110, cx, top + 280)
    out += line(cx - 90, top + 170, cx + 90, top + 165)
    out += line(cx, top + 280, cx - 65, top + 410)
    out += line(cx, top + 280, cx + 65, top + 410)
    return out


def svg(alt: str, parts: list[str]) -> str:
    return (
        f'<svg aria-label="{alt}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080" '
        'style="position:absolute;left:0px;top:0px;width:1920px;height:1080px">'
        '<defs><pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse">'
        '<path d="M40 0H0V40" fill="none" stroke="#E9ECEF" stroke-width="1.5"/></pattern></defs>'
        '<rect width="1920" height="1080" fill="#FCFCFA"/><rect width="1920" height="1080" fill="url(#g)"/>'
        + "".join(parts)
        + "</svg>"
    )


def T(x, y, w, text, size=40, font="Kalam", weight=400, color=INK, align="left", lh=1.2) -> str:
    # Rounded sans: Caveat notes -> Fredoka (a bit smaller, it runs wider); Kalam text -> Nunito.
    if font == "Caveat":
        font, size, weight = "Fredoka", round(size * 0.78), 500
    else:
        font, weight = "Nunito", (800 if weight >= 700 else 500)
    return (
        f'<p style="position:absolute;left:{x}px;top:{y}px;width:{w}px;'
        f"font-family:'{font}', Verdana, sans-serif;font-size:{size}px;font-weight:{weight};line-height:{lh};"
        f'color:{color};text-align:{align}">{text}</p>'
    )


def heading(text: str, under: int) -> tuple[list[str], str]:
    under = min(1640, round(len(text) * 0.43 * 88))
    head = T(128, 100, 1664, text, 88, weight=700).replace("'Nunito'", "'Fredoka'").replace("font-weight:800", "font-weight:600")
    return line(132, 212, 132 + under, 208, color=ORANGE, w=7, passes=2), head


def label(x, y, w, h, text, size=40, weight=700) -> str:
    return T(x, y + h / 2 - size * 0.62, w, text, size, weight=weight, align="center")


def section(sid: str, alt: str, parts: list[str], texts: list[str], notes: str) -> str:
    return (
        f'<section id="{sid}" data-transition="fade" style="background:#FCFCFA;color:{INK};'
        "font-family:'Nunito', sans-serif;padding:128px;display:flex;flex-direction:column\">\n"
        + svg(alt, parts)
        + "\n"
        + "\n".join(texts)
        + f"\n<aside>{notes}</aside>\n</section>\n"
    )


