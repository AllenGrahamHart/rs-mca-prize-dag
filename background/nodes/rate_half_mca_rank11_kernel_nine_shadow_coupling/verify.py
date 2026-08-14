#!/usr/bin/env python3
"""Verify the exact contract for the kernel nine-shadow coupling."""

from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "191af0d208a5cce6a6339bfc265de3be1bf8ca86b1c6da298ade68142e80c63e"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def sharp_spanning_nines(dimension: int) -> int:
    rank = 10 - dimension
    coloops = set(range(rank - 1))
    parallel = set(range(rank - 1, 11))
    count = 0
    for subset in combinations(range(11), 9):
        chosen = set(subset)
        rank_on_subset = len(chosen & coloops) + bool(chosen & parallel)
        if rank_on_subset == rank:
            count += 1
    return count


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-nine-shadow-coupling-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_record_support_capacity"
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["correction_dimension"], p["component_subset_size"], p["shadow_subset_size"]) == (10, 11, 9), "dimensions")
    require((p["minimum_corank"], p["maximum_corank"]) == (1, 9), "coranks")
    expected = [comb(dimension + 2, 2) for dimension in range(1, 10)]
    require(p["spanning_shadow_coefficients"] == expected, "coefficients")
    require(p["extension_formula"] == "C(K_prime-d-9,2)", "extension formula")
    require("C(m_prime,9)" in p["resource_formula"], "resource formula")
    require("parallel class" in p["sharp_model"], "sharp model")

    for dimension, coefficient in enumerate(expected, 1):
        dual_rank = dimension + 1
        require(dual_rank >= 2, "dual rank")
        require(4 * comb(dual_rank, 2) >= comb(dual_rank + 1, 2), "parallel-class case")
        require(sharp_spanning_nines(dimension) == coefficient, f"sharp d={dimension}")

    require("does not by itself pay" in str(data.get("nonclaim")), "nonclaim")
    return {"coefficient_sum": sum(expected), "sharp_models": len(expected)}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"]["spanning_shadow_coefficients"].__setitem__(0, 2),
        lambda item: item["parameters"].__setitem__("shadow_subset_size", 8),
        lambda item: item["parameters"].__setitem__("extension_formula", "C(K_prime-d-8,2)"),
        lambda item: item["dependencies"].clear(),
        lambda item: item.__setitem__("nonclaim", "complete payment"),
    )
    caught = 0
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_NINE_SHADOW_COUPLING_PASS "
        f"sharp_models={result['sharp_models']} coefficient_sum={result['coefficient_sum']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
