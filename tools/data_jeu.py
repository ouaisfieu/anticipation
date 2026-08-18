# -*- coding: utf-8 -*-
"""Contenu du parcours narratif « Le compte à rebours ».

Chaque chapitre : un encadré factuel sourcé, une scène de fiction clairement
étiquetée, puis trois ou quatre décisions dont les conséquences sont écrites
en clair dans le HTML (donc lisibles sans JavaScript et indexables)."""

CHAPTERS = [
{
 "id": "ch1", "n": 1, "slug": "01-le-comite-de-monitoring",
 "titre": "Le Comité de monitoring",
 "date": "4 septembre 2026",
 "lieu": "Rue de la Loi, Bruxelles",
 "meta_title": "Chapitre 1 — Le Comité de monitoring | Le compte à rebours",
 "meta_desc": "Septembre 2026 : le rapport budgétaire qui ouvre la saison politique. Dix milliards à trouver d’ici 2029, un écart de 6,7 milliards, et une première décision à prendre.",
 "kw": ["comité de monitoring", "budget fédéral 2027", "déficit belge", "procédure de déficit excessif", "Arizona"],
 "fait": """<p>Le <strong>Comité de monitoring</strong> est l’organe interadministratif qui évalue chaque année
la trajectoire budgétaire fédérale : il chiffre l’écart entre les recettes attendues et les dépenses engagées, sans
tenir compte des intentions politiques. Ses estimations 2026 tournent autour d’un besoin d’assainissement de
<strong>6,7 à 7,7 milliards d’euros</strong> pour respecter la trajectoire européenne.</p>
<p>Le 10 juillet 2026, le gouvernement De Wever est allé plus loin en s’engageant sur un effort de
<strong>10 milliards d’euros d’ici 2029</strong>, avec un conclave fixé à <strong>fin septembre</strong> et un
état de l’Union en <strong>octobre 2026</strong>. Le déficit public belge s’établit autour de
<strong>5,2 % du PIB</strong>, la dette approche <strong>115 %</strong>, et le pays est sous
<strong>procédure pour déficit excessif</strong> depuis l’été 2024.</p>""",
 "scene": """<p>Vous avez vingt-neuf ans, un diplôme en sciences politiques, deux ans d’administration fédérale et
un badge qui ouvre plus de portes que prévu. Depuis mars, vous êtes détaché·e comme rapporteur adjoint auprès du
Comité de monitoring — un poste dont personne ne parle onze mois par an, et dont tout le monde parle en septembre.</p>
<p>Le tableur est ouvert devant vous depuis six heures du matin. Il y a un problème, et il est petit : l’hypothèse
retenue pour la croissance des dépenses de soins de santé. Prenez la norme légale, l’écart tient dans une note de bas
de page. Prenez la tendance observée des trois dernières années, et il s’ouvre de <strong>1,4 milliard</strong>
supplémentaire — soit, à peu près, l’économie que le conclave de fin septembre est censé dégager sur ce poste.</p>
<p>Votre chef de service repose sa tasse. « Le cabinet du Premier veut le rapport lundi. Vous le présentez comment ? »</p>""",
 "choix": [
  {"id":"c1a","eff":"cred:+9,stab:-4,tension:+2",
   "t":"Publier le chiffre brut","s":"La tendance observée, sans lissage, avec l’écart de 1,4 milliard en première page.",
   "c":"""<p>Le rapport sort avec le chiffre le plus élevé. En deux heures, il est sur trois plateaux télévisés,
et l’opposition en fait le titre de sa rentrée. Le Comité de monitoring y gagne ce qu’un organe technique a de plus
rare : la certitude, pour tout le monde, qu’il ne négocie pas ses hypothèses.</p>
<p>Le cabinet du Premier, lui, doit ouvrir son conclave avec un trou plus large que celui qu’il avait annoncé en
juillet. La conférence de presse de rentrée est reportée de trois jours.</p>"""},
  {"id":"c1b","eff":"cred:-7,stab:+5,tension:-1",
   "t":"Retenir l’hypothèse la plus favorable","s":"La norme légale de croissance, l’écart signalé en note de bas de page.",
   "c":"""<p>Le rapport est techniquement défendable : la norme légale <em>est</em> une hypothèse légitime.
Il est aussi, tout le monde le sait, le seul scénario qui permet au conclave de commencer sans crise.</p>
<p>Personne ne vous reproche rien. Six mois plus tard, au contrôle budgétaire de mars, l’écart réapparaît —
augmenté des intérêts. Un journaliste retrouve la note de bas de page et écrit un papier sur « l’art belge de
reporter les mauvaises nouvelles ». Le Comité met deux ans à récupérer son autorité.</p>"""},
  {"id":"c1c","eff":"cred:+6,stab:+1,tension:0",
   "t":"Publier deux scénarios","s":"Fourchette basse et fourchette haute, avec l’explication de l’écart et de ce qui le déterminera.",
   "c":"""<p>C’est la solution la moins spectaculaire et la plus utilisée : une fourchette, un encadré méthodologique,
et la responsabilité du choix renvoyée au politique — ce qui est, formellement, sa place.</p>
<p>Le conclave s’ouvre avec deux chiffres. Chaque parti choisit le sien. Mais l’encadré méthodologique, lui, devient
la référence citée dans tous les débats de l’automne : pour la première fois, l’écart n’est plus une affaire
d’opinion, c’est une affaire d’hypothèse explicite.</p>"""},
  {"id":"c1d","eff":"cred:+3,soc:+7,stab:-2,tension:+1",
   "t":"Ajouter un chiffrage social","s":"Annexer au rapport l’effet des économies envisagées sur les ménages du premier quintile de revenus.",
   "c":"""<p>Ce n’est pas dans votre mandat. C’est aussi ce qui manque à tous les rapports de ce type :
un budget dit combien on économise, jamais sur qui.</p>
<p>L’annexe fait onze pages. Elle établit qu’à mesures constantes, l’effort porte à 62 % sur les deux quintiles
inférieurs. Les syndicats la citent dès le lendemain ; le cabinet du ministre du Budget demande, sans succès, son
retrait. Vous avez élargi le débat — et perdu, au passage, la réputation de neutralité qui vous protégeait.</p>"""},
 ],
 "sources": [
  ("L’Arizona s’engage à réaliser 10 milliards d’euros d’effort budgétaire pour 2029 — La Libre, 10 juillet 2026","https://www.lalibre.be/belgique/politique-belge/2026/07/10/larizona-sengage-a-realiser-10-milliards-deuros-deffort-budgetaire-pour-2029-G6Y4IT4PDVHCDKARKEUC4233W4/"),
  ("Croissance modérée et déficit persistant : la Belgique reste aux prises avec ses finances publiques — Banque nationale de Belgique","https://www.nbb.be/fr/actualites-et-evenements/actualites/croissance-moderee-et-deficit-persistant-la-belgique-reste-aux"),
  ("Procédure de déficit excessif : la Belgique obtient un sursis, pas une absolution — Trends/Le Vif","https://trends.levif.be/a-la-une/politique-economique/procedure-de-deficit-excessif-la-belgique-obtient-un-sursis-pas-une-absolution/"),
 ],
},
{
 "id": "ch2", "n": 2, "slug": "02-le-conclave",
 "titre": "Le conclave",
 "date": "28 septembre 2026",
 "lieu": "Résidence du Premier ministre, rue de la Loi 16",
 "meta_title": "Chapitre 2 — Le conclave budgétaire | Le compte à rebours",
 "meta_desc": "Fin septembre 2026 : dépenses ou recettes ? Le MR refuse tout nouvel impôt, Les Engagés proposent de taxer les patrimoines. Trois notes sur la table, une arbitrage à rendre.",
 "kw": ["conclave budgétaire", "kern", "MR impôts", "Les Engagés patrimoine", "taxe plus-values", "indexation salaires"],
 "fait": """<p>L’accord budgétaire de novembre 2025 avait déjà mobilisé la fiscalité indirecte : passage à
<strong>12 % de TVA</strong> pour l’hôtellerie, le camping, le sport et les repas à emporter, doublement de la
<strong>taxe sur les comptes-titres</strong> (0,15 % → 0,30 %), <strong>150 millions par an</strong> de taxe
bancaire, <strong>2 € par colis</strong> importé hors UE, et une <strong>indexation plafonnée</strong> pour les
salaires bruts au-dessus de 4 000 € (en 2026 et 2028). S’y ajoute une taxe de <strong>10 % sur les plus-values
financières</strong> entrée en vigueur au 1<sup>er</sup> janvier 2026.</p>
<p>À l’été 2026, les lignes rouges sont publiques : le <strong>MR</strong> refuse tout nouvel impôt ;
<strong>Les Engagés</strong> proposent de faire contribuer les patrimoines au-delà de
<strong>500 000 €</strong>. La chercheuse du CRISP Caroline Sägesser relève par ailleurs que les décisions
se prennent de plus en plus <strong>en Kern</strong>, entre vice-Premiers, le Conseil des ministres devenant
« une chambre d’entérinement ».</p>""",
 "scene": """<p>Le conclave dure depuis quarante et une heures. Vous n’êtes pas dans la salle — personne de votre rang
ne l’est — mais dans la pièce d’à côté, celle où les cabinets envoient chiffrer les propositions en temps réel.
Trois notes tournent depuis minuit.</p>
<p>La première fait porter la totalité de l’effort sur les dépenses : santé, fonction publique, allocations.
La deuxième ajoute une contribution sur les patrimoines élevés, hors résidence principale et outil professionnel.
La troisième est un compromis à 60/40 assorti d’une clause de rendez-vous en mars.</p>
<p>Le chef de cabinet adjoint pose la main sur votre écran. « On a besoin d’une note d’une page pour le Premier.
Laquelle tient debout ? »</p>""",
 "choix": [
  {"id":"c2a","eff":"cred:+2,soc:-9,stab:+2,tension:+1",
   "t":"Tout en dépenses","s":"L’option qui respecte les lignes rouges fiscales et ferme le débat en une nuit.",
   "c":"""<p>Arithmétiquement, elle boucle. Elle est aussi la plus rapide : aucune loi fiscale nouvelle, donc aucun
avis du Conseil d’État à attendre, donc un vote avant décembre.</p>
<p>Le coût est ailleurs. Les fédérations de services sociaux et les mutualités chiffrent l’impact sur les ménages
précaires ; le front commun syndical dépose un préavis dans la foulée. Vous avez acheté de la stabilité
gouvernementale avec du conflit social — un échange que la Belgique a déjà pratiqué, et rarement gagné longtemps.</p>"""},
  {"id":"c2b","eff":"cred:+2,soc:+7,stab:-4,tension:+2",
   "t":"Faire contribuer les patrimoines","s":"La note des Engagés : contribution au-delà de 500 000 €, hors résidence principale.",
   "c":"""<p>Sur le papier, l’équilibre est meilleur : l’effort se répartit, et la mesure répond à la critique
récurrente selon laquelle les paquets 2025-2026 ont surtout mobilisé la fiscalité indirecte, qui pèse
proportionnellement plus sur les bas revenus.</p>
<p>Politiquement, elle heurte de front la ligne rouge du MR. Le conclave gagne trois jours et se termine par un
communiqué qui parle de « poursuite des travaux ». Deux partenaires sortent en expliquant publiquement que
l’accord n’est pas ce qu’ils ont signé.</p>"""},
  {"id":"c2c","eff":"cred:-3,stab:+6,tension:-1",
   "t":"Le compromis 60/40","s":"Soixante pour cent en dépenses, quarante en recettes, avec clause de rendez-vous en mars.",
   "c":"""<p>C’est la sortie belge classique, et elle fonctionne : chacun peut annoncer avoir tenu sa ligne, et la
partie difficile est renvoyée au contrôle budgétaire de mars.</p>
<p>Le problème est connu de tous ceux qui l’écrivent : une clause de rendez-vous n’est pas une mesure, c’est une
promesse de mesure. Le Comité de monitoring la comptabilisera comme telle, et la Commission européenne aussi.
L’effort réel de l’année est inférieur d’environ un tiers à l’effort annoncé.</p>"""},
  {"id":"c2d","eff":"cred:-7,soc:+1,stab:+3,tension:+2",
   "t":"Reporter au contrôle budgétaire","s":"Boucler l’essentiel maintenant, tout arbitrer en mars.",
   "c":"""<p>Le conclave se termine à l’heure, l’état de l’Union d’octobre est sauvé, et le Premier peut annoncer
un « cap tenu ».</p>
<p>Mais le report devient la méthode. Chaque échéance repoussée alourdit la suivante d’une charge d’intérêts
et d’un degré de défiance : à mars, l’écart n’est plus de 1,4 milliard mais de 2,1, et l’argument
« nous avons tenu le cap » ne convainc plus personne autour de la table.</p>"""},
 ],
 "sources": [
  ("TVA, indexation des salaires, épaules les plus larges : l’accord budgétaire du gouvernement De Wever — RTBF, novembre 2025","https://www.rtbf.be/article/tva-indexation-des-salaires-epaules-les-plus-larges-voici-l-accord-budgetaire-du-gouvernement-de-wever-11636589"),
  ("« Une tendance inquiétante s’est renforcée sous le gouvernement De Wever » — La Libre, 25 juillet 2026","https://www.lalibre.be/belgique/politique-belge/2026/07/25/cetait-risque-pour-bart-de-wever-de-tenir-une-conference-de-presse-pour-presenter-son-accord-il-craint-certaines-questions-KDU7OIBW2BAUVN32TDHESOHPYM/"),
  ("Le gouvernement fédéral s’accorde sur la taxe sur les plus-values — BX1","https://bx1.be/categories/news/le-gouvernement-federal-saccorde-sur-la-taxe-sur-les-plus-values/"),
 ],
},
{
 "id": "ch3", "n": 3, "slug": "03-la-rue",
 "titre": "La rue et le guichet",
 "date": "17 novembre 2026",
 "lieu": "CPAS de Charleroi",
 "meta_title": "Chapitre 3 — La rue et le guichet | Le compte à rebours",
 "meta_desc": "Novembre 2026 : la limitation des allocations de chômage à deux ans produit ses effets. Environ 100 000 personnes basculent vers les CPAS. Que dit votre rapport ?",
 "kw": ["limitation chômage deux ans", "CPAS", "revenu d’intégration sociale", "exclusion chômage 2026", "front commun syndical"],
 "fait": """<p>Depuis le <strong>1<sup>er</sup> mars 2026</strong>, la limitation des allocations de chômage à
<strong>24 mois</strong> — mesure emblématique de l’accord Arizona — produit ses premiers effets. Les fédérations
de CPAS et l’Observatoire bruxellois estiment que <strong>près de 100 000 personnes</strong> basculent de
l’assurance fédérale (ONEM) vers l’assistance communale.</p>
<p>Un régime compensatoire dégressif a été négocié : l’État fédéral prend en charge <strong>100 %</strong>
du revenu d’intégration sociale des nouveaux exclus en 2026, puis <strong>75 % en 2029</strong>. Le RIS pour une
personne isolée s’élève à environ <strong>1 314 € par mois</strong>, soit un montant situé sous le seuil de risque
de pauvreté. Des subventions de personnel supplémentaires sont conditionnées à la signature de projets
individualisés d’intégration sociale (PIIS) par une part élevée des bénéficiaires.</p>""",
 "scene": """<p>Le hall du CPAS ouvre à huit heures. À sept heures quarante, la file fait le tour du bâtiment.
Vous êtes venu·e « objectiver le basculement » — c’est la formule de la lettre de mission — avec un questionnaire
de onze pages et l’autorisation d’assister à des entretiens.</p>
<p>La travailleuse sociale qui vous accueille a trente-quatre dossiers ouverts ce jour-là. Elle vous montre son
écran : le logiciel n’a pas de champ pour « personne exclue du chômage », alors elle tape la mention dans les
observations libres. « Vous allez écrire quoi, exactement ? »</p>
<p>Deux jours plus tard, le front commun syndical dépose un préavis de grève générale pour décembre.
Votre rapport est attendu pour le 30.</p>""",
 "choix": [
  {"id":"c3a","eff":"cred:+7,soc:+6,stab:-5,tension:+2",
   "t":"Écrire ce que vous avez vu","s":"Les délais réels, les refus, la saturation, sans atténuation ni recommandation.",
   "c":"""<p>Le rapport est factuel et il est dévastateur : délai moyen d’ouverture d’un droit passé de 21 à 47 jours,
un tiers des nouveaux demandeurs sans revenu pendant plus de six semaines, taux d’absentéisme des travailleurs
sociaux en hausse d’un quart.</p>
<p>Un organe fédéral qui documente l’effet d’une mesure fédérale : la presse s’en empare, l’opposition en fait
l’argument central de décembre, et deux partenaires de la coalition demandent, en interne, une « clause de
sauvegarde ». Vous n’avez recommandé rien du tout — c’est justement pourquoi c’est efficace.</p>"""},
  {"id":"c3b","eff":"cred:+2,soc:+8,stab:-1,tension:+1",
   "t":"Recommander une rallonge d’urgence","s":"Proposer de maintenir la prise en charge fédérale à 100 % jusqu’en 2029 et de financer 400 postes.",
   "c":"""<p>La recommandation est chiffrée, bornée, et politiquement acceptable : elle ne remet pas en cause la
réforme, elle en amortit le transfert. Le fédéral finit par lâcher une rallonge partielle, moins ambitieuse que
la vôtre, mais réelle.</p>
<p>C’est le type d’intervention qui ne fait jamais de titre et qui change des situations concrètes.
Elle a aussi un coût : vous avez accepté implicitement le cadre de la réforme, et vous devrez vivre avec
l’argument selon lequel une rallonge suffit à traiter un problème structurel.</p>"""},
  {"id":"c3c","eff":"cred:+1,soc:-6,stab:+4,tension:0",
   "t":"S’en tenir au mandat","s":"Compter les dossiers, remplir les tableaux, ne rien commenter.",
   "c":"""<p>Vous rendez un document irréprochable et sans effet. Les chiffres sont là, personne ne les lit :
un tableau sans phrase ne produit pas d’attention.</p>
<p>Le gouvernement traverse décembre sans encombre. Les CPAS, eux, absorbent la vague avec leurs propres moyens —
c’est-à-dire en allongeant les délais. Le coût n’a pas disparu, il a changé d’adresse et cessé d’être visible.</p>"""},
  {"id":"c3d","eff":"cred:-2,soc:+9,stab:-6,tension:+2",
   "t":"Proposer un moratoire","s":"Recommander la suspension d’un an des exclusions, le temps d’évaluer.",
   "c":"""<p>Sur le fond, l’argument est solide : on ne dispose d’aucune évaluation d’impact indépendante d’une
réforme qui déplace 100 000 personnes d’un système à un autre.</p>
<p>Sur la forme, un fonctionnaire qui recommande de suspendre une mesure votée sort de son rôle, et tout le monde
le lui dit. La proposition devient un objet politique : reprise telle quelle par l’opposition, elle est disqualifiée
par la majorité comme militante. Le débat sur l’évaluation, lui, est enterré pour un an.</p>"""},
 ],
 "sources": [
  ("Limitation à deux ans des allocations de chômage : le devenir possible des exclus et effets sur les CPAS — Brulocalis / Observatoire de la Santé et du Social","https://brulocalis.brussels/sites/default/files/2025-05/Vivalis_Limitation%20%C3%A0%20deux%20ans%20des%20alloc_f%C3%A9d%C3%A9rations%20des%20cpas_OBSS.pdf"),
  ("Régime compensatoire des CPAS à la suite de la limitation dans le temps des allocations de chômage — belgium.be","https://news.belgium.be/fr/regime-compensatoire-des-cpas-la-suite-de-la-limitation-dans-le-temps-des-allocations-de-chomage"),
  ("Réforme du chômage : le point sur les compensations octroyées aux CPAS — Union des Villes et Communes de Wallonie","https://www.uvcw.be/insertion/actus/art-9826"),
 ],
},
]

CHAPTERS += [
{
 "id": "ch4", "n": 4, "slug": "04-la-rupture",
 "titre": "La rupture",
 "date": "19 mars 2027",
 "lieu": "Chambre des représentants, Palais de la Nation",
 "meta_title": "Chapitre 4 — La rupture | Le compte à rebours",
 "meta_desc": "Mars 2027 : le contrôle budgétaire fait remonter l’écart. Un partenaire menace de partir. Comment un gouvernement fédéral belge se casse — et ce que cela déclenche vraiment.",
 "kw": ["coalition Arizona", "crise gouvernementale", "contrôle budgétaire", "question de confiance", "N-VA Vooruit"],
 "fait": """<p>La coalition <strong>Arizona</strong> réunit la <strong>N-VA</strong>, le <strong>MR</strong>,
<strong>Les Engagés</strong>, <strong>Vooruit</strong> et le <strong>CD&amp;V</strong>. Elle repose sur un
équilibre fragile : la N-VA doit tenir sa droite face à un Vlaams Belang crédité de 25 à 27 % en Flandre, tandis que
Vooruit doit défendre un bilan social devant un électorat qui voit progresser le PVDA.</p>
<p>Point de mécanique souvent ignoré : <strong>la chute d’un gouvernement fédéral ne déclenche pas
automatiquement des élections</strong>. Le gouvernement remet sa démission au Roi ; celui-ci l’accepte ou la met
« en suspens », et le gouvernement expédie les <strong>affaires courantes</strong> — parfois très longtemps :
541 jours en 2010-2011, un record mondial pour une démocratie. La dissolution obéit à des conditions séparées,
fixées par l’article 46 de la Constitution.</p>""",
 "scene": """<p>Vous avez changé de bureau. Depuis janvier, vous êtes conseiller·ère budgétaire d’un groupe
parlementaire — vous avez gardé les chiffres, vous avez perdu la neutralité, et vous avez gagné le droit d’être
dans la salle.</p>
<p>Le contrôle budgétaire de mars fait ce que tout le monde savait qu’il ferait : l’écart de septembre est revenu,
augmenté. Deux dossiers bloquent en même temps. Le premier est le second plafonnement de l’indexation, prévu pour
2028 : un partenaire annonce qu’il ne le votera pas. Le second est le volet pénibilité de la réforme des pensions,
que la N-VA veut durcir et que le CD&amp;V refuse de rouvrir.</p>
<p>À 23 h 10, le chef de groupe se tourne vers vous. « Si on va au vote demain, on tombe. Vous conseillez quoi ? »</p>""",
 "choix": [
  {"id":"c4a","eff":"stab:+8,cred:-5,soc:+2,tension:-2",
   "t":"Sauver la coalition","s":"Geler la mesure contestée, absorber l’écart par un ajustement technique.",
   "c":"""<p>Le gel passe en une nuit. La coalition tient, l’accord de gouvernement survit, et l’état de la Nation de
2027 pourra parler d’autre chose.</p>
<p>Ce qui a été gelé, en revanche, n’a pas été financé : l’ajustement technique consiste, pour l’essentiel, à
décaler des recettes attendues. Le Comité de monitoring l’écrira noir sur blanc en septembre, et la Commission
européenne aussi. La stabilité a été payée en crédibilité — un taux de change que la Belgique connaît bien.</p>"""},
  {"id":"c4b","eff":"stab:-7,cred:+1,soc:-5,tension:+3",
   "t":"Passer en force","s":"Faire trancher le Kern et imposer le texte au Conseil des ministres et au vote.",
   "c":"""<p>Le texte passe. Le partenaire qui avait annoncé qu’il ne le voterait pas le vote, en expliquant qu’il l’a
« amendé ». Personne n’est dupe, à commencer par sa base.</p>
<p>C’est exactement le mécanisme que décrivait Caroline Sägesser en juillet 2026 : les décisions se prennent en Kern,
le Conseil des ministres entérine, le Parlement enregistre. On gagne des textes et on perd des majorités : à partir
de ce printemps, chaque vote devient une négociation séparée, et la coalition ne gouverne plus, elle survit.</p>"""},
  {"id":"c4c","eff":"stab:+3,cred:+4,soc:+2,tension:0",
   "t":"Élargir la table","s":"Ouvrir une conférence interministérielle avec les Régions sur l’emploi et l’aide sociale.",
   "c":"""<p>Le blocage fédéral porte sur des mesures dont les conséquences sont régionales et communales :
c’est le Forem, Actiris et les CPAS qui reçoivent les personnes que le fédéral n’indemnise plus. Poser la question
au bon niveau est techniquement juste.</p>
<p>C’est aussi lent. La conférence se réunit trois fois avant l’été et produit un protocole non contraignant.
Mais elle crée quelque chose que la législature n’avait pas : un lieu où le fédéral, les Régions et les communes
regardent la même colonne de chiffres. Plusieurs des sorties de crise de l’automne partiront de là.</p>"""},
  {"id":"c4d","eff":"stab:-4,cred:+5,tension:+3",
   "t":"Poser la question de confiance","s":"Clarifier la majorité par un vote, quitte à la perdre.",
   "c":"""<p>C’est l’option la plus honnête et la plus risquée. Un gouvernement qui n’a plus de majorité sur ses
propres textes n’a plus de majorité : le vote le dit à voix haute.</p>
<p>La Constitution prend alors le relais. Si la Chambre refuse la confiance et ne propose pas de successeur au Roi
dans les trois jours, la dissolution devient possible — et les élections doivent avoir lieu dans les quarante jours.
Vous venez de mettre l’article 46 sur la table, et il n’en repartira plus.</p>"""},
 ],
 "sources": [
  ("Constitution belge, article 46 — dissolution des Chambres","https://www.senate.be/doc/const_fr.html"),
  ("613 jours sans gouvernement : retour sur la plus longue crise politique de l’histoire belge — BX1","https://bx1.be/categories/news/613-jours-sans-gouvernement-retour-sur-la-plus-longue-crise-politique-de-lhistoire-belge/"),
  ("Analyse de la supernota De Wever, devenue accord de gouvernement Arizona 2025-2030 — Forum for the Future","https://blog.forumforthefuture.be/fr/article/analyse-de-la-supernota-de-wever-devenue-accord-de-gouvernement-arizona-2025-2030/25886"),
 ],
},
{
 "id": "ch5", "n": 5, "slug": "05-la-dissolution",
 "titre": "La dissolution",
 "date": "11 juin 2027",
 "lieu": "Palais de Bruxelles, antichambre",
 "meta_title": "Chapitre 5 — La dissolution | Le compte à rebours",
 "meta_desc": "Comment déclenche-t-on réellement des élections anticipées en Belgique ? Article 46, motion de méfiance constructive, déclaration de révision : la mécanique expliquée par la fiction.",
 "kw": ["élections anticipées Belgique", "article 46 Constitution", "dissolution des Chambres", "informateur royal", "affaires courantes"],
 "fait": """<p>La dissolution des Chambres n’est pas à la main du Premier ministre. L’<strong>article 46</strong> de la
Constitution en fixe trois voies :</p>
<ol>
<li>la Chambre <strong>refuse la confiance</strong> et ne propose pas de successeur au Premier ministre dans les
trois jours ;</li>
<li>la Chambre adopte une <strong>motion de méfiance</strong> sans proposer simultanément de successeur
(la motion « constructive » — avec successeur — ne permet donc pas la dissolution) ;</li>
<li>le gouvernement <strong>démissionne</strong> et la Chambre marque son accord sur la dissolution à la
<strong>majorité absolue</strong> de ses membres.</li>
</ol>
<p>Dans tous les cas, les élections doivent se tenir dans les <strong>quarante jours</strong>. Une quatrième voie,
plus lente, existe : l’adoption d’une <strong>déclaration de révision de la Constitution</strong> entraîne la
dissolution de plein droit — mais à la fin de la législature. Sans déclenchement, les prochaines élections
fédérales ordinaires sont attendues en <strong>2029</strong>, couplées aux régionales et aux européennes.</p>""",
 "scene": """<p>On vous a convoqué·e comme expert technique, ce qui, dans ce bâtiment, signifie : quelqu’un qui
connaît les chiffres et ne parle qu’en réponse à une question.</p>
<p>L’informateur désigné il y a douze jours a fait le tour des présidents de parti. Le tableau qu’il vous montre
tient en trois lignes : aucune coalition alternative ne dispose d’une majorité dans la Chambre actuelle ; deux
formations refusent tout scénario incluant la N-VA ; une troisième refuse tout scénario l’excluant.</p>
<p>« Vous avez suivi le budget depuis septembre », dit-il. « Vous, techniquement, vous recommanderiez quoi ? »</p>""",
 "choix": [
  {"id":"c5a","eff":"tension:+3,stab:-3,cred:+3",
   "t":"La dissolution immédiate","s":"Activer l’article 46 et convoquer les électeurs dans les quarante jours.",
   "c":"""<p>C’est net et c’est démocratique : quand une majorité n’existe plus, le corps électoral tranche.</p>
<p>C’est aussi la solution qui produit le plus d’incertitude à court terme. Une campagne de quarante jours ne laisse
pas le temps de chiffrer les programmes ; le Bureau fédéral du Plan, qui réalise l’exercice de chiffrage depuis
2014, aura besoin de plusieurs mois. Et les sondages laissent entrevoir un Parlement plus fragmenté que celui qu’on
dissout : la question de la majorité n’est pas résolue, elle est déplacée de six mois.</p>"""},
  {"id":"c5b","eff":"cred:+8,stab:+2,tension:0",
   "t":"Un gouvernement de mission","s":"Une équipe resserrée, un mandat écrit, une durée limitée : budget et rien d’autre.",
   "c":"""<p>Ce n’est pas prévu par la Constitution, et c’est déjà arrivé : la Belgique a plusieurs fois gouverné avec
des majorités de mission, des pouvoirs spéciaux ou des gouvernements minoritaires soutenus texte par texte.</p>
<p>Le mandat écrit change tout : il rend le contrat vérifiable. Un gouvernement qui promet de boucler la
trajectoire budgétaire et de ne rien faire d’autre peut être jugé sur pièces à date fixe. C’est la seule option
qui augmente à la fois la crédibilité extérieure du pays et la lisibilité du mandat pour les électeurs.</p>"""},
  {"id":"c5c","eff":"stab:-6,soc:-4,tension:+1",
   "t":"Les affaires courantes jusqu’en 2029","s":"Laisser le gouvernement démissionnaire gérer, et attendre le scrutin ordinaire.",
   "c":"""<p>Constitutionnellement impeccable, et déjà vécu : 2007-2008, 2010-2011, 2018-2020. Le pays continue de
fonctionner ; l’administration, elle, tient.</p>
<p>Mais un gouvernement en affaires courantes ne peut engager de politique nouvelle. Pendant vingt-deux mois,
aucune réforme fiscale, aucun ajustement du régime des CPAS, aucune décision sur la trajectoire européenne.
La dette continue d’avancer pendant que la décision, elle, s’arrête. Le coût de l’immobilisme est invisible et
il est réel.</p>"""},
  {"id":"c5d","eff":"stab:-5,tension:+2,cred:+2",
   "t":"Ouvrir la révision constitutionnelle","s":"Adopter une déclaration de révision et préparer une réforme de l’État.",
   "c":"""<p>C’est la réponse que la Belgique donne à ses crises depuis 1970 : quand le désaccord n’est plus
gérable dans les institutions, on change les institutions.</p>
<p>La déclaration de révision entraîne la dissolution de plein droit à la fin de la législature — donc pas
d’élections immédiates, mais une campagne qui portera sur l’architecture de l’État plutôt que sur le budget.
Les questions posées en septembre 2026 — qui paie, qui reçoit, qui contrôle — ne disparaissent pas ; elles
attendront la fin d’une négociation institutionnelle dont personne n’a jamais su prédire la durée.</p>"""},
 ],
 "sources": [
  ("Constitution belge, articles 46 et 195 — Sénat de Belgique","https://www.senate.be/doc/const_fr.html"),
  ("Élections en Belgique — présentation générale","https://elections.fgov.be/"),
  ("Les différents types d’élections en Belgique — Bruxelles-J","https://www.bruxelles-j.be/exercer-ta-citoyennete/quels-sont-les-differents-types-delections/"),
 ],
},
{
 "id": "ch6", "n": 6, "slug": "06-la-campagne",
 "titre": "La campagne",
 "date": "Automne 2027",
 "lieu": "Une salle communale, quelque part entre Namur et Anvers",
 "meta_title": "Chapitre 6 — La campagne | Le compte à rebours",
 "meta_desc": "Cordon sanitaire, pouvoir d’achat, question institutionnelle : sur quoi se joue une campagne fédérale belge, et ce que chaque cadrage coûte au débat.",
 "kw": ["cordon sanitaire", "campagne électorale Belgique", "Vlaams Belang", "vote obligatoire", "débat électoral"],
 "fait": """<p>La Belgique francophone applique depuis le « dimanche noir » du 24 novembre 1991 un
<strong>cordon sanitaire</strong> double : politique (aucune coalition avec l’extrême droite) et médiatique
(pas d’accès au direct sur les médias de service public francophones). C’est une spécificité européenne, et elle
est régulièrement contestée — y compris par des responsables de partis démocratiques.</p>
<p>Le rapport de force est asymétrique. En Flandre, le <strong>Vlaams Belang</strong> se situe entre
<strong>25 et 27 %</strong> dans les enquêtes de 2026, au coude-à-coude avec la N-VA. En Wallonie, le
<strong>PS</strong> est repassé en tête (27,9 % en mars 2026) devant le MR ; à Bruxelles, le
<strong>PTB</strong> est devenu la première force (25,5 % en mars, 24,8 % en juin). Le vote reste
<strong>obligatoire</strong> pour les scrutins fédéral, régional et européen.</p>""",
 "scene": """<p>Vous avez quitté l’administration en juillet. Depuis, vous coordonnez un collectif citoyen qui
organise des débats budgétaires en salle communale — sans plateau, sans chronomètre, avec le tableur projeté
au mur. Vingt-trois soirées, de Herstal à Turnhout.</p>
<p>La question qui revient partout est la même, formulée de vingt-trois façons : <em>où est passé l’argent</em>.
Celle qui divise votre collectif est différente : qui invite-t-on à la tribune ?</p>
<p>Il reste six semaines avant le scrutin. La prochaine soirée est complète depuis dix jours.</p>""",
 "choix": [
  {"id":"c6a","eff":"cred:+5,soc:+2,stab:+2,tension:0",
   "t":"Tous les partis démocratiques, sur le budget","s":"Même tableur, mêmes vingt minutes, mêmes questions chiffrées pour chacun.",
   "c":"""<p>Le format est ingrat pour les orateurs et excellent pour le public : personne ne peut promettre sans
dire où il prend l’argent, parce que le tableau est projeté derrière lui.</p>
<p>Deux partis envoient des seconds couteaux, un troisième décline. Ceux qui viennent découvrent que le public
retient les chiffres. Trois questions posées ce soir-là seront reprises telles quelles dans les débats
télévisés — c’est peu, et c’est plus que ce que la plupart des campagnes produisent.</p>"""},
  {"id":"c6b","eff":"soc:+6,cred:-2,tension:+1",
   "t":"Centrer sur le pouvoir d’achat","s":"Factures, salaires, allocations, loyers : ce que les gens vivent, pas ce que l’État comptabilise.",
   "c":"""<p>La salle est pleine et le débat est vif. C’est le sujet sur lequel les électeurs ont la plus grande
compétence : ils vivent dedans.</p>
<p>Le risque est le pendant du bénéfice. Un débat cadré sur le vécu se prête mal aux arbitrages : chaque promesse
paraît raisonnable prise isolément, et l’addition n’est jamais faite. Le collectif gagne en audience et perd la
chose qui le distinguait — la contrainte budgétaire projetée au mur.</p>"""},
  {"id":"c6c","eff":"cred:+6,soc:-3,stab:-3,tension:+1",
   "t":"Centrer sur l’institutionnel","s":"Qui décide, qui paie, qui reçoit : le fédéral, les Régions, les communes.",
   "c":"""<p>C’est la question que la crise a réellement posée : les mesures se décident au fédéral et les
conséquences arrivent au guichet communal. Personne ne la traite parce qu’elle est aride.</p>
<p>Les soirées sont plus courtes et le public plus restreint — mais ce public repart en sachant lire un
transfert de charge. Vous alimentez aussi, sans l’avoir cherché, la campagne de ceux qui veulent régionaliser
davantage : une question institutionnelle bien posée ne reste jamais neutre longtemps.</p>"""},
  {"id":"c6d","eff":"stab:-8,soc:-8,cred:-2,tension:+2",
   "t":"Rompre le cordon","s":"Inviter l’extrême droite sur le plateau pour, dit-on, « la confronter aux chiffres ».",
   "c":"""<p>L’argument est ancien : la confrontation démasquerait. Les études comparatives européennes sont, au
mieux, incertaines sur ce point — la mise en visibilité produit aussi de la normalisation, et la « fenêtre
d’Overton » se déplace des deux côtés.</p>
<p>La soirée est la plus suivie de la série et la seule dont on retiendra un affrontement plutôt qu’un chiffre.
Deux partis se retirent du cycle, le collectif se scinde, et le débat public sur le budget se déplace vers un
débat sur le débat. Vous avez perdu l’outil, et l’attention avec.</p>"""},
 ],
 "sources": [
  ("Extrême droite francophone — CRISP","https://www.crisp.be/fr/248-extreme-droite-francophone"),
  ("Ne coupons pas le cordon sanitaire, consolidons-le — Agir par la culture","https://agirparlaculture.be/ne-coupons-pas-le-cordon-sanitaire-consolidons-le/"),
  ("Baromètre politique : le PS s’envole en Wallonie, le PTB première force à Bruxelles — L’Avenir, 13 mars 2026","https://www.lavenir.net/actu/belgique/politique/2026/03/13/barometre-politique-le-ps-senvole-en-wallonie-le-ptb-devient-la-premiere-force-a-bruxelles-5UHV62PLFZFTJDXSJXFVZYHJLY/"),
 ],
},
{
 "id": "ch7", "n": 7, "slug": "07-le-scrutin",
 "titre": "Le scrutin",
 "date": "Un dimanche de la fin 2027",
 "lieu": "Une école communale, votre bureau de vote",
 "meta_title": "Chapitre 7 — Le scrutin | Le compte à rebours",
 "meta_desc": "Proportionnelle D’Hondt, seuil de 5 %, vote obligatoire : ce que fait réellement votre bulletin, et pourquoi le vote utile ne fonctionne pas comme on le croit en Belgique.",
 "kw": ["système D’Hondt", "vote obligatoire Belgique", "seuil électoral 5 %", "vote blanc", "circonscriptions"],
 "fait": """<p>La Chambre des représentants compte <strong>150 sièges</strong>, répartis à la
<strong>proportionnelle selon la méthode D’Hondt</strong> dans des circonscriptions provinciales, plus
Bruxelles-Capitale. Une liste doit atteindre <strong>5 % des voix dans la circonscription</strong> pour participer
à la répartition.</p>
<p>Trois conséquences pratiques, souvent mal comprises : le <strong>vote utile</strong> a peu d’effet dans les
grandes circonscriptions, où le seuil est facilement franchi ; le <strong>vote blanc ou nul</strong> n’est pas
comptabilisé dans la répartition et ne bénéficie donc à personne, contrairement à une croyance tenace ; et le
<strong>vote est obligatoire</strong> pour les scrutins fédéral, régional et européen. Le nombre de sièges obtenu ne
détermine pas qui gouverne : la coalition se négocie après, et c’est là que les programmes se transforment.</p>""",
 "scene": """<p>L’école sent le café et le papier. Il y a une file, il y a un assesseur qui cherche votre nom, il y a
le rideau.</p>
<p>Quatorze mois plus tôt, vous ouvriez un tableur à six heures du matin en vous demandant s’il fallait publier
un chiffre. Vous avez vu ce que les décisions font aux gens, et ce que les gens font aux décisions. Vous savez
que le bulletin ne réglera pas la question posée en septembre 2026 — et qu’il n’y a rien d’autre à sa place.</p>
<p>Vous prenez le crayon rouge.</p>""",
 "choix": [
  {"id":"c7a","eff":"cred:+2,soc:+2,stab:+2,tension:0",
   "t":"Le programme le plus proche du vôtre","s":"Vous avez lu, comparé, et vous votez pour ce que vous voulez voir défendu.",
   "c":"""<p>C’est ce que mesure un test électoral, et c’est ce que la littérature académique appelle
l’efficacité politique interne : la confiance de l’électeur dans sa propre capacité à choisir.</p>
<p>La limite est connue et vaut d’être dite : un programme n’est pas un contrat. La Belgique gouverne par
coalitions de cinq ou six partis, et chaque coalition dilue les programmes qui la composent. Voter pour un
programme, c’est voter pour une position de départ dans une négociation — ce qui n’est pas rien, et n’est pas
tout.</p>"""},
  {"id":"c7b","eff":"stab:+3,cred:-1,tension:-1",
   "t":"Le vote utile","s":"Voter pour la liste la mieux placée pour bloquer la coalition que vous ne voulez pas.",
   "c":"""<p>Rationnel dans un scrutin majoritaire, beaucoup moins ici. Avec la proportionnelle D’Hondt et un seuil
de 5 % par circonscription, le report de voix vers un grand parti change rarement le nombre de sièges de plus
d’une unité.</p>
<p>Ce que le vote utile déplace vraiment, c’est le rapport de force <em>à l’intérieur</em> d’un bloc — qui obtient
le poste de formateur, qui parle au nom de sa famille politique. C’est réel, c’est plus modeste que la promesse,
et cela mérite d’être su avant d’entrer dans l’isoloir.</p>"""},
  {"id":"c7c","eff":"soc:-3,stab:-3,tension:+1",
   "t":"Le vote blanc","s":"Aucune liste ne vous convainc, et vous voulez que cela se voie.",
   "c":"""<p>Le geste est légitime et il est comptabilisé : les bulletins blancs et nuls sont publiés. Ils ne sont
simplement pas répartis, contrairement à la croyance selon laquelle ils profiteraient au parti arrivé en tête.</p>
<p>Son effet dépend entièrement de son ampleur. Marginal, il ne dit rien. Massif — au-delà de 8 à 10 % — il devient
un objet de commentaire politique et pèse sur la légitimité de la coalition qui suivra. Entre les deux, il est
surtout un message adressé à soi-même.</p>"""},
  {"id":"c7d","eff":"soc:+5,stab:-5,tension:+2",
   "t":"L’opposition frontale","s":"Voter pour une formation qui refuse la logique des coalitions de compromis.",
   "c":"""<p>C’est la dynamique dominante de 2026 : le PTB première force à Bruxelles, le Vlaams Belang au sommet
en Flandre. Deux positions opposées, une même adresse — le rejet du compromis gouvernemental.</p>
<p>L’effet est un déplacement du centre de gravité : un parti d’opposition frontale qui progresse contraint ses
voisins à durcir leur ligne pour retenir leur électorat. Il rend aussi les majorités plus difficiles à composer,
donc plus larges, donc plus hétérogènes — le mécanisme même que ce vote entend sanctionner.</p>"""},
 ],
 "sources": [
  ("Élections fédérales : mode de scrutin et répartition des sièges — SPF Intérieur","https://elections.fgov.be/"),
  ("Les jeunes et l’apprentissage politique par les systèmes d’aide au vote — Diversité (OpenEdition)","https://journals.openedition.org/diversite/6196"),
  ("Lancement du Test électoral — ISPOLE, UCLouvain","https://uclouvain.be/fr/instituts-recherche/ispole/news/lancement-du-test-electoral"),
 ],
},
]

FINS = [
{
 "slug": "fin-legislature",
 "titre": "La législature va à son terme",
 "meta": "Scrutin ordinaire, 2029 · Plausibilité : élevée",
 "corps": """<p>Rien ne casse. Les arbitrages sont douloureux, les conclaves durent trois jours de trop, les
partenaires se plaignent dans la presse le lundi et votent le jeudi — et la coalition arrive au bout. Les prochaines
élections fédérales se tiennent en 2029, couplées aux régionales et aux européennes comme le veut désormais
l’architecture belge.</p>
<p>C’est, historiquement, le dénouement le plus fréquent : depuis 1981, la majorité des gouvernements fédéraux
belges ont atteint le terme de la législature ou en sont sortis à quelques mois de l’échéance. Les crises se
règlent plus souvent par un gel de mesure que par une dissolution.</p>
<h4>Ce que ça coûte</h4>
<p>La stabilité obtenue par report a un prix comptable. Chaque mesure gelée sans financement de remplacement
alourdit la trajectoire suivante, et les intérêts de la dette — le poste qui augmente le plus vite dans le budget
fédéral belge — continuent de courir. Une législature qui va au bout n’est pas une législature qui a résolu ses
problèmes ; c’est une législature qui les a transmis.</p>
<h4>Signaux à surveiller</h4>
<ul><li>Les clauses de rendez-vous : combien sont effectivement honorées au contrôle budgétaire de mars ?</li>
<li>L’écart entre l’effort annoncé et l’effort constaté par le Comité de monitoring.</li>
<li>Le nombre de textes de l’accord d’été effectivement déposés et votés à la Chambre.</li></ul>""",
},
{
 "slug": "fin-gouvernement-de-mission",
 "titre": "Le gouvernement de mission",
 "meta": "Mandat écrit, durée limitée · Plausibilité : moyenne",
 "corps": """<p>La coalition ne survit pas telle quelle, mais le pays ne va pas aux urnes. Une équipe resserrée
reçoit un mandat écrit, borné dans le temps et dans son objet : boucler la trajectoire budgétaire, sécuriser le
régime compensatoire des CPAS, rien d’autre. Les partis qui la soutiennent ne signent pas un accord de
gouvernement complet, mais une liste de textes.</p>
<p>La Belgique a plusieurs fois pratiqué des variantes de ce dispositif : gouvernements minoritaires soutenus
texte par texte, pouvoirs spéciaux à durée déterminée, majorités de circonstance sur un objet unique. Ce n’est pas
prévu par la Constitution ; ce n’est pas non plus interdit par elle.</p>
<h4>Pourquoi ce dénouement suppose de la crédibilité technique</h4>
<p>Un mandat de mission n’est acceptable que s’il est vérifiable. Il exige des chiffres qui ne sont contestés par
personne, un calendrier public et un organe qui constate publiquement l’exécution. C’est exactement ce que
produisent, dans le parcours, les choix qui privilégient la transparence des hypothèses sur le confort politique.</p>
<h4>Signaux à surveiller</h4>
<ul><li>L’existence d’un document public de mandat, avec échéances datées.</li>
<li>Le maintien d’un contrôle parlementaire réel — un gouvernement de mission peut vite devenir un gouvernement
sans opposition organisée.</li>
<li>La position de la Commission européenne sur la trajectoire, qui conditionne la crédibilité extérieure.</li></ul>""",
},
{
 "slug": "fin-anticipees",
 "titre": "Les élections anticipées",
 "meta": "Article 46, scrutin dans les 40 jours · Plausibilité : moyenne-faible",
 "corps": """<p>La Chambre refuse la confiance et ne propose pas de successeur ; ou elle adopte une motion de
méfiance sans nom de remplacement ; ou le gouvernement démissionne et la Chambre approuve la dissolution à la
majorité absolue. Dans les trois cas, l’article 46 s’applique et les électeurs sont convoqués dans les quarante
jours.</p>
<p>C’est rare, et pour une raison très concrète : la dissolution fédérale désynchronise le calendrier électoral
belge. Depuis 2014, fédérales, régionales et européennes sont couplées ; un scrutin fédéral anticipé crée une
Chambre dont le mandat ne coïncide plus avec celui des Parlements régionaux, avec toutes les complications de
gouvernance que cela implique. La dernière dissolution anticipée réelle remonte à 2010.</p>
<h4>Ce que la campagne ne pourra pas faire</h4>
<p>Quarante jours ne suffisent pas au chiffrage des programmes par le Bureau fédéral du Plan, exercice qui
structure le débat économique belge depuis 2014. La campagne se joue donc sur des promesses non arbitrées —
au moment précis où le pays a besoin d’arbitrages.</p>
<h4>Signaux à surveiller</h4>
<ul><li>Le dépôt effectif d’une motion de méfiance et sa forme : avec ou sans successeur désigné.</li>
<li>L’attitude du Roi face à une démission : acceptation immédiate ou mise « en suspens ».</li>
<li>Les projections de sièges : une dissolution qui reconduit la même arithmétique ne résout rien.</li></ul>""",
},
{
 "slug": "fin-affaires-courantes",
 "titre": "Le pays en affaires courantes",
 "meta": "Gouvernement démissionnaire, durée indéterminée · Plausibilité : élevée",
 "corps": """<p>Le gouvernement tombe et rien ne le remplace. Il expédie les affaires courantes : il paie, il
exécute, il représente la Belgique dans les enceintes internationales, mais il n’engage plus de politique nouvelle.
La Belgique a établi en 2010-2011 le record mondial de durée en la matière — 541 jours sans gouvernement de plein
exercice — et l’a frôlé plusieurs fois depuis.</p>
<p>La démonstration la plus récente est régionale : Bruxelles est restée près de six cents jours sans gouvernement
après le scrutin de juin 2024, jusqu’à la prestation de serment du gouvernement Boris Dilliès le 14 février 2026
et le vote de confiance du 27 février.</p>
<h4>Le coût invisible</h4>
<p>L’administration tient, les guichets restent ouverts, les allocations sont payées. Ce qui s’arrête, ce sont
les décisions : pas d’ajustement du régime compensatoire des CPAS, pas de correction de trajectoire budgétaire,
pas de réponse aux recommandations européennes. Pendant ce temps, la charge d’intérêts progresse et les
dossiers s’empilent. L’immobilisme belge n’est pas gratuit, il est simplement non facturé sur l’exercice en cours.</p>
<h4>Signaux à surveiller</h4>
<ul><li>La doctrine retenue pour les affaires courantes : restrictive ou extensive ? Elle s’est élargie à chaque crise.</li>
<li>Le recours aux « douzièmes provisoires » pour le budget.</li>
<li>Le nombre de dossiers européens où la Belgique s’abstient faute de position gouvernementale.</li></ul>""",
},
{
 "slug": "fin-institutionnelle",
 "titre": "La sortie institutionnelle",
 "meta": "Déclaration de révision, réforme de l’État · Plausibilité : moyenne",
 "corps": """<p>Quand le désaccord cesse d’être gérable dans les institutions, la Belgique change les institutions.
C’est la logique des six réformes de l’État depuis 1970, et c’est le scénario que déclenche l’adoption d’une
déclaration de révision de la Constitution : la dissolution devient de plein droit à la fin de la législature, et
la campagne suivante porte sur l’architecture de l’État.</p>
<p>Les termes du débat sont connus : la N-VA défend le confédéralisme, plusieurs formations flamandes demandent
la régionalisation de pans de la sécurité sociale, tandis que la quasi-totalité des partis francophones s’y
opposent et posent, en retour, la question du refinancement de Bruxelles. Aucun de ces blocs ne dispose seul de la
majorité des deux tiers requise pour réviser la Constitution.</p>
<h4>Ce que cela fait au reste</h4>
<p>Une négociation institutionnelle absorbe l’agenda. Les questions posées en septembre 2026 — qui paie, qui
reçoit, qui contrôle — ne disparaissent pas : elles attendent, et la trajectoire budgétaire attend avec elles.
La réforme de l’État est une réponse à un blocage politique ; elle n’a jamais été une réponse à un déficit.</p>
<h4>Signaux à surveiller</h4>
<ul><li>Le contenu de la déclaration de révision : quels articles sont ouverts ?</li>
<li>L’existence, ou non, d’une majorité des deux tiers plausible dans les deux groupes linguistiques.</li>
<li>Le sort du financement de Bruxelles, variable d’ajustement récurrente de ces négociations.</li></ul>""",
},
{
 "slug": "fin-recomposition",
 "titre": "La recomposition",
 "meta": "Le cordon à l’épreuve · Plausibilité : moyenne",
 "corps": """<p>Le scrutin ne produit pas une alternance, il produit un paysage. Les formations d’opposition
frontale — le PTB au sud et à Bruxelles, le Vlaams Belang au nord — captent une part du vote telle que les partis
de gouvernement ne peuvent plus composer de majorité sans élargir considérablement leur assemblage, ou sans
rouvrir des questions qu’ils tenaient pour fermées.</p>
<p>Les chiffres de 2026 rendent le scénario tangible : le Vlaams Belang entre 25 et 27 % en Flandre, le PTB
première force à Bruxelles avec un électeur sur quatre, et un MR qui s’effondre dans la capitale. C’est le
dénouement que déclenche une partie où la cohésion sociale a été sacrifiée à la stabilité comptable.</p>
<h4>Le point de bascule</h4>
<p>Le cordon sanitaire francophone n’a jamais été testé sur une arithmétique où il coûte le gouvernement.
Tant qu’une majorité alternative existe, il tient à peu de frais. Le jour où il faut choisir entre le cordon et la
gouvernabilité, ce n’est plus une règle morale, c’est une décision politique — et c’est à ce moment-là que la
comparaison avec les autres démocraties européennes cesse d’être théorique.</p>
<h4>Signaux à surveiller</h4>
<ul><li>Le nombre de coalitions arithmétiquement possibles sans les formations sous cordon.</li>
<li>Les prises de position publiques sur le cordon <em>médiatique</em>, qui précèdent en général celles sur le
cordon politique.</li>
<li>La participation et le vote blanc : une abstention forte change les seuils autant que les reports de voix.</li></ul>""",
},
]
