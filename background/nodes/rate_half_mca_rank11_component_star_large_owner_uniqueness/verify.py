#!/usr/bin/env python3
"""Verify component-star large-owner uniqueness."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "731e65b2926b11ef0d192e11fb55e5eac280e0d93038270fe131d79b9ca7b076"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-component-star-large-owner-uniqueness-v1",
        "schema",
    )
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_component_star_owner_pencil_router",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["R"], p["d"]) == (1048576, 67472), "row")
    require((p["K_prime_min"], p["K_prime_max"]) == (10, 1048576), "range")
    delta = p["large_owner_deficiency_ceiling"]
    require(delta == 22320, "deficiency")
    require(p["two_owner_deficiency_sum"] == 2 * delta == 44640, "two owners")
    margin = p["d"] - 2 * delta
    require(p["distance_margin_after_two_owners"] == margin == 22832, "margin")
    require(p["intersection_over_root_cap"] == margin + 1 == 22833, "root gap")
    for k_value in (10, 11, 4923, 1048576):
        m_value = p["d"] + k_value
        require(m_value - 2 * delta > k_value - 1, "uniform root contradiction")
    require(p["owner_count_per_record"] == 1, "uniqueness")
    require("not a count of owners across records" in str(data.get("nonclaim")), "nonclaim")
    return {"delta": delta, "gap": margin + 1}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("d", 44639),
        lambda item: item["parameters"].__setitem__("large_owner_deficiency_ceiling", 33737),
        lambda item: item["parameters"].__setitem__("two_owner_deficiency_sum", 44639),
        lambda item: item["parameters"].__setitem__("distance_margin_after_two_owners", 22831),
        lambda item: item["parameters"].__setitem__("intersection_over_root_cap", 22832),
        lambda item: item["parameters"].__setitem__("owner_count_per_record", 2),
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
        "RATE_HALF_MCA_RANK11_COMPONENT_STAR_LARGE_OWNER_UNIQUENESS_PASS "
        f"delta={result['delta']} root_gap={result['gap']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
