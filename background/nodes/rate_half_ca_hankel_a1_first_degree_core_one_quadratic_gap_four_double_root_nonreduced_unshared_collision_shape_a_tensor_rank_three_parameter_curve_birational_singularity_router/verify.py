#!/usr/bin/env python3
"""Replay the official rank-three birational singularity ledger."""

from __future__ import annotations

import math
from dataclasses import dataclass


class VerificationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def ceil_div(left: int, right: int) -> int:
    return -(-left // right)


@dataclass(frozen=True)
class Formula:
    official_e: int = 183251937963
    official_m: int = 183251937961
    official_n: int = 274877906941
    total_column_deficit: int = 366503875919
    maximum_empty_columns: int = 1
    pair_branch_floor: int = 30541989660
    local_delta_floor: int = 466406566180502462970
    six_vertex_delta_floor: int = 2798439396930304829525


def replay(formula: Formula) -> dict[str, int]:
    e = ((1 << 39) + 1) // 3
    m = e - 2
    n = (3 * e - 7) // 2
    deficit = 2 * e - 7
    maximum_empty = deficit // n
    require(e == formula.official_e, "official e")
    require(m == formula.official_m, "official m")
    require(n == formula.official_n, "official n")
    require(deficit == formula.total_column_deficit, "column deficit")
    require(maximum_empty == formula.maximum_empty_columns, "empty columns")
    require(2 * n > deficit, "two-empty-column exclusion")
    require(math.gcd(m, 3 * e) == 1, "all-active gcd")
    require(math.gcd(m, 3 * e - 1) == 1, "one-empty gcd")

    branch_total = e - 8
    pair_floor = ceil_div(branch_total, 6)
    require(pair_floor == formula.pair_branch_floor, "pair branch floor")
    local_delta = pair_floor * (pair_floor - 1) // 2
    require(local_delta == formula.local_delta_floor, "local delta floor")

    quotient, remainder = divmod(branch_total, 6)
    six_delta = (
        remainder * (quotient + 1) * quotient // 2
        + (6 - remainder) * quotient * (quotient - 1) // 2
    )
    require(six_delta == formula.six_vertex_delta_floor, "six delta floor")
    return {
        "e": e,
        "m": m,
        "n": n,
        "deficit": deficit,
        "maximum_empty": maximum_empty,
        "pair_floor": pair_floor,
        "local_delta": local_delta,
        "six_delta": six_delta,
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
        "RATE_HALF_SHAPE_A_TENSOR_RANK_THREE_BIRATIONAL_ROUTER_PASS",
        f"empty_columns_max={result['maximum_empty']}",
        f"pair_branches={result['pair_floor']}",
        f"six_delta={result['six_delta']}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
