#!/usr/bin/env python3
"""Verify the degree-2048 symmetric-configuration ledger."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "ace7ff76890b4ec1234e259e8c2c5e6e23cb443f82f610582d0be0fe06a70264"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-plane218-power2048-symmetric-configuration-ledger-v1",
        "schema",
    )
    v, b, k = data.get("selected_points"), data.get("full_lines"), data.get("line_size")
    require((v, b, k, data.get("point_degree")) == (218, 218, 15, 15), "configuration pins")
    require((data.get("direction_subgroup_order"), data.get("distinct_directions")) ==
            (1024, 218), "direction pins")
    leave_degree = v - 1 - k * (k - 1)
    leave_edges = v * leave_degree // 2
    require(data.get("leave_degree") == leave_degree == 7, "leave degree")
    require(data.get("leave_edges") == leave_edges == 763, "leave edges")
    require(data.get("gram_identity") == "14I+J-L", "Gram identity")
    require(14 - leave_degree == 7 and 14 + v - leave_degree == 225,
            "positive Gram spectrum")
    require(data.get("incidence_matrix_rank_over_reals") == v, "real rank")

    e = data.get("quotient_fiber_size")
    full = data.get("full_coordinate_floor")
    require((e, full) == (2048, 446392), "fiber pins")
    defect = b * e - full
    require(data.get("aggregate_fiber_defect_ceiling") == defect == 72, "defect")
    saturated = b - defect
    require(data.get("saturated_fiber_floor") == saturated == 146, "saturated fibers")
    saturated_at_point = ceil_div(saturated * k, v)
    require(data.get("saturated_lines_at_one_point_floor") ==
            saturated_at_point == 11, "saturated point")
    incident_defect = (k * defect) // v
    require(data.get("incident_defect_at_one_point_ceiling") ==
            incident_defect == 4, "point defect")
    core_contribution = k * e - incident_defect
    require(data.get("full_core_coordinates_at_one_point_floor") ==
            core_contribution == 30716, "core contribution")
    require("does not exclude" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(
        nodes.get("rate_half_mca_rank11_pair_pencil_plane218_pure_power_router", {}).get("status")
        == "PROVED",
        "dependency",
    )
    return {"leave": leave_degree, "defect": defect, "saturated": saturated,
            "core": core_contribution}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("point_degree", 14),
        lambda item: item.__setitem__("distinct_directions", 217),
        lambda item: item.__setitem__("leave_degree", 8),
        lambda item: item.__setitem__("leave_edges", 762),
        lambda item: item.__setitem__("incidence_matrix_rank_over_reals", 217),
        lambda item: item.__setitem__("aggregate_fiber_defect_ceiling", 73),
        lambda item: item.__setitem__("saturated_fiber_floor", 145),
        lambda item: item.__setitem__("full_core_coordinates_at_one_point_floor", 30715),
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
        print(f"PLANE218_POWER2048_CONFIG_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "PLANE218_POWER2048_CONFIG_PASS "
        f"leave={checked['leave']} defect={checked['defect']} "
        f"saturated={checked['saturated']} core={checked['core']}"
    )


if __name__ == "__main__":
    main()
