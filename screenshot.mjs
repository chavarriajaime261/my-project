import puppeteer from 'puppeteer';
import { mkdir, readdir } from 'node:fs/promises';
import { join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(fileURLToPath(new URL('.', import.meta.url)));
const OUT_DIR = join(ROOT, 'temporary screenshots');

const url = process.argv[2];
const label = process.argv[3];
if (!url) {
  console.error('usage: node screenshot.mjs <url> [label]');
  process.exit(1);
}

await mkdir(OUT_DIR, { recursive: true });
const existing = await readdir(OUT_DIR).catch(() => []);
let maxN = 0;
for (const f of existing) {
  const m = f.match(/^screenshot-(\d+)(?:-.*)?\.png$/);
  if (m) maxN = Math.max(maxN, Number(m[1]));
}
const n = maxN + 1;
const name = label ? `screenshot-${n}-${label}.png` : `screenshot-${n}.png`;
const out = join(OUT_DIR, name);

const browser = await puppeteer.launch({
  headless: 'new',
  args: ['--no-sandbox', '--disable-setuid-sandbox'],
});
try {
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 1 });
  await page.goto(url, { waitUntil: 'networkidle0', timeout: 30000 });
  await new Promise((r) => setTimeout(r, 400));
  await page.screenshot({ path: out, fullPage: true });
  console.log('saved', out);
} finally {
  await browser.close();
}
