# Gemeinsame Bausteine der Glycodex-Website ("Luminous Stage")

LOGO = "/_blob/b2351e6e5fcfeeb1c5a449fca0bf7c27"
IMG = {
    "uebersicht": "/_blob/a28c53f178763bca0118d05bd294d06a",
    "automodus": "/_blob/1c8150adeb545d1d8ae0f5caa0f21850",
    "tagesverlauf": "/_blob/bc10e5872398895728944ed09fcefdf4",
    "codex": "/_blob/90bcc3bfcafc2b4cfb1bb43e460765f5",
    "dextro": "/_blob/d3e58979acd9e3d586237d3df1164393",
    "zielbereich": "/_blob/5059b4be673fd1b9fddc2a068ae82047",
}
ALT = {
    "uebersicht": "Übersicht von Glycodex mit Zeit im Zielbereich",
    "automodus": "Auswertung des Auto-Modus in Glycodex",
    "tagesverlauf": "Tagesverlauf mit Glukose, Insulin und Bewegung",
    "codex": "Seiten im persönlichen Codex",
    "dextro": "Dextro mit Vorschlägen für Fragen",
    "zielbereich": "Zeit im Zielbereich mit Zielmarkern",
}

DARK = ("--bg:#000000;--card:#1c1c1e;--ink:#f5f5f7;--ink-2:#a1a1a8;--line:rgba(84,84,88,0.5);"
        "--accent:#8e8bff;--accent-dark:#b3b0ff;--accent-soft:rgba(142,139,255,0.18);--accent-soft-2:rgba(142,139,255,0.28);"
        "--on-accent:#0b0b14;--t-in:#32d74b;--band:rgba(50,215,75,0.14);--shadow:none;"
        "--frame:#2c2c2e;--frame-edge:rgba(255,255,255,0.16);--head:rgba(0,0,0,0.82);--hover-tint:rgba(142,139,255,0.06);"
        "--ok-bg:rgba(50,215,75,0.18);--ok-ink:#32d74b;--fill:rgba(118,118,128,0.24);--ink-3:#6b6b72;--t-low:#ff453a;--t-high:#ffd60a;--body-c:#8a6a58;--body-e:#5a4236;--cath:#4cc3dd;--cath-soft:rgba(76,195,221,0.16);--warn-bg:#3a3000;--warn-ink:#ffe28a")

CSS = r"""
body{margin:0;background:#f2f2f7}
body:has(.gx[data-theme="dark"]){background:#000000}
@media (prefers-color-scheme: dark){body:has(.gx[data-theme="auto"]){background:#000000}}
.gx{--bg:#f2f2f7;--card:#ffffff;--ink:#1c1c1e;--ink-2:#6b6b72;--line:rgba(60,60,67,0.13);--accent:#5b57d9;--accent-dark:#3f3ab8;--accent-soft:rgba(91,87,217,0.12);--accent-soft-2:rgba(91,87,217,0.20);--on-accent:#ffffff;--t-in:#2fb35a;--band:rgba(47,179,90,0.10);--shadow:0 10px 28px -10px rgba(24,24,72,0.10);--frame:#1c1c1e;--frame-edge:rgba(60,60,67,0.2);--head:rgba(242,242,247,0.84);--hover-tint:rgba(91,87,217,0.04);--ok-bg:rgba(47,179,90,0.14);--ok-ink:#1a7d47;--warn-bg:#fff1b8;--warn-ink:#5c4400;--fill:rgba(118,118,128,0.12);--ink-3:#a1a1a8;--t-low:#ef3e36;--t-high:#f2a20c;--body-c:#f3d9c6;--body-e:#d9b39a;--cath:#0e7490;--cath-soft:rgba(14,116,144,0.12);--story-indigo:#3d3ab0;--story-petrol:#0f6f80;--story-nacht:#26245e;--ease:cubic-bezier(.32,.72,0,1);font-family:'Google Sans',system-ui,-apple-system,sans-serif;color:var(--ink);background:var(--bg);overflow-x:clip;-webkit-font-smoothing:antialiased;min-height:100vh}
.gx[data-theme="dark"]{%%DARK%%}
@media (prefers-color-scheme: dark){.gx[data-theme="auto"]{%%DARK%%}}
.gx *{box-sizing:border-box}
.gx :focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:6px}
.gx img{display:block;max-width:100%}
.skip{position:fixed;left:12px;top:-80px;z-index:60;display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border-radius:12px;background:var(--accent);color:var(--on-accent);font-weight:500;text-decoration:none}
.skip:focus{top:12px}
.wrap{max-width:1200px;margin:0 auto;padding:0 32px}
.sec{padding:48px 0;position:relative}
.display{margin:0;font-size:52px;line-height:1.12;font-weight:500;letter-spacing:-0.025em}
.h1s{margin:0;font-size:44px;line-height:1.15;font-weight:500;letter-spacing:-0.02em}
.h2{margin:0;font-size:36px;line-height:1.2;font-weight:500;letter-spacing:-0.015em}
.h2c{margin:0;font-size:28px;line-height:1.2;font-weight:500;letter-spacing:-0.015em}
.h3{margin:0;font-size:21px;line-height:1.3;font-weight:500;letter-spacing:-0.01em}
.lead{margin:0;font-size:18px;line-height:1.55;color:var(--ink-2)}
.body{margin:0;font-size:16px;line-height:1.6;color:var(--ink-2)}
.small{margin:0;font-size:14px;line-height:1.5;color:var(--ink-2)}
.eye{display:inline-flex;align-items:center;margin:0 0 16px;padding:6px 12px;border-radius:999px;background:var(--accent-soft);color:var(--accent-dark);font-size:13px;line-height:1.2;font-weight:500;letter-spacing:0.01em}
.center{text-align:center}
.mx{margin-left:auto;margin-right:auto}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:44px;padding:0 22px;border:0;border-radius:12px;font-family:inherit;font-size:15px;line-height:1.2;font-weight:500;text-decoration:none;cursor:pointer;transition:background-color 200ms var(--ease),color 200ms var(--ease),transform 200ms var(--ease)}
.btn:active{transform:scale(0.985)}
.btn-l{min-height:48px}
.btn-p{background:var(--accent);color:var(--on-accent)}
.btn-p:hover{background:var(--accent-dark);color:var(--on-accent)}
.btn-s{padding:0 20px;background:var(--accent-soft);color:var(--accent-dark)}
.btn-s:hover{background:var(--accent-soft-2);color:var(--accent-dark)}
.btns{display:flex;flex-wrap:wrap;gap:12px}
.tl{color:var(--accent-dark);text-decoration:underline;text-decoration-thickness:1.5px;text-underline-offset:4px}
.tl:hover{color:var(--ink)}
.tel{display:inline-flex;align-items:center;min-height:44px}
.linkbtn{display:inline;min-height:0;padding:0;border:0;background:none;font:inherit;color:var(--accent-dark);text-decoration:underline;text-decoration-thickness:1.5px;text-underline-offset:4px;cursor:pointer}
.linkbtn:hover{color:var(--ink)}
.soon{background:transparent;border:1.5px dashed var(--accent);color:var(--accent-dark);cursor:default}
.soon:active{transform:none}
.soon-b{margin-left:4px;padding:2px 8px;border-radius:999px;background:var(--accent-soft);font-size:12px;font-weight:500}
.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:32px;box-shadow:var(--shadow)}
.frame-box{background:var(--card);border:1.5px solid var(--accent);border-radius:18px;padding:36px}
.story{position:relative;overflow:hidden;border-radius:18px;padding:36px;color:#ffffff}
.story .body,.story .lead,.story .small{color:rgba(255,255,255,0.88)}
.story .eye{background:rgba(255,255,255,0.16);color:#ffffff}
.story :focus-visible{outline-color:#ffffff}
.story .btn-s{background:rgba(255,255,255,0.16);color:#ffffff}
.story .btn-s:hover{background:rgba(255,255,255,0.24);color:#ffffff}
.story .btn-p{background:#ffffff;color:var(--sc,#3d3ab0)}
.story .btn-p:hover{background:rgba(255,255,255,0.88);color:var(--sc,#3d3ab0)}
.st-indigo{background:var(--story-indigo);--sc:#3d3ab0}
.st-petrol{background:var(--story-petrol);--sc:#0f6f80}
.st-nacht{background:var(--story-nacht);--sc:#26245e}
.num{display:inline-flex;align-items:center;justify-content:center;min-width:40px;height:28px;padding:0 10px;border-radius:999px;background:var(--accent-soft);color:var(--accent-dark);font-size:13px;font-weight:500;letter-spacing:0.01em;font-variant-numeric:tabular-nums}
.stack{display:flex;flex-direction:column}
.g2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}
.g3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.split{display:grid;gap:56px;align-items:start}
.sticky{position:sticky;top:112px}
.ico{width:28px;height:28px;flex:none;color:var(--accent)}
.ring{position:absolute;pointer-events:none;color:var(--accent)}
.ring-w{color:#ffffff}
.band{display:block;width:100%;pointer-events:none}
.band .bd{fill:var(--band)}
.band .be{fill:none;stroke:var(--t-in);stroke-width:1;stroke-opacity:0.55}
.band .bl{fill:none;stroke:var(--accent);stroke-width:2}
/* Kopfzeile */
.hdr{position:sticky;top:0;z-index:40;background:var(--head);-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.hdr-in{height:72px;display:flex;align-items:center;justify-content:space-between;gap:16px}
.brand{display:inline-flex;align-items:center;gap:10px;min-height:44px;text-decoration:none;color:var(--ink)}
.brand img{width:26px;height:26px}
.wm{font-size:20px;font-weight:500;letter-spacing:-0.01em;color:var(--ink)}
.wm b{font-weight:700;color:var(--accent)}
.nav-d{display:flex;align-items:center;gap:4px}
.nav-d a{display:inline-flex;align-items:center;min-height:44px;padding:0 12px;color:var(--ink-2);text-decoration:none;font-size:15px;border-bottom:2px solid transparent;transition:color 200ms var(--ease)}
.nav-d a:hover{color:var(--ink)}
.nav-d a[aria-current="page"]{color:var(--accent-dark);font-weight:500;border-bottom-color:var(--accent)}
.hdr-r{display:flex;align-items:center;gap:10px}
.icon-btn{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;flex:none;border:0;border-radius:999px;background:var(--accent-soft);color:var(--accent-dark);cursor:pointer;transition:background-color 200ms var(--ease)}
.icon-btn:hover{background:var(--accent-soft-2)}
.lnote{margin:0;padding:14px 18px;border-radius:14px;background:var(--accent-soft);color:var(--accent-dark);font-size:15px;line-height:1.5}
.lang{position:relative}
.lang-btn{width:auto;gap:6px;padding:0 14px 0 12px;font-family:inherit;font-size:14px;font-weight:500;letter-spacing:0.02em}
.lang-m{position:absolute;right:0;top:calc(100% + 8px);z-index:60;display:flex;flex-direction:column;min-width:184px;padding:6px;border-radius:16px;background:var(--card);border:1px solid var(--line);box-shadow:0 18px 40px -16px rgba(24,24,72,0.28)}
.lang-m a{display:flex;align-items:center;min-height:44px;padding:0 14px;border-radius:10px;color:var(--ink);text-decoration:none;font-size:15px}
.lang-m a:hover{background:var(--fill)}
.lang-m a[aria-current]{color:var(--accent-dark);font-weight:500;background:var(--accent-soft)}
.menu-btn{display:none;align-items:center;gap:8px;min-height:44px;padding:0 18px;border:0;border-radius:999px;background:var(--accent-soft);color:var(--accent-dark);font-family:inherit;font-size:15px;font-weight:500;cursor:pointer;transition:background-color 200ms var(--ease),color 200ms var(--ease)}
.menu-btn:hover,.menu-btn[aria-expanded="true"]{background:var(--accent);color:var(--on-accent)}
.mpanel{display:none;background:var(--card);border-bottom:1px solid var(--line);box-shadow:var(--shadow)}
.mpanel a.ml{display:flex;align-items:center;min-height:52px;color:var(--ink);text-decoration:none;font-size:17px;font-weight:500;border-bottom:1px solid var(--line)}
.mpanel a.ml[aria-current="page"]{color:var(--accent-dark)}
.mpanel .btn{width:100%;margin:16px 0 20px}
/* Kennzahlen */
.metric{display:flex;align-items:center;gap:14px;padding:16px 22px;background:var(--card);border:1px solid var(--line);border-radius:18px;box-shadow:var(--shadow);text-align:left}
.metric b{font-size:28px;line-height:1.1;font-weight:500;letter-spacing:-0.02em;color:var(--accent-dark);font-variant-numeric:tabular-nums}
.metric span{font-size:14px;line-height:1.4;color:var(--ink-2);max-width:170px}
/* Screens */
.phone{position:relative;flex:none;padding:10px;border-radius:34px;background:var(--frame);box-shadow:0 0 0 1px var(--frame-edge),var(--shadow)}
.phone img{width:100%;aspect-ratio:9/19.5;object-fit:cover;object-position:top;border-radius:26px}
.co{position:relative;width:220px;padding:12px 14px;background:var(--card);border:1px solid var(--line);border-radius:14px;box-shadow:var(--shadow);transition:border-color 200ms var(--ease)}
.co:hover{border-color:var(--accent)}
.co-t{margin:0;font-size:14px;line-height:1.4;font-weight:500;color:var(--ink)}
.co-x{margin:4px 0 0;font-size:14px;line-height:1.5;color:var(--ink-2)}
.co-ln{position:absolute;top:22px;height:0;border-top:1.5px solid var(--accent);width:var(--lw,72px)}
.co-ln::after{content:"";position:absolute;top:-3.75px;width:6px;height:6px;border-radius:50%;background:var(--accent)}
.co-ln.to-l{right:100%}
.co-ln.to-l::after{left:-3px}
.co-ln.to-r{left:100%}
.co-ln.to-r::after{right:-3px}
/* Hinweis vor dem E-Mail-Programm */
.hint{margin-top:12px;max-width:620px;padding:20px 24px;border-radius:18px;background:var(--accent-soft);border:1px solid var(--accent);color:var(--ink);text-align:left;outline:none;animation:hintIn 280ms var(--ease) both}
.story .hint{background:var(--card);color:var(--ink)}
.hint p{margin:0;font-size:15px;line-height:1.55;color:var(--ink)}
.hint .hint-t{font-size:17px;font-weight:500}
.hint .hint-s{margin-top:8px;font-size:14px;color:var(--ink-2)}
.hint .btns{margin-top:16px}
.story .hint .btn-p{background:var(--accent);color:var(--on-accent)}
.story .hint .btn-p:hover{background:var(--accent-dark);color:var(--on-accent)}
.story .hint .btn-s{background:var(--accent-soft);color:var(--accent-dark)}
.story .hint .btn-s:hover{background:var(--accent-soft-2);color:var(--accent-dark)}
.story .hint :focus-visible{outline-color:var(--accent)}
@keyframes hintIn{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}
/* Zeitleiste */
.tline{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:16px}
.tline li{position:relative;display:grid;grid-template-columns:28px minmax(0,1fr);gap:16px}
.tline li::before{content:"";position:absolute;left:13px;top:0;bottom:-16px;width:2px;background:var(--accent)}
.tline li.open::before{background:var(--line)}
.tline li.now::before{background:linear-gradient(to bottom,var(--accent) 0,var(--accent) 31px,var(--line) 31px)}
.tline li:last-child::before{bottom:auto;height:30px}
.tnode{position:relative;z-index:1;margin-top:24px;margin-left:7px;width:14px;height:14px;border-radius:50%;background:var(--accent)}
.tnode.now{margin-top:22px;margin-left:5px;width:18px;height:18px;box-shadow:inset 0 0 0 3px var(--bg)}
.tnode.open{background:var(--bg);box-shadow:inset 0 0 0 2px var(--line)}
.tnode.n{display:inline-flex;align-items:center;justify-content:center;margin:18px 0 0;width:28px;height:28px;color:var(--on-accent);font-size:13px;font-weight:500}
.tcard{padding:22px 28px}
.tdate{margin:0 0 4px;font-size:14px;font-weight:500;color:var(--accent-dark)}
/* Häufige Fragen */
.faq{max-width:820px;margin:40px auto 0;padding:0;overflow:hidden}
.faq details{border-top:1px solid var(--line)}
.faq details:first-child{border-top:0}
.faq summary{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:64px;padding:20px 28px;list-style:none;cursor:pointer;font-size:17px;line-height:1.4;font-weight:500;color:var(--ink);transition:background-color 200ms var(--ease)}
.faq summary::-webkit-details-marker{display:none}
.faq summary:hover{background:var(--hover-tint)}
.faq summary:focus-visible{outline-offset:-2px;border-radius:0}
.faq summary svg{width:20px;height:20px;flex:none;color:var(--accent-dark);transition:transform 260ms var(--ease)}
.faq details[open] summary svg{transform:rotate(45deg)}
.faq .ans{margin:0;padding:0 28px 24px;font-size:16px;line-height:1.6;color:var(--ink-2)}
/* Seitenfuß */
.ftr{border-top:1px solid var(--line);padding:48px 0;background:var(--bg)}
.ftr-top{display:flex;flex-wrap:wrap;justify-content:space-between;gap:16px 32px;align-items:center}
.ftr nav{display:flex;flex-wrap:wrap;gap:0 20px}
.ftr nav a{display:inline-flex;align-items:center;min-height:44px;color:var(--ink-2);text-decoration:none;font-size:14px}
.ftr nav a:hover{color:var(--ink)}
.ftr-bot{display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px 32px;margin-top:24px;padding-top:24px;border-top:1px solid var(--line)}
.ftr-bot p{margin:0;font-size:13px;line-height:1.5;color:var(--ink-2)}
/* Einblenden */
@media (prefers-reduced-motion: no-preference){
.js .rv{opacity:0;transform:translateY(16px);transition:opacity 480ms var(--ease) var(--d,0ms),transform 480ms var(--ease) var(--d,0ms)}
.js .rv.in{opacity:1;transform:none}
.rise{animation:rise 550ms var(--ease) 80ms both}
}
@keyframes rise{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion: reduce){.gx *,.gx *::before,.gx *::after{transition-duration:0ms !important;animation-duration:0ms !important;animation-delay:0ms !important}}
/* Umbrüche */
@media (max-width:1023px){
.wrap{padding:0 24px}
.nav-d,.hdr-cta{display:none}
.menu-btn{display:inline-flex}
.mpanel{display:block}
.sticky{position:static}
}
@media (max-width:767px){
.lang-btn{width:44px;padding:0}
.lang-btn span{display:none}
.wrap{padding:0 20px}
.sec{padding:28px 0}
.hdr-in{height:64px}
.display{font-size:34px;line-height:1.15}
.h1s{font-size:30px}
.h2{font-size:28px}
.h2c{font-size:24px}
.h3{font-size:19px}
.lead{font-size:16px}
.body{font-size:15px}
.metric b{font-size:24px}
.card{padding:20px}
.frame-box,.story{padding:24px}
.g2,.g3,.split{grid-template-columns:minmax(0,1fr) !important;gap:14px}
.split{gap:24px}
.faq{margin-top:28px}
.faq summary{min-height:56px;padding:16px 20px;font-size:16px}
.faq .ans{padding:0 20px 20px;font-size:15px}
.hint .btns{flex-direction:column;align-items:stretch}
.co{width:auto;background:var(--accent-soft);border-color:transparent;box-shadow:none}
.co-ln{display:none}
.swipe{display:flex !important;flex-direction:row !important;overflow-x:auto;scroll-snap-type:x mandatory;gap:12px !important;margin-left:-20px;margin-right:-20px;padding:4px 20px 14px;scroll-padding-left:20px;scrollbar-width:none;align-items:stretch}
.swipe::-webkit-scrollbar{display:none}
.swipe > *{flex:0 0 82%;scroll-snap-align:start;min-width:0}
.ftr{padding:36px 0}
.tcard{padding:18px}
}
""".replace("%%DARK%%", DARK)


def ico(paths, cls="ico"):
    return ('<svg class="' + cls + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + paths + '</svg>')


ICONS = {
    "gefuehl": '<circle cx="12" cy="12" r="9"/><path d="M8.5 14.5c.9 1.2 2.1 1.8 3.5 1.8s2.6-.6 3.5-1.8"/><path d="M9 9.5h.01M15 9.5h.01"/>',
    "codex": '<path d="M4 5.5c2.5-1 5-1 8 1 3-2 5.5-2 8-1v13c-2.5-1-5-1-8 1-3-2-5.5-2-8-1z"/><path d="M12 6.5v13"/>',
    "dextro": '<path d="M5 5h14a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1h-8l-4 3.5V16H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z"/><path d="M8.5 10.5h7"/>',
    "team": '<circle cx="9" cy="8.5" r="3"/><path d="M3.5 19c.6-3 2.8-4.8 5.5-4.8s4.9 1.8 5.5 4.8"/><path d="M16 6a3 3 0 0 1 0 5.6M17.8 14.4c1.5.6 2.4 2.1 2.7 4.6"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5.5M12 7.8h.01"/>',
    "report": '<path d="M7 3.5h7l4 4v13H7a1 1 0 0 1-1-1v-15a1 1 0 0 1 1-1z"/><path d="M14 3.5v4h4M9 13h6M9 16.5h6"/>',
    "zugang": '<circle cx="8" cy="15" r="4"/><path d="M11 12l8-8M16 7l2.5 2.5M14 9l2 2"/>',
    "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    "schloss": '<rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/>',
    "tropfen": '<path d="M12 3.2c3.6 4.3 6 7.8 6 10.8a6 6 0 0 1-12 0c0-3 2.4-6.5 6-10.8z"/>',
    "mail": '<rect x="3.5" y="5.5" width="17" height="13" rx="2"/><path d="M4 7l8 6 8-6"/>',
    "katheter": '<ellipse cx="7" cy="17" rx="4.5" ry="2"/><path d="M7 15v-3M7 12c0-5 4-8 8-8h2a3 3 0 0 1 3 3v1"/><circle cx="20" cy="10.5" r="1.5"/>',
    "drehen": '<path d="M4 12a8 8 0 0 1 14-5.3M20 12a8 8 0 0 1-14 5.3"/><path d="M18 3v4h-4M6 21v-4h4"/>',
    "kamera": '<path d="M4 8.5a2 2 0 0 1 2-2h2l1.5-2h5L16 6.5h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/><circle cx="12" cy="13" r="3.5"/>',
    "karte": '<path d="M12 3.5c-2.2 0-3.5 1.6-3.5 3.5S9.8 10.5 12 10.5s3.5-1.6 3.5-3.5S14.2 3.5 12 3.5z"/><path d="M6 20.5c.4-4.3 2.6-7 6-7s5.6 2.7 6 7"/>',
}


def ring(size, ops=(0.20, 0.14, 0.09, 0.05), style="", white=False):
    n = len(ops)
    c = size / 2
    circles = ""
    for i, o in enumerate(ops):
        r = c * (0.43 + 0.57 * i / (n - 1)) - 1 if n > 1 else c - 1
        circles += '<circle cx="%g" cy="%g" r="%g" stroke-opacity="%s" stroke-width="1.5"/>' % (c, c, r, o)
    cls = "ring ring-w" if white else "ring"
    return ('<svg class="%s" width="%d" height="%d" viewBox="0 0 %d %d" fill="none" stroke="currentColor" aria-hidden="true" style="%s">%s</svg>'
            % (cls, size, size, size, size, style, circles))


def band(h=72, style=""):
    """Zielbereich als gerades Band mit zwei geraden Grenzlinien, darin die wellige Sensorkurve."""
    top, bot = h * .28, h * .74
    return ('<svg class="band" viewBox="0 0 1440 %d" preserveAspectRatio="none" aria-hidden="true" style="height:%dpx;%s">'
            '<rect class="bd" x="0" y="%g" width="1440" height="%g"/>'
            '<path class="be" vector-effect="non-scaling-stroke" d="M0 %g H1440 M0 %g H1440"/>'
            '<path class="bl" vector-effect="non-scaling-stroke" d="M0 %g C160 %g 300 %g 480 %g S760 %g 960 %g S1260 %g 1440 %g"/></svg>'
            % (h, h, style, top, bot - top, top, bot,
               h * .58, h * .66, h * .36, h * .44, h * .66, h * .52, h * .34, h * .48))


def phone(key, width, cls="", eager=False, style=""):
    load = "eager" if eager else "lazy"
    return ('<div class="phone %s" style="width: %dpx;%s"><img src="%s" alt="%s" loading="%s"></div>'
            % (cls, width, style, IMG[key], ALT[key], load))


def callout(title, text, line_dir, lw=72, style=""):
    return ('<div class="co" style="%s"><span class="co-ln to-%s" style="--lw: %dpx" aria-hidden="true"></span>'
            '<p class="co-t">%s</p><p class="co-x">%s</p></div>' % (style, line_dir, lw, title, text))


PLUS = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" aria-hidden="true"><path d="M10 4v12M4 10h12"/></svg>'
SUN = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6l1.4 1.4M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4L6 18M18 6l1.4-1.4"/></svg>'
MOON = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></svg>'
BURGER = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
CLOSE = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'

GLOBE = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9M12 3C9.5 5.6 8.2 8.6 8.2 12s1.3 6.4 3.8 9"/></svg>'
BASES = {"main": "Main", "teams": "Fachkreise", "partner": "Partner", "impressum": "Impressum", "datenschutz": "Datenschutz"}
LANGS = [("de", "Deutsch"), ("en", "English"), ("fr", "Français"), ("uk", "Українська")]


def lang_switch(page):
    base = BASES[page]
    items = "".join('<a href="§%s§%s" hreflang="%s" lang="%s" §CUR_%s§>%s</a>' % (base, c, c, c, c, n) for c, n in LANGS)
    return ('<div class="lang"><button type="button" class="icon-btn lang-btn" aria-label="Sprache wählen" aria-controls="langm" aria-expanded="{{langExpanded}}" onClick="{{toggleLang}}">'
            + GLOBE + '<span>§CODE§</span></button>'
            '<sc-if value="{{langOpen}}" hint-placeholder-val="{{false}}"><div id="langm" class="lang-m">' + items + '</div></sc-if></div>')


NAV = [
    ("main", "Funktionen", "Main.dc.html#funktionen", "#funktionen"),
    ("main", "So funktioniert's", "Main.dc.html#ablauf", "#ablauf"),
    ("teams", "Für Diabetes-Teams", "Fachkreise.dc.html", "Fachkreise.dc.html"),
    ("partner", "Für Partnerschaften", "Partner.dc.html", "Partner.dc.html"),
]


def header(page):
    links = ""
    mlinks = ""
    for key, label, href_other, href_main in NAV:
        href = href_main if page == "main" else href_other
        cur = ' aria-current="page"' if key == page and page != "main" else ""
        links += '<a href="%s"%s>%s</a>' % (href, cur, label)
        mlinks += '<a class="ml" href="%s"%s onClick="{{closeMenu}}">%s</a>' % (href, cur, label)
    kontakt = "#kontakt" if page in ("main", "teams", "partner") else "Main.dc.html#kontakt"
    home = "#top" if page == "main" else "Main.dc.html"
    if page != "main":
        mlinks = '<a class="ml" href="Main.dc.html" onClick="{{closeMenu}}">Startseite</a>' + mlinks
    return (
        '<a class="skip" href="#inhalt">Direkt zum Inhalt springen</a>\n'
        '<header class="hdr">\n<div class="wrap hdr-in">\n'
        '<a class="brand" href="' + home + '" aria-label="Glycodex Startseite"><img src="' + LOGO + '" alt=""><span class="wm">Glyco<b>dex</b></span></a>\n'
        '<nav class="nav-d" aria-label="Hauptnavigation">' + links + '</nav>\n'
        '<div class="hdr-r">' + lang_switch(page) +
        '<button type="button" class="icon-btn" aria-label="Farbschema wechseln" title="Farbschema wechseln" onClick="{{toggleTheme}}">'
        '<sc-if value="{{isDark}}" hint-placeholder-val="{{false}}">' + SUN + '</sc-if>'
        '<sc-if value="{{isLight}}" hint-placeholder-val="{{true}}">' + MOON + '</sc-if></button>'
        '<a class="btn btn-p hdr-cta" href="' + kontakt + '">Kontakt</a>'
        '<button type="button" class="menu-btn" aria-controls="mnav" aria-expanded="{{menuExpanded}}" onClick="{{toggleMenu}}">'
        '<sc-if value="{{menuOpen}}" hint-placeholder-val="{{false}}">' + CLOSE + '</sc-if>'
        '<sc-if value="{{menuClosed}}" hint-placeholder-val="{{true}}">' + BURGER + '</sc-if>Menü</button>'
        '</div>\n</div>\n'
        '<sc-if value="{{menuOpen}}" hint-placeholder-val="{{false}}"><nav id="mnav" class="mpanel" aria-label="Menü"><div class="wrap">'
        + mlinks +
        '<a class="btn btn-p btn-l" href="' + kontakt + '" onClick="{{closeMenu}}">Kontakt</a></div></nav></sc-if>\n'
        '</header>\n'
    )


def footer(page):
    items = [("main", "Startseite", "Main.dc.html"), ("teams", "Für Diabetes-Teams", "Fachkreise.dc.html"),
             ("partner", "Für Partnerschaften", "Partner.dc.html"), ("impressum", "Impressum", "Impressum.dc.html"),
             ("datenschutz", "Datenschutz", "Datenschutz.dc.html")]
    links = ""
    for key, label, href in items:
        cur = ' aria-current="page"' if key == page else ""
        links += '<a href="%s"%s>%s</a>' % (href, cur, label)
    return (
        '<footer class="ftr">\n<div class="wrap">\n<div class="ftr-top">'
        '<a class="brand" href="Main.dc.html"><img src="' + LOGO + '" alt=""><span class="wm">Glyco<b>dex</b></span></a>'
        '<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 12px 20px"><nav aria-label="Weitere Seiten">' + links + '</nav>' + insta() + '</div></div>\n'
        '<div class="ftr-bot"><p>© 2026 Lina Schröder · Delitzsch</p>'
        '<p style="max-width: 560px">Glycodex beschreibt Daten und gibt keine Therapie- oder Dosisempfehlungen. Kein Medizinprodukt. '
        'Unabhängig von den genannten Unternehmen. Im Notfall: 112.</p></div>\n</div>\n</footer>\n'
    )


def insta():
    # Platzhalter, bis das Instagram-Konto steht: dann wird daraus ein Link.
    return ('<span class="btn btn-s soon">' + ico(ICONS["kamera"]).replace('class="ico"', 'class="ico" style="width: 18px; height: 18px; color: currentColor"')
            + 'Instagram<span class="soon-b">folgt bald</span></span>')


def phone_reveal(cls="btn btn-s btn-l"):
    # Die Nummer steht nicht im HTML. Sie wird erst nach Klick aus Zeichencodes zusammengesetzt.
    return ('<sc-if value="{{phoneHidden}}" hint-placeholder-val="{{true}}"><button type="button" class="' + cls + '" onClick="{{showPhone}}">Telefonnummer anzeigen</button></sc-if>'
            '<sc-if value="{{phoneShown}}" hint-placeholder-val="{{false}}"><a class="' + cls + '" href="{{telHref}}">{{telText}}</a></sc-if>')


def hint(flag, sfx):
    return (
        '<sc-if value="{{' + flag + '}}" hint-placeholder-val="{{false}}"><div class="hint" role="dialog" aria-modal="false" '
        'aria-labelledby="mh-' + sfx + '" aria-describedby="md-' + sfx + '" tabindex="-1" ref="{{panelRef}}" onKeyDown="{{panelKey}}">'
        '<p class="hint-t" id="mh-' + sfx + '">Gleich öffnet sich dein E-Mail-Programm</p>'
        '<p id="md-' + sfx + '" style="margin-top: 6px">Die Nachricht an lina.schroeder@autarkflow.de ist mit dem Betreff „{{mailSubject}}“ vorbereitet. '
        'Kein E-Mail-Programm eingerichtet? Dann schreib einfach direkt an diese Adresse.</p>'
        '<p class="hint-s">Bitte schick mir keine Gesundheitsdaten wie Glukosewerte oder Befunde.</p>'
        '<div class="btns"><a class="btn btn-p" href="{{mailHref}}" onClick="{{sendMail}}">E-Mail schreiben</a>'
        '<button type="button" class="btn btn-s" onClick="{{closeMail}}">Erst einmal weiter informieren</button></div></div></sc-if>'
    )


def logic(asks, methods="", vals=""):
    """asks: list of (handlerName, subject, location)."""
    ask_lines = ""
    flags = set()
    for name, subj, at in asks:
        ask_lines += "%s: ask(%r, %r),\n" % (name, subj, at)
        flags.add(at)
    flag_lines = "".join("mailAt_%s: !!mail && mail.at === %r,\n" % (f, f) for f in sorted(flags))
    return r"""class Component extends DCLogic {
componentDidMount() {
let t = null;
try { t = window.localStorage.getItem('glycodex-theme'); } catch (e) {}
this.setState({ ready: true, theme: (t === 'light' || t === 'dark') ? t : 'auto' });
try {
this._mq = window.matchMedia('(prefers-color-scheme: dark)');
this._mqh = () => this.forceUpdate();
this._mq.addEventListener('change', this._mqh);
} catch (e) {}
this._timer = setTimeout(() => this.observe(), 30);
}
componentWillUnmount() {
try { if (this._mq) this._mq.removeEventListener('change', this._mqh); } catch (e) {}
if (this._io) this._io.disconnect();
clearTimeout(this._timer);
}
observe() {
const root = this._root;
if (!root) return;
const els = Array.prototype.slice.call(root.querySelectorAll('.rv'));
if (!('IntersectionObserver' in window)) { els.forEach((el) => el.classList.add('in')); return; }
this._io = new IntersectionObserver((entries) => {
entries.forEach((en) => {
if (en.isIntersecting) { en.target.classList.add('in'); this._io.unobserve(en.target); }
});
}, { threshold: 0.12 });
els.forEach((el) => this._io.observe(el));
}
""" + methods + r"""
renderVals() {
const s = this.state || {};
let dark = false;
if (s.theme === 'dark') dark = true;
else if (s.theme !== 'light') { try { dark = window.matchMedia('(prefers-color-scheme: dark)').matches; } catch (e) {} }
if (!this._rootRef) this._rootRef = (el) => { this._root = el; };
if (!this._panelRef) {
this._panelRef = (el) => {
if (!el) return;
let calm = false;
try { calm = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (x) {}
try { el.scrollIntoView({ behavior: calm ? 'auto' : 'smooth', block: 'center' }); } catch (x) {}
try { el.focus({ preventScroll: true }); } catch (x) {}
};
}
const open = !!s.menuOpen;
const mail = s.mail || null;
const subject = mail ? (mail.subj ? 'Glycodex – ' + mail.subj : 'Glycodex') : '';
const ask = (subj, at) => (e) => {
this._trigger = e && e.currentTarget;
this.setState({ mail: { subj: subj, at: at } });
};
const closeMail = () => {
this.setState({ mail: null });
const tr = this._trigger;
if (tr && tr.focus) { try { tr.focus({ preventScroll: true }); } catch (x) {} }
};
return {
rootClass: 'gx' + (s.ready ? ' js' : ''),
theme: s.theme || 'auto',
isDark: dark,
isLight: !dark,
toggleTheme: () => {
const next = dark ? 'light' : 'dark';
try { window.localStorage.setItem('glycodex-theme', next); } catch (e) {}
this.setState({ theme: next });
},
rootRef: this._rootRef,
menuOpen: open,
menuClosed: !open,
menuExpanded: open ? 'true' : 'false',
toggleMenu: () => this.setState({ menuOpen: !open, langOpen: false }),
langOpen: !!s.langOpen,
langExpanded: s.langOpen ? 'true' : 'false',
toggleLang: () => this.setState({ langOpen: !s.langOpen, menuOpen: false }),
closeMenu: () => this.setState({ menuOpen: false }),
mailSubject: subject,
mailHref: 'mailto:lina.schroeder@autarkflow.de?subject=' + encodeURIComponent(subject),
phoneShown: !!s.phone,
phoneHidden: !s.phone,
showPhone: () => this.setState({ phone: true }),
telText: s.phone ? String.fromCharCode.apply(null, [43, 52, 57, 32, 49, 53, 54, 32, 51, 48, 48, 50, 54, 52, 53, 54]) : '',
telHref: s.phone ? 'tel:' + String.fromCharCode.apply(null, [43, 52, 57, 49, 53, 54, 51, 48, 48, 50, 54, 52, 53, 54]) : '',
""" + vals + ask_lines + flag_lines + r"""panelRef: this._panelRef,
panelKey: (e) => { if (e.key === 'Escape') closeMail(); },
closeMail: closeMail,
sendMail: () => this.setState({ mail: null })
};
}
}"""


def page(title, body, page_key, asks, height, extra_css="", methods="", vals=""):
    return (
        '<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n<title>' + title + '</title>\n'
        '<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&amp;display=swap">\n'
        '<style>' + CSS + extra_css + '</style>\n</helmet>\n'
        '<div class="{{rootClass}}" data-theme="{{theme}}" ref="{{rootRef}}" id="top">\n'
        + header(page_key) +
        '<main id="inhalt">\n' + body + '</main>\n' + footer(page_key) +
        '</div>\n</x-dc>\n'
        '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":1280,"height":' + str(height) + '}}\'>\n'
        + logic(asks, methods, vals) + '\n</script>\n</body>\n</html>\n'
    )
