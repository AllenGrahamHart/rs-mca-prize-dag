#!/usr/bin/env python3
"""Independent exhaustive toy-RS audit of the affine-flat list bound."""

from itertools import product
from math import comb


P = 3
D = (0, 1, 2)
K = 2


def word(coeffs: tuple[int, int]) -> tuple[int, ...]:
    return tuple((coeffs[0] + coeffs[1] * x) % P for x in D)


def agreement(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    return sum(x == y for x, y in zip(a, b))


def main() -> None:
    coeffs = list(product(range(P), repeat=K))
    words = {a: word(a) for a in coeffs}
    directions = [(1, t) for t in range(P)] + [(0, 1)]
    flats: set[tuple[tuple[int, int], ...]] = set()
    for v in directions:
        for a in coeffs:
            flat = tuple(sorted(((a[0] + t * v[0]) % P,
                                 (a[1] + t * v[1]) % P) for t in range(P)))
            flats.add(flat)
    flats.add(tuple(sorted(coeffs)))

    checks = 0
    for flat in flats:
        s = 2 if len(flat) == P * P else 1
        for u in product(range(P), repeat=len(D)):
            for m in range(K, len(D) + 1):
                w = m - K
                listed = sum(agreement(words[a], u) >= m for a in flat)
                bound = comb(len(D) - K + s, s) // comb(w + s, s)
                assert listed <= bound
                checks += 1
    print(f"AUDIT_UPSTREAM_GFV4_AFFINE_SPAN_LIST_COMPILER_PASS checks={checks}")


if __name__ == "__main__":
    main()
