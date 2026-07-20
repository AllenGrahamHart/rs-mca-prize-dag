#!/usr/bin/env python3
"""Verify the all-branch c=1 parity Jacobi compiler."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_fiber_two_cycle_c1_parity_all_branch_jacobi_norm_compiler"
DEPENDENCIES = {
    "rate_half_list_budget_three_fiber_two_cycle_c1_parity_nonharmonic_scalar_compiler",
    "rate_half_list_budget_three_fiber_two_cycle_c1_parity_frobenius_router",
    "rate_half_list_budget_three_fiber_two_cycle_c1_parity_r0_jacobi_norm_transfer",
}
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 1009
IOTA = next(value for value in range(PRIME) if value * value % PRIME == PRIME - 1)


def inverse(value: int) -> int:
    return pow(value % PRIME, -1, PRIME)


def h_values(r_value: int, iota: int = IOTA) -> list[int]:
    r_value %= PRIME
    return [
        (-1 + iota) * (r_value * r_value + iota) * inverse(2 * r_value) % PRIME,
        -(r_value * r_value + 3 * (1 + iota) * r_value + iota)
        * inverse((r_value - 1) * (r_value - iota)) % PRIME,
        -(r_value * r_value - 3 * (1 + iota) * r_value + iota)
        * inverse((r_value + 1) * (r_value + iota)) % PRIME,
        -iota * (r_value + 1) * inverse(r_value - 1) % PRIME,
        (1 + 2 * iota) * (5 * r_value - 4 + 3 * iota)
        * inverse(5 * (r_value - iota)) % PRIME,
        (1 - 2 * iota) * (5 * r_value - 4 - 3 * iota)
        * inverse(5 * (r_value + iota)) % PRIME,
    ]


def source_norm(kind: str, x_value: int, v_value: int) -> int:
    x2 = x_value * x_value
    v2 = v_value * v_value
    v3 = v2 * v_value
    v4 = v2 * v2
    if kind == "R0":
        return (v4 - 2 * v2 + x2) % PRIME
    if kind == "R12":
        return (
            v4 * (x2 - 1) + 4 * v3 * (x2 - 1)
            + 6 * v2 * x2 + 58 * v2
            + 4 * v_value * x2 - 132 * v_value + x2 + 63
        ) % PRIME
    if kind == "P0":
        return (v4 * (x_value - 1) + 2 * v2 * (x_value + 3) + x_value - 1) % PRIME
    if kind == "P12":
        return (
            v4 * (x_value + 1) - 4 * v3 * (x_value + 1)
            + 14 * v2 * x_value - 18 * v2
            - 20 * v_value * x_value + 44 * v_value
            + 25 * x_value - 7
        ) % PRIME
    raise ValueError(kind)


def even_parts(kind: str, z_value: int, q_value: int) -> tuple[int, int]:
    q2 = q_value * q_value
    q3 = q2 * q_value
    q4 = q2 * q2
    if kind == "R0":
        return (z_value * (q4 * z_value - 2 * q2 + 1) % PRIME, 0)
    if kind == "R12":
        a_value = (
            q4 * z_value**3 - q4 * z_value**2
            + 6 * q2 * z_value**2 + 58 * q2 * z_value
            + z_value + 63
        )
        b_value = 4 * q_value * (
            q2 * z_value**2 - q2 * z_value + z_value - 33
        )
        return a_value % PRIME, b_value % PRIME
    if kind == "P0":
        return (
            (-q4 * z_value**2 + 6 * q2 * z_value - 1) % PRIME,
            pow(q2 * z_value + 1, 2, PRIME),
        )
    if kind == "P12":
        a_value = (
            q4 * z_value**2 - 4 * q3 * z_value**2
            - 18 * q2 * z_value - 20 * q_value * z_value - 7
        )
        b_value = (
            q4 * z_value**2 - 4 * q3 * z_value
            + 14 * q2 * z_value + 44 * q_value + 25
        )
        return a_value % PRIME, b_value % PRIME
    raise ValueError(kind)


def algebra_check() -> None:
    checked = 0
    role_kinds = ("R0", "R12", "R12", "P0", "P12", "P12")
    for r_value in range(2, 142):
        if pow(r_value, 4, PRIME) == 1:
            continue
        x_value = (
            r_value * r_value + pow(r_value, -2, PRIME)
        ) * inverse(2) % PRIME
        rotated = IOTA * r_value % PRIME
        rotated_x = (
            rotated * rotated + pow(rotated, -2, PRIME)
        ) * inverse(2) % PRIME
        assert pow(rotated, 4, PRIME) == pow(r_value, 4, PRIME)
        assert rotated_x == -x_value % PRIME
        assert h_values(inverse(r_value), IOTA) == h_values(
            r_value, -IOTA % PRIME
        )
        for kind, h_value in zip(role_kinds, h_values(r_value)):
            assert source_norm(kind, x_value, h_value) == 0

        z_value = x_value * x_value % PRIME
        for q_value in (3, 7, 19):
            v_value = x_value * q_value % PRIME
            for kind in ("R0", "R12", "P0", "P12"):
                a_value, b_value = even_parts(kind, z_value, q_value)
                assert source_norm(kind, x_value, v_value) == (
                    a_value + x_value * b_value
                ) % PRIME
                negative = source_norm(kind, -x_value % PRIME, -v_value % PRIME)
                assert negative == (a_value - x_value * b_value) % PRIME
                assert (
                    source_norm(kind, x_value, v_value) * negative
                ) % PRIME == (a_value * a_value - z_value * b_value * b_value) % PRIME
        checked += 1
    assert checked >= 120


def wiring_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "N_R12=v^4(x^2-1)+4v^3(x^2-1)",
        "N_P0=v^4(x-1)+2v^2(x+3)+x-1",
        "F_R=A_R^2-zB_R^2",
        "exactly seven tests",
        "All fourteen tests share the same torsion-only norm pair",
        "does not evaluate the shared norms",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    wiring_check()
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_PARITY_ALL_BRANCH_JACOBI_PASS "
        "source_families=4 tests_per_sign=7 jacobi_degree=2^36 shared_norms=2"
    )


if __name__ == "__main__":
    main()
