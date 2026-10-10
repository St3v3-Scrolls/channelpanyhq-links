"""Builds the channelpanyhq link hubs (links.channelpanyhq.com/<brand>/) from BRANDS below.

Run: python build.py   (writes <brand>/index.html, index.html, 404.html and resized logos into assets/)
Every URL here is a real account or product (taken from Postiz and the brand folders on Z:). Never add a guessed link.
"""
import html
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).parent

BRANDS = {
    "gracetoyou": {
        "name": "By Grace You Are Saved",
        "line": "Daily Scripture, the Gospel and sound doctrine.",
        "logo": r"Z:\scripts\gracetoyou\output\brand\logo_1024.png",
        "bg": "#0A0E1A", "panel": "#1A1F3A", "ink": "#F5F7FA", "muted": "#E0E4ED", "accent": "#D4AF8E",
        "offers": [
            ("Free: 7-Day Scripture Wallpaper Pack", "https://whop.com/gracetoyou/products/7-day-scripture-wallpaper-pack/"),
            ("Verse Card Pack (20 Scripture cards)", "https://whop.com/gracetoyou/products/verse-card-pack-20-scripture-cards/"),
            ("The 30-Day Grace Devotional", "https://whop.com/gracetoyou/products/the-30-day-grace-devotional/"),
            ("Reels B-Roll and Audio Pack (10 clips)", "https://whop.com/gracetoyou/products/reels-b-roll-audio-pack-10-clips/"),
            ("All resources", "https://whop.com/gracetoyou"),
        ],
        "socials": [
            ("Instagram", "https://www.instagram.com/by_grace_you.are_saved/"),
            ("Facebook", "https://www.facebook.com/profile.php?id=100086426433963"),
        ],
    },
    "ironhour": {
        "name": "The Iron Hour",
        "line": "Stoic discipline, one hour at a time.",
        "logo": r"Z:\brands\iron-hour\branding\iron-hour-profile-1024.png",
        "bg": "#0B0B0D", "panel": "#17171A", "ink": "#E8E5DF", "muted": "#9A9DA2", "accent": "#787C82",
        "offers": [],
        "socials": [
            ("YouTube", "https://www.youtube.com/@theironhour_03"),
            ("Instagram", "https://www.instagram.com/the_ironhour/"),
            ("Facebook", "https://www.facebook.com/TheIronHourTV"),
        ],
    },
    "stevescrolls": {
        "name": "Steve Scrolls",
        "line": "What's going viral in gaming, and beyond.",
        "logo": r"Z:\brands\stevescrolls\assets\avatar_master_1024.png",
        "bg": "#05070C", "panel": "#132A52", "ink": "#E8ECF4", "muted": "#A9B6CC", "accent": "#2EC5FF",
        "offers": [],
        "socials": [
            ("YouTube", "https://www.youtube.com/@SteveScrolls"),
            ("TikTok", "https://www.tiktok.com/@steve_scrolls"),
            ("Instagram", "https://www.instagram.com/stevescrolls/"),
            ("Facebook", "https://www.facebook.com/SteveScrollsTV"),
        ],
    },
    "peakmoments": {
        "name": "Peak Moments",
        "line": "Daily viral clips.",
        "logo": r"Z:\brands\peak-moments\assets\peak-moments-profile-pic.png",
        "bg": "#1A0B2E", "panel": "#2E1245", "ink": "#FFFFFF", "muted": "#CDBFDB", "accent": "#00C2CB",
        "offers": [],
        "socials": [
            ("YouTube", "https://www.youtube.com/@WatchPeakMoments"),
            ("TikTok", "https://www.tiktok.com/@peak_momentstv"),
            ("Instagram", "https://www.instagram.com/peak_momentstv/"),
            ("Facebook", "https://www.facebook.com/PeakMomentsTV"),
        ],
    },
    "driftlight": {
        "name": "Driftlight Moments",
        "line": "Ambient scenes and sound for focus, rest and sleep.",
        "logo": r"C:\Claude\ambient-channel\assets\branding\driftlight_moments_profile_800x800.png",
        "bg": "#0E1418", "panel": "#18232A", "ink": "#EAF2F4", "muted": "#A7B8BE", "accent": "#8FC7C2",
        "offers": [],
        "socials": [("YouTube", "https://www.youtube.com/@DriftlightMoments")],
    },
}

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{name}</title>
<meta name="description" content="{line}">
<meta property="og:title" content="{name}">
<meta property="og:description" content="{line}">
<meta property="og:image" content="https://links.channelpanyhq.com/assets/{slug}.png">
<link rel="icon" href="/assets/{slug}.png">
<style>
:root{{--bg:{bg};--panel:{panel};--ink:{ink};--muted:{muted};--accent:{accent}}}
*{{box-sizing:border-box}}
body{{margin:0;min-height:100vh;background:var(--bg);color:var(--ink);font:16px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;display:flex;justify-content:center;padding:48px 16px}}
main{{width:100%;max-width:440px;display:grid;gap:14px;justify-items:center;text-align:center}}
img.logo{{width:104px;height:104px;border-radius:50%;object-fit:cover;border:2px solid var(--accent)}}
h1{{margin:6px 0 0;font-size:1.45rem;letter-spacing:.01em}}
p.line{{margin:0 0 10px;color:var(--muted)}}
a.btn{{display:block;width:100%;padding:14px 18px;border-radius:12px;background:var(--panel);color:var(--ink);text-decoration:none;font-weight:600;border:1px solid color-mix(in srgb,var(--accent) 35%,transparent);transition:transform .12s,border-color .12s}}
a.btn:hover,a.btn:focus-visible{{transform:translateY(-1px);border-color:var(--accent);outline:none}}
a.btn.primary{{background:var(--accent);color:var(--bg);border-color:var(--accent)}}
.label{{width:100%;text-align:left;font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-top:10px}}
.socials{{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;width:100%}}
.socials a{{padding:9px 14px;border-radius:999px;border:1px solid color-mix(in srgb,var(--ink) 25%,transparent);color:var(--ink);text-decoration:none;font-size:.9rem}}
.socials a:hover{{border-color:var(--accent)}}
footer{{margin-top:22px;font-size:.75rem;color:var(--muted)}}
</style>
</head>
<body>
<main>
<img class="logo" src="/assets/{slug}.png" alt="{name} logo" width="104" height="104">
<h1>{name}</h1>
<p class="line">{line}</p>
{offers}
<div class="label">Follow</div>
<div class="socials">{socials}</div>
<footer>{name} · channelpanyhq</footer>
</main>
</body>
</html>
"""


def esc(s):
    return html.escape(s, quote=True)


def build():
    (ROOT / "assets").mkdir(exist_ok=True)
    for slug, b in BRANDS.items():
        img = Image.open(b["logo"]).convert("RGB")
        img.thumbnail((256, 256))
        img.save(ROOT / "assets" / f"{slug}.png", optimize=True)
        offers = ""
        if b["offers"]:
            offers = '<div class="label">Free and paid resources</div>\n' + "\n".join(
                f'<a class="btn{" primary" if i == 0 else ""}" href="{esc(u)}" rel="noopener">{esc(t)}</a>'
                for i, (t, u) in enumerate(b["offers"]))
        if b["offers"]:
            socials = "".join(f'<a href="{esc(u)}" rel="noopener">{esc(t)}</a>' for t, u in b["socials"])
        else:  # no products yet: the profiles are the page, so show them as full buttons
            offers = '<div class="label">Watch and follow</div>\n' + "\n".join(
                f'<a class="btn{" primary" if i == 0 else ""}" href="{esc(u)}" rel="noopener">{esc(t)}</a>'
                for i, (t, u) in enumerate(b["socials"]))
            socials = ""
        page = PAGE if socials else PAGE.replace('<div class="label">Follow</div>\n<div class="socials">{socials}</div>\n', "")
        out = page.format(slug=slug, name=esc(b["name"]), line=esc(b["line"]), offers=offers, socials=socials,
                          **{k: b[k] for k in ("bg", "panel", "ink", "muted", "accent")})
        (ROOT / slug).mkdir(exist_ok=True)
        (ROOT / slug / "index.html").write_text(out, encoding="utf-8")
    items = "".join(f'<a class="btn" href="/{s}/">{esc(b["name"])}</a>' for s, b in BRANDS.items())
    hub = PAGE.format(slug="ironhour", name="channelpanyhq", line="Our channels", offers=items,
                      socials="", bg="#0E1116", panel="#1A1F27", ink="#EEF1F5", muted="#9AA3AF", accent="#5CC0DE")
    hub = hub.replace('<img class="logo" src="/assets/ironhour.png" alt="channelpanyhq logo" width="104" height="104">', "") \
             .replace('<div class="label">Follow</div>\n<div class="socials"></div>', "")
    (ROOT / "index.html").write_text(hub, encoding="utf-8")
    (ROOT / "404.html").write_text(hub.replace("Our channels", "That page doesn't exist. Our channels:"), encoding="utf-8")
    (ROOT / "CNAME").write_text("links.channelpanyhq.com\n", encoding="utf-8")


if __name__ == "__main__":
    build()
    print("built", ", ".join(BRANDS))
