#!/usr/bin/env bash
# D2 ladder driver.  Each shard is a loop of ramguard-`local` invocations that
# checkpoint to state/lad_<FAM>_<SEED>.json and resume; nothing runs past the
# 5-minute profile wall inside a single invocation (LAD_SOFT=235s).
cd /home/u2470931/smooth-read-solomin/prize || exit 1
D=notes/pilots_20260809/large_v2_hunt
mkdir -p "$D/state" "$D/logs"
ROUNDS=${ROUNDS:-30}

run_shard() {
    local seed=$1 fam=$2
    for _ in $(seq 1 "$ROUNDS"); do
        LAD_SOFT=235 tools/ramguard local -- \
            python3 "$D/lad.py" "$seed" "$fam" \
            >> "$D/logs/lad_${fam}_${seed}.log" 2>&1 || true
    done
}

for s in 20260809 1009 2029 3049 4099 5119 6143 7177; do
    run_shard "$s" B &
done
for s in 8191 9209; do run_shard "$s" C3 & done
run_shard 10243 C5 &
run_shard 11261 A &
wait
