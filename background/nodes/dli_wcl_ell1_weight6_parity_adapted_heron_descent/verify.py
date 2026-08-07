#!/usr/bin/env python3
"""Verify the WCL parity-adapted Heron field descent."""

from __future__ import annotations

import itertools

import sympy as sp


def consecutive_pairs(values):
    assert len(values) % 2 == 0
    return [(values[index], values[index + 1]) for index in range(0, len(values), 2)]


def adapted_pairing(exponents):
    even = sorted(value for value in exponents if value % 2 == 0)
    odd = sorted(value for value in exponents if value % 2 == 1)
    sector = sum(exponents) & 1
    if sector == 0:
        pairs = consecutive_pairs(even) + consecutive_pairs(odd)
    else:
        even_last = even.pop()
        odd_last = odd.pop()
        pairs = consecutive_pairs(even) + consecutive_pairs(odd)
        pairs.append((even_last, odd_last))
    return sector, tuple(sorted(tuple(sorted(pair)) for pair in pairs))


def symbolic_norm_identity():
    s, d, v, w, t = sp.symbols("s d v w t")
    u_plus = s + 2 * t
    u_minus = s - 2 * t

    def h(u):
        return u**2 + v**2 + w**2 - 2 * (u * v + u * w + v * w)

    c = s**2 + 4*d - 2*s*(v+w) + (v-w)**2
    coefficient = 4*(s-v-w)
    reduced_plus = sp.expand(sp.expand(h(u_plus)).subs(t**2, d))
    assert sp.expand(reduced_plus - (c + coefficient*t)) == 0
    product = sp.Poly(sp.expand(h(u_plus) * h(u_minus)), t)
    reduced = sum(
        coefficient_value * d ** (degree[0] // 2)
        for degree, coefficient_value in product.terms()
    )
    assert all(degree[0] % 2 == 0 for degree, coefficient_value in product.terms())
    assert sp.expand(reduced - (c**2 - d*coefficient**2)) == 0


def main():
    symbolic_norm_identity()
    patterns = 0
    even_patterns = 0
    odd_patterns = 0
    for bits in itertools.product((0, 1), repeat=6):
        exponents = tuple(2 * index + bit for index, bit in enumerate(bits))
        sector, pairs = adapted_pairing(exponents)
        mixed = sum((left + right) & 1 for left, right in pairs)
        assert len(pairs) == 3
        if sector == 0:
            assert mixed == 0
            even_patterns += 1
        else:
            assert mixed == 1
            odd_patterns += 1
        patterns += 1
    assert (patterns, even_patterns, odd_patterns) == (64, 32, 32)

    controls = 0
    for s, d, v, w in ((3, 4, 5, 7), (11, 9, -4, 9), (0, 16, 6, -8)):
        c = s*s + 4*d - 2*s*(v+w) + (v-w)**2
        coefficient = 4*(s-v-w)
        for t in range(-20, 21):
            if t*t != d:
                continue
            def h(u):
                return u*u + v*v + w*w - 2*(u*v + u*w + v*w)
            assert h(s+2*t) * h(s-2*t) == c*c - d*coefficient*coefficient
            controls += 1
    assert controls == 6

    print(
        "DLI_WCL_ELL1_WEIGHT6_PARITY_HERON_DESCENT_PASS "
        f"patterns={patterns} even={even_patterns} odd={odd_patterns} "
        f"norm_controls={controls}"
    )


if __name__ == "__main__":
    main()
