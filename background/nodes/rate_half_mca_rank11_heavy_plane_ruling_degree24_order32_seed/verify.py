#!/usr/bin/env python3
"""Exact verifier for the heavy-ruling degree-24 order-32 seed."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def build(d: dict[str, int]) -> dict[str, int]:
    q4 = d["rank_four_pair_types"]
    heavy = d["orientation_mass"] - d["singleton_record_cap"]
    assert d["singleton_record_cap"] == q4
    assert heavy == d["heavy_record_mass"]

    heavy_cap = d["rank_two_pair_types"] * d["fixed_pair_multiplicity"]
    assert heavy_cap == d["large_core_heavy_capacity"]
    total_cap = heavy_cap + d["singleton_record_cap"]
    assert total_cap == d["large_core_total_capacity"]
    assert d["orientation_mass"] - total_cap == d["large_core_gap"] > 0

    dense = ceil_div(heavy, q4)
    assert dense == d["dense_pair_minimum"]
    assert d["maximum_additional_pair_types"] == d["component_dimension"]
    assert d["maximum_selected_pair_types"] == d["component_dimension"] + 1

    anchor = d["seed_size"] - 2 * d["maximum_additional_pair_types"]
    assert anchor == d["minimum_anchor_records"]
    assert dense >= anchor
    assert d["minimum_residual_dimension"] == 3
    assert d["minimum_slope_degree"] == anchor
    assert d["maximum_slope_degree"] == d["seed_size"] - 1
    return {"heavy": heavy, "gap": d["large_core_gap"], "dense": dense, "anchor": anchor}


def tamper_selftest(data: dict[str, int]) -> int:
    mutations = []
    keys = (
        "orientation_mass",
        "rank_four_pair_types",
        "singleton_record_cap",
        "heavy_record_mass",
        "rank_two_pair_types",
        "fixed_pair_multiplicity",
        "large_core_heavy_capacity",
        "large_core_total_capacity",
        "large_core_gap",
        "dense_pair_minimum",
        "component_dimension",
        "maximum_additional_pair_types",
        "maximum_selected_pair_types",
        "seed_size",
        "minimum_anchor_records",
        "minimum_residual_dimension",
        "minimum_slope_degree",
        "maximum_slope_degree",
    )
    for key in keys:
        changed = copy.deepcopy(data)
        changed[key] += 1
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
        print(f"RANK11_RULING_DEG24_TAMPER_PASS mutations={caught}/18")
        return
    print(
        "RANK11_RULING_DEG24_PASS "
        f"heavy={result['heavy']} gap={result['gap']} "
        f"dense={result['dense']} anchor={result['anchor']}"
    )


if __name__ == "__main__":
    main()
