#!/usr/bin/env python3
"""Verify the exact residual-petal rank-nine capacity cut."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "df54f15d0ba1f4e335eb606f8f47c496e240ac7e2fe3beb209e100a3a4a7dd39"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def packed_line(p: dict[str, object], a: int) -> tuple[int, int]:
    d = int(p["petal_budget_offset"])
    full, remainder = 1 + d // a, d % a
    slope = d + a
    intercept = (
        slope * (67462 - a)
        + (full * a * (a - 1) + remainder * (remainder - 1)) // 2
    )
    return slope, intercept


def packed_charge(p: dict[str, object], k: int, a: int) -> int:
    slope, intercept = packed_line(p, a)
    return slope * k + intercept


def demand_fraction(p: dict[str, object], k: int) -> tuple[int, int]:
    n, m = int(p["n_offset"]) + k, int(p["m_offset"]) + k
    return (
        int(p["lane_density_numerator"])
        * int(p["residual_record_floor"])
        * comb(m, 9)
        * comb(m - 9, 2),
        int(p["lane_density_denominator"]) * comb(n, 9),
    )


def cap(p: dict[str, object], k: int) -> int:
    return int(p["fixed_owner_record_cap"]) * (
        int(p["packed_charge_slope"]) * k
        + int(p["packed_charge_intercept"])
    )


def row(p: dict[str, object], k: int) -> tuple[int, int, int, bool]:
    numerator, denominator = demand_fraction(p, k)
    upper = cap(p, k)
    raw = numerator - upper * denominator
    return ceil_div(numerator, denominator), upper, raw, raw > 0


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-rank9-exact-petal-partition-capacity-cut-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_rank11_rank9_residual_petal_capacity_cut"],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(int(p["n_offset"]) - int(p["m_offset"]) == 981104, "complement")
    require(p["petal_budget_offset"] == p["fixed_owner_record_cap"] == 981105, "D1")
    require(p["fixed_subset_size"] == 9, "fixed subset")
    require(p["claimed_K_prime_interval"] == [10, 15634], "claimed interval")
    require(p["a_minimum"] == 67472, "minimum a")
    require(p["a_maximum_formula"] == "67462+K_prime", "maximum a formula")
    require(p["a_maximum_at_claimed_endpoint"] == 83096, "maximum a")
    require(p["partition_formula"] == "r*q_j(a)+q_j(b)", "partition formula")
    require(p["full_petals_formula"] == "1+floor(981105/a)", "full petals")
    require(p["remainder_formula"] == "981105 mod a", "remainder")

    blocks = p["quotient_blocks"]
    require(blocks == [
        [14, 67472, 70078],
        [13, 70079, 75469],
        [12, 75470, 81758],
        [11, 81759, 83096],
    ], "quotient blocks")
    d = int(p["petal_budget_offset"])
    for quotient, left, right in blocks:
        require(d // left == d // right == quotient, f"block quotient {quotient}")
        require(quotient * quotient + quotient - 1 > 0, f"block convexity {quotient}")
        if left < right:
            second = (
                packed_charge(p, 15634, left + 2)
                - 2 * packed_charge(p, 15634, left + 1)
                + packed_charge(p, 15634, left)
            )
            require(second == quotient * quotient + quotient - 1, f"second difference {quotient}")

    endpoints = p["convexity_endpoints"]
    require(endpoints == [item for block in blocks for item in block[1:]], "endpoints")
    baseline_a = int(p["maximizing_a"])
    endpoint_k = int(p["claimed_K_prime_interval"][-1])
    baseline = packed_charge(p, endpoint_k, baseline_a)
    gaps = [baseline - packed_charge(p, endpoint_k, int(a)) for a in endpoints]
    require(gaps == p["endpoint_gaps"], "endpoint gaps")
    require(all(gap >= 0 for gap in gaps), "endpoint maximum")
    require(all(d + int(a) > d + baseline_a for a in endpoints[1:]), "line slopes")

    slope, intercept = packed_line(p, baseline_a)
    require((slope, intercept) == (
        p["packed_charge_slope"], p["packed_charge_intercept"]
    ), "baseline line")
    require(p["maximizing_full_petals"] == 1 + d // baseline_a == 15, "full count")
    require(p["maximizing_remainder"] == d % baseline_a == 36497, "remainder")
    require(
        p["capacity_formula"] == "981105*(1048577*K_prime+34798536326)",
        "capacity formula",
    )

    last = row(p, int(p["last_open_K_prime"]))
    first = row(p, int(p["first_closed_K_prime"]))
    require(int(p["last_open_K_prime"]) + 1 == int(p["first_closed_K_prime"]) == 15529, "boundary")
    require(last == (
        p["last_open_demand"], p["last_open_cap"], p["last_open_raw_cross"], False
    ), "last open")
    require(first == (
        p["first_closed_demand"], p["first_closed_cap"], p["first_closed_raw_cross"], True
    ), "first closed")
    require(p["last_open_gap"] == last[1] - last[0] == 1296184504470, "last gap")
    require(p["first_closed_gap"] == first[0] - first[1] == 3893601214441, "first gap")

    a_term, b_term = int(p["m_offset"]) - 9, int(p["m_offset"]) - 10
    expected_poly = [
        slope,
        slope + 2 * intercept,
        intercept * (a_term + b_term + 1) - slope * a_term * b_term,
    ]
    require(p["persistence_polynomial"] == expected_poly, "persistence polynomial")
    shift = int(p["persistence_shift"])
    shifted = [
        expected_poly[0],
        2 * expected_poly[0] * shift + expected_poly[1],
        expected_poly[0] * shift * shift + expected_poly[1] * shift + expected_poly[2],
    ]
    require(p["persistence_shifted_polynomial"] == shifted, "shifted polynomial")
    require(all(value > 0 for value in shifted), "positive shifted coefficients")
    require(p["newly_closed_interval"] == [15529, 15634], "new closure")
    require(p["remaining_rank9_interval"] == [10, 15528], "remaining interval")
    require("remains open" in str(data.get("nonclaim")), "nonclaim")

    for k in range(10, 15529):
        require(not row(p, k)[3], f"premature crossing K'={k}")
    for k in range(15529, 15635):
        require(row(p, k)[3], f"lost crossing K'={k}")

    return {
        "endpoint_candidates": len(endpoints),
        "rows": 15634 - 10 + 1,
        "last_gap": last[1] - last[0],
        "first_gap": first[0] - first[1],
    }


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("petal_budget_offset", 981104),
        lambda item: item["parameters"]["quotient_blocks"][0].__setitem__(2, 70079),
        lambda item: item["parameters"]["endpoint_gaps"].__setitem__(1, 676268726),
        lambda item: item["parameters"].__setitem__("maximizing_a", 67473),
        lambda item: item["parameters"].__setitem__("last_open_K_prime", 15527),
        lambda item: item["parameters"].__setitem__("first_closed_gap", 3893601214440),
        lambda item: item["parameters"]["persistence_polynomial"].__setitem__(2, 0),
        lambda item: item.__setitem__("nonclaim", "all rows closed"),
    )
    rejected = 0
    for mutation in mutations:
        hostile = copy.deepcopy(data)
        mutation(hostile)
        try:
            validate(hostile)
        except (KeyError, Reject, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "hostile mutation rejection")
    print(
        "PASS exact-petal primary: "
        f"{result['rows']} rows, {result['endpoint_candidates']} endpoints, "
        f"{rejected}/{len(mutations)} hostile mutations"
    )


if __name__ == "__main__":
    main()
