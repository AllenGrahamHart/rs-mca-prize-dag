#!/usr/bin/env python3
r"""STAGE 4 -- exhaustive scans of REAL received pairs at d = 0.

For each (u,v) we take occlib's exhaustive k-subset scan, extract the LIVE
rays (max agreement exactly A, one selected support per slope), and measure

  V      = # live slopes
  M_0    = # live ray PAIRS with |S ^ S'| = k exactly   (the d = 0 moment,
           == sum_{|W|=k} C(L_W,2) restricted to d = 0, by T1)
  N_0    = # distinct k-cores carried by >= 2 live rays
  G_0    = # live slopes in >= 1 exact-k pair  (THE P-A1 d=0 COUNT)
  M_+/G_+ = the same with |S ^ S'| >= k  (the widened predicate)
  Lmax   = max_W L_W
  peel   = does the live family peel (every ray >= h points of cover <= 2)?
  rank   = condition rank of the live family, vs V*h and the locality cap
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

OUT = {"checks": [], "fail": 0, "pass": 0, "runs": []}


def chk(name, cond, info=None):
    OUT["checks"].append(dict(name=name, ok=bool(cond), info=info))
    if cond:
        OUT["pass"] += 1
    else:
        OUT["fail"] += 1
        print("  FAIL", name, info)
    return cond


def live_family(row, u, v):
    """Selected supports: per slope, max agreement; live iff == A."""
    pairs, rays, vmax = occlib.scan(row, u, v)
    best = {}
    for (z, S), s in rays.items():
        if z not in best or s > best[z][0] or (s == best[z][0] and
                                               tuple(sorted(S)) < best[z][1]):
            best[z] = (s, tuple(sorted(S)))
    live = {z: S for z, (s, S) in best.items() if s == row.A}
    over = {z: s for z, (s, S) in best.items() if s > row.A}
    return live, over, vmax, pairs


def peel(row, rays):
    """Iteratively drop rays with >= h points of coverage <= 2.
    Returns (#peeled, residual core)."""
    h = row.h
    cur = list(rays)
    peeled = 0
    changed = True
    while changed and cur:
        changed = False
        cov = defaultdict(int)
        for _, S in cur:
            for x in S:
                cov[x] += 1
        for idx, (z, S) in enumerate(cur):
            low = sum(1 for x in S if cov[x] <= 2)
            if low >= h:
                cur.pop(idx)
                peeled += 1
                changed = True
                break
    return peeled, cur


def measure(row, u, v):
    A, k, h = row.A, row.k, row.h
    live, over, vmax, pairs = live_family(row, u, v)
    rays = sorted(live.items())
    V = len(rays)
    inter = {}
    for i in range(V):
        for j in range(i + 1, V):
            inter[(i, j)] = len(set(rays[i][1]) & set(rays[j][1]))
    M0 = sum(1 for c in inter.values() if c == k)
    Mplus = sum(1 for c in inter.values() if c >= k)
    cores0, coresp = set(), set()
    deg0, degp = set(), set()
    for (i, j), c in inter.items():
        if c == k:
            cores0.add(tuple(sorted(set(rays[i][1]) & set(rays[j][1]))))
            deg0.add(i)
            deg0.add(j)
        if c >= k:
            degp.add(i)
            degp.add(j)
            for W in itertools.combinations(
                    sorted(set(rays[i][1]) & set(rays[j][1])), k):
                coresp.add(W)
    Lmax = 0
    if cores0:
        cnt = defaultdict(int)
        for idx, (z, S) in enumerate(rays):
            for W in cores0:
                if set(W) <= set(S):
                    cnt[W] += 1
        Lmax = max(cnt.values()) if cnt else 0
    npeel, core = peel(row, rays)
    rk, exp = Z.family_rank(row, rays) if rays else (0, 0)
    uni = len(set().union(*[set(S) for _, S in rays])) if rays else 0
    return dict(V=V, over=len(over), M0=M0, Mplus=Mplus, N0=len(cores0),
                Nplus=len(coresp), G0=len(deg0), Gplus=len(degp),
                Lmax=Lmax, peeled=npeel, core=len(core), rank=rk, Vh=exp,
                union=uni, locality=2 * (uni - k) - 1 if uni else 0,
                interprofile=sorted(defaultdict(
                    int, {c: sum(1 for x in inter.values() if x == c)
                          for c in set(inter.values())}).items()))


def main():
    rng = random.Random(777)
    shapes = [(14, 5, 3, 31), (16, 6, 3, 61), (16, 5, 4, 47),
              (18, 6, 3, 43), (20, 6, 3, 53)]
    for (n, k, h, q) in shapes:
        row = Z.make_row(n, k, h, q)
        tag = f"n{n}k{k}h{h}q{q}"
        # ---- random pairs
        for t in range(3):
            u = [rng.randrange(q) for _ in range(n)]
            v = [rng.randrange(1, q) for _ in range(n)]
            m = measure(row, u, v)
            m.update(tag=tag, kind="random", trial=t)
            OUT["runs"].append(m)
            chk(f"S4 rank<=Vh {tag} rnd{t}", m["rank"] <= m["Vh"])
            chk(f"S4 locality {tag} rnd{t}",
                m["V"] == 0 or m["rank"] <= m["locality"] + 1,
                (m["rank"], m["locality"]))
            chk(f"S4 G0<=2*M0 {tag} rnd{t}", m["G0"] <= 2 * m["M0"],
                (m["G0"], m["M0"]))
            chk(f"S4 G0<=V {tag} rnd{t}", m["G0"] <= m["V"])
        # ---- planted d=0 sunflower pair (common k-set W, disjoint petals)
        for t in range(2):
            W = tuple(range(k))
            mm = min((n - k) // h, 4)
            Ss = [tuple(sorted(set(W) | set(range(k + a * h, k + (a + 1) * h))))
                  for a in range(mm)]
            zs = rng.sample(range(1, q), mm)
            rows = []
            for z, S in zip(zs, Ss):
                rows += T.ray_rows(row, S, z)
            sol = T.realise(row, rows, seed=99 + t, tries=200,
                            require_v_nonzero=False)
            if sol is None:
                continue
            u, v = sol
            m = measure(row, u, v)
            m.update(tag=tag, kind="planted_sunflower", trial=t,
                     planted=mm)
            OUT["runs"].append(m)
            chk(f"S4p planted sunflower alive {tag} t{t}", m["V"] >= 2,
                m["V"])
    for r in OUT["runs"]:
        print(f"{r['tag']:<14}{r['kind']:<18}V={r['V']:<4}over={r['over']:<3}"
              f"M0={r['M0']:<4}N0={r['N0']:<4}G0={r['G0']:<4}"
              f"M+={r['Mplus']:<4}G+={r['Gplus']:<4}Lmax={r['Lmax']:<3}"
              f"rank={r['rank']:<4}Vh={r['Vh']:<4}peel={r['peeled']}/"
              f"{r['V']}")
    json.dump(OUT, open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "stage4.json"), "w"), indent=1)
    print(f"stage4: PASS={OUT['pass']} FAIL={OUT['fail']}")


if __name__ == "__main__":
    main()
