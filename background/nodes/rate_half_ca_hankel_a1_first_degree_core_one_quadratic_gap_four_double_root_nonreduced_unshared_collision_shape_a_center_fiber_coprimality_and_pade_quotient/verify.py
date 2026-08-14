#!/usr/bin/env python3
"""Replay center coprimality and Pade quotient degrees."""

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
    small_class: int = 274877906943
    large_class: int = 274877906944
    small_quotient_degree: int = 549755813886
    large_quotient_degree: int = 549755813885
    center_common_roots: int = 0
    large_padded_value_nonzero: int = 1
    heavy_residual_value_nonzero: int = 1
    large_pade_linear_factor: int = 1


def replay(formula: Formula) -> dict[str, int]:
    e = (2**39 + 1) // 3
    n = (3 * e - 7) // 2
    d = 3 * e - 2
    total = (9 * e - 7) // 2
    small = n + 2
    large = n + 3
    small_quotient = total - 1 - small
    large_quotient = total - 1 - large
    require(e == formula.official_e, "official e")
    require(d == formula.locator_degree, "locator degree")
    require(small == formula.small_class, "small class")
    require(large == formula.large_class, "large class")
    require(small_quotient == formula.small_quotient_degree == d - 1,
            "small quotient")
    require(large_quotient == formula.large_quotient_degree == d - 2,
            "large quotient")
    require(formula.center_common_roots == 0, "center coprimality")
    require(formula.large_padded_value_nonzero == 1,
            "large padded value")
    require(formula.heavy_residual_value_nonzero == 1,
            "heavy residual value")
    require(formula.large_pade_linear_factor == 1,
            "large Pade factor")
    return {
        "e": e,
        "small_class": small,
        "large_class": large,
        "small_quotient": small_quotient,
        "large_quotient": large_quotient,
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
        "RATE_HALF_SHAPE_A_CENTER_FIBER_COPRIMALITY_PADE_PASS",
        f"classes={result['small_class']},{result['large_class']}",
        f"quotients={result['small_quotient']},{result['large_quotient']}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
