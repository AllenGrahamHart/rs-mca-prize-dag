#!/usr/bin/env python3
"""Verify the rank-eleven relative correction ten-flat collapse."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "803cc5f5f922ffae6fe3b50439edf3baf73b1f4dd7e556e96e5361a8b22dcbec"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def rank_mod(vectors: list[list[int]], field: int) -> int:
    rows = [[value % field for value in vector] for vector in vectors]
    if not rows:
        return 0
    rank = 0
    columns = len(rows[0])
    for column in range(columns):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, field)
        rows[rank] = [(inverse * value) % field for value in rows[rank]]
        for i in range(len(rows)):
            if i == rank or not rows[i][column]:
                continue
            scale = rows[i][column]
            rows[i] = [(a - scale * b) % field for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank11-relative-correction-tenflat-collapse-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == [
            "rate_half_mca_rank11_global_core_rankdrop_highcomplexity_router",
            "rate_half_mca_rank11_relative_core_interpolant_ray_payment",
            "rate_half_mca_rank11_relative_correction_space_router",
        ],
        "dependencies",
    )
    dimensions = data.get("dimensions")
    require(isinstance(dimensions, dict), "dimensions")
    require(
        dimensions
        == {
            "deviation_space": 10,
            "correction_minimum_after_core_ray_payment": 2,
            "correction_maximum": 10,
            "proper_paid_through": 11,
            "clone_tolerant_nonabsorbing_paid_through": 9,
        },
        "dimension pins",
    )
    require(dimensions["correction_maximum"] < dimensions["proper_paid_through"], "proper collapse")
    require(
        dimensions["clone_tolerant_nonabsorbing_paid_through"]
        == dimensions["correction_maximum"] - 1,
        "absorption split",
    )
    require(
        data.get("containments")
        == [
            "all_explanation_deviations_in_V",
            "all_core_interpolant_high_coefficients_in_V",
            "all_corrections_in_V",
            "dimension_ten_correction_span_equals_V",
        ],
        "containments",
    )
    require(
        data.get("routes")
        == ["RANK_FLAT_ABSORB_HIGH", "POLYNOMIAL_CLONE_ABSORB_HIGH"],
        "routes",
    )
    toy = data.get("toy")
    require(isinstance(toy, dict) and toy.get("field") == 17, "toy")
    basis = toy.get("deviation_basis")
    coefficients = toy.get("interpolant_coefficients")
    deviation = toy.get("explanation_deviation")
    correction = toy.get("correction")
    require(toy.get("ambient_dimension") == 4, "ambient")
    require(rank_mod(basis, 17) == 3, "basis rank")
    require(all(rank_mod(basis + [vector], 17) == 3 for vector in coefficients), "coefficient span")
    require(rank_mod(basis + [deviation], 17) == 3, "deviation span")
    computed = [(a - b) % 17 for a, b in zip(deviation, coefficients[0])]
    require(computed == correction, "correction value")
    require(rank_mod(basis + [correction], 17) == 3, "correction span")
    require("remain unpaid" in str(data.get("nonclaim")), "nonclaim")
    return {"minimum": dimensions["correction_minimum_after_core_ray_payment"], "maximum": dimensions["correction_maximum"]}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["dimensions"].__setitem__("correction_maximum", 12),
        lambda item: item["dimensions"].__setitem__("correction_minimum_after_core_ray_payment", 1),
        lambda item: item["containments"].pop(),
        lambda item: item["routes"].append("DIM_GE_12"),
        lambda item: item["toy"]["interpolant_coefficients"][0].__setitem__(3, 1),
        lambda item: item["toy"].__setitem__("correction", [0, 0, 0, 0]),
    )
    controls = []
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_RELATIVE_CORRECTION_TENFLAT_COLLAPSE_PASS "
        f"dimension={result['minimum']}..{result['maximum']} routes=2 "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
