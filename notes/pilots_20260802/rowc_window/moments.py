#!/usr/bin/env python3
"""RowC window pilot -- part 2: EXACT first and second moments in the word
model, conditioned on admissibility, at explicit primes inside the RowC 1/4
band.

    tools/ramguard local -- python3 \
        notes/pilots_20260802/rowc_window/moments.py

THE MODEL (no heuristic anywhere in this file)
----------------------------------------------
D = mu_n < F_q^*, |D| = n, n | q-1.  (u,v) uniform on (F_q^D)^2.  w_z = u+zv.
For |S| = A the interpolant P_S(w) of w|_S has degree < A, and

    deg P_S(w) < K   <=>   p_s(S,w) := sum_{i in S} w_i x_i^s / Lambda'_S(x_i)
                                      = 0  for s = 0..h-1,

h = A-K  (expand P_S/Lambda_S at infinity).  These are h linear functionals of
w, surjective onto F_q^h.  Put

    N = #{ (S,z) : |S| = A, z in F_q, deg P_S(w_z) < K }.

EXACT MOMENTS.
  E[N] = C q^{1-h},  C = C(n,A).                                   (mu)

  For z = z' and S != S' with c = |S ^ S'|, the joint event is "some p,p' of
  degree < K with w = p on S, w = p' on S'".  Its solution set inside
  F_q^{S u S'} is linear of dimension 2K-c (c <= K) resp. K (c >= K), so

      P = q^{-2h}                  (c <= K)
      P = q^{-(2A-c-K)}            (c >= K)

  For z != z', (w_z,w_z') is uniform on (F_q^D)^2, so P = q^{-2h} exactly.
  Hence, with  Sh0 = sum_{c=K+1}^{A-1} C(A,c) C(n-A,A-c)  and
  Shi = sum_{c=K+1}^{A-1} C(A,c) C(n-A,A-c) q^{K+c-2A},

      Var[N] = mu + q C Shi - q C q^{-2h} (1 + Sh0).

  Everything above is an identity, not an estimate.

THE CERTIFICATE.  Let
  Bad   = the pair fails T0/T1/T2/T3/T4, global genericity, below cascade,
          or v has a zero
  Low   = { N < mu/2 }
  Dbl   = { two distinct witnesses at one slope }
  Hi    = { two witnesses with |S ^ S'| >= K }
On the complement of Bad u Low u Dbl u Hi the pair is P-B-admissible, every
live slope carries exactly one witness (so #live = N), no two selected
supports meet in >= K places (so Gamma_lo = Gamma = #live = N), and
|Gamma_lo| >= mu/2.  Markov + Chebyshev give an explicit numeric bound on
P[Bad] + P[Low] + P[Dbl] + P[Hi].
"""

from __future__ import annotations

import json
import os
import sys
from fractions import Fraction
from math import comb

sys.dont_write_bytecode = True

from mpmath import mp, mpf, log  # noqa: E402
from sympy import isprime  # noqa: E402

mp.dps = 50
LN2 = log(mpf(2))

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "MOMENTS.json")


def lg(x) -> float:
    if isinstance(x, Fraction):
        if x == 0:
            return float("-inf")
        return float((log(mpf(x.numerator)) - log(mpf(x.denominator))) / LN2)
    if x == 0:
        return float("-inf")
    return float(log(mpf(x)) / LN2)


def next_prime_1modn(x: int, n: int) -> int:
    """smallest prime >= x congruent to 1 mod n."""
    q = x + ((1 - x) % n)
    while not isprime(q):
        q += n
    return q


class Row:
    def __init__(self, name, n, k, A):
        self.name, self.n, self.k, self.A = name, n, k, A
        self.h = A - k
        self.K = k
        self.b8 = 3 + 3 * (n.bit_length() - 1)
        self.budget8 = 1 << self.b8
        self.C = comb(n, A)

    def _sharp(self, mu, var, Ep2low, Ehi, pbad):
        """Sharp certificate: Chebyshev at t = 2^10 sigma, Markov at 2^10.

        With probability >= 1 - pbad - 2^-20 - 2^-10 - Ehi the pair is
        admissible and  |Gamma_lo| >= mu - 2^10 sqrt(Var) - 2^10 E[P2low].
        """
        import math
        t = Fraction(1024)              # Chebyshev  -> P <= 2^-20
        s = Fraction(1 << 20)           # Markov     -> P <= 2^-20
        sq = Fraction(math.isqrt(int(var.numerator * var.denominator)),
                      var.denominator) if var > 0 else Fraction(0)
        guar = mu - t * sq - s * Ep2low
        pf = pbad + Fraction(1, 1 << 20) + Fraction(1, 1 << 20) + Ehi
        return dict(
            sharp_guaranteed_log2=lg(guar) if guar > 0 else None,
            sharp_guaranteed_over_8n3_log2=(lg(guar) - self.b8)
            if guar > 0 else None,
            sharp_log2_P_fail=lg(pf),
            sharp_ok=bool(guar > (1 << self.b8) and pf < Fraction(1, 2)),
        )

    # ---- exact moments at a given prime q ------------------------------
    def moments(self, q: int) -> dict:
        n, k, A, h, K, C = self.n, self.k, self.A, self.h, self.K, self.C
        Q = Fraction(q)
        mu = Fraction(C) / Q ** (h - 1)

        # high-core sums (c = K+1 .. A-1); at these rows h-1 <= 4 terms
        Sh0 = 0
        Shi = Fraction(0)
        percore = {}
        for c in range(K + 1, A):
            t = comb(A, c) * comb(n - A, A - c)
            if t == 0:
                continue
            Sh0 += t
            term = Fraction(t) * Q ** (K + c - 2 * A)
            Shi += term
            percore[c] = t
        # core >= K population fraction (used for E[Hi])
        Score = 0
        for c in range(K, A + 1):
            Score += comb(A, c) * comb(n - A, A - c)

        var = mu + Q * C * Shi - Q * C * Q ** (-2 * h) * (1 + Sh0)

        # E[# unordered same-slope witness pairs with core < K]
        #   -- these only make #live < N; #live >= N - P2low
        Slow = C - 1 - Sh0
        Ep2low = Q * C * Fraction(Slow) * Q ** (-2 * h) / 2
        # E[# unordered witness pairs with core >= K]  (both slope cases)
        # NOTE  a SAME-slope pair with core c in [K, A-1] forces p_S = p_S'
        # (two degree-<K polynomials agreeing on c >= K points), hence an
        # agreement set of size 2A-c >= A+1: it is a T2 over-agreement event
        # and is already inside pbad.  Only the DIFFERENT-slope high-core
        # pairs are an independent failure mode.
        Ehi_same = Q * C * Shi / 2
        Ehi_diff = Fraction(q * (q - 1), 2) * C * Fraction(Score) * Q ** (-2 * h)
        Ehi = Ehi_diff

        # ---- gate first moments (all exact) ----
        # T2 tangent: some z in P^1 and codeword c with agreement >= A+1
        Et2 = Fraction(0)
        for a in range(A + 1, n + 1):
            t = Fraction(comb(n, a)) * Q ** (k - a)
            Et2 += t
            if t < Fraction(1, 10 ** 40) and a > A + 3:
                break
        Et2 *= (q + 1)
        # T0 / global genericity: joint codeword-pair explanation on a
        # support of size >= A
        Egg = Fraction(0)
        for a in range(A, n + 1):
            t = Fraction(comb(n, a)) * Q ** (2 * (k - a))
            Egg += t
            if t < Fraction(1, 10 ** 40) and a > A + 2:
                break
        # below cascade: joint explanation on a support of size >= A-1
        Ecasc = Fraction(0)
        for a in range(A - 1, n + 1):
            t = Fraction(comb(n, a)) * Q ** (2 * (k - a))
            Ecasc += t
            if t < Fraction(1, 10 ** 40) and a > A + 1:
                break
        # T1 (u=0, v=0, v=lambda u), T4 (rank < 2) -- same event
        Et1 = Fraction(2, 1) * Q ** (-n) + Fraction(q) * Q ** (-n)
        # T3 quotient fold through x -> x^M, M | gcd(n,k), M > 1:
        # u and v both M-periodic
        Et3 = Fraction(0)
        M = 2
        g = 1
        while g * 2 <= min(n, k):
            g *= 2
        # gcd(n,k) is a power of two at every row
        gcd_nk = k if k <= n else n
        M = 2
        while M <= gcd_nk:
            if gcd_nk % M == 0:
                Et3 += Q ** (-2 * (n - n // M))
            M *= 2
        # v nowhere zero
        Evz = Fraction(n) * Q ** (-1)

        pbad = Et2 + Egg + Ecasc + Et1 + Et3 + Evz
        # Chebyshev: P[N < mu/2] <= 4 Var / mu^2
        plow = 4 * var / (mu * mu) if mu > 0 else Fraction(1)
        # Markov: P[P2low > mu/4] <= 4 E[P2low] / mu
        pdbl = 4 * Ep2low / mu if mu > 0 else Fraction(1)
        # Markov: P[some high-core pair] <= E[Hi]
        pfail = pbad + plow + pdbl + Ehi

        # conditioned first moment, Cauchy-Schwarz:
        #   E[N 1_bad] <= sqrt(E[N^2] P(bad)) = sqrt((var+mu^2) pbad)
        # so E[N | adm] >= (mu - sqrt((var+mu^2) pbad)) / (1 - pbad)
        en2 = var + mu * mu
        cs = mpf(en2.numerator) / mpf(en2.denominator) * \
            (mpf(pbad.numerator) / mpf(pbad.denominator))
        cs = mp.sqrt(cs)
        mu_f = mpf(mu.numerator) / mpf(mu.denominator)
        pbad_f = mpf(pbad.numerator) / mpf(pbad.denominator)
        cond_lo = (mu_f - cs) / (1 - pbad_f) if pbad_f < 1 else mpf(0)

        return dict(
            q=q, log2_q=float(lg(q)),
            log2_mu=lg(mu), mu_over_8n3_log2=lg(mu) - self.b8,
            log2_mean_Wz=lg(mu / Q),
            log2_var=lg(var), var_over_mu=float(lg(var) - lg(mu)),
            log2_E_T2_tangent=lg(Et2),
            log2_E_GG_generic=lg(Egg),
            log2_E_CASC=lg(Ecasc),
            log2_E_T1=lg(Et1), log2_E_T3=lg(Et3), log2_P_vzero=lg(Evz),
            log2_P_bad=lg(pbad),
            log2_P_low_cheb=lg(plow),
            log2_E_p2low=lg(Ep2low),
            log2_P_dbl_markov=lg(pdbl),
            log2_E_highcore_pair_diffslope=lg(Ehi),
            log2_E_highcore_pair_sameslope_subsumed_by_T2=lg(Ehi_same),
            log2_P_fail_total=lg(pfail),
            certificate_ok=bool(pfail < Fraction(1, 2)),
            guaranteed_Gamma_lo_log2=lg(mu / 4),
            guaranteed_over_8n3_log2=lg(mu / 4) - self.b8,
            **self._sharp(mu, var, Ep2low, Ehi, pbad),
            log2_cond_first_moment_lower=float(log(cond_lo) / LN2)
            if cond_lo > 0 else None,
            cond_over_mu=float(cond_lo / mu_f) if mu_f > 0 else None,
            highcore_population_log2=lg(Fraction(Score, C)),
        )


ROWS = [Row("RowC 1/4", 1 << 10, 1 << 8, 261),
        Row("RowC 1/8", 1 << 10, 1 << 7, 133),
        Row("RowC 1/16", 1 << 10, 1 << 6, 67)]


def main():
    out = {}
    r = ROWS[0]
    print("=" * 100)
    print("RowC 1/4 : n=1024 k=256 A=261 h=5 K=256 8n^3=2^33")
    print("EXACT word-model moments at explicit primes q = 1 mod 1024")
    print("=" * 100)

    targets = [
        ("just above the tangent gate  (G_T2 = 2^166.9988)", 167.02),
        ("gate slack 2^-20", 167.0 + 20 / 5),
        ("gate slack 2^-64", 167.0 + 64 / 5),
        ("below L1 (row itself unsound)", 185.0),
        ("L1 floor: mean live slopes = B*", 192.30),
        ("mid sound band", 196.0),
        ("near the top of the band", 200.0),
        ("above L3 -- P-B's first moment fits", 201.0),
        ("the banked envelope pin", 250.0),
    ]
    rows = []
    for label, lq in targets:
        q = next_prime_1modn(int(mpf(2) ** mpf(lq)), r.n)
        m = r.moments(q)
        m["label"] = label
        rows.append(m)

    print("%-42s %8s %10s %10s %10s %10s %10s" %
          ("point", "log2 q", "log2 mu", "mu/8n^3", "log2 Var",
           "lg P[bad]", "lg P[fail]"))
    for m in rows:
        print("%-42s %8.3f %10.3f %+10.3f %10.3f %10.2f %10.2f" %
              (m["label"], m["log2_q"], m["log2_mu"], m["mu_over_8n3_log2"],
               m["log2_var"], m["log2_P_bad"], m["log2_P_fail_total"]))

    print()
    print("gate detail (log2 of the exact first moments):")
    print("%-42s %10s %10s %10s %10s %10s" %
          ("point", "T2", "T0/GG", "CASC", "v=0", "E[hi-core]"))
    for m in rows:
        print("%-42s %10.2f %10.2f %10.2f %10.2f %10.2f" %
              (m["label"], m["log2_E_T2_tangent"], m["log2_E_GG_generic"],
               m["log2_E_CASC"], m["log2_P_vzero"],
               m["log2_E_highcore_pair_diffslope"]))

    print()
    print("concentration, conditioning, and the certificate:")
    print("%-42s %10s %10s %10s %12s %11s %s" %
          ("point", "lgVar/mu", "lgP[low]", "lgP[dbl]", "E[N|adm]/mu",
           "lg P[fail]", "guaranteed |Gamma_lo| / 8n^3"))
    for m in rows:
        print("%-42s %10.4f %10.2f %10.2f %12.6f %11.2f  2^%+.3f  %s" %
              (m["label"], m["var_over_mu"], m["log2_P_low_cheb"],
               m["log2_P_dbl_markov"],
               m["cond_over_mu"] if m["cond_over_mu"] is not None else -1,
               m["log2_P_fail_total"], m["guaranteed_over_8n3_log2"],
               "CERTIFIED COUNTEREXAMPLE" if m["certificate_ok"] and
               m["guaranteed_over_8n3_log2"] > 0 else ""))

    print()
    print("SHARP certificate  (Chebyshev at 2^10 sigma, Markov at 2^20):")
    print("%-42s %10s %14s %26s" %
          ("point", "lg P[fail]", "lg |Gamma_lo|", "|Gamma_lo| / 8n^3"))
    for m in rows:
        print("%-42s %10.4f %14s %26s   %s" %
              (m["label"], m["sharp_log2_P_fail"],
               ("%.4f" % m["sharp_guaranteed_log2"])
               if m["sharp_guaranteed_log2"] is not None else "-",
               ("2^%+.4f" % m["sharp_guaranteed_over_8n3_log2"])
               if m["sharp_guaranteed_over_8n3_log2"] is not None else "-",
               "P-B FALSE HERE" if m["sharp_ok"] else ""))

    out["RowC 1/4"] = rows

    # the other two RowC rows, at their own bare-band interiors, for contrast
    print()
    print("=" * 100)
    print("CONTRAST: RowC 1/8 and RowC 1/16 inside their BARE bands")
    print("(admissible + super-budget, but B* < 16n^3 there: the program")
    print(" floor q >= 2^162 excludes these)")
    print("=" * 100)
    for rr, lqs in ((ROWS[1], [120.0, 130.0]), (ROWS[2], [125.0, 155.0, 159.5])):
        rows2 = []
        for lq in lqs:
            q = next_prime_1modn(int(mpf(2) ** mpf(lq)), rr.n)
            m = rr.moments(q)
            m["label"] = "%s @ 2^%.1f" % (rr.name, lq)
            rows2.append(m)
            print("%-24s log2 mu = %8.3f  (%+8.3f over 8n^3)   "
                  "lg P[bad] = %8.2f   lg P[fail] = %8.2f   B*=2^%d" %
                  (m["label"], m["log2_mu"], m["mu_over_8n3_log2"],
                   m["log2_P_bad"], m["log2_P_fail_total"],
                   max(0, int(m["log2_q"]) - 128)))
        out[rr.name] = rows2

    with open(OUT, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True, default=str)
    print("\nwrote %s" % OUT)


if __name__ == "__main__":
    main()
