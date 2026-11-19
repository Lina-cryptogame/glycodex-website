# glycodex.de

Statische Website von Glycodex. Wird aus den Entwürfen auf der Claude-Leinwand erzeugt.

- `public/` – die ausgelieferten Seiten (Deutsch, Englisch, Französisch, Ukrainisch)
- `nginx/nginx.conf` – Webserver-Konfiguration
- `docker-compose.yml` – Container auf dem VPS (lädt dieses Repo beim Start)

Neu ausrollen: Änderungen hierher pushen und das Docker-Projekt `glycodex-web` neu starten.

## Quellen

- `quelle/seiten/` – Generator der Seiten (Python), Übersetzungen (`i18n/`), Körperkarte
- `quelle/export/` – macht aus den Leinwand-Seiten die statische Website, setzt den ersten Seitenzustand fest ein und testet sie

Ablauf: `python3 quelle/seiten/build.py` → `python3 quelle/export/static_build.py` → `node quelle/export/prerender.cjs` → Inhalt von `dist/` nach `public/`.
Die Pfade in den Skripten zeigen noch auf die Arbeitsumgebung von Claude und müssen bei einem Umzug angepasst werden.
