# -*- coding: utf-8 -*-
"""Génération des pages du parcours narratif."""
from layout import page, write, e, BASE
from data_jeu import CHAPTERS, FINS

LABELS = {"cred": "Crédibilité", "soc": "Cohésion sociale",
          "stab": "Stabilité institutionnelle", "tension": "Tension"}

def hud(depth=2):
    g = []
    for k, lab in (("cred", "Crédibilité"), ("soc", "Cohésion sociale"), ("stab", "Stabilité")):
        g.append(
            f'<div class="gauge" data-k="{k}" role="meter" aria-valuemin="0" aria-valuemax="100" '
            f'aria-valuenow="50" aria-label="{lab}">'
            f'<span class="lbl"><span>{lab}</span><b>50</b></span>'
            f'<span class="track"><span class="fill"></span></span></div>')
    return ('<div class="hud" aria-label="Vos indicateurs de partie">'
            f'<div class="hud-grid">{"".join(g)}</div>'
            '<p class="hud-foot"><span>Chapitres joués : <span data-done>0/7</span></span>'
            '<span>État du pays : <span class="clock">Législature stable</span></span>'
            '<button type="button" data-reset>Recommencer</button></p></div>')

def eff_chips(eff):
    out = []
    for part in eff.split(","):
        k, v = part.split(":")
        val = float(v)
        cls = "" if k == "tension" else ("up" if val > 0 else "dn")
        sign = "+" if val > 0 else "−"
        out.append(f'<li class="{cls}">{LABELS[k]} {sign}{abs(int(val))}</li>')
    return '<ul class="eff" aria-label="Effet de ce choix">%s</ul>' % "".join(out)

def chapter_body(ch, prev, nxt):
    choices = []
    for c in ch["choix"]:
        choices.append(
            f'<li class="choice" data-id="{c["id"]}" data-eff="{c["eff"]}">'
            f'<button class="pick" type="button">'
            f'<span class="num" aria-hidden="true"></span>'
            f'<span class="txt"><b>{c["t"]}</b><span>{c["s"]}</span></span></button>'
            f'<div class="consequence"><p class="kicker">Conséquence</p>{c["c"]}{eff_chips(c["eff"])}</div>'
            f'</li>')
    src = "".join(f'<li><a href="{u}" rel="noopener nofollow" target="_blank">{e(t)}</a></li>'
                  for t, u in ch["sources"])
    navprev = (f'<a href="../{prev["slug"]}/" rel="prev">← Chapitre {prev["n"]} · {e(prev["titre"])}</a>'
               if prev else '<a href="../" rel="up">← Présentation du parcours</a>')
    navnext = (f'<a href="../{nxt["slug"]}/" rel="next" data-next>Chapitre {nxt["n"]} · {e(nxt["titre"])} →</a>'
               if nxt else '<a href="../fins/" rel="next" data-next>Découvrir votre dénouement →</a>')
    return f"""
<div class="wrap">
  <div class="page-head">
    <p class="kicker">Le compte à rebours · Chapitre {ch['n']} sur 7</p>
    <h1>{e(ch['titre'])}</h1>
    <p class="lede"><time datetime="2026">{e(ch['date'])}</time> — {e(ch['lieu'])}</p>
  </div>
</div>
<div class="wrap">
  <article class="prose" data-chapter="{ch['id']}">
    {hud()}
    <section aria-labelledby="fait">
      <div class="callout fact">
        <p class="t" id="fait">Ce qui est vrai</p>
        {ch['fait']}
      </div>
    </section>
    <section class="scene" aria-label="Récit">
      <div class="callout fiction"><p class="t">Fiction d’anticipation</p>
      <p class="mb0">La scène qui suit est inventée. Les mécanismes, les institutions et les chiffres qu’elle
      mobilise ne le sont pas.</p></div>
      {ch['scene']}
    </section>
    <section aria-labelledby="decision">
      <h2 id="decision" style="margin-top:2.4rem">Votre décision</h2>
      <p>Choisissez une option : sa conséquence s’affiche et vos indicateurs se mettent à jour.
      Vous pouvez changer d’avis, l’effet précédent est annulé.</p>
      <noscript><div class="callout"><p class="t">Sans JavaScript</p><p class="mb0">Les quatre conséquences
      sont affichées ci-dessous. Le décompte des indicateurs, lui, nécessite JavaScript.</p></div></noscript>
      <ol class="choices">{"".join(choices)}</ol>
    </section>
    <section aria-labelledby="src">
      <h2 id="src">Sources de ce chapitre</h2>
      <ul class="source-list">{src}</ul>
    </section>
    <nav class="chapter-nav" aria-label="Navigation entre chapitres">{navprev}{navnext}</nav>
  </article>
</div>
"""

def build(outdir):
    n = len(CHAPTERS)
    for i, ch in enumerate(CHAPTERS):
        prev = CHAPTERS[i - 1] if i else None
        nxt = CHAPTERS[i + 1] if i + 1 < n else None
        path = f"jeu/{ch['slug']}/"
        ld = {"@context": "https://schema.org", "@type": "Chapter",
              "name": ch["titre"], "position": ch["n"],
              "isPartOf": {"@type": "Book", "name": "Le compte à rebours",
                           "url": BASE + "jeu/"},
              "url": BASE + path, "inLanguage": "fr-BE"}
        write(outdir, path, page(
            path, f"Chapitre {ch['n']} — {ch['titre']}", ch["meta_desc"], chapter_body(ch, prev, nxt),
            depth=2, trail=[("jeu/", "Le compte à rebours"), (path, f"Chapitre {ch['n']} · {ch['titre']}")],
            scripts=("jeu.js",), keywords=ch["kw"], nav_key="jeu/", extra_ld=[ld],
            section="Parcours narratif"))
    build_index(outdir)
    build_fins(outdir)

def build_index(outdir):
    cards = "".join(
        f'<a class="card" href="{c["slug"]}/"><p class="kicker">Chapitre {c["n"]} · {e(c["date"])}</p>'
        f'<h3>{e(c["titre"])}</h3><p>{e(c["meta_desc"])}</p></a>' for c in CHAPTERS)
    body = f"""
<div class="wrap">
  <div class="page-head">
    <p class="kicker">Parcours narratif · 7 chapitres · environ 30 minutes</p>
    <h1>Le compte à rebours</h1>
    <p class="lede">De septembre 2026 à un dimanche d’élection : un parcours à choix où chaque décision
    déplace trois indicateurs et rapproche — ou éloigne — la dissolution des Chambres.</p>
  </div>
</div>
<div class="wrap layout-side">
  <article class="prose">
    <h2 id="principe" style="margin-top:0">Le principe</h2>
    <p>Vous incarnez un·e jeune fonctionnaire détaché·e auprès du <a href="../glossaire/#comite-de-monitoring">Comité de
    monitoring</a>, l’organe qui chiffre chaque année l’écart budgétaire fédéral. Vous n’avez aucun pouvoir de
    décision, et c’est précisément ce qui rend le poste intéressant : vous voyez tout passer.</p>
    <p>Chaque chapitre s’ouvre sur un <strong>encadré factuel sourcé</strong> — mesures réellement adoptées,
    chiffres réellement publiés — puis bascule dans une <strong>scène de fiction</strong> clairement signalée.
    Vous tranchez. La conséquence est expliquée, et trois indicateurs bougent.</p>

    <h2 id="indicateurs">Les trois indicateurs</h2>
    <div class="stat-row">
      <div class="stat"><span class="v">50</span><span class="k"><strong>Crédibilité</strong> — la confiance
      accordée aux chiffres que vous produisez, par la presse, le Parlement et la Commission européenne.</span></div>
      <div class="stat"><span class="v">50</span><span class="k"><strong>Cohésion sociale</strong> — la capacité
      du corps social à absorber les décisions : conflits, exclusions, saturation des guichets.</span></div>
      <div class="stat"><span class="v">50</span><span class="k"><strong>Stabilité institutionnelle</strong> —
      la solidité de la coalition et des règles du jeu qui la tiennent debout.</span></div>
    </div>
    <p>S’y ajoute un compteur invisible : la <strong>tension</strong>. Elle ne se lit pas en chiffres mais en état
    du pays, de « législature stable » à « dissolution imminente ». C’est elle qui, croisée aux trois indicateurs,
    détermine lequel des <a href="fins/">six dénouements</a> vous obtenez.</p>

    <h2 id="regles">Ce que le jeu fait et ne fait pas</h2>
    <ul>
      <li>Il <strong>ne prédit rien</strong>. Les six dénouements sont des scénarios institutionnellement
      possibles, chacun accompagné de son degré de plausibilité et de ses précédents historiques.</li>
      <li>Il <strong>ne recommande aucun vote</strong>. Aucun choix n’est « le bon » : chacun a un coût explicite.</li>
      <li>Il <strong>fonctionne sans JavaScript</strong> : les conséquences sont écrites dans la page. Seul le
      décompte des indicateurs nécessite un navigateur moderne.</li>
      <li>Il <strong>ne collecte rien</strong>. Votre partie est enregistrée dans votre navigateur et n’en sort pas.</li>
    </ul>

    <div class="btnrow">
      <a class="btn" href="01-le-comite-de-monitoring/">Commencer le chapitre 1</a>
      <a class="btn ghost" href="fins/">Voir les six dénouements</a>
      <a class="btn ghost" href="../boussole/">Passer d’abord la boussole</a>
    </div>

    <h2 id="chapitres">Les sept chapitres</h2>
    <p>Chaque chapitre est une page autonome : vous pouvez entrer par n’importe laquelle, la lire comme un
    article et rejoindre le parcours ensuite.</p>
    <div class="grid grid-2">{cards}</div>
  </article>
  <aside class="side"><nav aria-label="Sommaire"><p class="kicker" style="margin-bottom:.6rem">Sur cette page</p>
  <ol><li><a href="#principe">Le principe</a></li><li><a href="#indicateurs">Les trois indicateurs</a></li>
  <li><a href="#regles">Ce que le jeu fait</a></li><li><a href="#chapitres">Les sept chapitres</a></li></ol></nav></aside>
</div>
"""
    ld = {"@context": "https://schema.org", "@type": "Game",
          "name": "Le compte à rebours", "url": BASE + "jeu/",
          "genre": ["Fiction interactive", "Éducation civique"],
          "inLanguage": "fr-BE", "numberOfPlayers": {"@type": "QuantitativeValue", "value": 1},
          "gamePlatform": "Navigateur web",
          "description": "Parcours narratif à choix multiples sur la crise budgétaire et institutionnelle belge de 2026-2027."}
    write(outdir, "jeu/", page(
        "jeu/", "Le compte à rebours — parcours narratif",
        "Sept chapitres à choix multiples sur la Belgique politique de septembre 2026 à un scrutin anticipé : budget, CPAS, rupture de coalition, dissolution. Faits sourcés, fiction assumée.",
        body, depth=1, trail=[("jeu/", "Le compte à rebours")], scripts=("jeu.js",),
        keywords=["jeu politique belge", "fiction interactive", "élections anticipées", "budget fédéral", "éducation civique"],
        nav_key="jeu/", og_type="website", extra_ld=[ld]))

def build_fins(outdir):
    blocks = "".join(
        f'<section class="ending" id="{f["slug"]}"><p class="meta">{e(f["meta"])}</p>'
        f'<h3>{e(f["titre"])}</h3>{f["corps"]}</section>' for f in FINS)
    body = f"""
<div class="wrap">
  <div class="page-head">
    <p class="kicker">Le compte à rebours · Dénouements</p>
    <h1>Les six dénouements</h1>
    <p class="lede">Six sorties de crise institutionnellement possibles pour la Belgique, avec leur degré de
    plausibilité, leurs précédents historiques et les signaux qui permettent de les repérer à l’avance.</p>
  </div>
</div>
<div class="wrap">
  <div class="prose" data-endings>
    {hud()}
    <div class="callout" data-verdict><p class="t">Aucune partie en cours</p>
    <p class="mb0">Les six dénouements ci-dessous sont tous décrits.
    <a href="../01-le-comite-de-monitoring/">Commencez le parcours</a> pour découvrir lequel votre partie déclenche.</p></div>
    <p>Aucun de ces dénouements n’est une prédiction. Ce sont des <strong>scénarios</strong> : des enchaînements
    compatibles avec le droit constitutionnel belge, l’arithmétique parlementaire de 2026 et les précédents des
    quarante dernières années. Ils sont classés du plus routinier au plus disruptif.</p>
    {blocks}
    <div class="btnrow">
      <a class="btn" href="../01-le-comite-de-monitoring/">Rejouer le parcours</a>
      <a class="btn ghost" href="../../dossiers/elections-anticipees-mode-demploi/">Le mode d’emploi juridique</a>
      <a class="btn ghost" href="../../boussole/">Passer la boussole électorale</a>
    </div>
  </div>
</div>
"""
    write(outdir, "jeu/fins/", page(
        "jeu/fins/", "Les six dénouements possibles",
        "Six sorties de crise pour la Belgique : législature au terme, gouvernement de mission, élections anticipées, affaires courantes, réforme de l’État, recomposition. Plausibilité et précédents.",
        body, depth=2, trail=[("jeu/", "Le compte à rebours"), ("jeu/fins/", "Les six dénouements")],
        scripts=("jeu.js",),
        keywords=["élections anticipées Belgique", "affaires courantes", "réforme de l’État", "dissolution des Chambres", "scénarios politiques"],
        nav_key="jeu/", section="Parcours narratif"))
