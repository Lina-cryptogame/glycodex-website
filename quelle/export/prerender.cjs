// Setzt den ersten Seitenzustand als fertiges HTML in jede Seite ein (für Suchmaschinen und ohne JavaScript).
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const http = require('http');

const ROOT = '/home/claude/site/dist';
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.webp': 'image/webp', '.woff2': 'font/woff2', '.png': 'image/png', '.txt': 'text/plain' };

function serve() {
  return new Promise((res) => {
    const srv = http.createServer((req, resp) => {
      let p = decodeURIComponent(req.url.split('?')[0].split('#')[0]);
      if (p.endsWith('/')) p += 'index.html';
      const f = path.join(ROOT, p);
      if (!f.startsWith(ROOT) || !fs.existsSync(f)) { resp.writeHead(404); resp.end(); return; }
      resp.writeHead(200, { 'content-type': TYPES[path.extname(f)] || 'application/octet-stream' });
      resp.end(fs.readFileSync(f));
    }).listen(0, () => res(srv));
  });
}

function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) { if (e.name !== 'assets') walk(p, out); }
    else if (e.name === 'index.html') out.push(p);
  }
  return out;
}

(async () => {
  const srv = await serve();
  const port = srv.address().port;
  const browser = await chromium.launch({ executablePath: '/usr/bin/google-chrome' });
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 }, colorScheme: 'light' });
  await ctx.addInitScript(() => { window.GX_PRERENDER = true; });
  const page = await ctx.newPage();
  const errs = [];
  page.on('pageerror', (e) => errs.push(e.message));
  for (const f of walk(ROOT)) {
    const rel = '/' + path.relative(ROOT, path.dirname(f)).replace(/\\/g, '/');
    const u = 'http://127.0.0.1:' + port + (rel === '/' ? '/' : rel + '/');
    await page.goto(u);
    await page.waitForFunction(() => document.documentElement.getAttribute('data-gx') === 'pre');
    const inner = await page.evaluate(() => document.getElementById('gx-app').innerHTML);
    const src = fs.readFileSync(f, 'utf8');
    fs.writeFileSync(f, src.replace('<!--PRERENDER-->', inner));
    console.log('ok', rel, inner.length);
  }
  if (errs.length) console.log('FEHLER', errs);
  await browser.close();
  srv.close();
})();
