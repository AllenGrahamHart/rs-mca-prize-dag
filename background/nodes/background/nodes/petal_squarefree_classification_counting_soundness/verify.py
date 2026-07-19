#!/usr/bin/env python3
"""Small check for finite-union polynomial counting."""

from __future__ import annotations


def union_bound(classes, n: int) -> int:
    return sum(c * (n**a) for c, a in classes)


def combined_bound(classes, n: int) -> int:
    exponent = max(a for _, a in classes)
    constant = sum(c for c, _ in classes)
    return constant * (n**exponent)


def main() -> None:
    examples = [
        [(2, 3), (5, 1), (7, 3)],
        [(1, 0), (4, 2), (9, 1), (3, 4)],
    ]
    for classes in examples:
        for n in (1, 2, 17, 101):
            assert union_bound(classes, n) <= combined_bound(classes, n)
    print("PASS: finite classified polynomial families have polynomial union")


if __name__ == "__main__":
    main()
