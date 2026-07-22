#!/usr/bin/env python3
"""Verify the XR prize effective-core floor."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_prize_flat_nullity_effective_core_floor"
PARENTS = {
    "xr_rs_flat_nullity_basis_charge",
    "xr_rs_common_root_basis_charge",
    "xr_target_budget_audit",
}
CONSUMER = "xr_highcore_collision_count"
ROWS = (
    ("prize-1/4", (1 << 33) + 1, 384, 16, 11_243_370, 11_243_354),
    ("prize-1/8", (1 << 33) + 1, 448, 16, 9_629_972, 9_629_956),
    ("prize-1/16", (1 << 32) + 1, 960, 14, 2_241_633, 2_241_619),
)


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def effective_floor(h: int, L: int) -> int:
    return ceil_div(h + 1, 2 * (L - 2))


def set_family_check() -> int:
    checks = 0
    # Exhaust the small range only. The theorem is symbolic; this check guards
    # the pointwise multiplicity inequality without materializing large block
    # families on the WSL host.
    for N in range(5, 8):
        ground = range(N)
        for kappa in range(1, N - 1):
            for h in range(1, N - kappa + 1):
                blocks = tuple(combinations(ground, kappa + h))
                for t in range(3, min(5, len(blocks) + 1)):
                    for family in combinations(blocks, t):
                        if any(
                            len(set(left) & set(right)) > kappa
                            for left, right in combinations(family, 2)
                        ):
                            continue
                        multiplicities = [
                            sum(x in block for block in family) for x in ground
                        ]
                        private = sum(value == 1 for value in multiplicities)
                        assert private >= t * h - t * (t - 2) * kappa
                        checks += 1
    return checks


def core_algebra_check() -> int:
    checks = 0
    for h in range(1, 100, 2):
        for L in range(4, 100):
            floor = effective_floor(h, L)
            assert 2 * (L - 2) * floor >= h + 1
            assert 2 * (L - 2) * (floor - 1) < h + 1
            for t in range(3, L + 1):
                kappa = floor - 1
                lower = t * h - t * (t - 2) * kappa
                upper = t * (h - 1) // 2
                # The weakest lower-vs-upper comparison occurs at t=L.
                assert lower > upper
                checks += 1
    return checks


def official_check() -> int:
    for _name, h, L, a, expected, expected_uv in ROWS:
        actual = effective_floor(h, L)
        assert actual == expected
        assert actual - a == expected_uv
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
        "kappa=a+u+v",
        "ceil((h+1)/(2(L-2)))",
        "11,243,354",
        "2,241,619",
        "maincontentisnonuniform",
    ):
        assert marker in statement


def main() -> None:
    family_checks = set_family_check()
    algebra_checks = core_algebra_check()
    rows = official_check()
    packet_check()
    print(
        "XR_PRIZE_FLAT_NULLITY_EFFECTIVE_CORE_FLOOR_PASS "
        f"rows={rows} family_checks={family_checks} "
        f"algebra_checks={algebra_checks}"
    )


if __name__ == "__main__":
    main()
