from common import *

MAIN_CSS = r"""
.hero{padding:88px 0 72px;text-align:center}
.hero .display{max-width:720px;margin:0 auto}
.hero .lead{max-width:640px;margin:16px auto 0}
.hero .btns{justify-content:center;margin-top:28px}
.metrics{display:flex;flex-wrap:wrap;justify-content:center;gap:16px;margin-top:28px}
.stage{position:relative;max-width:1040px;margin:48px auto 0;padding:24px 0 8px}
.stage .ring{left:50%;top:50%;transform:translate(-50%,-50%)}
.duo{position:relative;z-index:1;display:flex;justify-content:center;align-items:flex-start}
.duo .pa{z-index:2}
.duo .pb{z-index:1;margin-left:-24px;margin-top:72px}
.stage .co{position:absolute;z-index:3;width:200px;text-align:left}
.co-hl{left:0;top:406px}
.co-hr{right:0;top:299px}
.note{margin:28px 0 0;font-size:14px;color:var(--ink-2)}
.feat-wide{display:grid;grid-template-columns:minmax(0,1fr) 220px;gap:28px;align-items:start;overflow:hidden}
.zoom{position:relative;width:220px;height:300px;overflow:hidden;border-radius:22px;border:1px solid var(--line);background:#f2f2f7;box-shadow:var(--shadow);-webkit-mask-image:linear-gradient(#000 82%,transparent);mask-image:linear-gradient(#000 82%,transparent)}
.zoom img{position:absolute;left:0;width:100%;max-width:none}
.steps3{position:relative;margin:0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:36px}
.steps3::before{content:"";position:absolute;top:18px;left:18px;right:calc((100% - 72px) / 3 - 18px);height:1px;background:var(--line)}
.steps3 li{position:relative;display:flex;flex-direction:column;gap:12px}
.spill{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:50%;background:var(--accent);color:var(--on-accent);font-size:15px;font-weight:500;box-shadow:0 0 0 6px var(--card)}
.show-row4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px;margin-top:48px}
.show{margin:0;display:flex;flex-direction:column;gap:20px}
.show .phone{width:100% !important;max-width:240px;margin:0 auto}
.halt-band{position:relative;overflow:hidden;margin:48px 0;padding:104px 0;background:var(--story-indigo);color:#ffffff}
.halt-band .eye{background:rgba(255,255,255,0.16);color:#ffffff}
.halt-band :focus-visible{outline-color:#ffffff}
.halt-h{max-width:780px;font-size:44px;color:#ffffff}
.vals{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px;margin-top:48px}
.val{padding:28px;border-radius:18px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.18)}
.val .body{color:rgba(255,255,255,0.86)}
.val .h3{color:#ffffff}
.who1{display:grid;grid-template-columns:58fr 42fr;gap:24px}
.who2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;margin-top:24px}
.emblem{position:relative;overflow:hidden;aspect-ratio:1;max-width:380px;width:100%;border-radius:18px;background:var(--story-nacht);display:flex;align-items:center;justify-content:center}
.emb-logo{position:relative;z-index:1;display:flex;border-radius:30px;box-shadow:0 0 0 12px rgba(255,255,255,0.06),0 0 0 26px rgba(255,255,255,0.035),0 28px 56px -16px rgba(0,0,0,0.6)}
.emb-logo img{width:112px;height:112px;border-radius:30px}
.emblem .band .bd{fill:rgba(50,215,75,0.16)}
.emblem .band .be{stroke:#32d74b}
.emblem .band .bl{stroke:#ffffff;stroke-opacity:0.85}
.emblem .ring{left:50%;top:50%;transform:translate(-50%,-50%)}
.emblem .band{position:absolute;left:0;right:0;bottom:36px}
.quote{margin:28px 0 0;padding:28px 32px;border-left:3px solid var(--accent);border-radius:0 14px 14px 0;background:var(--accent-soft)}
.quote p{margin:0;font-size:18px;line-height:1.55;font-weight:500;color:var(--ink)}
.quote footer{margin-top:12px;font-size:14px;color:var(--ink-2)}
.kstage{position:relative;overflow:hidden;padding:64px;text-align:center}
.kstage .ring{left:auto;right:-420px;top:-420px;transform:none}
.kway{background:var(--bg);border-radius:18px;padding:24px;text-align:left;display:flex;flex-direction:column;gap:10px}
.dot{display:inline-block;width:10px;height:10px;border-radius:50%}
.kfoot{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:12px;margin-top:12px}
.kstage .hint{margin-left:auto;margin-right:auto}
.bm-card{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:0;align-items:stretch;margin-top:24px;padding:0;overflow:hidden}
.bm-text{display:flex;flex-direction:column;justify-content:center;padding:56px}
.bm-ico{display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;border-radius:16px;background:var(--cath-soft);color:var(--cath)}
.try{display:inline-flex;align-items:center;gap:10px;align-self:flex-start;margin:28px 0 0;padding:10px 16px;border-radius:999px;background:var(--accent-soft);color:var(--accent-dark);font-size:15px;line-height:1.4;font-weight:500}
.bm-stage{position:relative;display:flex;align-items:center;justify-content:center;padding:44px 24px;background:var(--bg);border-left:1px solid var(--line);overflow:hidden}
.bm-stage .ring{left:50%;top:50%;transform:translate(-50%,-50%)}
.phone-live{position:relative}
.phone-live{width:340px;max-width:100%;margin:0 auto;padding:10px;border-radius:38px;background:var(--frame);box-shadow:0 0 0 1px var(--frame-edge),var(--shadow)}
.ap{display:flex;flex-direction:column;gap:10px;padding:18px 14px 16px;border-radius:28px;background:var(--card);color:var(--ink);font-size:15px}
.ap-row{display:flex;align-items:center;justify-content:space-between;gap:8px}
.ap-lbl{font-size:13px;font-weight:500;color:var(--ink-2)}
.ap-small{font-size:13px;color:var(--ink-2)}
.ap-seg{display:flex;gap:2px;padding:2px;border-radius:9px;background:var(--fill)}
.ap-segb{flex:1 0 auto;min-height:40px;padding:8px 10px;border:0;border-radius:7px;background:none;font-family:inherit;font-size:14px;font-weight:500;color:var(--ink);cursor:pointer;transition:background-color 280ms var(--ease)}
.ap-segb.on{background:var(--card);box-shadow:0 1px 3px rgba(0,0,0,0.12);font-weight:600}
.ap-wrap{position:relative;border-radius:14px;background:var(--fill);touch-action:none;user-select:none;-webkit-user-select:none;overflow:hidden;cursor:grab}
.ap-wrap:active{cursor:grabbing}
.ap-svg{display:block;width:100%;height:auto;aspect-ratio:320/300}
.ap-info{display:flex;flex-direction:column;gap:6px}
.ap-txt{font-size:13px;line-height:1.4;color:var(--ink)}
.ap-txt b{font-weight:600}
.ap-btn{flex:none;min-height:36px;padding:0 14px;border:0;border-radius:10px;background:var(--fill);color:var(--ink);font-family:inherit;font-size:13px;font-weight:500;cursor:pointer}
.ap-warn{margin:0;padding-left:8px;border-left:3px solid var(--t-high);font-size:13px;line-height:1.4;font-weight:600;color:var(--ink)}
.ap-leg{display:flex;flex-wrap:wrap;gap:4px 10px;font-size:12px;color:var(--ink-2)}
.ap-leg span{display:inline-flex;align-items:center;gap:5px}
.ap-leg .dot{display:inline-block;width:9px;height:9px;border-radius:50%;box-sizing:border-box}
@media (max-width:1023px){
.vals{grid-template-columns:repeat(2,minmax(0,1fr))}
.bm-card{grid-template-columns:minmax(0,1fr)}.bm-stage{border-left:0;border-top:1px solid var(--line)}
.stage .co{position:static;width:auto}
.stage .co-ln{display:none}
.stage-cos{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:24px}
.show-row4{grid-template-columns:repeat(2,minmax(0,1fr));gap:40px 24px}
}
@media (min-width:1024px){.stage-cos{display:contents}}
@media (max-width:767px){
.bm-text{padding:28px 24px}.bm-stage{padding:24px 12px}.try{align-self:stretch;border-radius:14px}
.hero{padding:40px 0 48px}
.metrics{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.metric{flex-direction:column;align-items:flex-start;gap:4px;padding:12px 12px 14px}
.metric span{max-width:none;font-size:12px;line-height:1.35}
.duo .pa{width:240px !important}
.duo .pb{width:200px !important;margin-left:-100px;margin-top:40px}
.feat-wide{grid-template-columns:minmax(0,1fr)}
.zoom{width:220px;height:300px;margin:0 auto}
.steps3{grid-template-columns:minmax(0,1fr);gap:28px;padding-left:48px}
.steps3::before{top:16px;bottom:16px;left:16px;right:auto;width:1px;height:auto}
.steps3 li{padding-top:2px}
.steps3 .spill{position:absolute;left:-48px;top:0;width:32px;height:32px}
.show-row4{margin-top:28px}
.show-row4 > .show{flex-basis:72% !important}
.halt-band{padding:56px 0;margin:28px 0}
.halt-h{font-size:30px}
.vals{margin-top:28px}
.val{padding:22px}
.who1,.who2{grid-template-columns:minmax(0,1fr);gap:16px}
.who2{margin-top:16px}
.emblem{aspect-ratio:auto;max-width:none;height:200px}
.emblem .band{bottom:16px;height:40px !important}
.emb-logo img{width:72px;height:72px;border-radius:20px}
.emb-logo{border-radius:20px}
.quote{padding:20px}
.kstage{padding:32px 20px}
}
"""


SCREEN = (
'<div class="phone-live" aria-label="Körperkarte aus der App, mit erfundenen Testdaten">'
'<div class="ap">'
'<div class="ap-row"><span class="ap-lbl">{{bmLbl}}</span><span class="ap-small">{{bmView}}</span></div>'
'<div class="ap-seg" role="group" aria-label="Körperbereich"><sc-for list="{{bmModes}}" as="m" hint-placeholder-count="3"><button type="button" class="{{m.cls}}" aria-pressed="{{m.pressed}}" onClick="{{m.pick}}">{{m.n}}</button></sc-for></div>'
'<div class="ap-wrap" onPointerDown="{{bmDown}}" onPointerMove="{{bmMove}}" onPointerUp="{{bmUp}}" onPointerCancel="{{bmCancel}}">'
'<svg class="ap-svg" viewBox="0 0 320 300" role="img" aria-label="{{bmAria}}">'
'<defs>'
'<linearGradient id="bsh" x1="0" x2="1"><stop offset="0" stop-color="var(--body-e)"></stop><stop offset="0.5" stop-color="var(--body-c)"></stop><stop offset="1" stop-color="var(--body-e)"></stop></linearGradient>'
'<linearGradient id="bfade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"></stop><stop offset="0.12" stop-color="#fff"></stop><stop offset="0.9" stop-color="#fff"></stop><stop offset="1" stop-color="#fff" stop-opacity="0"></stop></linearGradient>'
'<mask id="bmask-b" maskUnits="userSpaceOnUse" x="0" y="0" width="320" height="300"><rect x="0" y="16" width="320" height="270" fill="url(#bfade)"></rect></mask>'
'<mask id="bmask-a" maskUnits="userSpaceOnUse" x="0" y="0" width="320" height="300"><rect x="0" y="4" width="320" height="296" fill="url(#bfade)"></rect></mask>'
'</defs>'
'<g mask="{{bmMask}}">'
'<path d="{{bmOutline}}" fill="url(#bsh)" stroke="var(--line)" stroke-width="1"></path>'
'<path d="{{bmGrid}}" fill="none" stroke="var(--ink-3)" stroke-width="0.6" opacity="0.35"></path>'
'<path d="{{bmSpine}}" fill="none" stroke="var(--ink-3)" stroke-width="1.6" opacity="0.7" stroke-dasharray="4 3"></path>'
'<path d="{{bmMarks}}" fill="none" stroke="var(--ink-2)" stroke-width="1.2" opacity="0.5"></path>'
'<path d="{{bmZone}}" fill="var(--t-in)" fill-opacity="0.08" stroke="var(--t-in)" stroke-opacity="0.3" stroke-dasharray="3 3"></path>'
'</g>'
'<path d="{{bmNavelRing}}" fill="var(--t-low)" fill-opacity="0.07" stroke="var(--t-low)" stroke-opacity="0.35" stroke-dasharray="3 3"></path>'
'<path d="{{bmNavel}}" fill="var(--ink-2)" opacity="0.7"></path>'
'<path d="{{bmR0}}" fill="var(--t-low)" fill-opacity="0.1"></path>'
'<path d="{{bmR1}}" fill="var(--t-high)" fill-opacity="0.1"></path>'
'<path d="{{bmR2}}" fill="var(--ink-3)" fill-opacity="0.05"></path>'
'<path d="{{bmC0}}" fill="var(--t-low)" stroke="var(--card)" stroke-width="1"></path>'
'<path d="{{bmC1}}" fill="var(--t-high)" stroke="var(--card)" stroke-width="1"></path>'
'<path d="{{bmC2}}" fill="var(--ink-3)" stroke="var(--card)" stroke-width="1"></path>'
'<path d="{{bmS0}}" fill="var(--t-low)" stroke="#7c3aed" stroke-width="1.6"></path>'
'<path d="{{bmS1}}" fill="var(--t-high)" stroke="#7c3aed" stroke-width="1.6"></path>'
'<path d="{{bmS2}}" fill="var(--ink-3)" stroke="#7c3aed" stroke-width="1.6"></path>'
'<path d="{{bmSug}}" fill="none" stroke="var(--t-in)" stroke-width="2" stroke-dasharray="4 3"></path>'
'<path d="{{bmSelRingC}}" fill="#0e7490" fill-opacity="0.12" stroke="#0e7490" stroke-opacity="0.6"></path>'
'<path d="{{bmSelDotC}}" fill="#0e7490" stroke="#ffffff" stroke-width="2"></path>'
'<path d="{{bmSelRingS}}" fill="#7c3aed" fill-opacity="0.12" stroke="#7c3aed" stroke-opacity="0.6"></path>'
'<path d="{{bmSelDotS}}" fill="#7c3aed" stroke="#ffffff" stroke-width="2"></path>'
'</svg></div>'
'<div class="ap-seg" role="group" aria-label="Ansicht drehen"><sc-for list="{{bmTurns}}" as="t" hint-placeholder-count="4"><button type="button" class="ap-segb" onClick="{{t.go}}">{{t.n}}</button></sc-for></div>'
'<p class="ap-small" style="margin: 0; line-height: 1.4">{{bmHint}}</p>'
'<div class="ap-info">'
'<sc-if value="{{bmHasSel}}" hint-placeholder-val="{{false}}"><div class="ap-row"><span class="ap-txt"><b>{{bmSelName}}</b>{{bmSelDist}}</span><button type="button" class="ap-btn" onClick="{{bmClear}}">Entfernen</button></div>'
'<sc-if value="{{bmHasWarn}}" hint-placeholder-val="{{false}}"><p class="ap-warn">{{bmWarn}}</p></sc-if></sc-if>'
'<sc-if value="{{bmHasSug}}" hint-placeholder-val="{{true}}"><div class="ap-row"><span class="ap-txt">Vorschlag: <b>{{bmSugName}}</b>, am weitesten weg von deinen letzten Stellen.</span><button type="button" class="ap-btn" onClick="{{bmTakeSug}}">Übernehmen</button></div></sc-if>'
'<div class="ap-leg"><span><i class="dot" style="background: var(--t-low)"></i>bis 3 Tage</span><span><i class="dot" style="background: var(--t-high)"></i>4–13 Tage</span><span><i class="dot" style="background: var(--ink-3)"></i>14–30 Tage</span><span><i class="dot" style="border: 2px solid #7c3aed; border-radius: 3px; background: none"></i>Sensor</span><span><i class="dot" style="border: 2px dashed var(--t-in); background: none"></i>Vorschlag</span></div>'
'</div></div></div>'
)


BODYMAP = (
'<div class="card bm-card rv">'
'<div class="bm-text">'
'<span class="bm-ico">' + ico(ICONS["katheter"]).replace('class="ico"', 'class="ico" style="color: currentColor"') + '</span>'
'<h3 class="h2c" style="margin-top: 24px">Körperkarte</h3>'
'<p class="lead" style="margin-top: 12px">Wechsel von Katheter und Schlauch mit Einstichstelle auf einer drehbaren Körperkarte, mit Erinnerung an frühere Stellen und Abstandswarnung.</p>'
'<p class="try">' + ico(ICONS["drehen"]).replace('class="ico"', 'class="ico" style="width: 20px; height: 20px; color: currentColor"') + 'Probier es selbst: Dreh den Körper und tipp auf eine Stelle.</p>'
'</div>'
'<div class="bm-stage">' + ring(760, (0.16, 0.11, 0.07, 0.04)) + SCREEN + '</div>'
'</div>\n'
)


def ways():
    data = [
        ("var(--story-indigo)", "Community", "Erzähl mir, was dir an deinen Daten fehlt. Jede Rückmeldung macht Glycodex besser.", "askRueck", "Schreib mir"),
        ("var(--story-nacht)", "Unternehmen der Medizintechnik", "Konzept, Prototyp und die Sicht einer Patientin. Das Kurzprofil schicke ich dir gern.", "askProfil", "Kurzprofil anfragen"),
        ("var(--story-petrol)", "Diabetes-Teams", "Wie Glycodex rechnet und was der Report zeigt, steht in einer Kurzinformation.", "askInfo", "Kurzinfo anfragen"),
    ]
    out = ""
    for i, (col, h, p, fn, lbl) in enumerate(data):
        out += ('<div class="kway rv" style="--d: %dms"><span class="dot" style="background: %s" aria-hidden="true"></span>'
                '<h3 class="h3">%s</h3><p class="body">%s</p>'
                '<button type="button" class="btn btn-s" onClick="{{%s}}" style="align-self: flex-start; margin-top: 6px">%s</button></div>'
                % (i * 80, col, h, p, fn, lbl))
    return out


BODY = (
# Einstieg
'<section class="hero" aria-labelledby="h-hero">\n<div class="wrap">\n'
'<p class="eye">Privates Diabetes-Tagebuch</p>\n'
'<h1 id="h-hero" class="display">Deine Diabetes&shy;daten. Endlich verständlich.</h1>\n'
'<p class="lead">Glycodex macht aus den Daten von Pumpe und Sensor eine ruhige Übersicht, ein Tagebuch und persönliche Muster. Entwickelt von einer Patientin mit Typ-1-Diabetes, für den Alltag mit Closed Loop.</p>\n'
'<div class="btns"><a class="btn btn-p btn-l" href="#funktionen">Glycodex entdecken</a><a class="btn btn-s btn-l" href="#kontakt">Kontakt aufnehmen</a></div>\n'
'<div class="metrics">'
'<div class="metric"><b>288</b><span>Sensorwerte am Tag, geordnet</span></div>'
'<div class="metric"><b>5</b><span>Bereiche nach internationalem Konsens</span></div>'
'<div class="metric"><b>0</b><span>Dosistipps, versprochen</span></div></div>\n'
'<div class="stage rise">' + ring(840, style="") +
'<div class="duo">' + phone("uebersicht", 280, "pa", eager=True) + phone("tagesverlauf", 256, "pb", eager=True) + '</div>'
'<div class="stage-cos swipe">'
+ callout("5 Bereiche nach internationalem Konsens", "Zeit im Zielbereich, Glukoseprofil und Kennzahlen. Mit deinem persönlichen Zielbereich daneben.", "r", 134, "").replace('class="co"', 'class="co co-hl"')
+ callout("Gefühl trifft Werte", "Stimmung, Tags und Notizen stehen direkt neben dem Tagesverlauf.", "l", 134, "").replace('class="co"', 'class="co co-hr"')
+ '</div></div>\n'
'<p class="note">Alle Abbildungen zeigen erfundene Testdaten.</p>\n'
'</div>\n</section>\n'

# Warum
'<section class="sec" aria-labelledby="h-warum" style="padding-top: 0">\n' + band(72) +
'<div class="wrap split" style="grid-template-columns: 42fr 58fr; margin-top: 40px">\n'
'<div class="sticky"><p class="eye">Warum Glycodex</p><h2 id="h-warum" class="h2">Rund 26.000 Werte in drei Monaten. Und kaum Antworten.</h2></div>\n'
'<div class="stack swipe" style="gap: 20px">'
'<div class="card rv"><span class="num">01</span><h3 class="h3" style="margin-top: 14px">Viele Daten, wenig Verständnis</h3><p class="body" style="margin-top: 8px">Portale zeigen die Werte. Was sie über deinen Alltag sagen, bleibt oft offen.</p></div>'
'<div class="card rv" style="--d: 80ms"><span class="num">02</span><h3 class="h3" style="margin-top: 14px">Der Closed Loop arbeitet unsichtbar</h3><p class="body" style="margin-top: 8px">Wann der Algorithmus eingreift und was danach passiert, ist im Alltag kaum nachzuvollziehen.</p></div>'
'<div class="card rv" style="--d: 160ms"><span class="num">03</span><h3 class="h3" style="margin-top: 14px">Gefühl und Werte getrennt</h3><p class="body" style="margin-top: 8px">Wie sich ein Tag angefühlt hat, steht nirgends neben dem, was der Sensor gemessen hat.</p></div>'
'</div>\n</div>\n</section>\n'

# Funktionen
'<section id="funktionen" class="sec" aria-labelledby="h-fn">\n<div class="wrap">\n'
'<div class="center mx" style="max-width: 640px"><p class="eye">Was Glycodex kann</p><h2 id="h-fn" class="h2">Alles, was du über deine Werte wissen willst. Ruhig erzählt.</h2></div>\n'
'<div class="g2" style="margin-top: 48px">'
'<div class="card feat-wide rv"><div><h3 class="h3">Ruhige Übersicht</h3><p class="body" style="margin-top: 8px">Zeit im Zielbereich, Glukoseprofil und Kennzahlen nach dem internationalen Konsens. Mit deinem persönlichen Zielbereich daneben.</p></div>'
'<div class="zoom"><img src="' + IMG["uebersicht"] + '" alt="Zeit im Zielbereich in der Übersicht von Glycodex" loading="lazy" style="top: -176px"></div></div>'
'<div class="card feat-wide rv" style="--d: 80ms"><div><h3 class="h3">Auto-Modus sichtbar</h3><p class="body" style="margin-top: 8px">Glycodex zeigt, wann der Closed Loop die Abgabe erhöht oder pausiert hat und was danach passiert ist. Beschrieben, nicht bewertet.</p></div>'
'<div class="zoom"><img src="' + IMG["automodus"] + '" alt="Auswertung des Auto-Modus in Glycodex" loading="lazy" style="top: -176px"></div></div>'
'</div>\n<div class="g2 swipe" style="margin-top: 24px">'
'<div class="card rv">' + ico(ICONS["gefuehl"]) + '<h3 class="h3" style="margin-top: 16px">Gefühl trifft Werte</h3><p class="body" style="margin-top: 8px">Stimmung, Tags und Notizen stehen im Tagebuch direkt neben dem Tagesverlauf von Glukose, Insulin, Essen und Bewegung.</p></div>'
'<div class="card rv" style="--d: 80ms">' + ico(ICONS["codex"]) + '<h3 class="h3" style="margin-top: 16px">Dein Codex</h3><p class="body" style="margin-top: 8px">Persönliche Muster als nummerierte Seiten, jeweils mit der Angabe, wie gefestigt sie sind. Ein Nachschlagewerk über dich.</p></div>'
'<div class="card rv">' + ico(ICONS["dextro"]) + '<h3 class="h3" style="margin-top: 16px">Dextro, dein Begleiter</h3><p class="body" style="margin-top: 8px">Ein KI-Begleiter, der deine Daten kennt und in normaler Sprache antwortet. Ohne Dosis- oder Therapieempfehlungen.</p></div>'
'<div class="card rv" style="--d: 80ms">' + ico(ICONS["team"]) + '<h3 class="h3" style="margin-top: 16px">Für dein Diabetes-Team</h3><p class="body" style="margin-top: 8px">Ein Report als PDF und Lesezugänge, auch als Einmal-Link für einen Termin. Du entscheidest, wer was sieht.</p></div>'
'</div>\n'
+ BODYMAP +
'</div>\n</section>\n'

# So funktioniert's
'<section id="ablauf" class="sec" aria-labelledby="h-ab">\n<div class="wrap">\n'
'<p class="eye">So funktioniert\'s</p><h2 id="h-ab" class="h2" style="max-width: 760px">Vom Export zur Übersicht in drei Schritten.</h2>\n'
'<div class="card rv" style="position: relative; overflow: hidden; margin-top: 40px; padding: 48px">'
+
'<ol class="steps3">'
'<li><span class="spill">1</span><h3 class="h3">Exportieren</h3><p class="body">Die Daten von Pumpe und Sensor laufen in Glooko zusammen. Von dort kommt der Export, als Datei zum Herunterladen.</p></li>'
'<li><span class="spill">2</span><h3 class="h3">Hochladen und ergänzen</h3><p class="body">Glycodex liest den Export ein und ordnet die Werte. Dazu kommen eigene Einträge wie Stimmung, Notizen, Bewegung und Blutdruck.</p></li>'
'<li><span class="spill">3</span><h3 class="h3">Verstehen</h3><p class="body">Übersicht, Tagebuch, Muster und Codex zeigen, was in den Daten steckt. Für den nächsten Termin gibt es den Report als PDF.</p></li>'
'</ol></div>\n'
'<p class="small" style="margin-top: 20px; max-width: 760px">Warum ein Export? Für Privatpersonen gibt es bei Glooko keine öffentliche Schnittstelle. Glycodex arbeitet deshalb mit dem manuellen Export und zeigt keine Echtzeitdaten.</p>\n'
'</div>\n</section>\n'

# Einblick
'<section class="sec" aria-labelledby="h-ein">\n<div class="wrap">\n'
'<div class="center"><p class="eye">Einblick</p><h2 id="h-ein" class="h2">So sieht dein Alltag in Glycodex aus.</h2><p class="small" style="margin-top: 12px">Abbildungen mit erfundenen Testdaten</p></div>\n'
'<div class="show-row4 swipe">'
+ "".join('<figure class="show rv" style="--d: %dms">' % (i * 80) + phone(k, 240) + '<figcaption><h3 class="h3">%s</h3><p class="body" style="margin-top: 6px">%s</p></figcaption></figure>' % (t, x)
  for i, (k, t, x) in enumerate([
    ("zielbereich", "Zeit im Zielbereich", "Nach Konsens, mit deinem persönlichen Zielbereich daneben."),
    ("tagesverlauf", "Tagesverlauf", "Glukose, Insulin, Essen und Bewegung in einem Verlauf, daneben Stimmung und Notizen."),
    ("codex", "Dein Codex", "Persönliche Muster als nummerierte Seiten, jeweils mit der Angabe, wie gefestigt sie sind."),
    ("dextro", "Dextro", "Antwortet in normaler Sprache. Ohne Dosis- oder Therapieempfehlungen.")])) +
'</div>\n</div>\n</section>\n\n'

# Haltung
'<section id="haltung" class="halt-band" aria-labelledby="h-hl">' + ring(980, (0.24, 0.16, 0.10, 0.06), "right: -300px; top: -300px", white=True) +
'<div class="wrap" style="position: relative">'
'<p class="eye">Haltung</p><h2 id="h-hl" class="h2 halt-h">Gebaut von jemandem, der weiß, wie sich ein holpriger Tag anfühlt.</h2>'
'<div class="vals swipe">'
'<div class="val rv"><h3 class="h3">Beschreiben statt bewerten</h3><p class="body" style="margin-top: 8px">Ein Tag ist holprig, nie schlecht. Glycodex sagt, was in den Daten steht, und sucht keine Schuld.</p></div>'
'<div class="val rv" style="--d: 80ms"><h3 class="h3">Dranbleiben zählt</h3><p class="body" style="margin-top: 8px">XP gibt es fürs Eintragen und Dabeibleiben, nicht für Werte. Abzeichen feiern die guten Tage.</p></div>'
'<div class="val rv" style="--d: 160ms"><h3 class="h3">Deine Daten gehören dir</h3><p class="body" style="margin-top: 8px">Verschlüsselt auf einem eigenen Server, ohne Werbung. Wer Zugang bekommt, entscheidest du.</p></div>'
'<div class="val rv" style="--d: 240ms"><h3 class="h3">Klinisch sauber</h3><p class="body" style="margin-top: 8px">Bereiche, Zielwerte und Kennzahlen folgen internationalen Empfehlungen. Reichen die Daten nicht, sagt Glycodex das offen.</p></div>'
'</div></div>\n</section>\n\n'

# Für wen
'<section class="sec" aria-labelledby="h-fw">\n<div class="wrap">\n'
'<p class="eye">Für wen</p><h2 id="h-fw" class="h2">Heute mein Tagebuch. Gedacht für viele.</h2>'
'<p class="lead" style="margin-top: 16px; max-width: 680px">Glycodex ist aus meinem eigenen Alltag entstanden. Die Fragen, die es beantwortet, haben viele Menschen mit Diabetes.</p>\n'
'<div class="who1" style="margin-top: 40px">'
'<div class="story st-indigo rv">' + ring(420, (0.08, 0.07, 0.06, 0.05), "right: -140px; bottom: -140px", white=True) +
'<div style="position: relative; display: flex; flex-direction: column; gap: 24px">'
'<div><h3 class="h3">Menschen mit Sensor und Pumpe</h3><p class="body" style="margin-top: 8px">Getestet mit YpsoPump, CamAPS FX und Dexcom G7. Die Daten kommen aus dem Glooko-Export.</p></div>'
'<div><h3 class="h3">Alle, die ihren Closed Loop verstehen wollen</h3><p class="body" style="margin-top: 8px">Was tut der Algorithmus, und was kann ich selbst noch verbessern?</p></div>'
'</div></div>'
'<div class="frame-box rv" style="--d: 80ms"><span class="num" style="min-width: 0">Offener Stand</span><h3 class="h3" style="margin-top: 14px">Ehrlich gesagt</h3>'
'<p class="body" style="margin-top: 8px">Glycodex ist heute ein privates Projekt, das ich selbst jeden Tag nutze. Es ist kein Medizinprodukt und wird nicht zum Download angeboten. Damit es vielen helfen kann, suche ich Partnerschaften in Medizintechnik und Community.</p></div>'
'</div>\n'
'<div class="who2 swipe">'
'<div class="story st-petrol rv"><h3 class="h3">Diabetes-Teams</h3><p class="body" style="margin-top: 8px">Ein klarer Report vor dem Termin, ein Lesezugang statt Zettelwirtschaft.</p>'
'<a class="btn btn-s" href="Fachkreise.dc.html" style="margin-top: 20px">Mehr für Diabetes-Teams</a></div>'
'<div class="story st-nacht rv" style="--d: 80ms"><h3 class="h3">Unternehmen der Medizintechnik</h3><p class="body" style="margin-top: 8px">Konzept, Prototyp und die Sicht einer Patientin.</p>'
'<a class="btn btn-s" href="Partner.dc.html" style="margin-top: 20px">Mehr zu Partnerschaften</a></div>'
'</div>\n</div>\n</section>\n'

# Über mich
'<section id="ueber" class="sec" aria-labelledby="h-ub">\n<div class="wrap split" style="grid-template-columns: 38fr 62fr; align-items: center">\n'
'<div class="emblem rv">' + ring(560, (0.30, 0.20, 0.12, 0.06), "", white=True) + band(64) +
'<span class="emb-logo"><img src="' + LOGO + '" alt=""></span></div>\n'
'<div><p class="eye">Über mich</p><h2 id="h-ub" class="h2">Ich bin Lina.</h2>'
'<p class="body" style="margin-top: 16px; max-width: 58ch">Ich lebe seit 2013 mit Typ-1-Diabetes. Nach Jahren mit Pen, hohen Werten und viel Müdigkeit nutze ich seit September 2026 einen Closed Loop. Glycodex habe ich in Eigenregie konzipiert, gestaltet und KI-gestützt umgesetzt. Neben meiner Arbeit in einer Kommunalverwaltung beschäftige ich mich intensiv mit KI, Webdesign und App-Entwicklung.</p>'
'<blockquote class="quote"><p>„Ich wollte den 26.000 Sensorwerten eine Darstellung bieten. Sichtbar machen, was die Krankheit in mir so treibt.“</p><footer>Lina Schröder</footer></blockquote>'
'</div>\n</div>\n</section>\n'

# Stand des Projekts
'<section id="stand" class="sec" aria-labelledby="h-st">\n<div class="wrap split" style="grid-template-columns: 34fr 66fr">\n'
'<div class="sticky"><p class="eye">Stand des Projekts</p><h2 id="h-st" class="h2">Aus dem Alltag entstanden. Im Alltag geprüft.</h2></div>\n'
'<ol class="tline">'
'<li class="rv"><span class="tnode" aria-hidden="true"></span><div class="card tcard"><p class="tdate">September 2026</p><h3 class="h3">Der Anstoß</h3><p class="body" style="margin-top: 6px">Mit dem Closed Loop kommt die Frage, was der Algorithmus eigentlich tut.</p></div></li>'
'<li class="rv"><span class="tnode" aria-hidden="true"></span><div class="card tcard"><p class="tdate">Vor dem Bau</p><h3 class="h3">Recherche und Leitlinien</h3><p class="body" style="margin-top: 6px">Vorhandene Apps, Medizinprodukterecht, KI-Verordnung und Datenschutz. Dazu klare Regeln, was Glycodex nie tut.</p></div></li>'
'<li class="rv"><span class="tnode" aria-hidden="true"></span><div class="card tcard"><p class="tdate">Anfang November 2026</p><h3 class="h3">Erste Version</h3><p class="body" style="margin-top: 6px">Übersicht, Tagebuch und Muster laufen mit meinen echten Daten.</p></div></li>'
'<li class="rv now"><span class="tnode now" aria-hidden="true"></span><div class="card tcard"><p class="tdate">11. November 2026</p><h3 class="h3">Live auf eigenem Server</h3><p class="body" style="margin-top: 6px">Mit Anmeldung, verschlüsselter Speicherung und Lesezugang für mein Diabetes-Team.</p></div></li>'
'<li class="rv open"><span class="tnode open" aria-hidden="true"></span><div class="card tcard"><p class="tdate">Als Nächstes</p><h3 class="h3">Partnerschaften und Community</h3><p class="body" style="margin-top: 6px">Gespräche mit der Medizintechnik und der Austausch mit der Diabetes-Community auf Social Media.</p></div></li>'
'</ol>\n</div>\n</section>\n'

# Häufige Fragen
'<section id="fragen" class="sec" aria-labelledby="h-fq">\n<div class="wrap">\n'
'<div class="center"><p class="eye">Häufige Fragen</p><h2 id="h-fq" class="h2">Kurz beantwortet.</h2>'
'<p class="body" style="margin-top: 12px">Deine Frage fehlt? <a class="tl" href="#kontakt">Schreib mir.</a></p></div>\n'
'<div class="card faq rv">'
'<details open><summary>Kann ich Glycodex nutzen?' + PLUS + '</summary><p class="ans">Noch nicht. Glycodex ist ein privates Projekt, das nur ich nutze. Würde ich es an andere weitergeben, wäre es sehr wahrscheinlich ein Medizinprodukt. Dafür braucht es ein Unternehmen mit Qualitätsmanagement und Zulassung. Genau deshalb suche ich Partnerschaften.</p></details>'
'<details><summary>Gibt Glycodex Empfehlungen zur Insulindosis?' + PLUS + '</summary><p class="ans">Nein. Glycodex beschreibt Daten und gibt keine Therapie- oder Dosisempfehlungen. Fragen zur Einstellung formuliert die App nur als Fragen an das Diabetes-Team.</p></details>'
'<details><summary>Mit welchen Geräten funktioniert Glycodex?' + PLUS + '</summary><p class="ans">Getestet ist Glycodex mit YpsoPump, CamAPS FX und Dexcom G7. Die Daten kommen aus dem Export von Glooko. Andere Geräte habe ich bisher nicht getestet.</p></details>'
'<details><summary>Wo liegen die Daten?' + PLUS + '</summary><p class="ans">Verschlüsselt auf meinem eigenen Server. Es gibt eine Anmeldung, Rollen und Lesezugänge. Wer Zugang bekommt, entscheide ich. Werbung gibt es nicht.</p></details>'
'<details><summary>Was ist Dextro?' + PLUS + '</summary><p class="ans">Dextro ist der KI-Begleiter in Glycodex. Er kennt die Daten und beantwortet Fragen in normaler Sprache, ohne Dosis- oder Therapieempfehlungen. Dextro nutzt ein Sprachmodell von Anthropic. Für eine Antwort werden die dafür nötigen Daten an diesen Dienst übermittelt.</p></details>'
'<details><summary>Wer steht hinter Glycodex?' + PLUS + '</summary><p class="ans">Ich, Lina Schröder, als Privatperson. Glycodex ist unabhängig und steht in keiner Verbindung zu den genannten Unternehmen.</p></details>'
'<details><summary>Wie kann ich helfen?' + PLUS + '</summary><p class="ans">Erzähl mir, was dir an deinen Daten fehlt, und teile Glycodex mit Menschen, die es interessieren könnte. Wenn du in der Medizintechnik arbeitest, freue ich mich über ein erstes Gespräch.</p></details>'
'</div>\n</div>\n</section>\n'

# Kontakt
'<section id="kontakt" class="sec" aria-labelledby="h-kt">\n<div class="wrap">\n'
'<div class="card kstage">' + ring(900, (0.18, 0.12, 0.08, 0.05)) +
'<div style="position: relative"><p class="eye">Kontakt</p><h2 id="h-kt" class="h2" style="font-size: clamp(28px, 4vw, 40px)">Lass uns sprechen.</h2>'
'<div class="g3 swipe" style="margin-top: 36px; gap: 20px">' + ways() + '</div>'
'<p class="small" style="margin-top: 36px">Oder direkt:</p><div class="kfoot">'
'<button type="button" class="btn btn-p btn-l" onClick="{{askMail}}">' + ico(ICONS["mail"]).replace('class="ico"', 'class="ico" style="width: 20px; height: 20px; color: currentColor"') + 'lina.schroeder@autarkflow.de</button>'
+ phone_reveal("btn btn-s btn-l") + '</div>'
+ hint("mailAt_kontakt", "kontakt") + '<div style="display: flex; justify-content: center; margin-top: 24px">' + insta() + '</div>' +
'</div></div>\n</div>\n</section>\n'
)

ASKS = [("askRueck", "Rückmeldung", "kontakt"), ("askProfil", "Kurzprofil", "kontakt"),
        ("askInfo", "Kurzinformation", "kontakt"), ("askMail", "", "kontakt")]

BM_JS = open("/home/claude/web/build/bodymap.js", encoding="utf-8").read()
HTML = page("Glycodex – Privates Diabetes-Tagebuch", BODY, "main", ASKS, 10600, MAIN_CSS, BM_JS, "...this.bmVals(),\n")
