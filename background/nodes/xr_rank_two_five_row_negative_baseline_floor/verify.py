#!/usr/bin/env python3
"""Verify the XR five-row negative-baseline rank floor."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_rank_two_five_row_negative_baseline_floor"
PARENTS = {
    "xr_rank_two_zero_baseline_arithmetic_router",
    "xr_rank_two_maxwell_collision_defect_identity",
    "xr_higher_rank_rank_two_shell_maxwell_router",
}
CONSUMER = "xr_highcore_collision_count"
ROWS = (
    ("RowC-1/4", 5, 5, 4, 9),
    ("RowC-1/8", 5, 5, 4, 9),
    ("RowC-1/16", 3, 3, 3, 6),
    ("prize-1/4", (1 << 33) + 1, 3, 2386092945, 9544371773),
    ("prize-1/8", (1 << 33) + 1, 3, 2386092945, 9544371773),
    ("prize-1/16", (1 << 32) + 1, 5, 1193046474, 4772185889),
)


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def row_floor(h: int) -> tuple[int, int, int, int]:
    b0 = next(b for b in range(1, 7) if (5 * h + b) % 6 == 0)
    D = ceil_div(5 * h + b0 + 30, 18)
    Z = (5 * h + 12 * D + b0) // 6
    assert 6 * Z == 5 * h + 12 * D + b0
    assert Z <= 5 * (D - 1)
    a = Z - D
    return b0, D, Z, a


def formula_check() -> int:
    checks = 0
    for h in range(1, 200, 2):
        b0, D0, _Z0, a0 = row_floor(h)
        assert b0 in (1, 3, 5)
        assert (5 * h + b0) % 6 == 0
        for q in range(8):
            b = b0 + 6 * q
            D = ceil_div(5 * h + b + 30, 18)
            Z = (5 * h + 12 * D + b) // 6
            assert Z <= 5 * (D - 1)
            assert Z - D >= a0

            lower = max(0, ceil_div(b - h + 1, 2))
            upper = b // 2
            for charge in range(lower, upper + 1):
                surplus = b - 2 * charge
                assert 0 <= surplus <= h - 1
            checks += 1
    return checks


def official_check() -> int:
    for _name, h, expected_b, expected_D, expected_a in ROWS:
        b, D, _Z, a = row_floor(h)
        assert (b, D, a) == (expected_b, expected_D, expected_a)
        assert h % 2 == 1
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
        "D_0<0",
        "bcongruent-5h(mod6)",
        "Z<=5(D-1)",
        "b=e+2C",
        "doesnottreataproperfive-blockcircuit",
    ):
        assert marker in statement


def main() -> None:
    checks = formula_check()
    rows = official_check()
    packet_check()
    print(
        "XR_RANK_TWO_FIVE_ROW_NEGATIVE_BASELINE_FLOOR_PASS "
        f"rows={rows} formula_checks={checks}"
    )


if __name__ == "__main__":
    main()
