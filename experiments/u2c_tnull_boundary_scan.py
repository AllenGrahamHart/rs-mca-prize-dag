#!/usr/bin/env python3
"""Bounded U2-C t-null boundary scan.

The U2-C premise says that giant/boundary-scale t-null blocks are exhausted by
the boundary/dictionary classes.  This local scan attacks the premise at the
small certifier scale already used by `u2_per_row_certifier`: exact
0/1 t-null blocks on mu_N.  It is not a proof of the giant statement.  It is a
fail-fast falsifier for primitive non-boundary blocks persisting in the clean
side of the known N=64, t=3 transition.
"""

from __future__ import annotations

import argparse
import itertools
import json
import time
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "experiments" / "amber_stress" / "u2c_tnull_boundary_scan_results.json"


def factor_int(n: int) -> list[int]:
    factors: list[int] = []
    d = 2
    value = n
    while d * d <= value:
        if value % d == 0:
            factors.append(d)
            while value % d == 0:
                value //= d
        d += 1 if d == 2 else 2
    if value > 1:
        factors.append(value)
    return factors


def primitive_root(p: int) -> int:
    factors = factor_int(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // f, p) != 1 for f in factors):
            return g
    raise ValueError(f"no primitive root for {p}")


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mask_from_combo(combo: tuple[int, ...]) -> int:
    mask = 0
    for a in combo:
        mask |= 1 << a
    return mask


def combo_sum(combo: tuple[int, ...], moments: list[tuple[int, ...]], p: int, t: int) -> tuple[int, ...]:
    sums = [0] * t
    for a in combo:
        row = moments[a]
        for i in range(t):
            sums[i] += row[i]
    return tuple(x % p for x in sums)


def mask_to_list(mask: int, n: int) -> list[int]:
    return [i for i in range(n) if (mask >> i) & 1]


def rotate_mask(mask: int, n: int, shift: int) -> int:
    out = 0
    for i in range(n):
        if (mask >> i) & 1:
            out |= 1 << ((i + shift) % n)
    return out


def reflect_mask(mask: int, n: int, center: int) -> int:
    out = 0
    for i in range(n):
        if (mask >> i) & 1:
            out |= 1 << ((center - i) % n)
    return out


def has_dihedral_symmetry(mask: int, n: int) -> bool:
    for shift in range(1, n):
        if rotate_mask(mask, n, shift) == mask:
            return True
    for center in range(n):
        if reflect_mask(mask, n, center) == mask:
            return True
    return False


def is_union_of_cosets(mask: int, n: int, subgroup_order: int) -> bool:
    step = n // subgroup_order
    for residue in range(step):
        coset_bits = [residue + j * step for j in range(subgroup_order)]
        count = sum((mask >> a) & 1 for a in coset_bits)
        if count not in (0, subgroup_order):
            return False
    return True


def boundary_coset_orders(mask: int, n: int, t: int) -> list[int]:
    return [
        order
        for order in divisors(n)
        if order >= t and is_union_of_cosets(mask, n, order)
    ]


def scan_cell(n: int, p: int, t: int, b: int, role: str, deadline: float) -> dict[str, Any]:
    if (p - 1) % n:
        raise ValueError(f"p={p} is not 1 mod N={n}")
    zeta = pow(primitive_root(p), (p - 1) // n, p)
    if pow(zeta, n, p) != 1:
        raise AssertionError("bad root of unity")

    moments = [
        tuple(pow(zeta, m * a, p) for m in range(1, t + 1))
        for a in range(n)
    ]
    h1 = b // 2
    h2 = b - h1
    table: dict[tuple[int, ...], list[int]] = defaultdict(list)
    partial = False

    for combo in itertools.combinations(range(n), h1):
        if time.monotonic() >= deadline:
            partial = True
            break
        table[combo_sum(combo, moments, p, t)].append(mask_from_combo(combo))

    blocks: set[int] = set()
    if not partial:
        for combo in itertools.combinations(range(n), h2):
            if time.monotonic() >= deadline:
                partial = True
                break
            key = tuple((-x) % p for x in combo_sum(combo, moments, p, t))
            m2 = mask_from_combo(combo)
            for m1 in table.get(key, ()):
                if m1 & m2:
                    continue
                block = m1 | m2
                if block.bit_count() == b:
                    blocks.add(block)

    primitive: list[int] = []
    boundary: list[int] = []
    nonboundary: list[int] = []
    for block in blocks:
        if has_dihedral_symmetry(block, n):
            continue
        primitive.append(block)
        if boundary_coset_orders(block, n, t):
            boundary.append(block)
        else:
            nonboundary.append(block)

    return {
        "N": n,
        "p": p,
        "t": t,
        "b": b,
        "role": role,
        "partial": partial,
        "half_split": [h1, h2],
        "left_combinations": sum(len(v) for v in table.values()),
        "left_sum_classes": len(table),
        "tnull_blocks": len(blocks),
        "primitive_blocks": len(primitive),
        "primitive_boundary_coset_blocks": len(boundary),
        "primitive_nonboundary_blocks": len(nonboundary),
        "primitive_nonboundary_examples": [mask_to_list(m, n) for m in sorted(nonboundary)[:5]],
        "boundary_coset_orders_seen": sorted(
            {
                order
                for m in primitive
                for order in boundary_coset_orders(m, n, t)
            }
        ),
    }


def checkpoint(results: dict[str, Any]) -> None:
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")


def summarize(results: dict[str, Any]) -> None:
    cells = results.get("cells", [])
    positive = [c for c in cells if c["role"] == "positive_control"]
    clean = [c for c in cells if c["role"] == "clean_control"]
    exploratory = [c for c in cells if c["role"] == "exploratory"]
    failures: list[dict[str, Any]] = []
    failures.extend(c for c in positive if not c.get("partial") and c.get("primitive_nonboundary_blocks", 0) == 0)
    failures.extend(c for c in clean if c.get("primitive_nonboundary_blocks", 0) > 0)
    failures.extend(c for c in cells if c.get("partial"))
    results["summary"] = {
        "status": "FAIL" if failures else "PASS",
        "cells_checked": len(cells),
        "positive_controls": len(positive),
        "positive_controls_detected": sum(1 for c in positive if c.get("primitive_nonboundary_blocks", 0) > 0),
        "clean_controls": len(clean),
        "clean_controls_with_primitive_nonboundary": sum(
            1 for c in clean if c.get("primitive_nonboundary_blocks", 0) > 0
        ),
        "exploratory_cells": len(exploratory),
        "max_primitive_nonboundary_blocks": max(
            (c.get("primitive_nonboundary_blocks", 0) for c in cells),
            default=0,
        ),
        "failures": [
            {
                "N": c["N"],
                "p": c["p"],
                "t": c["t"],
                "b": c["b"],
                "role": c["role"],
                "primitive_nonboundary_blocks": c.get("primitive_nonboundary_blocks", 0),
                "partial": c.get("partial", False),
            }
            for c in failures
        ],
    }


def planned_cells() -> list[tuple[int, int, int, int, str]]:
    return [
        # Reproduce the known t=3 primitive block side of the F2/U2 transition.
        (64, 257, 3, 8, "positive_control"),
        (64, 577, 3, 8, "positive_control"),
        # Clean controls recorded in the certifier note.
        (64, 641, 3, 8, "clean_control"),
        (64, 769, 3, 8, "clean_control"),
        # Smaller nearby cells broaden the scan without changing the verdict.
        (32, 97, 3, 6, "exploratory"),
        (32, 193, 3, 6, "exploratory"),
        (32, 193, 4, 8, "exploratory"),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=55.0)
    args = parser.parse_args()

    deadline = time.monotonic() + args.time_limit
    results: dict[str, Any] = {
        "started_at_unix": time.time(),
        "node": "u2c_giant_tnull_dichotomy / x4_exactlist_staircase_split",
        "time_limit_seconds": args.time_limit,
        "cells": [],
    }
    checkpoint(results)

    for n, p, t, b, role in planned_cells():
        if time.monotonic() + 2.0 >= deadline:
            break
        t0 = time.monotonic()
        cell = scan_cell(n, p, t, b, role, deadline)
        cell["wall_seconds"] = round(time.monotonic() - t0, 6)
        results["cells"].append(cell)
        summarize(results)
        checkpoint(results)

    results["finished_at_unix"] = time.time()
    summarize(results)
    checkpoint(results)
    print(json.dumps(results["summary"], indent=2, sort_keys=True))
    if results["summary"]["status"] == "PASS":
        print("PASS: U2-C t-null boundary scan found no clean-control primitive nonboundary blocks")
    else:
        print("FAIL: U2-C t-null boundary scan found an alarm or incomplete cell")
    return 0 if results["summary"]["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
