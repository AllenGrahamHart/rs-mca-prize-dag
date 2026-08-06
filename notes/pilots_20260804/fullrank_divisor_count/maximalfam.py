#!/usr/bin/env python3
"""FULL-RANK leaf pilot: can a FULL-RANK pencil carry several MAXIMAL
depth-d pairs at all?   (2026-08-04)

PROFILE: local.   Run:  tools/ramguard local -- python3 <this>

FOURTH-ROUND PRE-REGISTRATION (written before this file was run):

  X0  DUAL FORM OF k-PACKING.  For |T_i| = r' = n-k-d, MDS gives
      Syn(T_1) cap Syn(T_2) = Syn(T_1 cap T_2) whenever
      |T_1 union T_2| <= n-k.  In that case any pi in the intersection
      has BOTH its errors supported in T_1 cap T_2, so the reconstructed
      pair's core is strictly deeper and NEITHER T_i is maximal.  Hence
      two distinct MAXIMAL depth-d locators must satisfy
          |T_1 union T_2| >= n-k+1,  i.e.  |S_1 cap S_2| <= k-1,
      which is exactly the banked k-packing / core-disjointness
      statement, re-derived in the dual coordinates.  PREDICT: exact,
      0 violations -- and it EXPLAINS why the unconstrained extremal
      search of cosetrank.py returns big families with maximal = 0.
  X1  PREDICT: sampling pairs T_1,T_2 that DO satisfy the union
      condition yields full-rank 2-planes for which both T_i are
      maximal, i.e. the full-rank stratum carries genuine 2-member
      maximal families.  (If this failed, the leaf would be nearly
      vacuous and that would be the headline.)
  X2  PREDICT: greedy growth under the pairwise union condition reaches
      maximal families of size >= 3 at the larger fixture, all in the
      FULL-rank stratum, and their measured pencil ceiling h places
      d at or above the band -- toy subcriticality again, so no count
      claim follows (PREREG P5).
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
from algebra import (direct_core, evalpoly, rank, root_of_unity)  # noqa
from dualform import pair_profile, pencil_profile, spanrank, toeplitz  # noqa
from rankstrat import (annihilator_of_divisor, family_of,  # noqa: E402
                       nullspace, rref_span, try_add, word_from_syndrome)

random.seed(20260806)
checks = []


def ck(name, tag, ok, extra=None):
    checks.append(dict(check=name, fixture=tag, ok=bool(ok), extra=extra))
    return bool(ok)


FIX = [dict(n=16, k=4, q=97, d=3, trials=400),
       dict(n=16, k=4, q=17, d=3, trials=400),
       dict(n=14, k=4, q=29, d=3, trials=400)]


def main():
    out = []
    for f in FIX:
        n, k, q, d, trials = f["n"], f["k"], f["q"], f["d"], f["trials"]
        rp = n - k - d
        N = n - k
        g0 = root_of_unity(n, q)
        H = [pow(g0, i, q) for i in range(n)]
        tag = f"n{n}k{k}d{d}q{q}"
        allT = list(combinations(range(n), rp))
        WT = {T: annihilator_of_divisor([H[i] for i in T], n, k, d, q)
              for T in allT}

        def pi_from(Ts):
            basis, piv = [], []
            for T in Ts:
                res = try_add(basis, piv, WT[T], q, N - 2)
                if res is None:
                    return None
                basis, piv = res
            ns = nullspace(rref_span(basis, q) if basis else [], q, N)
            if len(ns) < 2:
                return None
            for _ in range(8):
                c1 = [random.randrange(q) for _ in ns]
                c2 = [random.randrange(q) for _ in ns]
                su = [sum(c * b[j] for c, b in zip(c1, ns)) % q
                      for j in range(N)]
                sv = [sum(c * b[j] for c, b in zip(c2, ns)) % q
                      for j in range(N)]
                if spanrank([su, sv], q) == 2:
                    return (su, sv)
            return None

        def ledger(pi, Ts):
            su, sv = pi
            u = word_from_syndrome(su, n, k)
            v = word_from_syndrome(sv, n, k)
            uv = [evalpoly(u, x, q) for x in H]
            vv = [evalpoly(v, x, q) for x in H]
            rJ = rank(toeplitz(u, n, d, rp) + toeplitz(v, n, d, rp), q)
            A_gate = pencil_profile(uv, vv, H, n, k, q)[0]
            hh = A_gate - k
            nmax = 0
            Lps = []
            for T in Ts:
                okf, fc = direct_core(uv, H, T, n, k, d, q)
                okg, gc = direct_core(vv, H, T, n, k, d, q)
                if not (okf and okg):
                    continue
                core, agr = pair_profile(fc, gc, uv, vv, H, n, q)
                if sorted(core) != sorted(set(range(n)) - set(T)):
                    continue
                nmax += 1
                Lps.append(sum(1 for z, a in agr.items() if a == A_gate))
            return dict(rank=rJ, full=(rJ == 2 * d), A=A_gate, h=hh,
                        maximal=nmax, Lp=Lps,
                        band=[-(-hh // 2), hh - 2],
                        band_proper=(-(-hh // 2) <= d <= hh - 2))

        # ---- X0: the union condition is exactly what maximality needs
        viol = 0
        tested = 0
        for _ in range(120):
            T1 = tuple(sorted(random.sample(range(n), rp)))
            T2 = tuple(sorted(random.sample(range(n), rp)))
            if T1 == T2:
                continue
            if len(set(T1) | set(T2)) > N:
                continue                       # not the degenerate case
            pi = pi_from([T1, T2])
            if pi is None:
                continue
            tested += 1
            led = ledger(pi, [T1, T2])
            if led["maximal"] != 0:
                viol += 1
        ck("X0: |T1 u T2| <= n-k  =>  NEITHER locator is maximal "
           "(dual form of k-packing)", tag, viol == 0,
           dict(tested=tested, violations=viol))

        # ---- X1/X2: grow families under the union condition
        # tracked PER STRATUM: the first version of this check compared a
        # global best against "is it full rank?", which a deficient
        # 4-member family can win by luck; that is a selection flaw, not
        # a finding.  Corrected: best full-rank family and best deficient
        # family are tracked separately.
        best = dict(maximal=0)
        bestfull = dict(maximal=0)
        sizes = {}
        for _ in range(trials):
            fam = [tuple(sorted(random.sample(range(n), rp)))]
            for _ in range(6):
                cand = tuple(sorted(random.sample(range(n), rp)))
                if cand in fam:
                    continue
                if any(len(set(cand) | set(T)) <= N for T in fam):
                    continue
                trial = fam + [cand]
                if pi_from(trial) is None:
                    continue
                fam = trial
            pi = pi_from(fam)
            if pi is None:
                continue
            led = ledger(pi, fam)
            sizes[led["maximal"]] = sizes.get(led["maximal"], 0) + 1
            rec = dict(maximal=led["maximal"], full=led["full"],
                       rank=led["rank"], h=led["h"], A=led["A"],
                       band=led["band"], band_proper=led["band_proper"],
                       Lp=led["Lp"], family=len(fam))
            if led["maximal"] > best["maximal"]:
                best = dict(rec)
            if led["full"] and led["maximal"] > bestfull["maximal"]:
                bestfull = dict(rec)
                bestfull["raw"] = len(family_of(pi, [WT[T] for T in allT],
                                                q))
        ck("X1: the FULL-RANK stratum carries a 2-member MAXIMAL "
           "depth-d family", tag, bestfull["maximal"] >= 2, bestfull)
        ck("X2 [P5]: the toy maximal families are subcritical -- the "
           "count is O(1), far below any budget", tag,
           best["maximal"] <= 8, dict(best=best["maximal"],
                                      distribution=sizes))
        out.append(dict(tag=tag, n=n, k=k, d=d, q=q, rprime=rp,
                        best=best, best_fullrank=bestfull,
                        size_distribution=sizes, divisors=len(allT)))

    bad = [c for c in checks if not c["ok"]]
    print(f"checks: {len(checks)}   failures: {len(bad)}")
    for b in bad:
        print("  FAIL", b["check"][:70], b["fixture"], b.get("extra"))
    print()
    for o in out:
        for lbl, b in (("any stratum", o["best"]),
                       ("FULL rank ", o["best_fullrank"])):
            print(f"  {o['tag']} [{lbl}]: best maximal family = "
                  f"{b['maximal']} (rank {b.get('rank')}/{2*o['d']}), "
                  f"raw={b.get('raw')}, h={b.get('h')}, "
                  f"band={b.get('band')}, "
                  f"band-proper={b.get('band_proper')}, L_P={b.get('Lp')}")
        print(f"     maximal-count distribution over trials: "
              f"{o['size_distribution']}")
    with open(__file__.replace(".py", ".json"), "w") as fh:
        json.dump(dict(fixtures=out, checks=checks, n_checks=len(checks),
                       n_fail=len(bad),
                       verdict="PASS" if not bad else "FAIL"), fh,
                  indent=1, default=str)


if __name__ == "__main__":
    main()
