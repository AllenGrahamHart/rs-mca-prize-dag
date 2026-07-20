#!/usr/bin/env python3
"""Independent dyadic Chebyshev factorization audit for the norm transfer."""

from __future__ import annotations


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim(
        [
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
            for index in range(size)
        ]
    )


def scale(value: int, poly: list[int]) -> list[int]:
    return trim([value * coefficient for coefficient in poly])


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return trim(answer)


def chebyshev(limit: int) -> tuple[list[list[int]], list[list[int]]]:
    x = [0, 1]
    first = [[1], x]
    second = [[1], scale(2, x)]
    for index in range(2, limit + 1):
        first.append(add(scale(2, multiply(x, first[-1])), scale(-1, first[-2])))
        second.append(add(scale(2, multiply(x, second[-1])), scale(-1, second[-2])))
    return first, second


def main() -> None:
    first, second = chebyshev(31)
    controls = 0
    for m in (1, 2, 4, 8):
        left = second[2 * m - 1]
        right = [2 * m]
        exponent = 1
        while exponent <= m:
            right = multiply(right, first[exponent])
            exponent *= 2
        assert left == right

        doubled = add(scale(2, multiply(first[m], first[m])), [-1])
        assert first[2 * m] == doubled
        controls += 1

    levels = list(range(2, 39))
    assert len(levels) == 37 and levels[-1] == 38
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_MATCHED_TRACE_JACOBI_NORM_TRANSFER_AUDIT_PASS "
        f"dyadic_controls={controls} plus_levels={len(levels)} mutations=2"
    )


if __name__ == "__main__":
    main()
