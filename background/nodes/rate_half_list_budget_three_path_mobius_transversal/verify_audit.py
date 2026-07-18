#!/usr/bin/env python3
"""Audit the sharp order-eight exception to the path Mobius theorem."""

from __future__ import annotations


P = 17


def multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % P
    return tuple(answer)


def locator(*roots: int) -> tuple[int, ...]:
    answer = (1,)
    for root in roots:
        answer = multiply(answer, (-root % P, 1))
    return answer


def evaluate(poly: tuple[int, ...], x: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % P
    return value


def main() -> None:
    factors = (
        locator(1, 2),
        locator(9, 4),
        locator(13, 8),
        locator(16, 15),
    )
    assert factors == ((2, 14, 1), (2, 4, 1), (2, 13, 1), (2, 3, 1))
    assert all(poly[0] == 2 and poly[2] == 1 for poly in factors)

    p0, p1, _, _ = factors
    votes = []
    for x in (15, 16):
        votes.append(evaluate(p1, x) * pow(evaluate(p0, x), -1, P) % P)
    assert votes == [14, 14]

    mutated = locator(14, 15)
    assert mutated[0] != 2
    print(
        "AUDIT_RATE_HALF_LIST_BUDGET_THREE_PATH_MOBIUS_TRANSVERSAL_PASS "
        "order8_members=4 complement_vote=14,14 mutation=1/1"
    )


if __name__ == "__main__":
    main()
