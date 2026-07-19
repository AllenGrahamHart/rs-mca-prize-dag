#!/usr/bin/env python3
"""Verify the Fourier-resultant branch collapse and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_fourier_resultant_branch_collapse"
FACTORIZATION = "rate_half_list_budget_three_antipodal_generic_deleted_pair_even_factorization"
FIELD = "rate_half_list_budget_three_maximal_field_degree_collapse"
CONSUMER = "rate_half_list_adjacent_crossing"


def arithmetic_check() -> None:
    n_value = 2**38
    assert 3 * 2**128 > 4 * n_value**2
    assert 3 * 2**128 > (2 * n_value) ** 2
    assert n_value // 8 == 2**35
    assert n_value // 4 == 2**36

    # Phi_16=X^8+1 repeats the two coefficient halves. Two repeated zeros
    # leave an odd number of signs per half, so a balanced coloring is impossible.
    first_half = [0, 1, 1, 1, -1, -1, -1, 1]
    second_half = first_half[:]
    assert sum(first_half + second_half) == 2
    assert sum(value != 0 for value in first_half) == 7
    assert second_half[0] == 0

    # The AM-GM exponents reproduce the two printed characteristic bounds.
    split_zeros = n_value // 8
    nonsplit_zeros = n_value // 4
    primitive_product_exponent = n_value // 4
    assert 2 * primitive_product_exponent // split_zeros == 4
    assert 2 * primitive_product_exponent // nonsplit_zeros == 2

    # Small exact analogue of the surviving p=1 mod 4N square-class step.
    prime, small_n, generator = 193, 16, 5
    zeta = pow(generator, (prime - 1) // small_n, prime)
    assert (prime - 1) % (4 * small_n) == 0
    assert pow(zeta, small_n, prime) == 1
    assert all(
        value == 1 or pow(value, (prime - 1) // 2, prime) == 1
        for value in (pow(zeta, index, prime) for index in range(small_n))
    )


def wiring_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[FACTORIZATION]["status"] == nodes[FIELD]["status"] == "PROVED"
    assert (FACTORIZATION, NODE, "req") in edges
    assert (FIELD, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "p<4N^2",
        "p<2N",
        "prime-field branch",
        "p=-1 mod N",
        "PGL_2(F_p)",
        "Only the full",
        "does not exclude",
    ):
        assert marker in statement


def main() -> None:
    arithmetic_check()
    wiring_check()
    print(
        "RATE_HALF_DELETED_PAIR_FOURIER_RESULTANT_BRANCH_PASS "
        "primitive_fraction=1/4 branches_closed=2 remaining_data=base_field"
    )


if __name__ == "__main__":
    main()
