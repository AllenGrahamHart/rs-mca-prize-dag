#!/usr/bin/env python3
"""FULL-RANK leaf pilot: does the SURVIVING structured class route to
this leaf?  And how large can a FULL-RANK family be?   (2026-08-04)

PROFILE: local.   Run:  tools/ramguard local -- python3 <this>

THIRD-ROUND PRE-REGISTRATION (written before this file was run):

  E1  ONE-CLASS (coset) PENCILS.  Let the syndrome window of u be
      supported in the residue class a mod M and that of v in class b
      (M | gcd(n,k,d); a != b is the P3-evading mixed-class case that
      survives the strips).  A stacked-rank deficiency splits by residue
      class into M independent quotient-level Pade syzygies, so a
      GENERIC one-class pair should have NO syzygy.
      PREDICT: coset pencils are generically FULL rank -- both for
      a != b and a = b -- and become deficient exactly when the pair is
      shift-related (part A of rankstrat.py).  CONSEQUENCE if it fires:
      the coset scales M = 2..2^20 that survive THEOREM L at the prize
      rows (rows.py R3) route to THIS leaf, not to the sibling.
  E2  FULL-RANK-CONSTRAINED EXTREMAL SEARCH.  Greedily grow a divisor
      family subject to the constraint that the 2-plane stays FULL rank
      (rank J_d = 2d).  PREDICT: the constrained maximum is >= 2 and
      grows with the affine window dimension r'-2d; i.e. the full-rank
      stratum is NOT limited to singleton families.
  E3  The full-rank families found are checked against the tangent gate
      and band-properness.  PREDICT: at toy rows they are NOT
      band-proper (toy subcriticality, PREREG P5), so nothing here is a
      count claim.
"""
import json
import os
import random
import sys
from itertools import combinations
from math import comb, log2

_HERE = os.path.dirname(os.path.abspath(__file__))
_SIB = os.path.normpath(os.path.join(_HERE, "..", "..",
                                     "pilots_20260803", "sl2_unstructured"))
sys.path.insert(0, _SIB)
sys.path.insert(0, _HERE)
from algebra import (evalpoly, rank, root_of_unity)      # noqa: E402
from dualform import spanrank, toeplitz                  # noqa: E402
from rankstrat import (analyse_family, annihilator_of_divisor,  # noqa: E402
                       family_of, nullspace, rref_span, syn_of,
                       try_add, word_from_syndrome)

random.seed(20260805)
checks = []


def ck(name, tag, ok, extra=None):
    checks.append(dict(check=name, fixture=tag, ok=bool(ok), extra=extra))
    return bool(ok)


def rankJ(su, sv, n, k, d, q):
    rp = n - k - d
    u = word_from_syndrome(su, n, k)
    v = word_from_syndrome(sv, n, k)
    return rank(toeplitz(u, n, d, rp) + toeplitz(v, n, d, rp), q)


def main():
    out = {}

    # ============================================ E1: one-class pencils
    E1 = []
    for f in [dict(n=16, k=4, q=97, d=4, M=2), dict(n=16, k=4, q=97, d=4, M=4),
              dict(n=16, k=8, q=17, d=2, M=2), dict(n=12, k=4, q=13, d=2, M=2),
              dict(n=20, k=8, q=41, d=4, M=2), dict(n=20, k=8, q=41, d=4, M=4)]:
        n, k, q, d, M = f["n"], f["k"], f["q"], f["d"], f["M"]
        rp = n - k - d
        assert d % M == 0 and n % M == 0 and k % M == 0
        for (a, b) in [(0, 1), (0, 0), (1, 1), (0, M - 1)]:
            if a >= M or b >= M:
                continue
            full = 0
            trials = 12
            ranks = {}
            for _ in range(trials):
                su = [0] * (n - k)
                sv = [0] * (n - k)
                for j in range(n - k):
                    if (k + j) % M == a:
                        su[j] = random.randrange(1, q)
                    if (k + j) % M == b:
                        sv[j] = random.randrange(1, q)
                if spanrank([su, sv], q) < 2:
                    continue
                rJ = rankJ(su, sv, n, k, d, q)
                ranks[rJ] = ranks.get(rJ, 0) + 1
                full += (rJ == min(2 * d, rp + 1))
            E1.append(dict(n=n, k=k, q=q, d=d, M=M, a=a, b=b,
                           full=full, trials=trials, ranks=ranks,
                           cap=min(2 * d, rp + 1)))
            # AS FIRST WRITTEN this demanded full rank in EVERY draw;
            # over a toy field (q=41) a one-class pair can pick up an
            # ACCIDENTAL syzygy.  Recorded as failed where it fires; the
            # substantive form is E1' (generic = large majority).
            ck("E1 [AS FIRST WRITTEN, universal quantifier -- recorded "
               "as failed where it fires]: one-class pencils are FULL "
               "rank in every draw",
               f"n{n}k{k}d{d}M{M}a{a}b{b}", full == trials,
               dict(full=full, trials=trials, ranks=ranks))
            ck("E1': GENERIC one-class (coset) pencils are stacked-FULL "
               "rank -- the surviving structured scales route to THIS leaf",
               f"n{n}k{k}d{d}M{M}a{a}b{b}", full >= 0.9 * trials,
               dict(full=full, trials=trials, ranks=ranks))
    out["E1_coset_rank"] = E1

    # ================================ E2/E3: full-rank extremal search
    E2 = []
    for f in [dict(n=14, k=4, q=29, d=3, trials=60, cand=700),
              dict(n=16, k=4, q=97, d=3, trials=30, cand=700),
              dict(n=16, k=4, q=17, d=3, trials=30, cand=700)]:
        n, k, q, d = f["n"], f["k"], f["q"], f["d"]
        rp = n - k - d
        N = n - k
        g0 = root_of_unity(n, q)
        H = [pow(g0, i, q) for i in range(n)]
        Tlist = list(combinations(range(n), rp))
        WT = [annihilator_of_divisor([H[i] for i in T], n, k, d, q)
              for T in Tlist]
        best = dict(size=0, pi=None, chosen=0)
        for _ in range(f["trials"]):
            basis, pivots, chosen = [], [], []
            keep_pi = None
            order = random.sample(range(len(Tlist)),
                                  min(len(Tlist), f["cand"]))
            for idx in order:
                res = try_add(basis, pivots, WT[idx], q, N - 2)
                if res is None:
                    continue
                nb, npv = res
                ns = nullspace(rref_span(nb, q), q, N)
                if len(ns) < 2:
                    continue
                found = None
                for _try in range(6):
                    c1 = [random.randrange(q) for _ in ns]
                    c2 = [random.randrange(q) for _ in ns]
                    su = [sum(c * bb[j] for c, bb in zip(c1, ns)) % q
                          for j in range(N)]
                    sv = [sum(c * bb[j] for c, bb in zip(c2, ns)) % q
                          for j in range(N)]
                    if spanrank([su, sv], q) < 2:
                        continue
                    if rankJ(su, sv, n, k, d, q) == 2 * d:
                        found = (su, sv)
                        break
                if found is None:
                    continue                 # adding this T kills full rank
                basis, pivots = nb, npv
                chosen.append(idx)
                keep_pi = found
            if keep_pi is None:
                continue
            fam = family_of(keep_pi, WT, q)
            if len(fam) > best["size"]:
                best = dict(size=len(fam), pi=keep_pi, chosen=len(chosen),
                            fam=fam)
        rec = dict(n=n, k=k, q=q, d=d, rprime=rp, affine_dim=rp - 2 * d,
                   divisors=len(Tlist), best_fullrank_family=best["size"],
                   greedy_seeds=best["chosen"])
        if best["pi"] is not None:
            led = analyse_family(best["pi"], [Tlist[i] for i in best["fam"]],
                                 H, n, k, d, q)
            rec["ledger"] = led
            h = led["h"]
            rec["band_proper"] = (h is not None and
                                  -(-h // 2) <= d <= h - 2)
            rec["rank_check"] = rankJ(best["pi"][0], best["pi"][1],
                                      n, k, d, q)
            ck("E2: the full-rank stratum carries families of size >= 2",
               f"n{n}k{k}d{d}q{q}", best["size"] >= 2,
               dict(size=best["size"], affine_dim=rp - 2 * d))
            ck("E2b: the recorded best full-rank pi really is full rank",
               f"n{n}k{k}d{d}q{q}", rec["rank_check"] == 2 * d,
               dict(rank=rec["rank_check"], twod=2 * d))
            ck("E3 [P5]: the toy full-rank family is NOT band-proper -- "
               "no count claim follows", f"n{n}k{k}d{d}q{q}",
               not rec["band_proper"],
               dict(h=h, d=d, band=[-(-h // 2), h - 2] if h else None))
        E2.append(rec)
    out["E2_fullrank_extremal"] = E2

    bad = [c for c in checks if not c["ok"]]
    print(f"checks: {len(checks)}   failures: {len(bad)}")
    for b in bad:
        print("  FAIL", b["check"][:60], b["fixture"], b.get("extra"))
    print()
    print("--- E1: one-class (coset) pencils, rank census ---")
    for e in E1:
        print(f"  n{e['n']}k{e['k']}d{e['d']} M={e['M']} classes "
              f"(a,b)=({e['a']},{e['b']}): full rank in "
              f"{e['full']}/{e['trials']} draws   ranks={e['ranks']}  "
              f"cap={e['cap']}")
    print()
    print("--- E2: max family size subject to FULL rank ---")
    for e in E2:
        led = e.get("ledger", {})
        print(f"  n{e['n']}k{e['k']}d{e['d']}q{e['q']}: affine dim "
              f"r'-2d={e['affine_dim']}  divisors={e['divisors']}  "
              f"max full-rank family={e['best_fullrank_family']}"
              f"  maximal={led.get('maximal')}  L_P>=2={led.get('live2')}"
              f"  h={led.get('h')}  band-proper={e.get('band_proper')}")
    out["checks"] = checks
    out["n_checks"] = len(checks)
    out["n_fail"] = len(bad)
    out["verdict"] = "PASS" if not bad else "FAIL"
    with open(__file__.replace(".py", ".json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)


if __name__ == "__main__":
    main()
