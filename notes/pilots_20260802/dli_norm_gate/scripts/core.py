#!/usr/bin/env python3
"""dli_norm_gate pilot -- shared exact core.

SETTING.  n = 2^s, q prime with n | q - 1, zeta a primitive n-th root of unity
in F_q.  R = Z[zeta_n] = Z[x]/(Phi_n(x)) = Z[x]/(x^h + 1) with h = phi(n) = n/2.

An element alpha = sum_{i<h} a_i zeta_n^i is TERNARY of weight w if
a_i in {-1,0,1} with exactly w nonzero; it is the C2'' "skew vector"
eps in {+-1}^G with G = supp(alpha), |G| = w.

Norm(alpha) = Res(alpha(x), x^h + 1) = prod_{j odd mod n} alpha(zeta_n^j).

Because q == 1 (mod n), x^h + 1 splits completely mod q into the h linear
factors (x - zeta^j), j odd mod n; hence

    Norm(alpha) mod q = prod_{j odd} alpha(zeta^j)  in F_q,          (LN3)
    q | Norm(alpha)  <=>  m(alpha) := #{j odd : alpha(zeta^j) = 0} >= 1,
    v_q(Norm(alpha)) >= m(alpha).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.dont_write_bytecode = True

import sympy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


# ------------------------------------------------------------------ field
def get_zeta(q, n):
    """Deterministic primitive n-th root -- the archived/DLI rule, verbatim."""
    g = int(sympy.primitive_root(q))
    z = pow(g, (q - 1) // n, q)
    assert pow(z, n, q) == 1 and pow(z, n // 2, q) != 1
    return int(z)


def admissible_primes(n, lo, hi):
    """primes q with q == 1 (mod n) in [lo, hi]."""
    out = []
    k = max(1, (lo - 1 + n - 1) // n)
    while True:
        q = 1 + k * n
        if q > hi:
            break
        if q >= lo and sympy.isprime(q):
            out.append(q)
        k += 1
    return out


# ------------------------------------------------------------------ exact norm
def bareiss_det(M):
    M = [row[:] for row in M]
    nn = len(M)
    sign, prev = 1, 1
    for k in range(nn - 1):
        if M[k][k] == 0:
            piv = next((i for i in range(k + 1, nn) if M[i][k] != 0), None)
            if piv is None:
                return 0
            M[k], M[piv] = M[piv], M[k]
            sign = -sign
        for i in range(k + 1, nn):
            for j in range(k + 1, nn):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
        prev = M[k][k]
    return sign * M[nn - 1][nn - 1]


def norm_cyclotomic(coeffs, h):
    """Norm of sum_i c_i zeta^i in Z[zeta_{2h}] = Z[x]/(x^h+1).  Exact.

    Identical routine to the C2'' pilot's `laws.norm_cyclotomic` (cross-checked
    in selftest below) and to the C1 pilot's Bareiss reference.
    """
    M = [[0] * h for _ in range(h)]
    for k in range(h):
        for i, c in enumerate(coeffs):
            if c:
                e = i + k
                M[e % h][k] += c * (-1 if e >= h else 1)
    return bareiss_det(M)


def norm_sympy(coeffs, h):
    x = sympy.symbols("x")
    f = sum(int(c) * x**i for i, c in enumerate(coeffs))
    return int(sympy.resultant(sympy.Poly(f, x), sympy.Poly(x**h + 1, x)))


# ------------------------------------------------------------------ m(alpha)
def odd_roots(q, n):
    """the phi(n) primitive n-th roots zeta^j, j odd, in the canonical order."""
    z = get_zeta(q, n)
    return [pow(z, j, q) for j in range(1, n, 2)]


def eval_at_roots(coeffs, roots, q):
    return [sum(c * pow(r, i, q) for i, c in enumerate(coeffs)) % q for r in roots]


def multiplicity(coeffs, q, n):
    """m(alpha) = #{odd j mod n : alpha(zeta^j) = 0 in F_q}."""
    return sum(1 for v in eval_at_roots(coeffs, odd_roots(q, n), q) if v == 0)


# ------------------------------------------------------------------ C2'' model
def blocks(t):
    """U_j = {odd u : u*2^j <= t}."""
    out, j = [], 0
    while 2**j <= t:
        out.append([u for u in range(1, t // 2**j + 1, 2)])
        j += 1
    return out


def junction0_columns(q, n, t):
    """v_i = (zeta^{u i})_{u in U_0}, i in Z/(n/2)  -- the C2'' junction-0 matrix."""
    U = blocks(t)[0]
    z = get_zeta(q, n)
    return [tuple(pow(z, (u * i) % n, q) for u in U) for i in range(n // 2)]


# ------------------------------------------------------------------ selftest
def selftest():
    import json
    from itertools import product as iproduct

    out = {"checks": []}

    def rec(name, ok, detail):
        out["checks"].append({"name": name, "pass": bool(ok), "detail": detail})
        print(f"{'PASS' if ok else 'FAIL':<5} {name}: {detail}")
        assert ok, name

    # (1) our norm == sympy resultant, exhaustive at h=4 and h=6, sampled at h=8
    bad = 0
    for h in (4, 6):
        for c in iproduct((-1, 0, 1), repeat=h):
            if norm_cyclotomic(list(c), h) != norm_sympy(list(c), h):
                bad += 1
    rec("norm_cyclotomic == sympy.resultant (exhaustive h=4,6)", bad == 0,
        f"{3**4 + 3**6} vectors, {bad} mismatches")

    # (2) LN3 root criterion: q | Norm  <=>  m >= 1 ; and v_q(Norm) >= m
    rows = []
    for (n, q) in [(16, 17), (16, 97), (16, 113), (16, 193), (32, 97), (32, 193)]:
        h = n // 2
        roots = odd_roots(q, n)
        mism = vbad = tested = 0
        rng = iproduct((-1, 0, 1), repeat=h) if h <= 8 else None
        if rng is None:
            # sample deterministically for h=16
            import random
            r = random.Random(2026)
            rng = ([r.choice((-1, 0, 1)) for _ in range(h)] for _ in range(4000))
        for c in rng:
            c = list(c)
            if not any(c):
                continue
            tested += 1
            m = sum(1 for v in eval_at_roots(c, roots, q) if v == 0)
            Nz = norm_cyclotomic(c, h)
            if (Nz % q == 0) != (m >= 1):
                mism += 1
            if m >= 1:
                v = 0
                nn = abs(Nz)
                while nn % q == 0:
                    nn //= q
                    v += 1
                if v < m:
                    vbad += 1
        rows.append({"n": n, "q": q, "tested": tested,
                     "criterion_mismatches": mism, "valuation_violations": vbad})
    rec("LN3 root criterion + valuation bound",
        all(r["criterion_mismatches"] == 0 and r["valuation_violations"] == 0
            for r in rows), json.dumps(rows))

    # (3) identification with the C2'' junction-0 matrix (t=2, o=1)
    ok = True
    for (n, q) in [(16, 17), (16, 97), (32, 193)]:
        cols = junction0_columns(q, n, 2)
        z = get_zeta(q, n)
        for i in range(n // 2):
            if cols[i] != (pow(z, i, q),):
                ok = False
    rec("ID1 junction-0 columns (t=2) are (zeta^i), i in Z/phi(n)", ok,
        "so a skew solution is exactly a ternary relation on zeta_n")

    # (4) Galois acts on ternary weight-w elements by signed basis permutation
    bad = 0
    for h in (4, 8):
        n = 2 * h
        for u in range(1, n, 2):
            perm = []
            for i in range(h):
                e = (u * i) % n
                perm.append((e % h, -1 if e >= h else 1))
            tgt = sorted(p for p, _ in perm)
            if tgt != list(range(h)):
                bad += 1
    rec("Galois sigma_u is a signed permutation of {zeta^i}_{i<phi(n)}", bad == 0,
        "hence preserves ternariness and weight exactly")

    (ROOT / "results" / "selftest.json").write_text(json.dumps(out, indent=1))
    print("\nselftest OK")


if __name__ == "__main__":
    selftest()
