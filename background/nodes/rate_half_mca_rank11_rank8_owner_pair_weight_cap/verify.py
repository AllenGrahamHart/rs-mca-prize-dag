#!/usr/bin/env python3
"""Verify the rank-eight owner-pair weighted cap."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "478aa8e2affd878acaf36cd1fd313fcdb857b552e5edf28dda1e4ad1c59cb32c"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-rank8-owner-pair-weight-cap-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_component_ninesubset_target_router",
        "rate_half_mca_rank11_relative_absorbing_clone_affine_collapse",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["n_offset"] - p["m_offset"] == p["support_complement"] == 981104, "complement")
    require(p["fixed_owner_record_cap"] == p["support_complement"] + 1 == 981105, "owner cap")
    require((p["fixed_subset_size"], p["component_subset_size"]) == (9, 11), "subset sizes")
    k = p["first_closed_dimension"]
    n, m = p["n_offset"] + k, p["m_offset"] + k
    require((n, m) == (p["first_closed_n"], p["first_closed_m"]), "boundary row")
    pairs = comb(n - p["fixed_subset_size"], 2)
    cap = p["fixed_owner_record_cap"] * pairs
    require(p["coordinate_pair_resource"] == pairs == 590309033203, "pair resource")
    require(p["first_closed_weighted_cap"] == cap == 579155144020629315, "weighted cap")
    require("does not pay the lower-shortening" in str(data.get("nonclaim")), "nonclaim")
    return {"pairs": pairs, "cap": cap}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("support_complement", 981103),
        lambda item: item["parameters"].__setitem__("fixed_owner_record_cap", 981104),
        lambda item: item["parameters"].__setitem__("fixed_subset_size", 10),
        lambda item: item["parameters"].__setitem__("component_subset_size", 10),
        lambda item: item["parameters"].__setitem__("coordinate_pair_resource", 590309033202),
        lambda item: item["parameters"].__setitem__("first_closed_weighted_cap", 579155144020629314),
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
        "RATE_HALF_MCA_RANK11_RANK8_OWNER_PAIR_WEIGHT_CAP_PASS "
        f"pairs={result['pairs']} cap={result['cap']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
