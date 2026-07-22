#!/usr/bin/env python3
"""Verify the prize u=0 loop-defect Maxwell/rank-one compiler."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_prize_u0_loop_defect_maxwell_rank_one_compiler"
PARENTS = {
    "xr_rs_flat_nullity_basis_charge",
    "xr_prize_flat_nullity_effective_core_floor",
    "xr_prize_flat_nullity_nonpersistent_root_cap",
    "xr_higher_rank_uniform_split_pencil_reduction",
}
CONSUMER = "xr_highcore_collision_count"
ROWS = (
    ("prize-1/4", 4, 256, 16, 11_243_354, 1_526_176_110),
    ("prize-1/8", 8, 256, 16, 9_629_956, 2_902_067_939),
    ("prize-1/16", 16, 512, 14, 2_241_619, 1_962_285_106),
)


def inverse(value: int, prime: int) -> int:
    return pow(value % prime, prime - 2, prime)


def locator_derivative(points: tuple[int, ...], x: int, prime: int) -> int:
    value = 1
    for y in points:
        if y != x:
            value = value * (x - y) % prime
    return value


def official_check() -> int:
    n = 1 << 41
    budget = 8 * n**3
    checks = 0
    for _name, rate, scale, a, lower, upper in ROWS:
        k = n // rate
        h = n // scale + 1
        r = n - k
        assert 0 < lower <= upper < k - a < budget
        assert h * (budget + 1 - upper) > 2 * (r + a) - 2 * (a + upper)
        checks += 2
    return checks


def dimension_check() -> int:
    checks = 0
    for a in range(2, 8):
        for h in range(1, 9):
            for v in range(1, 7):
                for t in range(3, 10):
                    for e in range(h):
                        numerator = h * t + 2 * (a + v) - e
                        if numerator % 2:
                            continue
                        union = numerator // 2
                        rows = (h + v) * t
                        rank_cap = 2 * union - (2 * a + 1)
                        assert rows - rank_cap == v * (t - 2) + e + 1
                        checks += 1
    return checks


def rank_one_fixture_check() -> tuple[int, int]:
    prime = 101
    slopes = (1, 2, 4)
    alpha = (
        slopes[1] - slopes[2],
        slopes[2] - slopes[0],
        slopes[0] - slopes[1],
    )
    assert sum(alpha) % prime == 0
    assert sum(x * y for x, y in zip(slopes, alpha, strict=True)) % prime == 0

    checks = 0
    mutations = 0
    for a, v, h, support, q_coefficients in (
        (2, 2, 3, (1, 3, 5), (7,)),
        (2, 2, 3, (1, 3, 5, 7), (7, 2)),
        (3, 2, 2, (1, 3, 5, 7), (9,)),
    ):
        m = a + h + v
        outside_size = m - len(support)
        blocks = tuple(
            support
            + tuple(10 + 10 * index + offset for offset in range(outside_size))
            for index in range(3)
        )
        base = {}
        for x in support:
            qx = sum(coefficient * pow(x, degree, prime) for degree, coefficient in enumerate(q_coefficients)) % prime
            assert qx
            base[x] = qx * inverse(locator_derivative(support, x, prime), prime) % prime

        rows = []
        for coefficient, block in zip(alpha, blocks, strict=True):
            row = {x: coefficient * base.get(x, 0) % prime for x in block}
            for degree in range(a):
                assert sum(value * pow(x, degree, prime) for x, value in row.items()) % prime == 0
            rows.append(row)

        domain = set().union(*map(set, blocks))
        for x in domain:
            assert sum(row.get(x, 0) for row in rows) % prime == 0
            assert sum(
                slope * row.get(x, 0)
                for slope, row in zip(slopes, rows, strict=True)
            ) % prime == 0
            checks += 2

        broken = list(alpha)
        broken[0] += 1
        assert sum(broken) % prime != 0
        mutations += 1
    return checks, mutations


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
        "v(t-2)+e+1",
        "a+1<=w=|S|<=a+v",
        "11,243,354<=v<=1,526,176,110",
        "structuralcompiler",
    ):
        assert marker in statement


def main() -> None:
    official = official_check()
    dimensions = dimension_check()
    fixtures, mutations = rank_one_fixture_check()
    packet_check()
    print(
        "XR_PRIZE_U0_LOOP_DEFECT_MAXWELL_RANK_ONE_COMPILER_PASS "
        f"official_checks={official} dimension_checks={dimensions} "
        f"fixture_checks={fixtures} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
