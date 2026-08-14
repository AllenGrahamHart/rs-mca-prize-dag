#!/usr/bin/env python3
"""Verify the record-support kernel capacity contract."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "ede7f01e37f1f856118ba73b3c94af8b99658361cac2e747f7f69fe24d3a7e7e"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-record-support-capacity-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_multibasis_decoration_compression",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["correction_dimension"], p["component_subset_size"]) == (10, 11), "dimensions")
    require((p["minimum_corank"], p["maximum_corank"]) == (1, 9), "coranks")
    require(p["extra_common_zero_offset"] == 10, "common-zero offset")
    require(p["basis_multiplicities"] == list(range(3, 12)), "multiplicities")
    require(p["capacity_formula"] == "floor(C(m_prime,10-d)*C(K_prime-10,d+1)/(d+2))", "formula")
    require("does not by itself pay" in str(data.get("nonclaim")), "nonclaim")
    return {"strata": 9, "minimum": 3, "maximum": 11}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("component_subset_size", 10),
        lambda item: item["parameters"].__setitem__("extra_common_zero_offset", 9),
        lambda item: item["parameters"]["basis_multiplicities"].__setitem__(2, 4),
        lambda item: item["parameters"].__setitem__("capacity_formula", "ceil(C(m_prime,10-d)*C(K_prime-10,d+1)/(d+2))"),
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
        "RATE_HALF_MCA_RANK11_KERNEL_RECORD_SUPPORT_CAPACITY_PASS "
        f"strata={result['strata']} multiplicities={result['minimum']}..{result['maximum']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
