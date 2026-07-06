#!/bin/bash
# Render orbit/prize_map_shareable.svg -> orbit/prize_map_share.png (lossless,
# social-media-ready). Bootstraps a persistent cairosvg venv on first run.
set -e
cd "$(dirname "$0")/.."
VENV=~/.venvs/svgpng
[ -x "$VENV/bin/python" ] || { python3 -m venv "$VENV" && "$VENV/bin/pip" -q install cairosvg; }
python3 tools/make_shareable_svg.py
"$VENV/bin/python" -c "
import cairosvg
cairosvg.svg2png(url='orbit/prize_map_shareable.svg',
                 write_to='orbit/prize_map_share.png', output_width=3200)
import os; print('PNG:', os.path.getsize('orbit/prize_map_share.png')//1024, 'KB ->', os.path.abspath('orbit/prize_map_share.png'))"
