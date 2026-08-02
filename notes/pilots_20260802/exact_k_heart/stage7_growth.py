#!/usr/bin/env python3
r"""STAGE 7 -- the growth law and the SHARP boundary of the d=0 ceiling.

G1  series at fixed rate k/n = 1/4 and h = 3: max admissible slope count
    vs the design ceiling (2R-1)/h.
G2  SHARP BOUNDARY: at V = floor((2R-1)/h) the family is admissible; at
    V = floor((2R-1)/h)+1 the rank must be deficient (Vh > 2R-1) -- is it
    still admissible?  (If never, the ceiling is a hard wall at toy scale.)
G3  the d=0 collision-graph shape of the extremal family: G_0, N_0, M_0.
"""
from __future__ import annotations

import json
import os
import random
import sys
from collections import defaultdict

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import dzlib as Z                                              # noqa: E402
import tslib as T                                              # noqa: E402
from stage6_official import (multi_sunflower, realise_family,   # noqa: E402
                             check_rays)

OUT = {"checks": [], "fail": 0, "pass": 0, "data": {}}


def chk(name, cond, info=None):
    OUT["checks"].append(dict(name=name, ok=bool(cond), info=info))
    if cond:
        OUT["pass"] += 1
    else:
        OUT["fail"] += 1
        print("  FAIL", name, info)
    return cond


def graph_stats(row, rays):
    k = row.k
    V = len(rays)
    cores, deg = set(), set()
    M0 = 0
    for i in range(V):
        for j in range(i + 1, V):
            c = set(rays[i][1]) & set(rays[j][1])
            if len(c) == k:
                M0 += 1
                cores.add(tuple(sorted(c)))
                deg.add(i)
                deg.add(j)
    return dict(V=V, M0=M0, N0=len(cores), G0=len(deg))


def main():
    series = [(24, 6, 3, 1009), (32, 8, 3, 1009), (40, 10, 3, 2003),
              (48, 12, 3, 3001), (56, 14, 3, 3001), (64, 16, 3, 4001),
              (72, 18, 3, 4001), (80, 20, 3, 5003)]
    g1 = []
    for (n, k, h, q) in series:
        row = Z.make_row(n, k, h, q)
        ceil_rank = (2 * row.R - 1) // h
        tag = f"n{n}k{k}h{h}"
        best, bestrays = 0, None
        for V in range(ceil_rank, 0, -1):
            hit = False
            for s in range(4):
                rng = random.Random(1000 * V + s + n)
                rays = multi_sunflower(row, V, rng, seed=V * 17 + n + 7 * s)
                if rays is None:
                    continue
                sol, rk = realise_family(row, rays, seed=V + s)
                if sol is None:
                    continue
                ok, why = check_rays(row, sol[0], sol[1], rays)
                if ok:
                    hit = True
                    if V > best:
                        best, bestrays = V, rays
                    break
            if hit:
                break
        # -------- G2 one past the ceiling
        over_ok = 0
        for s in range(6):
            V = ceil_rank + 1
            rng = random.Random(555 + s)
            rays = multi_sunflower(row, V, rng, seed=99 + s)
            if rays is None:
                continue
            sol, rk = realise_family(row, rays, seed=s)
            if sol is None:
                continue
            ok, why = check_rays(row, sol[0], sol[1], rays)
            if ok:
                over_ok += 1
        gs = graph_stats(row, bestrays) if bestrays else {}
        g1.append(dict(tag=tag, n=n, k=k, h=h, R=row.R, ceil=ceil_rank,
                       best=best, over_admissible=over_ok, graph=gs))
        chk(f"G2 ceiling+1 dead {tag}", over_ok == 0, over_ok)
        chk(f"G1 best <= ceiling {tag}", best <= ceil_rank, (best, ceil_rank))
        print(f"G1 {tag}: R={row.R} ceiling={ceil_rank} best={best} "
              f"(ceil+1 admissible in {over_ok}/6)  graph={gs}")
    OUT["data"]["g1"] = g1
    # linear fit of best vs n
    xs = [r["n"] for r in g1]
    ys = [r["best"] for r in g1]
    m = len(xs)
    sx, sy = sum(xs), sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    den = m * sxx - sx * sx
    slope = (m * sxy - sx * sy) / den
    icpt = (sy - slope * sx) / m
    OUT["data"]["fit"] = dict(slope=slope, intercept=icpt,
                              predicted_slope=2 * (1 - 0.25) / 3)
    print(f"G1 fit: best ~ {slope:.4f} n + {icpt:.3f}   "
          f"(theory 2(1-rate)/h = {2*0.75/3:.4f})")
    json.dump(OUT, open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "stage7.json"), "w"), indent=1)
    print(f"stage7: PASS={OUT['pass']} FAIL={OUT['fail']}")


if __name__ == "__main__":
    main()
