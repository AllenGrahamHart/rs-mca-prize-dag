#!/usr/bin/env bash
set -uo pipefail
RG=/home/u2470931/smooth-read-solomin/prize/tools/ramguard
D=/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/c1_imprimitivity
run () { echo "=== N=64 w=$1 ==="; $RG local -- python3 $D/scripts/scan_big.py --N 64 --w $1 --target $2 --outdir $D/results/n64 || echo "FAILED w=$1"; }
run 2 4294967296
run 3 1853020188851841
run 4 2177953337809371136
run 5 6132610415680998648961
run 6 3145186990070779381678336
