#!/usr/bin/env python3
"""Exact verifier for the rank-two residual base/plane dichotomy."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"


def build(d: dict[str, int]) -> dict[str, int]:
    assert d["bucket_mass"] == 388650911452
    assert d["base_output"] == d["base_cutoff"] + 1
    assert d["minimum_nonbase_roots"] == (
        d["residual_roots"] - d["base_cutoff"]
    )
    counts = [
        (d["universe"] - q) // (d["residual_roots"] - q)
        for q in range(d["base_cutoff"] + 1)
    ]
    maximum = max(counts)
    maximizing_q = max(q for q, value in enumerate(counts) if value == maximum)
    assert maximum == d["maximum_planes"]
    assert maximizing_q == d["base_cutoff"]
    heavy = (d["bucket_mass"] + maximum - 1) // maximum
    assert heavy == d["heavy_plane_mass"]
    assert d["rank_three_cap"] < heavy
    assert d["forced_correction_rank"] == 4
    return {"maximum": maximum, "q": maximizing_q, "heavy": heavy}


def tamper_selftest(data: dict[str, int]) -> int:
    mutations = []
    for key, delta in (
        ("base_output", 1),
        ("minimum_nonbase_roots", -1),
        ("maximum_planes", 1),
        ("bucket_mass", 1),
        ("heavy_plane_mass", -1),
        ("rank_three_cap", 7000000000),
        ("forced_correction_rank", -1),
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
        print(f"RANK11_BASE_PLANE_TAMPER_PASS mutations={tamper_selftest(data)}/7")
        return
    print(
        "RANK11_BASE_PLANE_PASS "
        f"planes={result['maximum']} q={result['q']} "
        f"heavy_mass={result['heavy']} rank={data['forced_correction_rank']}"
    )


if __name__ == "__main__":
    main()
