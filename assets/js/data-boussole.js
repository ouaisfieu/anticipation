/*! Anticipation — data-boussole.js
 *  Les 24 propositions du test électoral et le positionnement des six partis
 *  francophones, sur une échelle de -2 (opposition nette) à +2 (soutien net).
 *
 *  Ces positions sont une lecture des programmes 2024, des accords de
 *  gouvernement fédéral et régionaux 2024-2026 et des votes publics. Elles sont
 *  discutables : la page « Méthode » explique comment elles ont été établies,
 *  et chaque proposition est reproduite en clair dans le HTML de la page.
 */
window.BOUSSOLE = (function () {
  'use strict';

  var PARTIS = [
    { id: 'ps',    nom: 'PS',           long: 'Parti Socialiste',            cls: 'pcolor-ps',    url: '../partis/ps/' },
    { id: 'mr',    nom: 'MR',           long: 'Mouvement Réformateur',       cls: 'pcolor-mr',    url: '../partis/mr/' },
    { id: 'ptb',   nom: 'PTB',          long: 'Parti du Travail de Belgique',cls: 'pcolor-ptb',   url: '../partis/ptb/' },
    { id: 'le',    nom: 'Les Engagés',  long: 'Les Engagés',                 cls: 'pcolor-le',    url: '../partis/les-engages/' },
    { id: 'ecolo', nom: 'Ecolo',        long: 'Ecolo',                       cls: 'pcolor-ecolo', url: '../partis/ecolo/' },
    { id: 'defi',  nom: 'DéFI',         long: 'Démocrate Fédéraliste Indépendant', cls: 'pcolor-defi', url: '../partis/defi/' }
  ];

  /* q : intitulé — t : thème — eco/gal : direction et poids de l'accord
     p  : position des partis [ps, mr, ptb, le, ecolo, defi] */
  var Q = [
    { t:'Emploi',      q:'Les allocations de chômage doivent rester limitées à deux ans maximum.',
      eco:+1,   gal:0,     p:{ps:-2,mr:+2,ptb:-2,le:+1,ecolo:-2,defi:-1} },
    { t:'Fiscalité',   q:'Il faut instaurer un impôt sur les patrimoines supérieurs à un million d’euros.',
      eco:-1,   gal:0,     p:{ps:+2,mr:-2,ptb:+2,le:+1,ecolo:+2,defi:0} },
    { t:'Salaires',    q:'Le plafonnement de l’indexation automatique des salaires au-dessus de 4 000 € bruts est justifié.',
      eco:+1,   gal:0,     p:{ps:-2,mr:+2,ptb:-2,le:+1,ecolo:-1,defi:0} },
    { t:'Santé',       q:'Les soins de première ligne (généraliste, dentiste, psychologue) doivent devenir entièrement gratuits.',
      eco:-1,   gal:0,     p:{ps:+2,mr:-1,ptb:+2,le:0,ecolo:+2,defi:+1} },
    { t:'Énergie',     q:'Il faut prolonger et développer le parc nucléaire belge.',
      eco:0,    gal:+0.7,  p:{ps:+1,mr:+2,ptb:-1,le:+1,ecolo:-2,defi:+1} },
    { t:'Pensions',    q:'L’accès à la pension anticipée doit être durci : 42 années de travail effectif.',
      eco:+1,   gal:0,     p:{ps:-2,mr:+2,ptb:-2,le:+1,ecolo:-1,defi:0} },
    { t:'Fiscalité',   q:'La taxe de 10 % sur les plus-values financières doit être relevée.',
      eco:-1,   gal:0,     p:{ps:+2,mr:-2,ptb:+2,le:0,ecolo:+2,defi:0} },
    { t:'Travail',     q:'Les entreprises doivent pouvoir recourir plus librement au travail de nuit et du dimanche.',
      eco:+1,   gal:0,     p:{ps:-2,mr:+2,ptb:-2,le:+1,ecolo:-1,defi:0} },
    { t:'État',        q:'Il faut réduire le nombre de fonctionnaires et fusionner des administrations.',
      eco:+0.8, gal:+0.2,  p:{ps:-1,mr:+2,ptb:-2,le:+1,ecolo:-1,defi:0} },
    { t:'Mobilité',    q:'Les transports publics doivent être gratuits pour les jeunes et les bas revenus.',
      eco:-1,   gal:0,     p:{ps:+2,mr:-1,ptb:+2,le:0,ecolo:+2,defi:+1} },
    { t:'Démocratie',  q:'Le cordon sanitaire médiatique envers l’extrême droite doit être maintenu.',
      eco:0,    gal:-1,    p:{ps:+2,mr:0,ptb:+2,le:+1,ecolo:+2,defi:+2} },
    { t:'Institutions',q:'Davantage de compétences (santé, emploi) doivent être transférées aux Régions.',
      eco:0,    gal:+0.8,  p:{ps:-1,mr:+1,ptb:-2,le:0,ecolo:-1,defi:-2} },
    { t:'Migration',   q:'L’accès au séjour et au regroupement familial doit être nettement plus strict.',
      eco:0,    gal:+1,    p:{ps:-1,mr:+2,ptb:-2,le:+1,ecolo:-2,defi:0} },
    { t:'École',       q:'Le smartphone doit être interdit dans les écoles primaires.',
      eco:0,    gal:+0.5,  p:{ps:+1,mr:+2,ptb:0,le:+2,ecolo:0,defi:+1} },
    { t:'Défense',     q:'L’objectif de 2 % du PIB pour la défense doit être tenu, même au prix d’économies ailleurs.',
      eco:+0.3, gal:+0.7,  p:{ps:-1,mr:+2,ptb:-2,le:+1,ecolo:-1,defi:+1} },
    { t:'École',       q:'Il faut réintroduire des options dès la 3e secondaire plutôt qu’un tronc commun long.',
      eco:0,    gal:+0.8,  p:{ps:-1,mr:+2,ptb:-1,le:+2,ecolo:-2,defi:+1} },
    { t:'International',q:'La Belgique doit interdire l’importation de produits issus des colonies israéliennes.',
      eco:0,    gal:-0.8,  p:{ps:+2,mr:-1,ptb:+2,le:+1,ecolo:+2,defi:+1} },
    { t:'Climat',      q:'La fiscalité sur les énergies fossiles doit fortement augmenter (pollueur-payeur).',
      eco:-0.4, gal:-0.6,  p:{ps:+1,mr:-1,ptb:+1,le:+1,ecolo:+2,defi:0} },
    { t:'Santé',       q:'Les personnes en incapacité de travail de longue durée doivent être plus étroitement contrôlées.',
      eco:+1,   gal:0,     p:{ps:-1,mr:+2,ptb:-2,le:+1,ecolo:-1,defi:0} },
    { t:'Travail',     q:'Le droit de grève doit être encadré par un service minimum garanti.',
      eco:+0.6, gal:+0.4,  p:{ps:-2,mr:+2,ptb:-2,le:+1,ecolo:-1,defi:+1} },
    { t:'Gouvernance', q:'Il faut supprimer des niveaux de pouvoir et réduire le nombre de mandataires.',
      eco:0,    gal:+0.4,  p:{ps:0,mr:+2,ptb:+1,le:+2,ecolo:+1,defi:+1} },
    { t:'Bruxelles',   q:'Les 19 communes bruxelloises doivent fusionner en une seule entité.',
      eco:0,    gal:+0.3,  p:{ps:-1,mr:+2,ptb:-1,le:+1,ecolo:+1,defi:-2} },
    { t:'Social',      q:'Les allocations doivent être individualisées : suppression du statut de cohabitant.',
      eco:-0.6, gal:-0.4,  p:{ps:+2,mr:-1,ptb:+2,le:+1,ecolo:+2,defi:+1} },
    { t:'Fiscalité',   q:'Les droits de succession et de donation doivent continuer à baisser.',
      eco:+1,   gal:0,     p:{ps:-1,mr:+2,ptb:-2,le:+2,ecolo:-1,defi:+1} }
  ];

  return { partis: PARTIS, questions: Q };
})();
