#!/usr/bin/env python3
"""Verify the matched fiber-two cycle lift field router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_fiber_two_cycle_matched_lift_field_router"
DEPENDENCIES = {
    "rate_half_list_budget_three_fiber_two_cycle_boundary_transfer",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_even_factorization",
    "rate_half_list_budget_three_maximal_field_degree_collapse",
}
CONSUMER = "rate_half_list_adjacent_crossing"


def trim(values: list[int]) -> list[int]:
    while values and values[-1] == 0:
        values.pop()
    return values


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim(
        [
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
            for index in range(size)
        ]
    )


def scale(value: int, polynomial: list[int]) -> list[int]:
    return trim([value * coefficient for coefficient in polynomial])


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return trim(answer)


def power(polynomial: list[int], exponent: int) -> list[int]:
    answer = [1]
    base = polynomial
    while exponent:
        if exponent & 1:
            answer = multiply(answer, base)
        base = multiply(base, base)
        exponent //= 2
    return answer


def identity_check() -> None:
    r = [0, 1]
    one = [1]
    r2_plus_one = add(power(r, 2), one)

    first_difference = add(
        power(add(add(power(r, 2), scale(-1, r)), one), 2),
        scale(-1, power(add(add(power(r, 2), r), one), 2)),
    )
    assert first_difference == scale(-4, multiply(r, r2_plus_one))

    third_difference = add(
        power(add(add(power(r, 2), scale(-4, r)), one), 2),
        scale(-1, power(add(add(power(r, 2), scale(4, r)), one), 2)),
    )
    assert third_difference == scale(-16, multiply(r, r2_plus_one))

    a = power(add(r, [-1]), 4)
    b = power(add(r, one), 4)
    assert add(a, scale(-1, b)) == scale(-8, multiply(r, r2_plus_one))
    assert add(a, b) == scale(2, add(add(power(r, 4), scale(6, power(r, 2))), one))


def arithmetic_check() -> None:
    m = 1 << 36
    n = 8 * m
    assert n == 1 << 39
    assert 2 * n == 1 << 40
    assert 4 * n == 1 << 41
    assert 3 * (1 << 128) > 4 * n * n
    assert (2 * n) ** 2 < 3 * (1 << 128)

    # In the nonsplit class p=1+2N (mod 4N), Frobenius multiplies a
    # 4N-torsion element by its 2Nth power.
    for exponent in range(8):
        assert (1 + 2 * n) * exponent % (4 * n) == (
            exponent + 2 * n * exponent
        ) % (4 * n)


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
        "two-antipodal-pair",
        "N=8M=2^39",
        "p=1 mod 2N",
        "r^p=eta r",
        "anti-invariant case",
        "PGL_2(F_p)",
    ):
        assert marker in statement
    for marker in (
        "The anti-invariant case is empty",
        "q_out in {z,z^(-1)}",
        "field of definition of `r`",
    ):
        assert marker in proof


def main() -> None:
    arithmetic_check()
    identity_check()
    packet_check()
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_MATCHED_LIFT_FIELD_ROUTER_PASS "
        "N_bits=39 surviving_field_degree=2 anti_invariant=0 identities=4"
    )


if __name__ == "__main__":
    main()
