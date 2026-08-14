#!/usr/bin/env python3
"""Verify the kernel canonical-basis globalizer contract."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "98de8b079e0de815c691dcebfd49ad2520dc7ca3c232ea62b34eb4e94ecbfdfa"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-canonical-basis-globalizer-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_dense_locator_component_incidence_dichotomy",
        "rate_half_mca_support_local_transversality_compiler",
        "rate_half_mca_rank10_margin_interleaving_split_payment",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["correction_dimension"] == 10, "correction dimension")
    require(p["component_subset_size"] == 11, "component size")
    require((p["rank_minimum"], p["rank_maximum"]) == (1, 9), "rank interval")
    require(p["extra_common_zero_offset"] == 10, "zero offset")
    require(p["rank9_record_cap"] == 61871313426630599, "rank-nine cap")
    for rank in range(1, 10):
        dimension = p["correction_dimension"] - rank
        require(rank + dimension == p["extra_common_zero_offset"], "rank complement")
        require(p["component_subset_size"] - rank == dimension + 1, "extension size")
    require("does not pay" in str(data.get("nonclaim")), "nonclaim")
    return {"ranks": 9, "rank9": p["rank9_record_cap"]}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("correction_dimension", 11),
        lambda item: item["parameters"].__setitem__("component_subset_size", 12),
        lambda item: item["parameters"].__setitem__("rank_minimum", 0),
        lambda item: item["parameters"].__setitem__("rank_maximum", 8),
        lambda item: item["parameters"].__setitem__("extra_common_zero_offset", 9),
        lambda item: item["parameters"].__setitem__("rank9_record_cap", 61871313426630600),
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
        "RATE_HALF_MCA_RANK11_KERNEL_CANONICAL_BASIS_GLOBALIZER_PASS "
        f"ranks={result['ranks']} rank9_cap={result['rank9']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
