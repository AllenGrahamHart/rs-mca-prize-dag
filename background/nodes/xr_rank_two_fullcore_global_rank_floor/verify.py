#!/usr/bin/env python3
"""Verify the XR global full-core rank floor."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_rank_two_fullcore_global_rank_floor"
PARENTS = {
    "xr_rank_two_zero_baseline_arithmetic_router",
    "xr_rank_two_maxwell_collision_defect_identity",
    "xr_higher_rank_rank_two_shell_maxwell_router",
    "xr_higher_rank_uniform_split_pencil_reduction",
    "xr_prize_primitive_rank_two_shell_band",
}
CONSUMER = "xr_highcore_collision_count"
ROWS = (
    ("RowC-1/4", 5, 258, (8, 4, 4, 12, 4), 10),
    ("RowC-1/8", 5, 130, (8, 4, 4, 12, 4), 10),
    ("RowC-1/16", 3, 66, (5, 4, 3, 8, 2), 6),
    (
        "prize-1/4",
        (1 << 33) + 1,
        384,
        (8_590_051_854, 384, 22_428_335, 8_612_480_189, 174),
        8_601_474_050,
    ),
    (
        "prize-1/8",
        (1 << 33) + 1,
        448,
        (8_590_020_865, 448, 19_217_050, 8_609_237_915, 416),
        8_601_474_050,
    ),
    (
        "prize-1/16",
        (1 << 32) + 1,
        960,
        (4_294_977_670, 958, 4_487_961, 4_299_465_631, 734),
        4_302_648_690,
    ),
)


def mass_floor(t: int, D: int) -> int:
    return t * D // 2 if D % 2 == 0 else t * (D + 1) // 2 - 1


def negative_floor(h: int, t: int) -> tuple[int, int, int, int]:
    numerator = t * h + 2 * t * (t - 2)
    denominator = (t - 2) * (t + 1)
    D = max(3, numerator // denominator + 1)

    baseline = t * h + (t - 2) * (t - 1) * D
    scale = 2 * (t - 2)
    Z = max(mass_floor(t, D), baseline // scale + 1)
    b = scale * Z - baseline
    a = Z - D

    assert b > 0
    assert Z <= t * (D - 1)
    assert a >= D and a >= t - 2
    return a, D, Z, b


def formula_check() -> int:
    checks = 0
    for h in range(1, 200, 2):
        for t in range(4, 81):
            a0, D0, Z0, b0 = negative_floor(h, t)
            assert b0 == 2 * (t - 2) * Z0 - (
                t * h + (t - 2) * (t - 1) * D0
            )
            assert Z0 >= mass_floor(t, D0)
            assert a0 == Z0 - D0
            assert a0 >= D0 and a0 >= t - 2

            if D0 > 3:
                prior = D0 - 1
                prior_baseline = t * h + (t - 2) * (t - 1) * prior
                assert prior_baseline >= 2 * (t - 2) * t * (prior - 1)

            previous = a0
            for D in range(D0, D0 + 9):
                baseline = t * h + (t - 2) * (t - 1) * D
                Z = max(mass_floor(t, D), baseline // (2 * (t - 2)) + 1)
                floor = Z - D
                assert floor >= previous
                previous = floor
                checks += 1
    return checks


def official_check() -> int:
    for _name, h, t_max, expected, zero_floor in ROWS:
        candidates = []
        for t in range(4, t_max + 1):
            a, D, Z, b = negative_floor(h, t)
            candidates.append((a, t, D, Z, b))
        actual = min(candidates)
        assert actual == expected
        assert zero_floor > actual[0]
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
        "D_-(h,t)=max{3",
        "Z_-(h,t)=max",
        "8,590,051,854",
        "4,294,977,670",
        "notanexistencetheorem",
        "properfour/five-blockcircuit",
    ):
        assert marker in statement


def main() -> None:
    checks = formula_check()
    rows = official_check()
    packet_check()
    print(
        "XR_RANK_TWO_FULLCORE_GLOBAL_RANK_FLOOR_PASS "
        f"rows={rows} formula_checks={checks}"
    )


if __name__ == "__main__":
    main()
