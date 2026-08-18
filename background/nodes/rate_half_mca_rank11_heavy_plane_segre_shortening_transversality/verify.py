#!/usr/bin/env python3
"""Exact verifier for heavy-plane Segre shortening/transversality."""

from __future__ import annotations

import argparse
import copy
import json
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"


def falling(a: int, r: int) -> int:
    return prod(range(a - r + 1, a + 1))


def rising(a: int, r: int) -> int:
    return prod(range(a, a + r))


def cap(s: int, theta: int, redundancy: int, gap: int) -> int:
    n, m, rank = redundancy + s, gap + s, 4
    first = falling(n, rank + 1) // (m * theta * rising(gap + 1, rank - 1))
    second = falling(redundancy + rank, rank + 1) // (
        theta * rising(gap + 1, rank)
    )
    return max(first, second)


def build(d: dict[str, int]) -> dict[str, int]:
    assert d["mass"] == 9965407986
    assert d["rank_two_cap"] == 248644099
    assert d["shortened_k_min"] == 1048573 - d["locator_max"]
    assert d["shortened_k_max"] == 1048573 - d["locator_min"]
    assert d["turning_dimension"] == (
        d["redundancy"] - 5 * d["agreement_gap"] - 4
    ) // 4

    used = (d["mass"] + d["rank_two_cap"] - 1) // d["rank_two_cap"]
    assert used == d["minimum_used_factors"]
    assert (used - 1) * d["rank_two_cap"] < d["mass"]

    endpoints = (d["shortened_k_min"], d["shortened_k_max"])
    last = max(cap(s, d["last_margin"], d["redundancy"], d["agreement_gap"]) for s in endpoints)
    first = max(cap(s, d["first_paying_margin"], d["redundancy"], d["agreement_gap"]) for s in endpoints)
    assert last == d["last_margin_uniform_cap"] >= d["mass"]
    assert first == d["first_paying_uniform_cap"] < d["mass"]
    assert d["first_paying_margin"] == d["last_margin"] + 1
    return {"used": used, "last": last, "first": first}


def tamper_selftest(data: dict[str, int]) -> int:
    mutations = []
    for key, delta in (
        ("mass", 1),
        ("locator_max", 1),
        ("shortened_k_max", -1),
        ("rank_two_cap", 1),
        ("minimum_used_factors", -1),
        ("turning_dimension", 1),
        ("last_margin_uniform_cap", -1),
        ("first_paying_margin", 1),
        ("first_paying_uniform_cap", 1),
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
        print(f"RANK11_HEAVY_SEGRE_TAMPER_PASS mutations={tamper_selftest(data)}/9")
        return
    print(
        "RANK11_HEAVY_SEGRE_PASS "
        f"used_factors={result['used']} last_cap={result['last']} "
        f"paying_cap={result['first']}"
    )


if __name__ == "__main__":
    main()
