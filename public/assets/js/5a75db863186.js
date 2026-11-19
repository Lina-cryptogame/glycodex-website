class Component extends DCLogic {
componentDidMount() {
let t = null;
try { t = window.localStorage.getItem('glycodex-theme'); } catch (e) {}
this.setState({ ready: true, theme: (t === 'light' || t === 'dark') ? t : 'auto' });
try {
this._mq = window.matchMedia('(prefers-color-scheme: dark)');
this._mqh = () => this.forceUpdate();
this._mq.addEventListener('change', this._mqh);
} catch (e) {}
this._timer = setTimeout(() => this.observe(), 30);
}
componentWillUnmount() {
try { if (this._mq) this._mq.removeEventListener('change', this._mqh); } catch (e) {}
if (this._io) this._io.disconnect();
clearTimeout(this._timer);
}
observe() {
const root = this._root;
if (!root) return;
const els = Array.prototype.slice.call(root.querySelectorAll('.rv'));
if (!('IntersectionObserver' in window)) { els.forEach((el) => el.classList.add('in')); return; }
this._io = new IntersectionObserver((entries) => {
entries.forEach((en) => {
if (en.isIntersecting) { en.target.classList.add('in'); this._io.unobserve(en.target); }
});
}, { threshold: 0.12 });
els.forEach((el) => this._io.observe(el));
}
bmLib() {
if (this._bmLib) return this._bmLib;
// Übernommen aus der Glycodex-App (Körperkarte, Bauch und Oberarm, 360° drehbar), mit erfundenen Testdaten.
const rad = (d) => d * Math.PI / 180, deg = (r) => r * 180 / Math.PI;
const normDeg = (d) => ((d + 180) % 360 + 360) % 360 - 180;
const fx = (n) => n.toFixed(1);
const f1 = (n) => n.toFixed(1).replace('.', ',');
const MODELS = {
belly: { top: 46, h: 210, k: 0.22, Hcm: 30, br: 0.7, a: (y) => 104 * (0.98 - 0.13 * Math.exp(-(((y - 0.32) / 0.24) ** 2)) + 0.12 * y * y), circ: 90, refY: 0.35, navel: { p: 0, y: 0.67 } },
arm: { top: 34, h: 236, k: 0.16, Hcm: 22, br: 0.92, a: (y) => 50 * (1.12 - 0.3 * y + 0.08 * Math.sin(Math.PI * y)), circ: 30, refY: 0.5 }
};
const CX = 160;
const proj = (M, p, y, th) => {
const a = M.a(y), b = a * M.br, px = a * Math.sin(rad(p)), pz = b * Math.cos(rad(p)), t = rad(th);
const X = px * Math.cos(t) - pz * Math.sin(t), Z = px * Math.sin(t) + pz * Math.cos(t);
return { x: CX + X, y: M.top + y * M.h + M.k * Z, z: Z };
};
const inv = (M, sx, sy, th) => {
let y = (sy - M.top) / M.h, p = 0;
for (let it = 0; it < 4; it++) {
const yc = Math.max(0, Math.min(1, y)), a = M.a(yc), b = a * M.br, t = rad(th);
const R = Math.hypot(a * Math.cos(t), b * Math.sin(t)), d = Math.atan2(b * Math.sin(t), a * Math.cos(t)), u = (sx - CX) / R;
if (Math.abs(u) > 1) return null;
const c1 = deg(d + Math.asin(u)), c2 = deg(d + Math.PI - Math.asin(u));
p = proj(M, c1, yc, th).z >= proj(M, c2, yc, th).z ? c1 : c2;
y = (sy - M.top - M.k * proj(M, p, yc, th).z) / M.h;
}
if (y < -0.02 || y > 1.02) return null;
return { p: Math.round(normDeg(p)), y: Math.round(Math.max(0, Math.min(1, y)) * 100) / 100 };
};
const perim = (M, y) => { const a = M.a(y), b = a * M.br; return 2 * Math.PI * Math.sqrt((a * a + b * b) / 2); };
const cmPerDeg = (M, y) => M.circ * (perim(M, y) / perim(M, M.refY)) / 360;
const siteDist = (s1, s2) => {
if ((s1.m || 'belly') !== (s2.m || 'belly') || (s1.limb || '') !== (s2.limb || '')) return Infinity;
const M = MODELS[s1.m || 'belly'], y = (s1.y + s2.y) / 2;
return Math.hypot(Math.abs(normDeg(s1.p - s2.p)) * cmPerDeg(M, y), Math.abs(s1.y - s2.y) * M.Hcm);
};
const siteName = (s) => {
const p = s.p, ap = Math.abs(p), lvl = s.y < 0.34 ? 'oben' : s.y < 0.67 ? 'Mitte' : 'unten';
if (s.m === 'arm') {
const L = s.limb === 'R' ? 'rechts' : 'links', outer = s.limb === 'R' ? p < 0 : p > 0;
const face = ap >= 120 ? 'hinten' : ap <= 60 ? 'vorne' : outer ? 'außen' : 'innen';
return 'Oberarm ' + L + ' ' + face + (lvl === 'Mitte' ? '' : ', ' + lvl);
}
const side = p > 0 ? 'links' : 'rechts', sfx = lvl === 'Mitte' ? '' : ' ' + lvl;
if (ap <= 22) return 'Bauchmitte' + sfx;
if (ap <= 68) return 'Bauch ' + side + sfx;
if (ap <= 112) return 'Flanke ' + side + sfx;
if (ap <= 162) return s.y >= 0.6 ? 'Po oben ' + side : 'Rücken ' + side + sfx;
return 'Rückenmitte';
};
// Erfundene Testdaten: Alter in Tagen
const SITES = [
{ kind: 'cath', m: 'belly', limb: '', p: 38, y: 0.62, age: 1 },
{ kind: 'cath', m: 'belly', limb: '', p: -46, y: 0.56, age: 4 },
{ kind: 'cath', m: 'belly', limb: '', p: 72, y: 0.76, age: 7 },
{ kind: 'cath', m: 'belly', limb: '', p: -30, y: 0.82, age: 10 },
{ kind: 'cath', m: 'belly', limb: '', p: -78, y: 0.7, age: 16 },
{ kind: 'cath', m: 'belly', limb: '', p: 56, y: 0.42, age: 22 },
{ kind: 'sensor', m: 'belly', limb: '', p: -104, y: 0.46, age: 3 },
{ kind: 'sensor', m: 'arm', limb: 'L', p: 168, y: 0.46, age: 2 },
{ kind: 'sensor', m: 'arm', limb: 'L', p: -158, y: 0.6, age: 12 },
{ kind: 'sensor', m: 'arm', limb: 'L', p: 146, y: 0.34, age: 24 },
{ kind: 'sensor', m: 'arm', limb: 'R', p: -170, y: 0.5, age: 6 },
{ kind: 'sensor', m: 'arm', limb: 'R', p: 150, y: 0.64, age: 18 }
];
const SITE_MIN = 3, NAVEL_CM = 5, SITE_DAYS = 30;
const KC = { cath: '#0e7490', sensor: '#7c3aed' }, KN = { cath: 'Katheter', sensor: 'Sensor' };
const same = (h, s) => h.m === s.m && (h.limb || '') === (s.limb || '');
const check = (kind, s) => {
const hist = SITES.filter((h) => h.age <= SITE_DAYS && same(h, s)), out = [];
const near = hist.filter((h) => h.kind === kind).map((h) => ({ h, d: siteDist(h, s) })).sort((a, b) => a.d - b.d)[0];
if (near && near.d < SITE_MIN) out.push('Nur ' + f1(near.d) + ' cm von der Stelle vor ' + near.h.age + (near.h.age === 1 ? ' Tag' : ' Tagen') + ' entfernt.');
const other = kind === 'cath' ? 'sensor' : 'cath';
const act = hist.filter((h) => h.kind === other && h.age <= (other === 'cath' ? 4 : 11)).map((h) => ({ h, d: siteDist(h, s) })).sort((a, b) => a.d - b.d)[0];
if (act && act.d < 5) out.push('Nah an deinem aktuellen ' + KN[other] + ' (' + f1(act.d) + ' cm).');
if (s.m === 'belly') {
const nv = siteDist({ m: 'belly', limb: '', p: 0, y: 0.67 }, s);
if (nv < NAVEL_CM) out.push('Nah am Bauchnabel (' + f1(nv) + ' cm).');
if (Math.abs(s.p) > 162) out.push('Direkt an der Wirbelsäule.');
}
return { warn: out, near: near };
};
const suggest = (kind, m, limb) => {
const spot = { m: m, limb: limb };
const hist = SITES.filter((h) => h.age <= SITE_DAYS && same(h, spot));
const mine = hist.filter((h) => h.kind === kind);
if (!mine.length) return null;
const other = hist.filter((h) => h.kind !== kind && h.age <= 11);
const isArm = m === 'arm', span = isArm ? 180 : Math.min(160, Math.max(75, ...mine.map((h) => Math.abs(h.p) + 20)));
let best = null;
for (let p = -span; p <= span; p += 5) for (let y = isArm ? 0.25 : 0.2; y <= (isArm ? 0.8 : 0.92); y += 0.04) {
if (isArm && Math.abs(p) < 115) continue;
const s = { m: m, limb: limb, p: p, y: Math.round(y * 100) / 100 };
if (!isArm && siteDist({ m: 'belly', limb: '', p: 0, y: 0.67 }, s) < NAVEL_CM + 1) continue;
const mm = Math.min(...mine.map((h) => siteDist(h, s) + h.age * 0.6)), o = other.length ? Math.min(...other.map((h) => siteDist(h, s))) : 99;
if (o < 5) continue;
const sc = Math.min(mm, 10) - (isArm ? Math.abs(180 - Math.abs(p)) * 0.03 + Math.abs(s.y - 0.5) * 2 : Math.abs(p) * 0.03 + Math.abs(s.y - 0.6) * 2);
if (!best || sc > best.sc) best = Object.assign({}, s, { sc: sc });
}
return best;
};
const viewName = (th) => { const a = normDeg(th); return Math.abs(a) <= 30 ? 'Vorne' : Math.abs(a) >= 150 ? 'Hinten' : a > 0 ? 'Linke Seite' : 'Rechte Seite'; };
const ellD = (cx, cy, rx, ry) => 'M' + fx(cx - rx) + ' ' + fx(cy) + 'A' + fx(rx) + ' ' + fx(ry) + ' 0 1 0 ' + fx(cx + rx) + ' ' + fx(cy) + 'A' + fx(rx) + ' ' + fx(ry) + ' 0 1 0 ' + fx(cx - rx) + ' ' + fx(cy) + 'Z';
const rrD = (x, y, w, h, r) => {
r = Math.min(r, w / 2, h / 2);
return 'M' + fx(x + r) + ' ' + fx(y) + 'H' + fx(x + w - r) + 'A' + fx(r) + ' ' + fx(r) + ' 0 0 1 ' + fx(x + w) + ' ' + fx(y + r) + 'V' + fx(y + h - r) + 'A' + fx(r) + ' ' + fx(r) + ' 0 0 1 ' + fx(x + w - r) + ' ' + fx(y + h) + 'H' + fx(x + r) + 'A' + fx(r) + ' ' + fx(r) + ' 0 0 1 ' + fx(x) + ' ' + fx(y + h - r) + 'V' + fx(y + r) + 'A' + fx(r) + ' ' + fx(r) + ' 0 0 1 ' + fx(x + r) + ' ' + fx(y) + 'Z';
};
const render = (mName, limb, th, sel, kind) => {
const M = MODELS[mName], P = (p, y) => proj(M, p, y, th), ys = [];
for (let y = 0; y <= 1.0001; y += 0.05) ys.push(Math.round(y * 100) / 100);
const edge = (y, s) => { const a = M.a(y), b = a * M.br, t = rad(th), d = Math.atan2(b * Math.sin(t), a * Math.cos(t)); return P(deg(d + s * Math.PI / 2), y); };
const arc = (y, front) => { const pts = []; for (let p = -180; p <= 180; p += 6) { const q = P(p, y); if (front ? q.z >= 0 : q.z <= 0) pts.push(q); } return pts.sort((a, b) => a.x - b.x); };
const R = ys.map((y) => edge(y, 1)), L = ys.map((y) => edge(y, -1));
const outline = [].concat(R, arc(1, true).reverse(), L.slice().reverse(), arc(0, false)).map((q, i) => (i ? 'L' : 'M') + fx(q.x) + ' ' + fx(q.y)).join('') + 'Z';
const line = (pts) => { let d = '', on = false; for (const pr of pts) { const q = P(pr[0], pr[1]); if (q.z > 2) { d += (on ? 'L' : 'M') + fx(q.x) + ' ' + fx(q.y); on = true; } else on = false; } return d; };
let grid = '';
for (let p = -150; p < 180; p += 30) grid += line(ys.map((y) => [p, y]));
for (const y of [0.25, 0.5, 0.75]) { const pts = []; for (let p = -180; p <= 180; p += 5) pts.push([p, y]); grid += line(pts); }
const spine = line(ys.map((y) => [-180, y]));
let marks = '', zone = '', navelRing = '', navel = '';
const ring = (c, rcm) => { let d = '', on = false; for (let i = 0; i <= 36; i++) { const an = i / 36 * 2 * Math.PI, p = c.p + Math.cos(an) * rcm / cmPerDeg(M, c.y), y = c.y + Math.sin(an) * rcm / M.Hcm, q = P(p, y); if (q.z > 0) { d += (on ? 'L' : 'M') + fx(q.x) + ' ' + fx(q.y); on = true; } else on = false; } return d; };
if (mName === 'belly') {
const rib = []; for (let p = -75; p <= 75; p += 5) rib.push([p, 0.02 + 0.13 * (1 - Math.abs(p) / 75)]); marks += line(rib);
for (const s of [-1, 1]) { const q = P(s * 62, 0.86); if (q.z > 4) marks += 'M' + fx(q.x - 7) + ' ' + fx(q.y - 3) + 'q7 -6 14 0'; }
const nq = P(0, 0.67);
if (nq.z > 3) { const f = nq.z / (M.a(0.67) * M.br); navelRing = ring({ p: 0, y: 0.67 }, NAVEL_CM); navel = ellD(nq.x, nq.y, 3.2 * Math.max(0.25, f), 2.6); }
} else {
const el = P(180, 0.98); if (el.z > 2) marks += 'M' + fx(el.x - 9) + ' ' + fx(el.y - 4) + 'q9 8 18 0';
const zp = []; for (let p = 115; p <= 245; p += 5) zp.push([normDeg(p), 0.22]); for (let p = 245; p >= 115; p -= 5) zp.push([normDeg(p), 0.8]);
const vis = zp.map((pr) => P(pr[0], pr[1])).filter((q) => q.z > 0);
if (vis.length > 3) { const top = vis.filter((q, i) => i < vis.length / 2), bot = vis.filter((q, i) => i >= vis.length / 2); zone = [].concat(top, bot).map((q, i) => (i ? 'L' : 'M') + fx(q.x) + ' ' + fx(q.y)).join('') + 'Z'; }
}
const ringD = ['', '', ''], sensD = ['', '', ''], cathD = ['', '', ''], spot = { m: mName, limb: limb };
for (const h of SITES) {
if (h.age > SITE_DAYS || !same(h, spot)) continue;
const q = P(h.p, h.y); if (q.z <= 0) continue;
const b = h.age < 4 ? 0 : h.age < 14 ? 1 : 2, f = Math.max(0.35, q.z / (M.a(h.y) * M.br)), r = 5.5;
if (h.kind === kind) ringD[b] += ring(h, SITE_MIN);
if (h.kind === 'sensor') sensD[b] += rrD(q.x - r * f, q.y - r, 2 * r * f, 2 * r, r * 0.45);
else cathD[b] += ellD(q.x, q.y, r * f, r);
}
const sug = suggest(kind, mName, limb);
let sugD = '', selRing = '', selDot = '';
if (sug && !sel) { const q = P(sug.p, sug.y); if (q.z > 0) sugD = ellD(q.x, q.y, 11, 11); }
if (sel) { const q = P(sel.p, sel.y); if (q.z > 0) { selRing = ring(sel, SITE_MIN); selDot = ellD(q.x, q.y, 7, 7); } }
return { outline, grid, spine, marks, zone, navelRing, navel, ringD, sensD, cathD, sugD, selRing, selDot, sug, view: viewName(th) };
};
this._bmLib = { MODELS, inv, render, check, siteName, suggest, normDeg, f1, KC };
return this._bmLib;
}
bmCtx() {
const s = this.state || {};
const mode = s.bmMode || 'belly';
const mName = mode === 'belly' ? 'belly' : 'arm', limb = mode === 'armL' ? 'L' : mode === 'armR' ? 'R' : '';
const th = (s.bmTh && s.bmTh[mode] !== undefined) ? s.bmTh[mode] : (mName === 'arm' ? 180 : 0);
const sel = (s.bmSel && s.bmSel[mode]) || null;
return { mode, mName, limb, th, sel, kind: mName === 'arm' ? 'sensor' : 'cath' };
}
bmSetTh(th) {
const c = this.bmCtx(), s = this.state || {};
this.setState({ bmTh: Object.assign({}, s.bmTh || {}, { [c.mode]: th }) });
}
bmSetSel(sel) {
const c = this.bmCtx(), s = this.state || {};
this.setState({ bmSel: Object.assign({}, s.bmSel || {}, { [c.mode]: sel }) });
}
bmTurn(to) {
const L = this.bmLib(), c = this.bmCtx(), from = c.th, d = L.normDeg(to - from);
let calm = false;
try { calm = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (x) {}
if (calm) { this.bmSetTh(from + d); return; }
const t0 = performance.now();
const step = (now) => { const k = Math.min(1, (now - t0) / 350), e = 1 - Math.pow(1 - k, 3); this.bmSetTh(from + d * e); if (k < 1) requestAnimationFrame(step); };
requestAnimationFrame(step);
}
bmVals() {
const L = this.bmLib(), c = this.bmCtx(), M = L.MODELS[c.mName];
const r = L.render(c.mName, c.limb, c.th, c.sel, c.kind);
const chk = c.sel ? L.check(c.kind, Object.assign({ m: c.mName, limb: c.limb }, c.sel)) : null;
const pt = (e) => { const b = e.currentTarget.getBoundingClientRect(); return { x: (e.clientX - b.left) / b.width * 320, y: (e.clientY - b.top) / b.height * 300, ppu: b.width / 320 }; };
const modes = [['belly', 'Bauch'], ['armL', 'Arm links'], ['armR', 'Arm rechts']].map((m) => ({
n: m[1], cls: 'ap-segb' + (c.mode === m[0] ? ' on' : ''), pressed: c.mode === m[0] ? 'true' : 'false',
pick: () => this.setState({ bmMode: m[0] })
}));
const turns = [['Vorne', 0], ['Links', 90], ['Hinten', 180], ['Rechts', -90]].map((t) => ({ n: t[0], go: () => this.bmTurn(t[1]) }));
return {
bmModes: modes,
bmTurns: turns,
bmLbl: c.kind === 'sensor' ? 'Tragestelle' : 'Setzstelle',
bmView: r.view,
bmAria: (c.mName === 'arm' ? 'Oberarm' : 'Bauchbereich') + ', gedreht auf ' + Math.round(L.normDeg(c.th)) + ' Grad',
bmMask: c.mName === 'arm' ? 'url(#bmask-a)' : 'url(#bmask-b)',
bmOutline: r.outline, bmGrid: r.grid, bmSpine: r.spine, bmMarks: r.marks, bmZone: r.zone,
bmNavelRing: r.navelRing, bmNavel: r.navel,
bmR0: r.ringD[0], bmR1: r.ringD[1], bmR2: r.ringD[2],
bmS0: r.sensD[0], bmS1: r.sensD[1], bmS2: r.sensD[2],
bmC0: r.cathD[0], bmC1: r.cathD[1], bmC2: r.cathD[2],
bmSug: r.sugD,
bmSelRingC: c.kind === 'cath' ? r.selRing : '', bmSelDotC: c.kind === 'cath' ? r.selDot : '',
bmSelRingS: c.kind === 'sensor' ? r.selRing : '', bmSelDotS: c.kind === 'sensor' ? r.selDot : '',
bmHint: c.mName === 'arm' ? 'Wischen dreht den Arm. Tippe auf die Stelle des Sensors. Grün gestrichelt: Rückseite des Oberarms.' : 'Wischen dreht den Bauch. Tippe auf die Stelle, an der du den Katheter gesetzt hast.',
bmHasSel: !!c.sel,
bmNoSel: !c.sel,
bmSelName: c.sel ? L.siteName(Object.assign({ m: c.mName, limb: c.limb }, c.sel)) : '',
bmSelDist: chk && chk.near ? ' · ' + L.f1(chk.near.d) + ' cm zur nächsten Stelle der letzten 30 Tage' : '',
bmWarn: chk && chk.warn.length ? chk.warn.join(' ') + ' Mehr Abstand schont die Haut.' : '',
bmHasWarn: !!(chk && chk.warn.length),
bmHasSug: !c.sel && !!r.sug,
bmSugName: r.sug ? L.siteName(Object.assign({ m: c.mName, limb: c.limb }, r.sug)) : '',
bmTakeSug: () => { if (r.sug) { this.bmSetSel({ p: r.sug.p, y: r.sug.y }); this.bmTurn(r.sug.p); } },
bmClear: () => this.bmSetSel(null),
bmDown: (e) => {
const p = pt(e);
this._bmDrag = { x: e.clientX, y: e.clientY, th: c.th, moved: false, ppu: p.ppu };
try { e.currentTarget.setPointerCapture(e.pointerId); } catch (x) {}
},
bmMove: (e) => {
const d = this._bmDrag; if (!d) return;
const dx = e.clientX - d.x, dy = e.clientY - d.y;
if (!d.moved && Math.hypot(dx, dy) < 7) return;
d.moved = true;
const cc = this.bmCtx(), MM = L.MODELS[cc.mName];
this.bmSetTh(d.th - (dx / (MM.a(0.5) * d.ppu)) * 180 / Math.PI);
if (e.cancelable) e.preventDefault();
},
bmUp: (e) => {
const d = this._bmDrag; this._bmDrag = null;
if (!d || d.moved) return;
const cc = this.bmCtx(), MM = L.MODELS[cc.mName], p = pt(e), s = L.inv(MM, p.x, p.y, cc.th);
if (s) this.bmSetSel(s);
},
bmCancel: () => { this._bmDrag = null; }
};
}

renderVals() {
const s = this.state || {};
let dark = false;
if (s.theme === 'dark') dark = true;
else if (s.theme !== 'light') { try { dark = window.matchMedia('(prefers-color-scheme: dark)').matches; } catch (e) {} }
if (!this._rootRef) this._rootRef = (el) => { this._root = el; };
if (!this._panelRef) {
this._panelRef = (el) => {
if (!el) return;
let calm = false;
try { calm = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (x) {}
try { el.scrollIntoView({ behavior: calm ? 'auto' : 'smooth', block: 'center' }); } catch (x) {}
try { el.focus({ preventScroll: true }); } catch (x) {}
};
}
const open = !!s.menuOpen;
const mail = s.mail || null;
const subject = mail ? (mail.subj ? 'Glycodex – ' + mail.subj + ' (EN)' : 'Glycodex (EN)') : '';
const ask = (subj, at) => (e) => {
this._trigger = e && e.currentTarget;
this.setState({ mail: { subj: subj, at: at } });
};
const closeMail = () => {
this.setState({ mail: null });
const tr = this._trigger;
if (tr && tr.focus) { try { tr.focus({ preventScroll: true }); } catch (x) {} }
};
return {
rootClass: 'gx' + (s.ready ? ' js' : ''),
theme: s.theme || 'auto',
isDark: dark,
isLight: !dark,
toggleTheme: () => {
const next = dark ? 'light' : 'dark';
try { window.localStorage.setItem('glycodex-theme', next); } catch (e) {}
this.setState({ theme: next });
},
rootRef: this._rootRef,
menuOpen: open,
menuClosed: !open,
menuExpanded: open ? 'true' : 'false',
toggleMenu: () => this.setState({ menuOpen: !open, langOpen: false }),
langOpen: !!s.langOpen,
langExpanded: s.langOpen ? 'true' : 'false',
toggleLang: () => this.setState({ langOpen: !s.langOpen, menuOpen: false }),
closeMenu: () => this.setState({ menuOpen: false }),
mailSubject: subject,
mailHref: 'mailto:lina.schroeder@autarkflow.de?subject=' + encodeURIComponent(subject),
phoneShown: !!s.phone,
phoneHidden: !s.phone,
showPhone: () => this.setState({ phone: true }),
telText: s.phone ? String.fromCharCode.apply(null, [43, 52, 57, 32, 49, 53, 54, 32, 51, 48, 48, 50, 54, 52, 53, 54]) : '',
telHref: s.phone ? 'tel:' + String.fromCharCode.apply(null, [43, 52, 57, 49, 53, 54, 51, 48, 48, 50, 54, 52, 53, 54]) : '',
...this.bmVals(),
askRueck: ask('Feedback', 'kontakt'),
askProfil: ask('Short profile', 'kontakt'),
askInfo: ask('Information sheet', 'kontakt'),
askMail: ask('', 'kontakt'),
mailAt_kontakt: !!mail && mail.at === 'kontakt',
panelRef: this._panelRef,
panelKey: (e) => { if (e.key === 'Escape') closeMail(); },
closeMail: closeMail,
sendMail: () => this.setState({ mail: null })
};
}
}
GX.mount(Component, { prerender: !!window.GX_PRERENDER });
