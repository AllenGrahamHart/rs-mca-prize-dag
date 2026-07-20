#!/usr/bin/env python3
"""Independent finite construction audit for the XR support-width fence."""

from __future__ import annotations

from itertools import product


def hamming(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(x != y for x, y in zip(left, right))


def greedy_code(length: int, distance: int) -> list[tuple[int, ...]]:
    remaining = set(product((0, 1), repeat=length))
    code = []
    while remaining:
        word = min(remaining)
        code.append(word)
        remaining = {other for other in remaining if hamming(word, other) >= distance}
    return code


def main() -> None:
    length, distance = 8, 3
    code = greedy_code(length, distance)
    supports = [
        frozenset(2 * i + bit for i, bit in enumerate(word)) for word in code
    ]
    assert all(len(support) == length for support in supports)
    for i, left in enumerate(supports):
        for right in supports[i + 1 :]:
            assert len(left & right) <= length - distance
    volume = sum(__import__("math").comb(length, i) for i in range(distance))
    assert len(code) >= (2**length + volume - 1) // volume
    print(
        "AUDIT_XR_NONGENERIC_SUPPORT_ONLY_EXPONENTIAL_WIDTH_FENCE_PASS "
        f"length={length} distance={distance} codewords={len(code)}"
    )


if __name__ == "__main__":
    main()
