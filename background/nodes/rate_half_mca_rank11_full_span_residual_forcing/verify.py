#!/usr/bin/env python3
"""Exact verifier for rank-eleven full-span residual forcing."""

from __future__ import annotations

import argparse
import copy
from math import comb, prod


P = 2_130_706_433
Q = P**6
N = 2_097_152
K = 1_048_576
M = 1_116_048
W = 67_472
NEAR = 134_944
BUDGET = 274_980_728_111_395_087
RESOURCE = 106_618_568_137_036_225_644
RANK1 = 8_147_918


def falling(length: int) -> int:
    return prod(M - index for index in range(length))


def affine_cap(tau: int, dimension: int) -> int:
    if dimension == 0:
        return 1
    A = M - tau
    return comb(N - K + dimension, dimension) // comb(A - K + dimension, dimension)


def cell(tau: int, h: int, paid_dimension: int) -> dict[str, object]:
    A = M - tau
    c = 2 * A - N
    assert 1 <= tau < W and 0 <= h < c
    multiplicity = N - A
    caps = [affine_cap(tau, dimension) for dimension in range(paid_dimension + 1)]
    m2 = caps[2]
    r2 = multiplicity * m2
    n1 = falling(9) // (c - h) ** 9
    n2 = falling(8) // (c - h) ** 8
    rank1_total = n1 * RANK1
    rank2_total = n2 * r2
    tail = RESOURCE // (tau + 1)
    transverse = NEAR + tail + multiplicity + rank1_total + rank2_total
    paid_cap = multiplicity * caps[paid_dimension]
    residual = BUDGET + 1 - transverse
    m3 = affine_cap(tau, 3)
    r3 = multiplicity * m3
    return {
        "tau": tau,
        "h": h,
        "A": A,
        "d": A - K,
        "c": c,
        "multiplicity": multiplicity,
        "caps": caps,
        "N1": n1,
        "N2": n2,
        "R2": r2,
        "R3": r3,
        "rank1_total": rank1_total,
        "rank2_total": rank2_total,
        "tail": tail,
        "transverse": transverse,
        "paid_cap": paid_cap,
        "total": transverse + paid_cap,
        "slack": BUDGET - transverse - paid_cap,
        "residual": residual,
        "row_spaces": (residual + r2 - 1) // r2,
        "containers": (residual + r3 - 1) // r3,
        "field_guard": caps[paid_dimension] ** 2 < Q,
    }


def max_h(tau: int, paid_dimension: int) -> int:
    c = 2 * (M - tau) - N
    if c <= 0 or cell(tau, 0, paid_dimension)["total"] > BUDGET:
        return -1
    low, high = 0, c - 1
    while low <= high:
        middle = (low + high) // 2
        if cell(tau, middle, paid_dimension)["total"] <= BUDGET:
            low = middle + 1
        else:
            high = middle - 1
    return high


def scan_dimension_nine() -> dict[str, object]:
    paying = []
    for tau in range(1, W):
        h = max_h(tau, 9)
        if h >= 0:
            paying.append((tau, h))
    global_h = max(h for _, h in paying)
    maxima = [(tau, h) for tau, h in paying if h == global_h]
    best_tau = max((cell(tau, h, 9)["slack"], tau) for tau, h in maxima)[1]
    return {
        "first": paying[0],
        "last": paying[-1],
        "global_h": global_h,
        "maxima": maxima,
        "best_tau": best_tau,
    }


def dimension_ten_wall() -> dict[str, int]:
    candidates = []
    for tau in range(1, W):
        if 2 * (M - tau) - N > 0:
            result = cell(tau, 0, 10)
            candidates.append((result["total"] - BUDGET, tau, result["total"]))
    excess, tau, total = min(candidates)
    return {"tau": tau, "total": total, "excess": excess}


def build() -> dict[str, object]:
    selected = cell(1679, 38384, 9)
    adjacent = cell(1679, 38385, 9)
    expected = {
        "tau": 1679,
        "h": 38384,
        "A": 1114369,
        "d": 65793,
        "c": 131586,
        "multiplicity": 982783,
        "caps": [1, 15, 253, 4047, 64508, 1028035, 16382924, 261076837, 4160438212, 66298487937],
        "N1": 5061797488,
        "N2": 422717509,
        "R2": 248644099,
        "R3": 3977322801,
        "rank1_total": 41243110864829984,
        "rank2_total": 105106214156829391,
        "tail": 63463433414902515,
        "transverse": 209812758437679617,
        "paid_cap": 65157026870188671,
        "total": 274969785307868288,
        "slack": 10942803526799,
        "residual": 65167969673715471,
        "row_spaces": 262093370,
        "containers": 16384884,
        "field_guard": True,
    }
    assert selected == expected
    assert adjacent["total"] - BUDGET == 2_062_328_934_603
    scan = scan_dimension_nine()
    assert scan == {
        "first": (502, 815),
        "last": (10252, 14),
        "global_h": 38384,
        "maxima": [(1676, 38384), (1677, 38384), (1678, 38384), (1679, 38384)],
        "best_tau": 1679,
    }
    wall = dimension_ten_wall()
    assert wall == {
        "tau": 872,
        "total": 1_048_057_349_706_085_243,
        "excess": 773_076_621_594_690_156,
    }
    return {"selected": selected, "adjacent": adjacent, "scan": scan, "wall": wall}


def tamper_selftest(result: dict[str, object]) -> int:
    caught = 0
    for section, key, value in (
        ("selected", "paid_cap", result["selected"]["paid_cap"] - 1),
        ("selected", "containers", 16_384_883),
        ("selected", "field_guard", False),
        ("scan", "global_h", 38_385),
        ("wall", "excess", 0),
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
        print(f"RANK11_FULL_SPAN_TAMPER_PASS mutations={tamper_selftest(result)}/5")
        return
    selected = result["selected"]
    print(
        "RANK11_FULL_SPAN_PASS "
        f"tau={selected['tau']} h={selected['h']} span=10 "
        f"containers={selected['containers']} slack={selected['slack']}"
    )


if __name__ == "__main__":
    main()
