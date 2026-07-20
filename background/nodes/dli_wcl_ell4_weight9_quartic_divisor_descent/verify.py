#!/usr/bin/env python3
"""Light exact checks for the WCL (4,9) quartic-divisor descent."""

from itertools import combinations

import sympy as sp


NODE = "dli_wcl_ell4_weight9_quartic_divisor_descent"


def poly_mul_mod(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] = (out[i + j] + ai * bj) % p
    return out


def poly_rem_mod(f, g, p):
    f = [x % p for x in f]
    while len(f) >= len(g):
        lead = f[-1]
        shift = len(f) - len(g)
        for j, gj in enumerate(g):
            f[shift + j] = (f[shift + j] - lead * gj) % p
        while f and f[-1] == 0:
            f.pop()
    return f or [0]


def poly_pow_y_mod(exponent, modulus, p):
    acc = [1]
    base = [0, 1]
    while exponent:
        if exponent & 1:
            acc = poly_rem_mod(poly_mul_mod(acc, base, p), modulus, p)
        base = poly_rem_mod(poly_mul_mod(base, base, p), modulus, p)
        exponent >>= 1
    return acc


def symbolic_checks():
    x, y = sp.symbols("x y")
    c0, c1, c2, c3 = sp.symbols("c0 c1 c2 c3")
    A = y**4 + c3 * y**3 + c2 * y**2 + c1 * y + c0
    F = x * A.subs(y, x**2) - 1
    G = y * A**2 - 1
    assert sp.expand(-F * F.subs(x, -x) - G.subs(y, x**2)) == 0

    # The four missing elementary coefficients force the four odd moments.
    a2, a4, a6, a8 = sp.symbols("a2 a4 a6 a8")
    elementary = {0: 1, 1: 0, 2: a2, 3: 0, 4: a4,
                  5: 0, 6: a6, 7: 0, 8: a8}
    powers = {}
    for m in range(1, 8):
        # Newton: p_m-e1 p_(m-1)+...+(-1)^(m-1)e_(m-1)p1
        #         +(-1)^m m e_m=0.
        value = 0
        for i in range(1, m):
            value += (-1) ** (i - 1) * elementary[i] * powers[m - i]
        value += (-1) ** (m - 1) * m * elementary[m]
        powers[m] = sp.expand(value)
    for m in (1, 3, 5, 7):
        assert powers[m] == 0

    assert (9 * 1593 - 1) % 2048 == 0
    assert (9 * 1592 - 1) % 2048 != 0


def positive_control():
    # Over F_19, A=Y^4 gives G=Y^9-1. Its nine roots are the order-nine
    # subgroup and have all four required odd moments zero. This checks the
    # converse algebra and catches either sign in G.
    p = 19
    roots = [pow(4, i, p) for i in range(9)]  # 4 has order 9 modulo 19.
    assert len(set(roots)) == 9
    for m in (1, 3, 5, 7):
        assert sum(pow(r, m, p) for r in roots) % p == 0
    assert sp.prod(roots) % p == 1
    reconstructed = []
    for y in roots:
        A_y = pow(y, 4, p)
        rho = pow(A_y, -1, p)
        assert rho * rho % p == y
        reconstructed.append(rho)
    assert set(reconstructed) == set(roots)


def official_shape_checks():
    # Numerical repeated-squaring checks exercise the nine-dimensional
    # quotient endpoint without constructing symbolic official coefficients.
    p = 65537
    cases = [
        [1, 2, 3, 4, 1],
        [7, 0, 5, 9, 1],
        [p - 1, 1, 0, 2, 1],
    ]
    residues = []
    for A in cases:
        square = poly_mul_mod(A, A, p)
        G = [p - 1] + [0] * 9
        for i, value in enumerate(square):
            G[i + 1] = value
        assert len(G) == 10 and G[-1] == 1
        rem = poly_pow_y_mod(1024, G, p)
        rem[0] = (rem[0] - 1) % p
        residues.append(tuple(rem))
        assert len(rem) <= 9
    assert len(set(residues)) == len(cases)

    # The exact toy divisor A=Y^4, G=Y^9-1 is recognized at exponent 9,
    # while changing the exponent is detected.
    G = [p - 1] + [0] * 8 + [1]
    assert poly_pow_y_mod(9, G, p) == [1]
    assert poly_pow_y_mod(8, G, p) != [1]


def small_order_no_hit_crosscheck():
    # Complete N=16 divisor-side census over F_17. It is deliberately tiny
    # and is a verifier cross-check only, not evidence for the official row.
    p = 17
    roots = [pow(3, i, p) for i in range(16)]
    hits = 0
    inv2 = pow(2, -1, p)
    for indices in combinations(range(16), 9):
        G = [1]
        for i in indices:
            G = poly_mul_mod(G, [(-roots[i]) % p, 1], p)
        if G[0] != p - 1:
            continue
        h = G[1:]
        c3 = h[7] * inv2 % p
        c2 = (h[6] - c3 * c3) * inv2 % p
        c1 = (h[5] - 2 * c3 * c2) * inv2 % p
        c0 = (h[4] - c2 * c2 - 2 * c3 * c1) * inv2 % p
        A = [c0, c1, c2, c3, 1]
        if poly_mul_mod(A, A, p) == h:
            hits += 1
    assert hits == 0


def main():
    symbolic_checks()
    positive_control()
    official_shape_checks()
    small_order_no_hit_crosscheck()
    print("DLI_WCL_ELL4_WEIGHT9_QUARTIC_DIVISOR_DESCENT_PASS "
          "symbolic=1 positive=1 quotient=3 toy_subsets=11440")


if __name__ == "__main__":
    main()
