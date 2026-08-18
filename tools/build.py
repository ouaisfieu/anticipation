# -*- coding: utf-8 -*-
"""Script de génération complet.

Le site publié est composé exclusivement de fichiers statiques : ce script
n'est PAS nécessaire pour l'héberger, l'ouvrir ou le modifier à la main.
Il n'existe que pour régénérer l'ensemble d'un coup après une modification
du gabarit ou des données. Usage :  python3 tools/build.py
"""
import os, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from layout import BASE, UPDATED
import build_jeu, build_partis, build_dossiers, build_chrono
import build_sondages, build_glossaire, build_boussole, build_home

PAGES = [
    ("", "1.0", "weekly"),
    ("jeu/", "0.9", "monthly"),
    ("jeu/01-le-comite-de-monitoring/", "0.8", "monthly"),
    ("jeu/02-le-conclave/", "0.8", "monthly"),
    ("jeu/03-la-rue/", "0.8", "monthly"),
    ("jeu/04-la-rupture/", "0.8", "monthly"),
    ("jeu/05-la-dissolution/", "0.8", "monthly"),
    ("jeu/06-la-campagne/", "0.8", "monthly"),
    ("jeu/07-le-scrutin/", "0.8", "monthly"),
    ("jeu/fins/", "0.8", "monthly"),
    ("boussole/", "0.9", "monthly"),
    ("partis/", "0.8", "monthly"),
    ("partis/mr/", "0.7", "monthly"),
    ("partis/ps/", "0.7", "monthly"),
    ("partis/ptb/", "0.7", "monthly"),
    ("partis/les-engages/", "0.7", "monthly"),
    ("partis/ecolo/", "0.7", "monthly"),
    ("partis/defi/", "0.7", "monthly"),
    ("partis/flandre/", "0.7", "monthly"),
    ("dossiers/", "0.8", "monthly"),
    ("dossiers/chomage-limite-dans-le-temps/", "0.8", "monthly"),
    ("dossiers/budget-10-milliards/", "0.8", "weekly"),
    ("dossiers/pensions-et-malus/", "0.7", "monthly"),
    ("dossiers/crise-bruxelloise/", "0.7", "monthly"),
    ("dossiers/cordon-sanitaire/", "0.7", "monthly"),
    ("dossiers/elections-anticipees-mode-demploi/", "0.8", "monthly"),
    ("chronologie/", "0.7", "weekly"),
    ("sondages/", "0.7", "weekly"),
    ("glossaire/", "0.6", "monthly"),
    ("a-propos/", "0.5", "yearly"),
]

def sitemap():
    rows = "\n".join(
        f"  <url>\n    <loc>{BASE}{p}</loc>\n    <lastmod>{UPDATED}</lastmod>\n"
        f"    <changefreq>{cf}</changefreq>\n    <priority>{prio}</priority>\n  </url>"
        for p, prio, cf in PAGES)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{rows}
</urlset>
"""

def robots():
    return f"""# Anticipation — le jeu de la Belgique politique
User-agent: *
Allow: /
Disallow: /404.html

Sitemap: {BASE}sitemap.xml
"""

def manifest():
    return """{
  "name": "Anticipation — le jeu de la Belgique politique",
  "short_name": "Anticipation",
  "description": "Jeu textuel d'anticipation et outils de compréhension sur la situation politique et démocratique belge.",
  "lang": "fr-BE",
  "dir": "ltr",
  "start_url": "./",
  "scope": "./",
  "display": "standalone",
  "background_color": "#fbfaf7",
  "theme_color": "#fbfaf7",
  "categories": ["education", "news", "politics"],
  "icons": [
    { "src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "any" },
    { "src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
"""

def main():
    build_home.build(ROOT)
    build_jeu.build(ROOT)
    build_partis.build(ROOT)
    build_dossiers.build(ROOT)
    build_chrono.build(ROOT)
    build_sondages.build(ROOT)
    build_glossaire.build(ROOT)
    build_boussole.build(ROOT)
    for name, content in (("sitemap.xml", sitemap()), ("robots.txt", robots()),
                          ("manifest.webmanifest", manifest())):
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
            f.write(content)
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    print(f"{len(PAGES)} pages + 404 générées dans {ROOT}")

if __name__ == "__main__":
    main()
