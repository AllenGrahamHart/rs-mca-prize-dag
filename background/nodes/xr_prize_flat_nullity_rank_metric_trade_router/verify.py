#!/usr/bin/env python3
"""Verify the XR flat-nullity rank-metric trade router."""

from __future__ import annotations

import json
from math import ceil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_prize_flat_nullity_rank_metric_trade_router"
PARENT = "xr_prize_flat_nullity_maxwell_trade_space_compiler"
CONSUMER = "xr_highcore_collision_count"
ROWS = (
    ("prize-1/4", 4, 256, 16, 12, 18),
    ("prize-1/8", 8, 256, 16, 9, 13),
    ("prize-1/16", 16, 512, 14, 9, 13),
)


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def algebra_check() -> int:
    checks = 0
    for a in range(1, 8):
        for h in range(1, 8):
            for s in range(0, 12):
                for t in range(3, 12):
                    for e in range(h):
                        numerator = h * t - e
                        if numerator % 2:
                            continue
                        union = a + s + numerator // 2
                        dimension = s * (t - 2) + e + 1
                        compressed_rows = t - 2
                        assert 1 <= dimension <= compressed_rows * union
                        q = ceil_div(dimension, union)
                        rank_bound = t - 1 - q
                        assert 1 <= rank_bound <= compressed_rows
                        assert dimension > (compressed_rows - rank_bound) * union

                        no_rank_one = dimension <= (t - 3) * union
                        rm4 = 2 * s + (t - 1) * e + 2 <= (t - 3) * (
                            2 * a + h * t
                        )
                        assert no_rank_one == rm4

                        if t >= 4:
                            no_rank_two = dimension <= (t - 4) * union
                            rm5 = 4 * s + (t - 2) * e + 2 <= (t - 4) * (
                                2 * a + h * t
                            )
                            assert no_rank_two == rm5
                        checks += 5
    return checks


def official_check() -> int:
    n = 1 << 41
    checks = 0
    for _name, rate, scale, a, expected_one, expected_two in ROWS:
        k = n // rate
        h = n // scale + 1
        s = k - a
        rank_one = [
            t
            for t in range(3, 1000)
            if 2 * s + 2 > (t - 3) * (2 * a + h * t)
        ]
        rank_two = [
            t
            for t in range(3, 1000)
            if t <= 3 or 4 * s + 2 > (t - 4) * (2 * a + h * t)
        ]
        assert max(rank_one) == expected_one
        assert max(rank_two) == expected_two
        assert expected_one + 1 not in rank_one
        assert expected_two + 1 not in rank_two
        checks += 4
    return checks


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PARENT]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "D>(t-2-r)M",
        "t-1-ceil(D/M)",
        "12,9,9",
        "18,13,13",
    ):
        assert marker in statement


def main() -> None:
    algebra = algebra_check()
    official = official_check()
    packet_check()
    print(
        "XR_PRIZE_FLAT_NULLITY_RANK_METRIC_TRADE_ROUTER_PASS "
        f"algebra_checks={algebra} official_checks={official}"
    )


if __name__ == "__main__":
    main()
