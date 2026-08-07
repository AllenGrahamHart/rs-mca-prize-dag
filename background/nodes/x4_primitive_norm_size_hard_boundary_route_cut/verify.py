#!/usr/bin/env python3
"""Exact arithmetic audit of the X4 hard-boundary norm-size route cut."""

from fractions import Fraction


def main():
    n = 1 << 41
    t_max = n // 128 - 2
    e = n // 8
    d = e - t_max - 1
    assert d > 0 and e == t_max + d + 1
    assert 4 * e * e <= n * (e + d)

    levels = list(range(40))
    n_j = [n >> j for j in levels]
    assert n_j[-1] == 4

    m_upper = sum(Fraction(t_max, 1 << (j + 1)) + Fraction(1, 2) for j in levels)
    assert m_upper < Fraction(n, 128) + 20
    p_bits_upper = 256 * m_upper
    assert p_bits_upper < 2 * n + 5120

    all_cross = sum(Fraction(a * n, 1 << (a + 1)) for a in range(1, 40))
    infinite_cross = Fraction(n, 1)
    assert all_cross < infinite_cross
    assert infinite_cross + 40 + p_bits_upper < 3 * n + 5160

    # The ceiling is increasing for A in [N/4,N/2); its left endpoint is
    # exactly (N/4) log2(N/2)=10N because N=2^41.
    assert n.bit_length() - 1 == 41
    ceiling_bits_min = (n // 4) * 40
    assert ceiling_bits_min == 10 * n
    assert 3 * n + 5160 < ceiling_bits_min

    # Finite controls for the dyadic cross-pair identity.
    for count in range(2, 20):
        partial = sum(Fraction(a, 1 << (a + 1)) for a in range(1, count))
        assert partial < 1

    print(
        "X4_PRIMITIVE_NORM_SIZE_HARD_BOUNDARY_ROUTE_CUT_PASS "
        f"N={n} d={d} lower_bits_lt={3*n+5160} ceiling_bits={ceiling_bits_min}"
    )


if __name__ == "__main__":
    main()
