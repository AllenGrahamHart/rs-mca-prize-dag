#!/usr/bin/env python3
"""Verify the rank-eight dense-owner terminal bridge."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "c77779cfc39566264dbfa48bfe4081eb6c46a4913c579e21e1bcf204de13da67"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_ratio(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def row(p: dict[str, object], kprime: int) -> tuple[int, int, int]:
    nprime = int(p["n_offset"]) + kprime
    mprime = int(p["m_offset"]) + kprime
    weight = ceil_ratio(
        55 * int(p["component_ppb"]) * int(p["record_floor"]) * comb(mprime, 11),
        int(p["ppb_denominator"]) * comb(nprime, 9),
    )
    pairs = comb(nprime - 9, 2)
    signed = weight - int(p["comparison_multiplier"]) * pairs
    return weight, pairs, signed


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-rank8-dense-owner-terminal-bridge-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_component_ninesubset_weighted_concentrator",
        "rate_half_mca_rank11_rank8_owner_pair_weight_cap",
        "rate_half_mca_rank11_pair_core_route_cut_import",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(int(p["n_offset"]) - int(p["m_offset"]) == p["support_complement"] == 981104, "complement")
    require(p["owner_record_target"] - 1 == p["comparison_multiplier"] == 200631, "owner target")
    require(p["last_unforced_dimension"] + 1 == p["first_forced_dimension"] == 22526, "boundary")
    last = row(p, int(p["last_unforced_dimension"]))
    first = row(p, int(p["first_forced_dimension"]))
    require(last == (
        p["last_unforced_weight"], p["last_unforced_pair_resource"], -p["last_unforced_deficit"]
    ), "last unforced row")
    require(first == (
        p["first_forced_weight"], p["first_forced_pair_resource"], p["first_forced_excess"]
    ), "first forced row")
    require(p["delta5_record_cap"] == 1 + p["support_complement"] // 5 == 196221, "delta-five cap")
    require(p["delta5_record_cap"] < p["owner_record_target"], "deficiency cut")
    require(p["deficiency_ceiling"] == 4, "deficiency ceiling")
    for index in range(11):
        require(
            Fraction(89999 - index, 1071103 - index)
            > Fraction(89998 - index, 1071102 - index),
            f"monotone factor {index}",
        )
    require(p["terminal_interval_maximum"] == 37995, "interval maximum")
    require("not chronology-assigned" in str(data.get("nonclaim")), "nonclaim")
    return {"last": -last[2], "first": first[2], "delta5": int(p["delta5_record_cap"])}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("comparison_multiplier", 200630),
        lambda item: item["parameters"].__setitem__("first_forced_dimension", 22525),
        lambda item: item["parameters"].__setitem__("first_forced_excess", 11714977255864),
        lambda item: item["parameters"].__setitem__("delta5_record_cap", 196222),
        lambda item: item["parameters"].__setitem__("deficiency_ceiling", 5),
        lambda item: item["parameters"].__setitem__("terminal_interval_maximum", 37996),
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
        "RATE_HALF_MCA_RANK11_RANK8_DENSE_OWNER_TERMINAL_BRIDGE_PASS "
        f"last_deficit={result['last']} first_excess={result['first']} "
        f"delta5_cap={result['delta5']} controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
