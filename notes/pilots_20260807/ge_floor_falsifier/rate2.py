#!/usr/bin/env python3
"""*** SUPERSEDED BY cost.py -- DO NOT CITE ITS NUMBERS. ***

Two defects found after running it, both self-corrected in cost.py:
  (1) its cost functional (components of the gcd-graph on FULL norms) is far
      too loose at small h -- it is capped by the number of odd RATIONAL primes
      in the whole box (7 at h=4), so it under-counts the ideal cost ~5x;
  (2) it printed |F_m| = 1 + 2 N' m; an orbit {+- x^r c} has exactly N'
      elements, so |F_m| = 1 + N' m.
cost.py fixes both (exact small-prime ideal counting + gcd components only on
the large cofactors) and reproduces the exhaustive L_2(8) = 17 at 2 ideals.

ESCAPE-RATE, multi-orbit: what does the m-TH extra orbit cost?

F_m = {0} u orbit(c_1) u ... u orbit(c_m),  |F_m| = 1 + 2 N' m  centers.

EXACT UNIT REDUCTION: every nonzero pairwise difference of F_m is a unit times
one of
    c_i ,   c_i (x^t - 1) ,   x^t c_i +- c_j   (i < j, 0 <= t < h)
so the family's odd-ideal support is the union of the odd supports of
m + m(m-1)/2 * 2h  ring elements.  Ideals are unit-invariant, so this is exact.

  ORBCOST(m, N') = KMINLB(F_m)   [components of the gcd-graph on the odd parts
                                  of those norms: a RIGOROUS LOWER BOUND on the
                                  number of distinct odd prime ideals]
  chosen greedily: c_1 = 1 + x, then each c_{i+1} minimises the incremental
  cost over the candidate pool.

The registered decisive question: is L_k(N') POLYNOMIAL or EXPONENTIAL in k?
"""
import itertools
import math
import random
import sys

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from gelib import tower_norm


def oddpart(x):
    x = abs(x)
    while x and x % 2 == 0:
        x >>= 1
    return x


def comps_of(odds):
    n = len(odds)
    par = list(range(n))

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a
    for i in range(n):
        for j in range(i + 1, n):
            if find(i) != find(j) and math.gcd(odds[i], odds[j]) > 1:
                par[find(i)] = find(j)
    return len({find(i) for i in range(n)})


def shift(v, h):
    return [-v[h - 1]] + list(v[:h - 1])


def pair_odds(a, b, h):
    """odd parts of Norm(x^t a +- b), t = 0..h-1."""
    out = []
    cur = list(a)
    for _ in range(h):
        for sgn in (-1, 1):
            d = [cur[t] + sgn * b[t] for t in range(h)]
            if any(d):
                o = oddpart(tower_norm(d))
                if o > 1:
                    out.append(o)
        cur = shift(cur, h)
    return out


def valid(v, h):
    return (h - sum(1 for t in v if t != 0)) % 2 == 0


def main():
    hs = [int(t) for t in sys.argv[1].split(",")]
    mmax = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    trials = int(sys.argv[3]) if len(sys.argv) > 3 else 250
    rng = random.Random(770807)

    print("== ORBCOST(m, N'): odd prime IDEALS needed for m orbits of centers ==")
    for h in hs:
        N = 2 * h
        c1 = [0] * h
        c1[0] = 1
        c1[1] = 1
        chosen = [c1]
        odds = [oddpart(tower_norm(c1))]
        odds = [o for o in odds if o > 1]
        print("\n N' = %d  (h = %d)" % (N, h))
        print("  %-4s %-10s %-12s %-16s %-14s" %
              ("m", "|F_m|", "ORBCOST", "centers/ideal", "quadratic fit"))
        print("  %-4d %-10d %-12d %-16s %-14s" %
              (1, 1 + 2 * N, comps_of(odds) if odds else 0, "inf (free)", "-"))
        for m in range(2, mmax + 1):
            # candidate pool
            if h <= 8:
                pool = [list(v) for v in itertools.product((-1, 0, 1), repeat=h)
                        if any(v) and valid(v, h)]
                mode = "EXHAUSTIVE"
            else:
                pool = []
                for w in range(1, h + 1):
                    v = [0] * h
                    for t in range(w):
                        v[t] = 1
                    if valid(v, h):
                        pool.append(v)
                    v2 = [0] * h
                    for t in range(w):
                        v2[t] = 1 if t % 2 == 0 else -1
                    if valid(v2, h):
                        pool.append(v2)
                while len(pool) < trials:
                    v = [rng.choice((-1, 0, 1)) for _ in range(h)]
                    if any(v) and valid(v, h):
                        pool.append(v)
                mode = "GREEDY/SAMPLED"
            # orbit membership of already-chosen generators
            used = set()
            for c in chosen:
                cur = list(c)
                for _ in range(h):
                    used.add(tuple(cur))
                    used.add(tuple(-t for t in cur))
                    cur = shift(cur, h)
            best = None
            bestv = None
            bestodds = None
            for v in pool:
                if tuple(v) in used:
                    continue
                extra = []
                o = oddpart(tower_norm(v))
                if o > 1:
                    extra.append(o)
                for c in chosen:
                    extra.extend(pair_odds(c, v, h))
                k = comps_of(odds + extra)
                if best is None or k < best:
                    best = k
                    bestv = v
                    bestodds = odds + extra
            chosen.append(bestv)
            odds = bestodds
            nf = 1 + 2 * N * m
            fit = (m * (m - 1) / 2.0) * (h / 4.0)
            print("  %-4d %-10d %-12d %-16.3f %-14.1f  [%s]" %
                  (m, nf, best, (nf - 1.0) / best if best else float('inf'),
                   fit, mode))
    print("\nquadratic fit = C(m,2)*h/4 -- the model 'each ORBIT PAIR costs "
          "h/4 odd ideals'.")


if __name__ == "__main__":
    main()
