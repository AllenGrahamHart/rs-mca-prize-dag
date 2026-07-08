#!/usr/bin/env python3
"""Structure checks for the banked A=[0,1,2] activation exception list."""

from __future__ import annotations

import math


N = 96

EXCEPTIONS = [
    ((3, 17, 81), 207073),
    ((3, 26, 74), 1033441),
    ((3, 51, 53), 13249),
    ((5, 17, 81), 40897),
    ((7, 17, 81), 18913),
    ((7, 55, 61), 2574433),
    ((8, 56, 63), 12289),
    ((9, 29, 77), 47137),
    ((9, 57, 65), 62017),
    ((10, 58, 67), 20929),
    ((11, 30, 78), 49537),
    ((12, 60, 71), 1857217),
    ((13, 17, 81), 30817),
    ((13, 61, 73), 244129),
    ((15, 32, 80), 26682529),
    ((15, 63, 77), 120097),
    ((16, 64, 79), 281857),
    ((17, 33, 81), 10177),
    ((17, 37, 81), 30817),
    ((17, 43, 81), 18913),
    ((17, 45, 81), 40897),
    ((17, 47, 81), 207073),
    ((17, 51, 81), 207073),
    ((17, 53, 81), 40897),
    ((17, 55, 81), 18913),
    ((17, 61, 81), 30817),
    ((17, 65, 81), 10177),
    ((17, 81, 85), 30817),
    ((17, 81, 91), 18913),
    ((17, 81, 93), 40897),
    ((17, 81, 95), 207073),
    ((18, 66, 83), 26682529),
    ((19, 34, 82), 281857),
    ((20, 68, 87), 49537),
    ((21, 35, 83), 120097),
    ((21, 69, 89), 47137),
    ((24, 72, 95), 1033441),
    ((25, 37, 85), 244129),
    ((27, 38, 86), 1857217),
    ((31, 40, 88), 20929),
    ((33, 41, 89), 62017),
    ((35, 42, 90), 12289),
    ((37, 43, 91), 2574433),
    ((45, 47, 95), 13249),
]


def is_prime(m: int) -> bool:
    if m < 2:
        return False
    for p in range(2, int(m**0.5) + 1):
        if m % p == 0:
            return False
    return True


def has_fixed_pair(b: tuple[int, int, int]) -> bool:
    return 17 in b and 81 in b


def has_antipodal_pair(b: tuple[int, int, int]) -> bool:
    s = set(b)
    return any(((x + N // 2) % N) in s for x in s)


def reflect(b: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(sorted((2 - x) % N for x in b))


def main() -> None:
    ex = dict(EXCEPTIONS)
    if len(ex) != len(EXCEPTIONS):
        raise AssertionError("duplicate exceptions")

    fixed = [b for b, _ in EXCEPTIONS if has_fixed_pair(b)]
    antipodal = [b for b, _ in EXCEPTIONS if has_antipodal_pair(b)]
    overlap = [b for b, _ in EXCEPTIONS if has_fixed_pair(b) and has_antipodal_pair(b)]
    uncovered = [
        b for b, _ in EXCEPTIONS if not (has_fixed_pair(b) or has_antipodal_pair(b))
    ]
    if uncovered:
        raise AssertionError(f"uncovered exceptions: {uncovered}")
    if (len(fixed), len(antipodal), len(overlap), len(EXCEPTIONS)) != (18, 28, 2, 44):
        raise AssertionError((len(fixed), len(antipodal), len(overlap), len(EXCEPTIONS)))

    seen = set()
    orbits = []
    for b, p in EXCEPTIONS:
        if b in seen:
            continue
        rb = reflect(b)
        if rb not in ex:
            raise AssertionError(f"reflection partner missing for {b}: {rb}")
        if ex[rb] != p:
            raise AssertionError(f"reflection prime mismatch for {b}: {p} vs {rb}: {ex[rb]}")
        seen.add(b)
        seen.add(rb)
        orbits.append((b, rb, p))
    if len(orbits) != 22:
        raise AssertionError(len(orbits))

    bad_primes = [p for _, p in EXCEPTIONS if p % N != 1 or p < N * N or not is_prime(p)]
    if bad_primes:
        raise AssertionError(bad_primes)

    print(f"total={len(EXCEPTIONS)} fixed_pair={len(fixed)} antipodal_pair={len(antipodal)} overlap={len(overlap)}")
    print(f"reflection_orbits={len(orbits)}")
    print("prime_counts:")
    counts: dict[int, int] = {}
    for _, p in EXCEPTIONS:
        counts[p] = counts.get(p, 0) + 1
    for p, count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {p}: {count}")
    print("H3_CONSECUTIVE_CORE_STRUCTURE_PASS")


if __name__ == "__main__":
    main()
