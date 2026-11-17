"""Generates the Outfit Color Matcher page in each language.
Run: python3 _src/gen_color_matcher.py  (from the repo root)"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STYLE = open(os.path.join(ROOT, "_src/color_matcher_style.html")).read()
BASE = "https://ingy9999.github.io"

COLOR_KEYS = ["Black","White","Charcoal","Gray","Light gray","Navy","Beige","Brown","Camel","Olive","Burgundy",
              "Pink","Red","Orange","Yellow","Green","Teal","Light blue","Blue","Purple","Magenta","Denim blue"]

L = {
 "en": dict(path="outfit-color-matcher.html", lang_name="English",
   title="Outfit Color Matcher – Upload a Photo, Find Colors That Go With It",
   desc="Upload a photo of a top or pants and get color suggestions for the other half of your outfit: safe neutrals, matching tones and bold contrasts. Free, and your photo never leaves your device.",
   eyebrow="Free outfit tool", h1="Outfit Color Matcher",
   intro="Upload a photo of a top or a pair of pants. We read its color and suggest colors for the other half of your outfit.",
   nav_size="Japanese size converter", nav_how="How it works",
   step1="1. What do you have?", top_btn="A top", bottom_btn="Pants / skirt",
   step2="2. Add a photo or pick a color", privacy="Your photo is processed in your browser only. It is never uploaded anywhere.",
   drop1="Tap to choose a photo", drop2="or drag and drop it here",
   tap_hint="Wrong color? Tap on the clothing in the photo to pick a different spot.",
   manual="Or pick the color yourself",
   your_top="Your top", your_bottom="Your bottoms",
   res_for_pants="3. Colors for your pants", res_for_top="3. Colors for your top",
   g_neutral="Safe neutrals", g_neutral_sub="Hard to get wrong",
   g_tone="Tone on tone", g_tone_sub="Calm and put-together",
   g_contrast="Contrast", g_add="Add a color", g_contrast_sub="Stands out",
   note="These are suggestions based on color theory, not rules. Personal style always wins.",
   how_title="How it works",
   how=["<strong>Safe neutrals</strong> — black, white, gray, navy, beige and denim work with almost any color.",
        "<strong>Tone on tone</strong> — colors close to yours on the color wheel, made lighter or darker, give a calm, put-together look.",
        "<strong>Contrast</strong> — the opposite color on the color wheel, toned down so it is easy to wear, makes the outfit stand out."],
   footer="Color suggestions are for reference only. Colors in photos can look different depending on lighting and your screen.",
   shop="Shop {c} {item}:", item_pants="pants", item_top="tops", query="{c} {item}", lower=True,
   colors={k:k for k in COLOR_KEYS}),
 "ja": dict(path="ja/outfit-color-matcher.html", lang_name="日本語",
   title="服の色合わせツール｜写真から合う色の服がわかる【無料】",
   desc="トップスやパンツの写真をアップロードすると、その色に合うもう片方の服の色を提案します。定番の無彩色・同系色・反対色の3パターン。写真は端末の外に送信されません。",
   eyebrow="無料のコーディネートツール", h1="服の色合わせツール",
   intro="トップスかパンツの写真を入れると、服の色を読み取って、もう片方に合う色を提案します。",
   nav_size="サイズ換算ツール（英語）", nav_how="使い方と仕組み",
   step1="1. 手持ちの服はどちら？", top_btn="トップス", bottom_btn="パンツ・スカート",
   step2="2. 写真を入れるか、色を選ぶ", privacy="写真はお使いのブラウザの中だけで処理され、どこにも送信されません。",
   drop1="タップして写真を選ぶ", drop2="またはここにドラッグ＆ドロップ",
   tap_hint="色がずれている場合は、写真の服の部分をタップすると、その場所の色で選び直せます。",
   manual="または色を直接選ぶ",
   your_top="あなたのトップス", your_bottom="あなたのボトムス",
   res_for_pants="3. パンツに合う色", res_for_top="3. トップスに合う色",
   g_neutral="定番の無彩色", g_neutral_sub="どんな色とも合わせやすい",
   g_tone="同系色", g_tone_sub="落ち着いた、まとまりのある印象",
   g_contrast="反対色", g_add="差し色", g_contrast_sub="メリハリのある印象",
   note="色の組み合わせの理論にもとづく提案で、決まりではありません。最後は好みで選んでください。",
   how_title="使い方と仕組み",
   how=["<strong>定番の無彩色</strong>：黒・白・グレー・ネイビー・ベージュ・デニムは、ほとんどの色と合わせられます。",
        "<strong>同系色</strong>：色相環で近い色を、明るさを変えて合わせると、落ち着いたまとまりのある印象になります。",
        "<strong>反対色</strong>：色相環の反対側の色を、着やすいように少しくすませて合わせると、メリハリが出ます。"],
   footer="色の提案は参考情報です。写真の色は、照明や画面によって実物と違って見えることがあります。",
   shop="{c}の{item}を探す：", item_pants="パンツ", item_top="トップス", query="{c} {item}", lower=False,
   colors={"Black":"黒","White":"白","Charcoal":"チャコール","Gray":"グレー","Light gray":"ライトグレー","Navy":"ネイビー",
     "Beige":"ベージュ","Brown":"ブラウン","Camel":"キャメル","Olive":"オリーブ","Burgundy":"ボルドー","Pink":"ピンク","Red":"赤",
     "Orange":"オレンジ","Yellow":"イエロー","Green":"グリーン","Teal":"ティール","Light blue":"ライトブルー","Blue":"ブルー",
     "Purple":"パープル","Magenta":"マゼンタ","Denim blue":"デニムブルー"}),
}

SCRIPT = r'''<script>
const T=__T__;
let kind="top";
const $=id=>document.getElementById(id);
function rgb2hsl(r,g,b){r/=255;g/=255;b/=255;const mx=Math.max(r,g,b),mn=Math.min(r,g,b);let h=0,s=0,l=(mx+mn)/2;
 if(mx!==mn){const d=mx-mn;s=l>.5?d/(2-mx-mn):d/(mx+mn);
 h=mx===r?(g-b)/d+(g<b?6:0):mx===g?(b-r)/d+2:(r-g)/d+4;h*=60;}return [h,s*100,l*100];}
function hsl(h,s,l){return `hsl(${Math.round((h%360+360)%360)},${Math.round(s)}%,${Math.round(l)}%)`;}
function hex2rgb(x){return [1,3,5].map(i=>parseInt(x.substr(i,2),16));}
function rgb2hex(r,g,b){return "#"+[r,g,b].map(v=>v.toString(16).padStart(2,"0")).join("");}
function key(h,s,l){
 if(l<15) return "Black"; if(l>90&&s<30) return "White";
 if(s<12) return l<40?"Charcoal":l<70?"Gray":"Light gray";
 if(h>=200&&h<250&&l<30) return "Navy";
 if(h>=20&&h<50&&s<45&&l>55) return "Beige";
 if(h>=15&&h<45&&l<45) return "Brown";
 if(h>=15&&h<45&&s<55) return "Camel";
 if(h>=45&&h<90&&s<45&&l<50) return "Olive";
 if(h<12||h>=345) return l<35?"Burgundy":l>70?"Pink":"Red";
 if(h<40) return "Orange"; if(h<65) return "Yellow"; if(h<160) return "Green";
 if(h<195) return "Teal"; if(h<250) return l>65?"Light blue":"Blue";
 if(h<290) return "Purple"; return l>65?"Pink":"Magenta";}
const neutrals=[["Black",0,0,10],["White",0,0,97],["Gray",0,0,55],["Navy",222,45,22],["Beige",35,35,78],["Denim blue",212,35,45]];
function suggest(h,s,l){
 const out={n:[],t:[],c:[]};
 const isNeutral=s<15||l<15||l>90;
 for(const [nm,nh,ns,nl] of neutrals){
   if(Math.abs(nl-l)<12 && Math.abs(ns-s)<15 && (ns<15||Math.abs(nh-h)<20)) continue;
   out.n.push([nm,nh,ns,nl]); }
 if(!isNeutral){
   const ts=Math.min(s,55);
   const tl=l>50?Math.max(l-35,18):Math.min(l+30,82);
   out.t.push(["",h,ts,tl]); out.t.push(["",h+30,ts*.8,(tl+l)/2]); out.t.push(["",h-30,ts*.8,tl]);
   out.c.push(["",h+180,Math.min(s,45),l>50?30:65]); out.c.push(["",h+150,Math.min(s,40),50]); out.c.push(["",h+210,Math.min(s,40),50]);
 } else {
   for(const ah of [0,30,120,200,280]) out.c.push(["",ah,45,l<50?60:40]);
 }
 return out;}
const AMZ=(()=>{
 let tz="";try{tz=Intl.DateTimeFormat().resolvedOptions().timeZone||"";}catch(e){}
 const byTz=[[/^Asia\/Tokyo/,"co.jp"],[/^Europe\/London/,"co.uk"],[/^Europe\/(Berlin|Vienna|Zurich)/,"de"],[/^Europe\/Paris/,"fr"],
  [/^Europe\/Rome/,"it"],[/^Europe\/Madrid/,"es"],[/^Europe\/Amsterdam/,"nl"],[/^Australia\//,"com.au"],[/^Asia\/(Kolkata|Calcutta)/,"in"],
  [/^Asia\/Singapore/,"sg"],[/^America\/(Toronto|Vancouver|Edmonton|Winnipeg|Halifax|Regina|St_Johns)/,"ca"],
  [/^America\/Mexico_City/,"com.mx"],[/^America\/Sao_Paulo/,"com.br"]];
 for(const [re,d] of byTz) if(re.test(tz)) return "https://www.amazon."+d;
 return "https://www.amazon.com";})();
const cname=k=>T.colors[k]||k;
function card([nm,h,s,l]){
 let c=cname(nm||key(((h%360)+360)%360,s,l)); if(T.lower) c=c.toLowerCase();
 const item=kind==="top"?T.item_pants:T.item_top;
 const q=encodeURIComponent(T.query.replace("{c}",c).replace("{item}",item));
 const title=cname(nm||key(((h%360)+360)%360,s,l));
 return `<div class="card"><div class="c" style="background:${hsl(h,s,l)}"></div><div class="t"><b>${title}</b><span style="font-size:13px;color:var(--muted)">${T.shop.replace("{c}",c).replace("{item}",item)}</span><br><a href="https://www.google.com/search?tbm=shop&q=${q}" target="_blank" rel="noopener">Google Shopping</a> · <a href="${AMZ}/s?k=${q}" target="_blank" rel="noopener">Amazon</a></div></div>`;}
function render(r,g,b){
 const [h,s,l]=rgb2hsl(r,g,b);
 $("pickedSw").style.background=rgb2hex(r,g,b);
 $("pickedTxt").innerHTML=`${kind==="top"?T.your_top:T.your_bottom}: <b>${cname(key(h,s,l))}</b> <span style="color:var(--muted);font-size:13px">${rgb2hex(r,g,b)}</span>`;
 $("manual").value=rgb2hex(r,g,b);
 const sg=suggest(h,s,l);
 const grp=(t,sub,arr)=>arr.length?`<div class="group">${t}<span>${sub}</span></div><div class="grid">${arr.map(card).join("")}</div>`:"";
 $("resTitle").textContent=kind==="top"?T.res_for_pants:T.res_for_top;
 $("results").innerHTML=grp(T.g_neutral,T.g_neutral_sub,sg.n)+grp(T.g_tone,T.g_tone_sub,sg.t)+grp(sg.t.length?T.g_contrast:T.g_add,T.g_contrast_sub,sg.c);
}
let cur=hex2rgb("#2f3e5c");
function update(){render(...cur);}
$("kindSeg").addEventListener("click",e=>{if(!e.target.dataset.k)return;kind=e.target.dataset.k;
 [...e.currentTarget.children].forEach(b=>b.classList.toggle("on",b===e.target));update();});
$("manual").addEventListener("input",e=>{cur=hex2rgb(e.target.value);update();});
const cv=$("preview"),ctx=cv.getContext("2d",{willReadFrequently:true});
function sample(cx,cy,rad){
 const d=ctx.getImageData(Math.max(0,cx-rad),Math.max(0,cy-rad),rad*2,rad*2).data;const px=[];
 for(let i=0;i<d.length;i+=4) px.push([d[i],d[i+1],d[i+2]]);
 return [0,1,2].map(k=>{const v=px.map(p=>p[k]).sort((a,b)=>a-b);return v[v.length>>1];});}
function loadFile(f){if(!f||!f.type.startsWith("image/"))return;const img=new Image();
 img.onload=()=>{const sc=Math.min(1,900/Math.max(img.width,img.height));cv.width=img.width*sc;cv.height=img.height*sc;
  ctx.drawImage(img,0,0,cv.width,cv.height);cv.style.display="block";$("tapHint").style.display="block";
  cur=sample(cv.width>>1,cv.height>>1,Math.round(Math.min(cv.width,cv.height)*.12));update();URL.revokeObjectURL(img.src);};
 img.src=URL.createObjectURL(f);}
$("file").addEventListener("change",e=>loadFile(e.target.files[0]));
const dr=$("drop");["dragover","drop"].forEach(t=>dr.addEventListener(t,e=>{e.preventDefault();if(t==="drop")loadFile(e.dataTransfer.files[0]);}));
cv.addEventListener("click",e=>{const r=cv.getBoundingClientRect();const x=Math.round((e.clientX-r.left)*cv.width/r.width),y=Math.round((e.clientY-r.top)*cv.height/r.height);
 cur=sample(x,y,6);update();});
const sug=document.getElementById("langSuggest");
if(sug){const nl=(navigator.language||"").slice(0,2);const a=sug.querySelector(`a[hreflang="${nl}"]`);if(a&&nl!==document.documentElement.lang)sug.style.display="block",a.style.fontWeight="700";}
update();
</script>'''

def build(code):
    t = L[code]; depth = t["path"].count("/")
    up = "../" * depth
    alts = "\n".join(f'<link rel="alternate" hreflang="{c}" href="{BASE}/{L[c]["path"]}">' for c in L)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{BASE}/{L["en"]["path"]}">'
    switch = " · ".join(
        (f'<b>{L[c]["lang_name"]}</b>' if c == code else f'<a href="{up}{L[c]["path"]}" hreflang="{c}">{L[c]["lang_name"]}</a>')
        for c in L)
    sugg = " · ".join(f'<a href="{up}{L[c]["path"]}" hreflang="{c}">{L[c]["lang_name"]}</a>' for c in L if c != code)
    js_t = {k: t[k] for k in ["your_top","your_bottom","res_for_pants","res_for_top","g_neutral","g_neutral_sub","g_tone","g_tone_sub",
                              "g_contrast","g_add","g_contrast_sub","shop","item_pants","item_top","query","lower","colors"]}
    how = "\n".join(f"    <li>{x}</li>" for x in t["how"])
    html = f'''<!DOCTYPE html>
<html lang="{code}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["title"]}</title>
<link rel="canonical" href="{BASE}/{t["path"]}">
{alts}
<meta name="description" content="{t["desc"]}">
{STYLE}
</head>
<body>
<header>
  <div style="font-size:13px;margin-bottom:14px">🌐 {switch}</div>
  <div id="langSuggest" style="display:none;font-size:14px;background:var(--accent-soft);padding:8px 12px;border-radius:8px;margin-bottom:12px">{sugg}</div>
  <div class="eyebrow">{t["eyebrow"]}</div>
  <h1>{t["h1"]}</h1>
  <p>{t["intro"]}</p>
</header>
<nav>
  <a href="{up}">{t["nav_size"]}</a>
  <a href="#how">{t["nav_how"]}</a>
</nav>
<main>
<section>
  <h2>{t["step1"]}</h2>
  <div class="seg" id="kindSeg">
    <button type="button" data-k="top" class="on">{t["top_btn"]}</button>
    <button type="button" data-k="bottom">{t["bottom_btn"]}</button>
  </div>
  <h2>{t["step2"]}</h2>
  <p class="lead">{t["privacy"]}</p>
  <label class="drop" id="drop" for="file">{t["drop1"]}<br><span style="font-size:13px;color:var(--muted)">{t["drop2"]}</span></label>
  <input type="file" id="file" accept="image/*" style="display:none">
  <canvas id="preview"></canvas>
  <p class="note" id="tapHint" style="display:none">{t["tap_hint"]}</p>
  <div class="row" style="margin-top:14px">
    <div><label for="manual">{t["manual"]}</label><input type="color" id="manual" value="#2f3e5c" style="height:46px;padding:4px"></div>
  </div>
  <div class="picked"><div class="sw" id="pickedSw"></div><div id="pickedTxt"></div></div>
</section>
<section>
  <h2 id="resTitle"></h2>
  <div id="results"></div>
  <p class="note">{t["note"]}</p>
</section>
<section id="how">
  <h2>{t["how_title"]}</h2>
  <ul class="tips">
{how}
  </ul>
</section>
</main>
<footer>{t["footer"]}</footer>
{SCRIPT.replace("__T__", json.dumps(js_t, ensure_ascii=False))}
</body>
</html>'''
    out = os.path.join(ROOT, t["path"]); os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(html)
    return t["path"]

if __name__ == "__main__":
    for c in L: print("wrote", build(c))
