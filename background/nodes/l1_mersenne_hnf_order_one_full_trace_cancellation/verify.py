#!/usr/bin/env python3
"""Check the exact automatic-root cancellation and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_order_one_full_trace_cancellation"
DEPENDENCY = "l1_mersenne_hnf_order_one_newton_reciprocal_reduction"
CONSUMER = "l1_mixed_petal_amplification"


def traces(values: list[int], limit: int, modulus: int) -> list[int]:
    return [
        sum(pow(value, degree, modulus) for value in values) % modulus
        for degree in range(1, limit + 1)
    ]


def check_case(modulus: int, m: int, h: int, d: int, zeta: int) -> int:
    assert pow(zeta, m, modulus) == 1
    d_star = zeta * pow(d, -1, modulus) % modulus
    x0 = -pow(d, -1, modulus) % modulus
    x0_star = -pow(d_star, -1, modulus) % modulus
    for degree in range(1, h):
        assert pow(x0_star, m * degree, modulus) == pow(x0, -m * degree, modulus)

    reduced = list(range(2, h + 1))
    reduced_star = [pow(value, -1, modulus) for value in reversed(reduced)]
    full = [x0] + reduced
    full_star = [x0_star] + reduced_star
    inverse_reduced = [pow(value, -1, modulus) for value in reduced]
    inverse_full = [pow(value, -1, modulus) for value in full]

    powered_reduced_star = [pow(value, m, modulus) for value in reduced_star]
    powered_full_star = [pow(value, m, modulus) for value in full_star]
    powered_inverse_reduced = [pow(value, m, modulus) for value in inverse_reduced]
    powered_inverse_full = [pow(value, m, modulus) for value in inverse_full]

    assert traces(powered_reduced_star, h - 1, modulus) == traces(
        powered_inverse_reduced, h - 1, modulus
    )
    assert traces(powered_full_star, h - 1, modulus) == traces(
        powered_inverse_full, h - 1, modulus
    )

    mutated = powered_full_star[:]
    mutated[1] = (mutated[1] + 1) % modulus
    assert traces(mutated, 3, modulus) != traces(powered_inverse_full, 3, modulus)
    return 2 * (h - 1) + 3


def main() -> None:
    checks = check_case(97, 8, 7, 5, -1)
    checks += check_case(193, 16, 15, 7, -1)

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == statuses[DEPENDENCY] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(FTC1)", "(FTC3)", "(FTC5)", "8,16,24", "16,32,48"):
        assert anchor in statement
    for anchor in ("zeta^(-mj)", "Newton's identities are triangular", "monic reciprocal"):
        assert anchor in proof

    print(f"L1_MERSENNE_HNF_ORDER_ONE_FULL_TRACE_CANCELLATION_PASS checks={checks}")


if __name__ == "__main__":
    main()
