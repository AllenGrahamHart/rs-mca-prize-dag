#!/usr/bin/env python3
"""Verify exact phi-fiber extrema and a finite split-pencil divisor model."""

from itertools import combinations
from math import comb


def partitions(total: int, cap: int, ceiling: int | None = None):
    """Yield nonincreasing positive partitions with every part at most cap."""
    if total == 0:
        yield ()
        return
    top = min(total, cap, ceiling if ceiling is not None else cap)
    for first in range(top, 0, -1):
        for tail in partitions(total - first, cap, first):
            yield (first,) + tail


def triples(parts: tuple[int, ...]) -> int:
    return sum(parts[i] * parts[j] * parts[k]
               for i, j, k in combinations(range(len(parts)), 3))


def packed_minimum(r: int, ell: int) -> int:
    q, u = divmod(r, ell)
    return comb(q, 3) * ell**3 + comb(q, 2) * ell**2 * u


def high_fiber_minimum(r: int, ell: int) -> int:
    if r <= ell + 2:
        return r - 2
    if r <= 2 * ell:
        return ell * (r - ell - 1)
    return packed_minimum(r, ell)


checks = 0
for ell in range(1, 9):
    for r in range(1, 25):
        profiles = list(partitions(r, ell))
        values = [triples(profile) for profile in profiles]
        assert min(values) == packed_minimum(r, ell)
        checks += 1

        high_profiles = [profile for profile in profiles if len(profile) >= 3]
        if high_profiles:
            assert r >= 3
            assert min(map(triples, high_profiles)) == high_fiber_minimum(r, ell)
            checks += 1

# The cap is load-bearing: allowing one size-(ell+1) fiber lowers the claimed
# ell-capped extremum in this mutation example.
assert triples((3, 2, 2)) < packed_minimum(7, 2)
checks += 1


PRIME = 101


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % PRIME == 0:
        poly.pop()
    return [coefficient % PRIME for coefficient in poly]


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % PRIME
    return trim(out)


def scale_add(left: list[int], a: int, right: list[int], b: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += a * value
    for i, value in enumerate(right):
        out[i] += b * value
    return trim(out)


def evaluate(poly: list[int], x: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % PRIME
    return value


def remainder(dividend: list[int], divisor: list[int]) -> list[int]:
    work = trim(dividend[:])
    divisor = trim(divisor[:])
    inverse = pow(divisor[-1], -1, PRIME)
    while len(work) >= len(divisor) and work != [0]:
        shift = len(work) - len(divisor)
        factor = work[-1] * inverse % PRIME
        for i, value in enumerate(divisor):
            work[i + shift] = (work[i + shift] - factor * value) % PRIME
        trim(work)
    return trim(work)


# P=X^2+1 and Q=X+3 are coprime over F_101.  Their projective fibers have
# size at most ell=2.  A locator drawn from two fibers divides the product of
# the corresponding pencil members.
P = [1, 0, 1]
Q = [3, 1]
fibers: dict[tuple[int, int], list[int]] = {}
for x in range(PRIME):
    px, qx = evaluate(P, x), evaluate(Q, x)
    value = (px * pow(qx, -1, PRIME) % PRIME, 1) if qx else (1, 0)
    fibers.setdefault(value, []).append(x)
assert max(map(len, fibers.values())) <= 2

chosen = sorted(fibers, key=lambda value: (-len(fibers[value]), value))[:2]
assert len(chosen) == 2 and all(fibers[value] for value in chosen)
block = [x for value in chosen for x in fibers[value]]
locator = [1]
product = [1]
for x in block:
    locator = multiply(locator, [(-x) % PRIME, 1])
for a, b in chosen:
    product = multiply(product, scale_add(P, b, Q, -a))
assert remainder(product, locator) == [0]

# Omitting either occupied fiber destroys divisibility.
a, b = chosen[0]
assert remainder(scale_add(P, b, Q, -a), locator) != [0]
checks += 3

print(
    "XR_DEFICIENT_WINDOW_PHI_FIBER_SPLIT_PENCIL_ROUTER_PASS "
    f"checks={checks}"
)
