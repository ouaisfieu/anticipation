/*! Anticipation — app.js
 *  Navigation, thème, amélioration progressive.
 *  Aucune dépendance. Chargé avec `defer` sur toutes les pages.
 */
(function () {
  'use strict';
  document.documentElement.classList.add('js');

  /* ---- Stockage tolérant aux pannes (navigation privée, cookies bloqués) --- */
  var mem = {};
  var store = {
    get: function (k) {
      try { var v = localStorage.getItem(k); return v === null ? (k in mem ? mem[k] : null) : v; }
      catch (e) { return k in mem ? mem[k] : null; }
    },
    set: function (k, v) {
      mem[k] = v;
      try { localStorage.setItem(k, v); } catch (e) { /* silencieux */ }
    },
    del: function (k) {
      delete mem[k];
      try { localStorage.removeItem(k); } catch (e) { /* silencieux */ }
    }
  };
  window.ANTI = window.ANTI || {};
  window.ANTI.store = store;

  /* ---- Thème clair / sombre ---------------------------------------------- */
  var THEME_KEY = 'anti:theme';
  var saved = store.get(THEME_KEY);
  if (saved === 'clair' || saved === 'sombre') {
    document.documentElement.setAttribute('data-theme', saved);
  }
  function currentTheme() {
    var attr = document.documentElement.getAttribute('data-theme');
    if (attr) return attr;
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'sombre' : 'clair';
  }
  var themeBtn = document.querySelector('.theme-btn');
  function paintThemeBtn() {
    if (!themeBtn) return;
    var t = currentTheme();
    themeBtn.setAttribute('aria-label', t === 'sombre' ? 'Passer au thème clair' : 'Passer au thème sombre');
    themeBtn.setAttribute('title', themeBtn.getAttribute('aria-label'));
    themeBtn.textContent = t === 'sombre' ? '☀' : '☾';
  }
  if (themeBtn) {
    paintThemeBtn();
    themeBtn.addEventListener('click', function () {
      var next = currentTheme() === 'sombre' ? 'clair' : 'sombre';
      document.documentElement.setAttribute('data-theme', next);
      store.set(THEME_KEY, next);
      paintThemeBtn();
    });
  }

  /* ---- Menu mobile -------------------------------------------------------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('sitenav');
  if (toggle && nav) {
    toggle.setAttribute('aria-expanded', 'false');
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  /* ---- Sommaire latéral : surlignage de la section courante ---------------- */
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.side nav a[href^="#"]'));
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var targets = tocLinks.map(function (a) {
      return document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
    }).filter(Boolean);
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        tocLinks.forEach(function (a) { a.removeAttribute('aria-current'); });
        var match = tocLinks.filter(function (a) {
          return a.getAttribute('href') === '#' + en.target.id;
        })[0];
        if (match) match.setAttribute('aria-current', 'true');
      });
    }, { rootMargin: '-15% 0px -70% 0px', threshold: 0 });
    targets.forEach(function (t) { io.observe(t); });
  }

  /* ---- Année courante dans le pied de page -------------------------------- */
  var y = document.querySelector('[data-year]');
  if (y) y.textContent = String(new Date().getFullYear());
})();
