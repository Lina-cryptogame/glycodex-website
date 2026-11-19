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
const subject = mail ? (mail.subj ? 'Glycodex – ' + mail.subj + ' (UK)' : 'Glycodex (UK)') : '';
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
panelRef: this._panelRef,
panelKey: (e) => { if (e.key === 'Escape') closeMail(); },
closeMail: closeMail,
sendMail: () => this.setState({ mail: null })
};
}
}
GX.mount(Component, { prerender: !!window.GX_PRERENDER });
