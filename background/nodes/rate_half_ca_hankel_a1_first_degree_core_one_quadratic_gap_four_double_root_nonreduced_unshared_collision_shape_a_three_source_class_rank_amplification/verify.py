#!/usr/bin/env python3
"""Replay the Shape-A three-source-class rank amplification."""

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
    locator_rank: int = 183251937964
    split_x_degree: int = 274877906941
    locator_x_degree: int = 549755813887
    domain_rows: int = 824633720830
    source_classes: int = 3
    split_rank_floor: int = 61083979322


def replay(formula: Formula) -> dict[str, int]:
    e = (2**39 + 1) // 3
    n = (3 * e - 7) // 2
    locator_degree = 3 * e - 2
    rows = (9 * e - 7) // 2
    rank_floor = (e + 3) // 3
    require(e == formula.official_e, "official e")
    require(e + 1 == formula.locator_rank, "locator rank")
    require(n == formula.split_x_degree, "split X-degree")
    require(locator_degree == formula.locator_x_degree, "locator X-degree")
    require(rows == formula.domain_rows, "domain rows")
    require(formula.source_classes == 3, "source class count")
    require(rows > n, "split evaluation injection")
    require(rows > locator_degree, "locator evaluation injection")
    require(rows - locator_degree == (3 * e - 3) // 2, "locator margin")
    require(rank_floor == formula.split_rank_floor, "split rank floor")
    require(3 * rank_floor >= e + 1, "rank amplification")
    require(3 * (rank_floor - 1) < e + 1, "rank floor minimality")
    return {
        "e": e,
        "rows": rows,
        "locator_degree": locator_degree,
        "rank_floor": rank_floor,
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
        "RATE_HALF_SHAPE_A_THREE_SOURCE_CLASS_RANK_AMPLIFICATION_PASS",
        f"locator_rank={result['e'] + 1}",
        f"split_rank_floor={result['rank_floor']}",
        f"evaluation_margin={result['rows'] - result['locator_degree']}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
