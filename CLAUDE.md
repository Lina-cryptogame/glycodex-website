# Glycodex – Website

Statische Website von Glycodex unter https://glycodex.de, in Deutsch, Englisch, Französisch und Ukrainisch. Sie stellt die App vor: für Menschen mit Typ-1-Diabetes, für Diabetes-Teams und für Partner aus der Medizintechnik. Ziel jeder Seite: verstehen, Vertrauen fassen, Kontakt aufnehmen.

Dieses Repo ist öffentlich. Keine Zugangsdaten, keine privaten Notizen und keine persönlichen Gesundheitsangaben über das hinaus, was schon auf der Website steht.

## Feste Regeln

- Glycodex gibt **keine Therapie- oder Dosisempfehlungen** und ist kein Medizinprodukt. Keine Heilversprechen, keine erfundenen Zahlen, Zitate oder Stimmen von Nutzerinnen.
- Die App wird nicht zum Download angeboten. Nichts darf das andeuten.
- Abgestimmte Texte nicht eigenmächtig umschreiben. Änderungsvorschläge ausdrücklich als Textvorschlag kennzeichnen. Änderungen an einer Sprache in allen vier Sprachen nachziehen oder sagen, welche noch fehlen.
- Barrierefreiheit: WCAG 2.1 AA, Text mindestens 4,5:1, Touch-Ziele mindestens 44 px, Inhalte ohne JavaScript lesbar, `prefers-reduced-motion` beachten.
- Kontakt läuft per E-Mail. Der zweistufige Hinweis vor dem Öffnen des Mailprogramms („E-Mail schreiben“ / „Erst einmal weiter informieren“) bleibt.

## Zusammenarbeit mit Lina

- Sprache: Deutsch, kurz und einheitlich.
- Bei größeren oder mehrdeutigen Änderungen zuerst Fragen stellen, dann bauen.
- Wenn etwas unbekannt oder nicht geprüft ist, das vorher sagen statt zu raten.
- Jede Änderung auf einem eigenen Branch, Pull Request nach `main`. Nie direkt nach `main` pushen. Lina mergt selbst.

## Gestaltung

- Apple-nah, ruhig, warm, nie klinisch-kalt. Schrift Google Sans (selbst gehostet, `public/assets/fonts/`).
- Wortmarke „Glyco“ + „**dex**“ in Indigo, nie in Versalien. Logo: der Tropfen mit grünem Zielband und Kurve.
- Markenfarben wie in der App: Indigo `#5b57d9` (dunkel `#8e8bff`), Zielbereich-Grün `#2fb35a`. Helles und dunkles Thema sind gleichwertig.
- Motive: konzentrische Indigo-Ringe (nie hinter Text mit zu wenig Kontrast) und das grüne Zielband.
- Bewegung mit `cubic-bezier(.32,.72,0,1)`.

## Aufbau

- `public/`: die ausgelieferten Seiten. CSS und JS liegen mit Hash-Namen unter `public/assets/css/` und `public/assets/js/`, Bilder unter `public/assets/img/`.
- `nginx/nginx.conf`: Webserver mit strenger CSP (`script-src 'self'`). Inline-Skripte werden blockiert, JavaScript gehört in Dateien. Neue externe Quellen brauchen eine Änderung der CSP.
- `public/assets/stats.js`: Besucherstatistik über `stats.glycodex.de` (Umami, Projekt `glycodex-stats` auf dem VPS).
- `quelle/`: Generator, Übersetzungen (`quelle/seiten/i18n/`) und Export-Skripte, mit denen die Seiten ursprünglich erzeugt wurden.
  - **Achtung:** Die Skripte zeigen auf Pfade einer früheren Arbeitsumgebung (`/home/claude/web/…`, `/home/claude/handbuch/…`) und brauchen Dateien, die nicht im Repo liegen. Sie laufen so nicht.
  - Kleine Änderungen daher direkt in `public/` machen und in allen Sprachfassungen nachziehen. Für größere Umbauten zuerst mit Lina klären, ob der Generator repariert werden soll.

## Prüfen vor dem PR

- Lokal ausliefern, z. B. `python3 -m http.server -d public 8080`, und mit Playwright ansehen: Handy (390 px) und Desktop (1280 px), hell und dunkel, alle Sprachen der geänderten Seite.
- Keine Konsolenfehler, keine 404, Links und Sprachumschalter funktionieren.

## Ausrollen

- Läuft auf dem Hostinger-VPS (Docker Manager, Projekt `glycodex-web`) mit nginx hinter Traefik.
- Der Container lädt beim Start den Stand von `main` (`public/` und `nginx/`). **Update = Merge, dann Neustart des Projekts `glycodex-web`.** Mit dem Hostinger-Connector: `vps_docker_restart` mit dem Projektnamen `glycodex-web`.
