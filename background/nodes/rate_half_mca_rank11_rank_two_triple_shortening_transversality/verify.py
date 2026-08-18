#!/usr/bin/env python3
"""Exact verifier for rank-two-triple shortening/transversality."""

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


def support_cap(n: int, k: int, m: int, rank: int, theta: int) -> int:
    w = m - k
    first = falling(n, rank + 1) // (m * theta * rising(w + 1, rank - 1))
    second = falling(n - k + rank, rank + 1) // (
        theta * rising(w + 1, rank)
    )
    return max(first, second)


def build(d: dict[str, int]) -> dict[str, int]:
    assert d["mass"] == 388650911452
    assert d["rank_four_cap"] < d["mass"]
    assert d["residual_roots_after"] == (
        d["residual_roots_before"] - d["locator_degree"]
    )
    assert d["m_short"] - d["k_short"] == d["w"]

    checks = (
        (5, d["rank_five_last_margin"], d["rank_five_last_cap"]),
        (
            5,
            d["rank_five_first_paying_margin"],
            d["rank_five_first_paying_cap"],
        ),
        (6, d["rank_six_last_margin"], d["rank_six_last_cap"]),
        (
            6,
            d["rank_six_first_paying_margin"],
            d["rank_six_first_paying_cap"],
        ),
    )
    for rank, theta, expected in checks:
        assert support_cap(
            d["n_short"], d["k_short"], d["m_short"], rank, theta
        ) == expected

    assert d["rank_five_last_cap"] >= d["mass"]
    assert d["rank_five_first_paying_cap"] < d["mass"]
    assert d["rank_five_first_paying_margin"] == d["rank_five_last_margin"] + 1
    assert d["rank_six_last_cap"] >= d["mass"]
    assert d["rank_six_first_paying_cap"] < d["mass"]
    assert d["rank_six_first_paying_margin"] == d["rank_six_last_margin"] + 1
    return {
        "rank5": d["rank_five_last_margin"],
        "rank6": d["rank_six_last_margin"],
    }


def tamper_selftest(data: dict[str, int]) -> int:
    mutations = []
    for key, delta in (
        ("mass", 1),
        ("rank_four_cap", 400000000000),
        ("residual_roots_after", 1),
        ("n_short", 1),
        ("rank_five_last_cap", 1),
        ("rank_five_first_paying_margin", 1),
        ("rank_six_last_cap", -1),
        ("rank_six_first_paying_cap", 1),
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
        print(f"RANK11_RANK2_SHORT_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "RANK11_RANK2_SHORT_PASS "
        f"mass={data['mass']} rank5_exceptions={result['rank5']} "
        f"rank6_exceptions={result['rank6']}"
    )


if __name__ == "__main__":
    main()
