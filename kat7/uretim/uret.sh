#!/usr/bin/env bash
# Bir bölümü baştan sona üretir: ./uret.sh bolum01
# Gerekenler: python3 + numpy, node + playwright, ffmpeg, ElevenLabs anahtarı
# (bulut oturumunda proxy ekler; yerelde ELEVENLABS_API_KEY ortam değişkeni)
set -euo pipefail
cd "$(dirname "$0")"
ep="${1:-bolum01}"; out="cikti/$ep"
python3 ses.py "$ep.json" "$out"
node render.mjs "$out"
echo "Video: $out/video.mp4"
