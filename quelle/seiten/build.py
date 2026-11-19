import re
import sys
sys.path.insert(0, "/home/claude/web/build")
from main_page import HTML as MAIN
from sub_pages import TEAMS_HTML, PARTNER_HTML, IMPRESSUM_HTML, DATENSCHUTZ_HTML
from i18n_tool import apply

OUT = "/home/claude/web/project/"
B = "/home/claude/web/build/"
PAGES = [("Main", MAIN), ("Fachkreise", TEAMS_HTML), ("Partner", PARTNER_HTML),
         ("Impressum", IMPRESSUM_HTML), ("Datenschutz", DATENSCHUTZ_HTML)]
BASES = [p[0] for p in PAGES]
LEGAL = ("Impressum", "Datenschutz")
CODES = {"de": "DE", "en": "EN", "fr": "FR", "uk": "УКР"}

# Zusätze, die nicht aus den deutschen Segmenten kommen
EXTRA = {
    "en": {"Sprache wählen": "Choose language", "Glycodex auf Instagram, öffnet in neuem Tab": "Glycodex on Instagram, opens in a new tab", "⟦0⟧Instagram": "⟦0⟧Instagram"},
    "fr": {"Sprache wählen": "Choisir la langue", "Glycodex auf Instagram, öffnet in neuem Tab": "Glycodex sur Instagram, s’ouvre dans un nouvel onglet", "⟦0⟧Instagram": "⟦0⟧Instagram"},
    "uk": {"Sprache wählen": "Вибрати мову", "Glycodex auf Instagram, öffnet in neuem Tab": "Glycodex в Instagram, відкривається в новій вкладці", "⟦0⟧Instagram": "⟦0⟧Instagram"},
}
TITLES = {
    "en": {"Glycodex – Privates Diabetes-Tagebuch": "Glycodex – Private diabetes diary",
           "Glycodex für Diabetes-Teams": "Glycodex for diabetes care teams",
           "Glycodex für Partnerschaften": "Glycodex partnerships",
           "Impressum – Glycodex": "Legal notice – Glycodex", "Datenschutz – Glycodex": "Privacy – Glycodex"},
    "fr": {"Glycodex – Privates Diabetes-Tagebuch": "Glycodex – Journal privé du diabète",
           "Glycodex für Diabetes-Teams": "Glycodex pour les équipes soignantes",
           "Glycodex für Partnerschaften": "Glycodex – Partenariats",
           "Impressum – Glycodex": "Mentions légales – Glycodex", "Datenschutz – Glycodex": "Confidentialité – Glycodex"},
    "uk": {"Glycodex – Privates Diabetes-Tagebuch": "Glycodex – Приватний щоденник діабету",
           "Glycodex für Diabetes-Teams": "Glycodex для лікувальних команд",
           "Glycodex für Partnerschaften": "Glycodex – Партнерство",
           "Impressum – Glycodex": "Вихідні дані – Glycodex", "Datenschutz – Glycodex": "Конфіденційність – Glycodex"},
}
SUBJECTS = {
    "en": {"Kurzprofil": "Short profile", "Kurzinformation": "Information sheet", "Rückmeldung": "Feedback"},
    "fr": {"Kurzprofil": "Profil synthétique", "Kurzinformation": "Fiche d’information", "Rückmeldung": "Retour"},
    "uk": {"Kurzprofil": "Короткий профіль", "Kurzinformation": "Довідка", "Rückmeldung": "Відгук"},
}
LEGAL_NOTE = {
    "en": "This page is only available in German. The German version is the legally binding one.",
    "fr": "Cette page n’est disponible qu’en allemand. Seule la version allemande fait foi.",
    "uk": "Ця сторінка доступна лише німецькою мовою. Юридично чинною є німецька версія.",
}


def fname(base, lang):
    return base + ".dc.html" if lang == "de" else "%s-%s.dc.html" % (base, lang)


def load(lang):
    import json
    de = json.load(open(B + "i18n_de.json", encoding="utf-8"))
    table = {}
    for line in open(B + "i18n/%s.txt" % lang, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line:
            continue
        i, t = line.split("\t", 1)
        table[de[int(i)]] = t
    assert len(table) == len(de), (lang, len(table), len(de))
    table.update(EXTRA[lang])
    if lang == "fr":
        nb, nnb = " ", " "
        for k, v in table.items():
            v = re.sub(r" ([?!;])", nnb + r"\1", v)
            v = re.sub(r" :", nb + ":", v)
            v = v.replace("« ", "«" + nb).replace(" »", nb + "»")
            table[k] = v
    return table


def finalize(html, lang):
    for b in BASES:
        for c in CODES:
            html = html.replace("§%s§%s" % (b, c), fname(b, c))
    for c in CODES:
        html = html.replace(" §CUR_%s§" % c, ' aria-current="true"' if c == lang else "")
    return html.replace("§CODE§", CODES[lang])


def localize(name, html, lang, table, missing):
    skip = None
    if name in LEGAL:
        a = html.index('<main id="inhalt">')
        skip = (a, html.index("</main>"))
    html = apply(html, table, skip, missing)
    html = html.replace('<html lang="de">', '<html lang="%s">' % lang, 1)
    m = re.search(r"<title>([^<]*)</title>", html)
    html = html.replace(m.group(0), "<title>%s</title>" % TITLES[lang][m.group(1)], 1)
    for b in BASES:
        html = re.sub(r'href="%s\.dc\.html' % b, 'href="%s' % fname(b, lang), html)
    for de, tr in SUBJECTS[lang].items():
        html = html.replace("ask('%s'," % de, "ask('%s'," % tr)
    html = html.replace("? 'Glycodex – ' + mail.subj : 'Glycodex')",
                        "? 'Glycodex – ' + mail.subj + ' (%s)' : 'Glycodex (%s)')" % (lang.upper(), lang.upper()))
    if name in LEGAL:
        note = ('<div class="wrap" style="padding-top: 32px"><p class="lnote" lang="%s">%s</p></div>\n'
                % (lang, LEGAL_NOTE[lang]))
        html = html.replace('<main id="inhalt">', '<main id="inhalt" lang="de">\n' + note, 1)
    return html


HANDY = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400..700&amp;display=swap">
<style>
body{{margin:0;background:#f7f7fa}}
</style>
</helmet>
<div style="width: 390px; background: #f7f7fa; font-family: 'Google Sans', Arial, sans-serif; color: #1c1c1e">
<dc-import name="{name}" hint-size="390px,{h}px"></dc-import>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":390,"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
"""

if __name__ == "__main__":
    langs = sys.argv[1:] or ["de", "en", "fr", "uk"]
    for name, html in PAGES:
        with open(OUT + fname(name, "de"), "w", encoding="utf-8") as f:
            f.write(finalize(html, "de"))
    for lang in langs:
        if lang == "de":
            continue
        table = load(lang)
        missing = []
        for name, html in PAGES:
            out = finalize(localize(name, html, lang, table, missing), lang)
            with open(OUT + fname(name, lang), "w", encoding="utf-8") as f:
                f.write(out)
        rest = sorted(set(m for m in missing if not re.fullmatch(r"[\d\s·.,%/-]*|Deutsch|English|Français|Українська|§CODE§|Glyco<b>dex</b>", m)))
        print(lang, "fehlend:", rest)
