#!/usr/bin/env bash
set -uo pipefail
RG=/home/u2470931/smooth-read-solomin/prize/tools/ramguard
D=/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/c1_imprimitivity
h () {
  o=$D/results/hunt_N$1_w$2${5:-}.json
  [[ -s "$o" ]] && { echo "skip $1/$2"; return; }
  echo "=== hunt N=$1 w=$2 seed=${4:-20260802} ==="
  $RG local -- python3 $D/scripts/hunt.py --N $1 --w $2 --target $3 \
      --restarts 60000 --seconds 230 --seed ${4:-20260802} --out $o || echo "FAILED $1 $2"
}
h 32 11 34039471045456321
h 32 14 1082454936556614916
h 32 15 2601547162386900289
h 32 12 117228382536325636 777 _s777
h 32 13 604793599934583361 777 _s777
h 32 11 34039471045456321 999 _s999
h 32 10 7153912066963204 555 _s555
