#!/usr/bin/env python3
"""Independent behavior audit for the low-budget list certificate generator."""

from __future__ import annotations

import copy
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from prize_certificate_compiler import compile_certificate  # noqa: E402
from prize_row_descriptor import INPUT_SCHEMA  # noqa: E402
from rate_half_list_low_budget_certificate import (  # noqa: E402
    OUTPUT_SCHEMA,
    generate_certificate,
)


def row(p: int, extension_degree: int, subgroup_log2: int, rate: str = "1/2") -> dict:
    return {
        "schema": INPUT_SCHEMA,
        "p": str(p),
        "extension_degree": extension_degree,
        "subgroup_log2": subgroup_log2,
        "rate": rate,
    }


def rejected(source: dict, object_name: str, phrase: str) -> bool:
    try:
        generate_certificate(source, object_name)
    except ValueError as exc:
        return phrase in str(exc)
    return False


def main() -> None:
    fixtures = (
        (row(41, 24, 4), 1),
        (row(7, 46, 4), 2),
    )
    positives = 0
    for source, budget in fixtures:
        q = int(source["p"]) ** source["extension_degree"]
        assert q // (1 << 128) == budget
        assert (q - 1) % 16 == 0
        for object_name in ("LIST", "INTERLEAVED_LIST"):
            result = generate_certificate(source, object_name)
            assert result["schema"] == OUTPUT_SCHEMA
            assert result["status"] == "CERTIFIED_ADJACENT_CROSSING"
            assert result["prize_facing"]
            assert result["scope"]["B_star"] == str(budget)
            if object_name == "LIST":
                assert result["scope"]["arity"] == {"kind": "fixed", "value": 1}
                expected_claim = "rate_half_list_low_budget_exact_crossing"
            else:
                assert result["scope"]["arity"] == {"kind": "all_positive_integers"}
                expected_claim = "rate_half_list_low_budget_all_arity_crossing"
            assert result["theorem_packet"]["claim_id"] == expected_claim
            assert result["external_preconditions"] == [
                "p is prime",
                "the supplied code uses the order-n multiplicative subgroup or a proved equivalent coset",
            ]
            assert result["certificate"] == {
                "unsafe_agreement": 11,
                "safe_agreement": 12,
                "largest_safe_closed_radius": {"numerator": 4, "denominator": 16},
                "closed_ball_boundary_supremum": {
                    "numerator": 5,
                    "denominator": 16,
                    "attained": False,
                },
            }
            compiler_output = result["compiler_output"]
            assert compiler_output["B_star"] == str(budget)
            assert compiler_output["object"] == object_name
            assert compiler_output["certificate"] == result["certificate"]
            positives += 1

    mutations = [
        rejected(row(17, 32, 9), "LIST", "requires B*=1 or B*=2"),
        rejected(row(17, 1, 4), "LIST", "requires B*=1 or B*=2"),
        rejected(row(41, 24, 4, "1/4"), "LIST", "requires rate 1/2"),
        rejected(row(41, 24, 1), "LIST", "order divisible by 4"),
        rejected(row(41, 24, 4), "MCA_FINITE_SLOPE", "object must be one of"),
        rejected({**row(41, 24, 4), "schema": "wrong"}, "LIST", "row schema must be"),
        rejected({**row(41, 24, 4), "n": 16}, "LIST", "unknown row-input fields"),
        rejected(row(17, 1, 5), "LIST", "must divide q-1"),
    ]
    assert all(mutations)

    tampered = generate_certificate(fixtures[0][0], "LIST")["compiler_input"]
    tampered = copy.deepcopy(tampered)
    tampered["row_descriptor"]["target"]["B_star_decimal"] = "2"
    try:
        compile_certificate(tampered)
    except ValueError as exc:
        assert "canonical recomputation" in str(exc)
    else:
        raise AssertionError("tampered descriptor was accepted")

    print(
        "RATE_HALF_LIST_LOW_BUDGET_CERTIFICATE_AUDIT_PASS "
        f"positive={positives} refusals={sum(mutations)}/{len(mutations)} tampering=1/1"
    )


if __name__ == "__main__":
    main()
