#!/usr/bin/env python3
"""Verify the pure-power router for the 218-plane endpoint."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "8726a61ae156eb16e99b079545303aa1c43cdadb5b47c9a62122618a6f5fa17a"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def validate(data: object) -> dict[str, object]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-pair-pencil-plane218-pure-power-router-v1",
        "schema",
    )
    N = data.get("official_domain_order")
    kmin, kmax = data.get("shortened_K_floor"), data.get("shortened_K_ceiling")
    fconst = data.get("full_coordinate_floor_constant")
    fslope = data.get("full_coordinate_floor_slope")
    rmax = data.get("direction_ceiling")
    require((N, kmin, kmax, fconst, fslope, rmax) == (2**21, 2044, 5025, 28396, 204, 218), "pins")
    require(data.get("aggregate_degree_deficit_ceiling") == 41736, "parent deficit")

    feasible: dict[int, list[int]] = {}
    for exponent in range(22):
        e = 1 << exponent
        rows = [
            k for k in range(kmin, kmax + 1)
            if e <= k - 1 and fconst + fslope * k <= rmax * e
        ]
        if rows:
            feasible[e] = rows
    require(list(feasible) == data.get("surviving_degrees") == [2048, 4096], "degrees")

    cases = data.get("cases")
    require(isinstance(cases, dict), "cases")
    rows_2048 = feasible[2048]
    case_2048 = cases.get("2048", {})
    require((min(rows_2048), max(rows_2048), len(rows_2048)) == (2049, 2049, 1), "2048 rows")
    floor_2048 = fconst + fslope * rows_2048[0]
    direction_2048 = ceil_div(floor_2048, 2048)
    missing_2048 = rmax * 2048 - floor_2048
    require(
        case_2048
        == {
            "shortened_K_floor": 2049,
            "shortened_K_ceiling": 2049,
            "direction_floor": 218,
            "missing_slot_ceiling": 72,
        },
        "2048 case",
    )
    require((direction_2048, missing_2048) == (218, 72), "2048 arithmetic")

    rows_4096 = feasible[4096]
    case_4096 = cases.get("4096", {})
    direction_4096 = min(ceil_div(fconst + fslope * k, 4096) for k in rows_4096)
    missing_4096 = max(rmax * 4096 - (fconst + fslope * k) for k in rows_4096)
    require((min(rows_4096), max(rows_4096), len(rows_4096)) == (4097, 4237, 141), "4096 rows")
    require(
        case_4096
        == {
            "shortened_K_floor": 4097,
            "shortened_K_ceiling": 4237,
            "direction_floor": 211,
            "duplicate_line_ceiling": 7,
            "missing_slot_ceiling": 28744,
        },
        "4096 case",
    )
    require((direction_4096, rmax - direction_4096, missing_4096) == (211, 7, 28744), "4096 arithmetic")
    require("does not prove" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(
        nodes.get("rate_half_mca_rank11_pair_pencil_plane218_projective_direction_bank", {}).get("status")
        == "PROVED",
        "dependency",
    )
    return {"degrees": list(feasible), "rows_2048": len(rows_2048), "rows_4096": len(rows_4096)}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("shortened_K_floor", 2043),
        lambda item: item.__setitem__("shortened_K_ceiling", 5024),
        lambda item: item.__setitem__("direction_ceiling", 219),
        lambda item: item.__setitem__("surviving_degrees", [1024, 2048, 4096]),
        lambda item: item["cases"]["2048"].__setitem__("missing_slot_ceiling", 73),
        lambda item: item["cases"]["4096"].__setitem__("shortened_K_ceiling", 4238),
        lambda item: item["cases"]["4096"].__setitem__("direction_floor", 210),
        lambda item: item["cases"]["4096"].__setitem__("missing_slot_ceiling", 28743),
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
        print(f"PAIR_PENCIL_PLANE218_POWER_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "PAIR_PENCIL_PLANE218_POWER_PASS "
        f"degrees={checked['degrees']} rows=({checked['rows_2048']},{checked['rows_4096']})"
    )


if __name__ == "__main__":
    main()
