#!/usr/bin/env python3
"""Verify the rank-eleven dense-locator incidence dichotomy."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "6eec697bc3729eab2aba4d282b3c1536e862826cc7c1c17379c2df4ebf55d59b"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceiling_ratio(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def isolated_equivalent(R: int, d: int, K: int, bezout: int, size: int) -> int:
    return ceiling_ratio(bezout * comb(R + K, size), comb(d + K, size))


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-dense-locator-component-incidence-dichotomy-v1",
        "schema",
    )
    require(len(data.get("dependencies", [])) == 4, "dependencies")
    parameters = data.get("parameters")
    require(isinstance(parameters, dict), "parameters")
    pins = {
        "R": 1048576,
        "d": 67472,
        "K_min": 10,
        "K_max": 1048576,
        "correction_dimension": 10,
        "tuple_size": 11,
        "dense_locator_degree": 18,
        "isolated_bezout": 198,
        "budget": 274980728111395087,
        "near_charge": 134944,
        "removed_dense_records": 18,
        "non_dense_record_floor": 274980728111260126,
        "isolated_equivalent_ceiling": 2526815879272440,
        "isolated_incidence_ppb_ceiling": 9189066,
        "component_incidence_ppb_floor": 990810934,
        "one_lane_ppb_floor": 495405467,
    }
    require(parameters == pins, "parameter pins")
    require(
        parameters["isolated_bezout"]
        == parameters["dense_locator_degree"] * parameters["tuple_size"],
        "Bezout",
    )
    floor = parameters["budget"] + 1 - parameters["near_charge"] - parameters["removed_dense_records"]
    require(floor == parameters["non_dense_record_floor"], "record floor")
    endpoint = isolated_equivalent(
        parameters["R"],
        parameters["d"],
        parameters["K_min"],
        parameters["isolated_bezout"],
        parameters["tuple_size"],
    )
    require(endpoint == parameters["isolated_equivalent_ceiling"], "endpoint")
    for K in (10, 11, 100, 4923, 1048576):
        require(
            isolated_equivalent(1048576, 67472, K, 198, 11) <= endpoint,
            f"monotone sample {K}",
        )
    proper_ppb = ceiling_ratio(endpoint * 10**9, floor)
    require(proper_ppb == parameters["isolated_incidence_ppb_ceiling"], "proper ppb")
    require(10**9 - proper_ppb == parameters["component_incidence_ppb_floor"], "component ppb")
    require(
        parameters["component_incidence_ppb_floor"] // 2
        == parameters["one_lane_ppb_floor"],
        "lane ppb",
    )
    require(
        data.get("lanes")
        == ["FULL_RANK_AFFINE_OWNER_COMPONENT", "RANK_DEFICIENT_KERNEL_COMPONENT"],
        "lanes",
    )
    require(len(data.get("logical_pins", [])) == 5, "logical pins")
    require("Overlap multiplicity" in str(data.get("nonclaim")), "nonclaim")
    return {"endpoint": endpoint, "component_ppb": 10**9 - proper_ppb}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("dense_locator_degree", 19),
        lambda item: item["parameters"].__setitem__("isolated_bezout", 197),
        lambda item: item["parameters"].__setitem__("removed_dense_records", 17),
        lambda item: item["parameters"].__setitem__("isolated_equivalent_ceiling", 2526815879272439),
        lambda item: item["parameters"].__setitem__("component_incidence_ppb_floor", 990810935),
        lambda item: item["lanes"].pop(),
        lambda item: item["logical_pins"].pop(),
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
        "RATE_HALF_MCA_RANK11_DENSE_LOCATOR_COMPONENT_INCIDENCE_DICHOTOMY_PASS "
        f"isolated={result['endpoint']} component_ppb={result['component_ppb']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
