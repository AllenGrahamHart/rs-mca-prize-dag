#!/usr/bin/env python3
"""Exhaust the canonical d=4 path normal form on mu_16(F_97)."""

from __future__ import annotations

import json
from itertools import combinations


P = 97
GENERATOR = pow(5, 6, P)
DOMAIN = frozenset(pow(GENERATOR, exponent, P) for exponent in range(16))


def locator(roots: tuple[int, ...] | frozenset[int]) -> tuple[int, ...]:
    answer = [1]
    for root in roots:
        product = [0] * (len(answer) + 1)
        for index, coefficient in enumerate(answer):
            product[index] = (product[index] - root * coefficient) % P
            product[index + 1] = (product[index + 1] + coefficient) % P
        answer = product
    return tuple(answer)


def affine(left: tuple[int, ...], right: tuple[int, ...], scalar: int) -> tuple[int, ...]:
    return tuple((a + scalar * (b - a)) % P for a, b in zip(left, right, strict=True))


def main() -> None:
    assert len(DOMAIN) == 16
    locators = {
        degree: {locator(subset): frozenset(subset) for subset in combinations(DOMAIN, degree)}
        for degree in (3, 4)
    }
    triples = tuple(locators[3].items())
    second_pencils = 0
    assignments = 0
    witnesses: list[dict[str, object]] = []

    for a0, t0 in triples:
        for a1, t1 in triples:
            if t0 & t1:
                continue
            for first_scalar in range(2, P):
                t3 = locators[3].get(affine(a0, a1, first_scalar))
                if t3 is None or t3 & (t0 | t1):
                    continue
                second_pencils += 1
                remaining = DOMAIN - (t0 | t1 | t3)
                for r in remaining:
                    for s in remaining - {r}:
                        p0 = locator(tuple(t0) + (s,))
                        p1 = locator(tuple(t1) + (r,))
                        for second_scalar in range(2, P):
                            assignments += 1
                            t2 = locators[4].get(affine(p0, p1, second_scalar))
                            if t2 is None or not t2 <= remaining - {r, s}:
                                continue
                            leftover = remaining - t2 - {r, s}
                            if len(leftover) == 1:
                                witnesses.append(
                                    {
                                        "T0": sorted(t0),
                                        "T1": sorted(t1),
                                        "T2": sorted(t2),
                                        "T3": sorted(t3),
                                        "r": r,
                                        "s": s,
                                        "w": next(iter(leftover)),
                                    }
                                )

    print(
        json.dumps(
            {
                "schema": "rate-half-list-b3-path-proper-search-v1",
                "complete": True,
                "field_prime": P,
                "domain_generator": GENERATOR,
                "domain": sorted(DOMAIN),
                "second_pencils": second_pencils,
                "path_assignments": assignments,
                "witness_count": len(witnesses),
                "witnesses": witnesses,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
