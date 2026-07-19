#!/usr/bin/env python3
"""Audit multifiber locator independence over several finite fields."""

from __future__ import annotations


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % prime
    return answer


def locator(root: int, extras: list[int], m: int, prime: int) -> list[int]:
    answer = [pow(root, m - 1 - degree, prime) for degree in range(m)]
    for value in extras:
        factor = [-value % prime] + [0] * (m - 1) + [1]
        answer = multiply(answer, factor, prime)
    return answer


def rank(rows: list[list[int]], prime: int) -> int:
    work = [row[:] for row in rows]
    answer = 0
    for column in range(len(work[0])):
        pivot = next((i for i in range(answer, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[answer], work[pivot] = work[pivot], work[answer]
        inverse = pow(work[answer][column], -1, prime)
        work[answer] = [entry * inverse % prime for entry in work[answer]]
        for row in range(len(work)):
            if row != answer and work[row][column]:
                factor = work[row][column]
                work[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(work[row], work[answer], strict=True)
                ]
        answer += 1
    return answer


def main() -> None:
    checked = 0
    for prime in (97, 193, 257, 769):
        for m in range(3, 10):
            for s in range(1, 5):
                roots = list(range(2, 2 + min(m, 5)))
                polynomials = [
                    locator(
                        root,
                        [20 + 11 * i + 7 * j for j in range(s - 1)],
                        m,
                        prime,
                    )
                    for i, root in enumerate(roots)
                ]
                rows = [
                    [polynomial[degree] for polynomial in polynomials]
                    for degree in range(m * s)
                ]
                assert rank(rows, prime) == len(roots)
                checked += 1

        repeated = [
            locator(3, [31], 4, prime),
            locator(3, [31], 4, prime),
        ]
        repeated_rows = [[polynomial[d] for polynomial in repeated] for d in range(8)]
        assert rank(repeated_rows, prime) == 1

    print(
        "AUDIT_RATE_HALF_LIST_B3_MULTIFIBER_VANDERMONDE_EXCLUSION_PASS "
        f"field_cases={checked} repeated_root_controls=4"
    )


if __name__ == "__main__":
    main()
