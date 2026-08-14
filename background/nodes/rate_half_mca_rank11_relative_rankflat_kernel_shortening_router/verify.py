#!/usr/bin/env python3
"""Verify the rank-flat kernel-shortening router."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "7adb6a91110bfaceb837d610c00b278bdc95b5cd79c1599603749fc53d742cdc"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def rank_mod(matrix: list[list[int]], field: int) -> int:
    rows = [[value % field for value in row] for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
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
        data.get("schema")
        == "rate-half-mca-rank11-relative-rankflat-kernel-shortening-router-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == [
            "rate_half_mca_rank11_relative_correction_tenflat_collapse",
            "rate_half_mca_rank11_global_core_rankdrop_highcomplexity_router",
        ],
        "dependencies",
    )
    dimensions = data.get("dimensions")
    invariants = data.get("shortening_invariants")
    require(isinstance(dimensions, dict) and isinstance(invariants, dict), "sections")
    require(
        dimensions
        == {
            "component_minimum": 2,
            "component_maximum": 10,
            "evaluation_rank_minimum": 1,
            "kernel_minimum": 1,
            "kernel_maximum": 9,
            "paid_rank_maximum": 9,
            "flat_size_minimum": 3,
            "flat_size_maximum": 11,
        },
        "dimensions",
    )
    require(dimensions["kernel_maximum"] == dimensions["component_maximum"] - 1, "strict rank drop")
    require(dimensions["kernel_maximum"] <= dimensions["paid_rank_maximum"], "payment")
    require(dimensions["flat_size_minimum"] == dimensions["component_minimum"] + 1, "flat minimum")
    require(dimensions["flat_size_maximum"] == dimensions["component_maximum"] + 1, "flat maximum")
    require(
        invariants
        == {"R": 1048576, "d": 67472, "vertical_component_slope_cap": 1},
        "invariants",
    )
    require(
        data.get("routes")
        == ["VERTICAL_ONE_SLOPE", "SLOPE_DOMINATING_KERNEL_RANKDROP_PAID"],
        "routes",
    )
    toy = data.get("toy")
    require(isinstance(toy, dict) and toy.get("field") == 17, "toy")
    matrix = toy.get("evaluation_matrix")
    rank = rank_mod(matrix, 17)
    require(rank == toy.get("rank") == 2, "toy rank")
    require(len(matrix[0]) - rank == toy.get("kernel_dimension") == 1, "toy nullity")
    kernel = toy.get("kernel_vector")
    require(kernel == [0, 0, 1], "toy kernel")
    require(all(sum(a * b for a, b in zip(row, kernel)) % 17 == 0 for row in matrix), "toy vanishing")
    require("remain unpaid" in str(data.get("nonclaim")), "nonclaim")
    return {"rank": rank, "kernel": toy["kernel_dimension"], "paid": dimensions["paid_rank_maximum"]}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["dimensions"].__setitem__("kernel_maximum", 10),
        lambda item: item["dimensions"].__setitem__("paid_rank_maximum", 8),
        lambda item: item["dimensions"].__setitem__("flat_size_maximum", 10),
        lambda item: item["routes"].append("UNPAID_COMPONENT"),
        lambda item: item["toy"]["evaluation_matrix"][0].__setitem__(2, 1),
        lambda item: item["toy"].__setitem__("kernel_dimension", 2),
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
        "RATE_HALF_MCA_RANK11_RELATIVE_RANKFLAT_KERNEL_SHORTENING_ROUTER_PASS "
        f"rank={result['rank']} kernel={result['kernel']} paid_to={result['paid']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
