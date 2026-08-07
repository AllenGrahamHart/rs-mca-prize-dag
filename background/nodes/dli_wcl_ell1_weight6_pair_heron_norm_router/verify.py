#!/usr/bin/env python3
"""Verify the WCL weight-six pair-Heron factorization."""

from __future__ import annotations

import itertools

import sympy as sp


def heron(u, v, w, cross=-2):
    return u * u + v * v + w * w + cross * (u * v + u * w + v * w)


def matchings(labels: tuple[int, ...]):
    if not labels:
        yield ()
        return
    first = labels[0]
    for index in range(1, len(labels)):
        second = labels[index]
        rest = labels[1:index] + labels[index + 1 :]
        for tail in matchings(rest):
            yield ((first, second),) + tail


def normalized_signs(pairing):
    rows = set()
    for tau in itertools.product((-1, 1), repeat=3):
        for delta2, delta3 in itertools.product((-1, 1), repeat=2):
            signs = [0] * 6
            external = (1, delta2, delta3)
            for pair_index, (left, right) in enumerate(pairing):
                signs[left] = external[pair_index]
                signs[right] = external[pair_index] * tau[pair_index]
            rows.add(tuple(signs))
    return rows


def direct_product(roots, anchor, modulus=None):
    value = 1
    for tail in itertools.product((-1, 1), repeat=5):
        signs = []
        offset = 0
        for index in range(6):
            if index == anchor:
                signs.append(1)
            else:
                signs.append(tail[offset])
                offset += 1
        factor = sum(sign * root for sign, root in zip(signs, roots))
        value *= factor
        if modulus is not None:
            value %= modulus
    return value


def grouped_product(roots, pairing, modulus=None, cross=-2):
    value = 1
    for tau in itertools.product((-1, 1), repeat=3):
        pair_squares = []
        for pair_index, (left, right) in enumerate(pairing):
            pair_sum = roots[left] + tau[pair_index] * roots[right]
            pair_squares.append(pair_sum * pair_sum)
        value *= heron(*pair_squares, cross=cross)
        if modulus is not None:
            value %= modulus
    return value


def symbolic_identity():
    a, b, c = sp.symbols("a b c")
    factors = (a + b + c) * (a + b - c) * (a - b + c) * (a - b - c)
    assert sp.expand(factors - heron(a * a, b * b, c * c)) == 0

    r = sp.symbols("r1:7")
    pairing = ((0, 1), (2, 3), (4, 5))
    for tau in itertools.product((-1, 1), repeat=3):
        a = r[0] + tau[0] * r[1]
        b = r[2] + tau[1] * r[3]
        c = r[4] + tau[2] * r[5]
        external = (a + b + c) * (a + b - c) * (a - b + c) * (a - b - c)
        assert sp.expand(external - heron(a * a, b * b, c * c)) == 0


def main():
    symbolic_identity()
    pairing_rows = list(matchings(tuple(range(6))))
    assert len(pairing_rows) == 15 and len(set(pairing_rows)) == 15

    roots = (1, 3, 7, 12, 20, 31)
    mutations = 0
    for pairing in pairing_rows:
        anchor = pairing[0][0]
        expected_signs = {
            tuple(1 if index == anchor else tail[index - (index > anchor)]
                  for index in range(6))
            for tail in itertools.product((-1, 1), repeat=5)
        }
        assert normalized_signs(pairing) == expected_signs
        direct = direct_product(roots, anchor)
        assert grouped_product(roots, pairing) == direct
        if grouped_product(roots, pairing, cross=-1) != direct:
            mutations += 1
    assert mutations == 15

    p, omega = 97, 28
    exponents = (0, 1, 2, 3, 4, 8)
    signs = (1, -1, 1, 1, 1, 1)
    relation = tuple(
        sign * pow(omega, exponent, p) % p
        for exponent, sign in zip(exponents, signs)
    )
    assert sum(relation) % p == 0
    for pairing in pairing_rows:
        anchor = pairing[0][0]
        assert direct_product(relation, anchor, p) == 0
        assert grouped_product(relation, pairing, p) == 0

    print(
        "DLI_WCL_ELL1_WEIGHT6_PAIR_HERON_ROUTER_PASS "
        f"pairings={len(pairing_rows)} sign_classes=32 heron_factors=8 "
        f"mutations={mutations}/15"
    )


if __name__ == "__main__":
    main()
