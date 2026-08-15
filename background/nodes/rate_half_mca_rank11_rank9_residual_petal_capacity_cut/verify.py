#!/usr/bin/env python3
"""Verify the residual-petal rank-nine capacity crossing."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "2980ce37664731e481b65d74ea39f4635ef8e9cba09bd8c22d48cc1493d1a1a8"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def demand_fraction(p: dict[str, int], k: int) -> tuple[int, int]:
    n, m = p["n_offset"] + k, p["m_offset"] + k
    return (
        p["lane_density_numerator"]
        * p["residual_record_floor"]
        * comb(m, 9)
        * comb(m - 9, 2),
        p["lane_density_denominator"] * comb(n, 9),
    )


def cap_twice(p: dict[str, int], k: int, j: int | None = None) -> int:
    n, m = p["n_offset"] + k, p["m_offset"] + k
    core = k - 1 if j is None else j
    return p["fixed_owner_record_cap"] * (n - core) * (m + core - 20)


def cap(p: dict[str, int], k: int, j: int | None = None) -> int:
    return cap_twice(p, k, j) // 2


def row(p: dict[str, int], k: int) -> tuple[int, int, int, bool]:
    numerator, denominator = demand_fraction(p, k)
    upper = cap(p, k)
    raw_cross = 2 * numerator - cap_twice(p, k) * denominator
    return ceil_div(numerator, denominator), upper, raw_cross, raw_cross > 0


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-rank9-residual-petal-capacity-cut-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_component_ninesubset_target_router",
        "rate_half_mca_rank11_component_ninesubset_weighted_concentrator",
        "rate_half_mca_rank11_rank9_weighted_component_cap",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["n_offset"] - p["m_offset"] == p["support_complement"] == 981104, "complement")
    require(p["fixed_owner_record_cap"] == p["support_complement"] + 1, "owner cap")
    require(p["fixed_subset_size"] == p["common_core_minimum"] == 9, "fixed core")
    require(p["common_core_maximum_formula"] == "K_prime-1", "root ceiling")
    require(p["petal_pair_formula"] == "s*(j-9)+C(s,2)", "petal pairs")
    require(p["capacity_formula"] == "floor(981105*(n_prime-j)*(m_prime+j-20)/2)", "capacity")
    require(p["worst_core_on_claimed_interval"] == "j=K_prime-1", "worst core")
    require(p["last_open_K_prime"] + 1 == p["first_closed_K_prime"] == 15635, "boundary")
    require(p["closed_K_prime_maximum"] == 20617, "closed maximum")
    require(p["remaining_rank9_interval"] == [10, 15634], "remaining interval")

    last = row(p, p["last_open_K_prime"])
    first = row(p, p["first_closed_K_prime"])
    require(last == (
        p["last_open_demand"],
        p["last_open_cap"],
        p["last_open_raw_cross"],
        False,
    ), "last open")
    require(first == (
        p["first_closed_demand"],
        p["first_closed_cap"],
        p["first_closed_raw_cross"],
        True,
    ), "first closed")
    require(p["last_open_gap"] == last[1] - last[0] == 1881744358235, "last gap")
    require(p["first_closed_gap"] == first[0] - first[1] == 3381772318665, "first gap")
    require(last[2] == -18157619613263943707902051344298221552552276539946798639022884527164800, "last raw cross")
    require(first[2] == 32632198107169110848930789755311997983757628901001052346612176459768400, "first raw cross")
    require(p["support_complement"] - 2 * (p["closed_K_prime_maximum"] - 1) + 19 > 0, "core monotonicity")
    require(2 * (p["first_closed_K_prime"] - 11) > 0, "ratio monotonicity")
    require("remains open" in str(data.get("nonclaim")), "nonclaim")
    for k in range(10, p["last_open_K_prime"] + 1):
        require(not row(p, k)[3], f"premature raw crossing K'={k}")
    for k in range(p["first_closed_K_prime"], p["closed_K_prime_maximum"] + 1):
        require(row(p, k)[3], f"lost raw crossing K'={k}")
    return {"last_gap": last[1] - last[0], "first_gap": first[0] - first[1]}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("fixed_subset_size", 10),
        lambda item: item["parameters"].__setitem__("common_core_maximum_formula", "K_prime"),
        lambda item: item["parameters"].__setitem__("petal_pair_formula", "s*(m_prime-10)"),
        lambda item: item["parameters"].__setitem__("last_open_K_prime", 15633),
        lambda item: item["parameters"].__setitem__("first_closed_K_prime", 15634),
        lambda item: item["parameters"].__setitem__("first_closed_gap", 3381772318664),
        lambda item: item["parameters"].__setitem__("closed_K_prime_maximum", 500000),
        lambda item: item.__setitem__("nonclaim", "all rows closed"),
    )
    caught = 0
    for mutation in mutations:
        changed = copy.deepcopy(data)
        mutation(changed)
        try:
            validate(changed)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "hostile mutations")
    print(
        "RATE_HALF_MCA_RANK11_RANK9_RESIDUAL_PETAL_CAPACITY_CUT_PASS "
        f"last_gap={result['last_gap']} first_gap={result['first_gap']} "
        f"remaining=10..15634 controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
