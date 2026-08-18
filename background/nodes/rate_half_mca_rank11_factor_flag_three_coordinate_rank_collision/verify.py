#!/usr/bin/env python3
"""Exact verifier for the three-coordinate residual rank collision."""

from __future__ import annotations

import argparse
import copy
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
N = 2_097_152
K = 1_048_576
A = 1_114_369


def build(data: dict[str, int]) -> dict[str, int]:
    universe = data["anchor_good_universe"]
    roots = data["residual_roots"]
    first = data["initial_mass"]
    second = ((roots - 1) * first + (universe - 1) - 1) // (universe - 1)
    third = ((roots - 2) * second + (universe - 2) - 1) // (universe - 2)
    multiplicity = N - A
    cap4 = multiplicity * (comb(N - K + 4, 4) // comb(A - K + 4, 4))
    assert second == data["second_mass"]
    assert third == data["third_mass"]
    assert data["rank_three_correction_dimension"] == 4
    assert cap4 == data["rank_three_slope_cap"]
    assert third > cap4
    assert data["forced_rank_upper_bound"] == 2
    return {"second": second, "third": third, "cap4": cap4}


def tamper_selftest(data: dict[str, int]) -> int:
    mutations = []
    for key, delta in (
        ("second_mass", -1),
        ("third_mass", 1),
        ("rank_three_slope_cap", 1),
        ("forced_rank_upper_bound", 1),
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
        print(f"RANK11_THREE_COORD_TAMPER_PASS mutations={tamper_selftest(data)}/4")
        return
    print(
        "RANK11_THREE_COORD_PASS "
        f"mass2={result['second']} mass3={result['third']} cap4={result['cap4']} rank<=2"
    )


if __name__ == "__main__":
    main()
