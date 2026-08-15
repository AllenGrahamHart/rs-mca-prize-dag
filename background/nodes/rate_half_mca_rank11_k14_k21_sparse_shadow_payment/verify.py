#!/usr/bin/env python3
"""Verify the exact K'=14..21 joint sparse-shadow payments."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "eb1c5343d7aee27704ff1c9a5a30639e3cb101c51e7b13eb0a3f04be071f56e1"
RECORD_FLOOR = 274980728111260126
DENSITY_NUMERATOR = 990810934
DENSITY_DENOMINATOR = 10**9


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def kernel_record_cap(kprime: int, corank: int) -> int:
    if corank == 9:
        return 61871313426630599
    rank = 10 - corank
    shortened = kprime - rank
    zero_endpoint = Fraction(
        falling(1048576 + shortened, corank + 1),
        (67472 + shortened) * rising(67473, corank - 1),
    )
    maximum_endpoint = Fraction(
        falling(1048576 + corank, corank + 1),
        rising(67473, corank),
    )
    return int(max(zero_endpoint, maximum_endpoint))


def offset_capacity(petal_mass: int, total: int, offset: int) -> int:
    heavy = total // (petal_mass // 2 + 1)
    cross_floor = petal_mass * petal_mass // 4
    balanced = comb(total, 2) * (cross_floor + offset * petal_mass) // cross_floor
    collision = comb(heavy, 2) * (comb(petal_mass - 1, 2) + offset * petal_mass)
    vertex_num = (petal_mass - 2) * total + 2 * heavy * offset * petal_mass
    vertex_den = 2 * (petal_mass - 2)
    center = vertex_num // vertex_den
    clean = max(
        light
        * (
            (petal_mass - 2) * (total - light)
            + 2 * heavy * offset * petal_mass
        )
        // 2
        for light in range(max(0, center - 3), min(total, center + 3) + 1)
    )
    return clean + balanced + collision


def completion_value(m: int, support: int, completions: int) -> int:
    return completions * comb(m - support + 1 - completions, 11 - support)


def row(kprime: int) -> dict[str, int]:
    n = 1048576 + kprime
    m = 67472 + kprime
    quotient = kprime - 10

    kernel = sum(
        comb(n, 10 - corank)
        * kernel_record_cap(kprime, corank)
        * comb(quotient, corank + 1)
        for corank in range(1, min(9, quotient - 1) + 1)
    )

    core_caps = [
        offset_capacity(m - core, n - core, core - 9)
        for core in range(9, kprime)
    ]
    chart = max(core_caps)
    maximizing_core = 9 + core_caps.index(chart)
    marks = comb(n, 9) * chart

    structured: dict[int, int] = {}
    unstructured: dict[int, int] = {}
    for support in range(2, 6):
        structured[support] = (
            comb(quotient + 4, support) * comb(m - support, 11 - support)
        )
        maximum = max(
            completion_value(m, support, completions)
            for completions in range(quotient)
        )
        unstructured[support] = comb(m, support - 1) * maximum // support
    weights = {support: 45 - (55 - comb(11 - support, 2)) for support in range(2, 6)}
    structured_premium = sum(weights[support] * structured[support] for support in weights)
    unstructured_premium = sum(weights[support] * unstructured[support] for support in weights)
    premium = max(structured_premium, unstructured_premium)

    full_rank = (marks + RECORD_FLOOR * premium) // 45
    total = kernel + full_rank
    demand_numerator = DENSITY_NUMERATOR * RECORD_FLOOR * comb(m, 11)
    demand = (demand_numerator + DENSITY_DENOMINATOR - 1) // DENSITY_DENOMINATOR
    coefficient = 45 * DENSITY_NUMERATOR * comb(m, 11) - DENSITY_DENOMINATOR * premium
    raw = RECORD_FLOOR * coefficient - DENSITY_DENOMINATOR * (45 * kernel + marks)
    return {
        "kernel": kernel,
        "chart": chart,
        "maximizing_core": maximizing_core,
        "marks": marks,
        "structured_premium": structured_premium,
        "unstructured_premium": unstructured_premium,
        "premium": premium,
        "full_rank": full_rank,
        "total": total,
        "demand": demand,
        "gap": demand - total,
        "coefficient": coefficient,
        "raw": raw,
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank11-k14-k21-sparse-shadow-payment-v1",
        "schema",
    )
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_dense_locator_component_incidence_dichotomy",
        "rate_half_mca_rank11_dense_root_highspan_saturation",
        "rate_half_mca_rank11_kernel_rankstratified_capacity_cut",
        "rate_half_mca_rank11_rank9_residual_petal_capacity_cut",
        "rate_half_mca_weighted_split_pencil_core_offset_cap",
        "rate_half_mca_sparse_circuit_completion_dimension_ladder",
        "rate_half_mca_rank9_sparse_shadow_joint_ledger",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["closed_K_prime_interval"] == [14, 21], "closed interval")
    require(p["n_prime_formula"] == "1048576+K_prime", "n formula")
    require(p["m_prime_formula"] == "67472+K_prime", "m formula")
    require(p["correction_dimension"] == 10, "correction dimension")
    require((p["component_density_numerator"], p["component_density_denominator"])
            == (DENSITY_NUMERATOR, DENSITY_DENOMINATOR), "density")
    require(p["residual_record_floor"] == RECORD_FLOOR, "record floor")
    require(p["kernel_corank_ceiling"] == 9, "kernel ceiling")
    require(p["rank9_core_minimum"] == 9, "core minimum")
    require(p["rank9_core_maximum_formula"] == "K_prime-1", "core maximum")
    require(p["joint_shadow_denominator"] == 45, "joint denominator")
    require(p["premium_weights"] == [26, 18, 11, 5], "premium weights")

    rows = {str(kprime): row(kprime) for kprime in range(14, 22)}
    require(p["kernel_caps"] == {key: value["kernel"] for key, value in rows.items()}, "kernel caps")
    require(p["uniform_rank9_chart_caps"] == {key: value["chart"] for key, value in rows.items()}, "chart caps")
    require(all(value["maximizing_core"] == int(key) - 1 for key, value in rows.items()), "core maximizers")
    require(p["active_sparse_premiums"] == {key: value["premium"] for key, value in rows.items()}, "premiums")
    require(all(value["unstructured_premium"] > value["structured_premium"] for value in rows.values()), "active branches")
    require(p["total_capacities_at_record_floor"] == {key: value["total"] for key, value in rows.items()}, "total capacities")
    require(p["required_incidences_at_record_floor"] == {key: value["demand"] for key, value in rows.items()}, "demands")
    require(p["demand_capacity_gaps"] == {key: value["gap"] for key, value in rows.items()}, "gaps")
    require(all(value["gap"] > 0 and value["coefficient"] > 0 and value["raw"] > 0 for value in rows.values()), "strict rows")
    require(p["minimum_record_coefficient_cross"] == min(value["coefficient"] for value in rows.values()), "minimum coefficient")
    require(
        p["minimum_gap_row"] == 21
        and min(rows, key=lambda key: rows[key]["gap"]) == "21",
        "minimum gap row",
    )
    require(p["newly_closed_rows"] == [14, 21], "new rows")
    require(p["remaining_rank9_interval"] == [22, 15528], "remaining interval")

    wall = row(22)
    require(p["K22_method_wall"] == {
        "K_prime": 22,
        "total_capacity_at_record_floor": wall["total"],
        "required_incidence_at_record_floor": wall["demand"],
        "capacity_excess": wall["total"] - wall["demand"],
    }, "K'=22 wall")
    require(wall["gap"] < 0, "K'=22 failure")
    require("fails at K'=22" in str(data.get("nonclaim")), "nonclaim")
    return {
        "rows": len(rows),
        "minimum_gap": rows["21"]["gap"],
        "wall_excess": -wall["gap"],
    }


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("closed_K_prime_interval", [14, 20]),
        lambda item: item["parameters"].__setitem__("kernel_corank_ceiling", 8),
        lambda item: item["parameters"].__setitem__("rank9_core_maximum_formula", "K_prime-2"),
        lambda item: item["parameters"].__setitem__("joint_shadow_denominator", 46),
        lambda item: item["parameters"]["premium_weights"].__setitem__(0, 25),
        lambda item: item["parameters"]["kernel_caps"].__setitem__("20", 0),
        lambda item: item["parameters"]["uniform_rank9_chart_caps"].__setitem__("17", 0),
        lambda item: item["parameters"]["active_sparse_premiums"].__setitem__("14", 0),
        lambda item: item["parameters"]["total_capacities_at_record_floor"].__setitem__("21", 0),
        lambda item: item["parameters"]["required_incidences_at_record_floor"].__setitem__("18", 0),
        lambda item: item["parameters"]["demand_capacity_gaps"].__setitem__("16", 0),
        lambda item: item["parameters"].__setitem__("minimum_record_coefficient_cross", 0),
        lambda item: item["parameters"]["K22_method_wall"].__setitem__("capacity_excess", 0),
        lambda item: item.__setitem__("nonclaim", "K'=22 is closed"),
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
        "PASS K14..K21 joint sparse-shadow payment primary: "
        f"{result['rows']} rows, minimum gap {result['minimum_gap']}, "
        f"K22 excess {result['wall_excess']}, "
        f"{rejected}/{len(mutations)} hostile mutations"
    )


if __name__ == "__main__":
    main()
