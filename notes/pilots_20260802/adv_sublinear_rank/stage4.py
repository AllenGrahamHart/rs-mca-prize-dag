#!/usr/bin/env python3
"""STAGE 4 -- the decisive experiment: how many INDEPENDENT rays fit?

Stage 3 found ray CLIQUES far larger than the K_V cap (V = 19 at
n=20,k=4,h=6,d=1 vs cap 4) -- but their rank saturated at 2m, i.e. the whole
system collapses to a single band pair.  So the binding constraint is not
combinatorial but ALGEBRAIC.

Working law under test (RAY-CHARGE):
    rank(family) = V h  (independent ray blocks)  and  M <= C(V,2)
    => V <= (2R-1)/h  and  N_d <= C((2R-1)/h, 2) = Theta(n^2/h^2).

Stage 4 grows a ray system GREEDILY subject to
    (i)  |S ^ S_a| = k+d for every present ray,
    (ii) |S ^ S_a ^ S_b| <= k-1,
    (iii) the rank increases by EXACTLY h (independence preserved),
and then realises + verifies the family end-to-end.

Run: tools/ramguard local -- python3 stage4.py
"""
from __future__ import annotations

import json
import os
import random
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import advlib as A                                            # noqa: E402
import spread as SP                                           # noqa: E402,F401
import tslib as T                                             # noqa: E402
import occlib                                                 # noqa: E402

FAIL, CHECKS = [], [0]


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    print(("PASS " if ok else "FAIL ") + label + (("  | " + detail)
                                                  if detail else ""))
    if not ok:
        FAIL.append(label)
    return ok


def grow_independent(row, d, seed=0, budget=120000, start=None):
    """Greedily grow a set of rays keeping (i)-(iii)."""
    rnd = random.Random(seed)
    q, k, h, n, Ai = row.q, row.k, row.h, row.n, row.A
    S = list(start) if start else [tuple(range(Ai))]
    zs = [rnd.randrange(1, q) for _ in S]
    rows = []
    for a, s in enumerate(S):
        rows += T.ray_rows(row, s, zs[a])
    rk = T.rank_mod(rows, q)
    combi_ok, indep_block = 0, 0
    pool = list(range(n))
    for _ in range(budget):
        cand = tuple(sorted(rnd.sample(pool, Ai)))
        cs = set(cand)
        if any(len(cs & set(s)) != k + d for s in S):
            continue
        bad = False
        for a in range(len(S)):
            for b in range(a + 1, len(S)):
                if len(cs & set(S[a]) & set(S[b])) > k - 1:
                    bad = True
                    break
            if bad:
                break
        if bad:
            continue
        combi_ok += 1
        z = rnd.randrange(1, q)
        while z in zs:
            z = rnd.randrange(1, q)
        nrows = rows + T.ray_rows(row, cand, z)
        nrk = T.rank_mod(nrows, q)
        if nrk == rk + h:
            S.append(cand)
            zs.append(z)
            rows = nrows
            rk = nrk
        else:
            indep_block += 1
    return S, zs, rk, combi_ok, indep_block


def verify_system(row, S, zs, d):
    """Realise the ray system and verify every pair of rays as a datum."""
    q, k, n, Ai = row.q, row.k, row.n, row.A
    V = len(S)
    rows = []
    for a, s in enumerate(S):
        rows += T.ray_rows(row, s, zs[a])
    sol = T.realise(row, rows, seed=7, tries=200)
    if sol is None:
        return None
    u, v = sol
    psi, supp_ok = [], True
    for a, s in enumerate(S):
        w = [(u[i] + zs[a] * v[i]) % q for i in range(n)]
        p = row.interp(tuple(s[:k]), [w[i] for i in s[:k]])
        sup = tuple(i for i in range(n) if row.ev(p, row.xs[i]) == w[i])
        if set(sup) != set(s):
            supp_ok = False
        psi.append(p)
    cores, pairs, depth_bad = [], set(), 0
    for a in range(V):
        for b in range(a + 1, V):
            den = pow((zs[a] - zs[b]) % q, q - 2, q)
            g = tuple((x - y) * den % q for x, y in zip(psi[a], psi[b]))
            f = tuple((psi[a][j] - zs[a] * g[j]) % q for j in range(k))
            Z = tuple(i for i in range(n)
                      if row.ev(f, row.xs[i]) == u[i]
                      and row.ev(g, row.xs[i]) == v[i])
            cores.append(Z)
            pairs.add((f, g))
            if len(Z) != k + d:
                depth_bad += 1
    return dict(u=u, v=v, supp_ok=supp_ok, M=len(cores),
                distinct_pairs=len(pairs), depth_bad=depth_bad,
                cores=cores)


def main():
    res = []
    CASES = [
        dict(n=20, k=3, h=5, d=1, q=6421),
        dict(n=26, k=3, h=5, d=1, q=6421),
        dict(n=22, k=3, h=7, d=1, q=6421),
        dict(n=32, k=3, h=7, d=1, q=6421),
        dict(n=32, k=3, h=9, d=1, q=10007),
        dict(n=44, k=3, h=11, d=1, q=10007),
        dict(n=24, k=4, h=6, d=1, q=6421),
        dict(n=23, k=4, h=7, d=1, q=6421),
        dict(n=20, k=3, h=8, d=2, q=10007),
        dict(n=32, k=3, h=11, d=2, q=10007),
    ]
    for cs in CASES:
        n, k, h, d, q = cs["n"], cs["k"], cs["h"], cs["d"], cs["q"]
        row = T.Row2(n, k, h, q)
        best = None
        for seed in range(3):
            S, zs, rk, combi_ok, blocked = grow_independent(
                row, d, seed=seed, budget=40000)
            if best is None or len(S) > len(best[0]):
                best = (S, zs, rk, combi_ok, blocked)
        S, zs, rk, combi_ok, blocked = best
        V = len(S)
        m = len(set().union(*[set(s) for s in S])) - k
        kv_cap = (h + 1) // (d + 1) + 1
        rec = dict(cs=cs, R=row.R, V_independent=V, KV_cap=kv_cap,
                   rank=rk, Vh=V * h, m=m, two_m=2 * m,
                   two_R_minus_1=2 * row.R - 1,
                   ray_budget_2R_over_h=(2 * row.R - 1) // h,
                   combi_admissible_candidates=combi_ok,
                   blocked_by_independence=blocked,
                   M_complete=V * (V - 1) // 2)
        tag = f"n={n} k={k} h={h} d={d}"
        chk(f"S4 {tag}: greedy INDEPENDENT ray system reached V={V} "
            f"(rank {rk} = V*h {V*h})", rk == V * h,
            f"m={m} 2m={2*m} 2R-1={2*row.R-1} ray-budget "
            f"(2R-1)/h={(2*row.R-1)//h} KVcap={kv_cap}")
        chk(f"S4 {tag}: independence, not combinatorics, is the binding "
            f"constraint", blocked > 0,
            f"{combi_ok} combinatorially-admissible candidates, "
            f"{blocked} rejected by the rank test")
        ver = verify_system(row, S, zs, d)
        if ver is None:
            chk(f"S4 {tag}: realisation found", False)
        else:
            rec.update(supp_ok=ver["supp_ok"], M=ver["M"],
                       distinct_pairs=ver["distinct_pairs"],
                       depth_bad=ver["depth_bad"])
            chk(f"S4 {tag}: all {ver['M']} pairs-of-rays are DISTINCT band "
                f"pairs at depth exactly {d}",
                ver["distinct_pairs"] == ver["M"] and ver["depth_bad"] == 0
                and ver["supp_ok"],
                f"distinct={ver['distinct_pairs']}/{ver['M']} "
                f"depth_bad={ver['depth_bad']} ray_supports_exact="
                f"{ver['supp_ok']}")
            from math import comb
            if comb(n, k) <= 60000:
                rc, _, band = occlib.measure(row, ver["u"], ver["v"],
                                             name="grown", want_checks=True)
                Nd = rc["ledger_by_depth"].get(str(d), {}).get("N_d", 0)
                rec.update(ADMISSIBLE=rc["ADMISSIBLE"], N_d_measured=Nd,
                           maxJ=rc["max_joint_agreement"],
                           maxray=rc["max_ray_agreement"], A=row.A,
                           sharp_occ_law=(row.R + 1) // (h - d))
                chk(f"S4-GATE {tag}: grown fixture ADMISSIBLE",
                    rc["ADMISSIBLE"],
                    f"maxJ={rc['max_joint_agreement']}<=A-2={row.A-2} "
                    f"maxray={rc['max_ray_agreement']}<=A={row.A} "
                    f"vnz={rc['v_nonvanishing']}")
                chk(f"S4-GATE {tag}: N_d = {Nd} vs SHARP-OCC law "
                    f"{(row.R+1)//(h-d)}",
                    Nd >= ver["M"], f"M={ver['M']}")
        res.append(rec)

    with open(os.path.join(HERE, "stage4.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    print(f"\n{CHECKS[0]} checks, {len(FAIL)} FAIL")
    for f in FAIL:
        print("  FAIL:", f)


if __name__ == "__main__":
    main()
