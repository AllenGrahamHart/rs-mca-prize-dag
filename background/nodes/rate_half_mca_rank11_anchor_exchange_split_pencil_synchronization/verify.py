#!/usr/bin/env python3
"""Verify the anchor one-swap pencil-synchronization contract."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "da40b3e5c48ebf3c5f08a763edacb5c0035f5c7e3608c12881bd39536710f8e8"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def determinant(left: tuple[int, int], right: tuple[int, int], p: int) -> int:
    return (left[0] * right[1] - left[1] * right[0]) % p


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-anchor-exchange-split-pencil-synchronization-v1",
        "schema",
    )
    anchor, packet, per_type, t_min, t_max = (
        data.get("anchor_owned_slopes"),
        data.get("packet_size"),
        data.get("secondary_records_per_type"),
        data.get("minimum_secondary_types"),
        data.get("maximum_secondary_types"),
    )
    require((anchor, packet, per_type, t_min, t_max) == (5524, 32, 3, 1, 4), "pins")
    sizes = [packet - per_type * t for t in range(t_min, t_max + 1)]
    require(sizes == [29, 26, 23, 20], "anchor sizes")
    require(min(sizes) == data.get("minimum_anchor_packet_size") == 20, "minimum size")
    require(max(sizes) == data.get("maximum_anchor_packet_size") == 29, "maximum size")
    overlap = min(sizes) - 1
    require(overlap == data.get("minimum_one_swap_overlap") == 19, "overlap")
    require(data.get("locators_determining_pencil") == 2 <= overlap, "pencil uniqueness")
    require(
        (data.get("minimum_exception_degree"), data.get("maximum_exception_degree"))
        == (1, 11),
        "degree range",
    )
    require(data.get("high_complexity_threshold") == 2299571, "chi")
    require(anchor - min(sizes) > 0, "outside slopes")

    toy = data.get("toy")
    require(isinstance(toy, dict), "toy")
    p, count, toy_packet, base, removed = (
        toy.get("field"),
        toy.get("anchor_locators"),
        toy.get("packet_size"),
        toy.get("base_indices"),
        toy.get("removed_index"),
    )
    require((p, count, toy_packet, base, removed) == (101, 12, 5, [0, 1, 2, 3, 4], 0), "toy pins")
    locators = [((-root) % p, 1) for root in range(count)]
    require(all(determinant(locators[i], locators[j], p) != 0 for i in range(count) for j in range(i)), "toy distinct")
    common = [index for index in base if index != removed]
    require(len(common) == toy_packet - 1 >= 2, "toy overlap")
    first, second = locators[common[0]], locators[common[1]]
    basis_det = determinant(first, second, p)
    require(basis_det != 0, "toy basis")
    inverse_det = pow(basis_det, p - 2, p)
    for eta in range(count):
        if eta in base:
            continue
        swapped = common + [eta]
        require(len(swapped) == toy_packet, "toy packet size")
        for index in swapped:
            vector = locators[index]
            left_coefficient = determinant(vector, second, p) * inverse_det % p
            right_coefficient = determinant(first, vector, p) * inverse_det % p
            reconstructed = (
                (left_coefficient * first[0] + right_coefficient * second[0]) % p,
                (left_coefficient * first[1] + right_coefficient * second[1]) % p,
            )
            require(reconstructed == vector, "toy span")
    require("does not pay" in str(data.get("nonclaim")).lower(), "nonclaim")
    return {"anchor": anchor, "overlap": overlap, "swaps": anchor - min(sizes)}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("anchor_owned_slopes", 19),
        lambda item: item.__setitem__("packet_size", 31),
        lambda item: item.__setitem__("maximum_secondary_types", 5),
        lambda item: item.__setitem__("minimum_anchor_packet_size", 19),
        lambda item: item.__setitem__("minimum_one_swap_overlap", 18),
        lambda item: item.__setitem__("locators_determining_pencil", 20),
        lambda item: item.__setitem__("high_complexity_threshold", 2299570),
        lambda item: item["toy"].__setitem__("base_indices", [0, 0, 2, 3, 4]),
        lambda item: item.__setitem__("nonclaim", "pays both outputs"),
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
        print(f"RANK11_ANCHOR_EXCHANGE_SYNC_TAMPER_PASS mutations={tamper_selftest(data)}/9")
        return
    print(
        "RANK11_ANCHOR_EXCHANGE_SYNC_PASS "
        f"anchor={checked['anchor']} overlap={checked['overlap']} swaps>={checked['swaps']}"
    )


if __name__ == "__main__":
    main()
