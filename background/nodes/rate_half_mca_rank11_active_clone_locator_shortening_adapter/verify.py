#!/usr/bin/env python3
"""Exact verifier for the active-clone locator shortening adapter."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"


def build(d: dict[str, int]) -> dict[str, int]:
    n, k, m = d["n"], d["k"], d["m"]
    assert d["active_mass"] == 388650911452
    assert d["product_dimension_floor"] == 2 + 4 - 1
    assert d["clone_size_max"] == k - d["product_dimension_floor"]
    assert d["shortened_k_min"] == d["product_dimension_floor"]
    assert d["shortened_k_max"] == k - d["clone_size_min"]
    assert d["clone_size_min"] <= d["clone_size_max"]

    assert n - k == d["redundancy"]
    assert m - k == d["agreement_gap"]
    assert n - m == d["misses"]

    for c in (d["clone_size_min"], d["clone_size_max"]):
        nn, kk, mm = n - c, k - c, m - c
        assert d["shortened_k_min"] <= kk <= d["shortened_k_max"]
        assert nn - kk == d["redundancy"]
        assert mm - kk == d["agreement_gap"]
        assert nn - mm == d["misses"]

    root_floor_at_min = max(0, d["residual_roots"] - d["clone_size_min"])
    assert root_floor_at_min == 27735
    return {
        "c_min": d["clone_size_min"],
        "c_max": d["clone_size_max"],
        "k_min": d["shortened_k_min"],
        "k_max": d["shortened_k_max"],
        "root_floor_at_min": root_floor_at_min,
    }


def tamper_selftest(data: dict[str, int]) -> int:
    mutations = []
    for key, delta in (
        ("active_mass", 1),
        ("clone_size_min", -1),
        ("product_dimension_floor", -1),
        ("clone_size_max", 1),
        ("shortened_k_min", 1),
        ("shortened_k_max", -1),
        ("agreement_gap", 1),
        ("residual_roots", -1),
    ):
        changed = copy.deepcopy(data)
        changed[key] += delta
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
        print(f"RANK11_ACTIVE_CLONE_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "RANK11_ACTIVE_CLONE_PASS "
        f"c={result['c_min']}..{result['c_max']} "
        f"shortened_k={result['k_min']}..{result['k_max']} "
        f"mass={data['active_mass']}"
    )


if __name__ == "__main__":
    main()
