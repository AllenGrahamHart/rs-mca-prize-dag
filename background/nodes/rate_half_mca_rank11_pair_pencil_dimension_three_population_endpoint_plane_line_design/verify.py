#!/usr/bin/env python3
"""Verify the q=3170 saturated plane-line endpoint design."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "aa8c63b148f1fc666e055dd05357ef1a0a9b492c6d0bbbbcd8a70cb666f24406"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def row(kprime: int, q: int, plane: int, local_floor: int,
        full_constant: int, full_slope: int) -> tuple[int, int, int, int]:
    full = full_constant + full_slope * kprime
    planes = ceil_div(full, kprime - local_floor)
    incidence = plane * planes
    average, _ = divmod(incidence, q)
    lower = average * incidence - comb(average + 1, 2) * q
    capacity = 15 * comb(planes, 2)
    saturated = comb(planes, 2) - (capacity - lower)
    return full, planes, capacity - lower, saturated


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") ==
            "rate-half-mca-rank11-dimension-three-population-endpoint-plane-line-v1",
            "schema")
    q = data.get("type_population")
    kmin = data.get("residual_dimension_floor")
    kmax = data.get("residual_dimension_ceiling")
    plane = data.get("plane_occupancy")
    line = data.get("line_occupancy")
    local_floor = data.get("plane_local_residual_dimension_floor")
    full_constant = data.get("full_owner_floor_constant")
    full_slope = data.get("full_owner_floor_slope")
    require((q, kmin, kmax, plane, line, local_floor, full_constant, full_slope) ==
            (3170, 4960, 4982, 218, 15, 2044, -13661092, 2953),
            "input pins")

    rows = [row(k, q, plane, local_floor, full_constant, full_slope)
            for k in range(kmin, kmax + 1)]
    plane_counts = [item[1] for item in rows]
    saturated_counts = [item[3] for item in rows]
    require(min(plane_counts) == data["distinct_plane_floor"] == 339,
            "plane floor")
    require(max(plane_counts) == data["distinct_plane_ceiling_on_rows"] == 358,
            "plane ceiling")
    require(min(saturated_counts) == data["minimum_saturated_plane_pairs"] ==
            22752, "saturated pair floor")
    require(rows[0] == (985788, 339, 34539, 22752), "first row")
    require(rows[-1] == (1050754, 358, 36489, 27414), "last row")

    line_plane_cap = (q - line) // (plane - line)
    require(data["planes_per_saturated_line_ceiling"] == line_plane_cap == 15,
            "planes per line")
    pair_capacity = comb(line_plane_cap, 2)
    require(data["saturated_line_pair_capacity"] == pair_capacity == 105,
            "line pair capacity")
    line_floor = ceil_div(min(saturated_counts), pair_capacity)
    require(data["distinct_saturated_line_floor"] == line_floor == 217,
            "line floor")

    core_floor = ceil_div(line * 1116046 - 2097152, line - 1)
    require(data["saturated_line_common_core_floor"] == core_floor == 1045967,
            "line core")
    local_ceiling = 1048576 - core_floor
    require(data["saturated_line_local_dimension_ceiling"] ==
            local_ceiling == 2609, "line local dimension")
    recurrence = kmin - local_ceiling
    require(data["saturated_line_residual_recurrence_floor"] ==
            recurrence == 2351, "line recurrence")
    require("not paid" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for parent in (
        "rate_half_mca_rank11_pair_pencil_dimension_three_type_population_ceiling",
        "rate_half_mca_rank11_pair_pencil_plane218_projective_direction_bank",
    ):
        require(nodes.get(parent, {}).get("status") == "PROVED", f"dependency {parent}")
    return {"planes": min(plane_counts), "pairs": min(saturated_counts),
            "lines": line_floor, "recurrence": recurrence}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("type_population", 3169),
        lambda item: item.__setitem__("plane_local_residual_dimension_floor", 2043),
        lambda item: item.__setitem__("distinct_plane_floor", 338),
        lambda item: item.__setitem__("minimum_saturated_plane_pairs", 22751),
        lambda item: item.__setitem__("planes_per_saturated_line_ceiling", 16),
        lambda item: item.__setitem__("distinct_saturated_line_floor", 216),
        lambda item: item.__setitem__("saturated_line_common_core_floor", 1045966),
        lambda item: item.__setitem__("saturated_line_residual_recurrence_floor", 2350),
    )
    caught = 0
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutations")
    return caught


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256,
            "contract hash")
    data = json.loads(CONTRACT.read_text())
    checked = validate(data)
    if args.tamper_selftest:
        print(f"RANK11_D3_ENDPOINT_DESIGN_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "RANK11_D3_ENDPOINT_DESIGN_PASS "
        f"planes={checked['planes']} pairs={checked['pairs']} "
        f"lines={checked['lines']} recurrence={checked['recurrence']}"
    )


if __name__ == "__main__":
    main()
