"""Controls C-c and claim P1 for the (1,5) sharpest-leaf pilot.

C-c: the cyclotomic-norm routine must reproduce the banked engineered
     weight-6 order-512 witness from dli_wcl_engineered_terminal_scope.
P1 : the five coefficient equations of the (1,5) fixed divisor
     G(Y) = Y*A(Y)^2 - (b*Y+1)^2,  A = Y^2 + a1*Y + a0.

Run: tools/ramguard local -- python3 notes/pilots_20260804/c1_sharpest_leaf/verify_controls.py
"""

import sys

# ---------------------------------------------------------------- norm engine
def norm_neg(coeffs, d):
    """Norm from Q(zeta_{2d}) down to Q, for an element of Z[X]/(X^d+1).

    Uses the relative norm alpha(X)*alpha(-X), which is even, then X^2 -> X.
    `coeffs` is a length-d list; returns the exact integer norm.
    """
    a = list(coeffs)
    while d > 1:
        b = [(-c if (i & 1) else c) for i, c in enumerate(a)]  # alpha(-X)
        prod = [0] * (2 * d - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    if bj:
                        prod[i + j] += ai * bj
        # reduce mod X^d + 1
        for i in range(2 * d - 2, d - 1, -1):
            if prod[i]:
                prod[i - d] -= prod[i]
                prod[i] = 0
        # product is even in X: take gamma with gamma(X^2) = prod
        assert all(prod[i] == 0 for i in range(1, d, 2)), "relative norm not even"
        a = [prod[2 * i] for i in range(d // 2)]
        d //= 2
    return a[0]


def poly_from_terms(terms, d):
    """terms: list of (sign, exponent) with exponent in [0, 2d); X^d = -1."""
    c = [0] * d
    for s, e in terms:
        e %= 2 * d
        if e >= d:
            c[e - d] -= s
        else:
            c[e] += s
    return c


def v2(n):
    n = abs(n)
    k = 0
    while n and n % 2 == 0:
        n //= 2
        k += 1
    return k


# ---------------------------------------------------------------- C-c
def control_cc():
    # 1 - z^33 + z^40 - z^136 - z^143 + z^145, z of exact order 512  ->  d = 256
    terms = [(1, 0), (-1, 33), (1, 40), (-1, 136), (-1, 143), (1, 145)]
    c = poly_from_terms(terms, 256)
    n = norm_neg(c, 256)
    banked_norm = 122312418397310579415219240127455896396372121843316076135243835573788121252866
    banked_q = 61156209198655289707609620063727948198186060921658038067621917786894060626433
    ok_norm = (n == banked_norm)
    ok_split = (n == 2 * banked_q)
    from sympy import isprime
    ok_prime = isprime(banked_q)
    ok_v2 = (v2(banked_q - 1) == 9)
    print(f"C-c  norm computed      = {n}")
    print(f"C-c  norm == banked     : {ok_norm}")
    print(f"C-c  norm == 2q         : {ok_split}")
    print(f"C-c  q prime            : {ok_prime}")
    print(f"C-c  v_2(q-1) == 9      : {ok_v2}   (actual {v2(banked_q - 1)})")
    print(f"C-c  q bit length       : {banked_q.bit_length()}")
    return ok_norm and ok_split and ok_prime and ok_v2


# ---------------------------------------------------------------- P1
def claim_p1():
    from sympy import symbols, Poly, expand, simplify
    Y, a0, a1, b = symbols("Y a0 a1 b")
    A = Y**2 + a1 * Y + a0
    G = expand(Y * A**2 - (b * Y + 1) ** 2)
    p = Poly(G, Y)
    coeffs = [p.coeff_monomial(Y**k) for k in range(6)]
    # G = Y^5 - s1 Y^4 + s2 Y^3 - s3 Y^2 + s4 Y - s5
    got = {
        "lead":      coeffs[5],
        "s1":        -coeffs[4],
        "s2":         coeffs[3],
        "s3":        -coeffs[2],
        "s4":         coeffs[1],
        "s5":        -coeffs[0],
    }
    want = {
        "lead": 1,
        "s1":  -2 * a1,
        "s2":  a1**2 + 2 * a0,
        "s3":  -(2 * a0 * a1 - b**2),
        "s4":  a0**2 - 2 * b,
        "s5":  1,
    }
    allok = True
    for k in want:
        ok = simplify(got[k] - want[k]) == 0
        allok &= bool(ok)
        print(f"P1   {k:5s}: got {got[k]}   expected {want[k]}   MATCH={ok}")
    # the derived single constraint Phi
    print()
    print("P1   derived: a1 = -s1/2, a0 = (s2 - a1^2)/2, b = (a0^2 - s4)/2,")
    print("P1   residual constraint Phi := b^2 - (s3 + 2*a0*a1) = 0  with b = (a0^2-s4)/2")
    return allok


if __name__ == "__main__":
    print("=" * 68)
    ok1 = control_cc()
    print("=" * 68)
    ok2 = claim_p1()
    print("=" * 68)
    print(f"CONTROL C-c: {'PASS' if ok1 else 'FAIL'}")
    print(f"CLAIM   P1 : {'PASS' if ok2 else 'FAIL'}")
    sys.exit(0 if (ok1 and ok2) else 1)
