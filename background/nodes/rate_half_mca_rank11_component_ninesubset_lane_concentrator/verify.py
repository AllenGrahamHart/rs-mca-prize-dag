#!/usr/bin/env python3
"""Verify the component-lane nine-subset concentrator."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "f3e7cebc5b859df1d9950ca5cf49c085a994b91c949da3e49fbe701ffe169192"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceiling(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-component-ninesubset-lane-concentrator-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_rank11_dense_locator_component_incidence_dichotomy"],
        "dependency",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["R"] == 1048576 and p["d"] == 67472, "row split")
    require(p["K_min"] == 10 and p["K_max"] == 1048576, "K range")
    require(
        p["dominant_lane_incidence_ppb_floor"] * 2
        == p["combined_component_incidence_ppb_floor"]
        == 990810934,
        "lane split",
    )
    require((p["component_tuple_size"], p["selector_size"]) == (11, 9), "sizes")
    require(p["subsets_per_component_tuple"] == comb(11, 9) == 55, "subsets")
    n = p["R"] + p["K_min"]
    m = p["d"] + p["K_min"]
    require((n, m) == (p["endpoint_n"], p["endpoint_m"]), "endpoint row")
    endpoint = ceiling(Fraction(
        p["dominant_lane_incidence_ppb_floor"]
        * p["record_floor"]
        * comb(m, 9),
        10**9 * comb(n, 9),
    ))
    require(endpoint == p["uniform_fixed_selector_record_floor"] == 2578110, "endpoint")
    for index in range(9):
        require(p["R"] - p["d"] > 0, f"monotone factor {index}")
    require(data.get("routes") == [
        "DOMINANT_AFFINE_OWNER_LANE_FIXED_B",
        "DOMINANT_KERNEL_LANE_FIXED_B",
    ], "routes")
    require(len(data.get("identities", [])) == 3, "identities")
    require("not a component identity" in str(data.get("nonclaim")), "nonclaim")
    return {"endpoint": endpoint, "lane_ppb": p["dominant_lane_incidence_ppb_floor"]}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("record_floor", 1),
        lambda item: item["parameters"].__setitem__("dominant_lane_incidence_ppb_floor", 495405466),
        lambda item: item["parameters"].__setitem__("selector_size", 10),
        lambda item: item["parameters"].__setitem__("subsets_per_component_tuple", 54),
        lambda item: item["parameters"].__setitem__("uniform_fixed_selector_record_floor", 2578109),
        lambda item: item["routes"].pop(),
    )
    controls = []
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_COMPONENT_NINESUBSET_LANE_CONCENTRATOR_PASS "
        f"lane_ppb={result['lane_ppb']} endpoint={result['endpoint']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
