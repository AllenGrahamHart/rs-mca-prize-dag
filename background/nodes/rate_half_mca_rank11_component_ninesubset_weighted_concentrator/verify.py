#!/usr/bin/env python3
"""Verify the weighted nine-subset concentration theorem."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "050954321fc65a504b801b19dc0787e21d31f979f8062319ea67055e37709895"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-component-ninesubset-weighted-concentrator-v1",
        "schema",
    )
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_component_ninesubset_lane_concentrator",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["residual_dimension_minimum"] == 10, "minimum dimension")
    require((p["n_offset"], p["m_offset"]) == (1048576, 67472), "row offsets")
    require(p["residual_record_floor"] == 274980728111260126, "record floor")
    require(
        (p["lane_density_numerator"], p["lane_density_denominator"])
        == (495405467, 1000000000),
        "lane density",
    )
    k = p["residual_dimension_minimum"]
    n, m = p["n_offset"] + k, p["m_offset"] + k
    require((n, m) == (1048586, 67482), "endpoint row")
    require((p["subset_size"], p["extension_size"]) == (9, 2), "sizes")
    require(comb(11, 9) * comb(m, 11) == comb(m, 9) * comb(m - 9, 2), "mark identity")
    numerator = (
        p["lane_density_numerator"]
        * p["residual_record_floor"]
        * comb(m, 9)
        * comb(m - 9, 2)
    )
    denominator = p["lane_density_denominator"] * comb(n, 9)
    marked = ceil_div(numerator, denominator)
    distinct = ceil_div(
        p["lane_density_numerator"] * p["residual_record_floor"] * comb(m, 9),
        p["lane_density_denominator"] * comb(n, 9),
    )
    require(p["marked_endpoint_floor"] == marked == 5868470021012020, "marked endpoint")
    require(p["distinct_record_endpoint_floor"] == distinct == 2578110, "record endpoint")
    require(ceil_div(marked, comb(m - 9, 2)) == distinct, "deduplication")
    require("not a fixed-chart payment" in str(data.get("nonclaim")), "nonclaim")
    return {"marked": marked, "distinct": distinct}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("lane_density_numerator", 495405466),
        lambda item: item["parameters"].__setitem__("residual_record_floor", 274980728111260125),
        lambda item: item["parameters"].__setitem__("subset_size", 10),
        lambda item: item["parameters"].__setitem__("extension_size", 1),
        lambda item: item["parameters"].__setitem__("marked_endpoint_floor", 5868470021012019),
        lambda item: item["parameters"].__setitem__("distinct_record_endpoint_floor", 2578109),
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
        "RATE_HALF_MCA_RANK11_COMPONENT_NINESUBSET_WEIGHTED_CONCENTRATOR_PASS "
        f"marked={result['marked']} distinct={result['distinct']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
