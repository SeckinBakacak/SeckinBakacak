// Kullanım: node render.mjs <cikti_klasoru> [--onizleme t1,t2,...]
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const dir = path.dirname(fileURLToPath(import.meta.url));
const out = process.argv[2];
const prevIdx = process.argv.indexOf('--onizleme');
const FPS = 30;
const tl = JSON.parse(fs.readFileSync(path.join(out, 'timeline.json'), 'utf8'));

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 720, height: 1280 } });
await page.goto('file://' + path.join(dir, 'sahne.html'));
await page.evaluate(tl => window.setTL(tl), tl);
await page.evaluate(() => document.fonts.ready);

if (prevIdx > 0) {
  const ts = process.argv[prevIdx + 1].split(',').map(Number);
  for (const t of ts) {
    await page.evaluate(t => render(t), t);
    await page.screenshot({ path: path.join(out, `onizleme_${t}.jpg`), type: 'jpeg', quality: 80 });
  }
  await browser.close(); process.exit(0);
}

const mp4 = path.join(out, 'video.mp4');
const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
  '-i', path.join(out, 'ses.wav'), '-vf', 'scale=1080:1920:flags=lanczos', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20',
  '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', mp4], { stdio: ['pipe', 'inherit', 'inherit'] });
const N = Math.ceil(tl.total * FPS);
const t0 = Date.now();
for (let i = 0; i < N; i++) {
  await page.evaluate(t => render(t), i / FPS);
  const buf = await page.screenshot({ type: 'jpeg', quality: 92 });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  if (i % 300 === 0) console.log(`kare ${i}/${N}  ${((Date.now() - t0) / 1000).toFixed(0)} sn`);
}
ff.stdin.end();
await new Promise(r => ff.on('close', r));
await browser.close();
console.log('Bitti:', mp4);
