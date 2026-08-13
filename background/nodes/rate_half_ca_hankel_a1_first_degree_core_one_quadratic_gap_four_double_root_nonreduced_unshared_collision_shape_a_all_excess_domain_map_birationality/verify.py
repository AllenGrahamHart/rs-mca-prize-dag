#!/usr/bin/env python3
"""Replay all-rank Shape-A domain-map birationality arithmetic."""

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
    official_rows: int = 824633720830
    residual_norm_degree: int = 366503875919
    maximum_outside_points: int = 1
    gcd_complete: int = 1
    gcd_one_outside: int = 1


def replay(formula: Formula) -> dict[str, int]:
    e = (2**39 + 1) // 3
    m = e - 2
    n = (3 * e - 7) // 2
    rows = (9 * e - 7) // 2
    residual = 3 * e * n - rows * m
    maximum_outside = residual // m
    gcd_complete = math.gcd(n, rows)
    gcd_one = math.gcd(n, rows + 1)
    require(e == formula.official_e, "official e")
    require(m == formula.official_m, "official m")
    require(n == formula.official_n, "official n")
    require(rows == formula.official_rows, "official rows")
    require(residual == formula.residual_norm_degree, "residual norm")
    require(residual == 2 * m - 3, "two-m minus three")
    require(maximum_outside == formula.maximum_outside_points, "outside cap")
    require(gcd_complete == formula.gcd_complete, "complete-fiber gcd")
    require(gcd_one == formula.gcd_one_outside, "one-outside gcd")
    return {
        "e": e,
        "m": m,
        "n": n,
        "rows": rows,
        "residual": residual,
        "maximum_outside": maximum_outside,
        "gcd_complete": gcd_complete,
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
        "RATE_HALF_SHAPE_A_ALL_EXCESS_DOMAIN_MAP_BIRATIONALITY_PASS",
        f"residual_norm={result['residual']}",
        f"outside_max={result['maximum_outside']}",
        f"gcds={(result['gcd_complete'], result['gcd_one'])}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
