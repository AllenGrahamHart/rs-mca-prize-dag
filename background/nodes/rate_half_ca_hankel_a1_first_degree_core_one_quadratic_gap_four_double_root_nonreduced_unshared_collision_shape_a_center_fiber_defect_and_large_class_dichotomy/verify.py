#!/usr/bin/env python3
"""Replay the center-fiber and large-class dimension ledger."""

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
    small_class: int = 274877906943
    large_class: int = 274877906944
    locator_degree: int = 549755813887
    small_rest: int = 549755813887
    large_rest: int = 549755813886
    large_dual_dimension: int = 2
    residual_before: int = 3
    residual_after: int = 2
    small_toy_rank: int = 3
    large_toy_rank: int = 2


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[entry % prime for entry in row] for row in matrix]
    row = 0
    for col in range(len(work[0])):
        pivot = next((i for i in range(row, len(work))
                      if work[i][col]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        scale = pow(work[row][col], -1, prime)
        work[row] = [(scale * entry) % prime for entry in work[row]]
        for i in range(len(work)):
            if i != row and work[i][col]:
                factor = work[i][col]
                work[i] = [(left - factor * right) % prime
                           for left, right in zip(work[i], work[row])]
        row += 1
        if row == len(work):
            break
    return row


def dual_rs_toy(class_size: int) -> int:
    prime = 101
    n = 3
    points = list(range(1, class_size + 1))
    x_star = 17
    derivatives = []
    for x in points:
        value = 1
        for y in points:
            if y != x:
                value = value * (x - y) % prime
        derivatives.append(value)
    weights = [pow(value, -1, prime) for value in derivatives]
    forms = [
        lambda x: 1,
        lambda x: x - x_star,
        lambda x: x * x,
        lambda x: x * x * x,
    ]
    matrix = [
        [sum(weight * form(x) * pow(x, degree, prime)
             for x, weight in zip(points, weights)) % prime
         for degree in range(n + 1)]
        for form in forms
    ]
    return rank_mod(matrix, prime)


def replay(formula: Formula) -> dict[str, int]:
    e = (2**39 + 1) // 3
    n = (3 * e - 7) // 2
    d = 3 * e - 2
    total = (9 * e - 7) // 2
    r = (e + 1) // 2
    k2 = 3 * r - (e + 1)
    c1 = 2 * r - e
    projection_rank = k2 - c1
    small = n + 2
    large = n + 3
    require(e == formula.official_e, "official e")
    require(r == formula.boundary_rank, "boundary rank")
    require(projection_rank == r - 1, "coordinate projection rank")
    require(small == formula.small_class, "small class")
    require(large == formula.large_class, "large class")
    require(d == formula.locator_degree, "locator degree")
    require(total - small == formula.small_rest == d, "small rest")
    require(total - large == formula.large_rest == d - 1, "large rest")
    require(large - (n + 1) == formula.large_dual_dimension,
            "large dual dimension")
    require(formula.residual_before - 1 == formula.residual_after,
            "residual quotient")
    require(dual_rs_toy(5) == formula.small_toy_rank, "small toy rank")
    require(dual_rs_toy(6) == formula.large_toy_rank, "large toy rank")
    return {
        "e": e,
        "rank": r,
        "projection_rank": projection_rank,
        "small": small,
        "large": large,
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
        "RATE_HALF_SHAPE_A_CENTER_FIBER_LARGE_CLASS_DICHOTOMY_PASS",
        f"rank={result['rank']}",
        f"projection={result['projection_rank']}",
        f"classes={result['small']},{result['small']},{result['large']}",
        f"toy_ranks={Formula.small_toy_rank},{Formula.large_toy_rank}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
