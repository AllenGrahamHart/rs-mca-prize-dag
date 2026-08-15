#!/usr/bin/env python3
"""Verify the K'=11 circuit-shadow split-pencil payment."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "72c6d95b858551bceea1467d6832b9a0e1daf73edac9c9ae54dc9af3e11b692a"


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
        data.get("schema") == "rate-half-mca-rank11-k11-circuit-split-pencil-payment-v1",
        "schema",
    )
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_dense_locator_component_incidence_dichotomy",
        "rate_half_mca_rank11_dense_root_highspan_saturation",
        "rate_half_mca_rank11_rank8_codimension_one_circuit_shadow_census",
        "rate_half_mca_rank11_rank9_residual_petal_capacity_cut",
        "rate_half_mca_weighted_split_pencil_core_offset_cap",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    k, n, m = int(p["K_prime"]), int(p["n_prime"]), int(p["m_prime"])
    require(k == 11 and (n, m) == (1048576 + k, 67472 + k), "row")
    require(p["correction_dimension"] == 10, "correction dimension")
    require(p["ambient_RS_dimension"] == 11, "ambient dimension")
    require(p["rank9_core_sizes"] == [9, 10], "core sizes")
    require(p["rank9_core_caps"] == [9274924665987729, 9275866238180030], "core caps")
    chart_cap = max(p["rank9_core_caps"])
    require(p["uniform_rank9_chart_cap"] == chart_cap, "uniform chart cap")
    global_marks = comb(n, 9) * chart_cap
    require(
        p["global_rank9_mark_capacity"] == global_marks
        == 39175699244380414710274828706724897216747022733515052264273968850,
        "global rank-nine marks",
    )

    shadow_counts = [55 - comb(11 - c, 2) for c in range(1, 12)]
    require(p["high_circuit_threshold"] == 6, "high threshold")
    require(p["minimum_high_circuit_rank9_shadows"] == shadow_counts[5] == 45, "shadow floor")
    high_cap = global_marks // 45
    require(
        p["high_circuit_incidence_cap"] == high_cap
        == 870571094319564771339440637927219938149933838522556716983865974,
        "high incidence cap",
    )
    require(p["low_circuit_support_ceiling"] == 5, "low support ceiling")
    require(p["low_circuit_support_coalesces"] is True, "low coalescence")
    require(p["low_circuit_per_record_cap_formula"] == "C(m_prime-1,10)", "low formula")
    for circuit_size in range(1, 5):
        require(
            comb(m - circuit_size, 11 - circuit_size)
            > comb(m - circuit_size - 1, 10 - circuit_size),
            f"low cap monotonic c={circuit_size}",
        )

    records = int(p["residual_record_floor"])
    low_cap = records * comb(m - 1, 10)
    total_cap = high_cap + low_cap
    numerator = int(p["component_density_numerator"]) * records * comb(m, 11)
    denominator = int(p["component_density_denominator"])
    demand = ceil_div(numerator, denominator)
    raw = numerator - total_cap * denominator
    coefficient = (
        int(p["component_density_numerator"]) * comb(m, 11)
        - denominator * comb(m - 1, 10)
    )
    require(p["component_density_numerator"] == 990810934, "component density")
    require(p["component_density_denominator"] == 10**9, "density denominator")
    require(p["low_circuit_incidence_cap_at_record_floor"] == low_cap, "low cap")
    require(p["total_capacity_at_record_floor"] == total_cap, "total cap")
    require(p["required_incidence_at_record_floor"] == demand, "demand")
    require(p["demand_capacity_gap"] == demand - total_cap, "gap")
    require(p["raw_demand_capacity_cross"] == raw > 0, "raw crossing")
    require(p["record_coefficient_cross"] == coefficient > 0, "record monotonicity")
    require(p["newly_closed_rows"] == [11, 11], "closed row")
    require(p["remaining_rank9_interval"] == [12, 15528], "remaining interval")
    require("No row K'>=12" in str(data.get("nonclaim")), "nonclaim")
    return {
        "chart_cap": chart_cap,
        "global_marks": global_marks,
        "high_cap": high_cap,
        "low_cap": low_cap,
        "total_cap": total_cap,
        "demand": demand,
        "gap": demand - total_cap,
        "coefficient": coefficient,
    }


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("K_prime", 12),
        lambda item: item["parameters"].__setitem__("correction_dimension", 9),
        lambda item: item["parameters"].__setitem__("rank9_core_sizes", [9]),
        lambda item: item["parameters"].__setitem__("uniform_rank9_chart_cap", result["chart_cap"] - 1),
        lambda item: item["parameters"].__setitem__("high_circuit_threshold", 5),
        lambda item: item["parameters"].__setitem__("minimum_high_circuit_rank9_shadows", 44),
        lambda item: item["parameters"].__setitem__("low_circuit_support_coalesces", False),
        lambda item: item["parameters"].__setitem__("low_circuit_per_record_cap_formula", "C(m_prime,11)"),
        lambda item: item["parameters"].__setitem__("total_capacity_at_record_floor", result["total_cap"] + 1),
        lambda item: item["parameters"].__setitem__("demand_capacity_gap", result["gap"] - 1),
        lambda item: item["parameters"].__setitem__("record_coefficient_cross", 0),
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
        "PASS K11 circuit split-pencil payment primary: "
        f"chart_cap {result['chart_cap']}, demand {result['demand']}, "
        f"capacity {result['total_cap']}, gap {result['gap']}, "
        f"{rejected}/{len(mutations)} hostile mutations"
    )


if __name__ == "__main__":
    main()
