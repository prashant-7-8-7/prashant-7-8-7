"""Build self-hosted contact buttons, technology badges, and a typing ribbon.

Uses checked-in Simple Icons artwork (CC0-1.0) and Python's standard library.
No hosted badge service, API key, or JavaScript is needed to view the profile.
"""

from html import escape
from pathlib import Path
import json
import xml.etree.ElementTree as ET

from build_brand import PALETTES

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ICONS = json.loads((Path(__file__).parent / "icon_sources.json").read_text(encoding="utf-8"))["icons"]
NS = {"svg": "http://www.w3.org/2000/svg"}


def icon(slug, x, y, size, color):
    root = ET.fromstring(ICONS[slug])
    paths = root.findall(".//svg:path", NS)
    if not paths:
        raise ValueError(f"No icon path for {slug}")
    shape = "".join(f'<path d="{escape(node.attrib["d"], quote=True)}"/>' for node in paths)
    return f'<g transform="translate({x} {y}) scale({size/24:.5f})" fill="{color}">{shape}</g>'


def svg_start(width, height, title, description):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>
'''


def tech_badge(label, slug, color):
    width = max(94, 51 + len(label) * 7)
    s = svg_start(width, 34, label, f"{label} — used in projects or coursework; this badge does not represent a proficiency score.")
    s += f'<rect x=".5" y=".5" width="{width-1}" height="33" rx="9" fill="#101a30" stroke="#33415e"/>\n'
    s += icon(slug, 11, 7, 20, color)
    s += f'<text x="40" y="22" fill="#f1f5ff" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="12" font-weight="550">{escape(label)}</text>\n</svg>\n'
    return s


def contact_badge(label, slug, color):
    s = svg_start(156, 44, label, f"{label} contact button for Prashant Sharma. The surrounding README link provides the destination.")
    s += f'<rect x=".5" y=".5" width="155" height="43" rx="11" fill="{color}" stroke="#ffffff" stroke-opacity=".18"/>\n'
    if slug == "linkedin":
        # A typographic LinkedIn mark; the upstream Simple Icons set omits it.
        s += '<rect x="13" y="11" width="23" height="23" rx="3" fill="#ffffff"/><text x="15" y="29" fill="#0a66c2" font-family="Arial,sans-serif" font-size="20" font-weight="bold">in</text>\n'
    else:
        s += icon(slug, 13, 10, 24, "#ffffff")
    s += f'<text x="49" y="27" fill="#ffffff" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="14" font-weight="600">{escape(label)}</text>\n</svg>\n'
    return s


def typing_ribbon(p):
    lines = ["AI & ML student. Practical builder.", "Exploring trustworthy AI and retrieval.", "Learning by building and testing."]
    s = svg_start(880, 56, "Prashant's current focus", "Rotating focus: AI and ML student; trustworthy AI and retrieval; learning by building and testing. With reduced motion enabled, the first line remains visible.")
    s += f'''<style>
.mono{{font-family:'SFMono-Regular',Consolas,'Liberation Mono',monospace;font-size:22px}}
.line{{opacity:0}}.one{{opacity:1;animation:first 15s linear infinite}}.two{{animation:second 15s linear infinite}}.three{{animation:third 15s linear infinite}}
.typed{{animation:type 5s steps(38,end) infinite}}
@keyframes type{{0%,4%{{width:0}}28%,76%{{width:760px}}96%,100%{{width:0}}}}
@keyframes first{{0%,32%{{opacity:1}}33%,100%{{opacity:0}}}}
@keyframes second{{0%,32%{{opacity:0}}33%,65%{{opacity:1}}66%,100%{{opacity:0}}}}
@keyframes third{{0%,65%{{opacity:0}}66%,99%{{opacity:1}}100%{{opacity:0}}}}
@media(prefers-reduced-motion:reduce){{.line,.typed{{animation:none!important}}.line{{opacity:0}}.one{{opacity:1}}.typed{{width:760px}}}}
</style>
<defs><clipPath id="typing"><rect x="50" y="5" width="760" height="46" class="typed"/></clipPath></defs>
<rect x=".5" y=".5" width="879" height="55" rx="11" fill="{p['bg']}" stroke="{p['line']}"/>
<text x="20" y="35" class="mono" fill="{p['green']}">&gt;</text>
<g clip-path="url(#typing)">
'''
    for cls, text, color in zip(["one", "two", "three"], lines, [p["cyan"], p["violet"], p["green"]]):
        s += f'<text x="50" y="35" class="mono line {cls}" fill="{color}">{escape(text)}</text>\n'
    return s + '</g>\n</svg>\n'


def main():
    ASSETS.mkdir(exist_ok=True)
    tools = [
        ("Python", "python", "#75b9ed"), ("C++", "cplusplus", "#8cc5ff"),
        ("JavaScript", "javascript", "#f7df1e"), ("SQLite", "sqlite", "#80c9ec"),
        ("scikit-learn", "scikitlearn", "#ffb569"), ("pandas", "pandas", "#bfadff"),
        ("NumPy", "numpy", "#7ecbdf"), ("FastAPI", "fastapi", "#61dcb6"),
        ("Streamlit", "streamlit", "#ff7a86"), ("Git", "git", "#ff8a72"),
        ("GitHub", "github", "#eef2ff"), ("Flutter", "flutter", "#69d3ff"),
    ]
    for label, slug, color in tools:
        (ASSETS / f"tool-{slug}.svg").write_text(tech_badge(label, slug, color), encoding="utf-8")
    contacts = [("LinkedIn", "linkedin", "#0a66c2"), ("DEV.to", "devdotto", "#171c27"), ("Email me", "gmail", "#654ab3")]
    for label, slug, color in contacts:
        filename = {"linkedin": "linkedin", "devdotto": "dev", "gmail": "email"}[slug]
        (ASSETS / f"contact-{filename}.svg").write_text(contact_badge(label, slug, color), encoding="utf-8")
    for theme, p in PALETTES.items():
        (ASSETS / f"focus-{theme}.svg").write_text(typing_ribbon(p), encoding="utf-8")


if __name__ == "__main__":
    main()
