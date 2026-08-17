#!/usr/bin/env python3
"""Exact primary replay for rich-container incidence collisions."""

from math import comb


def packet(count: int):
    n, h = 1_116_048, 42_453
    incidence = count * h
    q, remainder = divmod(incidence, n)
    pair_total = remainder * comb(q + 1, 2) + (n - remainder) * comb(q, 2)
    triple_total = remainder * comb(q + 1, 3) + (n - remainder) * comb(q, 3)
    pair_floor = (pair_total + comb(count, 2) - 1) // comb(count, 2)
    triple_floor = (triple_total + comb(count, 3) - 1) // comb(count, 3)
    return incidence, q, remainder, pair_total, triple_total, pair_floor, triple_floor


full = packet(508)
typed = packet(254)
assert full == (21_566_124, 19, 361_212, 197_707_236, 1_143_217_764, 1_536, 53)
assert typed == (10_783_062, 9, 738_630, 46_825_398, 120_338_712, 1_458, 45)
assert (full[0] + 1_116_048 - 1) // 1_116_048 == 20
assert (typed[0] + 1_116_048 - 1) // 1_116_048 == 10
print("RANK11_RICH_CONTAINER_INCIDENCE_COLLISION_OK", full[-2:], typed[-2:])
