# -*- coding: utf-8 -*-
from layout import page, write, e, BASE, SITE

def build(outdir):
    body = """
<div class="wrap">
  <div class="hero">
    <p class="kicker">Jeu d’anticipation politique · Belgique · mise à jour août 2026</p>
    <h1>Et si la Belgique votait avant terme&nbsp;?</h1>
    <p class="lede">Un parcours narratif en sept chapitres et une boussole électorale, construits sur les faits
    réellement établis de la législature 2024-2029 : dix milliards à trouver, cent mille personnes basculées vers
    les CPAS, une Région restée six cents jours sans gouvernement, et un cordon sanitaire que l’arithmétique
    pourrait bientôt mettre à l’épreuve.</p>
    <div class="btnrow">
      <a class="btn" href="jeu/01-le-comite-de-monitoring/">Commencer le parcours</a>
      <a class="btn ghost" href="boussole/">Passer la boussole</a>
      <a class="btn ghost" href="dossiers/">Lire les dossiers</a>
    </div>
  </div>
</div>

<div class="wrap">
  <section class="prose" aria-labelledby="etat">
    <h2 id="etat" style="margin-top:0">Où en est la Belgique, en août 2026</h2>
    <div class="stat-row">
      <div class="stat"><span class="v">10 Mds €</span><span class="k">d’effort budgétaire annoncés le 10 juillet 2026 pour 2029, au-delà du minimum estimé par les administrations</span></div>
      <div class="stat"><span class="v">≈ 100 000</span><span class="k">personnes basculées de l’assurance chômage vers les CPAS depuis mars 2026</span></div>
      <div class="stat"><span class="v">≈ 600 j</span><span class="k">sans gouvernement à Bruxelles, jusqu’à la formation du gouvernement Dilliès en février 2026</span></div>
      <div class="stat"><span class="v">5,2 %</span><span class="k">de déficit public, pour une dette proche de 115 % du PIB</span></div>
    </div>
    <p>Le pays sort d’un été calme et entre dans un automne qui ne le sera pas. Le conclave budgétaire de fin
    septembre doit trancher ce que l’accord de juillet a explicitement laissé de côté : la répartition entre
    économies et recettes. Le <a href="partis/mr/">MR</a> refuse tout nouvel impôt ;
    <a href="partis/les-engages/">Les Engagés</a> proposent de faire contribuer les patrimoines au-delà de
    500 000 €. Entre les deux, il n’y a pas de position moyenne, il y a un arbitrage.</p>
    <p>Pendant ce temps, les enquêtes d’opinion décrivent trois pays. En Wallonie, le
    <a href="partis/ps/">PS</a> est repassé en tête. À Bruxelles, le <a href="partis/ptb/">PTB</a> est devenu la
    première force avec un électeur sur quatre, tandis que le MR y a perdu la moitié de son score de 2024. En
    Flandre, la N-VA et le Vlaams Belang sont à un dixième de point l’un de l’autre. Aucune de ces trois
    dynamiques ne pousse dans le même sens.</p>
    <div class="callout fact"><p class="t">Le dernier fait marquant</p>
    <p class="mb0">Du 14 au 17 août 2026, le plus important incendie de forêt de l’histoire belge a ravagé environ
    3 000 hectares dans les Hautes Fagnes, entraînant des évacuations et une coordination fédérale et régionale
    improvisée en pleine trêve estivale. Le monde politique est resté, pour l’essentiel, en retrait —
    ce qui, à trois semaines de la rentrée, est en soi une information.</p></div>
  </section>
</div>

<div class="wrap">
  <section class="prose" aria-labelledby="entrees">
    <h2 id="entrees">Trois façons d’entrer</h2>
    <div class="grid grid-3">
      <a class="card" href="jeu/"><p class="kicker">Jouer · 30 minutes</p><h3>Le compte à rebours</h3>
      <p>Sept chapitres, de septembre 2026 à un dimanche d’élection. Vous incarnez un·e fonctionnaire du Comité
      de monitoring : chaque décision déplace trois indicateurs et rapproche — ou non — la dissolution.</p></a>
      <a class="card" href="boussole/"><p class="kicker">Se situer · 5 minutes</p><h3>La boussole</h3>
      <p>Vingt-quatre propositions réellement débattues en 2026. Deux axes, six partis, et un tableau publié
      ligne par ligne pour que le résultat soit contestable.</p></a>
      <a class="card" href="dossiers/"><p class="kicker">Comprendre · à la carte</p><h3>Les six dossiers</h3>
      <p>Chômage limité à deux ans, dix milliards budgétaires, réforme des pensions, crise bruxelloise, cordon
      sanitaire, mode d’emploi des élections anticipées.</p></a>
    </div>
  </section>
</div>

<div class="wrap">
  <section class="prose" aria-labelledby="fins">
    <h2 id="fins">Six dénouements possibles</h2>
    <p>Le parcours ne prédit rien. Il conduit à l’un des six scénarios compatibles avec le droit constitutionnel
    belge, l’arithmétique parlementaire de 2026 et les précédents des quarante dernières années.</p>
    <div class="grid grid-3">
      <a class="card" href="jeu/fins/#fin-legislature"><h3>La législature va au bout</h3><p>Le dénouement le plus fréquent : les crises se règlent par un gel de mesure, pas par une dissolution.</p></a>
      <a class="card" href="jeu/fins/#fin-gouvernement-de-mission"><h3>Le gouvernement de mission</h3><p>Une équipe resserrée, un mandat écrit, une durée limitée. Pas prévu par la Constitution, pas interdit par elle.</p></a>
      <a class="card" href="jeu/fins/#fin-anticipees"><h3>Les élections anticipées</h3><p>Article 46, scrutin dans les quarante jours — et un calendrier électoral désynchronisé pour cinq ans.</p></a>
      <a class="card" href="jeu/fins/#fin-affaires-courantes"><h3>Le pays en affaires courantes</h3><p>541 jours en 2010-2011, près de 600 à Bruxelles en 2024-2026. Le coût est invisible et réel.</p></a>
      <a class="card" href="jeu/fins/#fin-institutionnelle"><h3>La sortie institutionnelle</h3><p>Quand le désaccord n’est plus gérable dans les institutions, la Belgique change les institutions.</p></a>
      <a class="card" href="jeu/fins/#fin-recomposition"><h3>La recomposition</h3><p>Le jour où le cordon sanitaire coûte le gouvernement, ce n’est plus une règle, c’est une décision.</p></a>
    </div>
  </section>
</div>

<div class="wrap">
  <section class="prose" aria-labelledby="promesse">
    <h2 id="promesse">Ce que ce site promet</h2>
    <div class="grid grid-2">
      <div class="callout fact"><p class="t">Ce qu’il fait</p>
      <ul style="margin-bottom:0">
        <li>Distinguer explicitement les <strong>faits sourcés</strong> de la <strong>fiction d’anticipation</strong>, encadré par encadré.</li>
        <li>Publier ses <strong>sources</strong> sur chaque page, et sa méthode de positionnement ligne par ligne.</li>
        <li>Fonctionner <strong>sans JavaScript</strong> pour la lecture : le texte est dans la page, pas dans un script.</li>
        <li>Ne <strong>rien collecter</strong> : aucune donnée ne quitte votre navigateur.</li>
      </ul></div>
      <div class="callout warn"><p class="t">Ce qu’il ne fait pas</p>
      <ul style="margin-bottom:0">
        <li>Il ne <strong>prédit</strong> aucun résultat électoral.</li>
        <li>Il ne <strong>recommande</strong> aucun vote : chaque choix a un coût explicite.</li>
        <li>Il ne <strong>remplace</strong> pas les outils académiques comme le Test électoral de l’UCLouvain.</li>
        <li>Il ne prétend pas à la <strong>neutralité parfaite</strong> : le choix des questions est déjà un choix.</li>
      </ul></div>
    </div>
    <div class="btnrow"><a class="btn ghost" href="a-propos/">Méthode, sources et limites</a></div>
  </section>
</div>
"""
    ld_site = {"@context":"https://schema.org","@type":"WebSite","name":SITE,
               "alternateName":"Anticipation — le jeu de la Belgique politique",
               "url":BASE,"inLanguage":"fr-BE",
               "description":"Jeu textuel d’anticipation et outils de compréhension sur la situation politique et démocratique belge."}
    ld_org = {"@context":"https://schema.org","@type":"Organization","name":SITE,"url":BASE,
              "logo":BASE+"assets/img/favicon.svg","sameAs":["https://github.com/ouaisfieu/anticipation"]}
    write(outdir, "index.html", page(
        "", "Et si la Belgique votait avant terme ?",
        "Jeu textuel d’anticipation sur la crise politique belge : parcours narratif en 7 chapitres, boussole électorale et dossiers sourcés sur le budget, le chômage et Bruxelles. Août 2026.",
        body, depth=0, trail=None, nav_key="", og_type="website", extra_ld=[ld_site, ld_org],
        keywords=["politique belge","élections anticipées Belgique","jeu politique","test électoral belge","gouvernement De Wever","crise démocratique"]))

    apropos = """
<div class="wrap">
  <div class="page-head">
    <p class="kicker">À propos</p>
    <h1>Méthode, sources et limites</h1>
    <p class="lede">Comment ce site est fabriqué, ce qu’il tient pour établi, ce qu’il invente, et où il peut
    se tromper.</p>
  </div>
</div>
<div class="wrap layout-side">
  <article class="prose">
    <h2 id="projet" style="margin-top:0">Le projet</h2>
    <p><strong>Anticipation</strong> est un site d’éducation civique par le jeu, consacré à la situation politique
    et démocratique belge. Il part d’un constat simple : les mécanismes qui décident réellement — l’article 46 de
    la Constitution, la méthode D’Hondt, le régime des affaires courantes, le calendrier d’un conclave — sont
    rarement expliqués, alors qu’ils déterminent ce qu’un vote peut ou ne peut pas produire.</p>
    <p>Le format retenu est celui du <em>gamebook</em> : une fiction à choix qui sert de véhicule à des
    explications factuelles. Le jeu n’est pas un habillage du contenu ; c’est le moyen de faire éprouver un
    arbitrage plutôt que de le décrire.</p>

    <h2 id="fiction">Faits et fiction</h2>
    <p>La séparation est la règle de fabrication la plus stricte du site.</p>
    <ul>
      <li>Les encadrés <strong>« Ce qui est vrai »</strong> ne contiennent que des éléments établis : mesures
      adoptées, chiffres publiés, dates vérifiables. Chaque chapitre publie ses sources.</li>
      <li>Les encadrés <strong>« Fiction d’anticipation »</strong> signalent le récit. Les personnages, les scènes
      et les dialogues sont inventés. Aucun propos n’est attribué à une personne réelle.</li>
      <li>Les <strong>six dénouements</strong> sont des scénarios, pas des prédictions. Chacun est accompagné de
      son degré de plausibilité et de ses précédents historiques.</li>
    </ul>

    <h2 id="methode">La méthode de la boussole</h2>
    <p>Les vingt-quatre propositions ont été choisies selon trois critères : elles font l’objet d’un
    <strong>désaccord réel</strong> entre partis, elles portent sur des décisions <strong>en cours</strong> en
    2026, et elles couvrent les <strong>deux axes</strong> de la science politique comparée (socio-économique et
    GAL/TAN).</p>
    <p>Les positions des partis sont codées de −2 à +2 à partir des programmes de 2024, des accords de
    gouvernement fédéral et régionaux 2024-2026, des votes publics et des prises de position officielles. Elles
    sont <a href="../boussole/#tableau">publiées intégralement</a>, ligne par ligne : c’est la seule manière de
    rendre le résultat contestable.</p>
    <p>Le calcul de proximité est un calcul de distance moyenne : pour chaque proposition, la proximité vaut
    <code>1 − |votre réponse − position du parti| / 4</code>, moyennée sur les propositions auxquelles vous avez
    répondu. Le positionnement sur les axes est une somme pondérée des réponses, normalisée entre −1 et +1.</p>
    <p><strong>Limites assumées :</strong> l’intensité des préférences n’est pas mesurée ; les compromis de
    coalition ne sont pas modélisés ; le choix des propositions est lui-même un choix éditorial. Ce site ne
    remplace pas les outils académiques, en particulier le <em>Test électoral</em> développé par l’ISPOLE
    (UCLouvain) et l’Université d’Anvers.</p>

    <h2 id="donnees">Les données chiffrées</h2>
    <ul>
      <li><strong>Résultats électoraux</strong> : scrutins du 9 juin 2024, résultats officiels du SPF Intérieur.</li>
      <li><strong>Intentions de vote</strong> : Grand Baromètre Ipsos–Le Soir–RTL, vague du 2 au 9 mars 2026
      (2 602 répondants, ±3,1 points en Wallonie et en Flandre, ±4 points à Bruxelles) et vague de juin 2026.</li>
      <li><strong>Finances publiques</strong> : Banque nationale de Belgique, Bureau fédéral du Plan, Comité de
      monitoring, Commission européenne.</li>
      <li><strong>Mesures sociales</strong> : textes des accords de gouvernement, communications officielles
      (belgium.be, ONEM, CAPAC), fédérations de CPAS et Union des Villes et Communes de Wallonie.</li>
    </ul>
    <p>Les chiffres arrêtés au <strong>18 août 2026</strong>. Les enquêtes d’opinion ont des marges d’erreur :
    un écart inférieur à la marge n’est pas un écart.</p>

    <h2 id="equilibre">Équilibre et parti pris</h2>
    <p>Le site ne recommande aucun vote et ne classe pas les partis par mérite. Chaque fiche présente forces et
    fragilités selon la même grille ; chaque dossier expose les arguments de la majorité et de l’opposition.</p>
    <p>Il ne prétend pas pour autant à la neutralité parfaite, qui n’existe pas : décider qu’une question mérite
    d’être posée est déjà un choix. Ce qui est promis, c’est la <strong>traçabilité</strong> — vous pouvez
    remonter à la source de chaque affirmation et contester chaque codage.</p>
    <p>Sur l’extrême droite, le site adopte une position explicite : il documente le <a
    href="../dossiers/cordon-sanitaire/">cordon sanitaire</a>, expose les arguments pour et contre, et n’intègre
    pas les formations concernées à la boussole francophone — parce qu’aucune ne dispose d’une représentation
    parlementaire francophone permettant un codage sur des votes.</p>

    <h2 id="technique">Comment c’est fait</h2>
    <p>HTML, CSS et JavaScript, sans framework, sans dépendance externe, sans police distante et sans traceur.
    Chaque page est un fichier statique complet : titre, description, canonical, données structurées
    <a href="https://schema.org" rel="noopener nofollow" target="_blank">schema.org</a>, Open Graph et fil
    d’Ariane. Le site est conçu pour que <strong>chaque page soit un point d’entrée valable</strong> —
    lisible seule, sans avoir parcouru le reste.</p>
    <p>Le JavaScript est une amélioration, jamais une condition : les textes du jeu et le tableau de la boussole
    sont présents dans le HTML. Sans script, on perd le décompte des indicateurs et le questionnaire interactif,
    pas le contenu. Votre progression est enregistrée dans le stockage local de votre navigateur et n’est
    transmise nulle part.</p>

    <h2 id="sources">Sources principales</h2>
    <ul class="source-list">
      <li><a href="https://www.nbb.be/fr/publications-et-recherche/publications/publications-economiques-et-financieres/projections" rel="noopener nofollow" target="_blank">Projections macroéconomiques — Banque nationale de Belgique</a></li>
      <li><a href="https://www.plan.be/" rel="noopener nofollow" target="_blank">Bureau fédéral du Plan</a></li>
      <li><a href="https://www.crisp.be/" rel="noopener nofollow" target="_blank">CRISP — Centre de recherche et d’information socio-politiques</a></li>
      <li><a href="https://uclouvain.be/fr/instituts-recherche/ispole" rel="noopener nofollow" target="_blank">ISPOLE — Institut de sciences politiques Louvain-Europe</a></li>
      <li><a href="https://www.senate.be/doc/const_fr.html" rel="noopener nofollow" target="_blank">Constitution belge — Sénat</a></li>
      <li><a href="https://elections.fgov.be/" rel="noopener nofollow" target="_blank">Élections — SPF Intérieur</a></li>
      <li><a href="https://news.belgium.be/fr" rel="noopener nofollow" target="_blank">Communications officielles du gouvernement fédéral</a></li>
      <li><a href="https://www.uvcw.be/" rel="noopener nofollow" target="_blank">Union des Villes et Communes de Wallonie</a></li>
      <li><a href="https://brulocalis.brussels/" rel="noopener nofollow" target="_blank">Brulocalis — Association Ville et Communes de Bruxelles</a></li>
      <li>Presse : RTBF, La Libre, Le Soir, L’Avenir, BX1, VRT NWS, Le Vif, Trends.</li>
    </ul>
    <p>Les sources spécifiques à chaque affirmation sont listées en bas des chapitres et des dossiers concernés.</p>

    <h2 id="corriger">Signaler une erreur</h2>
    <p>Une date fausse, un chiffre périmé, un codage de parti contestable : les corrections sont bienvenues et
    se font publiquement, via le dépôt du projet sur
    <a href="https://github.com/ouaisfieu/anticipation" rel="noopener nofollow" target="_blank">GitHub</a>.
    Merci d’indiquer la page, l’affirmation en cause et la source qui la contredit.</p>
  </article>
  <aside class="side"><nav aria-label="Sommaire"><p class="kicker" style="margin-bottom:.6rem">Sur cette page</p>
  <ol><li><a href="#projet">Le projet</a></li><li><a href="#fiction">Faits et fiction</a></li>
  <li><a href="#methode">La méthode de la boussole</a></li><li><a href="#donnees">Les données</a></li>
  <li><a href="#equilibre">Équilibre et parti pris</a></li><li><a href="#technique">Comment c’est fait</a></li>
  <li><a href="#sources">Sources</a></li><li><a href="#corriger">Signaler une erreur</a></li></ol></nav></aside>
</div>
"""
    write(outdir, "a-propos/", page(
        "a-propos/", "À propos : méthode, sources et limites",
        "Comment Anticipation est fabriqué : séparation stricte entre faits sourcés et fiction, méthode de codage de la boussole électorale, données chiffrées, parti pris assumés et signalement d’erreurs.",
        apropos, depth=1, trail=[("a-propos/","À propos")], nav_key="a-propos/",
        keywords=["méthode","sources","transparence","test électoral","éducation civique"]))

    err = """
<div class="wrap">
  <div class="page-head">
    <p class="kicker">Erreur 404</p>
    <h1>Cette page n’a pas été formée</h1>
    <p class="lede">Comme certaines coalitions. L’adresse demandée n’existe pas, ou plus.</p>
  </div>
</div>
<div class="wrap">
  <div class="prose">
    <h2>Où aller</h2>
    <div class="grid grid-2">
      <a class="card" href="/anticipation/"><h3>L’accueil</h3><p>L’état des lieux d’août 2026 et les trois entrées du site.</p></a>
      <a class="card" href="/anticipation/jeu/"><h3>Le parcours narratif</h3><p>Sept chapitres, de septembre 2026 au scrutin.</p></a>
      <a class="card" href="/anticipation/boussole/"><h3>La boussole</h3><p>Vingt-quatre propositions pour situer vos positions.</p></a>
      <a class="card" href="/anticipation/glossaire/"><h3>Le glossaire</h3><p>Trente termes de la politique belge, expliqués.</p></a>
    </div>
  </div>
</div>
"""
    write(outdir, "404.html", page(
        "404.html", "Page introuvable", "La page demandée n’existe pas. Retournez à l’accueil, au parcours narratif ou à la boussole électorale.",
        err, depth=0, trail=None, nav_key="", noindex=True))
