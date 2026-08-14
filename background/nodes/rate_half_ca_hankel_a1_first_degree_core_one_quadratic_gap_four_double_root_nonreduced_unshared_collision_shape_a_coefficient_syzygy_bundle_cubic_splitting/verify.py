#!/usr/bin/env python3
"""Replay the official coefficient syzygy-bundle profiles."""

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
    minimum_rank: int = 61083979322
    quadratic_kernel: int = 2
    profile_one_c3: int = 61083979320
    profile_two_c3: int = 61083979319
    gram_threshold: int = 137438953472


def profile(e: int, r: int, c1: int) -> tuple[int, int, int]:
    k2 = 3 * r - (e + 1)
    return c1, k2 - 2 * c1, r - 1 - k2 + c1


def replay(formula: Formula) -> dict[str, int | tuple[int, int, int]]:
    e = (2**39 + 1) // 3
    m = e - 2
    n = (3 * e - 7) // 2
    r = (e + 3) // 3
    k2 = 3 * r - (e + 1)
    first = profile(e, r, 1)
    second = profile(e, r, 0)
    gram_threshold = (n + 2) // 2 + 1
    require(e == formula.official_e, "official e")
    require(r == formula.minimum_rank, "minimum rank")
    require(k2 == formula.quadratic_kernel, "quadratic kernel")
    require(first == (1, 0, formula.profile_one_c3), "profile one")
    require(second == (0, 2, formula.profile_two_c3), "profile two")
    require(gram_threshold == formula.gram_threshold, "Gram threshold")
    for counts in (first, second):
        c1, c2, c3 = counts
        require(c1 + c2 + c3 == r - 1, "rank count")
        require(c1 + 2 * c2 + 3 * c3 == m, "degree count")
        require(2 * c1 + c2 == k2, "section count")
    return {
        "e": e,
        "rank": r,
        "kernel": k2,
        "first": first,
        "second": second,
        "gram_threshold": gram_threshold,
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
        "RATE_HALF_SHAPE_A_COEFFICIENT_SYZYGY_BUNDLE_CUBIC_SPLITTING_PASS",
        f"rank={result['rank']}",
        f"profiles={(result['first'], result['second'])}",
        f"gram_threshold={result['gram_threshold']}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
