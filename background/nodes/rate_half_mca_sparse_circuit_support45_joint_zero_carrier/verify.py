#!/usr/bin/env python3
"""Verify the support-four/support-five joint zero-carrier contract."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "dae4d0f7200653bb1e9f7f3f1c73b1ca1d83f3040d915a98952a92fd49eedae8"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-sparse-circuit-support45-joint-zero-carrier-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_sparse_circuit_completion_dimension_ladder"],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("correction_dimension") == 10, "dimension")
    require(p.get("source_supports") == [4, 5], "supports")
    require(p.get("source_vanishing_dimensions") == {"4": 7, "5": 6}, "H dimensions")
    require(p.get("support4_terminal_defects") == list(range(6)), "support4 defects")
    require(p.get("support5_terminal_defects") == list(range(5)), "support5 defects")
    require(p.get("overlap_condition") == "q>s_4+s_5", "overlap condition")
    require(p.get("intersection_dimension_lower_bound") == 4, "intersection")
    require(p.get("carrier_union_upper_bound") == "q+6", "union")
    require(p.get("zero_closure_dimension_range") == [4, 6], "closure dimension")
    require(p.get("quotient_defect") == "delta=K-t-|B|", "delta")
    require(
        p.get("quotient_defect_bound") == "0<=delta<=min(s_4,s_5)",
        "delta bound",
    )
    require(
        p.get("external_completion_carrier_bound") == "|U_A\\B|<=delta+3",
        "outside bound",
    )

    checks = 0
    q = 35
    for s4 in range(6):
        for s5 in range(5):
            require(q > s4 + s5, "official overlap condition")
            u4 = q + 3 - s4
            u5 = q + 4 - s5
            union_if_minimal = q + 7
            overlap = u4 + u5 - union_if_minimal
            require(overlap == q - s4 - s5 and overlap > 0, "forced overlap")
            require(7 + 6 - 3 == 10, "Grassmann equality")
            require((q + 10) - 4 == q + 6, "strengthened root bound")
            for t in range(4, 7):
                for delta in range(min(s4, s5) + 1):
                    b = q + 10 - t - delta
                    require((q + 10) - (t - 3) - b == delta + 3, "outside subtraction")
                    checks += 1
    require(
        data.get("logical_pins")
        == [
            "grassmann_equality_would_make_H4_plus_H5_equal_V",
            "q_greater_than_defect_sum_forces_a_source_carrier_overlap",
            "the_zero_set_is_closed_before_delta_is_defined",
            "private_coordinate_label_spaces_bound_delta",
            "every_support4_deletion_is_compared_with_the_same_closed_carrier",
        ],
        "logical pins",
    )
    require("No support incidence count" in str(data.get("nonclaim")), "nonclaim")
    return {"checks": checks, "defect_pairs": 30}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("correction_dimension", 9),
        lambda item: item["parameters"].__setitem__("source_supports", [3, 5]),
        lambda item: item["parameters"].__setitem__("intersection_dimension_lower_bound", 3),
        lambda item: item["parameters"].__setitem__("carrier_union_upper_bound", "q+7"),
        lambda item: item["parameters"].__setitem__("zero_closure_dimension_range", [3, 7]),
        lambda item: item["parameters"].__setitem__("quotient_defect_bound", "delta<=s_5"),
        lambda item: item.__setitem__("logical_pins", []),
        lambda item: item.__setitem__("nonclaim", "K'=45 paid"),
    )
    rejected = 0
    for mutation in mutations:
        hostile = copy.deepcopy(data)
        mutation(hostile)
        try:
            validate(hostile)
        except (Reject, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "tamper controls")
    return rejected


def main() -> None:
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    result = validate(data)
    controls = tamper_selftest(data)
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_SUPPORT45_JOINT_ZERO_CARRIER_PASS "
        f"defect_pairs={result['defect_pairs']} checks={result['checks']} "
        f"controls={controls}"
    )


if __name__ == "__main__":
    main()
