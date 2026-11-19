const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const svg = fs.readFileSync('/home/claude/handbuch/img/icon.svg', 'utf8');
  const b = await chromium.launch({ executablePath: '/usr/bin/google-chrome' });
  for (const s of [16, 32, 48, 180, 192, 512]) {
    const p = await b.newPage({ viewport: { width: s, height: s }, deviceScaleFactor: 1 });
    await p.setContent(`<html><body style="margin:0;background:transparent">${svg.replace('width="512" height="512"', `width="${s}" height="${s}"`)}</body></html>`);
    await p.screenshot({ path: `icon-${s}.png`, omitBackground: true, clip: { x: 0, y: 0, width: s, height: s } });
    await p.close();
  }
  await b.close();
})();
