#!/usr/bin/env python3
"""Verifier for dli_norm_gate_forward_and_ofold.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Check F imports `sympy` (present in the repo environment); it is the third leg
of the norm triple check and is NOT optional -- a missing sympy fails the run.

Exact integer replay:
  A   setting sanity: q prime, q == 1 (mod n), zeta of exact order n, and
      x^h + 1 == prod_{j odd mod n} (x - zeta^j) in F_q[x]              (LN0)
  B   (Z/n)^* acts simply transitively on the odd residues mod n        (LN0)
  C   LN3 evaluation criterion  q | Norm <=> m(alpha) >= 1, and the
      valuation bound v_q(Norm) >= m(alpha)                             (LN3)
  D   LN1 forward gate: alpha(zeta) = 0 => Norm(alpha) != 0 and q | Norm
  D'  the basis-range hypothesis is LOAD-BEARING (opposite pair folds to 0)
  E   LN2 o-fold upgrade: every U-solution has q^o | Norm; banked solution
      counts at (16,17,{1,3}) and (32,97,{1,3}) reproduced exactly
  F   triple check: Bareiss determinant == sympy.resultant, and both agree
      mod q with the LN3 product of evaluations

All assertions are on exact integers.
"""
from __future__ import annotations

import sys
from itertools import combinations, product

sys.dont_write_bytecode = True

FAILURES = []


def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    if not ok:
        FAILURES.append(label)


# ----------------------------------------------------------------- arithmetic
def is_prime(m):
    if m < 2:
        return False
    d = 2
    while d * d <= m:
        if m % d == 0:
            return False
        d += 1
    return True


def prime_factors(m):
    out, d = [], 2
    while d * d <= m:
        if m % d == 0:
            out.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out


def primitive_root(q):
    fs = prime_factors(q - 1)
    for g in range(2, q):
        if all(pow(g, (q - 1) // r, q) != 1 for r in fs):
            return g
    raise AssertionError("no primitive root")


def zeta_of_order(q, n):
    """Archived/DLI deterministic rule: g^((q-1)/n) for the least primitive root."""
    z = pow(primitive_root(q), (q - 1) // n, q)
    assert pow(z, n, q) == 1 and pow(z, n // 2, q) != 1
    return z


def mult_matrix(coeffs, h):
    """Multiplication-by-alpha matrix on Z[x]/(x^h+1); column k = alpha * x^k."""
    M = [[0] * h for _ in range(h)]
    for k in range(h):
        for i, c in enumerate(coeffs):
            if c:
                e = i + k
                M[e % h][k] += c * (-1 if e >= h else 1)
    return M


def bareiss_det(M):
    a = [row[:] for row in M]
    nn = len(a)
    sign, prev = 1, 1
    for k in range(nn - 1):
        if a[k][k] == 0:
            piv = next((i for i in range(k + 1, nn) if a[i][k] != 0), None)
            if piv is None:
                return 0
            a[k], a[piv] = a[piv], a[k]
            sign = -sign
        for i in range(k + 1, nn):
            aik, akk = a[i][k], a[k][k]
            rowi, rowk = a[i], a[k]
            for j in range(k + 1, nn):
                rowi[j] = (rowi[j] * akk - aik * rowk[j]) // prev
            rowi[k] = 0
        prev = a[k][k]
    return sign * a[nn - 1][nn - 1]


def norm(coeffs, h):
    return bareiss_det(mult_matrix(coeffs, h))


def v_q(m, q):
    v, m = 0, abs(m)
    while m % q == 0:
        m //= q
        v += 1
    return v


def root_table(q, n):
    """P[k][i] = (zeta^{j_k})^i mod q, j_k = 2k+1 the h odd residues mod n."""
    h = n // 2
    z = zeta_of_order(q, n)
    return [[pow(pow(z, 2 * k + 1, q), i, q) for i in range(h)] for k in range(h)]


def zero_set(coeffs, P, q):
    return [k for k, row in enumerate(P)
            if sum(c * row[i] for i, c in enumerate(coeffs) if c) % q == 0]


def ternary(h):
    return product((-1, 0, 1), repeat=h)


def weight_vectors(h, w):
    for S in combinations(range(h), w):
        for eps in product((1, -1), repeat=w):
            v = [0] * h
            for i, e in zip(S, eps):
                v[i] = e
            yield v


# ----------------------------------------------------------------------- main
GRID = [(8, 17), (16, 17), (16, 97), (16, 113), (32, 97), (32, 193)]


def main():
    # ---------------- A: setting sanity + complete splitting of x^h+1 mod q
    ok_all, detail = True, []
    for n, q in GRID:
        h = n // 2
        z = zeta_of_order(q, n)
        ok = is_prime(q) and (q - 1) % n == 0
        ok &= pow(z, n, q) == 1 and pow(z, n // 2, q) != 1
        poly = [1]                                   # low -> high coefficients
        for j in range(1, n, 2):
            r = pow(z, j, q)
            new = [0] * (len(poly) + 1)
            for i, c in enumerate(poly):
                new[i + 1] = (new[i + 1] + c) % q
                new[i] = (new[i] - c * r) % q
            poly = new
        ok &= poly == [1] + [0] * (h - 1) + [1]
        ok_all &= ok
        detail.append(f"({n},{q})")
    check("A: q prime, q == 1 (mod n), zeta of exact order n, and x^h+1 splits "
          "into h DISTINCT linear factors mod q (LN0)", ok_all,
          "(n,q) = " + " ".join(detail))

    # ---------------- B: simple transitivity of the Galois group
    ok_all = True
    for n in (8, 16, 32, 64):
        for j in range(1, n, 2):
            for jp in range(1, n, 2):
                if sum(1 for a in range(1, n, 2) if (a * j) % n == jp) != 1:
                    ok_all = False
    check("B: (Z/n)^* acts SIMPLY TRANSITIVELY on the odd residues mod n "
          "(n = 8,16,32,64) -- the o primes of LN2 are pairwise distinct",
          ok_all, "exactly one a with a*j = j' for every ordered pair (j,j')")

    # ---------------- norm caches (Norm is q-independent)
    norms4 = {c: norm(list(c), 4) for c in ternary(4)}
    norms8 = {c: norm(list(c), 8) for c in ternary(8)}
    norms16 = {}
    for w in (1, 2, 3):
        for v in weight_vectors(16, w):
            norms16[tuple(v)] = norm(v, 16)

    # ---------------- C / D: LN3 criterion, valuation bound, LN1 forward gate
    tot = crit_bad = val_bad = tot_div = 0
    ln1_wit = ln1_bad = zero_norm = 0
    for n, q in GRID:
        h = n // 2
        P = root_table(q, n)
        cache = {4: norms4, 8: norms8, 16: norms16}[h]
        for key, Nz in cache.items():
            if not any(key):
                continue
            v = list(key)
            tot += 1
            if Nz == 0:
                zero_norm += 1
            Z = zero_set(v, P, q)
            m = len(Z)
            if (Nz % q == 0) != (m >= 1):
                crit_bad += 1
            if m >= 1:
                tot_div += 1
                if Nz == 0 or v_q(Nz, q) < m:
                    val_bad += 1
                if 0 in Z:                       # alpha(zeta^1) = 0
                    ln1_wit += 1
                    if Nz == 0 or Nz % q != 0:
                        ln1_bad += 1
    check("C: LN3 criterion  q | Norm(alpha) <=> m(alpha) >= 1  (exhaustive "
          "ternary at h=4,8; all weights 1-3 at h=16)", crit_bad == 0,
          f"{tot} (vector,prime) pairs, {crit_bad} mismatches")
    check("C: LN3 valuation bound  v_q(Norm(alpha)) >= m(alpha)", val_bad == 0,
          f"{tot_div} norm-divisible pairs, {val_bad} violations")
    check("D: LN1 forward gate  alpha(zeta) = 0  =>  Norm(alpha) != 0 and "
          "q | Norm(alpha)", ln1_bad == 0 and ln1_wit > 0,
          f"{ln1_wit} witnesses, {ln1_bad} failures")
    check("D: Norm(alpha) != 0 for EVERY nonzero vector supported in the basis "
          "range [0,h)", zero_norm == 0, f"{tot} vectors, {zero_norm} zero norms")

    # ---------------- D': the basis-range hypothesis is load-bearing
    n, q, h = 16, 97, 8
    z = zeta_of_order(q, n)
    ev = [(pow(z, 0, q) + pow(z, (8 * (2 * k + 1)) % n, q)) % q for k in range(h)]
    folded = [0] * h                    # zeta^8 = -zeta^0, so the element is 0
    check("D': basis-range hypothesis is LOAD-BEARING -- the opposite pair "
          "{0, h} annihilates every root but IS the zero element (Norm = 0), "
          "so 'q | Norm != 0' fails once the support leaves [0,h)",
          all(e == 0 for e in ev) and norm(folded, h) == 0,
          f"all {h} evaluations vanish at (n,q)=({n},{q}); Norm = 0")

    # ---------------- E: LN2 o-fold upgrade
    #  banked counts from notes/pilots_20260802/dli_norm_gate/results/
    #  splitting_n16_o.json and splitting_n32_o.json
    LN2_JOBS = [
        # (n, q, U, weights, banked #solutions per weight)
        (16, 17, (1, 3), (5, 6, 7), {5: 0, 6: 16, 7: 0}),
        (16, 17, (1, 3, 5), (6, 7, 8), {6: 0, 7: 0, 8: 0}),
        (32, 97, (1, 3), (4, 5), {4: 0, 5: 64}),
    ]
    e_bad, e_lines = 0, []
    for n, q, U, weights, banked in LN2_JOBS:
        h = n // 2
        P = root_table(q, n)
        idx = {2 * k + 1: k for k in range(h)}
        rows = [P[idx[u % n]] for u in U]
        o = len(U)
        for w in weights:
            nsol = 0
            for S in combinations(range(h), w):
                cols = [[r[i] for i in S] for r in rows]
                for eps in product((1, -1), repeat=w):
                    if any(sum(e * c for e, c in zip(eps, col)) % q for col in cols):
                        continue
                    nsol += 1
                    v = [0] * h
                    for i, e in zip(S, eps):
                        v[i] = e
                    Nz = norm(v, h)
                    m = len(zero_set(v, P, q))
                    if Nz == 0 or Nz % q**o != 0 or m < o or v_q(Nz, q) < m:
                        e_bad += 1
            if nsol != banked[w]:
                e_bad += 1
            e_lines.append(f"(n={n},q={q},U={U},w={w}): {nsol} sols")
    check("E: LN2 -- every U-solution (|U| = o) has q^o | Norm != 0 and "
          "m(alpha) >= o; banked solution counts reproduced exactly",
          e_bad == 0, "; ".join(e_lines))

    # ---------------- F: triple check
    import sympy
    x = sympy.symbols("x")

    def norm_sympy(coeffs, hh):
        f = sum(int(c) * x**i for i, c in enumerate(coeffs))
        return int(sympy.resultant(sympy.Poly(f, x), sympy.Poly(x**hh + 1, x)))

    all8 = [list(c) for c in ternary(8) if any(c)]
    sample8 = [all8[(i * 97) % len(all8)] for i in range(60)]
    w16 = list(weight_vectors(16, 3))
    sample16 = [w16[(i * 131) % len(w16)] for i in range(12)]

    bad_sy = bad_ev = 0
    P8 = root_table(97, 16)
    P16 = root_table(97, 32)
    for v, hh, P, qq in ([(v, 8, P8, 97) for v in sample8]
                         + [(v, 16, P16, 97) for v in sample16]):
        b = norm(v, hh)
        if b != norm_sympy(v, hh):
            bad_sy += 1
        prod_ev = 1
        for k in range(hh):
            prod_ev = prod_ev * sum(c * P[k][i] for i, c in enumerate(v)) % qq
        if (b - prod_ev) % qq != 0:
            bad_ev += 1
    ns = len(sample8) + len(sample16)
    check("F: triple check -- Bareiss determinant == sympy.resultant",
          bad_sy == 0, f"{ns} samples (h=8 and h=16)")
    check("F: triple check -- Norm == prod_{j odd mod n} alpha(zeta^j) (mod q), "
          "the LN3 evaluation form", bad_ev == 0,
          f"{ns} samples at (n,q) = (16,97) and (32,97)")

    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("DLI_NORM_GATE_FORWARD_AND_OFOLD_ALL_PASS")


if __name__ == "__main__":
    main()
