#!/usr/bin/env python3
"""Replay the primitive source-pencil degree ledger."""

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
    total_degree_before_gcd: int = 824633720829
    small_class: int = 274877906943
    large_class: int = 274877906944
    small_residual_offset: int = 549755813886
    large_residual_offset: int = 549755813885
    maximum_fixed_degree: int = 549755813885
    parameter_rank: int = 2
    center_fibers: int = 3
    relation_dimension: int = 1
    nonzero_relation_coefficients: int = 3


def replay(formula: Formula, h: int = 0) -> dict[str, int]:
    e = (2**39 + 1) // 3
    n = (3 * e - 7) // 2
    d = 3 * e - 2
    total = (9 * e - 7) // 2
    before = total - 1
    small = n + 2
    large = n + 3
    require(e == formula.official_e, "official e")
    require(before == formula.total_degree_before_gcd, "pencil degree")
    require(small == formula.small_class, "small class")
    require(large == formula.large_class, "large class")
    require(before - small == formula.small_residual_offset == d - 1,
            "small residual offset")
    require(before - large == formula.large_residual_offset == d - 2,
            "large residual offset")
    require(formula.maximum_fixed_degree == d - 2, "fixed degree cap")
    require(0 <= h <= formula.maximum_fixed_degree, "sample fixed degree")
    require(formula.parameter_rank == 2, "parameter rank")
    require(formula.center_fibers == 3, "center fibers")
    require(formula.relation_dimension == formula.center_fibers - 2,
            "relation dimension")
    require(formula.nonzero_relation_coefficients == 3,
            "relation coefficients")
    return {
        "e": e,
        "degree": before - h,
        "small_residual": d - 1 - h,
        "large_residual": d - 2 - h,
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
    boundary = replay(Formula(), Formula.maximum_fixed_degree)
    generic = replay(Formula(), 0)
    mutations = tamper_selftest()
    print(
        "RATE_HALF_SHAPE_A_PRIMITIVE_SOURCE_PENCIL_PASS",
        f"degree_range={boundary['degree']}..{generic['degree']}",
        f"generic_residuals={generic['small_residual']},{generic['large_residual']}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
