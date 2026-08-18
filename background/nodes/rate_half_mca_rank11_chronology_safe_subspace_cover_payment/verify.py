#!/usr/bin/env python3
"""Exact verifier for the chronology-safe rank-eleven cover payment."""

from __future__ import annotations

import argparse
import copy
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"


def build(data: dict[str, object]) -> dict[str, object]:
    row = data["row"]
    n = row["n"]
    k = row["k"]
    agreement = row["A"]
    budget = row["budget"]
    transverse = row["transverse"]
    allowance = budget - transverse
    q = 2_130_706_433**6
    multiplicity = n - agreement

    assert allowance == row["allowance"] == 65_167_969_673_715_470
    computed = []
    for d in range(1, 10):
        list_cap = comb(n - k + d, d) // comb(agreement - k + d, d)
        slope_cap = multiplicity * list_cap
        first_unsafe = allowance // slope_cap + 1
        assert list_cap * list_cap < q
        computed.append(
            {
                "d": d,
                "M": list_cap,
                "R": slope_cap,
                "first_unsafe_uniform_cover": first_unsafe,
            }
        )

    assert computed == data["dimensions"]
    five = computed[4]
    corollaries = {
        "two_five_space_cost": 2 * five["R"],
        "maximum_paid_five_space_classes": allowance // five["R"],
    }
    assert corollaries == data["corollaries"]
    assert corollaries["two_five_space_cost"] < allowance
    return {"allowance": allowance, "dimensions": computed, "corollaries": corollaries}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = []
    changed = copy.deepcopy(data)
    changed["row"]["allowance"] += 1
    mutations.append(changed)
    changed = copy.deepcopy(data)
    changed["dimensions"][4]["first_unsafe_uniform_cover"] -= 1
    mutations.append(changed)
    changed = copy.deepcopy(data)
    changed["dimensions"][8]["R"] -= 1
    mutations.append(changed)
    changed = copy.deepcopy(data)
    changed["corollaries"]["two_five_space_cost"] += 1
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
        print(f"RANK11_SUBSPACE_COVER_TAMPER_PASS mutations={tamper_selftest(data)}/4")
        return
    print(
        "RANK11_SUBSPACE_COVER_PASS "
        f"allowance={result['allowance']} "
        f"five_spaces={result['corollaries']['maximum_paid_five_space_classes']}"
    )


if __name__ == "__main__":
    main()
