#!/usr/bin/env python3
"""Independent valuation audit for the joint C36' exceptional ideal."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_double_accident_derivative_ideal"
OLD = "f3_h3_global_derivative_ideal_valuation"
REDUCTION = "f3_h3_cutoff18_double_accident_reduction"
FIBER_CAP = "f3_h3_uniform_product_fiber_stepanov"
CONSUMER = "f3_h3_mobius_excess_half"


def ceil_cube_root(value: int) -> int:
    lower, upper = 0, 1 << ((value.bit_length() + 2) // 3)
    while lower + 1 < upper:
        middle = (lower + upper) // 2
        if middle * middle * middle < value:
            lower = middle
        else:
            upper = middle
    return upper


def main() -> None:
    cutoff = 18
    representation_cap = 64
    separator_exponent = representation_cap - cutoff
    local_checks = 0
    for multiplicity in range(representation_cap + 1):
        excess = max(multiplicity - cutoff, 0)
        for quotient_multiplicity in range(1, 17):
            for extra_j_valuation in range(4):
                j_valuation = 0 if excess == 0 else excess + extra_j_valuation
                delta_valuation = quotient_multiplicity - 1
                k_valuation = min(
                    j_valuation,
                    separator_exponent * delta_valuation,
                )
                expected_positive = excess > 0 and quotient_multiplicity >= 2
                assert (k_valuation > 0) == expected_positive
                if expected_positive:
                    assert k_valuation >= excess
                    cluster_valuation = quotient_multiplicity * k_valuation
                    desired = excess * (quotient_multiplicity - 1)
                    assert cluster_valuation >= desired
                local_checks += 1

    # The exact residual implication is checked independently of the ideal.
    residual_checks = 0
    for exponent in range(13, 42):
        n = 1 << exponent
        stepanov_ceiling = ceil_cube_root(33**3 * n * n)
        optimized_exponent = min(n - 19, stepanov_ceiling - 19)
        assert optimized_exponent >= 1
        assert optimized_exponent == (
            n - 19 if exponent <= 15 else stepanov_ceiling - 19
        )
        residual = 283 * n * n + 34 * n - 17
        assert residual + 17 * (n - 1) ** 2 == 300 * n * n
        quotient_degree = (n - 1) * (n - 2)
        # Since log(8)>log(6), this rational inequality proves that the naive
        # discriminant envelope misses even the p=6^(n/4) budget by more than
        # sixteen million.
        assert 68 * optimized_exponent * quotient_degree * (
            quotient_degree - 1
        ) > 16_000_000 * residual * n
        residual_checks += 1

    statement = (
        ROOT
        / "background/nodes/f3_h3_double_accident_derivative_ideal/statement.md"
    ).read_text()
    proof = (
        ROOT / "background/nodes/f3_h3_double_accident_derivative_ideal/proof.md"
    ).read_text()
    assert "f_n divides e_n" in statement
    assert "p divides f_n  iff  Y_18>0" in statement
    assert "B_n=min(n-19,ceil(33n^(2/3))-19)" in statement
    assert "f_n divides gcd(e_n,h_n^B_n)" in statement
    assert "ideal addition takes the minimum valuation" in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] in ("TARGET", "CONDITIONAL")  # 2026-07-19 amber re-pose
    assert (OLD, NODE, "req") in edges
    assert (REDUCTION, NODE, "req") in edges
    assert (FIBER_CAP, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "AUDIT_F3_H3_DOUBLE_ACCIDENT_DERIVATIVE_IDEAL_PASS "
        f"local_valuation_checks={local_checks} "
        f"residual_checks={residual_checks} dag=4/4"
    )


if __name__ == "__main__":
    main()
