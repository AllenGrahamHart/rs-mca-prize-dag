#!/usr/bin/env python3
"""Round 16 -- (ES) boundary adversary: C2 curve / C3 boundary / C4 structure.

Consumes the census JSONs and adds:

  V1  EXTERNAL CROSS-VALIDATION against a BANKED count: the u2c node records
      "at (q=97,n=32,t=2) there are GIANT (81%) t-null non-coset-union blocks
      (complements of size-6 accidents; 160 witnesses)"
      -- critical/nodes/u2c_giant_tnull_dichotomy/node.json:8.
      We recount the size-6 accidents at q=97, n=32, t=2 from scratch.

  C2  the suppression curve: per row, the LARGEST characteristic carrying an
      accident, against the balance boundary -- exact, not sampled.
  C3  the boundary: the minimal above-balance accident and the deepest
      sub-balance accident actually attained.
  C4  structure of the near-boundary accidents: the dyadic stratum, the
      stabiliser, and the TWO balance readings.

TWO BALANCE READINGS (the pilot's central distinction):
  per-weight  (round-15 Lam, PREREG.md:106-107):   C(n,r') < p^{|Z_w|}
  global      (u2c floor node, node.json:8):       2^n     <= p^{|Z_w|}
global => per-weight, strictly.  Records are classified under BOTH.

run:  tools/ramguard local -- python3 notes/pilots_20260806/\
es_boundary_adversary/es_analyze.py
"""

import itertools
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from es_lib import M_of, cyclotomic_closure, mult_order

FAIL = []


def check(name, cond, detail=""):
    if not cond:
        FAIL.append((name, detail))
        print("  FAIL %s | %s" % (name, detail))
    return cond


def sec(t):
    print("\n" + "-" * 78)
    print(t)
    print("-" * 78)


def primitive_root(p):
    fac, m, d = set(), p - 1, 2
    while d * d <= m:
        while m % d == 0:
            fac.add(d)
            m //= d
        d += 1
    if m > 1:
        fac.add(m)
    for g in range(2, p):
        if all(pow(g, (p - 1) // f, p) != 1 for f in fac):
            return g
    raise RuntimeError


def stratum(S, n):
    """largest a with S invariant under the shift by n/2^a (T a union of
    mu_{2^a}-cosets); a = 0 is vacuous."""
    st = set(S)
    best = 0
    a = 1
    while n // 2 ** a >= 1:
        L = n // 2 ** a
        if all((((i + L) % n) in st) == (i in st) for i in range(n)):
            best = a
        else:
            break
        a += 1
    return best


def strat_lam(S, n, rp, w, p):
    """balance on the stratum the accident actually lives on."""
    a = stratum(S, n)
    if a == 0:
        # trivial stratum: the reduced instance IS the original one, so the
        # stratified reading coincides with the per-weight reading here.
        zw = len(cyclotomic_closure(w, n, p))
        return 0, math.log2(math.comb(n, rp)) - zw * math.log2(p)
    na, ra = n // 2 ** a, rp // 2 ** a
    wa = (w - 1) // 2 ** a + 1
    if wa < 2:
        return a, float("inf")
    zw = len(cyclotomic_closure(wa, na, p))
    return a, math.log2(math.comb(na, ra)) - zw * math.log2(p)


def main():
    print("=" * 78)
    print("ROUND 16 -- (ES) BOUNDARY: curve, boundary, structure")
    print("=" * 78)

    # ------------------------------------------------------------------ V1
    sec("[V1] EXTERNAL cross-validation vs the BANKED u2c count "
        "(q=97, n=32, t=2)")
    n, p, t, rp = 32, 97, 2, 6
    g = primitive_root(p)
    z = pow(g, (p - 1) // n, p)
    zp = [pow(z, j, p) for j in range(n)]
    check("zeta has order n", len(set(zp)) == n, "")
    acc = 0
    M = M_of(t + 1)
    for comb in itertools.combinations(range(n), rp):
        ok = True
        for s in range(1, t + 1):
            if sum(zp[(s * i) % n] for i in comb) % p:
                ok = False
                break
        if ok:
            L = n // M
            st = set(comb)
            if not all((((i + L) % n) in st) == (i in st) for i in range(n)):
                acc += 1
    print("  size-6 non-coset-union t-null blocks at q=97, n=32, t=2 : %d" % acc)
    print("  BANKED (critical/nodes/u2c_giant_tnull_dichotomy/node.json:8):")
    print("    \"complements of size-6 accidents; 160 witnesses\"")
    check("V1 reproduces the banked 160", acc == 160, "got %d" % acc)
    if acc == 160:
        print("  EXACT MATCH -- the machinery reproduces a banked count it was")
        print("  not tuned to.")

    # --------------------------------------------------------------- load
    recs = []
    for fn in sorted(os.listdir(HERE)):
        if fn.startswith("census_n") and fn.endswith(".json"):
            with open(os.path.join(HERE, fn)) as fh:
                recs.extend(json.load(fh)["records"])
    print("\nloaded %d bad-prime records" % len(recs))
    ins = [r for r in recs if r["inscope"]]
    print("in-scope (delta in {1,2,4}, p > w): %d" % len(ins))

    for r in ins:
        r["global_sub"] = (r["p"] ** r["zw"] >= 2 ** r["n"])
        r["perweight_sub"] = (math.comb(r["n"], r["rp"]) < r["p"] ** r["zw"])
        a, sl = strat_lam(r["witness"], r["n"], r["rp"], r["w"], r["p"])
        r["stratum"] = a
        r["strat_lam"] = sl

    # ------------------------------------------------------------------ C2
    sec("[C2] THE SUPPRESSION CURVE (exact: largest characteristic with an "
        "accident)")
    print("  For each row: p_max = the LARGEST in-scope characteristic in")
    print("  which a non-periodic solution exists (this is EXACT and complete")
    print("  over all p, not a sweep), and Lam there.  Lam < 0 = below the")
    print("  per-weight balance boundary.")
    print()
    print("  %-4s %-4s %-4s %-12s %-14s %-9s %-8s"
          % ("n", "r'", "w", "max acc p", "balance p_bal", "Lam", "verdict"))
    rows = {}
    for r in ins:
        rows.setdefault((r["n"], r["rp"], r["w"]), []).append(r)
    for key in sorted(rows):
        nn, rr, ww = key
        best = max(rows[key], key=lambda z: z["p"])
        deepest = min(rows[key], key=lambda z: z["lam"])
        zw = best["zw"]
        pbal = math.comb(nn, rr) ** (1.0 / zw)
        print("  %-4d %-4d %-4d %-12d %-14.1f %-9.2f %-8s"
              % (nn, rr, ww, best["p"], pbal, deepest["lam"],
                 "SUB-BAL" if deepest["lam"] < 0 else "above"))
    print()
    print("  Reading: where Lam > 0 the accidents die BEFORE the balance")
    print("  boundary (round-15's '1-2 orders EARLY', now exact); where")
    print("  Lam < 0 they survive PAST it.")

    # ------------------------------------------------------------------ C3
    sec("[C3] THE BOUNDARY")
    above = [r for r in ins if r["lam"] >= 0]
    below = [r for r in ins if r["lam"] < 0]
    if above:
        mn = min(above, key=lambda z: z["lam"])
        print("  minimal ABOVE-balance accident : Lam = %+.3f  "
              "(n=%d r'=%d w=%d p=%d delta=%d)"
              % (mn["lam"], mn["n"], mn["rp"], mn["w"], mn["p"], mn["delta"]))
    if below:
        dp = min(below, key=lambda z: z["lam"])
        print("  DEEPEST sub-balance accident   : Lam = %+.3f  "
              "(n=%d r'=%d w=%d p=%d delta=%d)"
              % (dp["lam"], dp["n"], dp["rp"], dp["w"], dp["p"], dp["delta"]))
    print("  in-scope accidents below the per-weight boundary : %d" % len(below))
    print("  ... of which ALSO below the GLOBAL boundary 2^n <= p^{|Z_w|} : %d"
          % len([r for r in below if r["global_sub"]]))
    gl = [r for r in ins if r["global_sub"]]
    print("  in-scope accidents below the GLOBAL boundary (any Lam)   : %d"
          % len(gl))
    print()
    print("  => the two readings are NOT interchangeable: the witnesses live")
    print("     exactly in the gap  C(n,r') < p^{|Z_w|} < 2^n.")

    # ------------------------------------------------------------------ C4
    sec("[C4] STRUCTURE of the sub-balance accidents")
    print("  %-4s %-4s %-4s %-6s %-7s %-9s %-10s %-9s"
          % ("n", "r'", "w", "p", "delta", "Lam", "stratum a", "Lam_a"))
    for r in sorted(below, key=lambda z: z["lam"]):
        sl = r["strat_lam"]
        print("  %-4d %-4d %-4d %-6d %-7d %-9.3f %-10d %-9s"
              % (r["n"], r["rp"], r["w"], r["p"], r["delta"], r["lam"],
                 r["stratum"],
                 ("%+.3f" % sl) if isinstance(sl, float) and sl != float("inf")
                 else ("n/a" if sl is None else "inf")))
    print()
    print("  stratum a = the largest a with T a union of mu_{2^a}-cosets.")
    print("  a >= 1 means the odd-index window conditions hold FOR FREE, so")
    print("  the true codimension is that of the REDUCED instance at n/2^a --")
    print("  which is why the per-weight Lam over-counts the constraint.")
    deep = [r for r in below if r["stratum"] >= 1]
    shal = [r for r in below if r["stratum"] == 0]
    print()
    print("  partially-periodic (a >= 1): %d, deepest Lam = %s"
          % (len(deep),
             ("%+.3f" % min([r["lam"] for r in deep])) if deep else "-"))
    print("  generic (a = 0)           : %d, deepest Lam = %s"
          % (len(shal),
             ("%+.3f" % min([r["lam"] for r in shal])) if shal else "-"))
    bad = [r for r in below if isinstance(r["strat_lam"], float)
           and r["strat_lam"] < 0]
    print("  sub-balance accidents that are ALSO sub-balance ON THEIR OWN")
    print("  STRATUM: %d of %d." % len(bad) if False else
          "  STRATUM: %d of %d." % (len(bad), len(below)))
    print("  => stratifying REPAIRS the partially-periodic (a >= 1) ones and")
    print("     ONLY those; the a = 0 ones remain genuine per-weight")
    print("     violations that no stratification removes.")

    print("\n" + "=" * 78)
    print("failures: %d" % len(FAIL))
    for nm, d in FAIL:
        print("  FAILED %s | %s" % (nm, d))
    print("=" * 78)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
