"""Build the original, script-free SVG branding. Python standard library only."""

from pathlib import Path
from html import escape
import math

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
PALETTES = {
    "dark": {"bg": "#0b1020", "panel": "#101a30", "line": "#263552", "text": "#f1f5ff", "muted": "#a5b4ce", "cyan": "#67e8f9", "violet": "#b5a1ff", "green": "#73e2b0"},
    "light": {"bg": "#f5f7ff", "panel": "#e9eefc", "line": "#cbd5ed", "text": "#152443", "muted": "#4b607f", "cyan": "#087e94", "violet": "#6d49ca", "green": "#157b55"},
}


def start(width, height, title, desc, p):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<defs><linearGradient id="accent" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="1120" y2="410"><stop stop-color="{p['cyan']}"/><stop offset="1" stop-color="{p['violet']}"/></linearGradient>
<radialGradient id="halo"><stop stop-color="{p['violet']}" stop-opacity=".18"/><stop offset="1" stop-color="{p['violet']}" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".8" fill="{p['muted']}" opacity=".16"/></pattern></defs>
<style>text{{font-family:Inter,'Segoe UI',Arial,sans-serif}}.mono{{font-family:'SFMono-Regular',Consolas,monospace}}.signal{{stroke-dasharray:7 28;animation:flow 12s linear infinite}}.pulse{{transform-box:fill-box;transform-origin:center;animation:pulse 6s ease-in-out infinite}}.orbit{{transform-origin:925px 190px;animation:orbit 36s linear infinite}}@keyframes flow{{to{{stroke-dashoffset:-210}}}}@keyframes pulse{{0%,100%{{opacity:.6}}50%{{opacity:1}}}}@keyframes orbit{{to{{transform:rotate(360deg)}}}}@media(prefers-reduced-motion:reduce){{.signal,.pulse,.orbit{{animation:none!important}}}}</style>
<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="20" fill="{p['bg']}" stroke="{p['line']}"/>
'''


def header(p):
    s = start(740, 410, "Prashant Sharma | AI & ML", "AI and ML undergraduate at MITS Gwalior. Building useful, understandable, and testable AI systems. A separate student-at-laptop animation accompanies this introduction.", p)
    s += f'''<rect x="540" y="1" width="180" height="408" fill="url(#grid)"/>
<circle cx="682" cy="195" r="210" fill="url(#halo)"/>
<path d="M48 41H76" stroke="url(#accent)" stroke-width="3" stroke-linecap="round"/>
<text x="88" y="45" fill="{p['muted']}" font-size="13" letter-spacing="2.2" class="mono">PRASHANT / 787</text>
<text x="47" y="135" fill="{p['text']}" font-size="61" font-weight="750" letter-spacing="-2.2">Prashant Sharma</text>
<text x="49" y="180" fill="{p['muted']}" font-size="22">AI &amp; ML undergraduate · MITS Gwalior</text>
<path d="M49 215H113" stroke="url(#accent)" stroke-width="3" stroke-linecap="round"/>
<text x="48" y="260" fill="{p['text']}" font-size="28" font-weight="500">Building AI that is useful,</text>
<text x="48" y="299" fill="{p['cyan']}" font-size="28" font-weight="500">understandable, and testable.</text>
<text x="49" y="365" fill="{p['muted']}" font-size="12" letter-spacing="1.6" class="mono">PYTHON / MACHINE LEARNING / AI SYSTEMS</text>
<circle cx="659" cy="41" r="4" fill="{p['green']}" class="pulse"/>
<circle cx="679" cy="41" r="4" fill="{p['cyan']}" class="pulse"/>
<circle cx="699" cy="41" r="4" fill="{p['violet']}" class="pulse"/>
'''
    return s + '</svg>\n'


def footer(p):
    s = start(1120, 112, "Built with curiosity. Improved with evidence.", "A quiet animated waveform accompanies the profile's closing line.", p)
    points = " ".join(f"{x},{55 + math.sin((x-785)/22)*math.exp(-((x-915)/105)**2)*24:.2f}" for x in range(790, 1071, 4))
    return s + f'''<text x="34" y="50" fill="{p['text']}" font-size="22" font-weight="600">Built with curiosity. Improved with evidence.</text>
<text x="35" y="78" fill="{p['muted']}" class="mono" font-size="11" letter-spacing="1.6">PRASHANT SHARMA / ALWAYS A WORK IN PROGRESS</text>
<polyline points="{points}" fill="none" stroke="{p['line']}" stroke-width="2"/>
<polyline points="{points}" fill="none" stroke="url(#accent)" stroke-width="2" class="signal"/>
</svg>\n'''


def pending(p):
    s = start(1120, 220, "GitHub activity", "Awaiting the first successful GitHub Actions run. No sample statistics are displayed.", p)
    return s + f'''<text x="32" y="53" fill="{p['text']}" font-size="26" font-weight="650">Consistency, in motion.</text>
<text x="32" y="94" fill="{p['muted']}" font-size="18">A snapshot of my GitHub contribution calendar.</text>
<path d="M32 128H1088" stroke="{p['line']}"/>
<circle cx="39" cy="172" r="5" fill="{p['cyan']}" class="pulse"/>
<text x="57" y="179" fill="{p['muted']}" font-size="17">Activity updates after the first successful workflow run.</text>
</svg>\n'''


def main():
    ASSETS.mkdir(exist_ok=True)
    for theme, p in PALETTES.items():
        (ASSETS / f"header-{theme}.svg").write_text(header(p), encoding="utf-8")
        (ASSETS / f"footer-{theme}.svg").write_text(footer(p), encoding="utf-8")
        # Never replace actual generated activity when rebuilding the branding.
        for label in ["activity"]:
            path = ASSETS / f"{label}-{theme}.svg"
            if not path.exists():
                path.write_text(pending(p), encoding="utf-8")


if __name__ == "__main__":
    main()
