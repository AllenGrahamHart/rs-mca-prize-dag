#!/usr/bin/env python3
"""Verify the XR rank-two zero-baseline arithmetic router."""

from __future__ import annotations

import json
from math import isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_rank_two_zero_baseline_arithmetic_router"
PARENTS = {
    "xr_rank_two_maxwell_collision_defect_identity",
    "xr_higher_rank_rank_two_shell_maxwell_router",
    "xr_target_budget_audit",
}
CONSUMER = "xr_highcore_collision_count"
ROWS = (
    ("RowC-1/4", 5, 1 << 8, 2, (10, 1, 4, 10)),
    ("RowC-1/8", 5, 1 << 7, 2, (10, 1, 4, 10)),
    ("RowC-1/16", 3, 1 << 6, 2, (6, 1, 4, 6)),
    ("prize-1/4", (1 << 33) + 1, 1 << 39, 15, (8601474050, 2049, 4100, 2101250)),
    ("prize-1/8", (1 << 33) + 1, 1 << 38, 15, (8601474050, 2049, 4100, 2101250)),
    ("prize-1/16", (1 << 32) + 1, 1 << 37, 2, (4302648690, 641, 1284, 3359586)),
)


def divisors(value: int) -> tuple[int, ...]:
    small = []
    large = []
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor == 0:
            small.append(divisor)
            if divisor * divisor != value:
                large.append(value // divisor)
    return tuple(small + large[::-1])


def least_even_at_least(numerator: int, denominator: int) -> int:
    value = (numerator + denominator - 1) // denominator
    value = max(value, 2)
    return value if value % 2 == 0 else value + 1


def candidates(h: int, k: int | None = None) -> tuple[tuple[int, int, int, int, int], ...]:
    result = []
    for s in divisors(h):
        t = 2 * s + 2
        modulus = t - 3
        quotient = h + h // s
        residue = ((h - h // s) // 2) % modulus
        D = max(
            least_even_at_least(t * h, (t - 3) * (t - 2)),
            least_even_at_least(
                t * (h + 2 * (t - 2)), (t - 2) * (t + 1)
            ),
            least_even_at_least(quotient + 2 * t * residue, modulus),
        )
        upper = h + h // s
        if D > upper:
            continue
        rank_numerator = h + h // s + (2 * s - 1) * D
        assert rank_numerator % 2 == 0
        a_min = rank_numerator // 2
        if k is not None and a_min > k:
            continue
        result.append((a_min, s, t, D, upper))
    return tuple(result)


def formula_check() -> int:
    checks = 0
    for h in range(3, 100, 2):
        for a_min, s, t, D_min, upper in candidates(h):
            for D in range(D_min, upper + 1, 2):
                denominator = 2 * (t - 2)
                Z_numerator = t * h + (t - 2) * (t - 1) * D
                assert Z_numerator % denominator == 0
                Z = Z_numerator // denominator
                assert t * h + (t - 2) * ((t - 1) * D - 2 * Z) == 0

                quotient = t * h // (t - 2)
                assert quotient * (t - 2) == t * h
                Q = (t - 1) * (quotient - D) // 2
                P = ((t - 3) * D - quotient) // 2
                assert P >= 0 and Q >= 0
                assert P + Q == t * h // 2 - D
                constant = h + (t - 2) * D - Z
                residue = constant % (t - 3)
                assert P >= t * residue
                assert (P - t * residue) % (t - 3) == 0
                assert Z <= t * (D - 1)
                assert a_min <= Z - D
                checks += 1
    return checks


def official_check() -> tuple[int, int]:
    assert (1 << 33) + 1 == 3**2 * 67 * 683 * 20857
    assert (1 << 32) + 1 == 641 * 6700417
    row_count = 0
    arity_count = 0
    for _name, h, k, expected_count, expected_min in ROWS:
        assert h % 2 == 1
        row_candidates = candidates(h, k)
        assert len(row_candidates) == expected_count
        actual_min = min(row_candidates)
        assert actual_min[:4] == expected_min
        assert all(t % 2 == 0 and D % 2 == 0 for _, _, t, D, _ in row_candidates)
        assert all((t - 2) // 2 in divisors(h) for _, _, t, _, _ in row_candidates)
        row_count += 1
        arity_count += len(row_candidates)

    # Four rows collapse to D=2h and have no outside points.
    for h in (3, 5, (1 << 32) + 1, (1 << 33) + 1):
        t, D = 4, 2 * h
        quotient = t * h // (t - 2)
        P = ((t - 3) * D - quotient) // 2
        Q = (t - 1) * (quotient - D) // 2
        assert P == Q == 0
    return row_count, arity_count


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
        "t=2s+2",
        "I=sigma=H=0",
        "P+Q=th/2-D",
        "afive-rowrelationisimpossible",
        "Thistheoremdoesnotcount",
    ):
        assert marker in statement


def main() -> None:
    formula_checks = formula_check()
    rows, arities = official_check()
    packet_check()
    print(
        "XR_RANK_TWO_ZERO_BASELINE_ARITHMETIC_ROUTER_PASS "
        f"rows={rows} arities={arities} formula_checks={formula_checks}"
    )


if __name__ == "__main__":
    main()
