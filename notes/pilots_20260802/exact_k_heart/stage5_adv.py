#!/usr/bin/env python3
r"""STAGE 5 -- adversarial maximisation of the d = 0 slope count.

T1  single d=0 sunflower (common k-core W, V disjoint h-petals):
    point budget V <= R/h; always peelable => rank = Vh; admissible?
T2  MULTI-sunflower: stack independent sunflowers until the rank ceiling
    2R-1 bites.  Empirical max admissible V vs the design ceiling
    (2R-1)/h.
T3  growth law in n at fixed rate and h.
T4  un-peelable design hunt (the residual class): engineered families in
    which every ray has <= h-1 points of coverage <= 2.
T5  coset / mu_M-orbit supports at d = 0 (the BP 2-adic direction).
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
import occlib                                                  # noqa: E402

OUT = {"checks": [], "fail": 0, "pass": 0, "data": {}}


def chk(name, cond, info=None):
    OUT["checks"].append(dict(name=name, ok=bool(cond), info=info))
    if cond:
        OUT["pass"] += 1
    else:
        OUT["fail"] += 1
        print("  FAIL", name, info)
    return cond


def realise_family(row, rays, seed=0, tries=400):
    rows = []
    for z, S in rays:
        rows += T.ray_rows(row, S, z)
    return T.realise(row, rows, seed=seed, tries=tries,
                     require_v_nonzero=False), T.rank_mod(rows, row.q)


def check_rays(row, u, v, rays):
    """Every intended ray live at EXACTLY A with the intended support."""
    q, n, A = row.q, row.n, row.A
    ok_all, det = True, []
    for z, S in rays:
        w = [(u[i] + z * v[i]) % q for i in range(n)]
        W = tuple(sorted(S))[:row.k]
        f = row.interp(W, [w[i] for i in W])
        agr = sum(1 for i in range(n) if row.ev(f, row.xs[i]) == w[i])
        onS = all(row.ev(f, row.xs[i]) == w[i] for i in S)
        det.append((z, onS, agr))
        if not onS or agr != A:
            ok_all = False
    return ok_all, det


def full_check(row, u, v, rays):
    """occlib exhaustive: are the intended slopes live with those supports,
    and is the max agreement exactly A?"""
    pairs, rr, vmax = occlib.scan(row, u, v)
    best = {}
    for (z, S), s in rr.items():
        if z not in best or s > best[z][0]:
            best[z] = (s, tuple(sorted(S)))
    good = 0
    for z, S in rays:
        if z in best and best[z][0] == row.A and set(best[z][1]) == set(S):
            good += 1
    nlive = sum(1 for z, (s, S) in best.items() if s == row.A)
    nover = sum(1 for z, (s, S) in best.items() if s > row.A)
    return good, nlive, nover


def sunflower_rays(row, W, petals, zs):
    return [(z, tuple(sorted(set(W) | set(P)))) for P, z in zip(petals, zs)]


def main():
    rng = random.Random(31337)

    # -------------------------------------------------- T1 / T2
    shapes = [(16, 6, 3, 601), (18, 6, 3, 1009), (20, 8, 3, 1201),
              (16, 5, 4, 1009), (20, 6, 4, 1201), (14, 5, 3, 401)]
    t12 = []
    for (n, k, h, q) in shapes:
        row = Z.make_row(n, k, h, q)
        R, A = row.R, row.A
        cap_pt = R // h
        cap_rank = (2 * R - 1) // h
        tag = f"n{n}k{k}h{h}q{q}"
        # ---- T1 single sunflower at the point budget
        W = tuple(range(k))
        pet = [tuple(range(k + a * h, k + (a + 1) * h)) for a in range(cap_pt)]
        zs = rng.sample(range(1, q), cap_pt)
        rays = sunflower_rays(row, W, pet, zs)
        sol, rk = realise_family(row, rays, seed=7)
        ok1 = False
        if sol:
            ok1, det = check_rays(row, sol[0], sol[1], rays)
        chk(f"T1 sunflower rank=Vh {tag}", rk == cap_pt * h, (rk, cap_pt * h))
        chk(f"T1 sunflower admissible {tag} V={cap_pt}", ok1)
        # ---- T2 multi-sunflower: stack until the ceiling
        bestV = 0
        detail = None
        for nsf in (2, 3, 4):
            for Vper in range(cap_pt, 0, -1):
                if nsf * Vper > cap_rank:
                    continue
                rays2, used_ok = [], True
                pool = list(range(n))
                for s in range(nsf):
                    rng2 = random.Random(1000 * s + Vper + n)
                    Ws = tuple(sorted(rng2.sample(pool, k)))
                    rest = [x for x in pool if x not in set(Ws)]
                    if len(rest) < Vper * h:
                        used_ok = False
                        break
                    for a in range(Vper):
                        P = tuple(rest[a * h:(a + 1) * h])
                        rays2.append((0, tuple(sorted(set(Ws) | set(P)))))
                if not used_ok:
                    continue
                # distinct slopes, k-packed?
                sups = [S for _, S in rays2]
                if any(len(set(sups[i]) & set(sups[j])) > k
                       for i in range(len(sups))
                       for j in range(i + 1, len(sups))):
                    continue
                zz = rng.sample(range(1, q), len(rays2))
                rays2 = [(z, S) for z, (_, S) in zip(zz, rays2)]
                sol, rk = realise_family(row, rays2, seed=11)
                if sol is None:
                    continue
                ok2, det = check_rays(row, sol[0], sol[1], rays2)
                if ok2 and len(rays2) > bestV:
                    bestV = len(rays2)
                    detail = dict(nsf=nsf, Vper=Vper, rank=rk,
                                  Vh=len(rays2) * h)
                break
        t12.append(dict(tag=tag, n=n, k=k, h=h, R=R, cap_pt=cap_pt,
                        cap_rank=cap_rank, single_ok=ok1, bestV=bestV,
                        detail=detail))
        print(f"T1/T2 {tag}: R={R} pointcap={cap_pt} rankceil={cap_rank} "
              f"single_ok={ok1} bestV_multi={bestV} {detail}")
        chk(f"T2 bestV <= rank ceiling {tag}", bestV <= cap_rank,
            (bestV, cap_rank))
    OUT["data"]["t12"] = t12

    # -------------------------------------------------- T4 un-peelable hunt
    t4 = []
    for (n, k, h, q) in [(16, 6, 3, 601), (18, 8, 3, 1009), (20, 9, 3, 1201),
                         (18, 6, 3, 1009), (20, 8, 4, 1201)]:
        row = Z.make_row(n, k, h, q)
        tag = f"n{n}k{k}h{h}q{q}"
        found = dict(tried=0, unpeelable=0, realised=0, admissible=0,
                     ranks=[])
        for trial in range(300):
            V = rng.choice([4, 5, 6])
            sups = []
            for _ in range(V):
                S = tuple(sorted(rng.sample(range(n), row.A)))
                sups.append(S)
            if any(len(set(sups[i]) & set(sups[j])) > k
                   for i in range(V) for j in range(i + 1, V)):
                continue
            found["tried"] += 1
            cov = defaultdict(int)
            for S in sups:
                for x in S:
                    cov[x] += 1
            if any(sum(1 for x in S if cov[x] <= 2) >= h for S in sups):
                continue
            found["unpeelable"] += 1
            zz = rng.sample(range(1, q), V)
            rays = list(zip(zz, sups))
            sol, rk = realise_family(row, rays, seed=trial)
            found["ranks"].append([V, rk, V * h])
            if sol is None:
                continue
            found["realised"] += 1
            ok, det = check_rays(row, sol[0], sol[1], rays)
            if ok:
                found["admissible"] += 1
        t4.append(dict(tag=tag, **found))
        print(f"T4 {tag}: tried={found['tried']} unpeelable="
              f"{found['unpeelable']} realised={found['realised']} "
              f"admissible={found['admissible']}")
    OUT["data"]["t4"] = t4

    json.dump(OUT, open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "stage5.json"), "w"), indent=1)
    print(f"stage5: PASS={OUT['pass']} FAIL={OUT['fail']}")


if __name__ == "__main__":
    main()
