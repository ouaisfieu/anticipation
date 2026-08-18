# -*- coding: utf-8 -*-
from layout import page, write, e, BASE
from data_dossiers import DOSSIERS

def body(d):
    stats = "".join(f'<div class="stat"><span class="v">{e(v)}</span><span class="k">{e(k)}</span></div>'
                    for v, k in d["stats"])
    faq = "".join(f'<h3>{e(q)}</h3><p>{e(a)}</p>' for q, a in d["faq"])
    src = "".join(f'<li><a href="{u}" rel="noopener nofollow" target="_blank">{e(t)}</a></li>'
                  for t, u in d["sources"])
    voir = "".join(f'<a class="card" href="../../{h}"><h3>{e(l)}</h3><p>Continuer la lecture →</p></a>'
                   for h, l in d["voir"])
    toc = "".join(f'<li><a href="#{a}">{e(l)}</a></li>' for a, l in d["toc"])
    return f"""
<div class="wrap">
  <div class="page-head">
    <p class="kicker">{e(d['kicker'])}</p>
    <h1>{e(d['titre'])}</h1>
    <p class="lede">{e(d['lede'])}</p>
    <p class="updated" style="margin-top:1rem">Mis à jour le 18 août 2026</p>
  </div>
</div>
<div class="wrap layout-side">
  <article class="prose">
    <div class="stat-row">{stats}</div>
    {d['corps']}
    <h2 id="faq">Questions fréquentes</h2>
    {faq}
    <h2 id="sources">Sources</h2>
    <ul class="source-list">{src}</ul>
    <h2 id="voir">À lire ensuite</h2>
    <div class="grid grid-3">{voir}</div>
  </article>
  <aside class="side"><nav aria-label="Sommaire"><p class="kicker" style="margin-bottom:.6rem">Sur cette page</p>
  <ol>{toc}<li><a href="#sources">Sources</a></li></ol></nav></aside>
</div>
"""

def build(outdir):
    for d in DOSSIERS:
        path = f"dossiers/{d['slug']}/"
        faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
                  "mainEntity": [{"@type": "Question", "name": q,
                                  "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}
        write(outdir, path, page(
            path, d["titre"], d["meta_desc"], body(d), depth=2,
            trail=[("dossiers/", "Dossiers"), (path, d["titre"])],
            keywords=d["kw"], nav_key="dossiers/", extra_ld=[faq_ld], section="Dossiers"))
    cards = "".join(
        f'<a class="card" href="{d["slug"]}/"><p class="kicker">{e(d["kicker"].replace("Dossier · ", ""))}</p>'
        f'<h3>{e(d["titre"])}</h3><p>{e(d["lede"])}</p></a>' for d in DOSSIERS)
    idx_body = f"""
<div class="wrap">
  <div class="page-head">
    <p class="kicker">Comprendre</p>
    <h1>Six dossiers pour lire la crise</h1>
    <p class="lede">Chaque dossier part d’une décision réelle, en explique le mécanisme, chiffre ce qu’elle
    déplace et expose les arguments des deux camps — sans arbitrer à votre place.</p>
  </div>
</div>
<div class="wrap">
  <article class="prose">
    <p>La politique belge de 2026 se raconte souvent en personnalités et en petites phrases. Elle se comprend
    mieux en mécanismes : une mesure fédérale, une conséquence communale, une règle constitutionnelle et une
    arithmétique parlementaire.</p>
    <p>Ces six dossiers sont conçus pour être lus séparément. Chacun contient ses propres chiffres, ses propres
    sources et sa propre FAQ.</p>
    <div class="grid grid-2">{cards}</div>
    <div class="btnrow">
      <a class="btn" href="../jeu/">Jouer le parcours narratif</a>
      <a class="btn ghost" href="../boussole/">Passer la boussole électorale</a>
    </div>
  </article>
</div>
"""
    write(outdir, "dossiers/", page(
        "dossiers/", "Six dossiers pour lire la crise politique belge",
        "Six dossiers pour comprendre la crise politique belge de 2026 : limitation du chômage, 10 milliards budgétaires, réforme des pensions, crise bruxelloise, cordon sanitaire, élections anticipées.",
        idx_body, depth=1, trail=[("dossiers/", "Dossiers")], nav_key="dossiers/", og_type="website",
        keywords=["politique belge 2026", "dossiers", "réformes Arizona", "institutions belges"]))
