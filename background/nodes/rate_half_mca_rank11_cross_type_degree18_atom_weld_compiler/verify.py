#!/usr/bin/env python3
"""Verify symmetric degree-18 cross-type atom-weld packet profiles."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "8482df87726c964e3469bb112130f601bbbbbfc1353d4bddcd8f998efa4a851f"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(numerator: int, denominator: int) -> int:
    return -(-numerator // denominator)


def identity_margin(shared: int) -> int:
    n, m, dimension = 2097152, 1116048, 1048576
    return ceil_div(shared * m - n, shared - 1) - (dimension - 1)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-cross-type-degree18-atom-weld-compiler-v1",
        "schema",
    )
    size = data.get("packet_size")
    anchor = data.get("anchor_records")
    require((size, anchor) == (32, 18), "packet pins")
    require(data.get("minimum_large_type_records") == 29, "large type")
    require(data.get("minimum_triple_owner_records") == 3, "triple owner")
    require(data.get("component_selection_cap") == 4, "component cap")
    require(data.get("high_complexity_floor") == 2299571, "complexity")
    profiles = data.get("profiles")
    require(isinstance(profiles, list) and len(profiles) == 4, "profiles")
    minimum_shared = size
    for index, profile in enumerate(profiles, start=1):
        require(profile.get("secondary_types") == index, "secondary index")
        counterpart = 17 - 3 * index
        other = 3 * (index - 1)
        shared = 2 * counterpart + other
        require(profile.get("counterpart_records") == counterpart, "counterpart")
        require(profile.get("other_records") == other, "other")
        require(anchor + counterpart + other == size, "packet total")
        require(profile.get("shared_records") == shared == 31 - 3 * index, "shared")
        require(counterpart >= 3, "counterpart multiplicity")
        require(profile.get("identity_margin") == identity_margin(shared) > 0, "identity margin")
        minimum_shared = min(minimum_shared, shared)
    require(minimum_shared == 19, "minimum overlap")
    require(
        data.get("rational_output")
        == "projectively identical pole-simple scalar-locator certificates",
        "output",
    )
    require("not yet synchronized" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_multi_anchor_exchange_split_pencil_synchronization",
        "rate_half_mca_order32_partial_relative_harvest",
        "rate_half_mca_rank11_heavy_ruling_core_saturated_pure_locator_exclusion",
        "rate_half_mca_rank11_heavy_ruling_triple_owner_pole_simple_router",
        "rate_half_mca_rank11_cross_type_pole_simple_atom_identity",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"profiles": len(profiles), "minimum_shared": minimum_shared}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("packet_size", 31),
        lambda item: item.__setitem__("anchor_records", 17),
        lambda item: item.__setitem__("minimum_large_type_records", 28),
        lambda item: item.__setitem__("component_selection_cap", 5),
        lambda item: item["profiles"][0].__setitem__("counterpart_records", 13),
        lambda item: item["profiles"][1].__setitem__("other_records", 4),
        lambda item: item["profiles"][2].__setitem__("shared_records", 21),
        lambda item: item["profiles"][3].__setitem__("identity_margin", 12967),
        lambda item: item.__setitem__("high_complexity_floor", 2299570),
        lambda item: item.__setitem__("rational_output", "proportional scalar pairs"),
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
        print(f"CROSS_TYPE_DEGREE18_ATOM_WELD_TAMPER_PASS mutations={tamper_selftest(data)}/10")
        return
    print(
        "CROSS_TYPE_DEGREE18_ATOM_WELD_PASS "
        f"profiles={checked['profiles']} minimum_shared={checked['minimum_shared']}"
    )


if __name__ == "__main__":
    main()
