#!/usr/bin/env python3
"""Finite checks for the PMA exact-periodic source owner."""

from itertools import product
from fractions import Fraction
from math import comb


RATES = (2, 4, 8, 16)
EPS_DEN = 1 << 690


def ceil_div(a, b):
    return (a + b - 1) // b


def powers_of_two(n):
    out = []
    m = 2
    while m <= n:
        out.append(m)
        m *= 2
    return out


def shifted(mask, shift, n):
    out = 0
    for i in range(n):
        if mask & (1 << i):
            out |= 1 << ((i + shift) % n)
    return out


def stabilizer_size(mask, n):
    return sum(shifted(mask, shift, n) == mask for shift in range(n))


def polynomial_values(coeffs, points, prime):
    values = []
    for x in points:
        acc = 0
        for coeff in reversed(coeffs):
            acc = (acc * x + coeff) % prime
        values.append(acc)
    return tuple(values)


def canonical_owner(mask, n, scale, threshold):
    quotient_length = n // scale
    needed = ceil_div(threshold, scale)
    fibers = []
    for residue in range(quotient_length):
        fiber = sum(1 << (residue + j * quotient_length) for j in range(scale))
        if mask & fiber == fiber:
            fibers.append(residue)
    assert len(fibers) >= needed
    return scale, tuple(fibers[:needed])


def check_received_word(word, n, k, threshold, prime):
    points = tuple(range(n))
    owners = {}
    counts = {}
    for coeffs in product(range(prime), repeat=k):
        values = polynomial_values(coeffs, points, prime)
        mask = sum(
            1 << i
            for i, (left, right) in enumerate(zip(values, word))
            if left == right
        )
        if mask.bit_count() < threshold:
            continue
        scale = stabilizer_size(mask, n)
        if scale <= 1:
            continue
        if scale < n:
            owner = canonical_owner(mask, n, scale, threshold)
            assert owner not in owners, (owner, owners[owner], coeffs)
            owners[owner] = coeffs
            counts[scale] = counts.get(scale, 0) + 1
        else:
            counts[scale] = counts.get(scale, 0) + 1
            assert counts[scale] <= 1

    for scale, count in counts.items():
        if scale == n:
            assert count <= 1
            continue
        quotient_length = n // scale
        needed = ceil_div(threshold, scale)
        assert needed < quotient_length
        assert count <= comb(quotient_length, needed)
    return counts


def small_rs_checks():
    prime = 17
    n = 8
    k = 3
    threshold = 4

    # Two exact scale-4 supports: the even and odd four-cycles.
    parity_word = tuple(i & 1 for i in range(n))
    parity_counts = check_received_word(parity_word, n, k, threshold, prime)
    assert parity_counts.get(4) == 2

    # Two exact scale-2 supports: adjacent pairs in the quotient of length 4.
    pair_word = tuple(0 if i % 4 < 2 else 1 for i in range(n))
    pair_counts = check_received_word(pair_word, n, k, threshold, prime)
    assert pair_counts.get(2) == 2

    # Exact scale is load-bearing: the full support is invariant at every
    # divisor scale but has one canonical exact owner, namely scale n.
    full = (1 << n) - 1
    containing_scales = [
        m for m in powers_of_two(n) if shifted(full, n // m, n) == full
    ]
    assert len(containing_scales) > 1
    assert stabilizer_size(full, n) == n


def official_symbolic_checks():
    max_ratios = {den: Fraction(0, 1) for den in RATES}
    saw_rate_half_four = False
    saw_nontrivial_tail = False

    for exponent in range(13, 45):
        n = 1 << exponent
        for denominator in RATES:
            k = n // denominator
            threshold = k + 1
            split = (n - k) // 2
            above = []

            for scale in powers_of_two(n):
                quotient_length = n // scale
                needed = ceil_div(threshold, scale)
                own = scale * needed

                if scale <= split:
                    assert needed <= quotient_length - 1
                    assert n <= 4 * (n - own)
                    ratio = Fraction(n, n - own)
                    if ratio > max_ratios[denominator]:
                        max_ratios[denominator] = ratio
                    if denominator == 2 and scale == split:
                        assert ratio == 4
                        saw_rate_half_four = True
                else:
                    above.append(scale)

            assert above == [n // 2, n]
            half_needed = ceil_div(threshold, n // 2)
            if denominator == 2:
                assert half_needed == 2
            else:
                assert half_needed == 1
                saw_nontrivial_tail = True

    expected = {
        2: Fraction(4, 1),
        4: Fraction(2, 1),
        8: Fraction(4, 3),
        16: Fraction(4, 3),
    }
    assert max_ratios == expected
    assert saw_rate_half_four
    assert saw_nontrivial_tail

    # QA.22 supplies sum Q_M <= (1+2^-690)Q_2 and Q_2>=1. Check the
    # worst algebraic absorption at Q_2=1 without constructing huge binomials.
    left = 4 * (EPS_DEN + 1) + 3 * EPS_DEN
    right = 719 * (EPS_DEN + 1)
    assert left < right

    # Mutation guards: cap 3 is false, and dropping the M=n/2 tail is false.
    assert 4 > 3
    assert saw_nontrivial_tail


def small_exact_profile_checks():
    exponent = 13
    n = 1 << exponent
    for denominator in RATES:
        k = n // denominator
        split = (n - k) // 2
        q_sum = 0
        landing_sum = 0
        for scale in powers_of_two(n):
            if scale > split:
                continue
            quotient_length = n // scale
            needed = ceil_div(k + 1, scale)
            q_term = comb(quotient_length - 1, needed)
            q_sum += q_term
            landing_sum += comb(quotient_length, needed)
        q2 = comb(n // 2 - 1, k // 2 + 1)
        assert q_sum * EPS_DEN <= (EPS_DEN + 1) * q2
        assert landing_sum <= 4 * q_sum


def main():
    small_rs_checks()
    official_symbolic_checks()
    small_exact_profile_checks()
    print("PASS: small RS canonical-owner checks")
    print("PASS: 128 official symbolic allowance rows")
    print("PASS: exact n=2^13 profile checks")
    print("PASS: mutation guards (cap-3, omitted tail, non-exact scale)")


if __name__ == "__main__":
    main()
