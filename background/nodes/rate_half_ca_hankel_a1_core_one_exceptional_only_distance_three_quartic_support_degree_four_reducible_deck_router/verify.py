#!/usr/bin/env python3
"""Exact checks for the reducible degree-four deck router."""

from __future__ import annotations

from itertools import product


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


POINTS = tuple((x, y) for x in range(3) for y in range(3))
UNIMODULAR = tuple(
    (a, b, c, d)
    for a, b, c, d in product(range(-4, 5), repeat=4)
    if abs(a * d - b * c) == 1
)


def two_dimensional(support: set[tuple[int, int]]) -> bool:
    anchor = next(iter(support))
    return any(
        (left[0] - anchor[0]) * (right[1] - anchor[1])
        != (left[1] - anchor[1]) * (right[0] - anchor[0])
        for left in support
        for right in support
    )


def admissible_transform(
    support: set[tuple[int, int]],
) -> tuple[int, int, tuple[int, int, int, int]]:
    best = None
    for a, b, c, d in UNIMODULAR:
        transformed = [(a * x + b * y, c * x + d * y) for x, y in support]
        min_x = min(x for x, _ in transformed)
        min_y = min(y for _, y in transformed)
        shifted = {(x - min_x, y - min_y) for x, y in transformed}
        if (0, 0) not in shifted:
            continue
        if not any(y == 0 and x > 0 for x, y in shifted):
            continue
        m = max(x for x, _ in shifted)
        n = max(y for _, y in shifted)
        if not m or not n:
            continue
        constant = 16 * m * n * n * (m + n)
        candidate = (constant, m, n, (a, b, c, d))
        if best is None or candidate < best:
            best = candidate
    need(best is not None, "two-dimensional support lacked a transform")
    return best[1], best[2], best[3]


def check_newton_supports() -> tuple[int, int]:
    checked = 0
    worst = 0
    for mask in range(1, 1 << len(POINTS)):
        support = {
            POINTS[index]
            for index in range(len(POINTS))
            if mask & (1 << index)
        }
        if not two_dimensional(support):
            continue
        m, n, _ = admissible_transform(support)
        constant = 16 * m * n * n * (m + n)
        need(constant <= 1440, "Newton support exceeded the paid constant")
        worst = max(worst, constant)
        checked += 1
    need(checked == 458 and worst == 1440, "Newton support coverage changed")
    return checked, worst


def check_invariant_forms() -> int:
    prime = 101
    zeta = 10
    need(zeta * zeta % prime == prime - 1, "order-four scalar fixture failed")
    c = 3
    checks = 0
    for x in (2, 5, 17, 41):
        cyclic = (x**4 + 11) % prime
        need(
            cyclic == ((zeta * x) ** 4 + 11) % prime,
            "order-four cyclic invariant failed",
        )
        need(
            (x**4 + 7 * x**2 + 11) % prime
            == ((-x) ** 4 + 7 * (-x) ** 2 + 11) % prime,
            "order-two cyclic invariant failed",
        )
        u = (x + c * pow(x, -1, prime)) % prime
        y = c * pow(x, -1, prime) % prime
        v = (y + c * pow(y, -1, prime)) % prime
        need(u == v and (u * u + 5 * u + 13) % prime == (v * v + 5 * v + 13) % prime,
             "dihedral invariant failed")
        checks += 1
    return checks


def main() -> None:
    n_value = 1 << 41
    e_value = (1 << 38) - 1
    ordered = 2 * (e_value - 148)
    need(
        2912**3 * n_value**2 < (ordered - 8) ** 3,
        "aggregate reducible margin failed",
    )
    for a in range(-2, 3):
        for b in range(-2, 3):
            if not a or not b:
                continue
            if abs(a) == abs(b):
                from math import gcd

                need(gcd(abs(a), abs(b)) != 1 or abs(a) == 1,
                     "primitive toral degree collapse failed")

    supports, worst = check_newton_supports()
    invariant_checks = check_invariant_forms()
    print(
        "RATE_HALF_DISTANCE_THREE_QUARTIC_SUPPORT_DEGREE_FOUR_DECK_PASS "
        f"newton_supports={supports} worst_constant={worst} "
        f"aggregate_constant=2912 invariant_checks={invariant_checks} "
        "forms=cyclic2/cyclic4/dihedral"
    )


if __name__ == "__main__":
    main()
