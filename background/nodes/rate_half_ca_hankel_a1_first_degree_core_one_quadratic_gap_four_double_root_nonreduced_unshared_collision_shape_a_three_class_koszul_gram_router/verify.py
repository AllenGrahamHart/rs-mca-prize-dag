#!/usr/bin/env python3
"""Replay the official three-class Koszul/Gram arithmetic."""

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
    p: int = 274877906944
    rank_floor: int = 61083979322
    minimum_kernel: int = 2
    gram_nonzero_threshold: int = 137438953472
    class_small: int = 274877906943
    class_large: int = 274877906944


def replay(formula: Formula) -> dict[str, int]:
    e = (2**39 + 1) // 3
    n = (3 * e - 7) // 2
    p = n + 3
    rank_floor = (e + 3) // 3
    minimum_kernel = 3 * rank_floor - (e + 1)
    threshold = (n + 2) // 2 + 1
    require(e == formula.official_e, "official e")
    require(n == formula.n, "n")
    require(p == formula.p, "p")
    require(rank_floor == formula.rank_floor, "rank floor")
    require(minimum_kernel == formula.minimum_kernel, "minimum kernel")
    require(threshold == formula.gram_nonzero_threshold, "Gram threshold")
    require(p - 1 == formula.class_small, "small class")
    require(p == formula.class_large, "large class")
    require(p - 1 == n + 2, "class evaluation margin")
    require(2 * (threshold - 1) <= n + 2, "threshold predecessor")
    require(2 * threshold > n + 2, "threshold strictness")
    return {
        "e": e,
        "n": n,
        "rank_floor": rank_floor,
        "minimum_kernel": minimum_kernel,
        "threshold": threshold,
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
        "RATE_HALF_SHAPE_A_THREE_CLASS_KOSZUL_GRAM_PASS",
        f"rank_floor={result['rank_floor']}",
        f"kernel_min={result['minimum_kernel']}",
        f"gram_nonzero_from={result['threshold']}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
