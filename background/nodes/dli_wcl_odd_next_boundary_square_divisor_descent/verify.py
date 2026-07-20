#!/usr/bin/env python3
"""Exact checks for the WCL odd next-boundary square-divisor descent."""

from itertools import combinations

import sympy as sp


NODE = "dli_wcl_odd_next_boundary_square_divisor_descent"


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] = (out[i + j] + ai * bj) % p
    return out


def rem(f, g, p):
    f = [x % p for x in f]
    while len(f) >= len(g):
        lead = f[-1]
        shift = len(f) - len(g)
        for j, gj in enumerate(g):
            f[shift + j] = (f[shift + j] - lead * gj) % p
        while f and f[-1] == 0:
            f.pop()
    return f or [0]


def pow_y(exponent, modulus, p):
    acc, base = [1], [0, 1]
    while exponent:
        if exponent & 1:
            acc = rem(mul(acc, base, p), modulus, p)
        base = rem(mul(base, base, p), modulus, p)
        exponent >>= 1
    return acc


def build_g(A, b, p):
    square = mul(A, A, p)
    G = [0] * (len(square) + 1)
    G[0] = p - 1
    G[1] = (square[0] - 2 * b) % p
    G[2] = (square[1] - b * b) % p
    for j in range(2, len(square)):
        G[j + 1] = square[j]
    return G


def symbolic_checks():
    x, y, b = sp.symbols("x y b")
    for ell in (1, 2):
        coeffs = sp.symbols(f"c0:{ell + 1}")
        A = y ** (ell + 1) + sum(coeffs[j] * y**j
                                 for j in range(ell + 1))
        F = x * A.subs(y, x * x) - b * x * x - 1
        G = y * A * A - (b * y + 1) ** 2
        assert sp.expand(-F * F.subs(x, -x) - G.subs(y, x * x)) == 0

    assert (5 * 205 - 1) % 512 == 0
    assert (7 * 439 - 1) % 1024 == 0
    assert (5 * 204 - 1) % 512 != 0
    assert (7 * 438 - 1) % 1024 != 0


def subgroup_positive_controls():
    # A=Y^(ell+1), b=0 gives G=Y^w-1. The order-w subgroup is a
    # characteristic-p positive control for both exact converse formulas.
    controls = [(1, 5, 11, 3), (2, 7, 29, 16)]
    for ell, w, p, zeta in controls:
        ys = [pow(zeta, i, p) for i in range(w)]
        assert len(set(ys)) == w
        rhos = []
        for y in ys:
            A_y = pow(y, ell + 1, p)
            rho = pow(A_y, -1, p)
            assert rho * rho % p == y
            rhos.append(rho)
        assert set(rhos) == set(ys)
        assert sp.prod(rhos) % p == 1
        for m in range(1, 2 * ell, 2):
            assert sum(pow(r, m, p) for r in rhos) % p == 0


def official_shape_quotients():
    p = 65537
    cases = [
        (1, 256, [3, 7, 1], 11),
        (1, 256, [p - 2, 5, 1], 0),
        (2, 512, [4, 0, 9, 1], 13),
        (2, 512, [1, p - 1, 2, 1], 6),
    ]
    signatures = []
    for ell, N, A, b in cases:
        G = build_g(A, b, p)
        assert len(G) == 2 * ell + 4 and G[-1] == 1 and G[0] == p - 1
        residue = pow_y(N, G, p)
        residue[0] = (residue[0] - 1) % p
        assert len(residue) <= 2 * ell + 3
        signatures.append(tuple(residue))
    assert len(set(signatures)) == len(cases)


def recover_shape(G, ell, p):
    inv2 = pow(2, -1, p)
    if ell == 1:
        c1 = G[4] * inv2 % p
        c0 = (G[3] - c1 * c1) * inv2 % p
        A = [c0, c1, 1]
    else:
        c2 = G[6] * inv2 % p
        c1 = (G[5] - c2 * c2) * inv2 % p
        c0 = (G[4] - 2 * c2 * c1) * inv2 % p
        A = [c0, c1, c2, 1]
    b = (A[0] * A[0] - G[1]) * inv2 % p
    return A, b


def complete_toy_censuses():
    p, N = 17, 16
    roots = [pow(3, i, p) for i in range(N)]
    expected = {1: 6, 2: 0}
    totals = {}
    for ell in (1, 2):
        w = 2 * ell + 3
        hits = 0
        for indices in combinations(range(N), w):
            G = [1]
            for i in indices:
                G = mul(G, [(-roots[i]) % p, 1], p)
            if G[0] != p - 1:
                continue
            A, b = recover_shape(G, ell, p)
            if build_g(A, b, p) == G:
                hits += 1
        assert hits == expected[ell]
        totals[ell] = hits
    return totals


def main():
    symbolic_checks()
    subgroup_positive_controls()
    official_shape_quotients()
    totals = complete_toy_censuses()
    print("DLI_WCL_ODD_NEXT_BOUNDARY_SQUARE_DIVISOR_DESCENT_PASS "
          f"symbolic=2 positive=2 quotient=4 toy_hits={totals[1]},{totals[2]}")


if __name__ == "__main__":
    main()
