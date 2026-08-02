#!/usr/bin/env python3
r"""STAGE 9 -- the growth law RE-RUN in the STRUCTURAL regime.

Stage 8 A5 showed the stage-6/7 series (q = 3001, 4001) is
NOISE-DOMINATED: E[#coincidence live rays] = 2^16.9 / 2^29.0.  At the six
official rows that expectation is 2^-3.5e11.  A toy is faithful only when

    (q+1) C(n,A) q^{-h} << 1     i.e.   (h-1) log2 q > log2 C(n,A).

Here we redo G1/G2 with q chosen ABOVE that threshold (lazy inverse table,
so q can be large), which is the regime the official rows are in.
"""
from __future__ import annotations

import json
import math
import os
import random
import sys

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


class LazyInv:
    def __init__(self, q):
        self.q = q
        self.m = {}

    def __getitem__(self, a):
        a %= self.q
        r = self.m.get(a)
        if r is None:
            r = pow(a, self.q - 2, self.q)
            self.m[a] = r
        return r


class BigRow(T.Row2):
    def __init__(self, n, k, t, q, xs=None):
        self.n, self.k, self.t, self.q = n, k, t, q
        self.A = k + t
        self.h = t
        self.R = n - k
        self.r = n - self.A
        if xs is None:
            xs = [(i + 1) % q for i in range(n)]
        self.xs = list(xs)
        assert len(set(self.xs)) == n
        self.INV = LazyInv(q)
        self.DIFF = [[(self.xs[i] - self.xs[m]) % q for m in range(n)]
                     for i in range(n)]
        self.INVDIFF = [[self.INV[self.DIFF[i][m]] if i != m else 0
                         for m in range(n)] for i in range(n)]


def lgbinom(a, b):
    return (math.lgamma(a + 1) - math.lgamma(b + 1) -
            math.lgamma(a - b + 1)) / math.log(2)


def next_prime(x):
    def isp(m):
        if m < 2:
            return False
        for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            if m % p == 0:
                return m == p
        d, s = m - 1, 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            y = pow(a, d, m)
            if y in (1, m - 1):
                continue
            for _ in range(s - 1):
                y = y * y % m
                if y == m - 1:
                    break
            else:
                return False
        return True
    while not isp(x):
        x += 1
    return x


def main():
    series = [(24, 6, 3), (32, 8, 3), (40, 10, 3), (48, 12, 3),
              (56, 14, 3), (64, 16, 3)]
    g = []
    for (n, k, h) in series:
        A = k + h
        thresh = lgbinom(n, A) / (h - 1)
        q = next_prime(int(2 ** (thresh + 3)) | 1)
        lgE = math.log2(q + 1) + lgbinom(n, A) - h * math.log2(q)
        row = BigRow(n, k, h, q)
        ceil_ = (2 * row.R - 1) // h
        tag = f"n{n}k{k}h{h}q{q}"
        best = 0
        for V in range(ceil_, 0, -1):
            hit = False
            for s in range(3):
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
                    best = max(best, V)
                    break
            if hit:
                break
        over_ok = 0
        for s in range(5):
            rng = random.Random(555 + s)
            rays = multi_sunflower(row, ceil_ + 1, rng, seed=99 + s)
            if rays is None:
                continue
            sol, rk = realise_family(row, rays, seed=s)
            if sol is None:
                continue
            ok, why = check_rays(row, sol[0], sol[1], rays)
            over_ok += int(ok)
        g.append(dict(tag=tag, n=n, k=k, h=h, q=q, R=row.R, ceil=ceil_,
                      best=best, over=over_ok, lgE_noise=lgE))
        chk(f"S9 structural regime {tag}", lgE < 0, lgE)
        chk(f"S9 best == ceiling {tag}", best == ceil_, (best, ceil_))
        chk(f"S9 ceiling+1 dead {tag}", over_ok == 0, over_ok)
        print(f"S9 {tag}: lgE_noise={lgE:+.2f} R={row.R} "
              f"ceiling={ceil_} best={best} ceil+1 admissible={over_ok}/5")
    xs = [r["n"] for r in g]
    ys = [r["best"] for r in g]
    m = len(xs)
    sx, sy = sum(xs), sum(ys)
    den = m * sum(x * x for x in xs) - sx * sx
    slope = (m * sum(x * y for x, y in zip(xs, ys)) - sx * sy) / den
    icpt = (sy - slope * sx) / m
    OUT["data"] = dict(series=g, slope=slope, intercept=icpt,
                       theory_slope=2 * 0.75 / 3)
    print(f"S9 fit: best ~ {slope:.4f} n {icpt:+.3f}  "
          f"(theory 2(1-rate)/h = {2*0.75/3:.4f})")
    json.dump(OUT, open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "stage9.json"), "w"), indent=1)
    print(f"stage9: PASS={OUT['pass']} FAIL={OUT['fail']}")


if __name__ == "__main__":
    main()
