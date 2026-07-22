#!/usr/bin/env python3
"""Finite-field checks for the pair-locator Mobius dichotomy."""

from __future__ import annotations


P = 1009


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def inverse(value: int) -> int:
    return pow(value % P, P - 2, P)


def rank(rows: list[list[int]]) -> int:
    matrix = [row[:] for row in rows]
    pivot = 0
    for column in range(len(matrix[0])):
        choice = next(
            (row for row in range(pivot, len(matrix)) if matrix[row][column] % P),
            None,
        )
        if choice is None:
            continue
        matrix[pivot], matrix[choice] = matrix[choice], matrix[pivot]
        scale = inverse(matrix[pivot][column])
        matrix[pivot] = [scale * value % P for value in matrix[pivot]]
        for row in range(len(matrix)):
            if row == pivot:
                continue
            factor = matrix[row][column] % P
            if factor:
                matrix[row] = [
                    (left - factor * right) % P
                    for left, right in zip(matrix[row], matrix[pivot], strict=True)
                ]
        pivot += 1
    return pivot


def coefficients(pairs: list[tuple[int, int]]) -> list[list[int]]:
    return [[a * b % P, (-(a + b)) % P, 1] for a, b in pairs]


def phi(x: int, alpha: int, beta: int, gamma: int) -> int:
    return (gamma - alpha * x) * inverse(alpha + beta * x) % P


def involution_pairs(
    alpha: int, beta: int, gamma: int, seeds: list[int]
) -> list[tuple[int, int]]:
    require((alpha * alpha + beta * gamma) % P != 0, "singular Mobius matrix")
    pairs: list[tuple[int, int]] = []
    used: set[int] = set()
    for seed in seeds:
        mate = phi(seed, alpha, beta, gamma)
        require(seed != mate and seed not in used and mate not in used, "bad orbit seed")
        require(phi(mate, alpha, beta, gamma) == seed, "map is not an involution")
        pairs.append((seed, mate))
        used.update((seed, mate))
    return pairs


def check_relation(
    pairs: list[tuple[int, int]], alpha: int, beta: int, gamma: int
) -> None:
    for a, b in pairs:
        require(
            (beta * a * b + alpha * (a + b) - gamma) % P == 0,
            "pair misses the common Mobius relation",
        )


def main() -> None:
    antipodal = [(value, -value % P) for value in range(1, 7)]
    require(rank(coefficients(antipodal)) == 2, "antipodal locators are not rank two")
    check_relation(antipodal, alpha=1, beta=0, gamma=0)

    alpha, beta, gamma = 2, 3, 5
    fractional = involution_pairs(alpha, beta, gamma, [1, 2, 4, 7, 11])
    require(rank(coefficients(fractional)) == 2, "fractional locators are not rank two")
    check_relation(fractional, alpha, beta, gamma)

    generic = [(1, 2), (3, 5), (7, 11), (13, 17)]
    require(rank(coefficients(generic)) == 3, "generic pair family lost rank")

    mutated = fractional[:-1] + [(fractional[-1][0], 29)]
    require(rank(coefficients(mutated)) == 3, "mutation did not break the common line")

    scalar = (alpha * alpha + beta * gamma) % P
    matrix_square = (
        (alpha * alpha + beta * gamma) % P,
        (-alpha * gamma + gamma * alpha) % P,
        (-beta * alpha + alpha * beta) % P,
        (beta * gamma + alpha * alpha) % P,
    )
    require(matrix_square == (scalar, 0, 0, scalar), "trace-zero square identity failed")

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "DISTANCE_THREE_PAIR_LOCATOR_MOBIUS_DICHOTOMY_PASS "
        f"antipodal={len(antipodal)} fractional={len(fractional)} mutation=1"
    )


if __name__ == "__main__":
    main()
