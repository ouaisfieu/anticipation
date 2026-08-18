/*! Anticipation — boussole.js
 *  Test électoral : 24 propositions, deux axes, six partis francophones.
 *  Les propositions et les positions des partis sont aussi rendues en HTML
 *  statique plus bas dans la page : le contenu reste lisible sans JavaScript.
 */
(function () {
  'use strict';
  var D = window.BOUSSOLE;
  var root = document.getElementById('boussole');
  if (!D || !root) return;

  var KEY = 'anti:boussole:v1';
  var store = (window.ANTI && window.ANTI.store) || {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
    del: function (k) { try { localStorage.removeItem(k); } catch (e) {} }
  };

  var LIKERT = [
    { v: +2, l: 'Tout à fait d’accord' },
    { v: +1, l: 'Plutôt d’accord' },
    { v:  0, l: 'Neutre / sans avis' },
    { v: -1, l: 'Plutôt pas d’accord' },
    { v: -2, l: 'Pas du tout d’accord' }
  ];

  var answers = [];
  try { answers = JSON.parse(store.get(KEY)) || []; } catch (e) { answers = []; }
  if (!Array.isArray(answers) || answers.length !== D.questions.length) {
    answers = D.questions.map(function () { return null; });
  }
  var i = 0;
  for (var k = 0; k < answers.length; k++) { if (answers[k] === null) { i = k; break; } i = k; }

  root.innerHTML =
    '<div class="quiz" role="group" aria-labelledby="q-text">' +
      '<div class="progress" role="presentation"><i></i></div>' +
      '<p class="q-theme"></p>' +
      '<p class="q-text" id="q-text"></p>' +
      '<ul class="likert"></ul>' +
      '<div class="quiz-foot">' +
        '<button type="button" data-prev>← Précédent</button>' +
        '<button type="button" data-next>Suivant →</button>' +
        '<span data-count></span>' +
        '<button type="button" data-skip>Passer</button>' +
        '<button type="button" data-clear>Recommencer</button>' +
      '</div>' +
    '</div>' +
    '<div id="resultat" hidden></div>';

  var quiz = root.querySelector('.quiz');
  var elTheme = root.querySelector('.q-theme');
  var elText = root.querySelector('.q-text');
  var elList = root.querySelector('.likert');
  var elBar = root.querySelector('.progress i');
  var elCount = root.querySelector('[data-count]');
  var elRes = root.querySelector('#resultat');

  LIKERT.forEach(function (opt) {
    var li = document.createElement('li');
    var b = document.createElement('button');
    b.type = 'button';
    b.innerHTML = '<span class="dot" aria-hidden="true"></span><span>' + opt.l + '</span>';
    b.setAttribute('aria-pressed', 'false');
    b.addEventListener('click', function () {
      answers[i] = opt.v;
      persist();
      if (i < D.questions.length - 1) { i++; render(); }
      else { render(); finish(); }
    });
    li.appendChild(b);
    elList.appendChild(li);
  });

  root.querySelector('[data-prev]').addEventListener('click', function () { if (i > 0) { i--; render(); } });
  root.querySelector('[data-next]').addEventListener('click', function () {
    if (i < D.questions.length - 1) { i++; render(); } else { finish(); }
  });
  root.querySelector('[data-skip]').addEventListener('click', function () {
    answers[i] = 0; persist();
    if (i < D.questions.length - 1) { i++; render(); } else { finish(); }
  });
  root.querySelector('[data-clear]').addEventListener('click', function () {
    answers = D.questions.map(function () { return null; });
    store.del(KEY); i = 0; elRes.hidden = true; elRes.innerHTML = ''; quiz.hidden = false; render();
  });

  function persist() { store.set(KEY, JSON.stringify(answers)); }

  function render() {
    var q = D.questions[i];
    elTheme.textContent = q.t;
    elText.textContent = q.q;
    Array.prototype.forEach.call(elList.querySelectorAll('button'), function (b, n) {
      b.setAttribute('aria-pressed', answers[i] === LIKERT[n].v ? 'true' : 'false');
    });
    var done = answers.filter(function (a) { return a !== null; }).length;
    elBar.style.width = ((i) / (D.questions.length - 1) * 100) + '%';
    elCount.textContent = 'Question ' + (i + 1) + ' sur ' + D.questions.length + ' — ' + done + ' répondue' + (done > 1 ? 's' : '');
    root.querySelector('[data-prev]').disabled = (i === 0);
    root.querySelector('[data-next]').textContent = (i === D.questions.length - 1) ? 'Voir le résultat' : 'Suivant →';
  }

  function finish() {
    var answered = answers.filter(function (a) { return a !== null; }).length;
    if (answered < 5) {
      elRes.hidden = false;
      elRes.innerHTML = '<div class="callout warn"><p class="t">Trop peu de réponses</p><p class="mb0">Répondez à au moins cinq propositions pour obtenir un positionnement lisible.</p></div>';
      return;
    }
    var eco = 0, ecoMax = 0, gal = 0, galMax = 0;
    var score = {}, weight = {};
    D.partis.forEach(function (p) { score[p.id] = 0; weight[p.id] = 0; });

    D.questions.forEach(function (q, n) {
      var a = answers[n];
      if (a === null) return;
      eco += a * q.eco; ecoMax += Math.abs(q.eco) * 2;
      gal += a * q.gal; galMax += Math.abs(q.gal) * 2;
      D.partis.forEach(function (p) {
        var pos = q.p[p.id];
        if (typeof pos !== 'number') return;
        score[p.id] += 1 - Math.abs(a - pos) / 4;
        weight[p.id] += 1;
      });
    });

    var X = ecoMax ? Math.max(-1, Math.min(1, eco / ecoMax)) : 0;
    var Y = galMax ? Math.max(-1, Math.min(1, gal / galMax)) : 0;

    var ranked = D.partis.map(function (p) {
      return { p: p, pct: weight[p.id] ? Math.round(score[p.id] / weight[p.id] * 100) : 0 };
    }).sort(function (a, b) { return b.pct - a.pct; });

    var quadrant = describe(X, Y);
    elRes.hidden = false;
    quiz.hidden = false;
    elRes.innerHTML =
      '<h2 id="votre-resultat" style="margin-top:2.4rem">Votre positionnement</h2>' +
      '<p>Sur ' + answered + ' propositions, votre profil se situe <strong>' + quadrant.label + '</strong>. ' + quadrant.text + '</p>' +
      svg(X, Y, ranked) +
      '<h3>Proximité avec les six partis francophones</h3>' +
      '<ul class="matchlist">' + ranked.map(function (r) {
        return '<li class="' + r.p.cls + '"><a href="' + r.p.url + '">' + r.p.nom + '</a>' +
               '<span class="bar"><i style="width:' + r.pct + '%"></i></span>' +
               '<span class="pct">' + r.pct + '%</span></li>';
      }).join('') + '</ul>' +
      '<div class="callout"><p class="t">À lire avant de conclure</p>' +
      '<p class="mb0">Un pourcentage élevé ne signifie pas « votez pour ce parti ». Il mesure une distance moyenne sur 24 propositions, ' +
      'sans pondérer l’intensité de vos préférences ni les compromis que les partis acceptent une fois en coalition — ' +
      'l’angle mort documenté de tous les systèmes d’aide au vote. ' +
      '<a href="../a-propos/#methode">Notre méthode et ses limites</a>.</p></div>' +
      '<div class="btnrow"><a class="btn" href="../jeu/">Jouer le parcours narratif</a>' +
      '<a class="btn ghost" href="../partis/">Comparer les programmes</a></div>';

    if (location.hash !== '#votre-resultat') {
      document.getElementById('votre-resultat').scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  function describe(X, Y) {
    var eco = X > .18 ? 'à droite sur l’axe socio-économique' : (X < -.18 ? 'à gauche sur l’axe socio-économique' : 'au centre de l’axe socio-économique');
    var cul = Y > .18 ? 'du côté conservateur/national (TAN)' : (Y < -.18 ? 'du côté progressiste/écologiste (GAL)' : 'au milieu de l’axe culturel');
    var t = 'L’axe horizontal oppose redistribution et intervention publique (à gauche) à la logique de marché et d’activation (à droite). ' +
            'L’axe vertical oppose les valeurs vertes, alternatives et libertaires (en bas) aux valeurs traditionnelles, autoritaires et nationales (en haut).';
    return { label: eco + ' et ' + cul, text: t };
  }

  function svg(X, Y, ranked) {
    var S = 320, C = S / 2, R = C - 26;
    var px = C + X * R, py = C - Y * R;
    var dots = D.partis.map(function (p) {
      var e = 0, em = 0, g = 0, gm = 0;
      D.questions.forEach(function (q) {
        var pos = q.p[p.id];
        e += pos * q.eco; em += Math.abs(q.eco) * 2;
        g += pos * q.gal; gm += Math.abs(q.gal) * 2;
      });
      var x = C + Math.max(-1, Math.min(1, e / em)) * R;
      var y = C - Math.max(-1, Math.min(1, g / gm)) * R;
      return '<g><circle cx="' + x.toFixed(1) + '" cy="' + y.toFixed(1) + '" r="5.5" class="' + p.cls + '" fill="var(--c)" fill-opacity=".9" stroke="var(--paper-2)" stroke-width="1.5"/>' +
             '<text x="' + (x + 9).toFixed(1) + '" y="' + (y + 4).toFixed(1) + '" font-size="10.5" font-weight="600" ' +
             'stroke="var(--paper-2)" stroke-width="3" paint-order="stroke" fill="currentColor">' + p.nom + '</text></g>';
    }).join('');
    return '<svg class="compass" viewBox="0 0 ' + S + ' ' + S + '" role="img" ' +
      'aria-label="Diagramme à deux axes : votre position et celle des six partis francophones.">' +
      '<rect x="0" y="0" width="' + S + '" height="' + S + '" fill="none"/>' +
      '<line x1="18" y1="' + C + '" x2="' + (S - 18) + '" y2="' + C + '" stroke="currentColor" stroke-opacity=".22"/>' +
      '<line x1="' + C + '" y1="18" x2="' + C + '" y2="' + (S - 18) + '" stroke="currentColor" stroke-opacity=".22"/>' +
      '<text x="20" y="' + (C - 8) + '" font-size="9.5" fill="currentColor" fill-opacity=".55">redistribution</text>' +
      '<text x="' + (S - 20) + '" y="' + (C - 8) + '" font-size="9.5" text-anchor="end" fill="currentColor" fill-opacity=".55">marché</text>' +
      '<text x="' + (C + 6) + '" y="26" font-size="9.5" fill="currentColor" fill-opacity=".55">TAN</text>' +
      '<text x="' + (C + 6) + '" y="' + (S - 16) + '" font-size="9.5" fill="currentColor" fill-opacity=".55">GAL</text>' +
      dots +
      '<circle cx="' + px.toFixed(1) + '" cy="' + py.toFixed(1) + '" r="9.5" fill="var(--paper-2)" fill-opacity=".6" stroke="currentColor" stroke-width="2.5"/>' +
      '<circle cx="' + px.toFixed(1) + '" cy="' + py.toFixed(1) + '" r="3" fill="currentColor"/>' +
      '<text x="' + (px + 13).toFixed(1) + '" y="' + (py - 11).toFixed(1) + '" font-size="11" font-weight="700" ' +
      'stroke="var(--paper-2)" stroke-width="3.5" paint-order="stroke" fill="currentColor">vous</text>' +
      '</svg>';
  }

  render();
  if (answers.every(function (a) { return a !== null; })) finish();
})();
