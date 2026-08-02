#!/usr/bin/env python3
r"""STAGE 6 -- OFFICIAL-SHAPED toys (h << k, A/n ~ 1/4) : deficit hunt,
generalised clusters, growth law.

The stage-3/4/5 toys had A/n ~ 0.5 and h/A ~ 1/3; the six rows have
A/n in {0.255, 0.130, 0.065} and h/A ~ 0.02-0.05.  Here we use shapes with
h << k so that the exact-k geometry (supports sharing all but h points) is
the official one.  Only rank + intended-ray admissibility is available at
this scale (no exhaustive C(n,k) scan) -- stated as a caveat.

D1  design ceiling: largest admissible multi-sunflower system vs (2R-1)/h
D2  deficit hunt over random k-packed families
D3  GENERALISED CLUSTER: union k+c, complements of size c-h pairwise
    meeting in exactly c-2h.  PREDICTION: rank = min(Vh, 2c) and the
    family is DEAD exactly when rank = 2c (locality death).
D4  multiplicative-coset / orbit supports at d = 0
D5  growth law of the maximum admissible slope count in n
"""
from __future__ import annotations

import itertools
import json
import os
import random
import sys
from collections import defaultdict

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import dzlib as Z                                              # noqa: E402
import tslib as T                                              # noqa: E402

OUT = {"checks": [], "fail": 0, "pass": 0, "data": {}}


def chk(name, cond, info=None):
    OUT["checks"].append(dict(name=name, ok=bool(cond), info=info))
    if cond:
        OUT["pass"] += 1
    else:
        OUT["fail"] += 1
        print("  FAIL", name, info)
    return cond


def realise_family(row, rays, seed=0, tries=300):
    rows = []
    for z, S in rays:
        rows += T.ray_rows(row, S, z)
    rk = T.rank_mod(rows, row.q)
    return T.realise(row, rows, seed=seed, tries=tries,
                     require_v_nonzero=False), rk


def check_rays(row, u, v, rays):
    q, n, A = row.q, row.n, row.A
    for z, S in rays:
        w = [(u[i] + z * v[i]) % q for i in range(n)]
        W = tuple(sorted(S))[:row.k]
        f = row.interp(W, [w[i] for i in W])
        if not all(row.ev(f, row.xs[i]) == w[i] for i in S):
            return False, "not-a-codeword-on-S"
        agr = sum(1 for i in range(n) if row.ev(f, row.xs[i]) == w[i])
        if agr != A:
            return False, f"agr={agr}>A={A}"
    return True, "ok"


SHAPES = [(32, 8, 3, 1009), (40, 10, 3, 2003), (48, 12, 3, 3001),
          (44, 11, 3, 2003), (40, 10, 4, 2003), (48, 12, 4, 3001),
          (64, 16, 3, 4001)]


def multi_sunflower(row, V, rng, seed):
    """Stack disjoint-core sunflowers to reach V rays; k-packed by
    construction if the cores are far apart."""
    n, k, h = row.n, row.k, row.h
    per = max(1, (n - k) // h)
    rays, made = [], 0
    r2 = random.Random(seed)
    guard = 0
    while made < V and guard < 200:
        guard += 1
        Wc = tuple(sorted(r2.sample(range(n), k)))
        rest = [x for x in range(n) if x not in set(Wc)]
        r2.shuffle(rest)
        for a in range((len(rest)) // h):
            if made >= V:
                break
            P = tuple(rest[a * h:(a + 1) * h])
            S = tuple(sorted(set(Wc) | set(P)))
            if any(len(set(S) & set(S2)) > k for _, S2 in rays):
                continue
            rays.append((0, S))
            made += 1
    if made < V:
        return None
    zs = rng.sample(range(1, row.q), V)
    return [(z, S) for z, (_, S) in zip(zs, rays)]


def gen_cluster(row, c, V, kind="cycle"):
    """Union U of size k+c; complements t_a of size c-h inside U.
    kind='cycle': t_a = block_a u block_{a+1} (needs c = 3h);
    kind='disjoint': t_a disjoint (c = 2h)."""
    n, k, h = row.n, row.k, row.h
    if k + c > n:
        return None
    U = list(range(k + c))
    if kind == "disjoint":
        if c != 2 * h or V * h > k + c:
            return None
        ts = [tuple(U[a * h:(a + 1) * h]) for a in range(V)]
    elif kind == "cycle":
        if c != 3 * h:
            return None
        nb = (k + c) // h
        if V > nb:
            return None
        blocks = [tuple(U[a * h:(a + 1) * h]) for a in range(nb)]
        ts = [tuple(sorted(set(blocks[a]) | set(blocks[(a + 1) % nb])))
              for a in range(V)]
    else:
        return None
    Ss = [tuple(sorted(set(U) - set(t))) for t in ts]
    if any(len(S) != row.A for S in Ss):
        return None
    return U, ts, Ss


def main():
    rng = random.Random(90210)

    # ------------------------------------------------------- D1 + D5
    d1 = []
    for (n, k, h, q) in SHAPES:
        row = Z.make_row(n, k, h, q)
        R, ceil_rank = row.R, (2 * row.R - 1) // h
        tag = f"n{n}k{k}h{h}"
        best = 0
        for V in range(1, ceil_rank + 3):
            rays = multi_sunflower(row, V, rng, seed=V * 17 + n)
            if rays is None:
                break
            sol, rk = realise_family(row, rays, seed=V)
            if sol is None:
                continue
            ok, why = check_rays(row, sol[0], sol[1], rays)
            if ok:
                best = V
            else:
                break
        d1.append(dict(tag=tag, n=n, k=k, h=h, R=R, ceil=ceil_rank,
                       best=best, ratio=best / max(ceil_rank, 1)))
        chk(f"D1 best <= ceiling {tag}", best <= ceil_rank, (best, ceil_rank))
        print(f"D1 {tag}: R={R} ceiling=(2R-1)/h={ceil_rank} "
              f"max admissible V={best}")
    OUT["data"]["d1"] = d1

    # ------------------------------------------------------- D2 deficit hunt
    d2 = []
    for (n, k, h, q) in SHAPES[:5]:
        row = Z.make_row(n, k, h, q)
        tag = f"n{n}k{k}h{h}"
        ceil_rank = (2 * row.R - 1) // h
        stats = dict(trials=0, deficient=0, admissible_deficient=0,
                     min_percost=None)
        for tr in range(120):
            V = rng.randint(4, max(5, min(ceil_rank, 14)))
            sups = []
            for _ in range(V):
                S = tuple(sorted(rng.sample(range(n), row.A)))
                if any(len(set(S) & set(S2)) > k for S2 in sups):
                    continue
                sups.append(S)
            if len(sups) < 4:
                continue
            stats["trials"] += 1
            zs = rng.sample(range(1, q), len(sups))
            rays = list(zip(zs, sups))
            sol, rk = realise_family(row, rays, seed=tr)
            if rk < len(sups) * h:
                stats["deficient"] += 1
                if sol is not None:
                    ok, why = check_rays(row, sol[0], sol[1], rays)
                    if ok:
                        stats["admissible_deficient"] += 1
                        pc = rk / len(sups)
                        if stats["min_percost"] is None or \
                                pc < stats["min_percost"]:
                            stats["min_percost"] = pc
        d2.append(dict(tag=tag, h=h, **stats))
        print(f"D2 {tag}: trials={stats['trials']} deficient="
              f"{stats['deficient']} admissible-deficient="
              f"{stats['admissible_deficient']}")
    OUT["data"]["d2"] = d2

    # ------------------------------------------------------- D3 clusters
    d3 = []
    for (n, k, h, q) in SHAPES:
        row = Z.make_row(n, k, h, q)
        tag = f"n{n}k{k}h{h}"
        for kind, c in (("disjoint", 2 * h), ("cycle", 3 * h)):
            for V in range(2, 10):
                built = gen_cluster(row, c, V, kind)
                if built is None:
                    continue
                U, ts, Ss = built
                zs = rng.sample(range(1, q), V)
                rays = list(zip(zs, Ss))
                sol, rk = realise_family(row, rays, seed=V * 3)
                ok = False
                if sol is not None:
                    ok, why = check_rays(row, sol[0], sol[1], rays)
                pred = min(V * h, 2 * c)
                d3.append(dict(tag=tag, kind=kind, c=c, V=V, rank=rk,
                               pred=pred, Vh=V * h, cap=2 * c,
                               admissible=bool(ok)))
                chk(f"D3 rank=min(Vh,2c) {tag} {kind} V={V}", rk == pred,
                    (rk, pred))
                chk(f"D3 death iff rank=2c {tag} {kind} V={V}",
                    (rk == 2 * c) != bool(ok), (rk, 2 * c, ok))
    OUT["data"]["d3"] = d3
    cl = defaultdict(lambda: [0, 0])
    for r in d3:
        cl[(r["kind"], r["rank"] == r["cap"])][0] += 1
        cl[(r["kind"], r["rank"] == r["cap"])][1] += int(r["admissible"])
    print("D3 (kind, rank==2c) -> (count, #admissible):",
          {str(kk): vv for kk, vv in cl.items()})

    json.dump(OUT, open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "stage6.json"), "w"), indent=1)
    print(f"stage6: PASS={OUT['pass']} FAIL={OUT['fail']}")


if __name__ == "__main__":
    main()
