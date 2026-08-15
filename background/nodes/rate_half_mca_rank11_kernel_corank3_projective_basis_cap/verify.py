#!/usr/bin/env python3
"""Verify the exact corank-three projective-basis record cap."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "1df3954f0b52dc475f5212be64af83530645e3b1b035b2178185f422671e6b8a"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-kernel-corank3-projective-basis-cap-v1",
        "schema",
    )
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_canonical_basis_globalizer",
        "rate_half_mca_support_local_transversality_compiler",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")

    n, k, m, s, w = (p[key] for key in (
        "domain_size", "code_dimension", "support_size",
        "explanation_dimension", "support_excess",
    ))
    require((n, k, m, s, w) == (1048579, 3, 67475, 3, 67472), "shortened row")
    require(p["normal_space_dimension"] == s + 1 == 4, "normal dimension")
    require(p["zero_normal_upper_bound"] == k - s == 0, "zero normals")
    outside_class = w + s - 1
    require(outside_class == p["minimum_normals_outside_projective_class"], "one-span escape")
    require(m - outside_class == p["maximum_projective_class_size"] == 1, "class size")
    outside_line = w + s - 2
    require(outside_line == p["minimum_normals_outside_projective_line"], "two-span escape")
    require(m - outside_line == p["maximum_projective_line_size"] == 2, "line size")
    require(p["minimum_projective_points"] == m, "projective points")
    require(p["spans_projective_space"] is True, "projective span")

    maximum_coplanar = comb(m - 1, 4)
    require(maximum_coplanar == p["maximum_coplanar_unordered_quadruples"], "coplanar quadruples")
    minimum_bases = m * (m - 1) * (m - 2) * (m - 3) - 24 * maximum_coplanar
    require(minimum_bases == 4 * (m - 1) * (m - 2) * (m - 3), "basis identity")
    require(
        minimum_bases == p["minimum_independent_ordered_quadruples_per_record"],
        "independent quadruples",
    )

    resource = n * (n - 1) * (n - 2) * (n - 3)
    cap, remainder = divmod(resource, minimum_bases)
    require(resource == p["coordinate_ordered_quadruple_resource"], "quadruple resource")
    require((cap, remainder) == (
        p["projective_basis_record_cap"], p["division_remainder"]
    ), "cap division")
    previous_bases = m * (w + 1) * (w + 2)
    previous, previous_remainder = divmod(resource, previous_bases)
    require((previous, previous_remainder) == (
        p["previous_transversality_record_cap"],
        p["previous_division_remainder"],
    ), "previous cap")
    require(previous - cap == p["record_cap_improvement"], "improvement")

    q, r = 18, m - 18
    bound = comb(q, 4) + (q // 2) * comb(r, 2) + 2 * comb(r, 3) + comb(r, 4)
    difference = comb(m - 1, 4) - bound
    decomposition = (
        (q - 3) * comb(r, 3)
        + (comb(q - 1, 2) - q // 2) * comb(r, 2)
        + (r - 1) * comb(q - 1, 3)
    )
    require(difference == decomposition >= 0, "coplanar split identity")
    require("does not by itself" in str(data.get("nonclaim")), "nonclaim")
    return {"cap": cap, "bases": minimum_bases, "improvement": previous - cap}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("zero_normal_upper_bound", 1),
        lambda item: item["parameters"].__setitem__("maximum_projective_class_size", 2),
        lambda item: item["parameters"].__setitem__("maximum_projective_line_size", 3),
        lambda item: item["parameters"].__setitem__("spans_projective_space", False),
        lambda item: item["parameters"].__setitem__("maximum_coplanar_unordered_quadruples", item["parameters"]["maximum_coplanar_unordered_quadruples"] + 1),
        lambda item: item["parameters"].__setitem__("minimum_independent_ordered_quadruples_per_record", item["parameters"]["minimum_independent_ordered_quadruples_per_record"] - 1),
        lambda item: item["parameters"].__setitem__("projective_basis_record_cap", item["parameters"]["projective_basis_record_cap"] + 1),
        lambda item: item["parameters"].__setitem__("record_cap_improvement", item["parameters"]["record_cap_improvement"] - 1),
    )
    caught = 0
    for mutation in mutations:
        altered = copy.deepcopy(data)
        mutation(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_CORANK3_PROJECTIVE_BASIS_CAP_PASS "
        f"cap={result['cap']} bases={result['bases']} "
        f"improvement={result['improvement']} controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
