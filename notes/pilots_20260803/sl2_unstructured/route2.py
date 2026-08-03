#!/usr/bin/env python3
"""SL-2 pilot, route (2): the CORE-DISJOINTNESS union bound, computed
exactly at the six rows -- and shown INSUFFICIENT by two independent
margins.   (2026-08-03)

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 <this>

Route (2) as assigned: "> 0.68 n^2 members need massive correlation --
the CORE-DISJOINTNESS lemma caps the correlation structure; a union
bound over pairwise-nearly-disjoint cores may close it outright".
Two computations, both exact:

  (2a) THE PACKING BOUND.  CORE-DISJOINTNESS (band_heart_consolidation
       section 2, as CORRECTED): distinct MAXIMAL depth-d cores meet in
       <= k-1 points.  So no k-subset lies in two cores, giving
             N_d <= C(n, k) / C(k+d, k).
       This is the strongest bound derivable from the intersection
       pattern ALONE.  Reported in bits against the 0.68 n^2 budget.

  (2b) THE PLANTING / DIMENSION OBSTRUCTION.  A family Z_1..Z_N of
       depth-d cores forces u|_{Z_i} = f_i|_{Z_i} for codewords f_i in
       RS_k, so u is determined on U = union Z_i (|U| <= n) by the N k
       free parameters of (f_1..f_N).  A counting contradiction needs
       the determined coordinates to outnumber the parameters,
             |U| > N k,   hence   N < |U|/k <= n/k = 1/rate.
       So the counting/union-bound route can only ever exclude families
       of fewer than 1/rate members -- it dies at N = 4, 8, 16 while the
       budget is ~2^82.  This is a PROVED NEGATIVE about the route, not
       about SL-2.
"""
import json
from math import lgamma, log2

LN2 = 0.6931471805599453
ROWS = [
    dict(name="RowC 1/4", n=1024, k=256, h=5, C=None),
    dict(name="RowC 1/8", n=1024, k=128, h=5, C=None),
    dict(name="RowC 1/16", n=1024, k=64, h=3, C=None),
    dict(name="prize 1/4", n=2199023255552, k=549755813888,
         h=8589934593, C=0.800767298932776),
    dict(name="prize 1/8", n=2199023255552, k=274877906944,
         h=8589934593, C=0.6858649121282252),
    dict(name="prize 1/16", n=2199023255552, k=137438953472,
         h=4294967297, C=0.6596448038293138),
]
checks = []


def lbinom(n, j):
    if j < 0 or j > n:
        return float("-inf")
    if j == 0 or j == n:
        return 0.0
    return (lgamma(n + 1) - lgamma(j + 1) - lgamma(n - j + 1)) / LN2


def ck(name, tag, ok, extra=None):
    checks.append(dict(check=name, fixture=tag, ok=bool(ok), extra=extra))


def main():
    out = []
    for r in ROWS:
        n, k, h = r["n"], r["k"], r["h"]
        dlo, dhi = -(-h // 2), h - 2
        if dlo > dhi:
            out.append(dict(name=r["name"], band_proper_empty=True))
            continue
        budget = log2((r["C"] or 0.68) * n * n)
        rec = dict(name=r["name"], n=n, k=k, h=h,
                   band_proper=[dlo, dhi], budget_bits=budget,
                   packing=[], rate_inv=n // k)
        for d in (dlo, dhi):
            pk = lbinom(n, k) - lbinom(k + d, k)
            rec["packing"].append(dict(d=d, log2_bound=pk,
                                       excess_bits=pk - budget))
            ck("(2a) the packing bound is ASTRONOMICALLY above the "
               "budget (route insufficient)", f"{r['name']} d={d}",
               pk > budget, dict(log2_bound=pk, budget=budget))
        # (2b) the dimension obstruction dies at N = n/k
        ncrit = n // k
        rec["dimension_obstruction_N"] = ncrit
        rec["budget_over_obstruction_bits"] = budget - log2(ncrit)
        ck("(2b) the planting/dimension obstruction dies at N = 1/rate, "
           "far below the budget", r["name"], ncrit < (r["C"] or 0.68)
           * n * n, dict(N_crit=ncrit, budget_bits=budget))
        out.append(rec)

    bad = [c for c in checks if not c["ok"]]
    print(f"checks: {len(checks)}   failures: {len(bad)}")
    for b in bad:
        print("  FAIL", b)
    print()
    print(f"{'row':12s} {'d':>12s} {'packing bound':>16s} "
          f"{'budget':>9s} {'excess':>14s} {'dim-obstr N':>12s}")
    for rec in out:
        if rec.get("band_proper_empty"):
            print(f"{rec['name']:12s}  band proper EMPTY")
            continue
        for i, p in enumerate(rec["packing"]):
            print(f"{rec['name'] if i == 0 else '':12s} {p['d']:>12d} "
                  f"2^{p['log2_bound']:<14.4g} {rec['budget_bits']:>9.2f} "
                  f"2^{p['excess_bits']:<13.4g} "
                  f"{rec['dimension_obstruction_N'] if i == 0 else '':>12}")
    with open(__file__.replace(".py", ".json"), "w") as fh:
        json.dump(dict(rows=out, checks=checks, n_checks=len(checks),
                       n_fail=len(bad),
                       verdict="PASS" if not bad else "FAIL"), fh, indent=1)


if __name__ == "__main__":
    main()
