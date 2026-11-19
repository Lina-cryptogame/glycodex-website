"""Baut aus den .dc.html-Seiten der Leinwand die statische Website für glycodex.de."""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

from PIL import Image

SRC = "/home/claude/web/project/"
OUT = "/home/claude/site/dist/"
HERE = "/home/claude/site/"
FONT = "/home/claude/fontpkg/x/package/"
NOINDEX = True  # bis zur Freigabe unsichtbar
UMAMI_ID = None  # Website-ID aus Umami, sobald angelegt
UMAMI_HOST = "https://stats.glycodex.de"

PAGES = ["Main", "Fachkreise", "Partner", "Impressum", "Datenschutz"]
LANGS = ["de", "en", "fr", "uk"]
SLUG = {
    "de": {"Main": "", "Fachkreise": "diabetes-teams/", "Partner": "partnerschaften/", "Impressum": "impressum/", "Datenschutz": "datenschutz/"},
    "x": {"Main": "", "Fachkreise": "diabetes-teams/", "Partner": "partnerships/", "Impressum": "impressum/", "Datenschutz": "datenschutz/"},
}
BLOBS = {
    "b2351e6e5fcfeeb1c5a449fca0bf7c27": ("logo", None),
    "a28c53f178763bca0118d05bd294d06a": ("uebersicht", "/home/claude/handbuch/shots/02_uebersicht.png"),
    "1c8150adeb545d1d8ae0f5caa0f21850": ("automodus", "/home/claude/handbuch/shots/09_technik.png"),
    "90bcc3bfcafc2b4cfb1bb43e460765f5": ("codex", "/home/claude/web/assets/codex_seiten.png"),
    "bc10e5872398895728944ed09fcefdf4": ("tagesverlauf", "/home/claude/handbuch/shots/05_tagesverlauf.png"),
    "d3e58979acd9e3d586237d3df1164393": ("dextro", "/home/claude/handbuch/shots/13_dextro.png"),
    "5059b4be673fd1b9fddc2a068ae82047": ("zielbereich", "/home/claude/handbuch/shots/03_zielbereich.png"),
}
DESC = {
    "de": {"Main": "Glycodex macht aus den Daten von Pumpe und Sensor eine ruhige Übersicht, ein Tagebuch und persönliche Muster. Ein privates Diabetes-Tagebuch, entwickelt von einer Patientin mit Typ-1-Diabetes.",
           "Fachkreise": "Was Glycodex zeigt, wie es rechnet und was es bewusst nicht tut. Informationen für Diabetes-Teams.",
           "Partner": "Diabetesdaten aus Sicht einer Patientin, mit funktionierendem Prototyp. Informationen für Unternehmen der Medizintechnik.",
           "Impressum": "Impressum von Glycodex.", "Datenschutz": "Datenschutzerklärung von Glycodex."},
    "en": {"Main": "Glycodex turns pump and sensor data into a calm overview, a diary and personal patterns. A private diabetes diary developed by a patient with type 1 diabetes.",
           "Fachkreise": "What Glycodex shows, how it calculates and what it deliberately does not do. Information for diabetes care teams.",
           "Partner": "Diabetes data from a patient's perspective, with a working prototype. Information for medical technology companies.",
           "Impressum": "Legal notice of Glycodex.", "Datenschutz": "Privacy policy of Glycodex."},
    "fr": {"Main": "Glycodex transforme les données de la pompe et du capteur en une vue d’ensemble apaisée, un journal et des schémas personnels. Un journal privé du diabète créé par une patiente atteinte de diabète de type 1.",
           "Fachkreise": "Ce que montre Glycodex, comment il calcule et ce qu’il ne fait volontairement pas. Informations pour les équipes soignantes.",
           "Partner": "Les données du diabète vues par une patiente, avec un prototype fonctionnel. Informations pour les entreprises de technologies médicales.",
           "Impressum": "Mentions légales de Glycodex.", "Datenschutz": "Politique de confidentialité de Glycodex."},
    "uk": {"Main": "Glycodex перетворює дані з помпи та сенсора на спокійний огляд, щоденник і персональні закономірності. Приватний щоденник діабету, створений пацієнткою з діабетом 1 типу.",
           "Fachkreise": "Що показує Glycodex, як він рахує і чого свідомо не робить. Інформація для лікувальних команд.",
           "Partner": "Дані про діабет очима пацієнтки, з робочим прототипом. Інформація для компаній медичних технологій.",
           "Impressum": "Вихідні дані Glycodex.", "Datenschutz": "Політика конфіденційності Glycodex."},
}


NOT_FOUND = """<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Seite nicht gefunden – Glycodex</title><meta name="robots" content="noindex">
<link rel="icon" href="/assets/img/logo.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/fonts.css">
<style>
body{margin:0;min-height:100vh;display:grid;place-items:center;background:#f2f2f7;color:#1c1c1e;font-family:'Google Sans',system-ui,sans-serif;text-align:center;padding:24px;box-sizing:border-box}
@media (prefers-color-scheme: dark){body{background:#000;color:#f5f5f7}a.b{background:#8e8bff;color:#000}p{color:#a1a1a8}}
img{width:64px;height:64px;border-radius:16px}h1{font-size:32px;font-weight:500;margin:24px 0 8px}p{color:#6b6b72;margin:4px 0}
a.b{display:inline-flex;margin-top:28px;padding:12px 22px;border-radius:12px;background:#5b57d9;color:#fff;text-decoration:none;font-weight:500}
</style></head><body><main>
<img src="/assets/img/logo.svg" alt="Glycodex">
<h1>Diese Seite gibt es nicht.</h1>
<p lang="en">This page does not exist.</p><p lang="fr">Cette page n’existe pas.</p><p lang="uk">Цієї сторінки не існує.</p>
<a class="b" href="/">Zur Startseite</a>
</main></body></html>
"""


def url(page, lang):
    if lang == "de":
        return "/" + SLUG["de"][page]
    return "/%s/%s" % (lang, SLUG["x"][page])


def src_name(page, lang):
    return page + ".dc.html" if lang == "de" else "%s-%s.dc.html" % (page, lang)


def assets():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT + "assets/img")
    os.makedirs(OUT + "assets/fonts")
    for key, (name, path) in BLOBS.items():
        if path:
            im = Image.open(path).convert("RGB")
            im.save(OUT + "assets/img/%s.webp" % name, "WEBP", quality=84, method=6)
    shutil.copy("/home/claude/handbuch/img/icon.svg", OUT + "assets/img/logo.svg")
    shutil.copy("/home/claude/handbuch/img/icon180.png", OUT + "assets/img/apple-touch-icon.png")
    # Schrift: nur Latein und Kyrillisch, als variable Schrift
    css = open(FONT + "wght.css", encoding="utf-8").read()
    faces = []
    for block in re.findall(r"/\* (google-sans-[a-z-]+-wght-normal) \*/\s*(@font-face\s*{[^}]*})", css):
        name, face = block
        if not re.match(r"google-sans-(latin|latin-ext|cyrillic|cyrillic-ext)-wght-normal$", name):
            continue
        fn = name + ".woff2"
        shutil.copy(FONT + "files/" + fn, OUT + "assets/fonts/" + fn)
        face = face.replace("'Google Sans Variable'", "'Google Sans'").replace("./files/", "/assets/fonts/")
        faces.append(face)
    open(OUT + "assets/fonts.css", "w", encoding="utf-8").write("\n".join(faces) + "\n")
    shutil.copy(FONT + "LICENSE", OUT + "assets/fonts/OFL.txt")
    shutil.copy(HERE + "src/gx-runtime.js", OUT + "assets/gx-runtime.js")


def rewrite_links(html, lang):
    def rep(m):
        base, lg, hash_ = m.group(1), m.group(2), m.group(3) or ""
        return 'href="%s%s"' % (url(base, lg or "de"), hash_)
    html = re.sub(r'(<div class="zoom"><img [^>]*?)loading="lazy"', r'\1loading="eager"', html)
    html = re.sub(r'href="(Main|Fachkreise|Partner|Impressum|Datenschutz)(?:-(en|fr|uk))?\.dc\.html(#[^"]*)?"', rep, html)
    for key, (name, path) in BLOBS.items():
        target = "/assets/img/logo.svg" if name == "logo" else "/assets/img/%s.webp" % name
        html = html.replace("/_blob/" + key, target)
    return html


def stash(content, ext):
    h = hashlib.sha256(content.encode("utf-8")).hexdigest()[:12]
    rel = "/assets/%s/%s.%s" % (ext, h, ext)
    path = OUT + rel.lstrip("/")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        open(path, "w", encoding="utf-8").write(content)
    return rel


def page_html(page, lang):
    s = open(SRC + src_name(page, lang), encoding="utf-8").read()
    s = rewrite_links(s, lang)
    title = re.search(r"<title>([^<]*)</title>", s).group(1)
    xdc = s.split("<x-dc>")[1].split("</x-dc>")[0]
    helmet = xdc.split("<helmet>")[1].split("</helmet>")[0]
    style = re.search(r"<style>([\s\S]*)</style>", helmet).group(1)
    tpl = xdc.split("</helmet>")[1].strip()
    logic = re.search(r"data-dc-script[^>]*>\n([\s\S]*?)\n</script>", s).group(1)
    alts = "".join('<link rel="alternate" hreflang="%s" href="https://glycodex.de%s">' % (l, url(page, l)) for l in LANGS)
    alts += '<link rel="alternate" hreflang="x-default" href="https://glycodex.de%s">' % url(page, "de")
    robots = '<meta name="robots" content="noindex, nofollow">' if NOINDEX else ""
    return (
        '<!doctype html>\n<html lang="%s">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<title>%s</title>\n<meta name="description" content="%s">\n%s\n'
        '<link rel="canonical" href="https://glycodex.de%s">\n%s\n'
        '<link rel="icon" href="/assets/img/logo.svg" type="image/svg+xml">\n'
        '<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">\n'
        '<meta name="theme-color" content="#f2f2f7" media="(prefers-color-scheme: light)">\n'
        '<meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">\n'
        '<link rel="preload" href="/assets/fonts/google-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>\n'
        + (('<script defer src="%s/script.js" data-website-id="%s" data-domains="glycodex.de" data-do-not-track="true"></script>\n' % (UMAMI_HOST, UMAMI_ID)) if UMAMI_ID else '') +
        ''
        '<link rel="stylesheet" href="/assets/fonts.css">\n'
        '<link rel="stylesheet" href="%s">\n</head>\n<body>\n'
        '<div id="gx-app"><!--PRERENDER--></div>\n'
        '<template id="gx-tpl">%s</template>\n'
        '<script src="/assets/gx-runtime.js"></script>\n'
        '<script src="%s"></script>\n'
        '</body>\n</html>\n'
    ) % (lang, title, DESC[lang][page].replace('"', "&quot;"), robots, url(page, lang), alts, stash(style, "css"), tpl,
       stash(logic + "\nGX.mount(Component, { prerender: !!window.GX_PRERENDER });\n", "js"))


def build():
    assets()
    out = []
    for lang in LANGS:
        for page in PAGES:
            path = OUT + url(page, lang).lstrip("/") + "index.html"
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, "w", encoding="utf-8").write(page_html(page, lang))
            out.append(path)
    robots = "User-agent: *\nDisallow: /\n" if NOINDEX else "User-agent: *\nAllow: /\nSitemap: https://glycodex.de/sitemap.xml\n"
    open(OUT + "robots.txt", "w").write(robots)
    if not NOINDEX:
        items = "".join("<url><loc>https://glycodex.de%s</loc></url>" % url(p, l) for l in LANGS for p in PAGES)
        open(OUT + "sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>' % items)
    open(OUT + "404.html", "w", encoding="utf-8").write(NOT_FOUND)
    return out


if __name__ == "__main__":
    files = build()
    print(len(files), "Seiten")
