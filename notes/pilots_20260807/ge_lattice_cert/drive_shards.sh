#!/usr/bin/env bash
# Drive a sharded cell: NSHARD parallel shard-drivers, each resuming across
# the ramguard wall.  Usage: drive_shards.sh CELLID NSHARD SDEPTH [MAXROUNDS]
set -u
CID=$1; NS=$2; SD=$3; MAX=${4:-200}
D=notes/pilots_20260807/ge_lattice_cert
mkdir -p "$D/state"
# Complete the LLL FIRST, single-process.  Shards that start a fresh cell
# simultaneously would otherwise all run LLL and race on its checkpoint.
until grep -q '"stage": 2' "$D/state/$CID.lll.json" 2>/dev/null; do
  tools/ramguard local -- python3 "$D/runcell.py" "$CID" >/dev/null 2>&1 || true
done
rm -f "$D/state/$CID.enum.json"
for s in $(seq 0 $((NS-1))); do
  (
    LOG=$D/state/$CID.s$s.log
    : > "$LOG"
    for i in $(seq 1 "$MAX"); do
      out=$(GEL_SHARD=$s GEL_NSHARD=$NS GEL_SDEPTH=$SD \
            tools/ramguard local -- python3 "$D/runcell.py" "$CID" 2>&1)
      echo "$out" | grep -Ev '^      \.\.\.' | grep -E 'FP |RESULT|STATUS|FAIL' \
        >> "$LOG"
      if echo "$out" | grep -q '^STATUS: DONE'; then
        echo "SHARD $s FINISHED after $i rounds" >> "$LOG"; exit 0
      fi
      if ! echo "$out" | grep -q '^STATUS: RUNNING'; then
        echo "SHARD $s UNEXPECTED EXIT round $i" >> "$LOG"
        echo "$out" | tail -25 >> "$LOG"; exit 1
      fi
    done
    echo "SHARD $s BUDGET EXHAUSTED" >> "$LOG"
  ) &
done
wait
echo "ALL SHARDS RETURNED"
