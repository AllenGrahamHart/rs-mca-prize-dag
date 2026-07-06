#!/bin/bash
# Publish the critical DAG webapp to allengrahamhart.github.io/prize-dag/
# (rebuild -> copy -> commit -> push; the Hugo Action redeploys the site).
set -e
cd "$(dirname "$0")/.."
python3 tools/build_critical_orbit.py
SITE=~/smooth-read-solomin/allengrahamhart.github.io
git -C "$SITE" pull -q --rebase origin main
cp orbit/critical_orbit.html "$SITE/static/prize-dag/index.html"
if git -C "$SITE" diff --quiet static/prize-dag/index.html; then
  echo "site already current"; exit 0
fi
git -C "$SITE" add static/prize-dag/index.html
git -C "$SITE" -c user.name=AllenGrahamHart -c user.email=allenhart094@googlemail.com \
  commit -q -m "Update prize-dag webapp: $(date -u +%Y-%m-%d) $1

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git -C "$SITE" push -q origin main
echo "published -> https://allengrahamhart.github.io/prize-dag/"
