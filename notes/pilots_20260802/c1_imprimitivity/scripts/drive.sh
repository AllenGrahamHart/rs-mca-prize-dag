#!/usr/bin/env bash
# Chunked driver: each chunk is its own `ramguard local` invocation (1G / 5 min).
set -uo pipefail
RG=/home/u2470931/smooth-read-solomin/prize/tools/ramguard
D=/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/c1_imprimitivity
N=$1; W=$2; NP=$3; THR=${4:-}
for ((p=0;p<NP;p++)); do
  f=$(printf "%s/results/n%d/N%02d_w%02d_p%03dof%03d.json" "$D" "$N" "$N" "$W" "$p" "$NP")
  if [[ -s "$f" ]]; then echo "skip part $p"; continue; fi
  args=(--N "$N" --w "$W" --part "$p" --nparts "$NP" --outdir "$D/results/n$N")
  if [[ -n "$THR" ]]; then args+=(--threshold "$THR"); fi
  echo "=== part $p/$NP ==="
  $RG local -- python3 "$D/scripts/scan.py" "${args[@]}" || echo "FAILED part $p"
done
