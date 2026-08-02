#!/usr/bin/env bash
set -uo pipefail
RG=/home/u2470931/smooth-read-solomin/prize/tools/ramguard
D=/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/c1_imprimitivity
h () { # N w target seed
  o=$D/results/hunt_N$1_w$2.json
  [[ -s "$o" ]] && { echo "skip $1/$2"; return; }
  echo "=== hunt N=$1 w=$2 ==="
  $RG local -- python3 $D/scripts/hunt.py --N $1 --w $2 --target $3 \
      --restarts 40000 --seconds 230 --seed ${4:-20260802} --out $o || echo "FAILED $1 $2"
}
# CONTROL: the predicted break at w = N/2 for N = 32 (must find a BEAT)
h 32 16 5341156734071209984
# highest-risk interior points at 2N=64 (w -> N/2 = 16)
h 32 15 2601547162386900289
h 32 14 1082454936556614916
h 32 13 604793599934583361
h 32 12 117228382536325636
# 2N=128 beyond exhaustion
h 64 7  1104427674243920646305299201
h 64 8  47474308632323863464483717136
h 64 9  2301619141096101839813550846721
h 64 10 51178457861841741792166689945616
# 2N=256
h 128 4 4743480741674980702700443299789930496
h 128 5 37608910510519071039902074217516707306379521
h 128 6 9892201202510488880834903224968047565840171728896
