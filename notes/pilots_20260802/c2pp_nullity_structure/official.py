#!/usr/bin/env python3
"""C2'' pilot -- the nullity tail at the OFFICIAL schedule (exact arithmetic).

Official pins used (all cited, none invented here):
  t = 2^33, blocks ell_j = ceil(floor(t/2^j)/2) = (2^32,...,2,1,1), 34 blocks
      [C2PP_POSED_20260710.md, dli_wcl_zone_coverage, dli_marginal_baseline100]
  N_j = 256 ell_j                       [dli_marginal_baseline100_coverage]
  n   = 2^41 evaluation subgroup, so N_j = h_{j+1} = n/2^{j+1}   [pilot FX9]
  q prime, q = 1 + k 2^41, q < 2^256    [official_row_primes_pinning; the
                                         2^215-1 candidate progression]

O1  delta > 0  <=>  |S_0| < L_0   (exact, for t a power of two)
O2  the stratum {delta = t} is exactly the quotient-coset class, of size
    2^{n/2^{Lam+1}} = 2^128 at the official row
O3  that stratum alone contributes  q^t 2^{128-n}  to E_MF[q^delta]
O4  the per-block main term is  r_j = q^{ell_j}/2^{256 ell_j}, i.e. EXACTLY the
    constant the marginal-baseline node already carries
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy

HERE = Path(__file__).resolve().parent

N = 2**41
T = 2**33
LAM = 33                       # blocks j = 0..33
ELL = [-(-(T // 2**j) // 2) for j in range(34)]


def log2_upper(x: Fraction) -> Fraction:
    """Crude exact rational upper bound on log2(x) (bit length)."""
    return Fraction(x.numerator.bit_length() - x.denominator.bit_length() + 1)


def o1_lemma_check():
    """delta > 0 <=> |S_0| < L_0, verified exhaustively on small analogues."""
    from census import mf_support_law
    from dli_model import blocks
    out = []
    for (n, t) in [(16, 2), (16, 4), (16, 8), (32, 2), (32, 4), (32, 8),
                   (64, 4), (64, 8)]:
        B = blocks(t)
        L = [len(b) for b in B]
        law = mf_support_law(n, t)
        bad = 0
        for S, cnt in law.items():
            d = sum(max(0, L[j] - S[j]) for j in range(len(L)))
            if (d > 0) != (S[0] < L[0]):
                bad += cnt
        out.append({"n": n, "t": t, "L": L, "states": len(law),
                    "violating_mass": bad})
    return out


def official_numbers():
    cells_top = N // 2**(LAM + 1)                     # = 128
    res = {
        "n": str(N), "t": str(T), "blocks": 34, "junctions": 33,
        "ell": [str(e) for e in ELL],
        "N_j_equals_h_j1": [str(256 * ELL[j]) for j in range(33)],
        "support_to_constraint_ratio": 256,
        "coset_stratum_cells": cells_top,
        "coset_stratum_size": f"2^{cells_top}",
        "coset_stratum_probability": f"2^{cells_top - N}",
    }
    # O3: log2 of the coset-stratum contribution to E_MF[q^delta]
    #     = t*log2 q + cells_top - n = 2^33 (log2 q - 256) + 128
    res["coset_term_log2_formula"] = "2^33*(log2 q - 256) + 128"
    res["exceeds_2^21_iff"] = "256 - log2 q < 107/2^33 = 1.24556e-05"
    return res


def concrete_large_official_prime():
    """Largest few admissible q = 1 + k*2^41 below 2^256 that are prime."""
    step = 2**41
    k = (2**256 - 2) // step
    found = []
    while len(found) < 2 and k > 0:
        q = 1 + k * step
        if q < 2**256 and sympy.isprime(q):
            found.append(q)
        k -= 1
    return found


def coset_term_log2(q):
    """EXACT rational bounds on log2( q^t * 2^{128-n} ) = t*log2(q) + 128 - n.

    Writes q = 2^256 - u and uses  -z - z^2 <= ln(1-z) <= -z  for 0 < z <= 1/2,
    so   -(z+z^2)/ln2 <= log2(q) - 256 <= -z/ln2   with z = u/2^256.
    Returns (lower, upper) exact rational bounds on log2 of the coset term.
    """
    u = 2**256 - q
    z = Fraction(u, 2**256)
    # 1/ln2 in [1.4426950408, 1.4426950409]
    inv_ln2_lo = Fraction(14426950408, 10**10)
    inv_ln2_hi = Fraction(14426950409, 10**10)
    # log2(term) = t*log2 q + 128 - n = t*(log2 q - 256) + 128  since t*256 = n
    hi = T * (-(z * inv_ln2_lo)) + 128
    lo = T * (-((z + z * z) * inv_ln2_hi)) + 128
    return lo, hi


def main():
    out = {"official": official_numbers()}
    out["O1_lemma"] = o1_lemma_check()
    bad = sum(r["violating_mass"] for r in out["O1_lemma"])
    print("O1  delta > 0  <=>  |S_0| < L_0 :",
          f"{len(out['O1_lemma'])} (n,t) analogues, violating mass = {bad}")
    o = out["official"]
    print(f"O2  official coset stratum: {o['coset_stratum_cells']} level-34 cells "
          f"-> exactly {o['coset_stratum_size']} block-constant supports, "
          f"probability {o['coset_stratum_probability']}")
    print(f"O3  coset contribution to E_MF[q^delta] = {o['coset_term_log2_formula']} bits; "
          f"exceeds the 21-bit reserve iff {o['exceeds_2^21_iff']}")

    primes = concrete_large_official_prime()
    rows = []
    for q in primes:
        lo, hi = coset_term_log2(q)
        rows.append({"q": str(q), "q_bits": q.bit_length(),
                     "2^256_minus_q": str(2**256 - q),
                     "coset_term_log2_lower": str(float(lo)),
                     "coset_term_log2_upper": str(float(hi)),
                     "exceeds_2^21": bool(lo > 21)})
        print(f"O3* admissible official prime q = 2^256 - {2**256-q} "
              f"(q = 1 + k*2^41, prime, < 2^256):  log2 of the coset stratum's "
              f"contribution to E_MF[q^delta] in [{float(lo):.6f}, {float(hi):.6f}] "
              f"-> exceeds 2^21: {lo > 21}")
    out["large_q_rows"] = rows

    # small-q end of the admissible range
    small = []
    k = 1
    while len(small) < 2:
        q = 1 + k * 2**41
        if sympy.isprime(q):
            small.append(q)
        k += 1
    srows = []
    for q in small:
        lg = T * (Fraction(q.bit_length() - 1)) + 128 - N     # log2 q >= bits-1
        srows.append({"q": str(q), "coset_term_log2_upper_bound": str(float(
            T * Fraction(q.bit_length()) + 128 - N))})
        print(f"O3* small admissible prime q = {q}: coset contribution "
              f"<= 2^({float(T*Fraction(q.bit_length()) + 128 - N):.6g}) -- "
              f"utterly negligible")
    out["small_q_rows"] = srows

    # O4: the per-block main term IS the marginal-baseline r_j
    print("O4  the per-block nullity main term q^{ell_j} * 2^{-N_j} = "
          "q^{ell_j}/2^{256 ell_j} is verbatim the r_j of "
          "dli_marginal_baseline100_coverage (E_j - 1 <= 4 r_j (1 + W_cl))")
    out["O4"] = ("per-block nullity main term = q^{ell_j}/2^{256 ell_j} = r_j "
                 "of dli_marginal_baseline100_coverage")
    (HERE / "results" / "official_scale.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
