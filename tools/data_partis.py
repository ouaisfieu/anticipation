# -*- coding: utf-8 -*-
"""Fiches des partis. Chiffres électoraux : scrutins de juin 2024.
Intentions de vote : Grand Baromètre Ipsos-Le Soir-RTL, mars 2026 (et juin 2026 pour Bruxelles)."""

PARTIS = [
{
 "slug":"mr","nom":"MR","cls":"pcolor-mr","abbr":"MR",
 "long":"Mouvement Réformateur",
 "famille":"Libéral, centre droit à droite",
 "president":"Georges-Louis Bouchez",
 "site":"https://www.mr.be/",
 "resume":"Premier parti francophone depuis juin 2024, moteur idéologique des réformes d’activation. En forte baisse à Bruxelles dans les enquêtes de 2026.",
 "meta_desc":"MR : programme, bilan gouvernemental 2024-2026, résultats électoraux, forces et angles morts. Le parti libéral francophone au cœur des coalitions fédérale, wallonne, bruxelloise et de la FWB.",
 "kw":["MR","Mouvement Réformateur","Georges-Louis Bouchez","programme MR","libéraux francophones"],
 "chiffres":[("10,26 %","Chambre, juin 2024 — 20 sièges"),("29,6 %","Parlement wallon, juin 2024"),
             ("21,0 %","Wallonie, intentions de vote mars 2026"),("13,9 %","Bruxelles, juin 2026")],
 "adn":"""<p>Né en 2002 de la fusion des familles libérales francophones, le MR défend la primauté de l’initiative
privée, la baisse de la fiscalité sur le travail et un objectif affiché de <strong>80 % de taux d’emploi</strong>.
Sous la présidence de Georges-Louis Bouchez, il a durci sa ligne sur la sécurité, la migration et la place des
allocations sociales, jusqu’à devenir en juin 2024 le premier parti francophone du pays.</p>
<p>Le MR est le seul parti francophone présent dans les quatre exécutifs qui comptent : fédéral (Arizona),
wallon, bruxellois (gouvernement Dilliès depuis février 2026) et Fédération Wallonie-Bruxelles. Cette position
lui donne une capacité d’action inédite — et lui attribue, dans l’opinion, la responsabilité de l’ensemble du
bilan.</p>""",
 "mesures":[
   ("Emploi","Limitation des allocations de chômage à 24 mois, écart d’au moins 500 € entre revenus du travail et allocations, extension des flexi-jobs à tous les secteurs."),
   ("Fiscalité","Refus de tout impôt sur le patrimoine ; baisse de l’impôt des personnes physiques ; droits d’enregistrement wallons ramenés de 12,5 % à 3 % pour l’habitation propre et unique ; division par deux des droits de succession."),
   ("Pensions","Accès à la retraite anticipée conditionné à 42 années de travail effectif, système de bonus-malus, alignement progressif du régime des fonctionnaires sur le privé."),
   ("Énergie","Prolongation et développement du parc nucléaire, présentés comme la condition de la souveraineté énergétique."),
   ("État","Réduction de la fonction publique, fusion d’agences wallonnes, recentrage du Forem sur l’activation."),
   ("Enseignement","Fin du Pacte d’excellence, remplacé par un « Pacte de confiance » ; réintroduction d’options en 3e secondaire ; interdiction du smartphone en primaire."),
 ],
 "forces":["Position unique dans les quatre exécutifs francophones","Discours de gestion lisible et constant",
           "Ancrage solide dans les classes moyennes urbaines et l’indépendance économique"],
 "faiblesses":["Effondrement bruxellois : de ~26 % en 2024 à 13,9 % en juin 2026",
               "Portage de l’impopularité de mesures qu’il a lui-même conçues",
               "Tension permanente avec la N-VA sur la fiscalité et l’institutionnel"],
 "aussi":["ps","les-engages","ptb"],
},
{
 "slug":"ps","nom":"PS","cls":"pcolor-ps","abbr":"PS",
 "long":"Parti Socialiste",
 "famille":"Social-démocrate, centre gauche",
 "president":"Paul Magnette",
 "site":"https://www.ps.be/",
 "resume":"Redevenu premier parti en Wallonie dans les enquêtes de 2026 après avoir perdu la place en 2024. Opposition frontale aux réformes de l’Arizona, sous pression du PTB sur sa gauche.",
 "meta_desc":"PS : programme, ligne d’opposition à l’Arizona, impôt sur les grandes fortunes, gratuité des soins de première ligne, résultats et dynamique électorale 2024-2026.",
 "kw":["PS","Parti Socialiste","Paul Magnette","impôt grandes fortunes","gratuité soins de santé"],
 "chiffres":[("8,04 %","Chambre, juin 2024 — 16 sièges"),("23,2 %","Parlement wallon, juin 2024"),
             ("27,9 %","Wallonie, intentions de vote mars 2026"),("18,3 %","Bruxelles, juin 2026")],
 "adn":"""<p>Héritier d’un siècle de mouvement ouvrier, le PS défend l’État social, la sécurité sociale fédérale
et les services publics. Écarté de tous les exécutifs après juin 2024 — à l’exception du gouvernement bruxellois
qu’il a rejoint en février 2026 —, il a fait de l’opposition aux mesures d’activation son axe principal.</p>
<p>Sa reconstruction passe par un dispositif interne assumé : l’« EMILE », école de militantisme lancée en 2024,
et des panels citoyens tirés au sort préparant un congrès statutaire fin 2026. La pression du PTB, qui le
dépasse largement à Bruxelles, structure sa stratégie : ne laisser aucun espace à sa gauche sur la défense des
acquis sociaux.</p>""",
 "mesures":[
   ("Fiscalité","Impôt sur les patrimoines supérieurs à 1,25 million d’euros (hors résidence principale et outil professionnel) ; globalisation des revenus ; taxation des plus-values au-delà du taux de 10 % adopté en 2026."),
   ("Santé","Gratuité totale des soins de première ligne : généraliste, dentiste, psychologue, avec suppression des tickets modérateurs et visites à domicile gratuites après 75 ans."),
   ("Salaires","Défense inconditionnelle de l’indexation automatique intégrale ; opposition frontale au plafonnement adopté pour 2026 et 2028."),
   ("Pensions","Refus de tout recul de l’âge légal, refus du malus pour carrières longues et pénibles, défense de la pension minimum."),
   ("Emploi","Opposition à la limitation du chômage dans le temps ; priorité à la formation et à l’accompagnement."),
   ("Énergie","Prolongation du nucléaire de dix ans, objectif de 100 % de renouvelable en 2050, élargissement du tarif social."),
 ],
 "forces":["Réseau local dense : bourgmestres, mutualités, syndicat socialiste",
           "Redressement net dans les enquêtes wallonnes en 2026","Clarté de la ligne d’opposition"],
 "faiblesses":["Concurrence directe du PTB à Bruxelles, où il est distancé","Héritage de scandales de gouvernance",
               "Difficulté à chiffrer une alternative crédible sous contrainte européenne"],
 "aussi":["ptb","mr","ecolo"],
},
{
 "slug":"ptb","nom":"PTB","cls":"pcolor-ptb","abbr":"PTB",
 "long":"Parti du Travail de Belgique — PVDA",
 "famille":"Gauche radicale, unitaire (bilingue)",
 "president":"Raoul Hedebouw",
 "site":"https://www.ptb.be/",
 "resume":"Première force politique à Bruxelles selon les enquêtes de 2026, avec un électeur sur quatre. Seul parti unitaire du paysage belge, il progresse simultanément au nord et au sud.",
 "meta_desc":"PTB-PVDA : programme, taxe des millionnaires, opposition à l’Arizona, percée bruxelloise 2026. Le seul parti unitaire belge, première force à Bruxelles dans les sondages.",
 "kw":["PTB","PVDA","Raoul Hedebouw","taxe des millionnaires","gauche radicale Belgique"],
 "chiffres":[("9,86 %","Chambre, juin 2024 — 15 sièges"),("18,5 %","Parlement bruxellois, juin 2024"),
             ("25,5 %","Bruxelles, intentions de vote mars 2026"),("9,8 %","Flandre (PVDA), mars 2026")],
 "adn":"""<p>Fondé en 1979, longtemps marginal, le PTB a opéré à partir des années 2000 une mue stratégique :
langage accessible, implantation de terrain, refus assumé des coalitions de compromis. C’est le
<strong>seul parti véritablement unitaire</strong> du paysage belge, présent des deux côtés de la frontière
linguistique sous deux noms.</p>
<p>Sa percée bruxelloise de 2026 — 25,5 % en mars, 24,8 % en juin — est le fait électoral marquant de la
législature. Elle traduit une réaction directe aux mesures d’activation : là où le basculement des exclus du
chômage vers les CPAS est le plus dense, le vote de rupture progresse le plus vite.</p>""",
 "mesures":[
   ("Fiscalité","« Taxe des millionnaires » sans les exemptions dénoncées dans le dispositif Arizona ; TVA à 0 % sur les produits de première nécessité ; retour de la TVA énergie à 6 %."),
   ("Emploi","Opposition totale à la limitation du chômage dans le temps, au travail de nuit assoupli et aux flexi-jobs ; réduction collective du temps de travail."),
   ("Pensions","Refus du durcissement de l’accès anticipé, des 42 années de travail effectif et de la suppression des régimes de métiers pénibles."),
   ("Santé","Opposition à ce qu’il qualifie de « traque » des malades de longue durée ; hôpitaux publics ; gratuité des soins."),
   ("Services publics","Renationalisation de l’énergie et du rail, gratuité des transports en commun."),
   ("Méthode","Opposition parlementaire et extraparlementaire combinées : recours juridiques, pétitions, mobilisations de terrain."),
 ],
 "forces":["Seul parti présent dans les deux communautés linguistiques","Dynamique électorale la plus forte du pays",
           "Capacité de mobilisation hors des périodes électorales"],
 "faiblesses":["Aucune expérience de gouvernement, aucun partenaire de coalition disponible",
               "Chiffrage macroéconomique contesté par le Bureau fédéral du Plan",
               "Stagnation relative en Wallonie face à un PS qui se redresse"],
 "aussi":["ps","ecolo","mr"],
},
{
 "slug":"les-engages","nom":"Les Engagés","cls":"pcolor-le","abbr":"LE",
 "long":"Les Engagés",
 "famille":"Centre, héritage démocrate-chrétien",
 "president":"Maxime Prévot",
 "site":"https://www.lesengages.be/",
 "resume":"Grand gagnant de 2024 avec un quasi-triplement de ses sièges. Charnière de toutes les coalitions francophones, il propose en 2026 de taxer les patrimoines au-delà de 500 000 €.",
 "meta_desc":"Les Engagés : programme, « Régénération », position charnière dans les coalitions fédérale et régionales, proposition de contribution sur les patrimoines supérieurs à 500 000 €.",
 "kw":["Les Engagés","Maxime Prévot","cdH","Régénération","centre francophone"],
 "chiffres":[("6,77 %","Chambre, juin 2024 — 14 sièges"),("21,3 %","Parlement wallon, juin 2024"),
             ("19,4 %","Wallonie, intentions de vote mars 2026"),("10,0 %","Bruxelles, juin 2026")],
 "adn":"""<p>Refondation du cdH achevée en 2022, Les Engagés articulent leur doctrine autour de la
<strong>« Régénération »</strong> : refus du modèle de croissance infinie, recherche d’un équilibre entre
exigence budgétaire et ancrage social hérité de la démocratie chrétienne. Le pari a payé électoralement — le
parti a presque triplé sa représentation en juin 2024.</p>
<p>Sa position est structurellement charnière. Partenaire du MR en Wallonie, à Bruxelles et en Fédération
Wallonie-Bruxelles, membre de l’Arizona au fédéral, il est le parti sans lequel aucune majorité francophone ne
se compose. C’est aussi celui qui, en juillet 2026, a rouvert le débat fiscal en proposant de faire contribuer
les patrimoines au-delà de 500 000 € — contre la ligne rouge du MR.</p>""",
 "mesures":[
   ("Fiscalité","Rigueur budgétaire assumée, mais ouverture à une contribution sur les patrimoines élevés ; suppression de niches fiscales ; TVA réduite sur la réparation des biens."),
   ("Emploi","Soutien à l’activation, conditionné à un accompagnement personnalisé et à un investissement dans la formation continue."),
   ("Enseignement","Réintroduction d’options dès la 3e secondaire, fusion progressive des réseaux officiels, financement équitable par élève."),
   ("Gouvernance","Supracommunalité, révision des structures provinciales, transparence des subventions, 40 % de femmes dans les hautes fonctions fédérales dès 2027."),
   ("Économie","Économie circulaire, agriculture rémunératrice et souveraine, soutien aux indépendants."),
   ("Climat","Sortie graduelle des subsides fossiles, aides à l’efficacité énergétique, mix diversifié incluant le nucléaire."),
 ],
 "forces":["Incontournable dans toute majorité francophone","Image d’équilibre entre rigueur et social",
           "Progression conservée dans les enquêtes wallonnes de 2026"],
 "faiblesses":["Exposition au bilan de coalitions dont il ne fixe pas la ligne dominante",
               "Difficulté à exister médiatiquement entre le MR et le PS","Faiblesse relative à Bruxelles"],
 "aussi":["mr","ps","defi"],
},
{
 "slug":"ecolo","nom":"Ecolo","cls":"pcolor-ecolo","abbr":"Eco",
 "long":"Ecolo",
 "famille":"Écologiste, centre gauche à gauche",
 "president":"Coprésidence Marie-Colline Leroy et Gilles Vanden Burre",
 "site":"https://ecolo.be/",
 "resume":"Sanctionné très durement en 2024 (2 sièges fédéraux contre 13), le parti a traversé deux démissions de coprésidence avant de se doter d’une nouvelle direction en mars 2026.",
 "meta_desc":"Ecolo : reconstruction après la défaite de 2024, nouvelle coprésidence Leroy–Vanden Burre depuis mars 2026, programme climat, fiscalité verte et individualisation des droits sociaux.",
 "kw":["Ecolo","écologistes francophones","Marie-Colline Leroy","Gilles Vanden Burre","écologie populaire"],
 "chiffres":[("2,93 %","Chambre, juin 2024 — 3 sièges"),("6,97 %","Parlement wallon, juin 2024"),
             ("7,9 %","Wallonie, intentions de vote mars 2026"),("7,1 %","Bruxelles, mars 2026")],
 "adn":"""<p>Fondé en 1980, Ecolo a connu en juin 2024 la défaite la plus sévère de son histoire : perte de plus
de la moitié de ses élus (13 sièges fédéraux en 2019, 3 en 2024) et sortie de tous les exécutifs sauf communaux. S’en est suivie une crise de direction —
démission de Jean-Marc Nollet et Rajae Maouane, puis de leurs successeurs Samuel Cogolati et Marie Lecocq en
novembre 2025 — avant l’élection d’une nouvelle coprésidence en mars 2026.</p>
<p>La ligne défendue par Marie-Colline Leroy et Gilles Vanden Burre est celle d’une « écologie populaire » :
articuler exigence climatique et justice sociale pour répondre à ce qu’ils décrivent comme une guerre culturelle
menée par les conservateurs. Le parti est présent au gouvernement bruxellois via son homologue flamand Groen.</p>""",
 "mesures":[
   ("Climat","Application stricte du pollueur-payeur, suppression des subsides directs et indirects aux énergies fossiles, rénovation énergétique massive du bâti."),
   ("Social","Individualisation des droits sociaux et suppression du statut de cohabitant, qui pénalise particulièrement les femmes isolées."),
   ("Mobilité","Investissement massif dans les transports en commun, gratuité pour les jeunes, les aînés et les ménages précaires."),
   ("Fiscalité","Progressivité renforcée, taxation du capital au même niveau que le travail, lutte contre l’évasion fiscale."),
   ("Agriculture","Réorientation de la PAC vers l’agroécologie, sortie progressive de l’élevage intensif hors-sol, accompagnement financier des exploitants."),
   ("Travail","Réduction collective du temps de travail, emplois de la transition (isolation, rail, rénovation)."),
 ],
 "forces":["Cohérence programmatique reconnue sur le climat","Base militante fidèle et jeune",
           "Position d’opposition qui permet de reconstruire sans porter un bilan"],
 "faiblesses":["Représentation parlementaire fédérale réduite à trois sièges","Deux crises de direction en dix-huit mois",
               "Concurrence du PTB sur l’électorat urbain jeune"],
 "aussi":["ps","ptb","les-engages"],
},
{
 "slug":"defi","nom":"DéFI","cls":"pcolor-defi","abbr":"DéFI",
 "long":"Démocrate Fédéraliste Indépendant",
 "famille":"Social-libéral, régionaliste bruxellois",
 "president":"Sophie Rohonyi",
 "site":"https://www.defi.be/",
 "resume":"Réduit à un siège fédéral et six sièges bruxellois, le parti amarante joue sa survie sur la défense du statut de Bruxelles et de la bonne gouvernance.",
 "meta_desc":"DéFI : programme, défense des francophones de la périphérie, bonne gouvernance et justice, situation électorale après le recul de 2024 sous la présidence de Sophie Rohonyi.",
 "kw":["DéFI","Sophie Rohonyi","francophones périphérie","Bruxelles","fédéralistes"],
 "chiffres":[("1,2 %","Chambre, juin 2024 — 1 siège"),("8,11 %","Parlement bruxellois, juin 2024"),
             ("4,5 %","Bruxelles, intentions de vote mars 2026"),("0 siège","Parlement wallon depuis 2024")],
 "adn":"""<p>Héritier du FDF fondé en 1964, DéFI s’est constitué autour de la défense des francophones de
Bruxelles et de sa périphérie. Sous la présidence de Sophie Rohonyi, élue en juillet 2024, il combine un
libéralisme social modéré, une exigence de laïcité et un travail parlementaire concentré sur la gouvernance :
transparence publique, encadrement des transactions pénales, refinancement de la justice.</p>
<p>Son recul de 2024 l’a privé de toute représentation au Parlement wallon et réduit à un seul siège fédéral.
Sa survie se joue à Bruxelles, où il a alerté sur le sous-financement des CPAS face à la limitation du chômage
et où il s’oppose à la fusion des dix-neuf communes défendue par le MR.</p>""",
 "mesures":[
   ("Institutions","Défense du statut bilingue de Bruxelles et des communes à facilités ; opposition à la fusion des dix-neuf communes ; refinancement structurel de la Région."),
   ("Gouvernance","Transparence des rémunérations publiques, durcissement des transactions pénales, refinancement de la justice."),
   ("Social","Alerte sur la sous-compensation des CPAS face à la limitation du chômage ; 9 000 logements sociaux sur cinq ans."),
   ("Enseignement","Renforcement de l’apprentissage du français à Bruxelles, trilinguisme, soutien au parascolaire."),
   ("Économie","Simplification administrative et soutien ciblé aux PME bruxelloises."),
   ("Mobilité","Piétonnisation progressive, amélioration des transports en commun, calendrier réaliste."),
 ],
 "forces":["Expertise reconnue sur les dossiers bruxellois et périphériques","Ligne constante sur la gouvernance",
           "Électorat fidèle dans le sud-est bruxellois"],
 "faiblesses":["Représentation nationale marginale : un siège fédéral","Absence totale du Parlement wallon",
               "Espace politique comprimé entre MR, Les Engagés et PS"],
 "aussi":["mr","les-engages","ps"],
},
]

FLANDRE = [
 ("N-VA","pcolor-nva","Nationaliste flamand, conservateur","Bart De Wever (Premier ministre)","25,5 %",
  "Premier parti flamand de justesse dans les enquêtes de mars 2026. Pilote la coalition Arizona et défend le confédéralisme à moyen terme."),
 ("Vlaams Belang","pcolor-vb","Extrême droite, indépendantiste","Tom Van Grieken","25,4 %",
  "Au coude-à-coude avec la N-VA, entre 25 et 27 % selon les vagues. Sous cordon sanitaire politique et médiatique du côté francophone ; le cordon politique tient également en Flandre, sans équivalent médiatique."),
 ("Vooruit","pcolor-vooruit","Social-démocrate flamand","Conner Rousseau","12,8 %",
  "Partenaire de gauche de l’Arizona : doit défendre un bilan social devant un électorat qui voit progresser le PVDA. Point de friction récurrent sur l’indexation."),
 ("CD&V","pcolor-cdv","Démocrate-chrétien flamand","Sammy Mahdi","12,6 %",
  "Charnière de la coalition, attaché au volet pénibilité des pensions et aux équilibres sociaux hérités du pilier chrétien."),
 ("PVDA","pcolor-ptb","Gauche radicale (branche flamande du PTB)","Raoul Hedebouw","9,8 %",
  "Progression continue en Flandre : le seul parti à croître simultanément dans les trois Régions."),
 ("Groen","pcolor-groen","Écologiste flamand","Jeremie Vaneeckhout","7,7 %",
  "Dans l’opposition au fédéral, mais au gouvernement bruxellois depuis février 2026 (Elke Van den Brandt à la Mobilité)."),
 ("Anders","pcolor-anders","Libéral flamand (ex-Open Vld)","Frédéric De Gucht","5,6 %",
  "L’Open Vld a pris le nom d’« Anders » le 19 janvier 2026. Absent du gouvernement fédéral depuis 2024, il siège en revanche au gouvernement bruxellois."),
]
