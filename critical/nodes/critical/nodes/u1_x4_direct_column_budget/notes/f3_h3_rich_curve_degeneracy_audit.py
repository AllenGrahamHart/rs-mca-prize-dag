#!/usr/bin/env python3
"""Exact checks for the h=3 rich-curve degeneracy audit."""

from __future__ import annotations


CASES = (
    (97, 16),
    (193, 32),
    (257, 64),
    (769, 256),
)


def subgroup(p: int, h: int) -> set[int]:
    if (p - 1) % h != 0:
        raise ValueError((p, h))
    return {pow(x, (p - 1) // h, p) for x in range(1, p)}


def collapsed_count(p: int, h: int) -> tuple[int, tuple[int, int, int]]:
    hset = subgroup(p, h)
    constants = sorted(hset)
    coeffs = (constants[0], constants[1], constants[-1])
    count = 0
    for x in range(p):
        if all((c * x) % p in hset for c in coeffs):
            count += 1
    return count, coeffs


def shifted_count(p: int, h: int) -> int:
    """A non-collapsed comparison row: X, X+1, X+2 all in H."""

    hset = subgroup(p, h)
    count = 0
    for x in range(p):
        if x in hset and (x + 1) % p in hset and (x + 2) % p in hset:
            count += 1
    return count


def main() -> None:
    print(" p     h  collapsed_T  shifted_comparison  constants")
    for p, h in CASES:
        count, coeffs = collapsed_count(p, h)
        shifted = shifted_count(p, h)
        if count != h:
            raise AssertionError((p, h, count))
        print(f"{p:4d} {h:5d} {count:12d} {shifted:19d}  {coeffs}")
    print("collapsed family has T=h for every checked row")
    print("H3_RICH_CURVE_DEGENERACY_AUDIT_PASS")


if __name__ == "__main__":
    main()
