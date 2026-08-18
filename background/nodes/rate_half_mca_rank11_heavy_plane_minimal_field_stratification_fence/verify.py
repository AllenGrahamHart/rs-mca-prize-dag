#!/usr/bin/env python3
"""Exact verifier for the heavy-plane minimal-field stratification fence."""

from __future__ import annotations

import argparse
import copy
import json
from math import ceil
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def build(d: dict[str, object]) -> dict[str, int]:
    degree = int(d["extension_degree"])
    strata = [int(x) for x in d["minimal_field_degrees"]]
    mass = int(d["mass"])
    cap = int(d["rank_two_cap"])

    assert strata == divisors(degree) == [1, 2, 3, 6]
    assert int(d["stratum_count"]) == len(strata)
    heavy = ceil(mass / len(strata))
    assert heavy == int(d["heavy_stratum_mass"])
    ten = 10 * cap
    assert ten == int(d["ten_factor_capacity"])
    assert heavy - ten == int(d["heavy_stratum_gap"]) > 0
    needed = ceil(heavy / cap)
    assert needed == int(d["minimum_stratum_factors"]) == 11

    product_degrees = [int(x) for x in d["witness_product_degrees"]]
    assert product_degrees == [0, 2, 4, 6]
    assert len(set(product_degrees)) == 4
    assert max(product_degrees) < int(d["witness_shortened_dimension"])

    factor_count = int(d["witness_factor_count"])
    full = int(d["witness_full_factors"])
    last = mass - full * cap
    assert factor_count == full + 1 == 41
    assert last == int(d["witness_last_mass"])
    assert 0 < last <= cap
    return {"heavy": heavy, "needed": needed, "last": last}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations: list[dict[str, object]] = []
    for key, delta in (
        ("extension_degree", 1),
        ("stratum_count", -1),
        ("mass", 1),
        ("heavy_stratum_mass", -1),
        ("rank_two_cap", 1),
        ("ten_factor_capacity", 1),
        ("heavy_stratum_gap", -1),
        ("minimum_stratum_factors", -1),
        ("witness_shortened_dimension", -1),
        ("witness_factor_count", -1),
        ("witness_last_mass", 1),
    ):
        changed = copy.deepcopy(data)
        changed[key] = int(changed[key]) + delta
        mutations.append(changed)
    changed = copy.deepcopy(data)
    changed["minimal_field_degrees"] = [1, 2, 6]
    mutations.append(changed)
    changed = copy.deepcopy(data)
    changed["witness_product_degrees"] = [0, 2, 4, 7]
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
        print(f"RANK11_MINIMAL_FIELD_TAMPER_PASS mutations={caught}/13")
        return
    print(
        "RANK11_MINIMAL_FIELD_PASS "
        f"heavy_mass={result['heavy']} factors={result['needed']} "
        f"witness_last={result['last']}"
    )


if __name__ == "__main__":
    main()
