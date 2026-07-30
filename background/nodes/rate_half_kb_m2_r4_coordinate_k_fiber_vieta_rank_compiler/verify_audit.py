#!/usr/bin/env python3
"""Independent rational audit of the coordinate K-fiber Vieta gates."""

from fractions import Fraction


def evaluate_binary(coefficients: list[int], u: int, v: int) -> int:
    degree = len(coefficients) - 1
    return sum(coefficient * u ** index * v ** (degree - index)
               for index, coefficient in enumerate(coefficients))


def rank(matrix: list[list[Fraction]]) -> int:
    work = [row[:] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(pivot_row, len(work))
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [entry / scale for entry in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [left - scale * right
                         for left, right in zip(work[row], work[pivot_row])]
        pivot_row += 1
    return pivot_row


def main() -> None:
    # Deck-choice invariance is independent of any coefficient model.
    for x, left, right in ((1, 2, 3), (2, -1, 4), (3, 5, -2),
                           (4, 7, 9), (5, -3, -8)):
        product = left * right
        deck_sum = x * (left + right)
        assert product == (-left) * (-right)
        assert deck_sum == (-x) * ((-left) + (-right))
    for r, s, left in ((0, 1, 3), (1, 0, 5)):
        right = -left
        assert r * s * (left + right) == 0

    positive_kappas = [(0, 1), (1, 0), (1, 1), (4, 1), (9, 1)]
    a2, a0, b1 = [3, 5, 7], [11, 13, 17], [19, 23]
    positive = []
    positive_q = []
    for u, v in positive_kappas:
        lead = evaluate_binary(a2, u, v)
        product = Fraction(evaluate_binary(a0, u, v), lead)
        deck_sum = Fraction(-u * v * evaluate_binary(b1, u, v), lead)
        v2 = [v * v, u * v, u * u]
        positive.extend((
            [-product * value for value in v2] + v2 + [0, 0],
            [deck_sum * value for value in v2]
            + [0, 0, 0, u * v * v, u * u * v],
        ))
        positive_q.append([
            deck_sum * v * v, deck_sum * u * v, deck_sum * u * u,
            u * v * v, u * u * v,
        ])
    assert rank(positive) <= 7
    assert rank(positive_q) <= 4

    kappas = [1, 4, 9, 16, 25]
    b2, b0, a1 = [3, 5], [7, 11], [13, 17, 19]
    negative = []
    negative_p = []
    negative_q = []
    for kappa in kappas:
        lead = evaluate_binary(b2, kappa, 1)
        product = Fraction(evaluate_binary(b0, kappa, 1), lead)
        deck_sum = Fraction(-evaluate_binary(a1, kappa, 1), lead)
        v1 = [1, kappa]
        v2 = [1, kappa, kappa * kappa]
        negative.extend((
            [-product * value for value in v1] + v1 + [0, 0, 0],
            [deck_sum * value for value in v1] + [0, 0] + v2,
        ))
        negative_p.append([-product, -product * kappa, 1, kappa])
        negative_q.append([
            deck_sum, deck_sum * kappa, 1, kappa, kappa * kappa,
        ])
    assert rank(negative) <= 6
    assert rank(negative_p) <= 3
    assert rank(negative_q) <= 4
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_K_FIBER_VIETA_RANK_COMPILER_"
        "AUDIT_PASS deck_checks=5 rational_rank_gates=5"
    )


if __name__ == "__main__":
    main()
