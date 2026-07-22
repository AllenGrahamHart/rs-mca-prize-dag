#!/usr/bin/env python3
"""Verify the XR prize uniform-trade private-point floor."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_prize_uniform_trade_private_point_rank_floor"
PARENTS = {
    "xr_higher_rank_uniform_split_pencil_reduction",
    "xr_prize_primitive_rank_two_shell_band",
    "xr_target_budget_audit",
}
CONSUMER = "xr_highcore_collision_count"
ROWS = (
    ("prize-1/4", (1 << 33) + 1, 384, 11_243_370),
    ("prize-1/8", (1 << 33) + 1, 448, 9_629_972),
    ("prize-1/16", (1 << 32) + 1, 960, 2_241_633),
)


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def rank_floor(h: int, L: int) -> int:
    return ceil_div(h + 1, 2 * (L - 2))


def multiplicity_check() -> int:
    checks = 0
    for t in range(3, 24):
        for encoded in range(1 << min(t, 12)):
            histogram = [((encoded >> (m - 1)) & 1) for m in range(1, t + 1)]
            S = sum(m * histogram[m - 1] for m in range(1, t + 1))
            Q = sum(
                m * (m - 1) // 2 * histogram[m - 1]
                for m in range(1, t + 1)
            )
            P = histogram[0]
            assert P >= S - 2 * Q
            checks += 1
    return checks


def algebra_check() -> int:
    checks = 0
    for h in range(1, 100, 2):
        for L in range(4, 100):
            floor = rank_floor(h, L)
            assert 2 * (L - 2) * floor >= h + 1
            assert 2 * (L - 2) * (floor - 1) < h + 1
            for t in range(3, L + 1):
                a = floor - 1
                lower = t * h - t * (t - 2) * a
                upper = t * (h - 1) // 2 + (L - t) * t * a
                assert lower > upper
                checks += 1
    return checks


def official_check() -> int:
    for _name, h, L, expected in ROWS:
        assert rank_floor(h, L) == expected
    return len(ROWS)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "P_J>=th-t(t-2)a",
        "ceil((h+1)/(2(L-2)))",
        "11,243,370",
        "2,241,633",
        "coverseverytrade-matrixrank",
    ):
        assert marker in statement


def main() -> None:
    multiplicity_checks = multiplicity_check()
    algebra_checks = algebra_check()
    rows = official_check()
    packet_check()
    print(
        "XR_PRIZE_UNIFORM_TRADE_PRIVATE_POINT_RANK_FLOOR_PASS "
        f"rows={rows} multiplicity_checks={multiplicity_checks} "
        f"algebra_checks={algebra_checks}"
    )


if __name__ == "__main__":
    main()
