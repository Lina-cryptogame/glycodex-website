from common import *

SUB_CSS = r"""
.shero{padding:48px 0 48px}
.shero .story{padding:64px;display:grid;gap:40px;align-items:center}
.shero .ring{left:auto;right:-160px;top:50%;transform:translateY(-50%)}
.shero .pics{position:relative;display:flex;justify-content:center;align-items:flex-start}
.wichtig{margin-top:28px;padding:16px 20px;border-radius:14px;background:rgba(255,255,255,0.12);font-size:15px;line-height:1.55;color:#ffffff}
.dlc{margin:0;padding:0}
.dlc > div{display:grid;grid-template-columns:34fr 66fr;gap:24px;padding:22px 28px;border-top:1px solid var(--line)}
.dlc > div:first-child{border-top:0}
.dlc dt{font-size:16px;font-weight:500;color:var(--ink)}
.dlc dd{margin:0;font-size:16px;line-height:1.6;color:var(--ink-2)}
.list{margin:12px 0 0;padding:0 0 0 20px;font-size:16px;line-height:1.6;color:var(--ink-2)}
.list li{margin-bottom:4px}
.dots{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:12px}
.dots li{position:relative;padding-left:22px;font-size:17px;line-height:1.5;font-weight:500;color:var(--ink)}
.dots li::before{content:"";position:absolute;left:0;top:9px;width:8px;height:8px;border-radius:50%;background:var(--accent)}
.okpill{display:inline-flex;align-items:center;gap:8px;padding:6px 12px;border-radius:999px;background:var(--ok-bg);color:var(--ok-ink);font-size:13px;font-weight:500}
.okpill::before{content:"";width:8px;height:8px;border-radius:50%;background:currentColor}
.kstage{position:relative;overflow:hidden;padding:64px;text-align:center}
.kstage .ring{left:auto;right:-420px;top:-420px;transform:none}
.kstage .btns{justify-content:center;margin-top:28px}
.kstage .hint{margin-left:auto;margin-right:auto}
@media (max-width:767px){
.shero{padding:24px 0 28px}
.shero .story{padding:32px 20px !important;grid-template-columns:minmax(0,1fr) !important}
.shero .pics .phone{width:210px !important}
.shero .pics .pb{display:none}
.dlc > div{grid-template-columns:minmax(0,1fr);gap:6px;padding:18px 20px}
.kstage{padding:32px 20px}
.grenz{flex-direction:column}
.wide-story{grid-template-columns:minmax(0,1fr) !important;padding:24px 20px !important}
}
"""


def kontakt(h2, text, label, fn):
    return ('<section id="kontakt" class="sec" aria-labelledby="h-kt">\n<div class="wrap">\n'
            '<div class="card kstage">' + ring(900, (0.18, 0.12, 0.08, 0.05)) +
            '<div style="position: relative"><p class="eye">Kontakt</p>'
            '<h2 id="h-kt" class="h2 mx" style="max-width: 760px">' + h2 + '</h2>'
            '<p class="lead mx" style="margin-top: 16px; max-width: 640px">' + text + '</p>'
            '<div class="btns"><button type="button" class="btn btn-p btn-l" onClick="{{' + fn + '}}">' + label + '</button>'
            + phone_reveal("btn btn-s btn-l") + '</div>'
            + hint("mailAt_bottom", "bottom") +
            '</div></div>\n</div>\n</section>\n')


# ---------- Für Diabetes-Teams ----------
TEAMS = (
'<section class="shero" aria-labelledby="h-top">\n<div class="wrap">\n'
'<div class="story st-petrol" style="grid-template-columns: 62fr 38fr">' + ring(720, (0.10, 0.08, 0.06, 0.04), "", white=True) +
'<div style="position: relative">'
'<p class="eye">Für Diabetes-Teams</p>'
'<h1 id="h-top" class="h1s">Nachvollziehbar gerechnet. Ruhig dargestellt.</h1>'
'<p class="lead" style="margin-top: 20px">Glycodex ist ein privates Diabetes-Tagebuch, das ich als Patientin mit Typ-1-Diabetes selbst konzipiert und umgesetzt habe. Hier steht, was die App zeigt, wie sie rechnet und was sie bewusst nicht tut.</p>'
'<div class="btns" style="margin-top: 28px"><button type="button" class="btn btn-p btn-l" onClick="{{askTop}}">Kurzinformation anfragen</button><a class="btn btn-s btn-l" href="#methodik">Zur Methodik</a></div>'
+ hint("mailAt_top", "top") +
'<p class="wichtig"><b style="font-weight: 500">Wichtig:</b> Glycodex beschreibt Daten. Die App gibt keine Therapie- oder Dosisempfehlungen und ist kein Medizinprodukt. Fragen zur Einstellung formuliert sie nur als Fragen an das Diabetes-Team.</p>'
'</div>'
'<div class="pics rise">' + phone("zielbereich", 240, eager=True) + '</div>'
'</div>\n</div>\n</section>\n'

'<section class="sec" aria-labelledby="h-zeigt">\n<div class="wrap">\n'
'<p class="eye">Was Glycodex zeigt</p><h2 id="h-zeigt" class="h2" style="max-width: 760px">Vier Bereiche, eine Datengrundlage.</h2>'
'<p class="lead" style="margin-top: 16px; max-width: 760px">Grundlage sind die Exporte aus Glooko mit den Daten von YpsoPump, CamAPS FX und Dexcom G7. Dazu kommen eigene Einträge wie Stimmung, Notizen, Bewegung und Blutdruck.</p>\n'
+ band(32, "margin-top: 32px") +
'<div class="g2 swipe" style="margin-top: 24px">'
'<div class="card rv"><span class="num">01</span><h3 class="h3" style="margin-top: 14px">Übersicht</h3><p class="body" style="margin-top: 8px">Zeit in den Bereichen, wahlweise nach Konsens oder persönlichem Zielbereich, und Glukoseprofil (AGP).</p></div>'
'<div class="card rv" style="--d: 80ms"><span class="num">02</span><h3 class="h3" style="margin-top: 14px">Tagebuch</h3><p class="body" style="margin-top: 8px">Tagesverlauf mit Glukose, Bolus, Basal, Kohlenhydraten, Bewegung und eigenen Einträgen.</p></div>'
'<div class="card rv"><span class="num">03</span><h3 class="h3" style="margin-top: 14px">Muster · Klinik</h3><p class="body" style="margin-top: 8px">Kennzahlen, Ereignisse, Hypo-Analyse, Nacht und Tagesprofile.</p></div>'
'<div class="card rv" style="--d: 80ms"><span class="num">04</span><h3 class="h3" style="margin-top: 14px">Muster · Technik</h3><p class="body" style="margin-top: 8px">Auswertung des Auto-Modus. Die Ereignisse sind aus Basal und Glukose abgeleitet und stehen so nicht im Export.</p></div>'
'</div>\n</div>\n</section>\n'

'<section id="methodik" class="sec" aria-labelledby="h-mt">\n<div class="wrap split" style="grid-template-columns: 32fr 68fr">\n'
'<div class="sticky"><p class="eye">Methodik</p><h2 id="h-mt" class="h2">So rechnet Glycodex.</h2>'
'<p class="body" style="margin-top: 16px">Die Kennzahlen habe ich gegen eine unabhängige Referenzrechnung geprüft.</p></div>\n'
'<div class="card rv" style="padding: 0"><dl class="dlc">'
'<div><dt>Grundlage</dt><dd>Internationaler Konsens zur Zeit im Zielbereich (Battelino et al., Diabetes Care 2019) und Konsens zu CGM-Kennzahlen (Battelino et al., Lancet Diabetes Endocrinol 2023)</dd></div>'
'<div><dt>Datenbasis</dt><dd>Mindestens 14 Tage und 70 % Sensorzeit. Sonst weist die App darauf hin.</dd></div>'
'<div><dt>Ereignisse</dt><dd>Beginn und Ende nach 15 Minuten. Verlängerte Hypoglykämie über 120 Minuten. Verlängerte Hyperglykämie bei 90 von 120 Minuten über 13,9 mmol/L.</dd></div>'
'<div><dt>Abgeleitete Werte</dt><dd>GMI nach Bergenstal et al. 2018, GRI nach Klonoff et al. 2023</dd></div>'
'<div><dt>Datenbesonderheiten</dt><dd>Werte über dem Messbereich zählen als „sehr hoch“. Bei doppelter Aufzeichnung gilt der Wert aus CamAPS.</dd></div>'
'<div><dt>Zielbereich</dt><dd>Konsens (3,9 bis 10,0 mmol/L) oder ein frei einstellbarer persönlicher Zielbereich. Im Report bleibt der Konsens der Standard.</dd></div>'
'</dl></div>\n</div>\n</section>\n'

'<section class="sec" aria-labelledby="h-rp">\n<div class="wrap">\n'
'<p class="eye">Für den Termin</p><h2 id="h-rp" class="h2">Ansehen statt Zettel.</h2>\n'
'<div class="g3 swipe" style="margin-top: 40px">'
'<div class="card rv">' + ico(ICONS["report"]) + '<h3 class="h3" style="margin-top: 16px">Der Report als PDF</h3>'
'<p class="body" style="margin-top: 8px">Für Termine erstellt Glycodex einen Report, der die wichtigsten Seiten auf einen Blick zusammenfasst.</p>'
'<ul class="list"><li>Kennzahlen nach Konsens</li><li>Glukoseprofil und Tageszeiten</li><li>Fragen an das Diabetes-Team</li><li>Tagesprofile</li><li>Auswertung des Auto-Modus</li></ul></div>'
'<div class="card rv" style="--d: 80ms">' + ico(ICONS["zugang"]) + '<h3 class="h3" style="margin-top: 16px">Lesezugang</h3>'
'<p class="body" style="margin-top: 8px">Eigener Zugang mit Passwort. Nur ansehen, keine Änderungen möglich.</p></div>'
'<div class="card rv" style="--d: 160ms">' + ico(ICONS["link"]) + '<h3 class="h3" style="margin-top: 16px">Einmal-Link</h3>'
'<p class="body" style="margin-top: 8px">Für einen einzelnen Termin. Der Link funktioniert genau einmal und gibt danach für einige Stunden Zugriff.</p></div>'
'</div>\n'
'<p class="small" style="display: flex; align-items: center; gap: 10px; margin-top: 20px">' + ico(ICONS["schloss"]).replace('class="ico"', 'class="ico" style="width: 20px; height: 20px"') + 'Die Daten liegen verschlüsselt auf meinem eigenen Server. Wer Zugang hat, entscheide ich.</p>\n'
'</div>\n</section>\n'

'<section class="sec" aria-labelledby="h-gr">\n<div class="wrap">\n'
'<div class="frame-box grenz mx rv" style="max-width: 920px; padding: 36px 44px; display: flex; gap: 24px">'
+ ico(ICONS["info"]) +
'<div><p class="eye">Grenzen</p><h2 id="h-gr" class="h2">Was Glycodex nicht ist.</h2>'
'<ul class="list" style="margin-top: 16px"><li>Kein Medizinprodukt und kein Ersatz für die Beurteilung durch das Diabetes-Team</li>'
'<li>Abhängig vom manuellen Glooko-Export, keine Echtzeitdaten</li>'
'<li>Die Auswertung des Auto-Modus ist eine abgeleitete Beobachtung, keine Angabe der Herstellerfirma</li></ul></div>'
'</div>\n</div>\n</section>\n'

+ kontakt("Rückmeldungen aus fachlicher Sicht nehme ich sehr gerne auf.",
          "Die Kurzinformation für Diabetes-Teams schicke ich dir gern zu. Auf Wunsch zeige ich Glycodex auch in einer Live-Demo mit Testdaten.",
          "Kurzinformation anfragen", "askBottom")
)

TEAMS_HTML = page("Glycodex für Diabetes-Teams", TEAMS, "teams",
                  [("askTop", "Kurzinformation", "top"), ("askBottom", "Kurzinformation", "bottom")], 4300, SUB_CSS)


# ---------- Für Partner ----------
PARTNER = (
'<section class="shero" aria-labelledby="h-top">\n<div class="wrap">\n'
'<div class="story st-nacht" style="grid-template-columns: 60fr 40fr">' + ring(720, (0.08, 0.07, 0.05, 0.04), "", white=True) +
'<div style="position: relative">'
'<p class="eye">Für Unternehmen der Medizintechnik</p>'
'<h1 id="h-top" class="h1s">Diabetesdaten aus Sicht einer Patientin. Mit funktionierendem Prototyp.</h1>'
'<p class="lead" style="margin-top: 20px">Glycodex liest die Exporte aus Glooko ein und macht aus Pumpen- und Sensordaten eine ruhige, verständliche Übersicht. Ich nutze die App jeden Tag. Damit sie vielen helfen kann, suche ich Partnerschaften.</p>'
'<div class="btns" style="margin-top: 28px"><button type="button" class="btn btn-p btn-l" onClick="{{askTop}}">Kurzprofil anfragen</button><a class="btn btn-s btn-l" href="#suche">Was ich suche</a></div>'
+ hint("mailAt_top", "top") +
'</div>'
'<div class="pics rise">' + phone("uebersicht", 200, "pa", eager=True, style=" position: relative; z-index: 2") + phone("dextro", 200, "pb", eager=True, style=" margin-left: -56px; margin-top: 48px") + '</div>'
'</div>\n</div>\n</section>\n'

'<section class="sec" aria-labelledby="h-al">\n<div class="wrap g2" style="align-items: stretch">\n'
'<div class="card rv" style="padding: 36px"><p class="eye">Ausgangslage</p><h2 id="h-al" class="h2c">288 Werte am Tag. Gezeigt, aber kaum erklärt.</h2>'
'<div class="stack" style="gap: 20px; margin-top: 24px">'
'<div><h3 class="h3">Viele Daten, wenig Verständnis</h3><p class="body" style="margin-top: 6px">Die vorhandenen Portale zeigen die Werte, erklären sie aber kaum aus Sicht der Menschen, die damit leben.</p></div>'
'<div><h3 class="h3">Der Closed Loop bleibt unsichtbar</h3><p class="body" style="margin-top: 6px">Wann und wie der Algorithmus eingreift, ist im Alltag schwer nachzuvollziehen.</p></div>'
'<div><h3 class="h3">Befinden und Werte getrennt</h3><p class="body" style="margin-top: 6px">In meiner Recherche fand ich keine App, die Stimmung, Notizen und Alltag so mit den gemessenen Werten verbindet.</p></div>'
'<div><h3 class="h3">Datenweg</h3><p class="body" style="margin-top: 6px">Bei CamAPS laufen die Daten über Glooko. Für Privatpersonen gibt es dort keine öffentliche Schnittstelle, nur den manuellen Export.</p></div>'
'</div></div>'
'<div class="card rv" style="--d: 80ms; padding: 36px"><div style="display: flex; flex-wrap: wrap; gap: 10px; align-items: center"><p class="eye" style="margin: 0">Stand heute</p><span class="okpill">Täglich genutzt</span></div>'
'<h2 class="h2c" style="margin-top: 16px">Ein Prototyp im echten Alltag.</h2>'
'<dl class="dlc" style="margin: 16px -36px 0">'
'<div><dt>Technik</dt><dd>Web-App auf eigenem Server, verschlüsselte Speicherung, Rollen, Lesezugänge und Einmal-Links</dd></div>'
'<div><dt>Daten</dt><dd>Glooko-Export, manuell hochgeladen, dazu eigene Einträge</dd></div>'
'<div><dt>Geräte</dt><dd>Getestet mit YpsoPump, CamAPS FX und Dexcom G7</dd></div>'
'<div><dt>Prüfung</dt><dd>Kennzahlen gegen eine unabhängige Referenzrechnung geprüft. Safari noch nicht systematisch getestet.</dd></div>'
'<div><dt>Rechtlicher Status</dt><dd>Kein Medizinprodukt, reine Eigennutzung</dd></div>'
'</dl><p class="body" style="margin-top: 16px"><a class="tl" href="Main.dc.html#funktionen">Alle Funktionen auf der Startseite</a></p></div>'
'</div>\n</section>\n'

'<section class="sec" aria-labelledby="h-rg">\n<div class="wrap">\n'
'<div class="story st-indigo wide-story rv" style="display: grid; grid-template-columns: 42fr 58fr; gap: 48px; padding: 40px 48px">'
+ ring(520, (0.08, 0.07, 0.05, 0.04), "right: -180px; top: -180px", white=True) +
'<div style="position: relative"><p class="eye">Warum Partnerschaften</p><h2 id="h-rg" class="h2">Für viele braucht es mehr als eine Idee.</h2></div>'
'<p class="lead" style="position: relative; align-self: center">Würde ich Glycodex an andere weitergeben, wäre es sehr wahrscheinlich ein Medizinprodukt. Dafür braucht es ein Unternehmen mit Qualitätsmanagement, Zulassung und direktem Zugang zu den Gerätedaten.</p>'
'</div>\n</div>\n</section>\n'

'<section class="sec" aria-labelledby="h-mb">\n<div class="wrap">\n'
'<p class="eye">Was ich mitbringe</p><h2 id="h-mb" class="h2" style="max-width: 760px">Die Sicht von innen. Und die Arbeit dahinter.</h2>\n'
'<div class="g3 swipe" style="margin-top: 40px; gap: 20px">'
'<div class="card rv" style="padding: 28px"><span class="num">01</span><h3 class="h3" style="margin-top: 14px">Patientinnensicht</h3><p class="body" style="margin-top: 8px">Die Sicht einer Patientin mit Closed Loop, die ihre Daten verstehen will</p></div>'
'<div class="card rv" style="--d: 80ms; padding: 28px"><span class="num">02</span><h3 class="h3" style="margin-top: 14px">Durchdachtes Konzept</h3><p class="body" style="margin-top: 8px">Mit Leitlinien, Markensystem und einer einheitlichen Sprache</p></div>'
'<div class="card rv" style="--d: 160ms; padding: 28px"><span class="num">03</span><h3 class="h3" style="margin-top: 14px">Funktionierender Prototyp</h3><p class="body" style="margin-top: 8px">Täglich genutzt und laufend weiterentwickelt</p></div>'
'<div class="card rv" style="padding: 28px"><span class="num">04</span><h3 class="h3" style="margin-top: 14px">KI-gestützte Umsetzung</h3><p class="body" style="margin-top: 8px">Erfahrung in Konzeption und Gestaltung, beruflich in einem angemeldeten Nebengewerbe</p></div>'
'<div class="card rv" style="--d: 80ms; padding: 28px"><span class="num">05</span><h3 class="h3" style="margin-top: 14px">Nähe zur Community</h3><p class="body" style="margin-top: 8px">Der Plan, die Diabetes-Community auf Social Media zu erreichen</p></div>'
'<div class="card rv" style="--d: 160ms; padding: 28px"><span class="num">06</span><h3 class="h3" style="margin-top: 14px">Dokumentiert</h3><p class="body" style="margin-top: 8px">Das ausführliche Handbuch zur Entstehung sende ich auf Anfrage gern zu.</p></div>'
'</div>\n</div>\n</section>\n'

'<section class="sec" aria-labelledby="h-ws">\n<div class="wrap split" style="grid-template-columns: 34fr 66fr">\n'
'<div class="sticky"><p class="eye">Wie Glycodex entstanden ist</p><h2 id="h-ws" class="h2">In Eigenregie, Schritt für Schritt.</h2>'
'<p class="small" style="margin-top: 16px">Umgesetzt mit Claude von Anthropic. Idee, Anforderungen, Gestaltung, Prüfung und Abnahme jeder Version lagen bei mir.</p></div>\n'
'<ol class="tline">'
+ "".join(
    '<li class="rv"><span class="tnode n" aria-hidden="true">%d</span><div class="card tcard"><h3 class="h3">%s</h3><p class="body" style="margin-top: 6px">%s</p></div></li>' % (i + 1, h, p)
    for i, (h, p) in enumerate([
        ("Recherche vor dem Bau", "Schmerzpunkte von Menschen mit Diabetes, vorhandene Apps, Medizinprodukterecht, KI-Verordnung und Datenschutz"),
        ("Leitlinien festlegen", "Datenschutz zuerst, beschreiben statt bewerten, keine Dosisempfehlungen, ruhige Gestaltung"),
        ("Marke entwickeln", "Name, Logo und ein eigenes Markensystem mit Farben, Schrift und Sprache"),
        ("In kurzen Zyklen umsetzen", "Notizen aus dem Alltag, Vorschläge und Rückfragen, Umsetzung, Prüfung, Freigabe"),
        ("Sicher betreiben", "Eigener Server und eigene Domain, Anmeldung, Rollen, Einmal-Links und Verschlüsselung"),
        ("Feinschliff", "Drei Design-Runden. Vor und nach jeder Änderung wurden alle angezeigten Zahlen verglichen."),
    ])) +
'</ol>\n</div>\n</section>\n'

'<section id="suche" class="sec" aria-labelledby="h-su">\n<div class="wrap">\n'
'<div class="frame-box wide-story rv" style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 48px; padding: 44px 48px; align-items: center">'
'<div><p class="eye">Was ich suche</p><h2 id="h-su" class="h2">Ein erstes Gespräch.</h2>'
'<p class="body" style="margin-top: 16px">Gern zeige ich Glycodex in einer Live-Demo mit Testdaten. Denkbar ist vieles, zum Beispiel:</p></div>'
'<ul class="dots"><li>ein fachlicher Austausch</li><li>die Mitarbeit an einer Oberfläche für Menschen mit Diabetes</li><li>eine Lizenz</li><li>eine Partnerschaft zur Weiterentwicklung</li></ul>'
'</div>\n</div>\n</section>\n'

+ kontakt("Lass uns über Glycodex sprechen.",
          "Das Kurzprofil für Unternehmen der Medizintechnik schicke ich dir gern zu.",
          "Kurzprofil anfragen", "askBottom")
)

PARTNER_HTML = page("Glycodex für Partnerschaften", PARTNER, "partner",
                    [("askTop", "Kurzprofil", "top"), ("askBottom", "Kurzprofil", "bottom")], 4700, SUB_CSS)


# ---------- Rechtstexte ----------
LEGAL_CSS = r"""
.legal-wrap{max-width:760px;margin:0 auto;padding:72px 0 96px}
.draft{margin:0 0 28px;padding:14px 18px;border-radius:14px;background:var(--warn-bg);color:var(--warn-ink);font-size:15px;line-height:1.5}
.lcard{margin-top:28px;padding:48px 56px}
.lcard h2{margin:32px 0 10px;font-size:21px;line-height:1.3;font-weight:500;letter-spacing:-0.01em;color:var(--ink)}
.lcard h2:first-child{margin-top:0}
.lcard p,.lcard ul{margin:0 0 12px;font-size:16px;line-height:1.65;color:var(--ink-2)}
.lcard ul{padding-left:20px}
.lcard li{margin-bottom:4px}
.lcard a{color:var(--accent-dark);text-decoration:underline;text-decoration-thickness:1.5px;text-underline-offset:4px}
.ph{background:var(--warn-bg);color:var(--warn-ink);border-radius:4px;padding:0 4px}
.toc{margin:0 0 32px;padding:20px 24px;border-radius:14px;background:var(--accent-soft)}
.toc p{margin:0 0 8px !important;font-size:14px !important;font-weight:500;color:var(--accent-dark) !important}
.toc ol{margin:0;padding-left:20px;font-size:15px;line-height:1.5}
.toc li{margin:0}
.toc a{display:inline-flex;align-items:center;min-height:36px}
.legal-h1{margin:0;font-size:36px;line-height:1.15;font-weight:500;letter-spacing:-0.02em}
@media (max-width:767px){
.legal-wrap{padding:36px 0 56px}
.legal-h1{font-size:28px}
.lcard{padding:24px 20px}
.lcard h2{font-size:19px}
.lcard p,.lcard ul{font-size:15px}
}
"""

IMPRESSUM = (
'<div class="wrap"><div class="legal-wrap">\n'
'<p class="draft" role="note"><b style="font-weight: 500">Entwurf.</b> Vor der Veröffentlichung prüfen lassen. Keine Rechtsberatung.</p>\n'
'<h1 class="legal-h1">Impressum</h1>\n'
'<div class="card lcard">'
'<h2>Angaben gemäß § 5 DDG</h2><p>Lina Schröder<br>Chronist-Lehmann-Weg 2<br>04509 Delitzsch<br>Deutschland</p>'
'<h2>Kontakt</h2><p>E-Mail: <a href="mailto:lina.schroeder@autarkflow.de">lina.schroeder@autarkflow.de</a><br>Telefon: ' + phone_reveal("linkbtn") + '</p>'
'<h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2><p>Lina Schröder, Anschrift wie oben</p>'
'<h2>Hinweis zu Glycodex</h2><p>Glycodex ist ein privates Diabetes-Tagebuch. Die App beschreibt Daten und gibt keine Therapie- oder Dosisempfehlungen. Sie ist kein Medizinprodukt und wird nicht zum Download oder zur Nutzung angeboten. Die Inhalte dieser Website ersetzen keine ärztliche Beratung.</p>'
'<h2>Marken und Unabhängigkeit</h2><p>YpsoPump, CamAPS FX, Dexcom G7 und Glooko sind Marken ihrer jeweiligen Inhaber. Glycodex ist unabhängig und steht in keiner Verbindung zu diesen Unternehmen.</p>'
'<h2>Bildnachweis</h2><p>Alle Abbildungen der App zeigen erfundene Testdaten. Logo, Gestaltung und Texte: Lina Schröder.</p>'
'</div>\n</div></div>\n'
)

DS_SECTIONS = [
    ("Verantwortliche", '<p>Lina Schröder<br>Chronist-Lehmann-Weg 2<br>04509 Delitzsch<br>E-Mail: <a href="mailto:lina.schroeder@autarkflow.de">lina.schroeder@autarkflow.de</a><br>Telefon: ' + phone_reveal("linkbtn") + '</p>'),
    ("Hosting und Server-Logfiles", '<p>Diese Website liegt auf einem Server, den ich bei Hostinger International Ltd., 61 Lordou Vironos str., 6023 Larnaca, Zypern, miete. Beim Aufruf speichert der Server automatisch Daten, die dein Browser übermittelt:</p>'
     '<ul><li>IP-Adresse</li><li>Datum und Uhrzeit des Aufrufs</li><li>aufgerufene Seite und übertragene Datenmenge</li><li>zuvor besuchte Seite (Referrer)</li><li>Browser und Betriebssystem</li></ul>'
     '<p>Diese Daten brauche ich, um die Seite auszuliefern und ihren sicheren Betrieb zu gewährleisten. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. Die Logfiles werden nach <span class="ph">[Anzahl]</span> Tagen gelöscht. Mit Hostinger besteht ein Vertrag zur Auftragsverarbeitung nach Art. 28 DSGVO.</p>'),
    ("Verschlüsselte Verbindung", '<p>Die Website nutzt eine verschlüsselte Verbindung (TLS). Du erkennst sie an „https://“ in der Adresszeile.</p>'),
    ("Farbschema", '<p>Wenn du oben das Farbschema umschaltest, merkt sich dein Browser deine Wahl im lokalen Speicher, damit die Seite beim nächsten Aufruf gleich hell oder dunkel erscheint. Die Angabe bleibt auf deinem Gerät und wird nicht an mich übertragen. Rechtsgrundlage ist § 25 Abs. 2 Nr. 2 TDDDG. Du kannst die Angabe jederzeit in den Einstellungen deines Browsers löschen.</p>'),
    ("Besucherstatistik", '<p>Um zu sehen, wie viele Menschen die Website besuchen und welche Seiten gelesen werden, nutze ich das Open-Source-Werkzeug Umami. Es läuft auf meinem eigenen Server bei Hostinger, die Daten gehen an keinen anderen Dienst. Umami setzt keine Cookies und speichert nichts auf deinem Gerät.</p>'
     '<p>Erfasst werden die aufgerufene Seite, die zuvor besuchte Seite (Referrer), Browser, Betriebssystem, Gerätetyp, Bildschirmgröße, Spracheinstellung und das aus der IP-Adresse abgeleitete Land. Die IP-Adresse selbst wird nicht gespeichert. Um Besuche zählen zu können, bildet Umami aus IP-Adresse und Browserangaben einen nicht umkehrbaren Prüfwert (Hash), der regelmäßig wechselt. Ich sehe nur zusammengefasste Zahlen und kann einzelne Besuche keiner Person zuordnen.</p>'
     '<p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. Mein berechtigtes Interesse ist, die Reichweite der Website zu verstehen. Du kannst dieser Verarbeitung widersprechen (Art. 21 DSGVO), schreib mir dafür eine E-Mail. Die Statistikdaten werden nach <span class="ph">[Anzahl]</span> Monaten gelöscht.</p>'),
    ("Kontakt per E-Mail oder Telefon", '<p>Wenn du mir schreibst oder mich anrufst, verarbeite ich deine Angaben, um deine Anfrage zu beantworten. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, wenn es um eine mögliche Zusammenarbeit geht, sonst Art. 6 Abs. 1 lit. f DSGVO. Ich lösche die Daten, sobald die Anfrage erledigt ist und keine gesetzlichen Aufbewahrungspflichten bestehen. Mein E-Mail-Postfach liegt ebenfalls bei Hostinger.</p>'
     '<p>Bitte schick mir keine Gesundheitsdaten wie Glukosewerte oder Befunde, wenn ich nicht ausdrücklich danach frage.</p>'),
    ("Die App Glycodex", '<p>Diese Website ist von der App getrennt. Über diese Seite werden keine Gesundheitsdaten verarbeitet. Die App selbst ist nicht öffentlich zugänglich.</p>'),
    ("Deine Rechte", '<p>Du hast das Recht auf</p><ul><li>Auskunft über deine gespeicherten Daten (Art. 15 DSGVO)</li><li>Berichtigung unrichtiger Daten (Art. 16 DSGVO)</li><li>Löschung (Art. 17 DSGVO)</li><li>Einschränkung der Verarbeitung (Art. 18 DSGVO)</li><li>Datenübertragbarkeit (Art. 20 DSGVO)</li><li>Widerspruch gegen eine Verarbeitung auf Grundlage berechtigter Interessen (Art. 21 DSGVO)</li></ul><p>Schreib mir dafür einfach eine E-Mail.</p>'),
    ("Beschwerde bei der Aufsichtsbehörde", '<p>Du kannst dich bei einer Datenschutz-Aufsichtsbehörde beschweren (Art. 77 DSGVO). Für mich zuständig ist:</p><p>Sächsische Datenschutz- und Transparenzbeauftragte<br>Maternistraße 17<br>01067 Dresden<br><a href="https://www.datenschutz.sachsen.de">www.datenschutz.sachsen.de</a></p>'),
]

DATENSCHUTZ = (
'<div class="wrap"><div class="legal-wrap">\n'
'<p class="draft" role="note"><b style="font-weight: 500">Entwurf.</b> Vor der Veröffentlichung prüfen lassen. Gelb markierte Stellen sind noch offen. Keine Rechtsberatung.</p>\n'
'<h1 class="legal-h1">Datenschutz</h1>\n'
'<p class="lead" style="margin-top: 16px">Kurz gesagt: Diese Website informiert über Glycodex. Sie setzt keine Cookies, nutzt keine Trackingdienste und lädt keine Inhalte von fremden Servern. Für eine einfache Besucherstatistik ohne Cookies nutze ich ein Werkzeug auf meinem eigenen Server. Auch die Schrift liegt auf dem eigenen Server. Nur wenn du das Farbschema umschaltest, merkt sich dein Browser diese Wahl.</p>\n'
'<div class="card lcard">'
'<nav class="toc" aria-label="Inhalt"><p>Inhalt</p><ol>'
+ "".join('<li><a href="#ds-%d">%s</a></li>' % (i + 1, t) for i, (t, _) in enumerate(DS_SECTIONS)) +
'</ol></nav>'
+ "".join('<h2 id="ds-%d">%d. %s</h2>%s' % (i + 1, i + 1, t, c) for i, (t, c) in enumerate(DS_SECTIONS)) +
'<p style="margin-top: 32px; font-size: 14px">Stand: November 2026</p>'
'</div>\n</div></div>\n'
)

IMPRESSUM_HTML = page("Impressum – Glycodex", IMPRESSUM, "impressum", [], 2000, LEGAL_CSS)
DATENSCHUTZ_HTML = page("Datenschutz – Glycodex", DATENSCHUTZ, "datenschutz", [], 4000, LEGAL_CSS)
