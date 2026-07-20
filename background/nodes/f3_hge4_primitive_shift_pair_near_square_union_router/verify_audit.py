#!/usr/bin/env python3
"""Independent finite-field audit of the near-square union router."""

from __future__ import annotations

from itertools import combinations


def primitive_root(p: int) -> int:
    factors = set()
    value = p - 1
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.add(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.add(value)
    for candidate in range(2, p):
        if all(pow(candidate, (p - 1) // factor, p) != 1 for factor in factors):
            return candidate
    raise AssertionError("no primitive root")


def multiply(left: tuple[int, ...], right: tuple[int, ...], p: int) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return tuple(out)


def locator(roots: tuple[int, ...], p: int) -> tuple[int, ...]:
    poly = (1,)
    for root in roots:
        poly = multiply(poly, (1, -root % p), p)
    return poly


def evaluate(poly: tuple[int, ...], x: int, p: int) -> int:
    value = 0
    for coefficient in poly:
        value = (value * x + coefficient) % p
    return value


def centered_square(
    union_locator: tuple[int, ...], h: int, p: int
) -> tuple[tuple[int, ...], int] | None:
    inv_two = pow(2, -1, p)
    coefficients = [1]
    for degree_drop in range(1, h + 1):
        cross = sum(
            coefficients[i] * coefficients[degree_drop - i]
            for i in range(1, degree_drop)
        )
        coefficients.append(
            (union_locator[degree_drop] - cross) * inv_two % p
        )
    square = multiply(tuple(coefficients), tuple(coefficients), p)
    difference = tuple((a - b) % p for a, b in zip(square, union_locator))
    if any(difference[:-1]) or difference[-1] == 0:
        return None
    roots = [value for value in range(1, p) if value * value % p == difference[-1]]
    if len(roots) != 2:
        return None
    return tuple(coefficients), roots[0]


def translate(support: frozenset[int], shift: int, n: int) -> frozenset[int]:
    return frozenset((value + shift) % n for value in support)


def support_stabilizer(support: frozenset[int], n: int) -> tuple[int, ...]:
    return tuple(shift for shift in range(n) if translate(support, shift, n) == support)


def audit_row(
    n: int, p: int, h: int, pair_crosscheck: bool = False
) -> tuple[int, int, int, int]:
    generator = primitive_root(p)
    omega = pow(generator, (p - 1) // n, p)
    points = tuple(pow(omega, exponent, p) for exponent in range(n))
    exponent_of = {point: exponent for exponent, point in enumerate(points)}

    valid = {}
    for union_exponents in combinations(range(n), 2 * h):
        union = frozenset(union_exponents)
        data = centered_square(locator(tuple(points[i] for i in union), p), h, p)
        if data is None:
            continue
        center, d = data
        minus = list(center)
        plus = list(center)
        minus[-1] = (minus[-1] - d) % p
        plus[-1] = (plus[-1] + d) % p
        P = frozenset(exponent_of[x] for x in points if evaluate(tuple(minus), x, p) == 0)
        Q = frozenset(exponent_of[x] for x in points if evaluate(tuple(plus), x, p) == 0)
        assert len(P) == len(Q) == h and not (P & Q) and P | Q == union
        loc_p = locator(tuple(points[i] for i in P), p)
        loc_q = locator(tuple(points[i] for i in Q), p)
        assert loc_p[:-1] == loc_q[:-1] and loc_p[-1] != loc_q[-1]
        common_stabilizer = set(support_stabilizer(P, n)) & set(support_stabilizer(Q, n))
        if common_stabilizer == {0}:
            valid[union] = (P, Q)

    if pair_crosscheck:
        supports = tuple(frozenset(values) for values in combinations(range(n), h))
        locators = {
            support: locator(tuple(points[i] for i in support), p)
            for support in supports
        }
        pair_unions = set()
        for index, P in enumerate(supports):
            loc_p = locators[P]
            for Q in supports[index + 1 :]:
                if P & Q:
                    continue
                loc_q = locators[Q]
                if loc_p[:-1] != loc_q[:-1] or loc_p[-1] == loc_q[-1]:
                    continue
                common_stabilizer = set(support_stabilizer(P, n)) & set(
                    support_stabilizer(Q, n)
                )
                if common_stabilizer == {0}:
                    pair_unions.add(P | Q)
        assert pair_unions == set(valid)

    union_orbits = {}
    for union, pair in valid.items():
        key = min(tuple(sorted(translate(union, shift, n))) for shift in range(n))
        union_orbits.setdefault(key, pair)

    free = 0
    swap = 0
    for key, pair in union_orbits.items():
        union = frozenset(key)
        stab = support_stabilizer(union, n)
        if len(stab) == 1:
            free += 1
        else:
            assert stab == (0, n // 2)
            P, Q = valid[union]
            assert translate(P, n // 2, n) == Q
            swap += 1

    ordered = set()
    for P, Q in valid.values():
        for left, right in ((P, Q), (Q, P)):
            key = min(
                (tuple(sorted(translate(left, shift, n))),
                 tuple(sorted(translate(right, shift, n))))
                for shift in range(n)
            )
            ordered.add(key)

    anchored = sum(0 in union for union in valid)
    assert len(ordered) == 2 * free + swap
    assert anchored == h * len(ordered)
    return len(valid), len(ordered), free, swap


def main() -> None:
    # The h=3 control exercises the antipodal-swap stabilizer; the h=4 rows
    # exercise the theorem's retained range.
    rows = (
        (8, 17, 2, False),
        (16, 17, 3, False),
        (16, 17, 4, True),
        (16, 97, 4, False),
    )
    results = [audit_row(*row) for row in rows]
    assert any(ordered > 0 for _, ordered, _, _ in results)
    assert any(swap > 0 for _, _, _, swap in results)
    print(
        "AUDIT_F3_HGE4_PRIMITIVE_SHIFT_PAIR_NEAR_SQUARE_UNION_ROUTER_PASS "
        f"rows={len(rows)} results={results}"
    )


if __name__ == "__main__":
    main()
