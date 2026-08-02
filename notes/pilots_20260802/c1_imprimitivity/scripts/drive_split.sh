#!/usr/bin/env bash
set -uo pipefail
RG=/home/u2470931/smooth-read-solomin/prize/tools/ramguard
D=/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/c1_imprimitivity
for spec in "32 2 6" "32 7 7" "32 8 8"; do
  set -- $spec
  echo "=== split N=$1 w=$2..$3 ==="
  $RG local -- python3 $D/scripts/split.py $1 $2 $3 $D/results/split_N$1_w$2-$3.json || echo FAILED
done
