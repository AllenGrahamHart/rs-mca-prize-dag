#!/usr/bin/env python3
"""Verifier for PMA sigma-one first-layout domination."""

from itertools import product
from math import comb


def trim(poly):
    out = list(poly)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(a, b, p):
    out = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] = (out[i] + value) % p
    for i, value in enumerate(b):
        out[i] = (out[i] + value) % p
    return trim(out)


def scale(a, scalar, p):
    return trim([(scalar * value) % p for value in a])


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] = (out[i + j] + left * right) % p
    return trim(out)


def evaluate(poly, x, p):
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def locator(points, p):
    out = [1]
    for point in points:
        out = mul(out, [(-point) % p, 1], p)
    return out


def divide_exact(numerator, denominator, p):
    numerator = trim(numerator)
    denominator = trim(denominator)
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    inv_lead = pow(denominator[-1], p - 2, p)
    while len(numerator) >= len(denominator) and numerator != [0]:
        shift = len(numerator) - len(denominator)
        coefficient = numerator[-1] * inv_lead % p
        quotient[shift] = coefficient
        subtract = [0] * shift + scale(denominator, coefficient, p)
        numerator = add(numerator, scale(subtract, -1, p), p)
    assert numerator == [0]
    return trim(quotient)


def source_carriage_check():
    p, n, k = 17, 7, 3
    domain = tuple(range(n))
    core = (0, 1)
    background = 2
    petals = ((3, 4), (5, 6))
    labels = (2, 5)
    base = [2, 3, 1]
    core_locator = locator(core, p)
    anchors = [add(base, scale(core_locator, label, p), p) for label in labels]

    word = {x: evaluate(base, x, p) for x in core + (background,)}
    for petal, anchor in zip(petals, anchors):
        for x in petal:
            word[x] = evaluate(anchor, x, p)

    listed = 0
    extras = 0
    for coefficients in product(range(p), repeat=k):
        polynomial = trim(coefficients)
        agreements = {x for x in domain if evaluate(polynomial, x, p) == word[x]}
        if len(agreements) < k + 1:
            continue
        listed += 1
        if polynomial in anchors:
            continue
        extras += 1
        shifted = add(polynomial, scale(base, -1, p), p)
        core_agreements = tuple(x for x in core if x in agreements)
        missed = tuple(x for x in core if x not in agreements)
        w_poly = divide_exact(shifted, locator(core_agreements, p), p)
        assert len(w_poly) - 1 <= len(missed)
        if background in agreements:
            assert evaluate(w_poly, background, p) == 0
        missed_locator = locator(missed, p)
        for petal, label in zip(petals, labels):
            for x in petal:
                if x in agreements:
                    assert evaluate(w_poly, x, p) == label * evaluate(missed_locator, x, p) % p
    assert listed >= len(anchors) and extras > 0
    return listed, extras


def first_match(anchor_sets, universe, carry_override=None):
    groups = [[] for _ in anchor_sets]
    for item in universe:
        for index, anchors in enumerate(anchor_sets):
            carried = item not in anchors
            if carry_override is not None:
                carried = carry_override(item, index, carried)
            if carried:
                groups[index].append(item)
                break
    return groups


def combinatorial_checks():
    anchors = [
        {"a", "b", "c"},
        {"b", "c", "d"},
        {"a", "c", "e"},
        {"a", "b", "f"},
    ]
    universe = {"a", "b", "c", "d", "e", "f", "x", "y"}
    groups = first_match(anchors, universe)
    later = set().union(*map(set, groups[1:]))
    assert later <= anchors[0]
    assert sum(map(len, groups)) <= len(groups[0]) + len(anchors[0])

    def sparse_mutant(item, index, universal):
        if item == "x" and index == 0:
            return False
        return universal

    mutant = first_match(anchors, universe, sparse_mutant)
    mutant_later = set().union(*map(set, mutant[1:]))
    assert not mutant_later <= anchors[0]
    return len(universe), len(later)


def payment_checks():
    rows = 0
    for exponent in range(13, 45):
        n = 2**exponent
        for denominator in (2, 4, 8, 16):
            k = n // denominator
            length = n - k
            m = length // 2
            b_low = (k - 1) * (m + comb(length, 2) // 3)
            b_low += comb(k - 1, 2) * (
                comb(length, 2) // 3 + comb(length, 3) // 4
            )
            b_31 = comb(k - 1, 3) * (comb(length, 3) // 4)
            b_30_full = comb(k - 1, 3) * m * comb(length - 2, 2)
            paid = b_low + b_31 + b_30_full
            assert paid * 1024 < n**6
            assert (paid + m) * 1023 < n**6
            rows += 1
    return rows


def main():
    listed, extras = source_carriage_check()
    universe, later = combinatorial_checks()
    rows = payment_checks()
    print(
        "PMA_FIRST_LAYOUT_DOMINATION_PASS "
        f"source_listed={listed} source_extras={extras} "
        f"set_universe={universe} later={later} official_rows={rows} mutations=1"
    )


if __name__ == "__main__":
    main()
