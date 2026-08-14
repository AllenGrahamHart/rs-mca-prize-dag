#!/usr/bin/env python3
"""Verify the rank-nine weighted component cap."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "d8000c85400cd931d846b9da91d7203720fb31cedce7abcd08318bf4879a22b5"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-rank9-weighted-component-cap-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_rank9_ninecell_paircore_extension",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["n_offset"] - p["m_offset"] == p["support_complement"] == 981104, "complement")
    require(p["fixed_owner_record_cap"] == p["support_complement"] + 1 == 981105, "owner cap")
    require((p["fixed_subset_size"], p["component_subset_size"]) == (9, 11), "subset sizes")
    k = p["boundary_dimension"]
    n, m = p["n_offset"] + k, p["m_offset"] + k
    require((n, m) == (p["boundary_n"], p["boundary_m"]) == (1116049, 134945), "boundary row")
    cap = p["fixed_owner_record_cap"] * (m - 10) * n
    require(p["boundary_weighted_cap"] == cap == 147748596828055575, "weighted cap")
    require("not a kernel-lane cap" in str(data.get("nonclaim")), "nonclaim")
    return {"cap": cap, "owner": p["fixed_owner_record_cap"]}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("support_complement", 981103),
        lambda item: item["parameters"].__setitem__("fixed_owner_record_cap", 981104),
        lambda item: item["parameters"].__setitem__("fixed_subset_size", 10),
        lambda item: item["parameters"].__setitem__("component_subset_size", 12),
        lambda item: item["parameters"].__setitem__("boundary_m", 134944),
        lambda item: item["parameters"].__setitem__("boundary_weighted_cap", 147748596828055574),
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
        "RATE_HALF_MCA_RANK11_RANK9_WEIGHTED_COMPONENT_CAP_PASS "
        f"owner={result['owner']} boundary_cap={result['cap']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
