# -*- coding: utf-8 -*-
"""Page de la boussole. Les propositions sont lues directement dans
assets/js/data-boussole.js : une seule source de vérité, et le tableau HTML
statique ne peut pas diverger du questionnaire interactif."""
import re, os
from layout import page, write, e, BASE

PIDS = [("ps","PS","pcolor-ps"),("mr","MR","pcolor-mr"),("ptb","PTB","pcolor-ptb"),
        ("le","Les Engagés","pcolor-le"),("ecolo","Ecolo","pcolor-ecolo"),("defi","DéFI","pcolor-defi")]
MOT = {2:"Soutient nettement",1:"Plutôt favorable",0:"Position nuancée",
       -1:"Plutôt défavorable",-2:"S’y oppose nettement"}
SIG = {2:"++",1:"+",0:"~",-1:"−",-2:"−−"}

def parse(js_path):
    src = open(js_path, encoding="utf-8").read()
    block = src[src.index("var Q = ["):src.index("];", src.index("var Q = ["))]
    out = []
    for m in re.finditer(r"\{\s*t:'(.*?)',\s*q:'(.*?)',\s*\n?\s*eco:([+\-0-9.]+),\s*gal:([+\-0-9.]+),\s*p:\{(.*?)\}\s*\}", block, re.S):
        t, q, eco, gal, p = m.groups()
        pos = {}
        for kv in p.split(","):
            k, v = kv.split(":")
            pos[k.strip()] = int(v)
        out.append({"t": t, "q": q, "eco": float(eco), "gal": float(gal), "p": pos})
    return out

def build(outdir):
    Q = parse(os.path.join(outdir, "assets/js/data-boussole.js"))
    assert len(Q) == 24, f"attendu 24 propositions, trouvé {len(Q)}"
    head = "".join(f'<th scope="col" class="{c}"><span class="swatch" aria-hidden="true"></span>{e(n)}</th>'
                   for _, n, c in PIDS)
    rows = "".join(
        f'<tr><th scope="row"><small class="muted">{e(q["t"])}</small><br>{e(q["q"])}</th>' +
        "".join(f'<td class="num"><abbr title="{MOT[q["p"][pid]]}">{SIG[q["p"][pid]]}</abbr></td>'
                for pid, _, _ in PIDS) + "</tr>"
        for q in Q)
    body = f"""
<div class="wrap">
  <div class="page-head">
    <p class="kicker">Test électoral · 24 propositions · 5 minutes</p>
    <h1>La boussole</h1>
    <p class="lede">Vingt-quatre propositions tirées des débats réellement en cours en Belgique. À la fin :
    votre position sur deux axes, et votre distance aux six partis francophones.</p>
  </div>
</div>
<div class="wrap">
  <div class="prose">
    <p>Ce n’est pas un test de personnalité et ce n’est pas un conseil de vote. C’est un instrument de
    <strong>positionnement</strong> : il mesure une distance moyenne entre vos réponses et les positions
    documentées des partis, sur des questions qui font l’objet d’un désaccord réel — pas sur des principes
    généraux que tout le monde partage.</p>
    <noscript><div class="callout warn"><p class="t">JavaScript désactivé</p>
    <p class="mb0">Le questionnaire interactif ne peut pas fonctionner. Les vingt-quatre propositions et la
    position de chaque parti sont néanmoins reproduites en clair dans le tableau plus bas.</p></div></noscript>
    <div id="boussole" aria-live="polite"></div>
  </div>
</div>
<div class="wrap">
  <article class="prose">
    <h2 id="tableau">Les 24 propositions et la position des partis</h2>
    <p>Ce tableau est la matière première du test. Il est publié pour que le résultat soit vérifiable :
    vous pouvez contester une case, et vous saurez exactement laquelle.</p>
    <div class="table-scroll"><table>
      <caption>Positionnement des six partis francophones sur les 24 propositions —
      <strong>++</strong> soutient nettement, <strong>+</strong> plutôt favorable, <strong>~</strong> position
      nuancée, <strong>−</strong> plutôt défavorable, <strong>−−</strong> s’y oppose nettement</caption>
      <thead><tr><th scope="col">Proposition</th>{head}</tr></thead>
      <tbody>{rows}</tbody>
    </table></div>

    <h2 id="axes">Les deux axes</h2>
    <p>La science politique décrit habituellement les systèmes partisans européens par deux dimensions qui ne se
    superposent pas :</p>
    <ul>
      <li><strong>L’axe socio-économique</strong> oppose l’intervention publique et la redistribution à la logique
      de marché et d’activation. C’est l’axe historique du clivage gauche-droite.</li>
      <li><strong>L’axe socioculturel</strong>, dit <strong>GAL/TAN</strong>, oppose les valeurs
      <em>Green / Alternative / Libertarian</em> aux valeurs <em>Traditional / Authoritarian / Nationalist</em> :
      écologie, migration, autorité, question nationale.</li>
    </ul>
    <p>Un parti peut être à gauche sur le premier axe et conservateur sur le second — ou l’inverse. C’est
    précisément ce que deux axes permettent de voir, et qu’un simple classement gauche-droite masque.</p>

    <h2 id="limites">Les limites, dites franchement</h2>
    <ul>
      <li><strong>Les positions sont interprétées.</strong> Elles reposent sur les programmes de 2024, les accords
      de gouvernement 2024-2026 et les votes publics. Elles sont discutables : c’est pourquoi elles sont
      publiées ligne par ligne.</li>
      <li><strong>L’intensité n’est pas mesurée.</strong> Vos vingt-quatre réponses pèsent le même poids, alors
      que deux ou trois d’entre elles déterminent probablement votre vote à elles seules.</li>
      <li><strong>Les compromis de coalition sont invisibles.</strong> C’est l’angle mort de tous les systèmes
      d’aide au vote : un électeur proche d’un parti sur le papier peut être surpris par ce que ce parti signe
      une fois en gouvernement.</li>
      <li><strong>Seuls les partis francophones figurent ici.</strong> Le rapport de force flamand est traité
      <a href="../partis/flandre/">dans une page distincte</a>.</li>
    </ul>
    <p>La recherche menée notamment par l’ISPOLE (UCLouvain) montre que ces outils augmentent l’« efficacité
    politique interne » — la confiance de l’électeur dans sa capacité à choisir — sans pour autant réduire les
    inégalités socio-économiques face au vote. C’est utile, et c’est limité.</p>

    <h2 id="suite">Ensuite</h2>
    <div class="btnrow">
      <a class="btn" href="../jeu/">Jouer le parcours narratif</a>
      <a class="btn ghost" href="../partis/">Lire les fiches partis</a>
      <a class="btn ghost" href="../a-propos/#methode">La méthode en détail</a>
    </div>
  </article>
</div>
"""
    ld = {"@context":"https://schema.org","@type":"Quiz","name":"La boussole — test électoral belge",
          "url":BASE+"boussole/","educationalLevel":"Grand public","inLanguage":"fr-BE",
          "about":{"@type":"Thing","name":"Positionnement politique en Belgique francophone"},
          "numberOfQuestions":24,
          "description":"Vingt-quatre propositions issues des débats belges de 2026 pour situer ses positions sur deux axes et mesurer sa distance aux six partis francophones."}
    write(outdir, "boussole/", page(
        "boussole/", "La boussole — test électoral belge en 24 propositions",
        "Test électoral belge : 24 propositions réellement débattues en 2026 (chômage, patrimoine, indexation, cordon sanitaire) pour situer vos positions face au MR, PS, PTB, Les Engagés, Ecolo et DéFI.",
        body, depth=1, trail=[("boussole/","La boussole")], nav_key="boussole/", og_type="website",
        scripts=("data-boussole.js", "boussole.js"), extra_ld=[ld],
        keywords=["test électoral belge","boussole politique","positionnement politique","GAL TAN","partis francophones"]))
