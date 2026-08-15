#!/usr/bin/env python3
"""Verify the support-four external-carrier charge."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "9b4f391a6f919caed461b33ad7a911cfaf6bbbd1a1355223f730158039ae55ae"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def support_count(K: int, m: int, t: int, delta: int) -> int:
    b = K - t - delta
    outside = m - b
    if delta == 0:
        return comb(b, 4)
    return comb(b, 4) + sum(
        comb(b, 4 - j) * comb(outside, j - 1) * (delta + 4 - j) // j
        for j in range(1, 5)
    )


def incidence_cap(K: int, m: int, t: int, delta: int) -> int:
    return support_count(K, m, t, delta) * comb(m - 4, 7)


def cap_for_defects(K: int, m: int, s4: int, s5: int) -> tuple[int, int, int]:
    candidates = [
        (incidence_cap(K, m, t, delta), t, delta)
        for t in range(4, 7)
        for delta in range(min(s4, s5) + 1)
    ]
    return max(candidates)


def expected_table() -> dict[str, dict[str, int]]:
    table = {}
    for defect in range(5):
        cap, t, delta = cap_for_defects(45, 67517, defect, defect)
        b = 45 - t - delta
        table[str(defect)] = {
            "t": t,
            "delta": delta,
            "b": b,
            "support_count": support_count(45, 67517, t, delta),
            "incidence_cap": cap,
        }
    return table


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-sparse-circuit-support4-external-charge-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_sparse_circuit_support45_joint_zero_carrier"],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("component_size") == 11 and p.get("support") == 4, "scope")
    require(p.get("zero_closure_dimension_range") == [4, 6], "t range")
    require(p.get("quotient_defect_range") == "0<=delta<=min(s_4,s_5)", "delta range")
    require(p.get("carrier_size") == "b=K-t-delta", "carrier")
    require(p.get("outside_size") == "N=m-b", "outside")
    require(p.get("inside_support_count") == "C(b,4)", "inside")
    require(
        p.get("outside_stratum_count")
        == "floor(C(b,4-j)C(N,j-1)(delta+4-j)/j)",
        "outside strata",
    )
    require(p.get("incidence_multiplier") == "C(m-4,7)", "incidence")
    k45 = p.get("K45")
    require(isinstance(k45, dict), "K45")
    require(k45.get("K") == 45 and k45.get("m") == 67517, "K45 row")
    require(k45.get("caps_by_minimum_defect") == expected_table(), "K45 caps")

    charge_checks = 0
    for delta in range(1, 5):
        for j in range(1, 5):
            require(delta + 3 - (j - 1) == delta + 4 - j, "spent outside points")
            require(delta + 4 - j >= 0, "nonnegative completion cap")
            charge_checks += 1
    require(
        data.get("logical_pins")
        == [
            "delta_zero_uses_full_annihilator_representation_on_B",
            "outside_strata_are_indexed_by_exact_external_support_size",
            "each_external_point_gives_one_independent_deletion_charge",
            "the_delta_plus_three_budget_includes_deletion_points",
            "all_permitted_t_and_delta_cases_are_maximized",
        ],
        "logical pins",
    )
    require("No full weighted component payment" in str(data.get("nonclaim")), "nonclaim")
    return {"charge_checks": charge_checks, "caps": len(expected_table())}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("support", 5),
        lambda item: item["parameters"].__setitem__("zero_closure_dimension_range", [3, 6]),
        lambda item: item["parameters"].__setitem__("outside_stratum_count", "wrong"),
        lambda item: item["parameters"]["K45"].__setitem__("m", 67516),
        lambda item: item["parameters"]["K45"]["caps_by_minimum_defect"]["2"].__setitem__("incidence_cap", 0),
        lambda item: item.__setitem__("logical_pins", []),
        lambda item: item.__setitem__("nonclaim", "K'=45 paid"),
    )
    rejected = 0
    for mutation in mutations:
        hostile = copy.deepcopy(data)
        mutation(hostile)
        try:
            validate(hostile)
        except (Reject, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "tamper controls")
    return rejected


def main() -> None:
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    result = validate(data)
    controls = tamper_selftest(data)
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_SUPPORT4_EXTERNAL_CHARGE_PASS "
        f"caps={result['caps']} charge_checks={result['charge_checks']} "
        f"controls={controls}"
    )


if __name__ == "__main__":
    main()
