/*! Anticipation — jeu.js
 *  Moteur d’état du parcours narratif « Le compte à rebours ».
 *
 *  Principe : chaque chapitre est une VRAIE page HTML. Les textes de
 *  conséquence sont présents dans le document (donc indexables et lisibles
 *  sans JavaScript) ; ce script se contente de les masquer, de les révéler
 *  au clic et de tenir les compteurs. Sans JS, la page reste un texte complet.
 */
(function () {
  'use strict';

  var KEY = 'anti:jeu:v1';
  var store = (window.ANTI && window.ANTI.store) || {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
    del: function (k) { try { localStorage.removeItem(k); } catch (e) {} }
  };

  var CH_ORDER = ['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7'];
  function CLAMP(n) { return Math.max(0, Math.min(100, Math.round(n))); }
  function blank() { return { cred: 50, soc: 50, stab: 50, tension: 0, picks: {} }; }

  function load() {
    var raw = store.get(KEY);
    if (!raw) return blank();
    try {
      var s = JSON.parse(raw);
      if (!s || typeof s !== 'object' || !s.picks) return blank();
      s.cred = CLAMP(s.cred); s.soc = CLAMP(s.soc); s.stab = CLAMP(s.stab);
      s.tension = Number(s.tension) || 0;
      return s;
    } catch (e) { return blank(); }
  }
  function save(s) { store.set(KEY, JSON.stringify(s)); }

  /* Effets déclarés en HTML : data-eff="cred:+8,soc:-5,stab:-2,tension:+2" */
  function parseEff(str) {
    var out = {};
    (str || '').split(',').forEach(function (part) {
      var kv = part.split(':');
      if (kv.length !== 2) return;
      var k = kv[0].trim(), v = parseFloat(kv[1]);
      if (!isNaN(v)) out[k] = v;
    });
    return out;
  }
  function apply(state, eff, sign) {
    ['cred', 'soc', 'stab'].forEach(function (k) {
      if (eff[k]) state[k] = CLAMP(state[k] + sign * eff[k]);
    });
    if (eff.tension) state.tension += sign * eff.tension;
    return state;
  }

  function tensionLabel(t) {
    if (t <= 1) return 'Législature stable';
    if (t <= 3) return 'Turbulences';
    if (t <= 5) return 'Crise ouverte';
    if (t <= 7) return 'Rupture probable';
    return 'Dissolution imminente';
  }

  /* Arbre de décision : le premier test satisfait l’emporte. */
  function resolveEnding(s) {
    if (s.soc <= 38 && s.tension >= 5) return 'fin-recomposition';
    if (s.stab <= 38) return 'fin-institutionnelle';
    if (s.tension >= 6 && s.stab <= 48) return 'fin-affaires-courantes';
    if (s.cred >= 64 && s.stab >= 50) return 'fin-gouvernement-de-mission';
    if (s.tension >= 5) return 'fin-anticipees';
    return 'fin-legislature';
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function tag(label, v) {
    return '<li><span class="tag">' + escapeHtml(label) + ' : ' + v + '/100</span></li>';
  }

  var state = load();

  /* ---- Bandeau de jauges (HUD) -------------------------------------------- */
  function paintHud() {
    Array.prototype.forEach.call(document.querySelectorAll('.hud .gauge'), function (g) {
      var k = g.getAttribute('data-k');
      if (k !== 'cred' && k !== 'soc' && k !== 'stab') return;
      var v = state[k];
      var fill = g.querySelector('.fill');
      var out = g.querySelector('b');
      if (fill) fill.style.width = v + '%';
      if (out) out.textContent = v;
      g.setAttribute('aria-valuenow', String(v));
    });
    var clock = document.querySelector('.hud .clock');
    if (clock) clock.textContent = tensionLabel(state.tension);
    var done = document.querySelector('.hud [data-done]');
    if (done) {
      var n = CH_ORDER.filter(function (c) { return state.picks[c]; }).length;
      done.textContent = n + '/7';
    }
  }

  /* ---- Chapitres ---------------------------------------------------------- */
  var game = document.querySelector('[data-chapter]');
  if (game) {
    var chId = game.getAttribute('data-chapter');
    var choices = Array.prototype.slice.call(game.querySelectorAll('.choice'));
    var nextBtn = game.querySelector('[data-next]');

    choices.forEach(function (li) {
      var cons = li.querySelector('.consequence');
      if (cons) cons.hidden = true;
      var btn = li.querySelector('.pick');
      if (btn) { btn.setAttribute('type', 'button'); btn.setAttribute('aria-expanded', 'false'); }
    });
    if (nextBtn) nextBtn.setAttribute('disabled', 'disabled');

    var select = function (li, isRestore) {
      var id = li.getAttribute('data-id');
      var prev = state.picks[chId];
      if (prev === id && !isRestore) return;
      if (!isRestore) {
        if (prev) {
          var prevLi = choices.filter(function (x) { return x.getAttribute('data-id') === prev; })[0];
          if (prevLi) apply(state, parseEff(prevLi.getAttribute('data-eff')), -1);
        }
        apply(state, parseEff(li.getAttribute('data-eff')), 1);
        state.picks[chId] = id;
        save(state);
      }
      choices.forEach(function (x) {
        var on = x === li;
        x.setAttribute('data-picked', on ? '1' : '0');
        var c = x.querySelector('.consequence');
        if (c) c.hidden = !on;
        var b = x.querySelector('.pick');
        if (b) b.setAttribute('aria-expanded', on ? 'true' : 'false');
      });
      if (nextBtn) nextBtn.removeAttribute('disabled');
      paintHud();
    };

    choices.forEach(function (li) {
      var btn = li.querySelector('.pick');
      if (!btn) return;
      btn.addEventListener('click', function () { select(li, false); });
    });

    var restore = state.picks[chId];
    if (restore) {
      var li0 = choices.filter(function (x) { return x.getAttribute('data-id') === restore; })[0];
      if (li0) select(li0, true);
    }
  }

  /* ---- Remise à zéro ------------------------------------------------------ */
  Array.prototype.forEach.call(document.querySelectorAll('[data-reset]'), function (b) {
    b.addEventListener('click', function () {
      if (!window.confirm('Effacer votre partie et repartir de zéro ?')) return;
      state = blank();
      store.del(KEY);
      window.location.reload();
    });
  });

  /* ---- Page des fins ------------------------------------------------------ */
  var fins = document.querySelector('[data-endings]');
  if (fins) {
    var answered = CH_ORDER.filter(function (c) { return state.picks[c]; }).length;
    var box = document.querySelector('[data-verdict]');
    if (answered === 0) {
      if (box) {
        box.innerHTML = '<p class="t">Aucune partie en cours</p><p class="mb0">Les six dénouements ci-dessous sont tous décrits, ' +
          'avec leur degré de plausibilité institutionnelle. ' +
          '<a href="../01-le-comite-de-monitoring/">Commencez le parcours</a> pour découvrir lequel votre partie déclenche.</p>';
      }
    } else {
      var slug = resolveEnding(state);
      var target = document.getElementById(slug);
      if (target) target.setAttribute('data-active', '1');
      if (box) {
        var titre = target ? target.querySelector('h3').textContent : 'Dénouement';
        box.innerHTML =
          '<p class="t">Résultat de votre partie</p>' +
          '<p><strong>' + escapeHtml(titre) + '</strong> — ' + answered +
          ' chapitre' + (answered > 1 ? 's' : '') + ' sur 7 joué' + (answered > 1 ? 's' : '') + '.</p>' +
          '<ul class="taglist">' + tag('Crédibilité', state.cred) + tag('Cohésion sociale', state.soc) +
          tag('Stabilité institutionnelle', state.stab) +
          '<li><span class="tag">Tension : ' + escapeHtml(tensionLabel(state.tension)) + '</span></li></ul>' +
          (answered < 7
            ? '<p class="muted mb0">Partie incomplète : le dénouement se recalcule après chaque chapitre.</p>'
            : '<p class="muted mb0">Partie complète. Rejouez en ne changeant qu’un seul choix pour mesurer son poids.</p>') +
          '<p class="mb0" style="margin-top:1rem"><a class="btn" href="#' + slug + '">Lire ce dénouement</a></p>';
      }
    }
  }

  paintHud();
  window.ANTI = window.ANTI || {};
  window.ANTI.jeu = { state: function () { return state; }, reset: function () { store.del(KEY); } };
})();
