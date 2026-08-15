#!/usr/bin/env python3
"""Verify the exact K'=13 sparse-circuit completion payment."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "12473a9dbffe68438eb813e042d666c9ab08b25ac48bc8cdc0c5dcc2d3b4b30b"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def kernel_record_cap(kprime: int, corank: int) -> int:
    rank = 10 - corank
    shortened_k = kprime - rank
    endpoint_zero = Fraction(
        falling(1048576 + shortened_k, corank + 1),
        (67472 + shortened_k) * rising(67473, corank - 1),
    )
    endpoint_max = Fraction(
        falling(1048576 + corank, corank + 1),
        rising(67473, corank),
    )
    return int(max(endpoint_zero, endpoint_max))


def offset_capacity(petal_mass: int, total: int, offset: int) -> int:
    heavy = total // (petal_mass // 2 + 1)
    cross_floor = petal_mass * petal_mass // 4
    balanced = comb(total, 2) * (cross_floor + offset * petal_mass) // cross_floor
    collision = comb(heavy, 2) * (comb(petal_mass - 1, 2) + offset * petal_mass)
    center = (
        (petal_mass - 2) * total + 2 * heavy * offset * petal_mass
    ) // (2 * (petal_mass - 2))
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


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-k13-sparse-circuit-completion-payment-v1",
        "schema",
    )
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_dense_locator_component_incidence_dichotomy",
        "rate_half_mca_rank11_dense_root_highspan_saturation",
        "rate_half_mca_rank11_kernel_rankstratified_capacity_cut",
        "rate_half_mca_rank11_rank9_residual_petal_capacity_cut",
        "rate_half_mca_weighted_split_pencil_core_offset_cap",
        "rate_half_mca_codimension_three_sparse_circuit_completion_cap",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    k, n, m = int(p["K_prime"]), int(p["n_prime"]), int(p["m_prime"])
    require(k == 13 and (n, m) == (1048576 + k, 67472 + k), "row")
    require((p["correction_dimension"], p["ambient_RS_dimension"]) == (10, 13), "dimensions")

    coranks = list(p["kernel_coranks"])
    require(coranks == [1, 2], "kernel coranks")
    record_caps = [kernel_record_cap(k, corank) for corank in coranks]
    extensions = [comb(k - 10, corank + 1) for corank in coranks]
    terms = [
        comb(n, 10 - corank) * record_cap * extension
        for corank, record_cap, extension in zip(coranks, record_caps, extensions)
    ]
    require(p["kernel_record_caps"] == record_caps == [16295594, 253241283], "kernel record caps")
    require(p["kernel_extension_factors"] == extensions == [3, 1], "kernel extensions")
    require(p["kernel_incidence_terms"] == terms, "kernel terms")
    kernel = sum(terms)
    require(p["kernel_incidence_cap"] == kernel, "kernel capacity")

    require(p["rank9_core_sizes"] == [9, 10, 11, 12], "core sizes")
    caps = [offset_capacity(m - j, n - j, j - 9) for j in p["rank9_core_sizes"]]
    require(p["rank9_core_caps"] == caps, "core caps")
    chart = max(caps)
    require(p["uniform_rank9_chart_cap"] == chart, "chart cap")
    global_marks = comb(n, 9) * chart
    require(p["global_rank9_mark_capacity"] == global_marks, "global marks")
    require(p["high_circuit_threshold"] == 6, "high threshold")
    shadow_floor = min(55 - comb(11 - support, 2) for support in range(6, 12))
    require(p["minimum_high_circuit_rank9_shadows"] == shadow_floor == 45, "shadow floor")
    high = global_marks // shadow_floor
    require(p["high_circuit_incidence_cap"] == high, "high capacity")

    require(p["low_circuit_support_ceiling"] == 5, "low ceiling")
    low_per_record = int(p["low_circuit_per_record_cap"])
    require(low_per_record == 99254447944649683780146155758753837527116020, "low per record")
    records = int(p["residual_record_floor"])
    low = records * low_per_record
    require(p["low_circuit_incidence_cap_at_record_floor"] == low, "low capacity")

    total = kernel + high + low
    density_num = int(p["component_density_numerator"])
    density_den = int(p["component_density_denominator"])
    require((density_num, density_den) == (990810934, 10**9), "density")
    numerator = density_num * records * comb(m, 11)
    demand = ceil_div(numerator, density_den)
    raw = numerator - density_den * total
    coefficient = density_num * comb(m, 11) - density_den * low_per_record
    require(p["total_capacity_at_record_floor"] == total, "total capacity")
    require(p["required_incidence_at_record_floor"] == demand, "demand")
    require(p["demand_capacity_gap"] == demand - total > 0, "gap")
    require(p["raw_demand_capacity_cross"] == raw > 0, "raw crossing")
    require(p["record_coefficient_cross"] == coefficient > 0, "record coefficient")
    require(p["newly_closed_rows"] == [13, 13], "closed row")
    require(p["remaining_rank9_interval"] == [14, 15528], "remaining interval")
    require("No row K'>=14" in str(data.get("nonclaim")), "nonclaim")
    return {
        "kernel": kernel,
        "chart": chart,
        "high": high,
        "low": low,
        "total": total,
        "demand": demand,
        "gap": demand - total,
    }


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("K_prime", 14),
        lambda item: item["parameters"].__setitem__("kernel_coranks", [1]),
        lambda item: item["parameters"]["kernel_record_caps"].__setitem__(1, 0),
        lambda item: item["parameters"].__setitem__("kernel_extension_factors", [3, 0]),
        lambda item: item["parameters"].__setitem__("kernel_incidence_cap", result["kernel"] - 1),
        lambda item: item["parameters"].__setitem__("rank9_core_sizes", [9, 10, 11]),
        lambda item: item["parameters"].__setitem__("uniform_rank9_chart_cap", result["chart"] - 1),
        lambda item: item["parameters"].__setitem__("minimum_high_circuit_rank9_shadows", 44),
        lambda item: item["parameters"].__setitem__("low_circuit_per_record_cap", 0),
        lambda item: item["parameters"].__setitem__("total_capacity_at_record_floor", result["total"] - 1),
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
        "PASS K13 sparse-circuit completion payment primary: "
        f"kernel {result['kernel']}, chart {result['chart']}, "
        f"demand {result['demand']}, capacity {result['total']}, "
        f"gap {result['gap']}, {rejected}/{len(mutations)} hostile mutations"
    )


if __name__ == "__main__":
    main()
