#!/usr/bin/env python3
"""Verify the scalar-dimension-four heavy affine-three router."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "c5306e2db547697b6038be03a20b1535da279d60b0ff35cc3d181ae4c42198df"


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
        == "rate-half-mca-rank11-pair-pencil-dimension-four-heavy-affine-three-router-v1",
        "schema",
    )
    n, m, K = data.get("n"), data.get("m"), data.get("K")
    q = data.get("selected_types")
    s = data.get("pair_core_size")
    plane = data.get("affine_plane_cap")
    require((n, m, K, q, s, plane) == (2097152, 1116048, 1048576, 520, m - 2, 233), "pins")
    core = ceil_div(q * s - plane * n, q - plane)
    require(data.get("common_core_threshold") == core == 319539, "core threshold")
    heavy = plane + 1
    require(data.get("heavy_fiber_type_floor") == heavy == 234, "heavy type floor")
    record_floor = data.get("selected_type_record_floor")
    require(record_floor == 29, "record floor")
    records = heavy * record_floor
    require(data.get("heavy_fiber_record_floor") == records == 6786, "heavy records")
    require(data.get("preserved_excess") == m - K == 67472, "excess")
    nonclaim = str(data.get("nonclaim")).lower()
    require("neither" in nonclaim and "paid" in nonclaim, "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_pair_pencil_dimension_three_common_core_shortening",
        "rate_half_mca_rank11_quadratic_quotient_population_router",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"core": core, "heavy": heavy, "records": records}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("selected_types", 519),
        lambda item: item.__setitem__("pair_core_size", 1116045),
        lambda item: item.__setitem__("affine_plane_cap", 234),
        lambda item: item.__setitem__("common_core_threshold", 319538),
        lambda item: item.__setitem__("heavy_fiber_type_floor", 233),
        lambda item: item.__setitem__("selected_type_record_floor", 28),
        lambda item: item.__setitem__("heavy_fiber_record_floor", 6785),
        lambda item: item.__setitem__("preserved_excess", 67471),
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
        print(f"PAIR_PENCIL_DIM4_HEAVY_FIBER_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "PAIR_PENCIL_DIM4_HEAVY_FIBER_PASS "
        f"core={checked['core']} heavy={checked['heavy']} records={checked['records']}"
    )


if __name__ == "__main__":
    main()
