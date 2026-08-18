#!/usr/bin/env python3
"""Exact verifier for the factor-flag clone/line dichotomy."""

from __future__ import annotations

import argparse
import copy
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"


def clone_triples(universe: int, cutoff: int) -> int:
    blocks, remainder = divmod(universe, cutoff)
    return blocks * comb(cutoff, 3) + comb(remainder, 3)


def build(data: dict[str, int]) -> dict[str, int]:
    u = data["universe"]
    total = data["deep_mass"] * comb(data["residual_roots"], 3)
    rank_three = data["rank_three_cap"] * comb(u, 3)
    low = total - rank_three
    assert low == data["low_rank_incidence"] > 0

    cutoff = data["selected_clone_cutoff"]
    packed = clone_triples(u, cutoff)
    assert packed == data["selected_clone_triples"]
    residual = max(0, low - data["clone_bucket_cap"] * packed)
    line_mass = (residual + comb(u, 3) - 1) // comb(u, 3)
    assert line_mass == data["selected_rank_two_mass"]
    assert data["selected_clone_output"] == cutoff + 1

    need = (low + data["clone_bucket_cap"] - 1) // data["clone_bucket_cap"]
    first = next(c for c in range(3, u + 1) if clone_triples(u, c) >= need)
    assert first == data["first_clone_only_cutoff"]
    return {"low": low, "packed": packed, "line_mass": line_mass, "first": first}


def tamper_selftest(data: dict[str, int]) -> int:
    mutations = []
    for key, delta in (
        ("low_rank_incidence", 1),
        ("selected_clone_triples", -1),
        ("selected_rank_two_mass", 1),
        ("first_clone_only_cutoff", -1),
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
        print(f"RANK11_CLONE_LINE_TAMPER_PASS mutations={tamper_selftest(data)}/4")
        return
    print(
        "RANK11_CLONE_LINE_PASS "
        f"low_incidence={result['low']} line_mass={result['line_mass']} "
        f"clone_output={data['selected_clone_output']}"
    )


if __name__ == "__main__":
    main()
