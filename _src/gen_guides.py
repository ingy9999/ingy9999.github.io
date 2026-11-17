"""Generates the English guide pages. Run from repo root: python3 _src/gen_guides.py"""
import os, re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
idx=open(os.path.join(ROOT,"index.html")).read()
STYLE=re.search(r"<style>.*?</style>",idx,re.S).group(0)
BASE="https://ingy9999.github.io"
GUIDES=[
 ("how-to-read-japanese-size-charts.html","How to read a Japanese size chart"),
 ("japanese-clothing-sizes.html","Japanese clothing sizes vs US sizes"),
 ("japanese-shoe-size-chart.html","Japanese shoe size chart"),
 ("how-to-measure-for-japanese-sizes.html","How to measure for Japanese sizes"),
]
def page(fn,title,metatitle,desc,eyebrow,intro,body):
    others="".join(f'<li><a href="{f}">{t}</a></li>' for f,t in GUIDES if f!=fn)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{metatitle}</title>
<link rel="canonical" href="{BASE}/{fn}">
<meta name="description" content="{desc}">
{STYLE}
</head>
<body>
<header>
  <div class="eyebrow">{eyebrow}</div>
  <h1>{title}</h1>
  <p>{intro}</p>
</header>
<nav>
  <a href="./">Size converter tool</a>
  <a href="outfit-color-matcher.html">Outfit color matcher</a>
</nav>
<main>
{body}
<section>
  <h2>More guides</h2>
  <ul class="tips">{others}</ul>
</section>
</main>
<footer>Size conversions are approximate and for reference only. Always check the size chart of the item you are buying.</footer>
</body>
</html>'''

pages={}
# 1. Reading a size chart
terms=[("着丈","kitake","Length","From the top of the shoulder (or back of the collar) to the hem."),
 ("身幅","mihaba","Body width","Straight across the chest, measured flat. Double it for the circumference."),
 ("肩幅","katahaba","Shoulder width","From one shoulder seam to the other."),
 ("袖丈","sodetake","Sleeve length","From the shoulder seam to the end of the cuff."),
 ("裄丈","yukitake","Sleeve length from center back","From the middle of the back of the neck to the cuff. Common for raglan sleeves and knits."),
 ("ウエスト","uesuto","Waist","On pants, usually measured flat across the waistband. Double it."),
 ("ヒップ","hippu","Hip","Often measured flat across the widest part. Double it."),
 ("股上","matagami","Rise","From the crotch seam to the top of the waistband."),
 ("股下","matashita","Inseam","From the crotch seam to the hem of the leg."),
 ("渡り幅","watarihaba","Thigh width","Across the top of the leg, measured flat. Double it."),
 ("裾幅","susohaba","Hem width","Across the leg opening, measured flat. Double it."),
 ("総丈","sōtake","Total length","The full length of pants or a dress.")]
rows="".join(f'<tr><td><span class="jp">{j}</span><span class="rom">{r}</span></td><td><strong>{e}</strong><br>{d}</td></tr>' for j,r,e,d in terms)
pages["how-to-read-japanese-size-charts.html"]=page("how-to-read-japanese-size-charts.html","How to read a Japanese size chart",
 "How to Read a Japanese Size Chart (着丈, 身幅, 肩幅 Explained)",
 "What do 着丈, 身幅, 肩幅 and 股下 mean? A plain-English guide to the terms on Japanese size charts, and why some numbers need to be doubled.",
 "Size guide","Japanese online stores list the measurements of the garment itself, in centimeters and in Japanese. Here is what each term means.",
 f'''<section>
  <h2>The terms you will see</h2>
  <div class="scroll"><table><thead><tr><th>Japanese</th><th>Meaning</th></tr></thead><tbody>{rows}</tbody></table></div>
  <p class="note">Want to convert the numbers? Type them into the <a href="./#translator">size chart translator</a> to see them in inches.</p>
</section>
<section>
  <h2>Why some numbers look too small</h2>
  <p>Many Japanese stores measure clothes laid flat on a table. A measurement like 身幅 (body width) is taken across the front only, so it is half of the full circumference.</p>
  <p>For example, a 身幅 of 55 cm means the chest is about 110 cm (43.3 in) all the way around. The same goes for waist, hip, thigh and hem widths when they are measured flat.</p>
</section>
<section>
  <h2>Garment size is not body size</h2>
  <p>The numbers on a Japanese size chart describe the clothing, not the person wearing it. A shirt with a 110 cm chest is meant to fit someone with a smaller chest, because clothes need room to move. The easiest way to compare is to measure a piece of clothing you already own. See <a href="how-to-measure-for-japanese-sizes.html">how to measure for Japanese sizes</a>.</p>
</section>''')

# 2. Clothing sizes
men=[("S","80–88","31.5–34.6","XS–S"),("M","88–96","34.6–37.8","S–M"),("L","96–104","37.8–40.9","M–L"),("LL (XL)","104–112","40.9–44.1","L")]
wom=[("S","72–80","28.3–31.5","XS"),("M","79–87","31.1–34.3","XS–S"),("L","86–94","33.9–37.0","S–M")]
tb=lambda rs:"".join(f"<tr><td><strong>{a}</strong></td><td>{b} cm</td><td>{c} in</td><td>{d}</td></tr>" for a,b,c,d in rs)
head="<thead><tr><th>Japan</th><th>Chest / bust</th><th>Inches</th><th>Closest US</th></tr></thead>"
pages["japanese-clothing-sizes.html"]=page("japanese-clothing-sizes.html","Japanese clothing sizes vs US sizes",
 "Japanese Clothing Size Chart: S, M, L, LL vs US Sizes",
 "How do Japanese S, M, L and LL compare to US sizes? Body measurements behind Japanese clothing sizes, with a chest-size chart in cm and inches.",
 "Size guide","Most Japanese brands base their sizes on body measurements from the Japanese Industrial Standards (JIS). In practice, Japanese sizes usually run about one size smaller than US sizes.",
 f'''<section>
  <h2>Men's sizes</h2>
  <div class="scroll"><table>{head}<tbody>{tb(men)}</tbody></table></div>
</section>
<section>
  <h2>Women's sizes</h2>
  <div class="scroll"><table>{head}<tbody>{tb(wom)}</tbody></table></div>
  <p class="note">Some brands also offer LL (XL) and larger sizes. Their ranges vary, so check the brand's own chart.</p>
</section>
<section>
  <h2>What this means when you shop</h2>
  <ul class="tips">
    <li><strong>Don't just order your usual letter size.</strong> A Japanese M is often closer to a US S.</li>
    <li><strong>Watch for numbered sizes.</strong> Some Japanese brands use 0, 1, 2 or 1, 2, 3 instead of letters. These do not follow a common standard, so always check the chart.</li>
    <li><strong>UK and EU stores</strong> mostly use similar letter sizes to the US, but numeric EU sizes vary by brand.</li>
    <li><strong>Fit matters more than the label.</strong> An oversized fit can run several sizes larger than the chart suggests.</li>
  </ul>
  <p class="note">Find your size quickly with the <a href="./#clothing">clothing size finder</a>. The US column is approximate and based on common US retail charts.</p>
</section>''')

# 3. Shoe sizes
men_s=[[24.5,6.5,5.5,39],[25,7,6,40],[25.5,7.5,6.5,40.5],[26,8,7,41],[26.5,8.5,7.5,42],[27,9,8,42.5],[27.5,9.5,8.5,43],[28,10,9,44],[28.5,10.5,9.5,44.5],[29,11,10,45],[29.5,11.5,10.5,45.5],[30,12,11,46]]
wom_s=[[22,5,2.5,35],[22.5,5.5,3,35.5],[23,6,3.5,36],[23.5,6.5,4,37],[24,7,4.5,37.5],[24.5,7.5,5,38],[25,8,5.5,38.5],[25.5,8.5,6,39],[26,9,6.5,40]]
fmt=lambda v:("%g"%v)
st=lambda rs:"".join(f"<tr><td><strong>{fmt(a)}</strong></td><td>{fmt(b)}</td><td>{fmt(c)}</td><td>{fmt(d)}</td></tr>" for a,b,c,d in rs)
sh="<thead><tr><th>Japan (cm)</th><th>US</th><th>UK</th><th>EU</th></tr></thead>"
pages["japanese-shoe-size-chart.html"]=page("japanese-shoe-size-chart.html","Japanese shoe size chart",
 "Japanese Shoe Size Chart: cm to US, UK and EU (Men & Women)",
 "Japanese shoe sizes are your foot length in centimeters. Convert JP shoe sizes to US, UK and EU sizes for men and women, with tips for buying shoes from Japan.",
 "Size guide","Japanese shoe sizes are simple: the number is your foot length in centimeters. A 26.5 means a foot about 26.5 cm long.",
 f'''<section>
  <h2>Men's shoe sizes</h2>
  <div class="scroll"><table>{sh}<tbody>{st(men_s)}</tbody></table></div>
</section>
<section>
  <h2>Women's shoe sizes</h2>
  <div class="scroll"><table>{sh}<tbody>{st(wom_s)}</tbody></table></div>
  <p class="note"><strong>Sizes vary by brand.</strong> UK and EU equivalents in particular can differ by half to one size between brands (for example, Nike and adidas use different charts). Use this table as a starting point and check the brand's own chart when it has one.</p>
</section>
<section>
  <h2>How to find your Japanese shoe size</h2>
  <ul class="tips">
    <li><strong>Measure your foot.</strong> Stand on a piece of paper, mark your heel and longest toe, and measure the distance in cm. That is roughly your Japanese size.</li>
    <li><strong>Measure both feet</strong> and use the longer one.</li>
    <li><strong>Check the width.</strong> Japanese sizes also use width codes like E, 2E and 3E. If you have wide feet, look for these on the product page.</li>
  </ul>
  <p class="note">Convert in one tap with the <a href="./#shoes">shoe size converter</a>.</p>
</section>''')

# 4. Measuring
pages["how-to-measure-for-japanese-sizes.html"]=page("how-to-measure-for-japanese-sizes.html","How to measure for Japanese sizes",
 "How to Measure Yourself (and Your Clothes) for Japanese Sizes",
 "The most reliable way to choose a Japanese size: measure a piece of clothing that fits you well, the same way Japanese stores do, and compare.",
 "Size guide","The most reliable way to pick a Japanese size is not your body measurements or your usual label. It is a garment you already own and like the fit of.",
 '''<section>
  <h2>What you need</h2>
  <ul class="tips">
    <li>A shirt, jacket or pair of pants that fits you the way you like</li>
    <li>A tape measure (or a piece of string and a ruler)</li>
    <li>A flat surface like a table or the floor</li>
  </ul>
</section>
<section>
  <h2>Tops: 4 measurements</h2>
  <ul class="tips">
    <li><strong>Length (着丈)</strong> — lay the top flat, front side up. Measure from the highest point of the shoulder down to the hem.</li>
    <li><strong>Body width (身幅)</strong> — measure straight across, from armpit seam to armpit seam.</li>
    <li><strong>Shoulder width (肩幅)</strong> — measure from one shoulder seam to the other.</li>
    <li><strong>Sleeve length (袖丈)</strong> — measure from the shoulder seam to the end of the cuff.</li>
  </ul>
</section>
<section>
  <h2>Pants: 4 measurements</h2>
  <ul class="tips">
    <li><strong>Waist (ウエスト)</strong> — button the pants, lay them flat and measure straight across the top of the waistband.</li>
    <li><strong>Rise (股上)</strong> — from the crotch seam up to the top of the waistband, on the front.</li>
    <li><strong>Inseam (股下)</strong> — from the crotch seam down the inside of the leg to the hem.</li>
    <li><strong>Thigh width (渡り幅)</strong> — straight across the leg, just below the crotch.</li>
  </ul>
</section>
<section>
  <h2>Compare and choose</h2>
  <p>Write your numbers down in centimeters, then compare them with the size chart on the product page. Pick the size whose numbers are closest to yours, especially body width for tops and waist and inseam for pants.</p>
  <p>Remember that flat measurements are half the circumference. Measure your own clothes flat too, so you are comparing like with like.</p>
  <p class="note">Need to switch between cm and inches? Use the <a href="./#cm-inch">cm ⇄ inch converter</a> or the <a href="./#translator">size chart translator</a>.</p>
</section>''')

for fn,html in pages.items():
    open(os.path.join(ROOT,fn),"w").write(html); print("wrote",fn)
