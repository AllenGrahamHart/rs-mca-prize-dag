#!/usr/bin/env python3
"""Tiny checker for DLI odd-phase ledger coverage and summation."""

from __future__ import annotations


def accepts(required, records, budget) -> bool:
    by_key = {tuple(record["key"]): record for record in records}
    if set(by_key) != {tuple(key) for key in required}:
        return False
    total = 0
    for key in required:
        record = by_key[tuple(key)]
        if record.get("artin_schreier_trivial") is not False:
            return False
        bound = record.get("reduced_pole_bound")
        if not isinstance(bound, int) or bound < 0:
            return False
        total += bound
    return total <= budget


def main() -> None:
    required = [
        ("profile-a", "lambda-1", 1, "component-0"),
        ("profile-a", "lambda-1", 2, "component-0"),
        ("profile-b", "lambda-2", 1, "component-1"),
    ]
    good = [
        {"key": list(key), "artin_schreier_trivial": False, "reduced_pole_bound": i}
        for i, key in enumerate(required, start=1)
    ]
    assert accepts(required, good, budget=6)

    missing = good[:-1]
    assert not accepts(required, missing, budget=6)

    trivial = [dict(record) for record in good]
    trivial[0]["artin_schreier_trivial"] = True
    assert not accepts(required, trivial, budget=6)

    too_large = [dict(record) for record in good]
    too_large[1]["reduced_pole_bound"] = 10
    assert not accepts(required, too_large, budget=6)

    print("PASS: DLI odd-phase ledger soundness")


if __name__ == "__main__":
    main()
