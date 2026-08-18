# Anticipation — le jeu de la Belgique politique

Site statique d’éducation civique par le jeu, consacré à la situation politique et démocratique belge
en 2026-2027 : un parcours narratif à choix en sept chapitres, une boussole électorale à
vingt-quatre propositions, six dossiers de fond, une chronologie, les sondages et un glossaire.

**En ligne :** https://ouaisfieu.github.io/anticipation/

---

## Publier

Le site est **entièrement statique**. Aucune installation, aucune compilation, aucune dépendance.

1. Poussez le contenu de ce dossier à la racine du dépôt `ouaisfieu/anticipation`.
2. Dans *Settings → Pages*, choisissez « Deploy from a branch », branche `main`, dossier `/ (root)`.
3. C’est tout. Le fichier `.nojekyll` empêche GitHub de retraiter les fichiers.

Pour tester en local, n’importe quel serveur statique suffit :

```sh
python3 -m http.server 8000
# puis http://localhost:8000/
```

> ⚠️ Les liens internes sont relatifs, sauf dans `404.html` où ils pointent vers `/anticipation/`
> (chemin d’un *project site* GitHub Pages). Si vous publiez à la racine d’un domaine,
> remplacez `/anticipation/` par `/` dans ce seul fichier.

## Modifier

Deux façons, au choix.

**À la main.** Chaque page est un fichier HTML complet et lisible. Ouvrez-le, éditez le texte, sauvegardez.
Rien ne casse.

**Avec le générateur (optionnel).** Le dossier `tools/` contient les scripts Python qui ont produit les pages.
Ils ne sont *pas* nécessaires pour publier ni pour modifier le site — ils servent uniquement à régénérer
l’ensemble d’un coup après une modification du gabarit ou des données :

```sh
python3 tools/build.py
```

| Fichier | Rôle |
|---|---|
| `tools/layout.py` | Gabarit HTML commun : `<head>`, SEO, navigation, pied de page, données structurées |
| `tools/data_jeu.py` | Texte des sept chapitres et des six dénouements |
| `tools/data_partis.py` | Fiches des six partis francophones et des sept partis flamands |
| `tools/data_dossiers.py` | Texte des six dossiers thématiques |
| `tools/build_*.py` | Assemblage de chaque section |
| `tools/build.py` | Point d’entrée : régénère tout, plus `sitemap.xml`, `robots.txt`, `manifest.webmanifest` |

Les propositions de la boussole vivent dans `assets/js/data-boussole.js` : c’est la **source unique**.
Le tableau statique de la page `/boussole/` est relu depuis ce fichier au moment de la génération,
il ne peut donc pas diverger du questionnaire interactif.

## Structure

```
/                                   accueil, état des lieux d’août 2026
/jeu/                               présentation du parcours
/jeu/01-…-07-…/                     les sept chapitres
/jeu/fins/                          les six dénouements
/boussole/                          test électoral, 24 propositions
/partis/                            index + 6 fiches francophones + les partis flamands
/dossiers/                          index + 6 dossiers thématiques
/chronologie/                       juin 2024 → août 2026
/sondages/                          intentions de vote 2026
/glossaire/                         30 termes institutionnels
/a-propos/                          méthode, sources, limites
/assets/{css,js,img}/               une feuille de style, quatre scripts, les images
```

## Choix techniques

- **Pas de framework, pas de CDN, pas de police distante, pas de traceur.** Une seule feuille de style,
  quatre fichiers JavaScript, tous locaux.
- **Amélioration progressive.** Sans JavaScript, le jeu reste lisible (les conséquences des choix sont
  dans le HTML) et le tableau de la boussole reste consultable. Seuls le décompte des indicateurs et le
  questionnaire interactif nécessitent un script.
- **SEO et web sémantique.** Chaque page dispose d’un `title` et d’une `meta description` uniques,
  d’un `link rel=canonical`, de balises Open Graph et Twitter, d’un fil d’Ariane visible **et** en
  `BreadcrumbList` JSON-LD, et de données structurées adaptées à son type (`Article`, `Chapter`, `Game`,
  `Quiz`, `PoliticalParty`, `FAQPage`, `DefinedTermSet`, `ItemList`, `Dataset`).
- **Chaque page est un point d’entrée.** Aucune ne suppose la lecture d’une autre.
- **Accessibilité.** Structure sémantique, lien d’évitement, contrastes vérifiés, thème clair/sombre,
  `prefers-reduced-motion`, navigation au clavier, `aria-*` sur les composants interactifs.
- **Vie privée.** Progression du jeu et réponses de la boussole stockées dans le `localStorage` du
  navigateur, avec repli silencieux en mémoire si le stockage est refusé. Rien n’est transmis.

## Faits et fiction

La règle de fabrication est stricte et visible sur chaque page du parcours :

- encadré **« Ce qui est vrai »** → mesures adoptées, chiffres publiés, dates vérifiables, sources en bas de page ;
- encadré **« Fiction d’anticipation »** → récit inventé. Aucun propos n’est attribué à une personne réelle ;
- les six dénouements sont des **scénarios**, avec leur plausibilité et leurs précédents — pas des prédictions.

Données arrêtées au **18 août 2026**.

## Licence

Code sous licence MIT. Les textes sont publiés sous
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.fr) : réutilisez-les en citant la source
et en conservant la même licence.
