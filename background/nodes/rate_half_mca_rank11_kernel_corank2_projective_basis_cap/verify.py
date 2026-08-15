#!/usr/bin/env python3
"""Verify the exact corank-two projective-basis record cap."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "e1a679080c4efd83af40aa7d969960946b3ca3d7654e46e65be8dcb68a910d6c"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-kernel-corank2-projective-basis-cap-v1",
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
    require((n, k, m, s, w) == (1048578, 2, 67474, 2, 67472), "shortened row")
    require(p["normal_space_dimension"] == s + 1 == 3, "normal dimension")
    require(p["zero_normal_upper_bound"] == k - s == 0, "zero normals")
    outside = w + s - 1
    require(outside == p["minimum_normals_outside_projective_class"], "one-span escape")
    require(m - outside == p["maximum_projective_class_size"] == 1, "class size")
    require(p["minimum_projective_points"] == m, "projective points")
    require(p["noncollinear"] is True, "noncollinearity")

    maximum_collinear = comb(m - 1, 3)
    require(maximum_collinear == p["maximum_collinear_unordered_triples"], "collinear triples")
    minimum_bases = m * (m - 1) * (m - 2) - 6 * maximum_collinear
    require(minimum_bases == 3 * (m - 1) * (m - 2), "basis identity")
    require(
        minimum_bases == p["minimum_independent_ordered_triples_per_record"],
        "independent triples",
    )

    resource = n * (n - 1) * (n - 2)
    cap, remainder = divmod(resource, minimum_bases)
    require(resource == p["coordinate_ordered_triple_resource"], "triple resource")
    require((cap, remainder) == (
        p["projective_basis_record_cap"], p["division_remainder"]
    ), "cap division")
    previous, previous_remainder = divmod(resource, m * (m - 1))
    require((previous, previous_remainder) == (
        p["previous_transversality_record_cap"],
        p["previous_division_remainder"],
    ), "previous cap")
    require(previous - cap == p["record_cap_improvement"], "improvement")

    q, r = 17, m - 17
    difference = comb(m - 1, 3) - comb(q, 3) - comb(r + 1, 3)
    decomposition = (r - 1) * (comb(q, 2) - 1) + (q - 2) * comb(r - 1, 2)
    require(difference == decomposition >= 0, "collinear split identity")
    require("does not by itself" in str(data.get("nonclaim")), "nonclaim")
    return {"cap": cap, "bases": minimum_bases, "improvement": previous - cap}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("zero_normal_upper_bound", 1),
        lambda item: item["parameters"].__setitem__("maximum_projective_class_size", 2),
        lambda item: item["parameters"].__setitem__("noncollinear", False),
        lambda item: item["parameters"].__setitem__("maximum_collinear_unordered_triples", item["parameters"]["maximum_collinear_unordered_triples"] + 1),
        lambda item: item["parameters"].__setitem__("minimum_independent_ordered_triples_per_record", item["parameters"]["minimum_independent_ordered_triples_per_record"] - 1),
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
        "RATE_HALF_MCA_RANK11_KERNEL_CORANK2_PROJECTIVE_BASIS_CAP_PASS "
        f"cap={result['cap']} bases={result['bases']} "
        f"improvement={result['improvement']} controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
