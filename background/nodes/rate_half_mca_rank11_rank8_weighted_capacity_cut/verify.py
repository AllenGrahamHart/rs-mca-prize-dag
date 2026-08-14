#!/usr/bin/env python3
"""Verify the rank-eight weighted capacity crossing."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "dad2aa8f83ec9cd1bbcebad2f7b127efd2037743df539e2f2662629a4a1c1396"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_ratio(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def demand(p: dict[str, int], kprime: int) -> int:
    nprime = p["n_offset"] + kprime
    mprime = p["m_offset"] + kprime
    return ceil_ratio(
        55 * p["component_ppb"] * p["record_floor"] * comb(mprime, 11),
        p["ppb_denominator"] * comb(nprime, 9),
    )


def cap(p: dict[str, int], kprime: int) -> int:
    nprime = p["n_offset"] + kprime
    return p["fixed_owner_record_cap"] * comb(nprime - 9, 2)


def strict_raw_gap(p: dict[str, int], kprime: int) -> bool:
    nprime = p["n_offset"] + kprime
    mprime = p["m_offset"] + kprime
    left = 55 * p["component_ppb"] * p["record_floor"] * comb(mprime, 11)
    right = p["ppb_denominator"] * comb(nprime, 9) * cap(p, kprime)
    return left > right


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-rank8-weighted-capacity-cut-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_component_ninesubset_weighted_concentrator",
        "rate_half_mca_rank11_rank8_owner_pair_weight_cap",
        "rate_half_mca_rank11_rank9_weighted_target_elimination",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["n_offset"] - p["m_offset"] == p["support_complement"] == 981104, "complement")
    require(p["fixed_owner_record_cap"] == p["support_complement"] + 1 == 981105, "owner cap")
    require(p["last_open_dimension"] + 1 == p["first_closed_dimension"] == 37996, "boundary dimensions")
    last_demand = demand(p, p["last_open_dimension"])
    last_cap = cap(p, p["last_open_dimension"])
    first_demand = demand(p, p["first_closed_dimension"])
    first_cap = cap(p, p["first_closed_dimension"])
    require((last_demand, last_cap, last_cap - last_demand) == (
        p["last_open_demand"], p["last_open_cap"], p["last_open_gap"]
    ), "last open row")
    require((first_demand, first_cap, first_demand - first_cap) == (
        p["first_closed_demand"], p["first_closed_cap"], p["first_closed_gap"]
    ), "first closed row")
    require(last_demand <= last_cap and first_demand > first_cap, "crossing")
    require(strict_raw_gap(p, p["first_closed_dimension"]), "strict raw gap")
    require(p["ratio_formula"] == "constant*C(m_prime,11)/C(n_prime,11)", "ratio formula")
    require(p["deployed_dimension_maximum"] == 1048576, "deployed maximum")
    require("remains open below" in str(data.get("nonclaim")), "nonclaim")
    return {"last_gap": last_cap - last_demand, "first_gap": first_demand - first_cap}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("component_ppb", 495405466),
        lambda item: item["parameters"].__setitem__("record_floor", 274980728111260125),
        lambda item: item["parameters"].__setitem__("last_open_dimension", 37994),
        lambda item: item["parameters"].__setitem__("first_closed_dimension", 37995),
        lambda item: item["parameters"].__setitem__("first_closed_gap", 36370688210983),
        lambda item: item["parameters"].__setitem__("deployed_dimension_maximum", 1048575),
        lambda item: item["parameters"].__setitem__("ratio_formula", "constant*C(m_prime,10)/C(n_prime,10)"),
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
        "RATE_HALF_MCA_RANK11_RANK8_WEIGHTED_CAPACITY_CUT_PASS "
        f"last_gap={result['last_gap']} first_gap={result['first_gap']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
