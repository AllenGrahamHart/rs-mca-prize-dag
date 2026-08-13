#!/usr/bin/env python3
"""Replay all-rank Shape-A parameter-map birationality arithmetic."""

from __future__ import annotations

import math
from dataclasses import dataclass


class VerificationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


@dataclass(frozen=True)
class Formula:
    official_e: int = 183251937963
    official_m: int = 183251937961
    official_n: int = 274877906941
    total_deficit: int = 366503875919
    maximum_empty_columns: int = 1
    gcd_all_active: int = 1
    gcd_one_empty: int = 1


def replay(formula: Formula) -> dict[str, int]:
    e = (2**39 + 1) // 3
    m = e - 2
    n = (3 * e - 7) // 2
    deficit = 2 * e - 7
    maximum_empty = deficit // n
    gcd_all = math.gcd(m, 3 * e)
    gcd_one = math.gcd(m, 3 * e - 1)
    require(e == formula.official_e, "official e")
    require(m == formula.official_m, "official m")
    require(n == formula.official_n, "official n")
    require(deficit == formula.total_deficit, "total deficit")
    require(maximum_empty == formula.maximum_empty_columns, "empty columns")
    require(2 * n > deficit, "two-empty exclusion")
    require(gcd_all == formula.gcd_all_active, "all-active gcd")
    require(gcd_one == formula.gcd_one_empty, "one-empty gcd")
    return {
        "e": e,
        "m": m,
        "n": n,
        "deficit": deficit,
        "maximum_empty": maximum_empty,
        "gcd_all": gcd_all,
        "gcd_one": gcd_one,
    }


def tamper_selftest() -> int:
    base = Formula()
    rejected = 0
    for field in base.__dict__:
        values = dict(base.__dict__)
        values[field] += 1
        try:
            replay(Formula(**values))
        except VerificationError:
            rejected += 1
    require(rejected == len(base.__dict__), "hostile mutations")
    return rejected


def main() -> None:
    result = replay(Formula())
    mutations = tamper_selftest()
    print(
        "RATE_HALF_SHAPE_A_ALL_EXCESS_PARAMETER_MAP_BIRATIONALITY_PASS",
        f"empty_columns_max={result['maximum_empty']}",
        f"gcds={(result['gcd_all'], result['gcd_one'])}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
