#!/usr/bin/env python3
"""Verify the deleted-pair Möbius ratio router and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_mobius_ratio_router"
DEPENDENCIES = {
    "rate_half_list_budget_three_antipodal_mobius_weld",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_even_factorization",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_fourier_resultant_branch_collapse",
}
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 97
IOTA = 22


def inverse(value: int) -> int:
    return pow(value % PRIME, -1, PRIME)


def cross_ratio(a: int, b: int, c: int, d: int) -> int:
    return (a - c) * (b - d) * inverse((a - d) * (b - c)) % PRIME


def explicit_gate(pairing: int, r_value: int, q_value: int) -> int:
    r_value %= PRIME
    q_value %= PRIME
    left_factors = (
        r_value * r_value,
        pow(r_value - 1, 4, PRIME),
        pow(r_value * r_value + 1, 2, PRIME),
    )
    right_factors = (
        pow(r_value * r_value - r_value + 1, 2, PRIME),
        pow(r_value + 1, 4, PRIME),
        pow(r_value * r_value - 4 * r_value + 1, 2, PRIME),
    )
    return (
        left_factors[pairing] * pow(1 + q_value, 2, PRIME)
        - 4 * q_value * right_factors[pairing]
    ) % PRIME


def algebra_check() -> None:
    assert IOTA * IOTA % PRIME == PRIME - 1

    order = 8
    zeta = pow(5, (PRIME - 1) // order, PRIME)
    assert pow(zeta, order, PRIME) == 1
    assert pow(zeta, order // 2, PRIME) == PRIME - 1
    roots = [pow(zeta, exponent, PRIME) for exponent in range(order)]
    first_cell = roots[1:4]
    second_cell = roots[5:8]
    first_constant = -first_cell[0] * first_cell[1] * first_cell[2] % PRIME
    second_constant = -second_cell[0] * second_cell[1] * second_cell[2] % PRIME
    root_cell_ratio = second_constant * inverse(first_constant) % PRIME
    assert pow(first_constant, order, PRIME) == 1
    assert pow(second_constant, order, PRIME) == 1
    assert pow(root_cell_ratio, order, PRIME) == 1

    pairings = (
        ((0, 1), (2, 3)),
        ((0, 2), (1, 3)),
        ((0, 3), (1, 2)),
    )

    positive = None
    for r_value in range(1, PRIME):
        if pow(r_value, 4, PRIME) == 1:
            continue
        points = (1, IOTA, r_value, IOTA * r_value % PRIME)
        assert len(set(points)) == 4
        source_cross_ratios = []
        for (a_index, b_index), (c_index, d_index) in pairings:
            source_cross_ratios.append(cross_ratio(
                points[a_index], points[b_index], points[c_index], points[d_index]
            ))

        expected = (
            pow(r_value - 1, 2, PRIME) * inverse(r_value * r_value + 1),
            2 * r_value * inverse(r_value * r_value + 1),
            -2 * r_value * inverse(pow(r_value - 1, 2, PRIME)),
        )
        assert source_cross_ratios == [value % PRIME for value in expected]

        for y_value in range(1, PRIME):
            if y_value in (1, PRIME - 1):
                continue
            q_value = y_value * y_value % PRIME
            target = pow(1 - y_value, 2, PRIME) * inverse(
                pow(1 + y_value, 2, PRIME)
            ) % PRIME
            target_inverse = inverse(target)
            for pairing, source in enumerate(source_cross_ratios):
                gate = explicit_gate(pairing, r_value, q_value) == 0
                match = source in (target, target_inverse)
                assert gate == match
                if gate and positive is None:
                    positive = (r_value, y_value, pairing)

    assert positive == (2, 17, 2)

    # Harmonic q=-1 is retained only on the printed factors.
    for r_value in range(1, PRIME):
        if pow(r_value, 4, PRIME) == 1:
            continue
        assert (explicit_gate(0, r_value, PRIME - 1) == 0) == (
            (r_value * r_value - r_value + 1) % PRIME == 0
        )
        assert explicit_gate(1, r_value, PRIME - 1) != 0
        assert (explicit_gate(2, r_value, PRIME - 1) == 0) == (
            (r_value * r_value - 4 * r_value + 1) % PRIME == 0
        )


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
        "r^4=t",
        "q=(beta/alpha)^2=mu/lambda",
        "q^N=1",
        "ratios lying in `mu_N`",
        "r^2(1+q)^2",
        "(r-1)^4(1+q)^2",
        "(r^2+1)^2(1+q)^2",
        "at most three unordered",
        "harmonic case `q=-1`",
        "does not prove",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    wiring_check()
    print(
        "RATE_HALF_ANTIPODAL_DELETED_PAIR_MOBIUS_RATIO_PASS "
        "source_pairings=3 outer_ratio_orbits<=3 harmonic_retained=1"
    )


if __name__ == "__main__":
    main()
