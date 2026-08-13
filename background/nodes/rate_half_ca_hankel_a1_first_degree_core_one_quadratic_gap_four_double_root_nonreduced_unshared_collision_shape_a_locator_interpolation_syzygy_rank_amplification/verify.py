#!/usr/bin/env python3
"""Replay the locator-interpolation rank amplification."""

from __future__ import annotations

from dataclasses import dataclass


class VerificationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


@dataclass(frozen=True)
class Formula:
    official_e: int = 183251937963
    n: int = 274877906941
    locator_x_degree: int = 549755813887
    domain_rows: int = 824633720830
    rank_floor: int = 91625968982
    boundary_kernel: int = 91625968982
    former_floor: int = 61083979322


def replay(formula: Formula) -> dict[str, int]:
    e = (2**39 + 1) // 3
    n = (3 * e - 7) // 2
    d = 3 * e - 2
    rows = (9 * e - 7) // 2
    rank_floor = (e + 1) // 2
    boundary_kernel = 3 * rank_floor - (e + 1)
    former_floor = (e + 3) // 3
    require(e == formula.official_e, "official e")
    require(n == formula.n, "n")
    require(d == formula.locator_x_degree, "locator degree")
    require(rows == formula.domain_rows, "domain rows")
    require(rows - d - 2 == n, "parity range")
    require(rank_floor == formula.rank_floor, "rank floor")
    require(boundary_kernel == formula.boundary_kernel, "boundary kernel")
    require(former_floor == formula.former_floor, "former floor")
    require(2 * rank_floor >= e, "rank inequality")
    require(2 * (rank_floor - 1) < e, "rank floor minimality")
    require(3 * former_floor - (e + 1) < former_floor - 1,
            "former boundary excluded")
    return {
        "e": e,
        "n": n,
        "rank_floor": rank_floor,
        "boundary_kernel": boundary_kernel,
        "former_floor": former_floor,
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
        "RATE_HALF_SHAPE_A_LOCATOR_INTERPOLATION_RANK_AMPLIFICATION_PASS",
        f"rank_floor={result['rank_floor']}",
        f"boundary_kernel={result['boundary_kernel']}",
        f"former_floor={result['former_floor']}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
