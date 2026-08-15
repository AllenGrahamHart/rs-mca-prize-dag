#!/usr/bin/env python3
"""Verify the exact corank-one projective-pair record cap."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "274e46e67449c810193279941492511ddd67acff87649f5756b2b330718d9015"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-corank1-projective-pair-cap-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_canonical_basis_globalizer",
        "rate_half_mca_support_local_transversality_compiler",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")

    n, k, m, s = (p[key] for key in (
        "domain_size", "code_dimension", "support_size", "explanation_dimension"
    ))
    require((n, k, m, s) == (1048577, 1, 67473, 1), "shortened row")
    require(p["normal_space_dimension"] == s + 1 == 2, "normal dimension")
    require(p["zero_normal_upper_bound"] == k - s == 0, "zero normals")
    require(p["minimum_projective_classes"] == 2, "projective classes")

    maximum_dependent = (m - 1) ** 2 + 1
    minimum_independent = m * m - maximum_dependent
    require(maximum_dependent == p["maximum_dependent_ordered_pairs"], "dependent pairs")
    require(minimum_independent == 2 * (m - 1), "partition identity")
    require(minimum_independent == p["minimum_independent_ordered_pairs_per_record"], "independent pairs")

    resource = n * (n - 1)
    cap, remainder = divmod(resource, minimum_independent)
    require(resource == p["coordinate_ordered_pair_resource"], "pair resource")
    require((cap, remainder) == (p["projective_pair_record_cap"], p["division_remainder"]), "cap division")
    previous = resource // m
    require(previous == p["previous_transversality_record_cap"], "previous cap")
    require(previous - cap == p["record_cap_improvement"], "improvement")
    require("does not by itself" in str(data.get("nonclaim")), "nonclaim")
    return {"cap": cap, "pairs": minimum_independent, "improvement": previous - cap}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("zero_normal_upper_bound", 1),
        lambda item: item["parameters"].__setitem__("minimum_projective_classes", 1),
        lambda item: item["parameters"].__setitem__("maximum_dependent_ordered_pairs", item["parameters"]["maximum_dependent_ordered_pairs"] + 1),
        lambda item: item["parameters"].__setitem__("minimum_independent_ordered_pairs_per_record", item["parameters"]["minimum_independent_ordered_pairs_per_record"] - 1),
        lambda item: item["parameters"].__setitem__("projective_pair_record_cap", item["parameters"]["projective_pair_record_cap"] + 1),
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
        "RATE_HALF_MCA_RANK11_KERNEL_CORANK1_PROJECTIVE_PAIR_CAP_PASS "
        f"cap={result['cap']} pairs={result['pairs']} improvement={result['improvement']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
