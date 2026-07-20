#!/usr/bin/env python3
"""Verify the fiber-two cycle quotient-embedding packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_fiber_two_cycle_quotient_embedding"
DEPENDENCIES = {
    "rate_half_list_budget_three_multifiber_vandermonde_exclusion",
    "rate_half_list_budget_three_antipodal_mobius_weld",
    "rate_half_list_budget_three_antipodal_primitive_quotient_gate",
    "rate_half_list_budget_three_antipodal_pencil_degree_floor",
    "rate_half_list_budget_three_maximal_field_degree_collapse",
}
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 101


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return [
        ((left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0))
        % PRIME
        for i in range(size)
    ]


def scale(value: int, polynomial: list[int]) -> list[int]:
    return [value * coefficient % PRIME for coefficient in polynomial]


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % PRIME
    return answer


def lift_even(polynomial: list[int]) -> list[int]:
    answer = [0] * (2 * len(polynomial) - 1)
    for index, coefficient in enumerate(polynomial):
        answer[2 * index] = coefficient
    return answer


def trim(polynomial: list[int]) -> list[int]:
    while len(polynomial) > 1 and polynomial[-1] == 0:
        polynomial.pop()
    return polynomial


def barycentric_weights(points: tuple[int, ...]) -> tuple[int, ...]:
    weights = []
    for i, point in enumerate(points):
        denominator = 1
        for j, other in enumerate(points):
            if i != j:
                denominator = denominator * (point - other) % PRIME
        weights.append(pow(denominator, -1, PRIME))
    return tuple(weights)


def algebra_checks() -> int:
    u = [7, 3, 1]
    v = [4, 1]
    root_rows = (
        (2, 5, 9, 17),
        (2, PRIME - 2, 5, 9),
        (2, PRIME - 2, 5, PRIME - 5),
    )
    for roots in root_rows:
        weights = barycentric_weights(roots)
        for exponent in range(3):
            assert sum(
                weight * pow(root, exponent, PRIME)
                for weight, root in zip(weights, roots, strict=True)
            ) % PRIME == 0

        generators = [add(u, scale(root, v)) for root in roots]
        first = [0]
        second = [0]
        lifted_relation = [0]
        for weight, root, generator in zip(weights, roots, generators, strict=True):
            first = add(first, scale(weight, generator))
            second = add(second, scale(weight * root % PRIME, generator))
            locator = multiply([root, 1], lift_even(generator))
            lifted_relation = add(lifted_relation, scale(weight, locator))
            completed = multiply([-root * root % PRIME, 1], generator)
            assert multiply([-root % PRIME, 1], locator) == lift_even(completed)
        assert trim(first) == [0]
        assert trim(second) == [0]
        assert trim(lifted_relation) == [0]

        mutated = generators[:]
        mutated[-1] = add(mutated[-1], [1])
        bad = [0]
        for weight, generator in zip(weights, mutated, strict=True):
            bad = add(bad, scale(weight, generator))
        assert trim(bad) != [0]

    denominator_roots = (
        {pow(value, 2, PRIME) for value in root_rows[0]},
        {4, 25, 81, 17 * 17 % PRIME},
        {4, 25, 9 * 9 % PRIME, 17 * 17 % PRIME},
    )
    assert [len(values) for values in denominator_roots] == [4, 4, 4]
    return len(root_rows)


def official_check() -> None:
    d = 1 << 39
    s = d // 2
    d_ant = 2 * d
    r_ant = s - 1
    assert d == 2 * s
    assert d_ant == 4 * s == 1 << 40
    assert r_ant == (1 << 38) - 1
    assert (r_ant - 4 + 1) // 2 == (1 << 37) - 2
    assert (1 << 64) > d_ant


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    proof = (here / "proof.md").read_text()
    for marker in (
        "d_ant=2d=4s",
        "G_i=mu_i(R+rho_iS)",
        "deg(-R/S)=2^38-1",
        "deg V>=2^37-2",
        "denominator-mismatch",
        "automatically distinct",
    ):
        assert marker in statement
    for marker in (
        "cross-block\ncompletion roots occur exactly",
        "completion roots are distinct",
        "remaining\n`2c` roots of `E` occur in antipodal pairs",
        "monic squarefree quartic `D_*`",
        "general quartic `D_*`",
        "characteristic exceeds\n`2^64`",
    ):
        assert marker in proof


def main() -> None:
    checked = algebra_checks()
    official_check()
    packet_check()
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_CYCLE_QUOTIENT_EMBEDDING_PASS "
        f"pairing_strata={checked} quotient_order={1 << 40} mutation=1"
    )


if __name__ == "__main__":
    main()
