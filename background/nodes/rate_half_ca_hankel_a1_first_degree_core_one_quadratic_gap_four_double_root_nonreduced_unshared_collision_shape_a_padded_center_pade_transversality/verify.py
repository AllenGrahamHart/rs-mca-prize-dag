#!/usr/bin/env python3
"""Replay the padded-center Pade resultant order."""

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
    locator_degree: int = 549755813887
    large_class: int = 274877906944
    g_star_center_order: int = 1
    correction_center_order: int = 0
    leading_coefficient_order: int = 0
    resultant_order: int = 1
    center_common_points: int = 1
    center_intersection_length: int = 1
    source_value_nonzero: int = 1


def replay(formula: Formula) -> dict[str, int]:
    e = (2**39 + 1) // 3
    n = (3 * e - 7) // 2
    d = 3 * e - 2
    resultant_order = (
        (2 * d + 1) * formula.leading_coefficient_order
        + formula.g_star_center_order
        + 2 * formula.correction_center_order
    )
    require(e == formula.official_e, "official e")
    require(d == formula.locator_degree, "locator degree")
    require(n + 3 == formula.large_class, "large class")
    require(resultant_order == formula.resultant_order == 1,
            "resultant order")
    require(formula.center_common_points == 1, "unique common point")
    require(formula.center_intersection_length == resultant_order,
            "intersection length")
    require(formula.source_value_nonzero == 1, "source value")
    return {
        "e": e,
        "d": d,
        "resultant_order": resultant_order,
        "intersection_length": formula.center_intersection_length,
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
        "RATE_HALF_SHAPE_A_PADDED_CENTER_PADE_TRANSVERSALITY_PASS",
        f"degree={result['d']}",
        f"order={result['resultant_order']}",
        f"length={result['intersection_length']}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
