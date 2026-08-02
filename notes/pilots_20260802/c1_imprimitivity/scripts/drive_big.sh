#!/usr/bin/env bash
set -uo pipefail
RG=/home/u2470931/smooth-read-solomin/prize/tools/ramguard
D=/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/c1_imprimitivity
N=$1; W=$2; TGT=$3; NP=$4
for ((p=0;p<NP;p++)); do
  f=$(printf "%s/results/n%dbig/N%02d_w%02d_p%03dof%03d.json" "$D" "$N" "$N" "$W" "$p" "$NP")
  [[ -s "$f" ]] && { echo "skip $p"; continue; }
  echo "=== N=$N w=$W part $p/$NP ==="
  $RG local -- python3 $D/scripts/scan_big.py --N $N --w $W --target $TGT \
      --part $p --nparts $NP --outdir $D/results/n${N}big || echo "FAILED $p"
done
