# -*- coding: utf-8 -*-
from layout import page, write, e, BASE
import unicodedata, re

TERMES = [
("Affaires courantes","affaires-courantes","Régime dans lequel opère un gouvernement démissionnaire : il exécute, paie et représente l’État, mais n’engage pas de politique nouvelle. La doctrine s’est élargie à chaque crise. Record belge : 541 jours en 2010-2011."),
("Anders","anders","Nouveau nom du parti libéral flamand Open Vld, adopté le 19 janvier 2026. « Anders » signifie « autrement » en néerlandais."),
("Arizona (coalition)","arizona","Coalition fédérale formée en 2025 par la N-VA, le MR, Les Engagés, Vooruit et le CD&V, dirigée par Bart De Wever. Le nom vient des couleurs des partis, qui évoquent le drapeau de l’État américain."),
("Bureau fédéral du Plan","bureau-federal-du-plan","Organisme public indépendant d’analyse économique. Depuis 2014, il chiffre les programmes électoraux des partis à leur demande — un exercice qui prend plusieurs mois et structure le débat économique belge."),
("Cabinet ministériel","cabinet-ministeriel","Équipe de conseillers politiques et techniques entourant un ministre, distincte de l’administration. La Belgique en fait un usage particulièrement intensif, ce qui déplace une partie de la décision hors des services publics."),
("Comité de monitoring","comite-de-monitoring","Organe interadministratif qui évalue chaque année la trajectoire budgétaire fédérale, sans tenir compte des intentions politiques. Ses estimations servent de référence commune aux négociations."),
("Conclave budgétaire","conclave-budgetaire","Négociation gouvernementale à huis clos, généralement de plusieurs jours, consacrée à l’arbitrage du budget. En Belgique, il se tient traditionnellement à l’automne, avant l’état de l’Union."),
("Cordon sanitaire","cordon-sanitaire","Engagement des partis démocratiques francophones, pris après le « dimanche noir » de novembre 1991, de ne conclure aucun accord de gouvernement avec l’extrême droite. Il se double d’une règle médiatique interdisant le direct sur le service public francophone."),
("CPAS","cpas","Centre public d’action sociale : institution communale chargée de l’aide sociale, notamment du revenu d’intégration. C’est l’échelon qui absorbe les personnes exclues de l’assurance chômage fédérale."),
("D’Hondt (méthode)","dhondt","Système de répartition proportionnelle des sièges utilisé en Belgique. Il favorise légèrement les listes les plus fortes et rend le « vote utile » moins déterminant que dans un scrutin majoritaire."),
("Déclaration de politique régionale","dpr","Document programmatique d’un gouvernement régional en début de législature. La DPR wallonne de 2024 porte le slogan « Avoir le courage de changer pour que l’avenir s’éclaire »."),
("Déclaration de révision de la Constitution","declaration-de-revision","Acte par lequel les Chambres listent les articles constitutionnels ouverts à révision. Son adoption entraîne la dissolution de plein droit — mais à la fin de la législature, pas immédiatement."),
("Dissolution des Chambres","dissolution","Fin anticipée de la législature, encadrée par l’article 46 de la Constitution. Trois conditions permettent une dissolution rapide ; les élections doivent alors se tenir dans les quarante jours."),
("État de l’Union","etat-de-lunion","Déclaration de politique générale que le Premier ministre prononce devant la Chambre, traditionnellement en octobre. Elle suit le conclave budgétaire et en présente les arbitrages."),
("Fédération Wallonie-Bruxelles","fwb","Entité fédérée compétente pour l’enseignement, la culture et l’aide à la jeunesse des francophones de Wallonie et de Bruxelles. Ses finances sont structurellement tendues ; sa notation a été dégradée par Moody’s de A2 à A3."),
("Flexi-job","flexi-job","Statut d’emploi à charges sociales réduites, initialement réservé à l’horeca et étendu par la coalition Arizona à l’ensemble des secteurs."),
("Formateur, informateur, préformateur","formateur","Personnalités successivement chargées par le Roi d’explorer, puis de préparer, puis de constituer une coalition. Le vocabulaire n’a aucune base constitutionnelle : c’est une coutume."),
("Groupe linguistique","groupe-linguistique","Division des assemblées belges entre élus francophones et néerlandophones. Certaines décisions exigent une majorité dans chaque groupe — mécanisme au cœur de la difficulté de former un gouvernement bruxellois."),
("Indexation automatique","indexation","Mécanisme belge d’ajustement des salaires et allocations à l’inflation. La coalition Arizona l’a plafonné pour 2026 et 2028 : indexation intégrale sous 4 000 € bruts, en montant fixe au-delà."),
("Kern","kern","Conseil des ministres restreint, réunissant le Premier ministre et les vice-Premiers. C’est l’organe où se prennent en pratique la plupart des arbitrages, ce qui interroge le rôle du Conseil des ministres plénier."),
("Loi-programme","loi-programme","Loi fourre-tout adoptée en fin d’année pour traduire juridiquement les décisions budgétaires. Sa densité et sa vitesse d’adoption limitent le contrôle parlementaire."),
("Motion de méfiance constructive","motion-de-mefiance","Motion qui renverse le gouvernement en désignant simultanément un successeur. Parce qu’elle propose une alternative, elle n’ouvre pas la voie à la dissolution — contrairement à une motion de méfiance simple."),
("ONEM","onem","Office national de l’emploi : institution fédérale qui gère l’assurance chômage. La limitation des allocations à 24 mois transfère une partie de sa charge vers les CPAS communaux."),
("Périodes assimilées","periodes-assimilees","Périodes non travaillées (chômage, maladie, prépension, congé parental) historiquement prises en compte dans le calcul de la carrière. Leur réduction est le cœur technique de la réforme des pensions."),
("PIIS","piis","Projet individualisé d’intégration sociale : contrat entre un bénéficiaire du revenu d’intégration et son CPAS. Des subventions fédérales de personnel sont conditionnées à sa signature par une part élevée des bénéficiaires."),
("Procédure pour déficit excessif","pde","Procédure européenne ouverte à l’encontre d’un État dont le déficit dépasse durablement 3 % du PIB. La Belgique y est soumise depuis l’été 2024."),
("Revenu d’intégration sociale (RIS)","ris","Allocation versée par les CPAS aux personnes sans ressources suffisantes. Environ 1 314 € par mois pour une personne isolée — un montant situé sous le seuil de risque de pauvreté."),
("Seuil électoral","seuil-electoral","Pourcentage minimal de voix — 5 % par circonscription en Belgique — nécessaire pour participer à la répartition des sièges."),
("Trajet de réintégration (ReAT)","reat","Dispositif obligeant employeurs, mutualités et médecins du travail à évaluer précocement la capacité de travail des personnes en incapacité de longue durée, en vue d’un retour à l’emploi adapté."),
("Vote obligatoire","vote-obligatoire","Obligation de se présenter au bureau de vote, maintenue en Belgique pour les scrutins fédéral, régional et européen. La Flandre l’a supprimée pour ses élections communales à partir de 2024."),
]

def build(outdir):
    letters = sorted({strip(t[0])[0].upper() for t in TERMES})
    az = "".join(f'<li><a href="#{l.lower()}">{l}</a></li>' for l in letters)
    seen = set()
    out = []
    for nom, slug, d in sorted(TERMES, key=lambda x: strip(x[0])):
        first = strip(nom)[0].upper()
        anchor = (f'<span id="{first.lower()}" class="visually-hidden">{first}</span>'
                  if first not in seen else "")
        seen.add(first)
        out.append(f'<dt id="{slug}">{anchor}{e(nom)}</dt><dd>{e(d)}</dd>')
    body = f"""
<div class="wrap">
  <div class="page-head">
    <p class="kicker">Repères · vocabulaire</p>
    <h1>Glossaire institutionnel belge</h1>
    <p class="lede">Trente termes qui reviennent dans chaque article de politique belge et que personne
    n’explique jamais. Définitions courtes, sans jargon.</p>
  </div>
</div>
<div class="wrap layout-side">
  <article class="prose">
    <ul class="az" aria-label="Navigation alphabétique">{az}</ul>
    <dl class="glossary">{"".join(out)}</dl>
    <div class="btnrow">
      <a class="btn" href="../dossiers/elections-anticipees-mode-demploi/">Élections anticipées : mode d’emploi</a>
      <a class="btn ghost" href="../jeu/">Jouer le parcours</a>
    </div>
  </article>
  <aside class="side"><nav aria-label="Sommaire"><p class="kicker" style="margin-bottom:.6rem">Aller à</p>
  <ol>{"".join(f'<li><a href="#{l.lower()}">{l}</a></li>' for l in letters)}</ol></nav></aside>
</div>
"""
    ld = {"@context":"https://schema.org","@type":"DefinedTermSet","name":"Glossaire institutionnel belge",
          "url": BASE+"glossaire/","inLanguage":"fr-BE",
          "hasDefinedTerm":[{"@type":"DefinedTerm","name":n,"description":d,"url":BASE+"glossaire/#"+s}
                            for n,s,d in TERMES]}
    write(outdir, "glossaire/", page(
        "glossaire/", "Glossaire institutionnel belge : 30 termes expliqués",
        "Affaires courantes, Kern, conclave, cordon sanitaire, CPAS, méthode D’Hondt, périodes assimilées, article 46 : le vocabulaire de la politique belge expliqué simplement.",
        body, depth=1, trail=[("glossaire/","Glossaire")], nav_key="glossaire/", extra_ld=[ld],
        keywords=["glossaire politique belge","affaires courantes","Kern","cordon sanitaire","méthode D’Hondt","CPAS"]))

def strip(s):
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
