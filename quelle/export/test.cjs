// Prüft die statische Website: Darstellung und die wichtigsten Interaktionen.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const http = require('http');
const ROOT = '/home/claude/site/dist';
const OUTD = '/home/claude/site/shots/';
fs.mkdirSync(OUTD, { recursive: true });
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.webp': 'image/webp', '.woff2': 'font/woff2', '.png': 'image/png' };
const srv = http.createServer((req, resp) => {
  let p = decodeURIComponent(req.url.split('?')[0].split('#')[0]);
  if (p.endsWith('/')) p += 'index.html';
  const f = path.join(ROOT, p);
  if (!fs.existsSync(f) || fs.statSync(f).isDirectory()) { resp.writeHead(404); resp.end(); return; }
  resp.writeHead(200, { 'content-type': TYPES[path.extname(f)] || 'application/octet-stream' });
  resp.end(fs.readFileSync(f));
}).listen(0);

(async () => {
  const port = srv.address().port, B = 'http://127.0.0.1:' + port;
  const browser = await chromium.launch({ executablePath: '/usr/bin/google-chrome' });
  const errs = [];
  const log = (...a) => console.log(...a);
  async function open(u, w, dark) {
    const ctx = await browser.newContext({ viewport: { width: w, height: 900 }, colorScheme: dark ? 'dark' : 'light', hasTouch: w < 500 });
    const pg = await ctx.newPage();
    pg.on('pageerror', (e) => errs.push(u + ': ' + e.message));
    pg.on('console', (m) => { if (m.type() === 'error') errs.push(u + ' console: ' + m.text()); });
    pg.on('requestfailed', (r) => errs.push('404/fail ' + r.url()));
    pg.on('response', (r) => { if (r.status() >= 400) errs.push(r.status() + ' ' + r.url()); });
    await pg.goto(B + u);
    await pg.waitForFunction(() => document.documentElement.getAttribute('data-gx') === 'live');
    await pg.waitForTimeout(300);
    return { ctx, pg };
  }
  // Desktop Startseite
  let { ctx, pg } = await open('/', 1280);
  await pg.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 40)); } window.scrollTo(0, 0); });
  await pg.waitForTimeout(500);
  await pg.screenshot({ path: OUTD + 'd_full.png', fullPage: true });
  // Sprachmenü
  await pg.click('.lang-btn'); await pg.waitForTimeout(150);
  log('Sprachmenü offen:', await pg.isVisible('#langm'), await pg.$$eval('#langm a', (a) => a.map((x) => x.getAttribute('href'))));
  await pg.screenshot({ path: OUTD + 'd_lang.png', clip: { x: 700, y: 0, width: 580, height: 330 } });
  await pg.click('#langm a[hreflang="en"]'); await pg.waitForFunction(() => document.documentElement.lang === 'en');
  log('nach Klick:', pg.url());
  await pg.goBack(); await pg.waitForFunction(() => document.documentElement.getAttribute('data-gx') === 'live');
  // Farbschema
  await pg.click('button[aria-label="Farbschema wechseln"]'); await pg.waitForTimeout(150);
  log('Theme:', await pg.getAttribute('.gx', 'data-theme'), await pg.evaluate(() => localStorage.getItem('glycodex-theme')));
  await pg.screenshot({ path: OUTD + 'd_dark.png' });
  await pg.click('button[aria-label="Farbschema wechseln"]');
  // Mail-Hinweis
  const ask = await pg.$('#kontakt button.btn');
  await ask.click(); await pg.waitForTimeout(700);
  log('Hinweis sichtbar:', await pg.isVisible('.hint'), 'Fokus:', await pg.evaluate(() => document.activeElement && document.activeElement.className));
  log('mailto:', await pg.getAttribute('.hint a.btn-p', 'href'));
  await pg.screenshot({ path: OUTD + 'd_hint.png' });
  await pg.keyboard.press('Escape'); await pg.waitForTimeout(150);
  log('Hinweis nach Esc:', await pg.isVisible('.hint'));
  // Telefon
  const html0 = await pg.content();
  log('Nummer im HTML vor Klick:', /30026456|15630026456/.test(html0));
  await pg.click('#kontakt button:has-text("Telefonnummer anzeigen")'); await pg.waitForTimeout(100);
  log('Telefon:', await pg.textContent('#kontakt a[href^="tel:"]'));
  // Körperkarte
  const stage = await pg.$('.phone-live svg');
  const bb = await stage.boundingBox();
  const p0 = await pg.$eval('.phone-live svg', (s) => s.innerHTML.length);
  await pg.mouse.move(bb.x + bb.width / 2, bb.y + bb.height / 2); await pg.mouse.down();
  await pg.mouse.move(bb.x + bb.width / 2 + 80, bb.y + bb.height / 2, { steps: 8 }); await pg.mouse.up();
  await pg.waitForTimeout(200);
  const p1 = await pg.$eval('.phone-live svg', (s) => s.innerHTML.length);
  log('Körperkarte gedreht (SVG geändert):', p0 !== p1);
  await pg.click('.phone-live button:has-text("Arm links")'); await pg.waitForTimeout(200);
  await pg.$eval('.phone-live', (e) => e.scrollIntoView({ block: 'center' }));
  await pg.screenshot({ path: OUTD + 'd_body.png' });
  await ctx.close();
  // Handy
  ({ ctx, pg } = await open('/uk/', 390));
  await pg.click('.menu-btn'); await pg.waitForTimeout(150);
  log('Handy-Menü offen:', await pg.isVisible('#mnav'));
  await pg.screenshot({ path: OUTD + 'm_menu.png' });
  await pg.click('.menu-btn');
  await pg.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 500) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 30)); } window.scrollTo(0, 0); });
  await pg.waitForTimeout(400);
  await pg.screenshot({ path: OUTD + 'm_full.png', fullPage: true });
  await ctx.close();
  // Rechtliches und Unterseiten
  for (const u of ['/impressum/', '/en/datenschutz/', '/fr/partnerships/', '/diabetes-teams/']) {
    ({ ctx, pg } = await open(u, 1280));
    await pg.screenshot({ path: OUTD + 'p_' + u.replace(/\//g, '_') + '.png' });
    await ctx.close();
  }
  // Ohne JavaScript
  const c2 = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 1280, height: 900 } });
  const p2 = await c2.newPage(); await p2.goto(B + '/');
  await p2.screenshot({ path: OUTD + 'nojs.png' });
  log('Ohne JS Text vorhanden:', (await p2.textContent('h1')).trim());
  await c2.close();
  console.log('FEHLER:', errs.length ? errs : 'keine');
  await browser.close(); srv.close();
})();
