/* Glycodex – kleine Laufzeit für die Seitenvorlagen.
   Versteht {{platzhalter}}, <sc-if>, <sc-for>, ref und on*-Ereignisse.
   Die Seite wird einmal aufgebaut, danach werden nur geänderte Stellen aktualisiert. */
(function () {
  'use strict';
  var HOLE = /\{\{\s*([^}]+?)\s*\}\}/g;
  var ONE = /^\s*\{\{\s*([^}]+?)\s*\}\}\s*$/;

  function lookup(path, scope) {
    path = path.trim();
    if (path === 'true') return true;
    if (path === 'false') return false;
    var v = scope;
    var parts = path.split('.');
    for (var i = 0; i < parts.length; i++) {
      if (v == null) return undefined;
      v = v[parts[i]];
    }
    return v;
  }
  function str(v) { return v == null || typeof v === 'function' ? '' : String(v); }
  function fill(s, scope) { return s.replace(HOLE, function (m, p) { return str(lookup(p, scope)); }); }
  function holePath(s) { var m = ONE.exec(s || ''); return m ? m[1] : null; }

  // Ein Block ist eine Menge von Bindungen, die gemeinsam aktualisiert und entfernt werden.
  function Block() { this.items = []; this.refs = []; }
  Block.prototype.update = function (scope) { for (var i = 0; i < this.items.length; i++) this.items[i](scope); };
  Block.prototype.destroy = function () {
    for (var i = 0; i < this.refs.length; i++) { try { this.refs[i](null); } catch (e) {} }
    for (var j = 0; j < this.items.length; j++) { if (this.items[j].destroy) this.items[j].destroy(); }
  };

  function compileChildren(parent, block, getScope) {
    var kids = Array.prototype.slice.call(parent.childNodes);
    for (var i = 0; i < kids.length; i++) compile(kids[i], block, getScope);
  }

  function compile(node, block, getScope) {
    if (node.nodeType === 3) {
      if (node.nodeValue.indexOf('{{') < 0) return;
      var tpl = node.nodeValue, last = null;
      block.items.push(function (scope) {
        var v = fill(tpl, scope);
        if (v !== last) { node.nodeValue = v; last = v; }
      });
      return;
    }
    if (node.nodeType !== 1) return;
    var tag = node.tagName.toLowerCase();
    if (tag === 'sc-if') return compileIf(node, block);
    if (tag === 'sc-for') return compileFor(node, block);

    var attrs = Array.prototype.slice.call(node.attributes);
    for (var a = 0; a < attrs.length; a++) {
      var name = attrs[a].name, val = attrs[a].value;
      if (name.indexOf('hint-') === 0) { node.removeAttribute(name); continue; }
      if (/^on[a-z]/i.test(name)) {
        node.removeAttribute(name);
        bindEvent(node, name.slice(2).toLowerCase(), holePath(val), block, getScope);
        continue;
      }
      if (name === 'ref') {
        node.removeAttribute(name);
        bindRef(node, holePath(val), block, getScope);
        continue;
      }
      if (val.indexOf('{{') >= 0) bindAttr(node, name, val, block);
    }
    compileChildren(node, block, getScope);
  }

  function bindAttr(el, name, tpl, block) {
    var last = null;
    el.removeAttribute(name);
    block.items.push(function (scope) {
      var v = fill(tpl, scope);
      if (v === last) return;
      last = v;
      el.setAttribute(name, v);
    });
  }

  function bindEvent(el, type, path, block, getScope) {
    if (!path) return;
    el.addEventListener(type, function (e) {
      var fn = lookup(path, getScope());
      if (typeof fn === 'function') fn(e);
    });
  }

  function bindRef(el, path, block, getScope) {
    if (!path) return;
    var done = false, fn = null;
    var item = function (scope) {
      if (done) return;
      done = true;
      fn = lookup(path, scope);
      if (typeof fn === 'function') {
        // erst nach dem Einhängen ins Dokument aufrufen
        Promise.resolve().then(function () { if (el.isConnected) fn(el); });
      }
    };
    block.items.push(item);
    block.refs.push(function (x) { if (typeof fn === 'function') fn(x); });
  }

  function compileIf(node, block) {
    var path = holePath(node.getAttribute('value')) || 'false';
    var anchor = document.createComment('if');
    var content = document.createDocumentFragment();
    while (node.firstChild) content.appendChild(node.firstChild);
    node.parentNode.replaceChild(anchor, node);
    var mounted = null, nodes = [], scopeNow = null;
    var getScope = function () { return scopeNow; };
    var item = function (scope) {
      scopeNow = scope;
      var on = !!lookup(path, scope);
      if (on && !mounted) {
        var frag = content.cloneNode(true);
        mounted = new Block();
        nodes = Array.prototype.slice.call(frag.childNodes);
        var box = document.createElement('div');
        box.appendChild(frag);
        compileChildren(box, mounted, getScope);
        nodes = Array.prototype.slice.call(box.childNodes);
        var ref = anchor.nextSibling;
        for (var i = 0; i < nodes.length; i++) anchor.parentNode.insertBefore(nodes[i], ref);
        mounted.update(scope);
      } else if (!on && mounted) {
        mounted.destroy();
        for (var j = 0; j < nodes.length; j++) if (nodes[j].parentNode) nodes[j].parentNode.removeChild(nodes[j]);
        mounted = null; nodes = [];
      } else if (mounted) {
        mounted.update(scope);
      }
    };
    item.destroy = function () { if (mounted) mounted.destroy(); };
    block.items.push(item);
  }

  function compileFor(node, block) {
    var path = holePath(node.getAttribute('list')) || '';
    var as = node.getAttribute('as') || 'item';
    var anchor = document.createComment('for');
    var content = document.createDocumentFragment();
    while (node.firstChild) content.appendChild(node.firstChild);
    node.parentNode.replaceChild(anchor, node);
    var rows = [];
    var item = function (scope) {
      var list = lookup(path, scope) || [];
      while (rows.length > list.length) {
        var r = rows.pop();
        r.block.destroy();
        r.nodes.forEach(function (n) { if (n.parentNode) n.parentNode.removeChild(n); });
      }
      for (var i = 0; i < list.length; i++) {
        var sc = Object.create(scope);
        sc[as] = list[i];
        sc.$index = i;
        if (!rows[i]) {
          var row = { block: new Block(), nodes: [], scope: sc };
          (function (row) {
            var box = document.createElement('div');
            box.appendChild(content.cloneNode(true));
            compileChildren(box, row.block, function () { return row.scope; });
            row.nodes = Array.prototype.slice.call(box.childNodes);
          })(row);
          var after = i === 0 ? anchor : rows[i - 1].nodes[rows[i - 1].nodes.length - 1] || anchor;
          var ref = after.nextSibling;
          row.nodes.forEach(function (n) { anchor.parentNode.insertBefore(n, ref); });
          rows[i] = row;
        }
        rows[i].scope = sc;
        rows[i].block.update(sc);
      }
    };
    item.destroy = function () { rows.forEach(function (r) { r.block.destroy(); }); };
    block.items.push(item);
  }

  function DCLogic() { this.state = null; this.props = {}; }
  DCLogic.prototype.setState = function (o) {
    this.state = Object.assign({}, this.state || {}, typeof o === 'function' ? o(this.state || {}) : o);
    if (this.__schedule) this.__schedule();
  };
  DCLogic.prototype.forceUpdate = function () { if (this.__schedule) this.__schedule(); };

  function mount(Component, opts) {
    opts = opts || {};
    var tpl = document.getElementById('gx-tpl');
    var host = document.getElementById('gx-app');
    var comp = new Component();
    var vals = null, pending = false;
    var root = new Block();
    var box = document.createElement('div');
    box.appendChild(tpl.content.cloneNode(true));
    compileChildren(box, root, function () { return vals; });
    function render() {
      pending = false;
      vals = comp.renderVals();
      root.update(vals);
    }
    comp.__schedule = function () {
      if (pending) return;
      pending = true;
      Promise.resolve().then(render);
    };
    vals = comp.renderVals();
    root.update(vals);
    host.innerHTML = '';
    while (box.firstChild) host.appendChild(box.firstChild);
    if (!opts.prerender && typeof comp.componentDidMount === 'function') comp.componentDidMount();
    document.documentElement.setAttribute('data-gx', opts.prerender ? 'pre' : 'live');
    return comp;
  }

  window.DCLogic = DCLogic;
  window.GX = { mount: mount };
})();
