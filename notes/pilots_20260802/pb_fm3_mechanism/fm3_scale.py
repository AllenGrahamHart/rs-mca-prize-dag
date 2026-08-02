#!/usr/bin/env python3
"""FM3 mechanism pilot -- scaling study of the validated greedy-depletion model.

Two questions the banked grid cannot answer directly:

  (1) how does P[core >= K] for the selected family scale with n at FIXED
      rate and FIXED witness density?
  (2) what does the model say at the official RowC scales (n = 1024)?

The model is the parameter-free greedy-depletion chain validated in
fm3_mine.py (ratio observed/model = 0.78-1.35 at every n=32 point with
>= 1700 witnesses/slope).  Everything here is a MODEL EXTRAPOLATION and is
labelled as such.

For large n the exact 3-index overlap DP is replaced by the Poisson-binomial
approximation  core ~ sum_i Bern(p_i * p_i); the two are cross-checked
against each other at every n = 16/32 point first.
"""
from __future__ import annotations
import json
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, _HERE)
from fm3_mine import greedy_pi, greedy_marginals, greedy_overlap, tail  # noqa


def poibin_overlap(p):
    """law of sum_i Bern(p_i^2)  (independent-coordinate approximation)."""
    dist = [1.0]
    for pi in p:
        pp = pi * pi
        nd = [0.0] * (len(dist) + 1)
        for t, v in enumerate(dist):
            if v == 0.0:
                continue
            nd[t] += v * (1 - pp)
            nd[t + 1] += v * pp
        # prune
        while len(nd) > 1 and nd[-1] < 1e-300:
            nd.pop()
        dist = nd
    return dist


def model(n, A, K, q, h, prefer_include=True, exact=True):
    pi = greedy_pi(n, A, q, h, prefer_include)
    marg = greedy_marginals(pi, n, A)
    chi = sum(p * p for p in marg)
    var = sum(p * p * (1 - p * p) for p in marg)
    pb = poibin_overlap(marg)
    out = dict(n=n, A=A, K=K, q=q, h=h,
               block100=sum(1 for p in marg if p > 1 - 1e-9),
               block90=sum(1 for p in marg if p >= 0.90),
               chi=chi, sd=math.sqrt(var) if var > 0 else 0.0,
               sigma_gap=((K - chi) / math.sqrt(var)) if var > 0 else float("inf"),
               p_ge_K_poibin=sum(pb[K:]) if K < len(pb) else 0.0,
               marg=marg)
    if exact:
        ov = greedy_overlap(pi, n, A)
        out["p_ge_K_exact"] = tail(ov, K)
        out["chi_exact"] = sum(t * ov[t] for t in range(len(ov)))
    return out


def main():
    res = {}

    print("=" * 104)
    print("A. cross-check: exact overlap DP vs Poisson-binomial approximation "
          "(model internal)")
    print("=" * 104)
    print(f"{'n':>4s} {'A':>3s} {'K':>3s} {'q':>5s} {'h':>2s} {'chi':>7s} "
          f"{'chi_ex':>7s} {'sd':>6s} {'gap/sd':>7s} {'P_exact':>10s} "
          f"{'P_poibin':>10s} {'ratio':>7s}")
    grid = [(16, 6, 4, 17, 2), (16, 7, 4, 17, 3), (16, 6, 4, 97, 2),
            (32, 10, 8, 97, 2), (32, 10, 8, 193, 2), (32, 10, 8, 449, 2),
            (32, 11, 8, 97, 3), (32, 11, 8, 193, 3),
            (32, 18, 16, 97, 2), (32, 18, 16, 193, 2), (32, 19, 16, 97, 3),
            (32, 13, 8, 97, 5)]
    xcheck = []
    for n, A, K, q, h in grid:
        m = model(n, A, K, q, h, True, exact=True)
        r = (m["p_ge_K_poibin"] / m["p_ge_K_exact"]
             if m["p_ge_K_exact"] > 0 else float("nan"))
        xcheck.append(dict(n=n, A=A, K=K, q=q, h=h,
                           exact=m["p_ge_K_exact"],
                           poibin=m["p_ge_K_poibin"], ratio=r))
        print(f"{n:4d} {A:3d} {K:3d} {q:5d} {h:2d} {m['chi']:7.3f} "
              f"{m['chi_exact']:7.3f} {m['sd']:6.3f} {m['sigma_gap']:7.2f} "
              f"{m['p_ge_K_exact']:10.3e} {m['p_ge_K_poibin']:10.3e} "
              f"{r:7.3f}")
    res["poibin_crosscheck"] = xcheck

    print()
    print("=" * 104)
    print("B. n-scaling at FIXED rate 1/4 (K = n/4, A = K + h, h = m = 2) and "
          "matched witness density")
    print("=" * 104)
    print(f"{'n':>5s} {'K':>5s} {'A':>4s} {'q':>10s} {'|W_z|':>12s} "
          f"{'L*':>4s} {'K-L*':>5s} {'A-L*':>5s} {'chi':>9s} {'sd':>7s} "
          f"{'(K-chi)/sd':>10s} {'P[core>=K]':>12s} {'q*P':>11s}")
    rows = []
    for n in [16, 24, 32, 40, 48, 64, 96, 128, 256, 512, 1024]:
        K = n // 4
        h = 2
        A = K + h
        CnA = math.comb(n, A)
        for dens in [1e2, 1e4, 1e6]:
            # q chosen so that C(n,A)/q^h ~ dens
            q = max(3.0, (CnA / dens) ** (1.0 / h))
            W = CnA / q ** h
            mm = model(n, A, K, q, h, True, exact=(n <= 32))
            P = mm["p_ge_K_poibin"]
            rows.append(dict(n=n, K=K, A=A, q=q, W=W, dens=dens,
                             L=mm["block100"], chi=mm["chi"], sd=mm["sd"],
                             sigma=mm["sigma_gap"], P=P, qP=q * P))
            print(f"{n:5d} {K:5d} {A:4d} {q:10.3g} {W:12.3g} "
                  f"{mm['block100']:4d} {K-mm['block100']:5d} "
                  f"{A-mm['block100']:5d} {mm['chi']:9.2f} {mm['sd']:7.3f} "
                  f"{mm['sigma_gap']:10.2f} {P:12.3e} {q*P:11.3e}")
        print("-" * 104)
    res["rate_quarter_scaling"] = rows

    print()
    print("=" * 104)
    print("C. n-scaling at FIXED rate 1/2 (K = n/2, A = K+2), matched density")
    print("=" * 104)
    rows = []
    for n in [16, 32, 44, 48, 64, 128, 256, 512, 1024]:
        K = n // 2
        h = 2
        A = K + h
        CnA = math.comb(n, A)
        for dens in [1e2, 1e4, 1e6]:
            q = max(3.0, (CnA / dens) ** (1.0 / h))
            mm = model(n, A, K, q, h, True, exact=False)
            P = mm["p_ge_K_poibin"]
            rows.append(dict(n=n, K=K, A=A, q=q, dens=dens, L=mm["block100"],
                             chi=mm["chi"], sd=mm["sd"], sigma=mm["sigma_gap"],
                             P=P, qP=q * P))
            print(f"{n:5d} {K:5d} {A:4d} {q:10.3g} {CnA/q**h:12.3g} "
                  f"{mm['block100']:4d} {K-mm['block100']:5d} "
                  f"{A-mm['block100']:5d} {mm['chi']:9.2f} {mm['sd']:7.3f} "
                  f"{mm['sigma_gap']:10.2f} {P:12.3e} {q*P:11.3e}")
        print("-" * 104)
    res["rate_half_scaling"] = rows

    print()
    print("=" * 104)
    print("D. OFFICIAL-SCALE extrapolation (n = N = 1024, split-fibre m = 4, "
          "h = 5, A = K + 5)")
    print("=" * 104)
    print(f"{'row':10s} {'K':>5s} {'A':>5s} {'q':>12s} {'log2|W_z|':>10s} "
          f"{'L*':>5s} {'K-L*':>5s} {'A-L*':>5s} {'chi':>9s} {'sd':>7s} "
          f"{'(K-chi)/sd':>10s} {'log2 P':>9s} {'log2(q P)':>10s}")
    rows = []
    offi = [("RowC 1/4", 1024, 256, 5, 4, 1.3e11),
            ("RowC 1/4", 1024, 256, 5, 4, 12289.0),
            ("RowC 1/2", 1024, 512, 5, 4, 1.3e11),
            ("RowC 1/2", 1024, 512, 5, 4, 12289.0)]
    for tag, n, K, h, m, q in offi:
        A = K + h
        CnA = math.comb(n, A)
        W = CnA / q ** h
        mm = model(n, A, K, q, h, True, exact=False)
        P = mm["p_ge_K_poibin"]
        l2P = math.log2(P) if P > 0 else float("-inf")
        rows.append(dict(tag=tag, n=n, K=K, A=A, q=q, h=h, m=m,
                         log2W=math.log2(W) if W > 0 else None,
                         L=mm["block100"], chi=mm["chi"], sd=mm["sd"],
                         sigma=mm["sigma_gap"], log2P=l2P,
                         log2qP=(l2P + math.log2(q)) if P > 0 else None))
        print(f"{tag:10s} {K:5d} {A:5d} {q:12.4g} "
              f"{math.log2(W):10.1f} {mm['block100']:5d} "
              f"{K-mm['block100']:5d} {A-mm['block100']:5d} {mm['chi']:9.1f} "
              f"{mm['sd']:7.3f} {mm['sigma_gap']:10.1f} {l2P:9.1f} "
              f"{(l2P + math.log2(q)):10.1f}")
    res["official_extrapolation"] = rows

    print()
    print("=" * 104)
    print("E. POPULATION-LEVEL feasibility: expected number of >=K-core "
          "partners per witness (exact counting, no selector)")
    print("=" * 104)
    print("   partners(S) ~ sum_{c=K..A-m} C(A,A-c) * C(n-c, A-c) / q^(h-1) "
          "  [choose the core inside S, complete it elsewhere]")
    print(f"{'tag':12s} {'n':>5s} {'K':>5s} {'A':>4s} {'m':>2s} {'h':>2s} "
          f"{'q':>12s} {'log2 partners':>14s}")
    rows = []
    pts = [("Q9", 32, 16, 18, 2, 2, 97), ("Q4", 32, 8, 10, 2, 2, 97),
           ("Q6", 32, 8, 10, 2, 2, 449), ("Q8", 32, 8, 11, 2, 3, 193),
           ("n=44 r1/2", 44, 22, 24, 2, 2, 1327217),
           ("RowC1/4 sm", 1024, 256, 261, 4, 5, 12289),
           ("RowC1/4 big", 1024, 256, 261, 4, 5, 1.3e11),
           ("RowC1/2 big", 1024, 512, 517, 4, 5, 1.3e11)]
    for tag, n, K, A, m, h, q in pts:
        tot = 0.0
        for c in range(K, A - m + 1):
            tot += math.comb(A, A - c) * math.comb(n - c, A - c) / q ** (h - 1)
        rows.append(dict(tag=tag, n=n, K=K, A=A, m=m, h=h, q=q,
                         log2_partners=(math.log2(tot) if tot > 0
                                        else float("-inf"))))
        print(f"{tag:12s} {n:5d} {K:5d} {A:4d} {m:2d} {h:2d} {q:12.4g} "
              f"{(math.log2(tot) if tot > 0 else float('-inf')):14.2f}")
    res["population_partner_count"] = rows

    with open(os.path.join(_HERE, "SCALE.json"), "w") as fh:
        json.dump(res, fh, sort_keys=True, default=str)
    print("\n->", os.path.join(_HERE, "SCALE.json"))


if __name__ == "__main__":
    main()
