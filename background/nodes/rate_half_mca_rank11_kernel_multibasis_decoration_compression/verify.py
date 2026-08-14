#!/usr/bin/env python3
"""Verify the kernel multi-basis decoration contract."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "2db1ee7ecda1fb2498203ee3eec190f732d149e21e1aa8df87d8e52aafd16f52"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-multibasis-decoration-compression-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_canonical_basis_globalizer",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["correction_dimension"], p["component_subset_size"]) == (10, 11), "dimensions")
    require((p["minimum_corank"], p["maximum_corank"]) == (1, 9), "coranks")
    require(p["global_common_zero_count"] == 0, "looplessness")
    expected = []
    for d in range(p["minimum_corank"], p["maximum_corank"] + 1):
        rank = p["correction_dimension"] - d
        expected.append(1 + p["component_subset_size"] - rank)
    require(p["basis_multiplicities"] == expected == list(range(3, 12)), "basis multiplicities")
    require("does not pay" in str(data.get("nonclaim")), "nonclaim")
    return {"strata": len(expected), "minimum": min(expected), "maximum": max(expected)}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("global_common_zero_count", 1),
        lambda item: item["parameters"].__setitem__("component_subset_size", 10),
        lambda item: item["parameters"]["basis_multiplicities"].__setitem__(0, 2),
        lambda item: item["parameters"].__setitem__("maximum_corank", 8),
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
        "RATE_HALF_MCA_RANK11_KERNEL_MULTIBASIS_DECORATION_COMPRESSION_PASS "
        f"strata={result['strata']} multiplicities={result['minimum']}..{result['maximum']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
