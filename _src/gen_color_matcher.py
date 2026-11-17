"""Generates the Outfit Color Matcher page in each language.
Run: python3 _src/gen_color_matcher.py  (from the repo root)"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STYLE = open(os.path.join(ROOT, "_src/color_matcher_style.html")).read()
BASE = "https://ingy9999.github.io"

COLOR_KEYS = ["Black","White","Charcoal","Gray","Light gray","Navy","Beige","Brown","Camel","Olive","Burgundy",
              "Pink","Red","Orange","Yellow","Green","Teal","Light blue","Blue","Purple","Magenta","Denim blue"]

L = {
 "en": dict(path="outfit-color-matcher.html", hl="en", lang_name="English",
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
 "ja": dict(path="ja/outfit-color-matcher.html", hl="ja", lang_name="日本語",
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

 "zh": dict(path="zh/outfit-color-matcher.html", hl="zh-Hans", lang_name="简体中文",
   title="服装配色工具｜上传照片，找到相配的衣服颜色【免费】",
   desc="上传上衣或裤子的照片，即可获得另一半搭配的颜色建议：百搭的无彩色、同色系和撞色。完全免费，照片不会离开你的设备。",
   eyebrow="免费穿搭工具", h1="服装配色工具",
   intro="上传一张上衣或裤子的照片，我们会识别它的颜色，并推荐适合搭配的另一半衣服的颜色。",
   nav_size="日本尺码换算工具（英文）", nav_how="使用方法与原理",
   step1="1. 你手上的是哪一件？", top_btn="上衣", bottom_btn="裤子 / 裙子",
   step2="2. 上传照片或选择颜色", privacy="照片只在你的浏览器中处理，不会上传到任何地方。",
   drop1="点击选择照片", drop2="或将照片拖放到这里",
   tap_hint="颜色不对？点击照片中衣服的位置，即可重新选取颜色。",
   manual="或者直接选择颜色",
   your_top="你的上衣", your_bottom="你的下装",
   res_for_pants="3. 适合搭配的裤子颜色", res_for_top="3. 适合搭配的上衣颜色",
   g_neutral="百搭无彩色", g_neutral_sub="几乎不会出错",
   g_tone="同色系", g_tone_sub="沉稳、协调",
   g_contrast="撞色", g_add="点缀色", g_contrast_sub="醒目、有层次",
   note="以上是基于色彩理论的建议，并非规则。最终请按照自己的喜好选择。",
   how_title="使用方法与原理",
   how=["<strong>百搭无彩色</strong>：黑、白、灰、藏青、米色和牛仔色几乎可以搭配任何颜色。",
        "<strong>同色系</strong>：选择色相环上相近的颜色，并调整深浅，能营造沉稳协调的感觉。",
        "<strong>撞色</strong>：选择色相环上相对的颜色，并适当降低鲜艳度，让整体更醒目又不难驾驭。"],
   footer="颜色建议仅供参考。照片中的颜色可能因光线和屏幕不同而与实物有差异。",
   shop="搜索{c}{item}：", item_pants="裤子", item_top="上衣", query="{c}{item}", lower=False,
   colors={"Black":"黑色","White":"白色","Charcoal":"炭灰色","Gray":"灰色","Light gray":"浅灰色","Navy":"藏青色",
     "Beige":"米色","Brown":"棕色","Camel":"驼色","Olive":"橄榄绿","Burgundy":"酒红色","Pink":"粉色","Red":"红色",
     "Orange":"橙色","Yellow":"黄色","Green":"绿色","Teal":"青绿色","Light blue":"浅蓝色","Blue":"蓝色",
     "Purple":"紫色","Magenta":"洋红色","Denim blue":"牛仔蓝"}),
 "ko": dict(path="ko/outfit-color-matcher.html", hl="ko", lang_name="한국어",
   title="옷 색깔 매칭 도구｜사진으로 어울리는 옷 색깔 찾기【무료】",
   desc="상의나 바지 사진을 올리면 나머지 한쪽에 어울리는 색깔을 추천해 드립니다. 무난한 무채색, 같은 계열 색, 보색의 3가지. 무료이며 사진은 기기 밖으로 전송되지 않습니다.",
   eyebrow="무료 코디 도구", h1="옷 색깔 매칭 도구",
   intro="상의나 바지 사진을 올리면 옷의 색깔을 읽어서, 나머지 한쪽에 어울리는 색깔을 추천해 드립니다.",
   nav_size="일본 사이즈 변환 도구(영어)", nav_how="사용 방법과 원리",
   step1="1. 가지고 있는 옷은 어느 쪽인가요?", top_btn="상의", bottom_btn="바지 / 치마",
   step2="2. 사진을 올리거나 색깔을 고르세요", privacy="사진은 브라우저 안에서만 처리되며, 어디에도 업로드되지 않습니다.",
   drop1="탭해서 사진 선택", drop2="또는 여기로 끌어다 놓기",
   tap_hint="색깔이 다르게 나왔나요? 사진 속 옷 부분을 탭하면 그 위치의 색깔로 다시 고를 수 있습니다.",
   manual="또는 색깔을 직접 고르기",
   your_top="내 상의", your_bottom="내 하의",
   res_for_pants="3. 바지에 어울리는 색깔", res_for_top="3. 상의에 어울리는 색깔",
   g_neutral="무난한 무채색", g_neutral_sub="어떤 색과도 잘 어울림",
   g_tone="같은 계열 색", g_tone_sub="차분하고 정돈된 느낌",
   g_contrast="보색", g_add="포인트 색", g_contrast_sub="눈에 띄는 느낌",
   note="색채 이론에 근거한 추천이며, 정답은 아닙니다. 마지막은 취향대로 고르세요.",
   how_title="사용 방법과 원리",
   how=["<strong>무난한 무채색</strong>: 블랙, 화이트, 그레이, 네이비, 베이지, 데님은 거의 모든 색과 어울립니다.",
        "<strong>같은 계열 색</strong>: 색상환에서 가까운 색을 밝기를 달리해서 맞추면 차분하고 정돈된 느낌이 됩니다.",
        "<strong>보색</strong>: 색상환의 반대쪽 색을 입기 쉽게 채도를 낮춰서 맞추면 포인트가 생깁니다."],
   footer="색깔 추천은 참고용입니다. 사진 속 색깔은 조명이나 화면에 따라 실제와 다르게 보일 수 있습니다.",
   shop="{c} {item} 찾기:", item_pants="바지", item_top="상의", query="{c} {item}", lower=False,
   colors={"Black":"블랙","White":"화이트","Charcoal":"차콜","Gray":"그레이","Light gray":"라이트 그레이","Navy":"네이비",
     "Beige":"베이지","Brown":"브라운","Camel":"카멜","Olive":"올리브","Burgundy":"버건디","Pink":"핑크","Red":"레드",
     "Orange":"오렌지","Yellow":"옐로","Green":"그린","Teal":"틸","Light blue":"라이트 블루","Blue":"블루",
     "Purple":"퍼플","Magenta":"마젠타","Denim blue":"데님 블루"}),
 "fr": dict(path="fr/outfit-color-matcher.html", hl="fr", lang_name="Français",
   title="Assortir les couleurs de vos vêtements – à partir d'une photo (gratuit)",
   desc="Envoyez la photo d'un haut ou d'un pantalon et recevez des idées de couleurs pour l'autre moitié de votre tenue : neutres, ton sur ton et contrastes. Gratuit, et votre photo reste sur votre appareil.",
   eyebrow="Outil de style gratuit", h1="Assortir les couleurs de vos vêtements",
   intro="Ajoutez la photo d'un haut ou d'un pantalon. Nous détectons sa couleur et vous proposons des couleurs pour l'autre moitié de votre tenue.",
   nav_size="Convertisseur de tailles japonaises (anglais)", nav_how="Fonctionnement",
   step1="1. Quel vêtement avez-vous ?", top_btn="Un haut", bottom_btn="Pantalon / jupe",
   step2="2. Ajoutez une photo ou choisissez une couleur", privacy="Votre photo est traitée uniquement dans votre navigateur. Elle n'est envoyée nulle part.",
   drop1="Touchez pour choisir une photo", drop2="ou glissez-la ici",
   tap_hint="La couleur n'est pas la bonne ? Touchez le vêtement sur la photo pour choisir un autre endroit.",
   manual="Ou choisissez la couleur vous-même",
   your_top="Votre haut", your_bottom="Votre bas",
   res_for_pants="3. Couleurs pour votre pantalon", res_for_top="3. Couleurs pour votre haut",
   g_neutral="Les neutres", g_neutral_sub="Difficile de se tromper",
   g_tone="Ton sur ton", g_tone_sub="Harmonieux et sobre",
   g_contrast="Contraste", g_add="Une touche de couleur", g_contrast_sub="Qui se remarque",
   note="Ce sont des suggestions fondées sur la théorie des couleurs, pas des règles. Votre style a toujours le dernier mot.",
   how_title="Fonctionnement",
   how=["<strong>Les neutres</strong> : noir, blanc, gris, bleu marine, beige et denim vont avec presque toutes les couleurs.",
        "<strong>Ton sur ton</strong> : des couleurs proches de la vôtre sur le cercle chromatique, plus claires ou plus foncées, donnent une allure harmonieuse.",
        "<strong>Contraste</strong> : la couleur opposée sur le cercle chromatique, adoucie pour être facile à porter, fait ressortir la tenue."],
   footer="Les suggestions de couleurs sont données à titre indicatif. Les couleurs d'une photo peuvent varier selon l'éclairage et l'écran.",
   shop="Chercher un {item} {c} :", item_pants="pantalon", item_top="haut", query="{item} {c}", lower=True,
   colors={"Black":"Noir","White":"Blanc","Charcoal":"Anthracite","Gray":"Gris","Light gray":"Gris clair","Navy":"Bleu marine",
     "Beige":"Beige","Brown":"Marron","Camel":"Camel","Olive":"Olive","Burgundy":"Bordeaux","Pink":"Rose","Red":"Rouge",
     "Orange":"Orange","Yellow":"Jaune","Green":"Vert","Teal":"Bleu canard","Light blue":"Bleu clair","Blue":"Bleu",
     "Purple":"Violet","Magenta":"Magenta","Denim blue":"Bleu jean"}),
 "es": dict(path="es/outfit-color-matcher.html", hl="es", lang_name="Español",
   title="Combinar colores de ropa: sube una foto y descubre qué colores van bien (gratis)",
   desc="Sube la foto de una prenda de arriba o de un pantalón y recibe ideas de colores para la otra mitad de tu look: neutros, tonos similares y contrastes. Gratis, y tu foto no sale de tu dispositivo.",
   eyebrow="Herramienta de moda gratuita", h1="Combinar colores de ropa",
   intro="Sube la foto de una prenda de arriba o de un pantalón. Detectamos su color y te sugerimos colores para la otra mitad de tu look.",
   nav_size="Conversor de tallas japonesas (inglés)", nav_how="Cómo funciona",
   step1="1. ¿Qué prenda tienes?", top_btn="Prenda de arriba", bottom_btn="Pantalón / falda",
   step2="2. Sube una foto o elige un color", privacy="Tu foto se procesa solo en tu navegador. No se sube a ningún sitio.",
   drop1="Toca para elegir una foto", drop2="o arrástrala aquí",
   tap_hint="¿El color no es correcto? Toca la prenda en la foto para elegir otro punto.",
   manual="O elige el color tú mismo",
   your_top="Tu prenda de arriba", your_bottom="Tu prenda de abajo",
   res_for_pants="3. Colores para tu pantalón", res_for_top="3. Colores para tu prenda de arriba",
   g_neutral="Neutros seguros", g_neutral_sub="Difícil equivocarse",
   g_tone="Tonos similares", g_tone_sub="Tranquilo y armonioso",
   g_contrast="Contraste", g_add="Un toque de color", g_contrast_sub="Llama la atención",
   note="Son sugerencias basadas en la teoría del color, no reglas. Al final, manda tu estilo.",
   how_title="Cómo funciona",
   how=["<strong>Neutros seguros</strong>: negro, blanco, gris, azul marino, beige y vaquero combinan con casi cualquier color.",
        "<strong>Tonos similares</strong>: colores cercanos al tuyo en el círculo cromático, más claros u oscuros, dan un look tranquilo y armonioso.",
        "<strong>Contraste</strong>: el color opuesto en el círculo cromático, suavizado para que sea fácil de llevar, hace que el look destaque."],
   footer="Las sugerencias de color son solo orientativas. Los colores de una foto pueden variar según la luz y la pantalla.",
   shop="Buscar {item} color {c}:", item_pants="pantalón", item_top="camiseta", query="{item} color {c}", lower=True,
   colors={"Black":"Negro","White":"Blanco","Charcoal":"Gris marengo","Gray":"Gris","Light gray":"Gris claro","Navy":"Azul marino",
     "Beige":"Beige","Brown":"Marrón","Camel":"Camel","Olive":"Verde oliva","Burgundy":"Burdeos","Pink":"Rosa","Red":"Rojo",
     "Orange":"Naranja","Yellow":"Amarillo","Green":"Verde","Teal":"Verde azulado","Light blue":"Azul claro","Blue":"Azul",
     "Purple":"Morado","Magenta":"Magenta","Denim blue":"Azul vaquero"}),
 "it": dict(path="it/outfit-color-matcher.html", hl="it", lang_name="Italiano",
   title="Abbinare i colori dei vestiti: carica una foto e scopri i colori giusti (gratis)",
   desc="Carica la foto di una maglia o di un pantalone e ricevi idee di colore per l'altra metà del tuo outfit: neutri, tono su tono e contrasti. Gratis, e la foto non lascia il tuo dispositivo.",
   eyebrow="Strumento di stile gratuito", h1="Abbinare i colori dei vestiti",
   intro="Carica la foto di una maglia o di un pantalone. Riconosciamo il colore e ti suggeriamo i colori per l'altra metà del tuo outfit.",
   nav_size="Convertitore di taglie giapponesi (inglese)", nav_how="Come funziona",
   step1="1. Che capo hai?", top_btn="Una maglia", bottom_btn="Pantaloni / gonna",
   step2="2. Aggiungi una foto o scegli un colore", privacy="La foto viene elaborata solo nel tuo browser. Non viene caricata da nessuna parte.",
   drop1="Tocca per scegliere una foto", drop2="oppure trascinala qui",
   tap_hint="Il colore non è giusto? Tocca il capo nella foto per scegliere un altro punto.",
   manual="Oppure scegli tu il colore",
   your_top="La tua maglia", your_bottom="I tuoi pantaloni",
   res_for_pants="3. Colori per i tuoi pantaloni", res_for_top="3. Colori per la tua maglia",
   g_neutral="Neutri sicuri", g_neutral_sub="Difficile sbagliare",
   g_tone="Tono su tono", g_tone_sub="Armonioso e ordinato",
   g_contrast="Contrasto", g_add="Un tocco di colore", g_contrast_sub="Si fa notare",
   note="Sono suggerimenti basati sulla teoria dei colori, non regole. Alla fine decide il tuo stile.",
   how_title="Come funziona",
   how=["<strong>Neutri sicuri</strong>: nero, bianco, grigio, blu navy, beige e denim stanno bene con quasi tutti i colori.",
        "<strong>Tono su tono</strong>: colori vicini al tuo sul cerchio cromatico, più chiari o più scuri, danno un look armonioso.",
        "<strong>Contrasto</strong>: il colore opposto sul cerchio cromatico, ammorbidito per essere facile da indossare, fa risaltare l'outfit."],
   footer="I suggerimenti di colore sono solo indicativi. I colori di una foto possono variare in base alla luce e allo schermo.",
   shop="Cerca {item} colore {c}:", item_pants="pantaloni", item_top="maglia", query="{item} colore {c}", lower=True,
   colors={"Black":"Nero","White":"Bianco","Charcoal":"Antracite","Gray":"Grigio","Light gray":"Grigio chiaro","Navy":"Blu navy",
     "Beige":"Beige","Brown":"Marrone","Camel":"Cammello","Olive":"Verde oliva","Burgundy":"Bordeaux","Pink":"Rosa","Red":"Rosso",
     "Orange":"Arancione","Yellow":"Giallo","Green":"Verde","Teal":"Verde petrolio","Light blue":"Azzurro","Blue":"Blu",
     "Purple":"Viola","Magenta":"Magenta","Denim blue":"Blu denim"}),
}

SCRIPT = r'''<script>
const T=__T__;
const AQ=__AQ__;
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
 let d="com";for(const [re,dd] of byTz) if(re.test(tz)){d=dd;break;}
 const ql={"co.jp":"ja","fr":"fr","es":"es","com.mx":"es","it":"it"}[d]||"en";
 return {url:"https://www.amazon."+d, ql};})();
const cname=k=>T.colors[k]||k;
function aq(k,item){const Q=AQ[AMZ.ql]; let c=Q.colors[k]||k; if(Q.lower) c=c.toLowerCase();
 const it=kind==="top"?Q.item_pants:Q.item_top; return encodeURIComponent(Q.query.replace("{c}",c).replace("{item}",it));}
function card([nm,h,s,l]){
 let c=cname(nm||key(((h%360)+360)%360,s,l)); if(T.lower) c=c.toLowerCase();
 const item=kind==="top"?T.item_pants:T.item_top;
 const q=encodeURIComponent(T.query.replace("{c}",c).replace("{item}",item));
 const title=cname(nm||key(((h%360)+360)%360,s,l));
 return `<div class="card"><div class="c" style="background:${hsl(h,s,l)}"></div><div class="t"><b>${title}</b><span style="font-size:13px;color:var(--muted)">${T.shop.replace("{c}",c).replace("{item}",item)}</span><br><a href="https://www.google.com/search?tbm=shop&q=${q}" target="_blank" rel="noopener">Google Shopping</a> · <a href="${AMZ.url}/s?k=${aq(nm||key(((h%360)+360)%360,s,l),item)}" target="_blank" rel="noopener">Amazon</a></div></div>`;}
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
if(sug){const nl=(navigator.language||"").slice(0,2);const a=[...sug.querySelectorAll("a")].find(x=>x.hreflang.slice(0,2)===nl);if(a&&nl!==document.documentElement.lang.slice(0,2)){sug.innerHTML="";sug.appendChild(a);sug.style.display="block";}}
update();
</script>'''

AQ = {c: {k: L[c][k] for k in ["colors","item_pants","item_top","query","lower"]} for c in ["en","ja","fr","es","it"]}

def build(code):
    t = L[code]; depth = t["path"].count("/")
    up = "../" * depth
    alts = "\n".join(f'<link rel="alternate" hreflang="{L[c]["hl"]}" href="{BASE}/{L[c]["path"]}">' for c in L)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{BASE}/{L["en"]["path"]}">'
    items = "".join(
        (f'<li><b>{L[c]["lang_name"]}</b></li>' if c == code else f'<li><a href="{up}{L[c]["path"]}" hreflang="{L[c]["hl"]}" lang="{L[c]["hl"]}">{L[c]["lang_name"]}</a></li>')
        for c in L)
    switch = f'<details class="lang"><summary>🌐 {t["lang_name"]}</summary><ul>{items}</ul></details>'
    sugg = " · ".join(f'<a href="{up}{L[c]["path"]}" hreflang="{L[c]["hl"]}">{L[c]["lang_name"]}</a>' for c in L if c != code)
    js_t = {k: t[k] for k in ["your_top","your_bottom","res_for_pants","res_for_top","g_neutral","g_neutral_sub","g_tone","g_tone_sub",
                              "g_contrast","g_add","g_contrast_sub","shop","item_pants","item_top","query","lower","colors"]}
    how = "\n".join(f"    <li>{x}</li>" for x in t["how"])
    html = f'''<!DOCTYPE html>
<html lang="{t["hl"]}">
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
  {switch}
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
{SCRIPT.replace("__T__", json.dumps(js_t, ensure_ascii=False)).replace("__AQ__", json.dumps(AQ, ensure_ascii=False))}
</body>
</html>'''
    out = os.path.join(ROOT, t["path"]); os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(html)
    return t["path"]

if __name__ == "__main__":
    for c in L: print("wrote", build(c))
