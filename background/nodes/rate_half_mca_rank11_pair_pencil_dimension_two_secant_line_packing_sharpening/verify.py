#!/usr/bin/env python3
"""Verify the dimension-two secant-line packing sharpening."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "6ab24a38ea900cd9eac807bc6d49a480751c9125ffcf6ab0abd186fd347f9b59"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank11-pair-pencil-dimension-two-secant-line-packing-sharpening-v1",
        "schema",
    )
    n = data.get("n")
    q = data.get("selected_points")
    cap = data.get("line_occupancy_cap")
    degree = math.ceil((q - 1) / (cap - 1))
    incidence = q * degree
    ordered = q * (q - 1)
    lines = math.ceil(incidence * incidence / (ordered + incidence))
    roots = data.get("direction_intersection_floor")
    core = math.ceil((lines * roots - n) / (lines - 1))
    petal = roots - core
    slack = (n - core) - lines * petal
    require((n, q, cap) == (2097152, 520, 15), "input pins")
    require(data.get("lines_per_point_floor") == degree == 38, "point degree")
    require(data.get("point_line_incidence_floor") == incidence == 19760, "incidence")
    require(data.get("ordered_pair_count") == ordered == 269880, "ordered pairs")
    require(data.get("affine_secant_line_floor") == lines == 1349, "line floor")
    require(roots == 134940, "intersection floor")
    require(data.get("common_core_floor") == core == 133485, "core floor")
    require(data.get("residual_petal_floor") == petal == 1455, "petal floor")
    require(data.get("minimum_floor_slack") == slack == 872, "slack")
    require("not paid" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_pair_pencil_affine_line_cap_direction_router",
        "rate_half_mca_rank11_pair_pencil_dimension_two_common_core_shortening",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"lines": lines, "core": core, "petal": petal, "slack": slack}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("selected_points", 519),
        lambda item: item.__setitem__("line_occupancy_cap", 16),
        lambda item: item.__setitem__("lines_per_point_floor", 37),
        lambda item: item.__setitem__("point_line_incidence_floor", 19759),
        lambda item: item.__setitem__("ordered_pair_count", 269879),
        lambda item: item.__setitem__("affine_secant_line_floor", 1348),
        lambda item: item.__setitem__("common_core_floor", 133484),
        lambda item: item.__setitem__("minimum_floor_slack", 871),
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
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    checked = validate(data)
    if args.tamper_selftest:
        print(f"PAIR_PENCIL_DIM2_SECANT_PACKING_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "PAIR_PENCIL_DIM2_SECANT_PACKING_PASS "
        f"lines={checked['lines']} core={checked['core']} "
        f"petal={checked['petal']} slack={checked['slack']}"
    )


if __name__ == "__main__":
    main()
