#!/usr/bin/env python3
"""Count unsigned WCL weight-six affine-Galois classes by Burnside."""

from __future__ import annotations

import json
from pathlib import Path

import modal


ORDER = 256
WEIGHT = 6
OUTPUT = Path(__file__).with_name(
    "dli_wcl_ell1_weight6_unsigned_burnside_result.json"
)

app = modal.App("rs-mca-wcl16-unsigned-burnside")


@app.function(cpu=1, memory=512, timeout=60, max_containers=1)
def count() -> dict[str, object]:
    import hashlib
    import time

    started = time.monotonic()
    fixed_total = [0, 0]
    transformation_digest = hashlib.sha256()
    transformations = 0

    for multiplier in range(1, ORDER, 2):
        for shift in range(ORDER):
            seen = [False] * ORDER
            cycles = []
            for start in range(ORDER):
                if seen[start]:
                    continue
                cycle = []
                point = start
                while not seen[point]:
                    seen[point] = True
                    cycle.append(point)
                    point = (multiplier * point + shift) % ORDER
                if point != start:
                    raise AssertionError("noncycle")
                cycles.append(cycle)

            dp = [[0, 0] for _ in range(WEIGHT + 1)]
            dp[0][0] = 1
            for cycle in cycles:
                length = len(cycle)
                if length > WEIGHT:
                    continue
                parity = sum(cycle) & 1
                for size in range(WEIGHT - length, -1, -1):
                    for old_parity in range(2):
                        dp[size + length][old_parity ^ parity] += dp[size][old_parity]

            even, odd = dp[WEIGHT]
            fixed_total[0] += even
            fixed_total[1] += odd
            transformation_digest.update(
                f"{multiplier}:{shift}:{even}:{odd}\n".encode()
            )
            transformations += 1

    group_order = ORDER * (ORDER // 2)
    if transformations != group_order:
        raise AssertionError("group coverage")
    if any(value % group_order for value in fixed_total):
        raise AssertionError("Burnside divisibility")
    sector_orbits = [value // group_order for value in fixed_total]
    return {
        "schema": "dli-wcl-ell1-weight6-unsigned-burnside-v1",
        "status": "COMPLETE",
        "order": ORDER,
        "weight": WEIGHT,
        "group_order": group_order,
        "transformations": transformations,
        "fixed_sums_by_product_parity": fixed_total,
        "orbits_by_product_parity": sector_orbits,
        "orbit_count": sum(sector_orbits),
        "signed_affine_galois_classes": 185_569_028,
        "compression_ratio": 185_569_028 / sum(sector_orbits),
        "transformation_digest": transformation_digest.hexdigest(),
        "seconds": round(time.monotonic() - started, 6),
    }


@app.local_entrypoint()
def main() -> None:
    result = count.remote()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_ELL1_WEIGHT6_UNSIGNED_BURNSIDE "
        f"orbits={result['orbit_count']} sectors={result['orbits_by_product_parity']} "
        f"compression={result['compression_ratio']:.6f}"
    )
