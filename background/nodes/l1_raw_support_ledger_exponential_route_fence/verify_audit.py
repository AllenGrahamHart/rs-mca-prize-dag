#!/usr/bin/env python3
"""Mutation audit for the L1 raw-ledger route fence."""

from __future__ import annotations


def valid(values: dict[str, int]) -> bool:
    n = values["n"]
    return all(
        (
            values["N"] + values["b"] + values["M"] * values["ell"] == n,
            values["b"] < values["ell"],
            values["r"] + values["h"] == values["ell"] + values["d"],
            0 < values["a"] <= values["d"],
            values["h"] > values["d"],
            values["u"] == n // 4,
            values["e"] == n // 4 - 2 * values["ell"] + 1,
            values["gamma"] == n // 4 - 3 * values["ell"] // 2 + 1,
            values["gamma"] >= n // 8,
        )
    )


def base() -> dict[str, int]:
    j = 16
    n = 1 << j
    ell = n // j
    M = j // 2
    a = ell // 2
    h = M * a
    d = h - ell
    return {
        "n": n,
        "N": n // 2 - 1,
        "b": 1,
        "M": M,
        "ell": ell,
        "r": 0,
        "a": a,
        "h": h,
        "d": d,
        "u": M * ell - h,
        "e": max(0, 2 * d + 1 - h),
        "gamma": d - a + 1,
    }


def main() -> None:
    row = base()
    assert valid(row)
    keys = ("N", "b", "M", "r", "h", "d", "e", "gamma")
    caught = 0
    for key in keys:
        mutant = dict(row)
        mutant[key] += 1
        if not valid(mutant):
            caught += 1
    assert caught == len(keys)
    print(f"L1_RAW_SUPPORT_LEDGER_ROUTE_FENCE_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
