import puppeteer from 'puppeteer';
import { mkdir, readdir } from 'node:fs/promises';
import { join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(fileURLToPath(new URL('.', import.meta.url)));
const OUT_DIR = join(ROOT, 'temporary screenshots');

const url = process.argv[2];
const label = process.argv[3] || 'vp';
const y = Number(process.argv[4] || 0);

await mkdir(OUT_DIR, { recursive: true });
const existing = await readdir(OUT_DIR).catch(() => []);
let maxN = 0;
for (const f of existing) {
  const m = f.match(/^screenshot-(\d+)(?:-.*)?\.png$/);
  if (m) maxN = Math.max(maxN, Number(m[1]));
}
const n = maxN + 1;
const out = join(OUT_DIR, `screenshot-${n}-${label}.png`);

const browser = await puppeteer.launch({ headless: 'new' });
try {
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 1 });
  await page.goto(url, { waitUntil: 'networkidle0', timeout: 30000 });
  if (y) await page.evaluate((yy) => window.scrollTo(0, yy), y);
  await new Promise((r) => setTimeout(r, 400));
  await page.screenshot({ path: out, fullPage: false });
  console.log('saved', out);
} finally {
  await browser.close();
}
