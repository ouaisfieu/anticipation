# -*- coding: utf-8 -*-
from layout import page, write, e, BASE

WAL_2026 = [("PS","pcolor-ps",27.9),("MR","pcolor-mr",21.0),("Les Engagés","pcolor-le",19.4),
            ("PTB","pcolor-ptb",17.0),("Ecolo","pcolor-ecolo",7.9)]
BXL_2026 = [("PTB","pcolor-ptb",25.5),("PS","pcolor-ps",18.4),("MR","pcolor-mr",16.4),
            ("Les Engagés","pcolor-le",11.7),("Ecolo","pcolor-ecolo",7.1),("DéFI","pcolor-defi",4.5)]
FLA_2026 = [("N-VA","pcolor-nva",25.5),("Vlaams Belang","pcolor-vb",25.4),("Vooruit","pcolor-vooruit",12.8),
            ("CD&V","pcolor-cdv",12.6),("PVDA","pcolor-ptb",9.8),("Groen","pcolor-groen",7.7),("Anders","pcolor-anders",5.6)]
BXL_JUIN = [("PTB","pcolor-ptb",24.8),("PS","pcolor-ps",18.3),("MR","pcolor-mr",13.9),("Les Engagés","pcolor-le",10.0)]

def bars(data, maxv=30.0):
    return '<ul class="pollbars">' + "".join(
        f'<li class="{cls}"><span><span class="swatch" aria-hidden="true"></span>{e(n)}</span>'
        f'<span class="bar"><i style="width:{v/maxv*100:.1f}%"></i></span>'
        f'<span class="v">{str(v).replace(".", ",")} %</span></li>' for n, cls, v in data) + '</ul>'

def build(outdir):
    body = f"""
<div class="wrap">
  <div class="page-head">
    <p class="kicker">Repères · intentions de vote</p>
    <h1>Où en sont les partis</h1>
    <p class="lede">Trois Régions, trois dynamiques opposées. Ce que disent les enquêtes de 2026 — et ce
    qu’elles ne disent pas.</p>
  </div>
</div>
<div class="wrap layout-side">
  <article class="prose">
    <div class="callout"><p class="t">Comment lire ces chiffres</p>
    <p class="mb0">Les données proviennent du Grand Baromètre Ipsos–Le Soir–RTL, vague du 2 au 9 mars 2026
    (2 602 répondants) et vague de juin 2026. Les marges d’erreur sont d’environ <strong>±3,1 points</strong> en
    Wallonie et en Flandre, <strong>±4 points</strong> à Bruxelles. Un écart inférieur à la marge — par exemple
    entre la N-VA et le Vlaams Belang — n’est pas un écart.</p></div>

    <h2 id="wallonie">Wallonie : le PS repasse en tête</h2>
    {bars(WAL_2026)}
    <p>Le PS retrouve la première place qu’il avait perdue en juin 2024, à <strong>27,9 %</strong>, devant un MR
    à 21 %. Les Engagés se maintiennent à un niveau élevé (19,4 %). Le PTB, à 17 %, progresse sans réaliser au sud
    la percée qu’il connaît à Bruxelles. Ecolo reste sous les 8 %.</p>
    <p>La lecture la plus plausible : l’application concrète des mesures d’activation, à partir de mars 2026,
    a produit un retour vers le parti historique de la protection sociale plutôt que vers l’opposition frontale.</p>

    <h2 id="bruxelles">Bruxelles : le basculement</h2>
    {bars(BXL_2026, 28.0)}
    <p>C’est le fait électoral marquant de la législature. Le PTB devient la première force de la Région avec
    <strong>25,5 %</strong> en mars, confirmés à <strong>24,8 %</strong> en juin. Le MR, vainqueur de 2024 avec
    environ 26 %, tombe à 16,4 % puis <strong>13,9 %</strong> — une division par deux en deux ans.</p>
    <h3>Vague de juin 2026</h3>
    {bars(BXL_JUIN, 28.0)}
    <p>Bruxelles concentre les effets de la limitation du chômage : c’est là que la densité de chômeurs de longue
    durée est la plus forte, donc là que le basculement vers les CPAS est le plus visible. C’est aussi la Région
    qui est restée près de six cents jours sans gouvernement.</p>

    <h2 id="flandre">Flandre : un duel à un dixième de point</h2>
    {bars(FLA_2026, 28.0)}
    <p>La N-VA (25,5 %) et le Vlaams Belang (25,4 %) sont à égalité statistique — l’écart est très inférieur à la
    marge d’erreur. Les vagues antérieures avaient donné le Vlaams Belang devant, à 26,7 % contre 23,4 %.</p>
    <p>Cette situation conditionne tout le reste : elle pousse la N-VA à durcir sa ligne socio-économique et
    identitaire pour retenir son électorat, ce qui rétrécit l’espace de compromis avec ses partenaires
    francophones au sein de la coalition fédérale.</p>

    <h2 id="limites">Ce que les sondages ne disent pas</h2>
    <ul>
      <li><strong>Ils ne donnent pas des sièges.</strong> La conversion en sièges dépend de la méthode D’Hondt et
      des circonscriptions provinciales : deux partis à égalité de voix peuvent obtenir un nombre de sièges
      différent.</li>
      <li><strong>Ils ne disent pas qui gouvernera.</strong> En Belgique, le gouvernement se négocie après le
      scrutin. Un parti en tête peut rester dans l’opposition — c’est arrivé au PS en 2024.</li>
      <li><strong>Ils mesurent une intention, pas un vote.</strong> Le vote étant obligatoire aux scrutins
      fédéral, régional et européen, les électeurs indécis se décident souvent dans les derniers jours.</li>
      <li><strong>Ils ne captent pas les recompositions.</strong> Un parti qui change de nom, comme l’Open Vld
      devenu Anders en janvier 2026, met plusieurs vagues à retrouver une mesure stable.</li>
    </ul>
    <div class="btnrow">
      <a class="btn" href="../boussole/">Situer vos propres positions</a>
      <a class="btn ghost" href="../partis/">Les fiches partis</a>
    </div>
  </article>
  <aside class="side"><nav aria-label="Sommaire"><p class="kicker" style="margin-bottom:.6rem">Sur cette page</p>
  <ol><li><a href="#wallonie">Wallonie</a></li><li><a href="#bruxelles">Bruxelles</a></li>
  <li><a href="#flandre">Flandre</a></li><li><a href="#limites">Les limites</a></li></ol></nav></aside>
</div>
"""
    ld = {"@context":"https://schema.org","@type":"Dataset",
          "name":"Intentions de vote en Belgique, 2026",
          "description":"Intentions de vote par Région issues du Grand Baromètre Ipsos–Le Soir–RTL, vagues de mars et juin 2026.",
          "temporalCoverage":"2026-03/2026-06","spatialCoverage":"Belgique","inLanguage":"fr-BE",
          "creator":{"@type":"Organization","name":"Ipsos – Le Soir – RTL"}}
    write(outdir, "sondages/", page(
        "sondages/", "Sondages 2026 : les intentions de vote",
        "Grand Baromètre Ipsos 2026 : le PS premier en Wallonie (27,9 %), le PTB premier à Bruxelles (25,5 %), N-VA et Vlaams Belang à égalité en Flandre. Chiffres, marges d’erreur et limites.",
        body, depth=1, trail=[("sondages/","Sondages")], nav_key="sondages/", extra_ld=[ld],
        keywords=["sondage Belgique 2026","Grand Baromètre Ipsos","intentions de vote","PTB Bruxelles","Vlaams Belang N-VA"]))
