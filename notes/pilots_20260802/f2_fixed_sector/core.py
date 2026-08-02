#!/usr/bin/env python3
"""Two-sector (fixed x moving) census machinery for the F2 absorption question.

Pilot notes/pilots_20260802/f2_fixed_sector/, 2026-08-02.

QUESTION (the obligation opened by the deployed-windows pilot, REPORT.md:55,75):
does the FIXED sector mu_{2^24} <= F_p absorb the parity-pure frequency class
that the slice theorem provably cannot cover?

------------------------------------------------------------------ the model --
p odd with v_2(p-1) = e exactly;  F_{p^2} = F_p(w), w^2 = N,  Tr(a+bw) = 2a;
psi(s) = e_p(s) = zeta_p^s.  Take the rung-1 group

    mu_n,  n = 2^{e+1},   mu_n cap F_p = mu_{2^e}  (v_2(p-1) = e)

which splits into

    FIXED sector  mu_{n_0}, n_0 = 2^e  (Frobenius-fixed; the analytic-regime
                  sector of campaign log #75, F2_CAMPAIGN_LOG.md:1394-1410)
    MOVING sector the 2^e elements of order exactly 2^{e+1}, in 2^{e-1}
                  ANTIPODAL pairs {y,-y}  (antipodal descent lemma, deployed-
                  windows pilot tower.py:22-43).

The census term at a frequency c = (c_l) is the SIGNED REAL (PRO_FLOOR_2 brief
"THE PROBLEM"):

    T(c) = prod_{x in mu_n} (1 + psi(chi_c(x))),  chi_c(x) = Tr(sum_l c_l x^l),

and it FACTORS over the sectors:  T(c) = F(c) * M(c)  with F the fixed-sector
product and M the moving one.  The b-resolved version replaces each factor by
its z-polynomial  prod (1 + z psi(chi(x))), and sector composition becomes the
convolution in b.

------------------------------------------------------------ THE KEY REMARK --
-1 lies in mu_{n_0} = mu_{2^e} (e >= 1), so the FIXED SECTOR IS ITSELF
ANTIPODALLY CLOSED.  A parity-pure (odd-support) frequency therefore satisfies
chi_c(-x) = -chi_c(x) on the fixed sector too, and psi(-s) = conj psi(s) gives

    F(c) = prod_{fixed pairs} |1 + psi(chi_c(x))|^2  >=  0.

That is the same positivity the moving sector has -- which is what this pilot
measures, exactly, in Z[zeta_p].

Everything banked here is exact integer / cyclotomic-integer arithmetic; floats
appear only in quantities labelled `_float` (magnitudes, logs, means).
"""
from __future__ import annotations

import math
import os
import sys

sys.dont_write_bytecode = True          # never litter the imported pilots

_HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(_HERE, "results")


# ----------------------------------------------------------------- primes ----


def is_prime(m: int) -> bool:
    if m < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % q == 0:
            return m == q
    d, r = m - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(r - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def v2(x: int) -> int:
    return (x & -x).bit_length() - 1


def official_shaped_prime(e: int) -> int:
    """Smallest prime p with v_2(p-1) == e exactly (matches deployed/tower.py)."""
    k = 1
    while True:
        p = (1 << e) * k + 1
        if is_prime(p) and v2(p - 1) == e:
            return p
        k += 2


# ------------------------------------------------------------------ F_p^2 ----


class Fp2:
    """F_{p^2} = F_p(w), w^2 = N (least non-residue).  Elements are (a, b)."""

    __slots__ = ("p", "N")

    def __init__(self, p: int):
        self.p = p
        n = 2
        while pow(n, (p - 1) // 2, p) != p - 1:
            n += 1
        self.N = n

    def mul(self, u, v):
        p, N = self.p, self.N
        a, b = u
        c, d = v
        return ((a * c + N * b * d) % p, (a * d + b * c) % p)

    def pow(self, u, k: int):
        r = (1, 0)
        b = u
        while k:
            if k & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            k >>= 1
        return r

    def trace(self, u) -> int:
        return (2 * u[0]) % self.p

    def neg(self, u):
        return ((-u[0]) % self.p, (-u[1]) % self.p)

    def order(self, u) -> int:
        n = self.p * self.p - 1
        o = n
        m = n
        d = 2
        fac = {}
        while d * d <= m:
            while m % d == 0:
                fac[d] = fac.get(d, 0) + 1
                m //= d
            d += 1
        if m > 1:
            fac[m] = fac.get(m, 0) + 1
        for q in fac:
            while o % q == 0 and self.pow(u, o // q) == (1, 0):
                o //= q
        return o

    def subgroup(self, n: int):
        """mu_n as an ordered list of powers of a generator."""
        assert (self.p * self.p - 1) % n == 0
        g = (2, 1)
        while True:
            h = self.pow(g, (self.p * self.p - 1) // n)
            if self.order(h) == n:
                break
            g = (g[0] + 1, g[1] + 1) if g[0] + 1 < self.p else (1, g[1] + 2)
        out, cur = [], (1, 0)
        for _ in range(n):
            out.append(cur)
            cur = self.mul(cur, h)
        return out


def sectors(F: Fp2, e: int):
    """(fixed elements, moving pair representatives) of mu_{2^{e+1}}."""
    n = 1 << (e + 1)
    mu = F.subgroup(n)
    fixed = [x for x in mu if x[1] == 0]          # mu_n cap F_p = mu_{2^e}
    moving = [x for x in mu if x[1] != 0]
    assert len(fixed) == (1 << e), (len(fixed), 1 << e)
    reps, seen = [], set()
    for y in moving:
        if y in seen:
            continue
        reps.append(y)
        seen.add(y)
        seen.add(F.neg(y))
    assert 2 * len(reps) == len(moving)
    # fixed-sector antipodal pairing (legitimate: -1 in mu_{2^e} for e >= 1)
    freps, fseen = [], set()
    for x in fixed:
        if x in fseen:
            continue
        freps.append(x)
        fseen.add(x)
        fseen.add(F.neg(x))
    assert 2 * len(freps) == len(fixed)
    return fixed, reps, freps


# ------------------------------------------------------------- characters ----


def chi_values(F: Fp2, coeffs: dict, xs, n_ord: int):
    """chi_c(x) = Tr(sum_l c_l x^l) in F_p, exact, for each x in xs."""
    p = F.p
    out = []
    for x in xs:
        acc = (0, 0)
        for l, cl in coeffs.items():
            t = F.mul(cl, F.pow(x, l % n_ord))
            acc = ((acc[0] + t[0]) % p, (acc[1] + t[1]) % p)
        out.append(F.trace(acc))
    return out


def parity_class(coeffs: dict) -> str:
    """K1 = purely odd support, K2 = purely even (no constant), G = mixed."""
    ls = [l for l, c in coeffs.items() if c != (0, 0)]
    if not ls:
        return "vacuous"
    odd = [l for l in ls if l % 2 == 1]
    ev = [l for l in ls if l % 2 == 0]
    if ev and not odd:
        return "K2"
    if odd and not ev:
        return "K1"
    return "G"


# ---------------------------------------------------------------- Z[zeta_p] --
# vector of p ints modulo  sum_{i<p} zeta^i = 0;  canonical form: a_{p-1} = 0.


def canon(u):
    t = u[-1]
    if t:
        return [x - t for x in u]
    return list(u)


def cyc_one(p):
    v = [0] * p
    v[0] = 1
    return v


def cyc_shift(u, s):
    """u * zeta^s (cyclic shift), canonicalised."""
    p = len(u)
    s %= p
    if s == 0:
        return list(u)
    return canon(u[-s:] + u[:-s])


def cyc_add(u, v):
    return [a + b for a, b in zip(u, v)]


def cyc_is_rational_integer(u):
    """(bool, value) -- true iff u is a rational integer in canonical form."""
    return (all(x == 0 for x in u[1:]), u[0])


def cyc_conj(u):
    """complex conjugation zeta -> zeta^{-1}."""
    p = len(u)
    out = [0] * p
    for i, a in enumerate(u):
        out[(-i) % p] += a
    return canon(out)


def cyc_is_real(u):
    return canon(list(u)) == cyc_conj(u)


def cyc_abs(u, dps: int = 60) -> float:
    """|sum a_i zeta^i| as a float, evaluated at `dps` digits (diagnostic)."""
    from mpmath import mp, mpf, exp, mpc, pi
    mp.dps = dps
    p = len(u)
    s = mpc(0)
    for i, a in enumerate(u):
        if a:
            s += mpf(a) * exp(mpc(0, 1) * 2 * pi * i / p)
    return float(abs(s))


def cyc_log2abs(u, dps: int = 60) -> float:
    from mpmath import mp, mpf, exp, mpc, pi, log
    mp.dps = dps
    p = len(u)
    s = mpc(0)
    for i, a in enumerate(u):
        if a:
            s += mpf(a) * exp(mpc(0, 1) * 2 * pi * i / p)
    if s == 0:
        return float("-inf")
    return float(log(abs(s)) / log(2))


def cyc_embed(u, k: int = 1, dps: int = 60):
    """sigma_k(u) = sum a_i zeta^{ik} evaluated at `dps` digits (mpmath mpc)."""
    from mpmath import mp, mpf, exp, mpc, pi
    mp.dps = dps
    p = len(u)
    s = mpc(0)
    for i, a in enumerate(u):
        if a:
            s += mpf(a) * exp(mpc(0, 1) * 2 * pi * ((i * k) % p) / p)
    return s


def cyc_min_conjugate(u, dps: int = 40) -> float:
    """min over the p-1 embeddings of Re sigma_k(u) (diagnostic for total
    positivity of a REAL cyclotomic integer)."""
    p = len(u)
    return min(float(cyc_embed(u, k, dps).real) for k in range(1, p))


def pair_product(p: int, pair_values):
    """prod over pairs of (2 + zeta^s + zeta^{-s}) -- the EXACT antipodal
    normal form of a parity-pure sector factor.  Each factor is 2+2cos > 0."""
    acc = cyc_one(p)
    for s in pair_values:
        a, b = cyc_shift(acc, s), cyc_shift(acc, -s)
        acc = canon([2 * x + y + z for x, y, z in zip(acc, a, b)])
    return acc


def cyc_mul(u, v):
    p = len(u)
    out = [0] * p
    for i, a in enumerate(u):
        if not a:
            continue
        for j, b in enumerate(v):
            if b:
                out[(i + j) % p] += a * b
    return canon(out)


def census_term(p: int, values):
    """prod_x (1 + zeta_p^{s_x}) as an EXACT cyclotomic integer."""
    acc = cyc_one(p)
    for s in values:
        acc = cyc_add(acc, cyc_shift(acc, s))
        acc = canon(acc)
    return acc


def census_poly(p: int, values):
    """[z^b] prod_x (1 + z zeta_p^{s_x}) for b = 0..len(values), EXACT."""
    poly = [cyc_one(p)]
    for s in values:
        new = [None] * (len(poly) + 1)
        new[0] = poly[0]
        for b in range(1, len(poly) + 1):
            hi = cyc_shift(poly[b - 1], s)
            if b < len(poly):
                new[b] = canon(cyc_add(poly[b], hi))
            else:
                new[b] = hi
        poly = new
    return poly


# ------------------------------------------------- the lane's carry window ---


def sigma_of(p: int, s: int) -> int:
    """sigma = least residue lifted into Z/2p by the half-interval flag."""
    s %= p
    return s + p * (1 if 2 * s > p else 0)


def window_of(F: Fp2, coeffs: dict, reps, n_ord: int):
    """(Delta list, base) of the window whose coordinates are the pairs
    {y, -y} with representative y -- the lane's deployed-window data."""
    p = F.p
    two_p = 2 * p
    plus = chi_values(F, coeffs, reps, n_ord)
    minus = chi_values(F, coeffs, [F.neg(y) for y in reps], n_ord)
    D, base = [], 0
    for sp, sm in zip(plus, minus):
        a, b = sigma_of(p, sp), sigma_of(p, sm)
        D.append((a - b) % two_p)
        base += b
    return D, base % two_p


def DP_V(p: int, deltas, base: int):
    """Exact integer V_b (balanced-weight carry statistic).

    Identical to notes/pilots_20260802/f2_deployed_windows/verify.py:184-202;
    reimplemented here so this pilot never writes into that directory.
    """
    two_p = 2 * p
    n = len(deltas)
    dp = [[0] * two_p for _ in range(n + 1)]
    dp[0][0] = 1
    for i, d in enumerate(deltas):
        nd = [[0] * two_p for _ in range(n + 1)]
        for b in range(i + 1):
            row = dp[b]
            ndb, ndb1 = nd[b], nd[b + 1]
            for r in range(two_p):
                v = row[r]
                if v:
                    ndb[r] += v
                    ndb1[(r + d) % two_p] += v
        dp = nd
    sgn = [1 if (base + r) % two_p < p else -1 for r in range(two_p)]
    return [sum(dp[b][r] * sgn[r] for r in range(two_p)) for b in range(n + 1)]


def maxR_float(p: int, deltas):
    """(max_k odd |R_k|, argmax k) -- float diagnostic, as in census.py."""
    import numpy as np
    two_p = 2 * p
    cnt = np.bincount(np.array([d % two_p for d in deltas], dtype=np.int64),
                      minlength=two_p)
    Ff = np.fft.fft(cnt.astype(float))
    R = np.abs(Ff[1::2]) / len(deltas)
    j = int(np.argmax(R))
    return float(R[j]), int(2 * j + 1)


def all_even(deltas) -> bool:
    return all(d % 2 == 0 for d in deltas)


# ---------------------------------------------------------------------- io ---


def dump(name, obj):
    import json
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, name), "w") as f:
        json.dump(obj, f, indent=1, default=str)
    print(f"[wrote] results/{name}")
