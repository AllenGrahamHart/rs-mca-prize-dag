#!/usr/bin/env python3
"""dli_norm_gate -- THE CENSUS BRIDGE.

Claim ID1: at junction 0 with t = 2 (o = L_0 = 1) the C2'' skew-solution space
at (n, q) IS the C1 ternary-relation space at 2N = n, N = phi(n) = n/2.  So the
"skew-norm ladder" IS the C1 norm ladder and the skew census IS the C1
exceptional-prime census, only stratified by SUPPORT instead of by WEIGHT.

This script tests that by rebuilding the census from the SKEW side, through an
independent code path (negacyclic field-norm descent + smallest-prime-factor
sieve; the C1 pilot used Bareiss/int64-descent/sympy, the C2'' pilot used
Bareiss), and comparing with the banked numbers.
"""

from __future__ import annotations

import json
import sys
from itertools import combinations, product as iproduct
from pathlib import Path

sys.dont_write_bytecode = True

import numpy as np

from core import admissible_primes, get_zeta, norm_cyclotomic

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
C1 = ROOT.parent / "c1_norm_ladder" / "results"

BANKED_2N16_CENSUS = {17: 3, 97: 4, 113: 5, 193: 5, 241: 5, 337: 7, 353: 6,
                      401: 5, 433: 5, 577: 6, 881: 7}
BANKED_2N32_W3 = [97, 193, 257, 353, 449]
BANKED_2N32_W4 = [97, 193, 257, 353, 449, 577, 641, 673, 929, 1153, 1217, 1249,
                  1409, 2113, 2273, 2593, 2689, 3137, 3457, 4001, 4129, 4993,
                  5857, 7937]
BANKED_2N32_W5_COUNT = 160


# ---------------------------------------------------------- negacyclic norm
def _negconv(a, b, m):
    """negacyclic product mod y^m+1, batched: a,b are (K,m) int64."""
    K = a.shape[0]
    out = np.zeros((K, m), dtype=np.int64)
    for i in range(m):
        ai = a[:, i:i + 1]
        for j in range(m):
            e = i + j
            if e < m:
                out[:, e] += ai[:, 0] * b[:, j]
            else:
                out[:, e - m] -= ai[:, 0] * b[:, j]
    return out


def norms_batch(A):
    """Norm_{Z[x]/(x^h+1)}(alpha) for each row of A (K,h) int64, exact in int64.

    Field-norm descent: f(x)f(-x) = g(x^2) with g = f_e^2 - y f_o^2 in
    Z[y]/(y^{h/2}+1), so Norm_h(f) = Norm_{h/2}(g); base h=1 gives the coeff.
    """
    A = np.asarray(A, dtype=np.int64)
    m = A.shape[1]
    while m > 1:
        fe = A[:, 0::2]
        fo = A[:, 1::2]
        mm = m // 2
        g = _negconv(fe, fe, mm)
        yfo2 = _negconv(fo, fo, mm)
        # multiply yfo2 by y (negacyclic shift) then subtract
        sh = np.empty_like(yfo2)
        sh[:, 0] = -yfo2[:, mm - 1]
        sh[:, 1:] = yfo2[:, :mm - 1]
        A = g - sh
        m = mm
    return A[:, 0]


def ternary_weight_block(h, w):
    """all ternary vectors of weight exactly w, as an (K,h) int64 array."""
    supports = list(combinations(range(h), w))
    signs = np.array(list(iproduct((1, -1), repeat=w)), dtype=np.int64)
    K = len(supports) * len(signs)
    A = np.zeros((K, h), dtype=np.int64)
    r = 0
    ns = len(signs)
    for S in supports:
        A[r:r + ns][:, list(S)] = signs
        r += ns
    return A


def spf_sieve(limit):
    spf = np.zeros(limit + 1, dtype=np.int64)
    for i in range(2, limit + 1):
        if spf[i] == 0:
            spf[i::i] = np.where(spf[i::i] == 0, i, spf[i::i])
    return spf


def factor_with(spf, x):
    out = set()
    while x > 1:
        p = int(spf[x])
        out.add(p)
        while x % p == 0:
            x //= p
    return out


# ---------------------------------------------------------- (a) n = 16
def census_n16():
    h, n = 8, 16
    A = np.array([list(c) for c in iproduct((-1, 0, 1), repeat=h)
                  if any(c)], dtype=np.int64)
    Nz = norms_batch(A)
    # exact cross-check against the Bareiss reference on a sample
    idx = list(range(0, len(A), 977))
    bad = sum(1 for i in idx if norm_cyclotomic(list(A[i]), h) != int(Nz[i]))
    wts = (A != 0).sum(axis=1)
    qs = admissible_primes(n, 2, 3000)
    got = {}
    for q in qs:
        z = get_zeta(q, n)
        pw = np.array([pow(z, i, q) for i in range(h)], dtype=np.int64)
        val = (A % q) @ pw % q
        sol = np.nonzero(val == 0)[0]
        if len(sol):
            got[q] = int(wts[sol].min())
    return {"n": n, "descent_vs_bareiss_mismatches": bad,
            "n_sampled_for_bareiss": len(idx),
            "skew_side_census": {str(k): v for k, v in sorted(got.items())},
            "banked_C1_2N16_census": {str(k): v for k, v in BANKED_2N16_CENSUS.items()},
            "identical": got == BANKED_2N16_CENSUS,
            "n_admissible_scanned": len(qs)}


# ---------------------------------------------------------- (b) n = 32, w<=5
def census_n32_low():
    h, n = 16, 32
    T5 = 279841
    spf = spf_sieve(T5)
    per_w = {}
    minw = {}
    for w in range(1, 6):
        A = ternary_weight_block(h, w)
        Nz = norms_batch(A)
        assert (Nz > 0).all(), "norm positivity"
        mx = int(Nz.max())
        primes = set()
        for v in np.unique(Nz):
            for p in factor_with(spf, int(v)):
                if p % n == 1:
                    primes.add(p)
        for p in primes:
            minw.setdefault(p, w)
        per_w[w] = {"maxnorm": mx, "ceiling_w^(h/2)": w**(h // 2),
                    "n_vectors": int(A.shape[0]),
                    "n_admissible_prime_divisors_cum": len(minw),
                    "new_primes": sorted(p for p in primes if minw[p] == w)}
    w3 = sorted(p for p, v in minw.items() if v <= 3)
    w4 = sorted(p for p, v in minw.items() if v <= 4)
    w5 = sorted(p for p, v in minw.items() if v <= 5)
    return {"n": n, "per_w": {str(k): v for k, v in per_w.items()},
            "w<=3": w3, "w<=3_matches_banked": w3 == BANKED_2N32_W3,
            "w<=4_count": len(w4), "w<=4_matches_banked": w4 == BANKED_2N32_W4,
            "w<=5_count": len(w5),
            "w<=5_matches_banked_count": len(w5) == BANKED_2N32_W5_COUNT}


# ---------------------------------------------------------- (c) 70529
def check_70529():
    h, n, q = 16, 32, 70529
    f = [1, 1, 1, 1, 0, -1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    Nz = norm_cyclotomic(f, h)
    z = get_zeta(q, n)
    # the banked witness is a relation for SOME primitive root; find which
    hits = [j for j in range(1, n, 2)
            if sum(c * pow(pow(z, j, q), i, q) for i, c in enumerate(f)) % q == 0]
    # global-max full-weight norm at 2N=32
    A = ternary_weight_block(h, 16)
    Nz16 = norms_batch(A)
    gmax = int(Nz16.max())
    return {"q": 70529, "admissible_mod_32": q % n == 1,
            "banked_witness_norm": Nz, "norm_equals_q": Nz == q,
            "n_primitive_roots_annihilated": len(hits), "which_odd_j": hits,
            "full_weight_maxnorm_2N32": gmax,
            "factorisation_check": {"2^15*70529": 2**15 * 70529,
                                    "equals_gmax": 2**15 * 70529 == gmax}}


def main():
    out = {}
    out["a_n16"] = census_n16()
    print("n=16 skew census identical to banked C1 2N=16 census:",
          out["a_n16"]["identical"],
          "| descent-vs-Bareiss mismatches:",
          out["a_n16"]["descent_vs_bareiss_mismatches"])
    out["b_n32_low"] = census_n32_low()
    b = out["b_n32_low"]
    print("n=32 w<=3 matches:", b["w<=3_matches_banked"],
          "| w<=4 matches:", b["w<=4_matches_banked"],
          f"({b['w<=4_count']} primes)",
          "| w<=5 count:", b["w<=5_count"], "matches:",
          b["w<=5_matches_banked_count"])
    for w, r in b["per_w"].items():
        print(f"   w={w}: maxnorm={r['maxnorm']} ceiling={r['ceiling_w^(h/2)']}"
              f" saturates={r['maxnorm']==r['ceiling_w^(h/2)']}")
    out["c_70529"] = check_70529()
    print("70529:", json.dumps(out["c_70529"]))
    (ROOT / "results" / "bridge.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
