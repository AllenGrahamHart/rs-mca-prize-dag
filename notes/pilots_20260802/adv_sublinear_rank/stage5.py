#!/usr/bin/env python3
"""STAGE 5 -- can a SATURATED K_V family be grown further?

Stage 4 diagnosed the failure mode precisely: a ray system realises a genuine
family only if the solution space of the ray conditions RESTRICTED TO
T = union S_a strictly contains C|_T x C|_T, i.e.

        rank  <=  2m - 1,        m := |T| - k.

Combined with independence (rank = V h) this is the RAY BUDGET

        V h  <=  2m - 1  <=  2(n-k) - 1  =  2R - 1.

Stage 5 starts from the K_V family at its own cap V = (h+1)/(d+1)+1, gives it
extra room (n above the K_V point budget) and tries to grow it with rays that
(i) meet every present ray in exactly k+d, (ii) keep all triples <= k-1,
(iii) raise the rank by exactly h, and (iv) still admit a NON-DEGENERATE
realisation (every ray support exact, all C(V,2) pairs distinct at depth d).

Run: tools/ramguard local -- python3 stage5.py
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


def nondegenerate_realise(row, S, zs, d, tries=400, seed=0):
    """Find (u,v) realising the ray system with every ray support EXACT and
    all C(V,2) pairs distinct at depth exactly d.  Returns dict or None."""
    rnd = random.Random(seed)
    q, k, n = row.q, row.k, row.n
    V = len(S)
    rows = []
    for a, s in enumerate(S):
        rows += T.ray_rows(row, s, zs[a])
    ns = T.nullspace_mod(rows, 2 * n, q)
    if not ns:
        return None
    for _ in range(tries):
        w = [0] * (2 * n)
        for b in ns:
            cf = rnd.randrange(q)
            if cf:
                for i in range(2 * n):
                    w[i] = (w[i] + cf * b[i]) % q
        u, v = w[:n], w[n:]
        if any(x == 0 for x in v):
            continue
        psi, ok = [], True
        for a, s in enumerate(S):
            ww = [(u[i] + zs[a] * v[i]) % q for i in range(n)]
            p = row.interp(tuple(s[:k]), [ww[i] for i in s[:k]])
            sup = [i for i in range(n) if row.ev(p, row.xs[i]) == ww[i]]
            if set(sup) != set(s):
                ok = False
                break
            psi.append(p)
        if not ok:
            continue
        cores, pairs, bad = [], set(), 0
        for a in range(V):
            for b2 in range(a + 1, V):
                den = pow((zs[a] - zs[b2]) % q, q - 2, q)
                g = tuple((x - y) * den % q
                          for x, y in zip(psi[a], psi[b2]))
                f = tuple((psi[a][j] - zs[a] * g[j]) % q for j in range(k))
                Z = tuple(i for i in range(n)
                          if row.ev(f, row.xs[i]) == u[i]
                          and row.ev(g, row.xs[i]) == v[i])
                cores.append(Z)
                pairs.add((f, g))
                if len(Z) != k + d:
                    bad += 1
        if bad or len(pairs) != len(cores):
            continue
        return dict(u=u, v=v, cores=cores, M=len(cores))
    return None


def try_grow(row, S, zs, d, budget=200000, seed=0):
    """Try to add one more ray."""
    rnd = random.Random(seed)
    q, k, h, n, Ai = row.q, row.k, row.h, row.n, row.A
    rows = []
    for a, s in enumerate(S):
        rows += T.ray_rows(row, s, zs[a])
    rk = T.rank_mod(rows, q)
    combi, indep_fail, degen_fail = 0, 0, 0
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
        combi += 1
        z = rnd.randrange(1, q)
        while z in zs:
            z = rnd.randrange(1, q)
        nrk = T.rank_mod(rows + T.ray_rows(row, cand, z), q)
        if nrk != rk + h:
            indep_fail += 1
            continue
        got = nondegenerate_realise(row, list(S) + [cand], list(zs) + [z], d,
                                    tries=120, seed=seed + 11)
        if got is None:
            degen_fail += 1
            continue
        return cand, z, nrk, dict(combi=combi, indep_fail=indep_fail,
                                  degen_fail=degen_fail)
    return None, None, rk, dict(combi=combi, indep_fail=indep_fail,
                                degen_fail=degen_fail)


def main():
    res = []
    CASES = [
        dict(k=3, h=5, d=1, q=6421, extra=[0, 4, 10, 20]),
        dict(k=3, h=7, d=1, q=6421, extra=[0, 6, 14]),
        dict(k=3, h=9, d=1, q=10007, extra=[0, 8]),
        dict(k=3, h=8, d=2, q=10007, extra=[0, 6, 12]),
        dict(k=4, h=7, d=1, q=6421, extra=[0, 8]),
    ]
    for cs in CASES:
        k, h, d, q = cs["k"], cs["h"], cs["d"], cs["q"]
        Vcap = (h + 1) // (d + 1) + 1
        M0 = Vcap * (Vcap - 1) // 2
        n0 = (k - 1) + M0 * (d + 1)
        for ex in cs["extra"]:
            n = max(n0 + ex, k + h + 2)
            row = T.Row2(n, k, h, q)
            b = A.build_KV(row, d, Vcap, seed=0)
            if b is None:
                print(f"SKIP KV k={k} h={h} d={d} V={Vcap} n={n}")
                continue
            u, v, info = b
            S = [tuple(s) for s in info["supports"].values()]
            zs = list(info["zs"])
            V = len(S)
            grew = []
            for step in range(4):
                cand, z, rk, stats = try_grow(row, S, zs, d, budget=120000,
                                              seed=step)
                if cand is None:
                    break
                S.append(cand)
                zs.append(z)
                V += 1
                grew.append(stats)
            rows = []
            for a, s in enumerate(S):
                rows += T.ray_rows(row, s, zs[a])
            rk = T.rank_mod(rows, q)
            m = len(set().union(*[set(s) for s in S])) - k
            got = nondegenerate_realise(row, S, zs, d, tries=400, seed=3)
            tag = f"k={k} h={h} d={d} n={n} R={row.R}"
            rec = dict(cs=cs, n=n, R=row.R, V_start=Vcap, V_final=V,
                       KV_cap=Vcap, rank=rk, Vh=V * h, m=m, two_m=2 * m,
                       ray_budget=(2 * row.R - 1) // h,
                       M=V * (V - 1) // 2,
                       grew=len(S) - Vcap,
                       realised=got is not None,
                       last_stats=grew[-1] if grew else None)
            chk(f"S5 {tag}: K_V at cap V={Vcap} could NOT be grown "
                f"(final V={V}, ray budget (2R-1)/h={(2*row.R-1)//h})",
                V == Vcap,
                f"rank={rk} Vh={V*h} m={m} 2m={2*m} grew={V-Vcap}")
            if got is not None:
                from math import comb
                if comb(n, k) <= 80000:
                    rc, _, band = occlib.measure(row, got["u"], got["v"],
                                                 name="grown",
                                                 want_checks=True)
                    Nd = rc["ledger_by_depth"].get(str(d), {}).get("N_d", 0)
                    rec.update(ADMISSIBLE=rc["ADMISSIBLE"], N_d=Nd,
                               law=(row.R + 1) // (h - d))
                    chk(f"S5-GATE {tag} V={V}: ADMISSIBLE, N_d={Nd} vs "
                        f"SHARP-OCC law {(row.R+1)//(h-d)}",
                        rc["ADMISSIBLE"] and Nd >= got["M"],
                        f"M={got['M']} maxJ={rc['max_joint_agreement']} "
                        f"maxray={rc['max_ray_agreement']} A={row.A}")
            res.append(rec)

    with open(os.path.join(HERE, "stage5.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    print(f"\n{CHECKS[0]} checks, {len(FAIL)} FAIL")
    for f in FAIL:
        print("  FAIL:", f)


if __name__ == "__main__":
    main()
