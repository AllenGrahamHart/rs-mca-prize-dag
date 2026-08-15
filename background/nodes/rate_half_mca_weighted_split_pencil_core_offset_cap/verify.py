#!/usr/bin/env python3
"""Verify the weighted split-pencil common-core-offset theorem."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "c16ddeb5b7e492a6ababe1f558ba7f7b049ac4f1116149191d7065dbed163159"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def capacity(petal_mass: int, total: int, offset: int) -> dict[str, int]:
    heavy = total // (petal_mass // 2 + 1)
    cross_floor = petal_mass * petal_mass // 4
    balanced = comb(total, 2) * (cross_floor + offset * petal_mass) // cross_floor
    collision = comb(heavy, 2) * (comb(petal_mass - 1, 2) + offset * petal_mass)
    vertex_num = (petal_mass - 2) * total + 2 * heavy * offset * petal_mass
    vertex_den = 2 * (petal_mass - 2)
    center = vertex_num // vertex_den
    candidates = range(max(0, center - 3), min(total, center + 3) + 1)
    clean, light = max(
        (
            ell
            * ((petal_mass - 2) * (total - ell) + 2 * heavy * offset * petal_mass)
            // 2,
            ell,
        )
        for ell in candidates
    )
    return {
        "heavy_count": heavy,
        "balanced_cross_floor": cross_floor,
        "maximizing_light_mass": light,
        "clean_cap": clean,
        "balanced_cap": balanced,
        "collision_cap": collision,
        "total_cap": clean + balanced + collision,
    }


def partitions(total: int, ceiling: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []

    def visit(remaining: int, maximum: int, prefix: tuple[int, ...]) -> None:
        if remaining == 0:
            out.append(prefix)
            return
        for value in range(min(maximum, remaining), 0, -1):
            visit(remaining - value, value, prefix + (value,))

    visit(total, min(total, ceiling), ())
    return out


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-weighted-split-pencil-core-offset-cap-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_weighted_split_pencil_selected_support_cap"],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["minimum_P"] == 3 and p["minimum_r"] == 0, "parameter minima")
    require(p["owner_weight_ceiling_formula"] == "P-1", "owner ceiling")
    require(p["selected_line_mass_formula"] == "sum_p x_Lp=P", "line mass")
    require(p["line_charge_formula"] == "sum_p C(x_Lp,2)+rP", "line charge")
    require(p["balanced_cross_floor_formula"] == "floor(P^2/4)", "cross floor")
    require(
        p["clean_inequality_slack_factorization"] == "(d-1)*(d+s)*(s-1)",
        "clean factorization",
    )

    specializations = p["K11_specializations"]
    require(isinstance(specializations, list) and len(specializations) == 2, "specializations")
    for expected in specializations:
        actual = capacity(int(expected["P"]), int(expected["S"]), int(expected["r"]))
        require(expected["j"] in (9, 10), "core size")
        for key, value in actual.items():
            require(expected[key] == value, f"specialization {expected['j']} {key}")
    require(specializations[0]["total_cap"] == 9274924665987729, "j9 cap")
    require(specializations[1]["total_cap"] == 9275866238180030, "j10 cap")

    partition_checks = 0
    balanced_checks = 0
    for petal_mass in range(3, 15):
        cross_floor = petal_mass * petal_mass // 4
        for part in partitions(petal_mass, petal_mass - 1):
            charge = sum(comb(value, 2) for value in part)
            cross = comb(petal_mass, 2) - charge
            require(charge <= comb(petal_mass - 1, 2), "line convexity")
            if 2 * max(part) <= petal_mass:
                require(charge <= cross, "balanced charge")
                require(cross >= cross_floor, "balanced line-count floor")
                balanced_checks += 1
            partition_checks += 1

    clean_checks = 0
    for petal_mass in range(3, 80):
        for size in range(petal_mass // 2 + 1, petal_mass):
            deficit = petal_mass - size
            charge_twice = size * (size - 1) + deficit * (deficit - 1)
            slack = deficit * size * (petal_mass - 2) - charge_twice
            require(
                slack == (deficit - 1) * petal_mass * (size - 1) >= 0,
                "clean slack",
            )
            clean_checks += 1

    require("not claimed sharp" in str(data.get("nonclaim")), "nonclaim")
    return {
        "partition_checks": partition_checks,
        "balanced_checks": balanced_checks,
        "clean_checks": clean_checks,
    }


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("minimum_P", 2),
        lambda item: item["parameters"].__setitem__("owner_weight_ceiling_formula", "P"),
        lambda item: item["parameters"].__setitem__("line_charge_formula", "sum_p C(x_Lp,2)"),
        lambda item: item["parameters"].__setitem__("balanced_cross_floor_formula", "ceil(P^2/4)"),
        lambda item: item["parameters"]["K11_specializations"][0].__setitem__("total_cap", 0),
        lambda item: item["parameters"]["K11_specializations"][1].__setitem__("balanced_cap", 0),
        lambda item: item["parameters"]["K11_specializations"][1].__setitem__("maximizing_light_mass", 524319),
        lambda item: item.__setitem__("nonclaim", "sharp"),
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
        "PASS split-pencil core-offset primary: "
        f"{result['partition_checks']} partitions, "
        f"{result['balanced_checks']} balanced, "
        f"{result['clean_checks']} clean, "
        f"{rejected}/{len(mutations)} hostile mutations"
    )


if __name__ == "__main__":
    main()
