#!/usr/bin/env python3
"""Verify the component nine-subset target router."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "6bcbfc8f5ae87e892898137660af54014a48c57f5d55295327923af6ab5f6e4b"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def rank_mod(rows: list[list[int]], field: int) -> int:
    matrix = [[value % field for value in row] for row in rows]
    rank = 0
    for column in range(len(matrix[0]) if matrix else 0):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], -1, field)
        matrix[rank] = [(inverse * value) % field for value in matrix[rank]]
        for i, row in enumerate(matrix):
            if i == rank or row[column] == 0:
                continue
            factor = row[column]
            matrix[i] = [(a - factor * b) % field for a, b in zip(row, matrix[rank])]
        rank += 1
    return rank


def toy_rank8_errors() -> int:
    # U=<e1,e2>, with one independent received direction e3.
    deviations = ([0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 0])
    errors = []
    for slope, deviation in enumerate(deviations):
        errors.append([
            -deviation[0],
            -deviation[1],
            slope - deviation[2],
        ])
    differences = [
        [(value - errors[0][i]) % 101 for i, value in enumerate(error)]
        for error in errors[1:]
    ]
    return rank_mod(differences, 101)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-component-ninesubset-target-router-v1",
        "schema",
    )
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_component_ninesubset_lane_concentrator",
        "rate_half_mca_rank11_rank9_ninecell_paircore_extension",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["correction_dimension"], p["component_tuple_size"], p["fixed_selector_size"]) == (10, 11, 9), "dimensions")
    require(p["fixed_selector_population_floor"] == 2578110, "population")
    require(p["rank9_low_common_core_plane_cap"] == 1434405, "plane cap")
    excess = p["fixed_selector_population_floor"] - p["rank9_low_common_core_plane_cap"]
    require(excess == p["population_excess_over_plane_cap"] == 1143705, "excess")
    require(p["rank9_shared_pair_core_floor"] == 134944, "shared core")
    require((p["rank8_kernel_dimension"], p["rank8_error_rank_ceiling"]) == (2, 3), "rank8")
    require(p["kernel_lane_ambient_kernel_dimension_floor"] == 1, "kernel lane")
    require(toy_rank8_errors() == 3, "sharp rank-three toy")
    require(data.get("routes") == [
        "FIXED_KERNEL_NINESUBSET_CHART",
        "RANK9_SHARED_PAIR_CORE_PLANE",
        "RANK8_OWNER_FLAT_ERROR_RANK_AT_MOST_3",
    ], "routes")
    require("not a complete-lane selector" in str(data.get("nonclaim")), "nonclaim")
    return {"population": p["fixed_selector_population_floor"], "excess": excess}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("fixed_selector_size", 10),
        lambda item: item["parameters"].__setitem__("fixed_selector_population_floor", 1434405),
        lambda item: item["parameters"].__setitem__("population_excess_over_plane_cap", 1143704),
        lambda item: item["parameters"].__setitem__("rank9_shared_pair_core_floor", 134943),
        lambda item: item["parameters"].__setitem__("rank8_error_rank_ceiling", 4),
        lambda item: item["routes"].pop(),
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
        "RATE_HALF_MCA_RANK11_COMPONENT_NINESUBSET_TARGET_ROUTER_PASS "
        f"population={result['population']} excess={result['excess']} "
        f"rank8_toy=3 controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
