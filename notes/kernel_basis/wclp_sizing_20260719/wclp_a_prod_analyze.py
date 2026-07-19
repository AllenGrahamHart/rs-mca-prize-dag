#!/usr/bin/env python3
"""Analyze the downloaded production batch checkpoints of the (1,5) sweep
(weight5-recursive-norm-full-v2/batch_summaries) -- coverage, timing, tails."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent / "wclp_a_batches" / "batch_summaries"
CLASS_COUNT = 2_296_920
BATCH = 64
EXPECTED_SHA = "9ac0ca650e704a13514180fe2d8bcea94943c771f125b3942888a6aba8c87f00"

rows_covered = 0
indices = []
secs = []
fsecs = []
unresolved = []
max_v2 = -1
max_norm_bits = 0
max_prime_bits = 0
high_gate = 0
bad = 0
resolved_rows = 0
for path in ROOT.glob("part_*.json"):
    try:
        row = json.loads(path.read_text())
    except json.JSONDecodeError:
        bad += 1
        continue
    if (
        row.get("schema") != "dli-wcl-weight5-recursive-norm-batch-v2"
        or row.get("run_id") != "weight5-recursive-norm-full-v2"
        or row.get("representative_sha256") != EXPECTED_SHA
        or row.get("status") != "COMPLETE"
    ):
        bad += 1
        continue
    index = int(row["batch_index"])
    if row["start"] != index * BATCH or row["rows"] != row["end"] - row["start"]:
        bad += 1
        continue
    indices.append(index)
    rows_covered += int(row["rows"])
    resolved_rows += int(row["resolved_rows"])
    secs.append(float(row["seconds"]))
    fsecs.append(float(row["factor_seconds"]))
    unresolved.extend(row["unresolved_cases"])
    max_v2 = max(max_v2, int(row["max_v2_prime_minus_1"]))
    max_norm_bits = max(max_norm_bits, int(row["max_norm_bits"]))
    max_prime_bits = max(max_prime_bits, int(row["max_prime_bits"]))
    high_gate += len(row["high_gate_cases"])

indices.sort()
gaps = []
prev = -1
for index in indices:
    if index != prev + 1:
        gaps.append((prev + 1, index - 1))
    prev = index
secs.sort()
fsecs.sort()
n = len(secs)


def pct(v, p):
    return v[int(p * (len(v) - 1))]


print(f"complete batches      : {n} (bad/foreign files: {bad})")
print(f"index range           : {indices[0]}..{indices[-1]}; gaps: {gaps[:10]}{'...' if len(gaps)>10 else ''} ({len(gaps)} gaps)")
print(f"rows covered          : {rows_covered:,} of {CLASS_COUNT:,} ({rows_covered/CLASS_COUNT:.2%})")
print(f"rows remaining        : {CLASS_COUNT - rows_covered:,}")
print(f"resolved rows         : {resolved_rows:,}; unresolved (60s timeouts): {len(unresolved)} ({len(unresolved)/rows_covered:.4%} of covered)")
print(f"batch wall seconds    : sum {sum(secs):,.0f} s = {sum(secs)/3600:,.1f} h; mean {sum(secs)/n:.2f} med {pct(secs,.5):.2f} p90 {pct(secs,.9):.2f} p99 {pct(secs,.99):.2f} max {secs[-1]:.2f}")
print(f"factor-phase wall     : sum {sum(fsecs):,.0f} s = {sum(fsecs)/3600:,.1f} h (2-thread phase, cpu=2 workers)")
print(f"per-row batch-wall    : {sum(secs)/rows_covered:.4f} s/row (x2 cores reserved => {2*sum(secs)/rows_covered:.4f} reserved-core-s/row)")
print(f"max_v2(p-1) observed  : {max_v2}; high-gate cases: {high_gate}")
print(f"max norm bits         : {max_norm_bits}; max prime bits: {max_prime_bits}")

norm_bits_of_unresolved = sorted(int(c["norm_bits"]) for c in unresolved)
if unresolved:
    print(f"unresolved norm bits  : med {pct(norm_bits_of_unresolved,.5)} max {norm_bits_of_unresolved[-1]}")

out = {
    "complete_batches": n,
    "rows_covered": rows_covered,
    "rows_remaining": CLASS_COUNT - rows_covered,
    "frontier_contiguous_through": (gaps[0][0] * BATCH if gaps else (indices[-1] + 1) * BATCH),
    "unresolved": len(unresolved),
    "sum_batch_seconds": sum(secs),
    "sum_factor_seconds": sum(fsecs),
}
Path(__file__).with_name("wclp_a_prod_summary.json").write_text(
    json.dumps(out, indent=2, sort_keys=True) + "\n"
)
print("frontier (first uncovered row, contiguous):", out["frontier_contiguous_through"])
