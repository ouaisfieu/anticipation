# -*- coding: utf-8 -*-
from layout import page, write, e, BASE
from data_partis import PARTIS, FLANDRE

BY = {p["slug"]: p for p in PARTIS}

def fiche_body(p):
    ch = "".join(f'<div class="stat"><span class="v">{e(v)}</span><span class="k">{e(k)}</span></div>'
                 for v, k in p["chiffres"])
    mes = "".join(f"<tr><th scope=\"row\">{e(t)}</th><td>{e(d)}</td></tr>" for t, d in p["mesures"])
    fo = "".join(f"<li>{e(x)}</li>" for x in p["forces"])
    fa = "".join(f"<li>{e(x)}</li>" for x in p["faiblesses"])
    autres = "".join(
        f'<a class="card {BY[s]["cls"]}" href="../{s}/"><p class="kicker">{e(BY[s]["famille"])}</p>'
        f'<h3>{e(BY[s]["long"])}</h3><p>{e(BY[s]["resume"])}</p></a>' for s in p["aussi"] if s in BY)
    return f"""
<div class="wrap">
  <div class="page-head {p['cls']}">
    <p class="kicker">Fiche parti · francophone</p>
    <div class="party-head"><span class="chip" aria-hidden="true">{e(p['abbr'])}</span>
      <h1 style="margin:0">{e(p['long'])}</h1></div>
    <p class="lede">{e(p['resume'])}</p>
  </div>
</div>
<div class="wrap layout-side">
  <article class="prose {p['cls']}">
    <dl class="dl-facts">
      <dt>Famille politique</dt><dd>{e(p['famille'])}</dd>
      <dt>Direction</dt><dd>{e(p['president'])}</dd>
      <dt>Site officiel</dt><dd><a href="{p['site']}" rel="noopener nofollow" target="_blank">{e(p['site'])}</a></dd>
      <dt>Position en 2026</dt><dd>{e(p['famille'])}</dd>
    </dl>

    <h2 id="chiffres" style="margin-top:2rem">Les chiffres</h2>
    <div class="stat-row">{ch}</div>
    <p class="muted"><small>Résultats : scrutins du 9 juin 2024 (SPF Intérieur). Intentions de vote :
    Grand Baromètre Ipsos–Le Soir–RTL, vague de mars 2026 ; vague de juin 2026 pour Bruxelles.
    Marges d’erreur d’environ ±3,1 points en Wallonie et en Flandre, ±4 points à Bruxelles.</small></p>

    <h2 id="adn">L’ADN du parti</h2>
    {p['adn']}

    <h2 id="mesures">Ce qu’il défend, thème par thème</h2>
    <div class="table-scroll"><table>
      <caption>Positions programmatiques de {e(p['nom'])}, 2024-2026</caption>
      <thead><tr><th scope="col">Thème</th><th scope="col">Position</th></tr></thead>
      <tbody>{mes}</tbody>
    </table></div>

    <h2 id="bilan">Forces et angles morts</h2>
    <div class="grid grid-2">
      <div class="callout"><p class="t">Forces</p><ul style="margin-bottom:0">{fo}</ul></div>
      <div class="callout warn"><p class="t">Fragilités</p><ul style="margin-bottom:0">{fa}</ul></div>
    </div>

    <h2 id="suite">Aller plus loin</h2>
    <div class="btnrow">
      <a class="btn" href="../../boussole/">Mesurer votre proximité avec ce parti</a>
      <a class="btn ghost" href="../../sondages/">Voir la dynamique dans les sondages</a>
    </div>
    <h3>Autres fiches</h3>
    <div class="grid grid-3">{autres}</div>
  </article>
  <aside class="side"><nav aria-label="Sommaire"><p class="kicker" style="margin-bottom:.6rem">Sur cette page</p>
    <ol><li><a href="#chiffres">Les chiffres</a></li><li><a href="#adn">L’ADN du parti</a></li>
    <li><a href="#mesures">Positions</a></li><li><a href="#bilan">Forces et angles morts</a></li>
    <li><a href="#suite">Aller plus loin</a></li></ol></nav></aside>
</div>
"""

def build(outdir):
    for p in PARTIS:
        path = f"partis/{p['slug']}/"
        ld = {"@context": "https://schema.org", "@type": "PoliticalParty",
              "name": p["long"], "alternateName": p["nom"], "url": p["site"],
              "areaServed": "BE", "sameAs": [p["site"]]}
        write(outdir, path, page(
            path, f"{p['long']} ({p['nom']})", p["meta_desc"], fiche_body(p),
            depth=2, trail=[("partis/", "Les partis"), (path, p["long"])],
            keywords=p["kw"], nav_key="partis/", extra_ld=[ld], section="Fiches partis"))
    build_index(outdir)
    build_flandre(outdir)

def build_index(outdir):
    cards = "".join(
        f'<a class="card {p["cls"]}" href="{p["slug"]}/">'
        f'<div class="party-head" style="margin-bottom:.4rem"><span class="chip" aria-hidden="true">{e(p["abbr"])}</span>'
        f'<span><p class="kicker" style="margin:0">{e(p["famille"])}</p>'
        f'<h3 style="margin:.1rem 0 0">{e(p["long"])}</h3></span></div>'
        f'<p>{e(p["resume"])}</p></a>' for p in PARTIS)
    rows = "".join(
        f'<tr><th scope="row">{e(p["long"])}</th><td>{e(p["famille"])}</td>'
        f'<td>{e(p["president"])}</td><td class="num">{e(p["chiffres"][0][0])}</td></tr>' for p in PARTIS)
    body = f"""
<div class="wrap">
  <div class="page-head">
    <p class="kicker">Repères</p>
    <h1>Les partis francophones belges</h1>
    <p class="lede">Six formations, six logiques. Programme, bilan de coalition, dynamique électorale et
    fragilités — sans recommandation de vote.</p>
  </div>
</div>
<div class="wrap">
  <article class="prose">
    <p>Le paysage francophone de 2026 s’organise sur deux fractures qui ne se recouvrent pas. La première est
    socio-économique : faut-il assainir par l’activation et la baisse de la dépense, ou par la contribution des
    patrimoines et du capital ? La seconde est institutionnelle : que faire de Bruxelles, du financement de la
    Fédération Wallonie-Bruxelles et des demandes flamandes de régionalisation ?</p>
    <p>Chaque fiche est une page autonome : elle peut se lire seule, sans avoir parcouru le reste du site.</p>
    <div class="grid grid-3">{cards}</div>

    <h2 id="tableau">Vue d’ensemble</h2>
    <div class="table-scroll"><table>
      <caption>Les six partis francophones, août 2026</caption>
      <thead><tr><th scope="col">Parti</th><th scope="col">Famille</th><th scope="col">Direction</th>
      <th scope="col" class="num">Chambre 2024</th></tr></thead>
      <tbody>{rows}</tbody>
    </table></div>

    <h2 id="flandre">Et en Flandre ?</h2>
    <p>Aucune majorité fédérale ne se compose sans le nord du pays. Le rapport de force flamand détermine
    directement ce que les partis francophones peuvent obtenir — et ce qu’ils doivent concéder.</p>
    <div class="btnrow"><a class="btn" href="flandre/">Les sept partis flamands</a>
    <a class="btn ghost" href="../boussole/">Passer la boussole électorale</a></div>
  </article>
</div>
"""
    write(outdir, "partis/", page(
        "partis/", "Les partis politiques francophones belges",
        "MR, PS, PTB, Les Engagés, Ecolo, DéFI : programme, bilan de coalition 2024-2026, résultats électoraux et fragilités. Fiches comparables, sans recommandation de vote.",
        body, depth=1, trail=[("partis/", "Les partis")], nav_key="partis/", og_type="website",
        keywords=["partis politiques belges", "partis francophones", "MR PS PTB Les Engagés Ecolo DéFI", "programmes électoraux"]))

def build_flandre(outdir):
    rows = "".join(
        f'<tr class="{cls}"><th scope="row"><span class="swatch" aria-hidden="true"></span>{e(nom)}</th>'
        f'<td>{e(fam)}</td><td>{e(pres)}</td><td class="num">{e(pct)}</td></tr>'
        for nom, cls, fam, pres, pct, _ in FLANDRE)
    blocs = "".join(
        f'<div class="callout {cls}"><p class="t">{e(nom)} — {e(pct)}</p><p class="mb0">{e(txt)}</p></div>'
        for nom, cls, fam, pres, pct, txt in FLANDRE)
    body = f"""
<div class="wrap">
  <div class="page-head">
    <p class="kicker">Repères · l’autre moitié du Parlement</p>
    <h1>Les partis flamands, vus du sud</h1>
    <p class="lede">Sept formations qui décident, à elles seules, de ce qu’une majorité fédérale peut faire.
    Intentions de vote de mars 2026 et rôle dans les équilibres actuels.</p>
  </div>
</div>
<div class="wrap">
  <article class="prose">
    <p>La Chambre compte 150 sièges, dont environ 87 issus des circonscriptions flamandes. Aucune coalition
    fédérale ne se forme sans une majorité dans le groupe linguistique néerlandais — c’est la contrainte
    arithmétique la plus structurante de la politique belge, et celle que les débats francophones oublient le
    plus souvent.</p>
    <p>Deux faits dominent 2026 : le <strong>duel N-VA / Vlaams Belang</strong>, qui se joue à un dixième de
    point, et la <strong>progression continue du PVDA</strong>, seule formation à croître dans les trois Régions.</p>

    <h2 id="tableau">Le rapport de force</h2>
    <div class="table-scroll"><table>
      <caption>Intentions de vote en Flandre, Grand Baromètre Ipsos, mars 2026 (±3,1 points)</caption>
      <thead><tr><th scope="col">Parti</th><th scope="col">Famille</th><th scope="col">Direction</th>
      <th scope="col" class="num">Mars 2026</th></tr></thead>
      <tbody>{rows}</tbody>
    </table></div>

    <h2 id="roles">Le rôle de chacun</h2>
    {blocs}

    <h2 id="cordon">Une asymétrie décisive</h2>
    <p>Le <a href="../../dossiers/cordon-sanitaire/">cordon sanitaire</a> francophone est double — politique et
    médiatique — tandis que du côté flamand seul le cordon politique s’applique : le Vlaams Belang a accès aux
    plateaux. Cette asymétrie explique une partie de l’écart de dynamique entre les deux extrêmes droites du
    pays, et elle sera l’un des points de bascule de la prochaine campagne.</p>
    <div class="btnrow"><a class="btn" href="../">Les six partis francophones</a>
    <a class="btn ghost" href="../../sondages/">Tous les sondages</a></div>
  </article>
</div>
"""
    write(outdir, "partis/flandre/", page(
        "partis/flandre/", "Les partis flamands, vus du sud",
        "Le rapport de force flamand en 2026 : duel N-VA / Vlaams Belang à 25 %, progression du PVDA, rôle de chaque parti dans la coalition fédérale Arizona et à Bruxelles.",
        body, depth=2, trail=[("partis/", "Les partis"), ("partis/flandre/", "Les partis flamands")],
        nav_key="partis/", keywords=["N-VA", "Vlaams Belang", "Vooruit", "CD&V", "Anders Open Vld", "partis flamands"]))
