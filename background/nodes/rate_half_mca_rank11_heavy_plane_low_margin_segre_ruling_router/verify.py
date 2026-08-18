#!/usr/bin/env python3
"""Exact verifier for the heavy-plane low-margin Segre ruling router."""

from __future__ import annotations

import argparse
import copy
import json
from math import comb, prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"


def falling(a: int, r: int) -> int:
    return prod(range(a - r + 1, a + 1))


def rising(a: int, r: int) -> int:
    return prod(range(a, a + r))


def support_cap(k: int, rank: int, margin: int, r: int, gap: int) -> int:
    n, m = r + k, gap + k
    if rank == 0:
        return n // margin
    first = falling(n, rank + 1) // (
        m * margin * rising(gap + 1, rank - 1)
    )
    second = falling(r + rank, rank + 1) // (
        margin * rising(gap + 1, rank)
    )
    return max(first, second)


def build(d: dict[str, object]) -> dict[str, int]:
    r = int(d["redundancy"])
    gap = int(d["agreement_gap"])
    margin = int(d["margin"])
    endpoints = (int(d["shortened_k_min"]), int(d["shortened_k_max"]))

    caps = []
    for rank in range(5):
        caps.append(max(support_cap(k, rank, margin, r, gap) for k in endpoints))
    assert caps == [int(x) for x in d["high_caps_by_rank"]]
    high = max(caps)
    assert high == int(d["high_cap"])
    low = int(d["mass"]) - high
    assert low == int(d["low_mass"])

    q4 = comb(r + 4, 4) // comb(gap - margin + 5, 4)
    assert q4 == int(d["rank_four_pair_types"])
    assert q4 * q4 == int(d["rank_four_pair_types_squared"])
    nonruling = 2 * q4
    assert nonruling == int(d["nonruling_cap"])
    ruling = low - nonruling
    assert ruling == int(d["ruling_mass"])

    multiplicity = r - gap + margin - 1
    assert multiplicity == int(d["fixed_pair_multiplicity"])
    q2 = comb(r + 2, 2) // comb(gap - margin + 3, 2)
    assert q2 == int(d["rank_two_pair_types"])
    ruling_cap = multiplicity * q2
    assert ruling_cap == int(d["fixed_ruling_cap"])
    planes = (ruling + ruling_cap - 1) // ruling_cap
    assert planes == int(d["minimum_ruling_planes"])

    zero = q4 - 1 + multiplicity
    assert zero == int(d["zero_correction_cap"])
    nonzero = ruling - zero
    assert nonzero == int(d["nonzero_ruling_mass"])
    orientation = (nonzero + 1) // 2
    assert orientation == int(d["orientation_mass"])
    orientation_planes = (orientation + ruling_cap - 1) // ruling_cap
    assert orientation_planes == int(d["minimum_orientation_planes"])
    return {
        "high": high,
        "low": low,
        "ruling": ruling,
        "nonzero": nonzero,
        "planes": planes,
    }


def tamper_selftest(data: dict[str, object]) -> int:
    mutations: list[dict[str, object]] = []
    scalar_keys = (
        "margin",
        "mass",
        "high_cap",
        "low_mass",
        "rank_four_pair_types",
        "rank_four_pair_types_squared",
        "nonruling_cap",
        "ruling_mass",
        "rank_two_pair_types",
        "fixed_pair_multiplicity",
        "fixed_ruling_cap",
        "minimum_ruling_planes",
        "zero_correction_cap",
        "nonzero_ruling_mass",
        "orientation_mass",
        "minimum_orientation_planes",
    )
    for key in scalar_keys:
        changed = copy.deepcopy(data)
        changed[key] = int(changed[key]) + 1
        mutations.append(changed)
    changed = copy.deepcopy(data)
    changed["high_caps_by_rank"] = list(changed["high_caps_by_rank"])
    changed["high_caps_by_rank"][4] += 1
    mutations.append(changed)

    caught = 0
    for mutation in mutations:
        try:
            build(mutation)
        except AssertionError:
            caught += 1
    assert caught == len(mutations)
    return caught


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(CONTRACT.read_text())
    result = build(data)
    if args.tamper_selftest:
        caught = tamper_selftest(data)
        print(f"RANK11_SEGRE_RULING_TAMPER_PASS mutations={caught}/17")
        return
    print(
        "RANK11_SEGRE_RULING_PASS "
        f"high={result['high']} low={result['low']} "
        f"ruling={result['ruling']} nonzero={result['nonzero']} "
        f"planes={result['planes']}"
    )


if __name__ == "__main__":
    main()
