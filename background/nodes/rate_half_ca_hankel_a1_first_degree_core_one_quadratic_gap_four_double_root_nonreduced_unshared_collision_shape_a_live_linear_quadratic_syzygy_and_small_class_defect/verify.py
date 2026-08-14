#!/usr/bin/env python3
"""Replay the live syzygy profile and small-class defect dimensions."""

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
    boundary_c1: int = 1
    boundary_c2: int = 91625968980
    boundary_c3: int = 0
    small_class: int = 274877906943
    small_classes: int = 2


def counts(e: int, r: int) -> tuple[int, int, int]:
    return 2 * r - e, e - r - 1, 0


def replay(formula: Formula) -> dict[str, int | tuple[int, int, int]]:
    e = (2**39 + 1) // 3
    m = e - 2
    n = (3 * e - 7) // 2
    r = (e + 1) // 2
    profile = counts(e, r)
    c1, c2, c3 = profile
    k2 = 3 * r - (e + 1)
    require(e == formula.official_e, "official e")
    require(r == formula.boundary_rank, "boundary rank")
    require(profile == (formula.boundary_c1, formula.boundary_c2,
                        formula.boundary_c3), "boundary profile")
    require(n + 2 == formula.small_class, "small class")
    require(formula.small_classes == 2, "small-class count")
    require(c1 + c2 + c3 == r - 1, "profile rank")
    require(c1 + 2 * c2 + 3 * c3 == m, "profile degree")
    require(2 * c1 + c2 == k2, "profile sections")
    for sample in (r, r + 1, e - 2, e - 1):
        a, b, c = counts(e, sample)
        require(min(a, b, c) >= 0, "sample nonnegative")
        require(a + b + c == sample - 1, "sample rank")
        require(a + 2 * b + 3 * c == m, "sample degree")
    return {
        "e": e,
        "rank": r,
        "profile": profile,
        "small_class": n + 2,
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
        "RATE_HALF_SHAPE_A_LIVE_LINEAR_QUADRATIC_SYZYGY_DEFECT_PASS",
        f"rank={result['rank']}",
        f"profile={result['profile']}",
        f"small_class={result['small_class']}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
