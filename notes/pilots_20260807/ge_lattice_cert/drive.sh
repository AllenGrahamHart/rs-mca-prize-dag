#!/usr/bin/env bash
# Drive one cell across the ramguard 5-minute wall by repeated resume.
# Usage (from repo root):  notes/pilots_20260807/ge_lattice_cert/drive.sh CELLID [MAXROUNDS]
set -u
CID=$1
MAX=${2:-200}
D=notes/pilots_20260807/ge_lattice_cert
LOG=$D/state/$CID.drive.log
: > "$LOG"
for i in $(seq 1 "$MAX"); do
    out=$(tools/ramguard local -- python3 "$D/runcell.py" "$CID" 2>&1)
    echo "--- round $i ---" >> "$LOG"
    echo "$out" | grep -Ev '^      \.\.\.' >> "$LOG"
    if echo "$out" | grep -q '^STATUS: DONE'; then
        echo "FINISHED after $i rounds" >> "$LOG"
        exit 0
    fi
    if ! echo "$out" | grep -q '^STATUS: RUNNING'; then
        echo "UNEXPECTED EXIT at round $i" >> "$LOG"
        echo "$out" | tail -20 >> "$LOG"
        exit 1
    fi
done
echo "ROUND BUDGET EXHAUSTED after $MAX rounds" >> "$LOG"
exit 2
