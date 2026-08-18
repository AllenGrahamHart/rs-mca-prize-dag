#!/usr/bin/env python3
"""Verify the cross-type one-swap synchronization wall."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "1befeda8f067182ab717a44bce4f202e7a9f1f58eb4de24011025f24d473266b"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def count_profiles(size: int) -> list[tuple[int, int, int]]:
    return [
        (p_count, q_count, size - p_count - q_count)
        for p_count in range(size + 1)
        for q_count in range(size - p_count + 1)
    ]


def maximum_cross_anchor_overlap(size: int, threshold: int) -> int:
    profiles = count_profiles(size)
    maximum = 0
    for p_packet in profiles:
        if p_packet[0] < threshold:
            continue
        for q_packet in profiles:
            if q_packet[1] < threshold:
                continue
            overlap = sum(min(left, right) for left, right in zip(p_packet, q_packet))
            maximum = max(maximum, overlap)
    return maximum


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-cross-type-one-swap-synchronization-wall-v1",
        "schema",
    )
    size = data.get("packet_size")
    partial = data.get("partial_relative_anchor_threshold")
    heavy = data.get("heavy_ruling_anchor_threshold")
    one_swap = data.get("one_swap_overlap")
    require((size, partial, heavy, one_swap) == (32, 18, 20, 31), "pins")
    require(2 * partial > size and 2 * heavy > size, "unique anchors")
    partial_cap = maximum_cross_anchor_overlap(size, partial)
    heavy_cap = maximum_cross_anchor_overlap(size, heavy)
    require(data.get("partial_relative_cross_anchor_overlap_cap") == partial_cap == 28, "partial cap")
    require(data.get("heavy_ruling_cross_anchor_overlap_cap") == heavy_cap == 24, "heavy cap")
    require(one_swap > partial_cap and one_swap > heavy_cap, "one-swap separation")
    require(data.get("quotient_population_floor") == 520, "population pin")
    shared = data.get("cross_type_shared_records")
    g_floor = data.get("collision_forced_common_zero_before_shortening")
    denominator = data.get("denominator_degree_cap")
    core_floor = data.get("collision_forced_pair_core_before_shortening")
    pair_cap = data.get("distinct_pair_agreement_cap_before_shortening")
    require(shared == 28, "collision overlap")
    require(g_floor == (shared * 1116048 - 2097152 + shared - 2) // (shared - 1) == 1079711, "collision core")
    require(denominator == 67472, "denominator")
    require(core_floor == g_floor - denominator == 1012239, "pair core floor")
    require(pair_cap == 1048575, "pair cap")
    require(data.get("collision_pair_uniqueness_gap") == pair_cap - core_floor == 36336, "collision gap")
    require("does not prove" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_order32_partial_relative_harvest",
        "rate_half_mca_rank11_multi_anchor_exchange_split_pencil_synchronization",
        "rate_half_mca_rank11_quadratic_quotient_population_router",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"partial_cap": partial_cap, "heavy_cap": heavy_cap}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("packet_size", 31),
        lambda item: item.__setitem__("partial_relative_anchor_threshold", 17),
        lambda item: item.__setitem__("partial_relative_cross_anchor_overlap_cap", 29),
        lambda item: item.__setitem__("heavy_ruling_anchor_threshold", 19),
        lambda item: item.__setitem__("heavy_ruling_cross_anchor_overlap_cap", 25),
        lambda item: item.__setitem__("one_swap_overlap", 28),
        lambda item: item.__setitem__("quotient_population_floor", 519),
        lambda item: item.__setitem__("collision_forced_pair_core_before_shortening", 1012240),
        lambda item: item.__setitem__("collision_pair_uniqueness_gap", 36335),
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
        print(f"CROSS_TYPE_ONE_SWAP_WALL_TAMPER_PASS mutations={tamper_selftest(data)}/9")
        return
    print(
        "CROSS_TYPE_ONE_SWAP_WALL_PASS "
        f"caps={checked['partial_cap']},{checked['heavy_cap']}"
    )


if __name__ == "__main__":
    main()
