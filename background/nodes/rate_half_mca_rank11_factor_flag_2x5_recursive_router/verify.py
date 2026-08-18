#!/usr/bin/env python3
"""Exact optimizer for the KoalaBear two-by-five factor-flag router."""

from __future__ import annotations

import argparse
import copy
from math import comb


N = 2_097_152
K = 1_048_576
M = 1_116_048
TAU = 1_679
A = M - TAU
MULTIPLICITY = N - A
H = 38_385
BUDGET = 274_980_728_111_395_087
TRANSVERSE = 209_812_758_437_679_617
AVAILABLE = BUDGET - TRANSVERSE


def affine_cap(dimension: int) -> int:
    return comb(N - K + dimension, dimension) // comb(A - K + dimension, dimension)


R = {dimension: MULTIPLICITY * affine_cap(dimension) for dimension in (4, 5, 6)}
FALL2 = M * (M - 1)
FALL3 = FALL2 * (M - 2)


def cell(factor_cutoff: int, residual_h: int) -> dict[str, int]:
    residual_roots = H - factor_cutoff + 1
    gap = residual_roots - residual_h
    assert factor_cutoff >= 1 and gap > 0
    factor_classes = M // factor_cutoff
    residual_dim2 = FALL3 // gap**3
    residual_dim3 = FALL2 // gap**2
    factor_cost = factor_classes * R[5]
    dim2_cost = residual_dim2 * R[4]
    dim3_cost = residual_dim3 * R[6]
    union_cost = factor_cost + dim2_cost + dim3_cost
    return {
        "factor_cutoff": factor_cutoff,
        "residual_h": residual_h,
        "residual_roots": residual_roots,
        "gap": gap,
        "factor_classes": factor_classes,
        "residual_dim2": residual_dim2,
        "residual_dim3": residual_dim3,
        "factor_cost": factor_cost,
        "dim2_cost": dim2_cost,
        "dim3_cost": dim3_cost,
        "union_cost": union_cost,
        "total": TRANSVERSE + union_cost,
        "slack": AVAILABLE - union_cost,
    }


def max_h(factor_cutoff: int) -> int:
    residual_roots = H - factor_cutoff + 1
    if residual_roots <= 2 or cell(factor_cutoff, 2)["union_cost"] > AVAILABLE:
        return -1
    low, high = 2, residual_roots - 1
    while low <= high:
        middle = (low + high) // 2
        if cell(factor_cutoff, middle)["union_cost"] <= AVAILABLE:
            low = middle + 1
        else:
            high = middle - 1
    return high


def scan() -> dict[str, object]:
    paying = []
    for cutoff in range(1, H):
        h = max_h(cutoff)
        if h >= 0:
            paying.append((cutoff, h))
    global_h = max(h for _, h in paying)
    maxima = [(cutoff, h) for cutoff, h in paying if h == global_h]
    selected = max(maxima, key=lambda item: cell(*item)["slack"])
    return {"global_h": global_h, "maxima": maxima, "selected": selected}


def build() -> dict[str, object]:
    assert R == {4: 63_397_365_764, 5: 1_010_335_321_405, 6: 16_100_859_197_492}
    selected = cell(408, 18165)
    expected = {
        "factor_cutoff": 408,
        "residual_h": 18165,
        "residual_roots": 37978,
        "gap": 19813,
        "factor_classes": 2735,
        "residual_dim2": 178729,
        "residual_dim3": 3172,
        "factor_cost": 2763267104042675,
        "dim2_cost": 11330947785633956,
        "dim3_cost": 51071925374444624,
        "union_cost": 65166140264121255,
        "total": 274978898701800872,
        "slack": 1829409594215,
    }
    assert selected == expected
    adjacent = cell(408, 18166)
    assert adjacent["total"] - BUDGET == 15_983_178_478_905
    exact_scan = scan()
    assert exact_scan == {
        "global_h": 18165,
        "maxima": [(408, 18165), (411, 18165)],
        "selected": (408, 18165),
    }
    return {"selected": selected, "adjacent": adjacent, "scan": exact_scan}


def tamper_selftest(result: dict[str, object]) -> int:
    caught = 0
    for section, key, value in (
        ("selected", "factor_classes", 2734),
        ("selected", "residual_dim2", 178728),
        ("selected", "union_cost", AVAILABLE + 1),
        ("adjacent", "total", BUDGET),
        ("scan", "global_h", 18166),
    ):
        changed = copy.deepcopy(result)
        changed[section][key] = value
        try:
            assert changed == result
        except AssertionError:
            caught += 1
    assert caught == 5
    return caught


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        print(f"RANK11_FACTOR_FLAG_2X5_TAMPER_PASS mutations={tamper_selftest(result)}/5")
        return
    selected = result["selected"]
    print(
        "RANK11_FACTOR_FLAG_2X5_PASS "
        f"T={selected['factor_cutoff']} h={selected['residual_h']} "
        f"union={selected['union_cost']} slack={selected['slack']}"
    )


if __name__ == "__main__":
    main()
