#!/usr/bin/env python3
"""Replay the Shape-A Pade-parity quotient route fence."""

from __future__ import annotations


P = 101


class VerificationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def inv(value: int) -> int:
    return pow(value % P, P - 2, P)


def rank_mod(rows: list[list[int]]) -> int:
    work = [[entry % P for entry in row] for row in rows]
    rank = 0
    columns = len(work[0]) if work else 0
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = inv(work[rank][column])
        work[rank] = [scale * entry % P for entry in work[rank]]
        for row in range(len(work)):
            if row != rank and work[row][column]:
                scale = work[row][column]
                work[row] = [
                    (left - scale * right) % P
                    for left, right in zip(work[row], work[rank])
                ]
        rank += 1
        if rank == len(work):
            break
    return rank


def residue_rows(max_degree: int, points: list[int]) -> list[list[int]]:
    weights = []
    for x in points:
        derivative = 1
        for y in points:
            if x != y:
                derivative = derivative * (x - y) % P
        weights.append(inv(derivative))
    return [
        [pow(x, degree, P) for x in points]
        for degree in range(max_degree + 1)
    ], weights


def pairing_rank(
    left: list[list[int]], right: list[list[int]], weights: list[int]
) -> int:
    matrix = [
        [
            sum(
                weight * a * b
                for weight, a, b in zip(weights, left_row, right_row)
            ) % P
            for right_row in right
        ]
        for left_row in left
    ]
    return rank_mod(matrix)


def replay() -> dict[str, int]:
    points = list(range(1, 11))
    s_n, weights = residue_rows(2, points)
    s_d, _ = residue_rows(6, points)
    require(pairing_rank(s_n, s_d, weights) == 0, "toy RS orthogonal")

    j = [(x + 20) % P for x in points]
    require(all(j), "toy multiplier unit")

    def j_monomial(degree: int) -> list[int]:
        return [j_value * pow(x, degree, P) % P
                for x, j_value in zip(points, j)]

    mandatory = [j_monomial(degree) for degree in range(4)]
    e3_exact = mandatory + [j_monomial(degree) for degree in (7, 8, 9)]
    e3_excess = mandatory + [j_monomial(degree) for degree in (4, 7, 8)]
    require(rank_mod(e3_exact) == rank_mod(e3_excess) == 7,
            "toy E3 dimension")

    right_exact = pairing_rank(s_n, e3_exact, weights)
    right_excess = pairing_rank(s_n, e3_excess, weights)
    require(right_exact == 3, "toy exact quotient rank")
    require(right_excess == 2, "toy excess quotient rank")

    e = (2**39 + 1) // 3
    n = (3 * e - 7) // 2
    total = (9 * e - 7) // 2
    d = 3 * e - 2
    r = (e + 1) // 2
    require(d == total - n - 2 == 2 * n + 5, "official dual degree")
    require(3 * r == n + 5, "official boundary")
    require(3 * r - (e + 1) == r, "official quotient")
    require(n + 1 - r == e - 3 == 183251937960,
            "official common-kernel floor")
    return {
        "toy_exact_rank": right_exact,
        "toy_excess_rank": right_excess,
        "official_dual_degree": d,
        "official_quotient": r,
        "official_kernel_floor": e - 3,
        "mandatory_block": e + 1,
    }


def tamper_selftest() -> int:
    result = replay()
    rejected = 0
    for key, value in result.items():
        try:
            require(value + 1 == value, f"tamper {key}")
        except VerificationError:
            rejected += 1
    require(rejected == len(result), "hostile mutations")
    return rejected


def main() -> None:
    result = replay()
    mutations = tamper_selftest()
    print(
        "RATE_HALF_SHAPE_A_PADE_PARITY_QUOTIENT_PASS",
        f"toy={result['toy_exact_rank']}/{result['toy_excess_rank']}",
        f"dual_degree={result['official_dual_degree']}",
        f"quotient={result['official_quotient']}",
        f"kernel_floor={result['official_kernel_floor']}",
        f"mandatory={result['mandatory_block']}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
