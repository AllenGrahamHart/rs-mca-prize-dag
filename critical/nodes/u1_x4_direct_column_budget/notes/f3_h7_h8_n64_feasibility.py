#!/usr/bin/env python3
"""Exact feasibility arithmetic for n=64 h=7/h=8 anchored certificates."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
NOTES = ROOT / "critical/nodes/u1_x4_direct_column_budget/notes"
H6_BASE = NOTES / "f3_h6_n64_boundary_certificate.json"


def mib(bytes_count: int) -> float:
    return bytes_count / (1024 * 1024)


def main() -> None:
    h6 = json.loads(H6_BASE.read_text())
    record_bytes = 32
    rows = []
    for h in (6, 7, 8):
        left = math.comb(63, h - 1)
        right = math.comb(63, h)
        rows.append(
            {
                "h": h,
                "left_records": left,
                "right_probes": right,
                "left_record_memory_mib_at_32B": round(mib(left * record_bytes), 1),
                "left_factor_vs_h6": round(left / h6["hashed_per_shard"], 3),
                "right_factor_vs_h6": round(right / h6["probed"], 3),
                "signature_shards_for_h6_left_memory": math.ceil(left / h6["hashed_per_shard"]),
                "right_shards_for_h6_probe_count": math.ceil(right / h6["probed"]),
            }
        )

    h7 = rows[1]
    h8 = rows[2]
    print("baseline h6 max shard seconds:", h6["max_elapsed_sec"])
    for row in rows:
        print(
            "h={h} left={left_records} right={right_probes} "
            "mem32={left_record_memory_mib_at_32B}MiB "
            "left_factor={left_factor_vs_h6} right_factor={right_factor_vs_h6} "
            "sig_shards={signature_shards_for_h6_left_memory} "
            "right_shards={right_shards_for_h6_probe_count}".format(**row)
        )
    if h7["left_record_memory_mib_at_32B"] < 4096:
        print("h=7 n64 may be a one-shard Modal gate, but current all-left sort is time-risky")
    if h8["left_record_memory_mib_at_32B"] > 8192:
        print("h=8 n64 is not a current all-left hash certificate under the light-compute rule")
    print("H7_H8_N64_FEASIBILITY_PASS")


if __name__ == "__main__":
    main()
