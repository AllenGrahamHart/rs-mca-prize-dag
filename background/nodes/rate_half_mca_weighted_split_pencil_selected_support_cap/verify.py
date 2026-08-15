#!/usr/bin/env python3
"""Verify the weighted selected-support split-pencil capacity theorem."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "414e1f902ec6a53abdb7ea789061c6147af9953c841440b963d71d6dfb7be434"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def capacity(a: int, total: int) -> tuple[int, int, int, int, int]:
    heavy_threshold = a // 2 + 1
    heavy_count = total // heavy_threshold
    clean = (a - 2) * total * total // 8
    balanced = comb(total, 2)
    collision = comb(heavy_count, 2) * comb(a - 1, 2)
    return clean + balanced + collision, clean, balanced, collision, heavy_count


def partitions(total: int, ceiling: int | None = None) -> list[tuple[int, ...]]:
    ceiling = total if ceiling is None else min(ceiling, total)
    out: list[tuple[int, ...]] = []

    def visit(remaining: int, maximum: int, prefix: tuple[int, ...]) -> None:
        if remaining == 0:
            out.append(prefix)
            return
        for value in range(min(maximum, remaining), 0, -1):
            visit(remaining - value, value, prefix + (value,))

    visit(total, ceiling, ())
    return out


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-weighted-split-pencil-selected-support-cap-v1",
        "schema",
    )
    require(data.get("dependencies") == [], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["minimum_A"] == 3, "minimum A")
    require(p["owner_weight_ceiling_formula"] == "A-1", "owner ceiling")
    require(p["selected_line_mass_formula"] == "sum_p x_Lp=A", "line mass")
    require(p["line_charge_formula"] == "sum_p C(x_Lp,2)", "line charge")
    require(p["heavy_threshold_formula"] == "floor(A/2)+1", "heavy threshold")
    require(
        p["total_cap_formula"]
        == "floor((A-2)*S^2/8)+C(S,2)+C(h,2)*C(A-1,2)",
        "total formula",
    )
    require(
        p["clean_inequality_slack_factorization"]
        == "(d-1)*(d+s)*(s-1)",
        "factorization",
    )

    specialization = p["specialization"]
    require(isinstance(specialization, dict), "specialization")
    a, total = int(specialization["A"]), int(specialization["S"])
    cap, clean, balanced, collision, heavy_count = capacity(a, total)
    require(specialization["heavy_threshold"] == a // 2 + 1 == 33737, "threshold")
    require(specialization["heavy_count"] == heavy_count == 31, "heavy count")
    require(specialization["clean_dominant_cap"] == clean, "clean cap")
    require(specialization["balanced_cap"] == balanced, "balanced cap")
    require(specialization["heavy_collision_cap"] == collision, "collision cap")
    require(specialization["total_cap"] == cap == 9274769506943785, "total cap")

    clean_checks = 0
    for size in range(a // 2 + 1, a):
        deficit = a - size
        line_charge = comb(size, 2) + comb(deficit, 2)
        slack = deficit * size * (a - 2) - 2 * line_charge
        require(slack == (deficit - 1) * a * (size - 1), f"clean slack {size}")
        require(slack >= 0, f"clean inequality {size}")
        clean_checks += 1

    partition_checks = 0
    balanced_checks = 0
    for small_a in range(3, 14):
        line_cap = comb(small_a - 1, 2)
        for part in partitions(small_a, small_a - 1):
            charge = sum(comb(value, 2) for value in part)
            cross = comb(small_a, 2) - charge
            require(charge <= line_cap, f"line convexity {small_a} {part}")
            if 2 * max(part) <= small_a:
                require(charge <= cross, f"balanced charge {small_a} {part}")
                balanced_checks += 1
            partition_checks += 1

    require("not claimed sharp" in str(data.get("nonclaim")), "nonclaim")
    return {
        "clean_checks": clean_checks,
        "partition_checks": partition_checks,
        "balanced_checks": balanced_checks,
    }


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("minimum_A", 2),
        lambda item: item["parameters"].__setitem__("owner_weight_ceiling_formula", "A"),
        lambda item: item["parameters"].__setitem__("selected_line_mass_formula", "sum_p x_Lp>=A"),
        lambda item: item["parameters"].__setitem__("heavy_threshold_formula", "floor(A/2)"),
        lambda item: item["parameters"]["specialization"].__setitem__("heavy_count", 32),
        lambda item: item["parameters"]["specialization"].__setitem__("balanced_cap", 0),
        lambda item: item["parameters"]["specialization"].__setitem__("total_cap", 9274769506943784),
        lambda item: item.__setitem__("nonclaim", "sharp for duplicate lines"),
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
        "PASS weighted split-pencil primary: "
        f"{result['clean_checks']} clean sizes, "
        f"{result['partition_checks']} partitions, "
        f"{result['balanced_checks']} balanced, "
        f"{rejected}/{len(mutations)} hostile mutations"
    )


if __name__ == "__main__":
    main()
