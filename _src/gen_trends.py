"""Generates the weekly Japanese fashion trends pages (English + Japanese).
Content for each week lives in _src/trends/YYYY-MM-DD.json.
The newest week becomes japanese-fashion-trends.html / ja/japanese-fashion-trends.html;
older weeks become archives at trends/YYYY-MM-DD.html / ja/trends/YYYY-MM-DD.html.
Run: python3 _src/gen_trends.py  (from the repo root)"""
import json, os, re, glob, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://ingy9999.github.io"
INDEX = open(os.path.join(ROOT, "index.html")).read()
STYLE = re.search(r"<style>.*?</style>", INDEX, re.S).group(0)
SEP = {"en": ":", "ja": "："}
ACTIVE = ' style="border-color:var(--accent);color:var(--accent)" aria-current="page"'

T = {
 "en": dict(hl="en", cur="japanese-fashion-trends.html", arch="trends/{d}.html",
   title="What's Trending in Japanese Fashion This Week ({d})",
   desc="This week's Japanese fashion trends ({d}): the items, colors, collabs and street styles people in Japan are buying and wearing, with sources and tips for shopping from overseas.",
   eyebrow="Japanese fashion, weekly", h1="What's trending in Japanese fashion this week",
   updated="Updated {d} (JST)", what="What", why="Why", how="Try it from abroad",
   sources="Sources", archive="Past weeks", no_archive="Earlier weeks will be listed here.",
   arch_note="This is an archived edition from {d}.", latest="See this week's trends →",
   nav=[("./", "Japanese size converter"), ("outfit-color-matcher.html", "Outfit color matcher")],
   footer="Trends are summarized from the linked sources. Prices and dates are as reported in Japan and may change.",
   color="outfit-color-matcher.html", size="./", shoes="./#shoes"),
 "ja": dict(hl="ja", cur="ja/japanese-fashion-trends.html", arch="ja/trends/{d}.html",
   title="今週の日本のファッショントレンド（{d}）｜流行アイテム・色・コラボ",
   desc="{d}更新。今週、日本で話題のファッションアイテム、流行色、ブランドのコラボ、着こなしを出典つきでまとめました。",
   eyebrow="毎週更新のファッショントレンド", h1="今週の日本のファッショントレンド",
   updated="{d} 更新", what="流行っているもの", why="人気の理由", how="取り入れ方",
   sources="出典", archive="過去のトレンド", no_archive="過去の週のトレンドはここに追加されます。",
   arch_note="これは{d}時点のアーカイブです。", latest="今週のトレンドを見る →",
   nav=[("outfit-color-matcher.html", "服の色合わせツール")],
   footer="内容はリンク先の情報をもとに要約しています。価格や日程は変更される場合があります。",
   color="outfit-color-matcher.html", size=None, shoes=None),
}

def fmt_date(code, d):
    y, m, dd = d.split("-")
    if code == "ja":
        return f"{y}年{int(m)}月{int(dd)}日"
    months = "January February March April May June July August September October November December".split()
    return f"{months[int(m)-1]} {int(dd)}, {y}"

def esc(s): return html.escape(s, quote=False)

def build(code, d, weeks, is_current):
    t = T[code]
    other = "ja" if code == "en" else "en"
    path = t["cur"] if is_current else t["arch"].format(d=d)
    opath = T[other]["cur"] if is_current else T[other]["arch"].format(d=d)
    depth = path.count("/")
    up = "../" * depth
    # base dir of this language's current page (root for en, ja/ for ja)
    langbase = up + ("ja/" if code == "ja" else "")
    def rel(p): return up + p  # p is repo-relative
    data = json.load(open(os.path.join(ROOT, "_src/trends", d + ".json")))[code]
    fd = fmt_date(code, d)
    link_target = {"color": rel(("ja/" if code == "ja" else "") + t["color"]),
                   "size": rel("") if t["size"] else None, "shoes": rel("#shoes") if t["shoes"] else None}
    if code == "en":
        link_target["size"] = up or "./"
        link_target["shoes"] = (up or "./") + "#shoes"
    items = []
    for i, it in enumerate(data["items"], 1):
        cta = " · ".join(f'<a href="{link_target[k]}">{esc(txt)} →</a>' for k, txt in it["links"] if link_target.get(k))
        src = ", ".join(f'<a href="{html.escape(u)}" target="_blank" rel="noopener">{esc(n)}</a>' for n, u in it["src"])
        items.append(f'''<section id="t{i}">
  <h2>{i}. {esc(it["h"])}</h2>
  <p><strong>{t["what"]}{SEP[code]}</strong> {esc(it["what"])}</p>
  <p><strong>{t["why"]}{SEP[code]}</strong> {esc(it["why"])}</p>
  <p><strong>{t["how"]}{SEP[code]}</strong> {esc(it["how"])}</p>
  {f'<p class="result">{cta}</p>' if cta else ''}
  <p class="note">{t["sources"]}{SEP[code]} {src}</p>
</section>''')
    past = [w for w in weeks if w != weeks[0]]
    if past:
        arch_items = "\n".join(
            f'    <li>{"<b>" + fmt_date(code, w) + "</b>" if (not is_current and w == d) else f"<a href=\"{rel(t["arch"].format(d=w))}\">{fmt_date(code, w)}</a>"}</li>'
            for w in past)
        arch = f'  <ul class="tips">\n{arch_items}\n  </ul>'
    else:
        arch = f'  <p class="lead">{t["no_archive"]}</p>'
    if not is_current:
        arch = f'  <p><a href="{rel(t["cur"])}">{t["latest"]}</a></p>\n' + arch
    banner = "" if is_current else f'\n  <p class="result">{t["arch_note"].format(d=fd)} <a href="{rel(t["cur"])}">{t["latest"]}</a></p>'
    en_href = rel(T["en"]["cur"] if is_current else T["en"]["arch"].format(d=d))
    ja_href = rel(T["ja"]["cur"] if is_current else T["ja"]["arch"].format(d=d))
    sw = (f'<a href="{en_href}" hreflang="en" lang="en"{ACTIVE if code=="en" else ""}>English</a>'
          f'<a href="{ja_href}" hreflang="ja" lang="ja"{ACTIVE if code=="ja" else ""}>日本語</a>')
    enurl = f'{BASE}/{T["en"]["cur"] if is_current else T["en"]["arch"].format(d=d)}'
    jaurl = f'{BASE}/{T["ja"]["cur"] if is_current else T["ja"]["arch"].format(d=d)}'
    nav = "\n".join(f'  <a href="{rel(("ja/" if code == "ja" else "") + p) if p != "./" else (up or "./")}">{esc(n)}</a>' for p, n in t["nav"])
    page = f'''<!DOCTYPE html>
<html lang="{t["hl"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t["title"].format(d=fd))}</title>
<link rel="canonical" href="{BASE}/{path}">
<link rel="alternate" hreflang="en" href="{enurl}">
<link rel="alternate" hreflang="ja" href="{jaurl}">
<link rel="alternate" hreflang="x-default" href="{enurl}">
<meta name="description" content="{html.escape(t["desc"].format(d=fd))}">
{STYLE}
</head>
<body>

<nav aria-label="Language" style="padding-top:20px">
  {sw}
</nav>

<header style="padding-top:20px">
  <div class="eyebrow">{t["eyebrow"]}</div>
  <h1>{t["h1"]}</h1>
  <p><strong>{t["updated"].format(d=fd)}</strong></p>
  <p>{esc(data["intro"])}</p>{banner}
</header>

<nav>
{nav}
</nav>

<main>

{chr(10).join(items)}

<section id="archive">
  <h2>{t["archive"]}</h2>
{arch}
</section>

</main>

<footer>
  {t["footer"]}
</footer>

</body>
</html>
'''
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out) or ROOT, exist_ok=True)
    open(out, "w").write(page)
    return path

def update_sitemap(paths, today):
    """Add any missing URLs to sitemap.xml and set lastmod=today on the current pages and new archives."""
    sm = os.path.join(ROOT, "sitemap.xml"); s = open(sm).read()
    for p in paths:
        loc = f"{BASE}/{p}"
        if f"<loc>{loc}</loc>" in s:
            s = re.sub(rf"(<loc>{re.escape(loc)}</loc><lastmod>)[^<]*(</lastmod>)", rf"\g<1>{today}\g<2>", s)
        else:
            s = s.replace("</urlset>", f"  <url><loc>{loc}</loc><lastmod>{today}</lastmod></url>\n</urlset>")
    open(sm, "w").write(s)

if __name__ == "__main__":
    weeks = sorted((os.path.basename(p)[:-5] for p in glob.glob(os.path.join(ROOT, "_src/trends/*.json"))), reverse=True)
    written = []
    for code in T:
        for w in weeks:
            written.append(build(code, w, weeks, w == weeks[0]))
            print("wrote", written[-1])
    update_sitemap(written, weeks[0])
