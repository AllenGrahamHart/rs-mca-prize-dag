#!/usr/bin/env python3
"""Verify the XR prize proper-circuit private-point floor."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_prize_rank_two_proper_circuit_private_point_floor"
PARENTS = {
    "xr_rank_two_proper_circuit_defect_host_router",
    "xr_rank_two_extension_family_collision_ledger",
    "xr_higher_rank_uniform_split_pencil_reduction",
    "xr_prize_primitive_rank_two_shell_band",
    "xr_trade_circuit_arity_segre_atlas",
}
COMPOSED_PARENT = "xr_rank_two_fullcore_global_rank_floor"
CONSUMER = "xr_highcore_collision_count"
ROWS = (
    (
        "prize-1/4",
        (1 << 33) + 1,
        384,
        (11_265_488, 11_290_661),
        11_265_488,
        8_590_051_854,
    ),
    (
        "prize-1/8",
        (1 << 33) + 1,
        448,
        (9_646_193, 9_664_643),
        9_646_193,
        8_590_020_865,
    ),
    (
        "prize-1/16",
        (1 << 32) + 1,
        960,
        (2_243_389, 2_245_383),
        2_243_389,
        4_294_977_670,
    ),
)


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def rank_floor(h: int, L: int, t: int) -> int:
    numerator = t * (h + 1) // 2 + 3 * (t - 1) * (t - 3)
    denominator = t * L - t * (t - 2) - 3
    assert denominator > 0
    return ceil_div(numerator, denominator)


def multiplicity_identity_check() -> int:
    checks = 0
    for t in (4, 5):
        for counts in range(1 << (3 * t)):
            # Decode small multiplicity histograms n_m in {0,...,7}.
            value = counts
            histogram = []
            for _m in range(1, t + 1):
                histogram.append(value & 7)
                value >>= 3
            S = sum(m * histogram[m - 1] for m in range(1, t + 1))
            Q2 = sum(
                m * (m - 1) // 2 * histogram[m - 1]
                for m in range(1, t + 1)
            )
            H = sum(
                (m - 1) * (m - 2) // 2 * histogram[m - 1]
                for m in range(1, t + 1)
            )
            P1 = histogram[0]
            assert P1 >= S - 2 * Q2 + 2 * H
            checks += 1
    return checks


def formula_check() -> int:
    checks = 0
    for h in range(1, 100, 2):
        for L in range(6, 80):
            for t in (4, 5):
                if L < t:
                    continue
                floor = rank_floor(h, L, t)
                numerator = t * (h + 1) // 2 + 3 * (t - 1) * (t - 3)
                denominator = t * L - t * (t - 2) - 3
                assert denominator * floor >= numerator
                if floor > 0:
                    assert denominator * (floor - 1) < numerator
                checks += 1
    return checks


def official_check() -> int:
    for _name, h, L, expected_pair, expected_min, full_floor in ROWS:
        actual = tuple(rank_floor(h, L, t) for t in (4, 5))
        assert actual == expected_pair
        assert min(actual) == expected_min
        assert full_floor > expected_min
    return len(ROWS)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert nodes[COMPOSED_PARENT]["status"] == "PROVED"
    assert (COMPOSED_PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "P_1>=th+t(t-2)D-(2t-3)Z+2C+I",
        "11,265,488",
        "2,243,389",
        "notanexistencetheorem",
        "trade-matrixrankatleastthree",
    ):
        assert marker in statement


def main() -> None:
    multiplicity_checks = multiplicity_identity_check()
    formula_checks = formula_check()
    rows = official_check()
    packet_check()
    print(
        "XR_PRIZE_RANK_TWO_PROPER_CIRCUIT_PRIVATE_POINT_FLOOR_PASS "
        f"rows={rows} multiplicity_checks={multiplicity_checks} "
        f"formula_checks={formula_checks}"
    )


if __name__ == "__main__":
    main()
