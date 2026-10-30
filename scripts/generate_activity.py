"""Generate two honest activity cards using GitHub's real contribution calendar.

No external Python packages or personal access token are required in Actions.
Fail before writing if the API is unavailable; keep the last successful image.
"""

from datetime import date, datetime, timezone
from html import escape
from pathlib import Path
import json
import os
import re
import urllib.error
import urllib.request

from build_brand import PALETTES, start

ROOT = Path(__file__).resolve().parents[1]
QUERY = """
query ProfileCalendar($login: String!) {
  user(login: $login) {
    contributionsCollection {
      startedAt
      endedAt
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""


def fetch_calendar(username, token):
    if not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?", username):
        raise ValueError("A valid GitHub username is required.")
    if not token:
        raise ValueError("GITHUB_TOKEN is required; use the automatic Actions token.")
    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": username}}).encode(),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "User-Agent": "prashant-profile-assets"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    if payload.get("errors") or not payload.get("data", {}).get("user"):
        raise ValueError("GitHub did not return a valid contribution calendar.")
    return payload["data"]["user"]["contributionsCollection"]


def normalize(collection):
    calendar = collection["contributionCalendar"]
    total = calendar["totalContributions"]
    if not isinstance(total, int) or isinstance(total, bool) or total < 0:
        raise ValueError("Invalid contribution total.")
    days = []
    seen = set()
    for week in calendar["weeks"]:
        for day in week["contributionDays"]:
            stamp = date.fromisoformat(day["date"])
            count = day["contributionCount"]
            if not isinstance(count, int) or isinstance(count, bool) or count < 0:
                raise ValueError("Invalid daily contribution count.")
            if stamp in seen:
                raise ValueError("Duplicate calendar date.")
            seen.add(stamp)
            days.append((stamp, count))
    days.sort()
    if not days or sum(count for _, count in days) != total:
        raise ValueError("Incomplete or inconsistent contribution calendar.")
    if any((b[0]-a[0]).days != 1 for a, b in zip(days, days[1:])):
        raise ValueError("The contribution calendar has missing dates.")
    # Count only what GitHub actually returned. No invented or extrapolated data.
    active = sum(count > 0 for _, count in days)
    busiest = max(count for _, count in days)
    return {"total": total, "active": active, "busiest": busiest, "days": days}


def render(data, p, updated):
    days = data["days"]
    span = f"{days[0][0]:%d %b %Y} – {days[-1][0]:%d %b %Y}"
    s = start(1120, 300, "GitHub contribution activity", f"{data['total']} contributions across {data['active']} active days. Highest daily count: {data['busiest']}. Calendar: {span}. Updated {updated} UTC. Counts follow GitHub's contribution rules.", p)
    s += f'''<text x="32" y="43" fill="{p['text']}" font-size="23" font-weight="650">Consistency, in motion.</text>
<text x="1088" y="42" text-anchor="end" fill="{p['muted']}" font-size="11" class="mono">UPDATED {escape(updated.upper())} UTC</text>
<text x="32" y="71" fill="{p['muted']}" font-size="13">{escape(span)} · GitHub contribution calendar</text>
'''
    for x, key, label in [(32, "total", "CONTRIBUTIONS"), (399, "active", "ACTIVE DAYS"), (766, "busiest", "MOST IN ONE DAY")]:
        s += f'<text x="{x}" y="130" fill="{p["text"]}" font-size="43" font-weight="700">{data[key]:,}</text><text x="{x}" y="157" fill="{p["muted"]}" class="mono" font-size="11" letter-spacing="1.5">{label}</text>\n'
    s += f'<path d="M32 180H1088" stroke="{p["line"]}"/><text x="32" y="204" fill="{p["muted"]}" class="mono" font-size="10" letter-spacing="1.3">DAILY CONTRIBUTIONS / OLDEST → NEWEST</text>\n'
    maximum = max(1, data["busiest"])
    step = 1056 / len(days)
    for i, (stamp, count) in enumerate(days):
        height = 2 + 44 * count / maximum
        s += f'<rect x="{32+i*step:.2f}" y="{265-height:.2f}" width="{max(.5,step-.7):.2f}" height="{height:.2f}" rx=".6" fill="{p["cyan"] if count else p["line"]}" opacity="{.45+.55*count/maximum:.3f}"><title>{stamp.isoformat()}: {count} contributions</title></rect>\n'
    return s + f'<text x="32" y="285" fill="{p["muted"]}" font-size="10">Activity counts reflect GitHub’s contribution rules; they are not a measure of code quality.</text>\n</svg>\n'


def main():
    try:
        collection = fetch_calendar(os.environ.get("PROFILE_USERNAME", ""), os.environ.get("GITHUB_TOKEN", ""))
        data = normalize(collection)
        updated = datetime.now(timezone.utc).strftime("%d %b %Y")
        images = {theme: render(data, p, updated) for theme, p in PALETTES.items()}
        for theme, content in images.items():
            path = ROOT / "assets" / f"activity-{theme}.svg"
            temporary = path.with_suffix(".svg.tmp")
            temporary.write_text(content, encoding="utf-8")
            temporary.replace(path)
        print("Generated activity cards from GitHub's verified calendar response.")
    except (ValueError, KeyError, TypeError, OSError, urllib.error.URLError):
        raise SystemExit("Activity refresh failed. Existing cards were preserved; check API availability and Actions permissions.") from None


if __name__ == "__main__":
    main()
