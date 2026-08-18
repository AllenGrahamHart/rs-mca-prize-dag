#!/usr/bin/env python3
"""Verify the multi-anchor exchange-synchronization contract."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "23f845b7dda0dc7c0b648dd7cdab4b0b1da6326d8cef877912265f8f7986a072"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-multi-anchor-exchange-split-pencil-synchronization-v1",
        "schema",
    )
    minimum, packet, per_type, t_min, t_max = (
        data.get("minimum_anchor_records"),
        data.get("packet_size"),
        data.get("secondary_records_per_type"),
        data.get("minimum_secondary_types"),
        data.get("maximum_secondary_types"),
    )
    require((minimum, packet, per_type, t_min, t_max) == (29, 32, 3, 1, 4), "pins")
    sizes = [packet - per_type * t for t in range(t_min, t_max + 1)]
    require(sizes == data.get("anchor_packet_sizes") == [29, 26, 23, 20], "sizes")
    require(minimum >= max(sizes), "uniform anchor threshold")
    overlap = min(sizes) - 1
    require(overlap == data.get("minimum_one_swap_overlap") == 19, "overlap")
    require(data.get("locators_determining_pencil") == 2 <= overlap, "pencil")
    require(
        (data.get("minimum_exception_degree"), data.get("maximum_exception_degree"))
        == (1, 11),
        "degrees",
    )
    require(data.get("high_complexity_threshold") == 2299571, "chi")
    populations = data.get("toy_pair_populations")
    require(populations == [3, 28, 29, 30, 1154], "populations")
    synchronized = [size for size in populations if size >= minimum]
    require(synchronized == [29, 30, 1154], "threshold partition")
    require(all(size >= max(sizes) for size in synchronized), "packet feasibility")
    require("per first-owned pair type" in str(data.get("nonclaim")).lower(), "nonclaim")
    return {"minimum": minimum, "overlap": overlap, "toy_synchronized": len(synchronized)}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("minimum_anchor_records", 28),
        lambda item: item.__setitem__("packet_size", 31),
        lambda item: item.__setitem__("maximum_secondary_types", 5),
        lambda item: item.__setitem__("anchor_packet_sizes", [29, 26, 23, 19]),
        lambda item: item.__setitem__("minimum_one_swap_overlap", 18),
        lambda item: item.__setitem__("locators_determining_pencil", 20),
        lambda item: item.__setitem__("maximum_exception_degree", 12),
        lambda item: item.__setitem__("high_complexity_threshold", 2299570),
        lambda item: item.__setitem__("nonclaim", "one pencil for all pair types"),
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
        print(f"RANK11_MULTI_ANCHOR_SYNC_TAMPER_PASS mutations={tamper_selftest(data)}/9")
        return
    print(
        "RANK11_MULTI_ANCHOR_SYNC_PASS "
        f"minimum={checked['minimum']} overlap={checked['overlap']} "
        f"toy_synchronized={checked['toy_synchronized']}"
    )


if __name__ == "__main__":
    main()
