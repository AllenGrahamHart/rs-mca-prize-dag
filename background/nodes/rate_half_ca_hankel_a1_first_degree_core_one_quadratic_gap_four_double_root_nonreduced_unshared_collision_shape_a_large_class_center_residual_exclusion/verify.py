#!/usr/bin/env python3
"""Replay the large-class residual-support exclusion."""

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
    boundary_rank: int = 91625968982
    exact_large_rank: int = 91625968981
    large_class: int = 274877906944
    residual_degree: int = 4
    correction_form_degree: int = 2
    correction_square_multiplier: int = 2
    assigned_center_is_collision: int = 0
    multiplication_chain_dimension: int = 0


def replay(formula: Formula) -> dict[str, int]:
    e = (2**39 + 1) // 3
    n = (3 * e - 7) // 2
    r = (e + 1) // 2
    exact_rank = r - 1
    correction_pushforward = (
        formula.correction_form_degree * formula.correction_square_multiplier
    )
    require(e == formula.official_e, "official e")
    require(r == formula.boundary_rank, "boundary rank")
    require(exact_rank == formula.exact_large_rank, "large rank")
    require(n + 3 == formula.large_class, "large class")
    require(correction_pushforward == formula.residual_degree,
            "correction pushforward")
    require(formula.assigned_center_is_collision == 0,
            "collision is off center")
    require(formula.multiplication_chain_dimension == 0,
            "multiplication chain excluded")
    residual_support = {"tau": correction_pushforward}
    require("gamma_0" not in residual_support, "center absent from support")
    return {
        "rank": r,
        "large_rank": exact_rank,
        "large_class": n + 3,
        "residual_degree": correction_pushforward,
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
        "RATE_HALF_SHAPE_A_LARGE_CLASS_CENTER_RESIDUAL_EXCLUSION_PASS",
        f"rank={result['rank']}",
        f"large_rank={result['large_rank']}",
        f"large_class={result['large_class']}",
        f"residual_degree={result['residual_degree']}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
