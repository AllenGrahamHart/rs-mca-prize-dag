#!/usr/bin/env python3
"""Verify elimination of the rank-nine weighted target."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "78436c5e0cc6cd9d313e8d4de24e849d87676a4236be6e2c09b203576a002ab9"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def demand_fraction(p: dict[str, int], k: int) -> tuple[int, int]:
    n, m = p["n_offset"] + k, p["m_offset"] + k
    numerator = (
        p["lane_density_numerator"]
        * p["residual_record_floor"]
        * comb(m, 9)
        * comb(m - 9, 2)
    )
    denominator = p["lane_density_denominator"] * comb(n, 9)
    return numerator, denominator


def weighted_cap(p: dict[str, int], k: int) -> int:
    n, m = p["n_offset"] + k, p["m_offset"] + k
    return (p["support_complement"] + 1) * (m - 10) * n


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-rank9-weighted-target-elimination-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_component_ninesubset_target_router",
        "rate_half_mca_rank11_component_ninesubset_weighted_concentrator",
        "rate_half_mca_rank11_rank9_weighted_component_cap",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["n_offset"] - p["m_offset"] == p["support_complement"] == 981104, "complement")
    require(p["fixed_record_population"] == 2578110 > p["low_core_record_cap"] == 1434405, "population gap")
    require(p["forced_common_core_floor"] == 134944, "core floor")
    require(p["m_offset"] + p["small_dimension_ceiling"] == 134944, "small split")
    require(p["weighted_boundary_dimension"] == p["small_dimension_ceiling"] + 1 == 67473, "boundary")
    k = p["weighted_boundary_dimension"]
    n, m = p["n_offset"] + k, p["m_offset"] + k
    require((n, m) == (p["weighted_boundary_n"], p["weighted_boundary_m"]) == (1116049, 134945), "boundary row")
    numerator, denominator = demand_fraction(p, k)
    demand = ceil_div(numerator, denominator)
    cap = weighted_cap(p, k)
    require(numerator > cap * denominator, "rational boundary gap")
    require(p["weighted_boundary_demand"] == demand == 6849288576200976639, "boundary demand")
    require(p["weighted_boundary_cap"] == cap == 147748596828055575, "boundary cap")
    require(p["weighted_boundary_gap"] == demand - cap == 6701539979372921064, "integer gap")
    # The simplified ratio has ten increasing positive factors.
    for i in range(9):
        require((m + 1 - i) * (n - i) > (m - i) * (n + 1 - i), f"ratio factor {i}")
    require((m - 8) * n > (m - 9) * (n + 1), "final ratio factor")
    require("leaves the fixed-kernel" in str(data.get("nonclaim")), "nonclaim")
    return {"demand": demand, "cap": cap, "gap": demand - cap}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("fixed_record_population", 1434405),
        lambda item: item["parameters"].__setitem__("forced_common_core_floor", 134943),
        lambda item: item["parameters"].__setitem__("small_dimension_ceiling", 67473),
        lambda item: item["parameters"].__setitem__("weighted_boundary_dimension", 67472),
        lambda item: item["parameters"].__setitem__("lane_density_numerator", 495405466),
        lambda item: item["parameters"].__setitem__("weighted_boundary_demand", 6849288576200976638),
        lambda item: item["parameters"].__setitem__("weighted_boundary_cap", 147748596828055576),
        lambda item: item["parameters"].__setitem__("weighted_boundary_gap", 6701539979372921063),
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
        "RATE_HALF_MCA_RANK11_RANK9_WEIGHTED_TARGET_ELIMINATION_PASS "
        f"demand={result['demand']} cap={result['cap']} gap={result['gap']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
