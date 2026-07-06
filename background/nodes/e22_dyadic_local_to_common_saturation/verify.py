#!/usr/bin/env python3
"""Light verifier for dyadic fiber refinement."""

from itertools import combinations


def fiber(n: int, m: int, residue: int) -> set[int]:
    step = n // m
    return {x for x in range(n) if x % step == residue % step}


def fibers(n: int, m: int) -> list[set[int]]:
    step = n // m
    return [fiber(n, m, r) for r in range(step)]


def is_union_of_fibers(n: int, m: int, points: set[int]) -> bool:
    return all(f <= points or f.isdisjoint(points) for f in fibers(n, m))


def main() -> None:
    for exponent in range(3, 8):
        n = 2**exponent
        moduli = [2**i for i in range(1, exponent + 1)]
        for i, m_min in enumerate(moduli):
            for m_big in moduli[i:]:
                for big_fiber in fibers(n, m_big):
                    assert is_union_of_fibers(n, m_min, big_fiber), (
                        n,
                        m_min,
                        m_big,
                        sorted(big_fiber),
                    )

        # Also check unions of several locally saturated blocks.
        for selected in combinations(moduli, min(3, len(moduli))):
            m_min = min(selected)
            union: set[int] = set()
            for offset, m in enumerate(selected):
                fs = fibers(n, m)
                union |= fs[offset % len(fs)]
            assert is_union_of_fibers(n, m_min, union), (n, selected, union)

    print("PASS: dyadic local saturated blocks glue to the minimum modulus")


if __name__ == "__main__":
    main()
