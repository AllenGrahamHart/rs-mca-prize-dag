#!/usr/bin/env python3
"""Verifier for dli_norm_gate_energy_ceiling.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Pure python integers only; no imports beyond itertools/sys.

Exact integer replay:
  A  negacyclic Parseval as an exact integer identity: the constant
     coefficient of alpha * alpha~ mod (x^h+1) is E = sum a_i^2, and
     Tr(zeta_n^i) = 0 for 0 < i < h                                  (LN4 step)
  B  positivity and the ENERGY ceiling 1 <= Norm <= E^{h/2} for
     arbitrary integer coefficient vectors -- exhaustive and sampled
  C  per-weight maxima reproduce the banked C1 maxnorm tables at
     2N = 8, 16, 32; the AM-GM ceiling is attained exactly at the
     banked saturating weights
  D  ternariness is NOT used: non-ternary witnesses attain the ceiling
  E  LN5 junction router: the exact criterion q^o <= E^{N/2} at the
     256:1 schedule is equivalent to q <= E^128, and a real junction-0
     instance is empirically empty as the router predicts
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
def mult_matrix(coeffs, h):
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


def negacyclic_mul(a, b, h):
    out = [0] * h
    for i, ai in enumerate(a):
        if not ai:
            continue
        for j, bj in enumerate(b):
            if not bj:
                continue
            e = i + j
            out[e % h] += ai * bj * (-1 if e >= h else 1)
    return out


def conj_vector(a, h):
    """coefficients of alpha~ = sum a_i zeta^{-i}; zeta^{-i} = -zeta^{h-i}."""
    b = [0] * h
    b[0] = a[0]
    for i in range(1, h):
        b[h - i] -= a[i]
    return b


def weight_vectors(h, w):
    for S in combinations(range(h), w):
        for eps in product((1, -1), repeat=w):
            v = [0] * h
            for i, e in zip(S, eps):
                v[i] = e
            yield v


def iota(g):
    """g(y) -> g(x^2): spread coefficients onto even indices (banked Claim 1)."""
    f = [0] * (2 * len(g))
    for i, c in enumerate(g):
        f[2 * i] = c
    return f


class LCG:
    """deterministic, dependency-free pseudo-random source."""

    def __init__(self, seed):
        self.s = seed

    def randint(self, lo, hi):
        self.s = (6364136223846793005 * self.s + 1442695040888963407) % (1 << 64)
        return lo + (self.s >> 33) % (hi - lo + 1)


# --------------------------------------------------------------- banked tables
# background/nodes/dli_c1_ternary_relation_norm_sandwich/verify.py (2N = 8, 16)
# and notes/pilots_20260802/dli_norm_gate/scripts/{splitting,ladder}.py (2N = 32)
BANKED = {
    8:  {1: 1, 2: 4, 3: 9, 4: 8},
    16: {1: 1, 2: 16, 3: 81, 4: 196, 5: 529, 6: 1154, 7: 2401, 8: 2176},
    32: {1: 1, 2: 256, 3: 6561, 4: 38416, 5: 279841, 6: 1331716},
}
SATURATING = {8: {1, 2, 3}, 16: {1, 2, 3, 7}}


def main():
    # ---------------- A: negacyclic Parseval, exact integer form
    bad = tot = 0
    for h in (4, 8):
        for a in product(range(-2, 3), repeat=h):
            tot += 1
            E = sum(v * v for v in a)
            c = negacyclic_mul(list(a), conj_vector(list(a), h), h)
            if c[0] != E:
                bad += 1
    check("A: negacyclic Parseval -- const. coeff. of alpha*alpha~ mod (x^h+1) "
          "equals E = sum a_i^2 (exhaustive coeffs in [-2,2], h=4,8)",
          bad == 0, f"{tot} vectors, {bad} violations")

    # Tr(zeta_n^i) = sum_{j odd mod n} zeta_n^{ij} = h if i == 0, else 0.
    # Exact integer form: the trace of multiplication by zeta_n^i on the basis.
    bad = 0
    for h in (4, 8, 16):
        for i in range(h):
            e = [0] * h
            e[i] = 1
            M = mult_matrix(e, h)
            tr = sum(M[k][k] for k in range(h))
            if tr != (h if i == 0 else 0):
                bad += 1
    check("A: Tr(zeta_n^i) = h*[i == 0] for 0 <= i < h (h = 4, 8, 16) -- the "
          "orthogonality behind Parseval", bad == 0, f"{bad} violations")

    # ---------------- B: positivity + energy ceiling
    # (i) exhaustive, general integer coefficients, h = 4
    tot = bad = tight = neg = 0
    for a in product(range(-3, 4), repeat=4):
        if not any(a):
            continue
        tot += 1
        E = sum(v * v for v in a)
        d = norm(list(a), 4)
        if d < 0:
            neg += 1
        if not (1 <= d <= E ** 2):
            bad += 1
        if d == E ** 2:
            tight += 1
    check("B: 1 <= Norm <= E^{h/2} exhaustive over coefficients in [-3,3]^4 "
          "(h = 4, general INTEGER coefficients)", bad == 0 and neg == 0,
          f"{tot} vectors, {bad} violations, {tight} attain the ceiling")

    # (ii) exhaustive ternary, h = 8; collect per-weight maxima
    maxima8 = {w: 0 for w in range(9)}
    tot = bad = 0
    argmax8 = {}
    for a in product((-1, 0, 1), repeat=8):
        w = sum(1 for c in a if c)
        d = norm(list(a), 8)
        if w == 0:
            if d != 0:
                bad += 1
            continue
        tot += 1
        E = sum(c * c for c in a)          # = w for ternary
        if E != w or not (1 <= d <= E ** 4):
            bad += 1
        if d > maxima8[w]:
            maxima8[w] = d
            argmax8[w] = list(a)
    check("B: 1 <= Norm <= E^{h/2} exhaustive over ternary vectors at h = 8",
          bad == 0, f"{tot} nonzero vectors, {bad} violations")

    # (iii) sampled, large non-ternary coefficients, h = 8
    rng = LCG(20260802)
    tot = bad = 0
    best_num, best_den = 0, 1
    for _ in range(4000):
        a = [rng.randint(-4, 4) for _ in range(8)]
        if not any(a):
            continue
        tot += 1
        E = sum(v * v for v in a)
        d = norm(a, 8)
        if not (1 <= d <= E ** 4):
            bad += 1
        if d * best_den > best_num * E ** 4:
            best_num, best_den = d, E ** 4
    check("B: 1 <= Norm <= E^{h/2} on 4000 deterministic samples from "
          "[-4,4]^8 (E up to 128, far outside the ternary range)", bad == 0,
          f"{tot} nonzero samples, {bad} violations, "
          f"max Norm/E^4 = {best_num}/{best_den}")

    # ---------------- C: banked maxnorm reproduction
    maxima4 = {w: 0 for w in range(5)}
    for a in product((-1, 0, 1), repeat=4):
        w = sum(1 for c in a if c)
        if w:
            maxima4[w] = max(maxima4[w], norm(list(a), 4))
    check("C: per-weight ternary maxima at 2N = 8 reproduce the banked "
          "sandwich table", {w: maxima4[w] for w in range(1, 5)} == BANKED[8],
          str({w: maxima4[w] for w in range(1, 5)}))
    check("C: per-weight ternary maxima at 2N = 16 reproduce the banked "
          "sandwich table", {w: maxima8[w] for w in range(1, 9)} == BANKED[16],
          str({w: maxima8[w] for w in range(1, 9)}))
    sat8 = {w for w in range(1, 9) if maxima8[w] == w ** 4}
    check("C: the ceiling is ATTAINED exactly at the banked saturating weights "
          "{1,2,3,7} at 2N = 16", sat8 == SATURATING[16], str(sorted(sat8)))

    # h = 16 (2N = 32): exhaustive at w <= 3, iota witnesses at w = 4,5,6
    maxima16 = {}
    for w in (1, 2, 3):
        maxima16[w] = max(norm(v, 16) for v in weight_vectors(16, w))
    check("C: per-weight ternary maxima at 2N = 32 reproduce the banked table "
          "for w <= 3 (exhaustive)",
          {w: maxima16[w] for w in (1, 2, 3)}
          == {w: BANKED[32][w] for w in (1, 2, 3)}, str(maxima16))
    ok = True
    wit = {}
    for w in (4, 5, 6):
        f = iota(argmax8[w])
        v = norm(f, 16)
        wit[w] = v
        ok &= (v == maxima8[w] ** 2 == BANKED[32][w] <= w ** 8)
    check("C: the doubling witnesses iota(argmax_{2N=16}) attain the banked "
          "2N = 32 maxima at w = 4,5,6 and sit under the ceiling w^8", ok,
          str(wit))

    # ---------------- D: ternariness is not used
    #   coefficient-2 witnesses whose energy differs from their weight
    d_ok = True
    rows = []
    for a, h in ([[2, 0, 0, 0], 4], [[2, 2, 0, 0], 4], [[2, 1, -1, 0], 4],
                 [[3, 0, 0, 0], 4], [[2, 2, 2, -2, -2, 2, -2, 0], 8]):
        E = sum(c * c for c in a)
        w = sum(1 for c in a if c)
        d = norm(a, h)
        d_ok &= (1 <= d <= E ** (h // 2)) and E != w
        rows.append(f"E={E} w={w} Norm={d} ceiling={E**(h//2)}")
    check("D: ceiling holds for NON-ternary vectors, where E != weight -- "
          "ternariness is never used", d_ok, "; ".join(rows))
    # the ternary case is the banked special case E = w
    check("D: on ternary vectors E = w exactly, so LN4 specializes to the "
          "banked sandwich Claim 2 (Norm <= w^{h/2})",
          all(sum(c * c for c in v) == sum(1 for c in v if c)
              for v in weight_vectors(8, 3)), "E = w on all weight-3 vectors")

    # ---------------- E: LN5 router
    # (i) the 256:1 collapse, exact integers on scaled-down surrogates
    bad = 0
    for o in (1, 2, 3, 4):
        N = 256 * o
        for q in (97, 193, 2**41 + 1, 3**128, 3**128 + 1, 2**255):
            for E in (1, 2, 3, 4, 5):
                lhs = q ** o <= E ** (N // 2)
                rhs = q <= E ** 128
                if lhs != rhs:
                    bad += 1
    check("E: at the official 256:1 schedule the criterion q^o <= E^{N/2} "
          "with N = 256o is EQUIVALENT to q <= E^128, for every o "
          "(exact integer comparison, o = 1..4)", bad == 0,
          "120 (o,q,E) triples, 0 disagreements")

    # (ii) a real junction-0 instance: (n,t,q) = (32,8,97), U_0 = {1,3,5,7},
    #      cells = h_1 = 16, L_0 = 4.  Router: 97^4 = 88529281 > 3^8 = 6561,
    #      so NO ternary junction-0 skew of support <= 3 can solve the block.
    n, t, q = 32, 8, 97
    h = n // 2
    U = [u for u in range(1, t + 1, 2)]
    L = len(U)

    def prim_root(p):
        m, fs, d = p - 1, [], 2
        while d * d <= m:
            if m % d == 0:
                fs.append(d)
                while m % d == 0:
                    m //= d
            d += 1
        if m > 1:
            fs.append(m)
        for g in range(2, p):
            if all(pow(g, (p - 1) // r, p) != 1 for r in fs):
                return g
        raise AssertionError

    z = pow(prim_root(q), (q - 1) // n, q)
    rows_u = [[pow(z, (u * i) % n, q) for i in range(h)] for u in U]
    found = 0
    scanned = 0
    for w in (1, 2, 3):
        for S in combinations(range(h), w):
            cols = [[r[i] for i in S] for r in rows_u]
            for eps in product((1, -1), repeat=w):
                scanned += 1
                if all(sum(e * c for e, c in zip(eps, col)) % q == 0
                       for col in cols):
                    found += 1
    check("E: LN5 router at the real junction (n,t,q,j) = (32,8,97,0): "
          f"q^L = 97^{L} = {q**L} > 3^8 = {3**8} = max ceiling at E <= 3, so "
          "every support of size <= 3 is predicted EMPTY -- confirmed by "
          "exhaustive enumeration", found == 0,
          f"{scanned} ternary skews of weight <= 3, {found} solutions")

    # (iii) the contrapositive as an exact energy floor
    ok = True
    for (q, o, N) in [(97, 4, 16), (193, 2, 8), (257, 2, 8)]:
        Emin = 1
        while Emin ** (N // 2) < q ** o:
            Emin += 1
        ok &= all(E ** (N // 2) < q ** o for E in range(1, Emin))
    check("E: contrapositive -- every junction solution has "
          "E >= min{E : E^{N/2} >= q^o}; the excluded band is exactly "
          "1..E_min-1 (exact integer sweep)", ok,
          "checked at (q,o,N) = (97,4,16), (193,2,8), (257,2,8)")

    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("DLI_NORM_GATE_ENERGY_CEILING_ALL_PASS")


if __name__ == "__main__":
    main()
