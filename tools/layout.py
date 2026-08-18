# -*- coding: utf-8 -*-
"""Gabarit HTML commun. Produit des fichiers statiques : aucune dépendance
côté visiteur, aucun générateur nécessaire pour publier le site."""

import html, json, os

SITE = "Anticipation"
TAGLINE = "Le jeu de la Belgique politique"
BASE = "https://ouaisfieu.github.io/anticipation/"
AUTHOR = "ouaisfieu"
LOCALE = "fr_BE"
UPDATED = "2026-08-18"

NAV = [
    ("jeu/",        "Le parcours"),
    ("boussole/",   "Boussole"),
    ("partis/",     "Partis"),
    ("dossiers/",   "Dossiers"),
    ("chronologie/","Chronologie"),
    ("sondages/",   "Sondages"),
    ("glossaire/",  "Glossaire"),
]

FOOT = [
    ("Jouer", [("jeu/", "Le compte à rebours"), ("jeu/01-le-comite-de-monitoring/", "Chapitre 1"),
               ("jeu/fins/", "Les six dénouements"), ("boussole/", "Boussole électorale")]),
    ("Comprendre", [("partis/", "Les partis"), ("dossiers/", "Les dossiers"),
                    ("chronologie/", "Chronologie 2024-2026"), ("sondages/", "Sondages")]),
    ("Références", [("glossaire/", "Glossaire institutionnel"),
                    ("dossiers/elections-anticipees-mode-demploi/", "Élections anticipées : mode d’emploi"),
                    ("a-propos/", "À propos & méthode"), ("a-propos/#sources", "Sources")]),
]

def e(s):
    return html.escape(str(s), quote=True)

def rel(depth):
    return "../" * depth if depth else ""

def _jsonld(objs):
    if not objs:
        return ""
    out = []
    for o in objs:
        out.append('<script type="application/ld+json">%s</script>' %
                   json.dumps(o, ensure_ascii=False, separators=(",", ":")))
    return "\n".join(out)

def breadcrumb_html(trail, depth):
    if not trail:
        return ""
    r = rel(depth)
    items = ['<li><a href="%s">Accueil</a></li>' % (r or "./")]
    for i, (href, label) in enumerate(trail):
        last = i == len(trail) - 1
        if last or not href:
            items.append('<li><span aria-current="page">%s</span></li>' % e(label))
        else:
            items.append('<li><a href="%s%s">%s</a></li>' % (r, href, e(label)))
    return ('<nav class="breadcrumb wrap" aria-label="Fil d’Ariane"><ol>%s</ol></nav>'
            % "".join(items))

def breadcrumb_ld(trail):
    els = [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": BASE}]
    for i, (href, label) in enumerate(trail):
        els.append({"@type": "ListItem", "position": i + 2, "name": label,
                    "item": BASE + (href or "")})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": els}

GLYPH = ('<svg class="glyph" viewBox="0 0 32 32" aria-hidden="true" focusable="false">'
         '<rect x="1" y="1" width="30" height="30" rx="7" fill="currentColor" opacity=".08"/>'
         '<circle cx="16" cy="16" r="11" fill="none" stroke="currentColor" stroke-width="2" opacity=".55"/>'
         '<path d="M16 7v9l6 4" fill="none" stroke="currentColor" stroke-width="2.4" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')

def page(path, title, description, body, depth=0, trail=None, extra_ld=None,
         scripts=(), keywords=None, og_type="article", section=None, nav_key=None,
         toc=None, updated=UPDATED, noindex=False):
    """Assemble une page complète. `path` est l'URL relative à la racine."""
    r = rel(depth)
    canonical = BASE + path
    trail = trail or []
    nav_key = nav_key or (path.split("/")[0] + "/" if "/" in path and path != "" else path)

    lds = [breadcrumb_ld(trail)] if trail else []
    lds.append({
        "@context": "https://schema.org",
        "@type": "WebPage" if og_type != "article" else "Article",
        "headline": title,
        "name": title,
        "description": description,
        "inLanguage": "fr-BE",
        "url": canonical,
        "isPartOf": {"@type": "WebSite", "name": SITE, "url": BASE},
        "dateModified": updated,
        "datePublished": "2026-08-18",
        "author": {"@type": "Organization", "name": AUTHOR, "url": "https://github.com/ouaisfieu"},
        "publisher": {"@type": "Organization", "name": SITE, "url": BASE},
        **({"articleSection": section} if section and og_type == "article" else {}),
    })
    for o in (extra_ld or []):
        lds.append(o)

    navhtml = "".join(
        '<li><a href="%s%s"%s>%s</a></li>' % (r, href, ' aria-current="page"' if href == nav_key else "", e(label))
        for href, label in NAV)

    foothtml = "".join(
        '<div><h2>%s</h2><ul>%s</ul></div>' % (
            e(sec), "".join('<li><a href="%s%s">%s</a></li>' % (r, h, e(l)) for h, l in links))
        for sec, links in FOOT)

    side = ""
    if toc:
        side = ('<aside class="side"><nav aria-label="Sommaire de la page">'
                '<p class="kicker" style="margin-bottom:.6rem">Sur cette page</p><ol>%s</ol></nav></aside>'
                % "".join('<li><a href="#%s">%s</a></li>' % (a, e(l)) for a, l in toc))

    scr = "".join('<script src="%sassets/js/%s" defer></script>' % (r, s) for s in scripts)

    return f"""<!DOCTYPE html>
<html lang="fr" prefix="og: https://ogp.me/ns#">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)} — {SITE}</title>
<meta name="description" content="{e(description)}">
{'<meta name="keywords" content="%s">' % e(", ".join(keywords)) if keywords else ''}
<link rel="canonical" href="{e(canonical)}">
<meta name="robots" content="{'noindex,follow' if noindex else 'index,follow,max-image-preview:large,max-snippet:-1'}">
<meta name="author" content="{e(AUTHOR)}">
<meta name="theme-color" content="#fbfaf7" media="(prefers-color-scheme:light)">
<meta name="theme-color" content="#101216" media="(prefers-color-scheme:dark)">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{SITE} — {TAGLINE}">
<meta property="og:locale" content="{LOCALE}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{e(canonical)}">
<meta property="og:image" content="{BASE}assets/img/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Anticipation — le jeu de la Belgique politique">
<meta property="article:modified_time" content="{updated}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(description)}">
<meta name="twitter:image" content="{BASE}assets/img/og.png">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/img/favicon.svg">
<link rel="manifest" href="{r}manifest.webmanifest">
<link rel="sitemap" type="application/xml" href="{BASE}sitemap.xml">
<link rel="stylesheet" href="{r}assets/css/style.css">
{_jsonld(lds)}
<script src="{r}assets/js/app.js" defer></script>{scr}
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="masthead">
  <div class="wrap bar">
    <a class="brand" href="{r or './'}">{GLYPH}<span>{SITE}</span><span class="sub">Belgique</span></a>
    <button class="nav-toggle" type="button" aria-controls="sitenav" aria-expanded="false">Menu</button>
    <nav id="sitenav" aria-label="Navigation principale"><ul>{navhtml}</ul></nav>
    <button class="theme-btn" type="button" aria-label="Changer de thème">☾</button>
  </div>
</header>
{breadcrumb_html(trail, depth)}
<main id="contenu">
{body}
</main>
<footer class="sitefoot">
  <div class="wrap">
    <div class="foot-grid">{foothtml}</div>
    <p class="foot-legal">
      <strong>{SITE}</strong> — {TAGLINE}. Site statique en HTML, CSS et JavaScript, sans traceur,
      sans cookie publicitaire et sans serveur : vos réponses restent dans votre navigateur.
      Dernière mise à jour des données : 18 août 2026. © <span data-year>2026</span> {AUTHOR} —
      <a href="{r}a-propos/">à propos, méthode et sources</a>.
      Ce site mêle <em>faits sourcés</em> et <em>fiction d’anticipation</em> : les passages fictifs sont toujours signalés.
    </p>
  </div>
</footer>
</body>
</html>
"""

def write(outdir, path, content):
    full = os.path.join(outdir, path if path.endswith(".html") else path + "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return full
