#!/usr/bin/env python3
"""Exact verifier for the KoalaBear rank-eleven low-span payment."""

from __future__ import annotations

import argparse
import copy
from math import comb, prod


ROW = {
    "p": 2_130_706_433,
    "extension_degree": 6,
    "n": 2_097_152,
    "K": 1_048_576,
    "m": 1_116_048,
    "w": 67_472,
    "near": 134_944,
    "budget": 274_980_728_111_395_087,
    "theta_resource_s10": 106_618_568_137_036_225_644,
    "rank1_group_cap": 8_147_918,
}

TAU = 1_549
H = 42_451


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def falling(value: int, length: int) -> int:
    return prod(value - index for index in range(length))


def affine_cap(tau: int, dimension: int) -> int:
    if dimension == 0:
        return 1
    A = ROW["m"] - tau
    return comb(ROW["n"] - ROW["K"] + dimension, dimension) // comb(
        A - ROW["K"] + dimension, dimension
    )


def build_envelope(tau: int, h: int) -> dict[str, int | bool | list[int]]:
    n, K, m = (ROW[key] for key in ("n", "K", "m"))
    A = m - tau
    c = 2 * A - n
    require(1 <= tau < ROW["w"] and 0 <= h < c, "legal cell")
    multiplicity = n - A
    caps = [affine_cap(tau, dimension) for dimension in range(7)]
    m2 = caps[2]
    m3 = caps[3]
    m6 = caps[6]
    r2 = multiplicity * m2
    r3 = multiplicity * m3
    r6 = multiplicity * m6
    n1 = falling(m, 9) // (c - h) ** 9
    n2 = falling(m, 8) // (c - h) ** 8
    rank1_total = n1 * ROW["rank1_group_cap"]
    rank2_total = n2 * r2
    high_tail = ROW["theta_resource_s10"] // (tau + 1)
    transverse = ROW["near"] + high_tail + multiplicity + rank1_total + rank2_total
    total = transverse + r6
    residual = ROW["budget"] + 1 - transverse
    return {
        "tau": tau,
        "h": h,
        "A": A,
        "d": A - K,
        "c": c,
        "multiplicity": multiplicity,
        "affine_caps_0_to_6": caps,
        "M2": m2,
        "M3": m3,
        "M6": m6,
        "R2": r2,
        "R3": r3,
        "R6": r6,
        "N1": n1,
        "N2": n2,
        "rank1_total": rank1_total,
        "rank2_total": rank2_total,
        "high_tail": high_tail,
        "transverse": transverse,
        "total": total,
        "slack": ROW["budget"] - total,
        "residual": residual,
        "row_spaces": (residual + r2 - 1) // r2,
        "containers": (residual + r3 - 1) // r3,
        "field_guard": m6 * m6 < ROW["p"] ** ROW["extension_degree"],
    }


def max_paying_h(tau: int) -> int:
    c = 2 * (ROW["m"] - tau) - ROW["n"]
    if c <= 0 or build_envelope(tau, 0)["total"] > ROW["budget"]:
        return -1
    low, high, best = 0, c - 1, -1
    while low <= high:
        middle = (low + high) // 2
        if build_envelope(tau, middle)["total"] <= ROW["budget"]:
            best = middle
            low = middle + 1
        else:
            high = middle - 1
    return best


def scan() -> dict[str, object]:
    paying = []
    for tau in range(1, ROW["w"]):
        h = max_paying_h(tau)
        if h >= 0:
            paying.append((tau, h))
    global_h = max(h for _, h in paying)
    maxima = [(tau, h) for tau, h in paying if h == global_h]
    best_slack = max(
        (build_envelope(tau, h)["slack"], tau) for tau, h in maxima
    )
    return {
        "first": paying[0],
        "last": paying[-1],
        "global_h": global_h,
        "maxima": maxima,
        "best_slack_tau": best_slack[1],
    }


def build() -> dict[str, object]:
    selected = build_envelope(TAU, H)
    adjacent = build_envelope(TAU, H + 1)
    expected = {
        "tau": 1549,
        "h": 42451,
        "A": 1114499,
        "d": 65923,
        "c": 131846,
        "multiplicity": 982653,
        "affine_caps_0_to_6": [1, 15, 252, 4023, 64001, 1017939, 16190045],
        "M2": 252,
        "M3": 4023,
        "M6": 16190045,
        "R2": 247628556,
        "R3": 3953213019,
        "R6": 15909196289385,
        "N1": 7367375311,
        "N2": 590128056,
        "rank1_total": 60028769909252498,
        "rank2_total": 146132558362367136,
        "high_tail": 68786172991636274,
        "transverse": 274947501264373505,
        "total": 274963410460662890,
        "slack": 17317650732197,
        "residual": 33226847021583,
        "row_spaces": 134181,
        "containers": 8406,
        "field_guard": True,
    }
    require(selected == expected, "selected exact ledger")
    require(adjacent["total"] - ROW["budget"] == 1_804_196_591_101,
            "adjacent payment wall")
    exact_scan = scan()
    require(
        exact_scan == {
            "first": (397, 68),
            "last": (21131, 1),
            "global_h": 42451,
            "maxima": [(1547, 42451), (1548, 42451), (1549, 42451)],
            "best_slack_tau": 1549,
        },
        "global cutoff scan",
    )
    return {"selected": selected, "adjacent": adjacent, "scan": exact_scan}


def tamper_selftest(result: dict[str, object]) -> int:
    caught = 0
    for section, key, value in (
        ("selected", "R6", result["selected"]["R6"] - 1),
        ("selected", "containers", 8405),
        ("selected", "field_guard", False),
        ("adjacent", "total", ROW["budget"]),
        ("scan", "global_h", 42452),
    ):
        changed = copy.deepcopy(result)
        changed[section][key] = value
        try:
            require(changed == result, "canonical result")
        except AssertionError:
            caught += 1
    require(caught == 5, "all hostile mutations caught")
    return caught


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        print(f"RANK11_LOW_SPAN_TAMPER_PASS mutations={tamper_selftest(result)}/5")
        return
    selected = result["selected"]
    print(
        "RANK11_LOW_SPAN_PASS "
        f"tau={selected['tau']} h={selected['h']} span_floor=7 "
        f"containers={selected['containers']} total={selected['total']} "
        f"slack={selected['slack']}"
    )


if __name__ == "__main__":
    main()
