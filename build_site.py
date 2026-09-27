"""Build a standalone copy of the portfolio for static hosting (ChatGPT Sites, GitHub Pages, etc.).

index.html is written for the Claude Artifact host, which supplies the <!doctype>/<html>/<head>/<body>
wrapper. This script adds that wrapper plus share-preview tags and a favicon, and copies the images
next to the page. Output: site/dist/. Run after every edit:  python build_site.py
"""
from pathlib import Path
import shutil

ROOT = Path(__file__).parent
DIST = ROOT / "site" / "dist"

src = (ROOT / "index.html").read_text(encoding="utf-8")
cut = src.index("</style>") + len("</style>")
head_part, body_part = src[:cut], src[cut:]

favicon = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
    "%3Crect width='64' height='64' rx='14' fill='%232E5BFF'/%3E"
    "%3Ctext x='32' y='42' font-family='Arial,sans-serif' font-size='28' font-weight='700' "
    "text-anchor='middle' fill='white'%3EDQ%3C/text%3E%3C/svg%3E"
)
meta = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta property="og:type" content="website">
<meta property="og:title" content="Daniel Quek">
<meta property="og:description" content="Applied AI and automation on Singapore's public data.">
<meta name="twitter:card" content="summary">
<link rel="icon" href="{favicon}">
"""

html = f"""<!doctype html>
<html lang="en" data-mode="light">
<head>
{meta}{head_part}
</head>
<body>{body_part}
</body>
</html>
"""

if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir(parents=True)
(DIST / "index.html").write_text(html, encoding="utf-8")
for img in (ROOT / "assets").glob("*.jpg"):
    shutil.copy2(img, DIST / img.name)
print("Built", DIST, sorted(p.name for p in DIST.iterdir()))
