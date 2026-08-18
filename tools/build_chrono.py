# -*- coding: utf-8 -*-
from layout import page, write, e, BASE

EVENTS = [
 ("2024-06-09","9 juin 2024","Le méga-scrutin", True,
  "Élections fédérales, régionales et européennes le même jour. Le MR devient le premier parti francophone (10,26 %, 20 sièges à la Chambre), Les Engagés triplent presque leur représentation (14 sièges), Ecolo s’effondre (3 sièges contre 13), le PTB-PVDA atteint 15 sièges. En Flandre, la N-VA reste en tête (24 sièges) devant le Vlaams Belang (20)."),
 ("2024-07","Été 2024","La Belgique sous procédure européenne", False,
  "La Commission européenne ouvre une procédure pour déficit excessif à l’encontre de la Belgique. La trajectoire budgétaire devient une contrainte juridique, plus seulement politique."),
 ("2024-07","Juillet 2024","Nouvelles directions", False,
  "Sophie Rohonyi prend la présidence de DéFI. Chez Ecolo, Samuel Cogolati et Marie Lecocq succèdent à Jean-Marc Nollet et Rajae Maouane."),
 ("2024-09","Septembre 2024","Wallonie et FWB : la coalition MR–Les Engagés", True,
  "Déclarations de politique régionale et communautaire sous le slogan « Avoir le courage de changer ». Réduction des droits d’enregistrement à 3 %, fin du Pacte d’excellence, recentrage du Forem sur l’activation."),
 ("2025-02","Février 2025","Le gouvernement De Wever entre en fonction", True,
  "La coalition Arizona (N-VA, MR, Les Engagés, Vooruit, CD&V) se met en place autour de la « supernota ». Le programme : limitation du chômage dans le temps, flexibilisation du travail, durcissement des pensions, écart de 500 € entre travail et allocations."),
 ("2025-01","1er janvier 2025","Droits d’enregistrement wallons à 3 %", False,
  "L’achat d’une habitation propre et unique passe de 12,5 % à 3 %, avec suppression du chèque-habitat. Les droits de succession en ligne directe sont divisés par deux."),
 ("2025-07-21","21 juillet 2025","L’accord de l’été", True,
  "Après une nuit de négociations : réforme des pensions avec malus, annualisation et flexibilisation du travail, plan de réintégration des malades de longue durée, aide aux CPAS, taxation des plus-values."),
 ("2025-11-24","24 novembre 2025","L’accord budgétaire", True,
  "2,15 milliards pour 2026, 9,2 milliards à plein régime en 2029. TVA à 12 % sur l’hôtellerie, le sport et les repas à emporter ; taxe comptes-titres doublée à 0,30 % ; indexation plafonnée au-dessus de 4 000 € bruts ; taxe de 2 € par colis hors UE ; 377 inspecteurs anti-fraude."),
 ("2025-11","Novembre 2025","Ecolo sans direction", False,
  "Samuel Cogolati et Marie Lecocq démissionnent de la coprésidence, faute d’accord sur le rythme de la refondation du parti."),
 ("2026-01-01","1er janvier 2026","Taxe sur les plus-values", True,
  "Entrée en vigueur de la taxe de 10 % sur les plus-values financières (actions, crypto-actifs), première du genre en Belgique. Les exemptions accordées aux sociétés patrimoniales sont immédiatement contestées."),
 ("2026-01-19","19 janvier 2026","L’Open Vld devient Anders", False,
  "Le parti libéral flamand abandonne le nom qu’il portait depuis sa fondation. « Assez des petits rêves », annonce la direction."),
 ("2026-02-14","14 février 2026","Bruxelles a un gouvernement", True,
  "Après près de six cents jours de blocage, le gouvernement Boris Dilliès (MR) prête serment. Sept formations : MR, PS, Les Engagés, Groen, Vooruit, Anders, avec le CD&V en soutien. Le Parlement lui accorde sa confiance le 27 février."),
 ("2026-03-01","1er mars 2026","Le chômage limité à deux ans", True,
  "Mise en œuvre progressive de la limitation des allocations à 24 mois. Environ 100 000 personnes basculent vers les CPAS, avec une prise en charge fédérale du revenu d’intégration de 100 % en 2026, ramenée à 75 % en 2029."),
 ("2026-03-13","13 mars 2026","Le baromètre qui rebat les cartes", True,
  "Grand Baromètre Ipsos : le PS repasse en tête en Wallonie (27,9 %), le PTB devient la première force à Bruxelles (25,5 %), le MR y chute à 16,4 %. En Flandre, N-VA et Vlaams Belang sont à un dixième de point l’un de l’autre."),
 ("2026-03","Mars 2026","Ecolo se redonne une direction", False,
  "Marie-Colline Leroy et Gilles Vanden Burre sont élus à la coprésidence, sur une ligne d’« écologie populaire »."),
 ("2026-03-26","26 mars 2026","Premières coupes bruxelloises", False,
  "Le gouvernement Dilliès engage des économies régionales. Chez visit.brussels, les syndicats annoncent qu’un emploi sur deux est menacé."),
 ("2026-06","Juin 2026","Bruxelles confirme le basculement", False,
  "Nouvelle vague du Grand Baromètre : à Bruxelles, le PTB atteint 24,8 %, le PS 18,3 %, le MR tombe à 13,9 % — contre environ 26 % obtenus en juin 2024."),
 ("2026-07-10","10 juillet 2026","Dix milliards d’ici 2029", True,
  "Le gouvernement annonce viser un effort budgétaire de 10 milliards d’euros d’ici 2029, au-delà du minimum estimé par les administrations. Conclave fin septembre, état de l’Union en octobre. La répartition entre économies et recettes n’est pas tranchée."),
 ("2026-07-25","25 juillet 2026","L’accord d’été, version 2026", False,
  "Annualisation du temps de travail, interdiction d’importation de produits issus des colonies israéliennes, décisions périphériques. La chercheuse Caroline Sägesser (CRISP) relève que les décisions se concentrent en Kern, le Conseil des ministres devenant « une chambre d’entérinement »."),
 ("2026-08-14","14-17 août 2026","L’incendie des Hautes Fagnes", True,
  "Le plus important incendie de forêt de l’histoire belge ravage les Hautes Fagnes : environ 3 000 hectares, des évacuations, une coordination fédérale et régionale improvisée en pleine trêve estivale. Le monde politique reste, pour l’essentiel, en retrait."),
 ("2026-09","Septembre 2026","Le conclave", False,
  "À venir : l’arbitrage entre économies et recettes, reporté depuis juillet. C’est le point de départ du parcours narratif de ce site."),
 ("2026-10","Octobre 2026","L’état de l’Union", False,
  "À venir : la déclaration de politique générale du Premier ministre devant la Chambre, échéance à laquelle le paquet budgétaire doit être bouclé."),
 ("2029","2029","Le scrutin ordinaire", False,
  "Sauf dissolution anticipée, les prochaines élections fédérales, régionales et européennes se tiennent la même année, comme depuis 2014."),
]

def build(outdir):
    items = "".join(
        f'<li class="{"key" if key else ""}"><span class="when"><time datetime="{dt}">{e(lab)}</time></span>'
        f'<h3>{e(t)}</h3><p>{e(d)}</p></li>' for dt, lab, t, key, d in EVENTS)
    body = f"""
<div class="wrap">
  <div class="page-head">
    <p class="kicker">Repères · juin 2024 → août 2026</p>
    <h1>Chronologie d’une législature sous tension</h1>
    <p class="lede">Vingt-trois étapes, du méga-scrutin de juin 2024 au conclave budgétaire de l’automne 2026.
    Les jalons décisifs sont marqués d’un point doré.</p>
  </div>
</div>
<div class="wrap layout-side">
  <article class="prose">
    <p>Une législature belge se lit rarement dans les discours. Elle se lit dans l’enchaînement des dates :
    un scrutin, une procédure européenne, deux accords de gouvernement, un accord d’été, un accord budgétaire,
    une entrée en vigueur — et l’écart, chaque fois, entre ce qui est annoncé et ce qui est déposé au Parlement.</p>
    <ol class="timeline">{items}</ol>
    <div class="btnrow">
      <a class="btn" href="../jeu/">Jouer la suite</a>
      <a class="btn ghost" href="../dossiers/">Les dossiers de fond</a>
      <a class="btn ghost" href="../sondages/">Les sondages</a>
    </div>
  </article>
  <aside class="side"><nav aria-label="Repères"><p class="kicker" style="margin-bottom:.6rem">Années</p>
  <ol><li><a href="#contenu">2024 — le scrutin</a></li><li><a href="#contenu">2025 — les accords</a></li>
  <li><a href="#contenu">2026 — l’application</a></li></ol></nav></aside>
</div>
"""
    ld = {"@context":"https://schema.org","@type":"ItemList","name":"Chronologie politique belge 2024-2026",
          "numberOfItems":len(EVENTS),
          "itemListElement":[{"@type":"ListItem","position":i+1,"name":t} for i,(_,_,t,_,_) in enumerate(EVENTS)]}
    write(outdir, "chronologie/", page(
        "chronologie/", "Chronologie de la politique belge, 2024-2026",
        "De juin 2024 au conclave de l’automne 2026 : scrutin, coalitions Arizona et MR–Les Engagés, accords budgétaires, limitation du chômage, crise bruxelloise. Vingt-trois dates clés.",
        body, depth=1, trail=[("chronologie/","Chronologie")], nav_key="chronologie/", extra_ld=[ld],
        keywords=["chronologie politique belge","élections 2024","gouvernement De Wever","accord budgétaire 2025","crise bruxelloise"]))
