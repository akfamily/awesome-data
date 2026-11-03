"""Build the static site at https://akfamily.xyz/akhub/.

README.md becomes index.html and README.en.md becomes en/index.html, so the
README files stay the only source of content. Run locally with:

    pip install -r .github/scripts/requirements-site.txt
    python .github/scripts/build_site.py
    python -m http.server -d _site 8000
"""

import html
import re
import sys
from pathlib import Path

from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "_site"
REPO = "https://github.com/akfamily/akhub"
SITE = "https://akfamily.xyz/akhub/"

PAGES = [
    {
        "src": "README.md",
        "dst": "index.html",
        "lang": "zh-CN",
        "url": SITE,
        "home": "AKFamily 主页",
        "repo": "GitHub 仓库",
        "edit": "在 GitHub 上编辑",
        "updated": "内容来自仓库的 README，合并到 main 后自动更新。",
        # Relative links in README.md, rewritten for the site.
        "links": {"README.en.md": "en/", "README.md": "./"},
    },
    {
        "src": "README.en.md",
        "dst": "en/index.html",
        "lang": "en",
        "url": SITE + "en/",
        "home": "AKFamily",
        "repo": "GitHub",
        "edit": "Edit on GitHub",
        "updated": "Generated from the repository README and updated on every merge to main.",
        "links": {"README.md": "../", "README.en.md": "./"},
    },
]


def github_slug(text):
    """Heading anchor compatible with GitHub, so README TOC links keep working."""
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def make_renderer(links):
    md = MarkdownIt("commonmark", {"html": False}).enable("table")
    md.use(anchors_plugin, min_level=1, max_level=3, slug_func=github_slug)

    def link_open(self, tokens, idx, options, env):
        token = tokens[idx]
        href = token.attrGet("href") or ""
        if href in links:
            token.attrSet("href", links[href])
        elif re.match(r"^[\w.-]+\.(md|txt)$|^LICENSE$", href):
            token.attrSet("href", f"{REPO}/blob/main/{href}")
        elif href.startswith(("http://", "https://")):
            token.attrSet("target", "_blank")
            token.attrSet("rel", "noopener")
        return self.renderToken(tokens, idx, options, env)

    md.add_render_rule("link_open", link_open)
    return md


TEMPLATE = """<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — AKFamily</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="zh-CN" href="{site}">
  <link rel="alternate" hreflang="en" href="{site}en/">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{url}">
  <link rel="icon" href="/favicon.ico">
  <style>{css}</style>
</head>
<body>
  <header class="nav">
    <div class="wrap nav-inner">
      <a class="brand" href="/"><span class="ak">AK</span>Family</a>
      <nav>
        <a href="/">{home}</a>
        <a href="{repo_url}" target="_blank" rel="noopener">{repo}</a>
      </nav>
    </div>
  </header>
  <main class="wrap content">
{body}
  </main>
  <footer class="footer">
    <div class="wrap">
      <p>{updated} <a href="{repo_url}/edit/main/{src}" target="_blank" rel="noopener">{edit}</a></p>
      <p>© 2019–{year} AKFamily</p>
    </div>
  </footer>
</body>
</html>
"""

CSS = """
:root{--brand:#433dff;--text:#1f2328;--muted:#59636e;--line:#e3e6ea;--bg-alt:#f6f7fb;
font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB",
"Microsoft YaHei",Arial,sans-serif;color:var(--text);line-height:1.75}
*{box-sizing:border-box}html{scroll-padding-top:76px}body{margin:0}
a{color:var(--brand);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:900px;margin:0 auto;padding:0 24px}.ak{color:var(--brand)}
.nav{position:sticky;top:0;z-index:10;background:rgba(255,255,255,.92);
backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.nav-inner{display:flex;align-items:center;justify-content:space-between;height:60px}
.brand{font-size:22px;font-weight:700;color:var(--text)}.brand:hover{text-decoration:none}
.nav nav{display:flex;gap:24px}.nav nav a{color:var(--text);font-size:15px}
.content{padding:32px 24px 48px}
.content h1{font-size:36px;margin:8px 0 8px}
.content h2{font-size:24px;margin:48px 0 16px;padding-bottom:8px;border-bottom:1px solid var(--line)}
.content h1 a,.content h2 a{color:inherit}
.content blockquote{margin:16px 0;padding:12px 18px;background:var(--bg-alt);
border-left:4px solid var(--brand);border-radius:0 8px 8px 0;color:var(--muted)}
.content blockquote p{margin:0}
.content table{border-collapse:collapse;width:100%;font-size:15px}
.content th,.content td{border:1px solid var(--line);padding:8px 12px;text-align:left}
.content th{background:var(--bg-alt)}
.content ul{padding-left:22px}
.content > ul > li{margin:0 0 16px}
.content li > p{margin:0}
.content > ul > li > p:first-child{font-weight:600;font-size:17px}
.content > ul > li > ul{list-style:none;padding-left:0;margin:2px 0 0;color:var(--muted)}
.content > ul > li > ul > li{margin:2px 0}
.content h2#目录 + ul,.content h2#contents + ul{display:flex;flex-wrap:wrap;gap:8px 10px;
list-style:none;padding:0}
.content h2#目录 + ul > li,.content h2#contents + ul > li{margin:0}
.content h2#目录 + ul a,.content h2#contents + ul a{display:block;padding:4px 14px;
border:1px solid var(--line);border-radius:999px;font-size:14px}
.content h2#目录 + ul a:hover,.content h2#contents + ul a:hover{border-color:var(--brand);
text-decoration:none}
code{font-family:Consolas,"SFMono-Regular",Menlo,monospace;font-size:13px;
background:#eef1ff;color:var(--brand);padding:1px 8px;border-radius:999px;margin-right:4px}
pre code{background:none;color:inherit;padding:0}
pre{background:#f3f4f6;padding:12px 16px;border-radius:8px;overflow-x:auto}
.footer{padding:28px 0;text-align:center;font-size:14px;color:var(--muted);
border-top:1px solid var(--line)}.footer p{margin:4px 0}.footer a{color:var(--muted)}
@media (max-width:600px){.wrap{padding:0 16px}.content{padding:24px 16px 40px}
.content h1{font-size:28px}.nav nav{gap:14px}.nav nav a{font-size:14px}}
"""


def first_paragraph(text):
    for block in text.split("\n\n"):
        block = block.strip()
        if block and not block.startswith(("#", ">", "-", "|", "[", "简体中文")):
            return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", block)
    return ""


def main():
    import datetime

    year = datetime.date.today().year
    for page in PAGES:
        text = (ROOT / page["src"]).read_text(encoding="utf-8")
        title = re.search(r"^# (.+)$", text, re.M).group(1).strip()
        body = make_renderer(page["links"]).render(text)
        out = OUT / page["dst"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            TEMPLATE.format(
                lang=page["lang"],
                title=html.escape(title),
                description=html.escape(first_paragraph(text)),
                url=page["url"],
                site=SITE,
                css=CSS,
                home=page["home"],
                repo=page["repo"],
                repo_url=REPO,
                body=body,
                updated=page["updated"],
                edit=page["edit"],
                src=page["src"],
                year=year,
            ),
            encoding="utf-8",
        )
        print(f"built {out.relative_to(ROOT)}")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
