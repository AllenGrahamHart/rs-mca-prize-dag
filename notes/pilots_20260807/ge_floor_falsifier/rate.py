#!/usr/bin/env python3
"""*** ITS `ORBITADD`/`RATE` NUMBERS ARE SUPERSEDED BY cost.py. ***
The cost functional here (components of the gcd-graph on FULL norms) is capped
by the number of odd RATIONAL primes in the whole box, so it under-counts the
ideal cost about 5x at small h (it reported ORBITADD(8) = 1 where the exact
answer, confirmed by the exhaustive clique search, is 2).  The EXACT UNIT
REDUCTION documented below is correct and is reused by cost.py.

ESCAPE-RATE upper bounds: what does ONE EXTRA ORBIT of centers COST in odd
prime ideals?  Measured at h = 4, 8, 16, 32, 64 -- i.e. INCLUDING the prize
cell N' = 128.

EXACT UNIT REDUCTION (this is what makes h = 64 reachable).
For F = {0} u orbit(c) u orbit(c'), orbit(z) = {+- x^r z}, every nonzero
pairwise difference is a UNIT times one of

    c ,  c' ,  c (x^t - 1) ,  c' (x^t - 1) ,  x^t c - c' ,  x^t c + c'

with 0 <= t < h.  Ideals are unit-invariant, so the family's odd ideal support
is EXACTLY the union of the odd supports of those 2h + 2 elements.  With
c = 1 + x (Norm 2) the first four groups are lambda-powers and cost 0.

Functionals (CATCH-19C):
  REPS(N')       = 2h + 2, the number of difference IDEAL CLASSES
  KMINLB(F)      RIGOROUS LOWER BOUND on the number of distinct odd prime
                 IDEALS certifying F: components of the gcd-graph on the odd
                 parts of the representative norms use pairwise DISJOINT
                 rational-prime sets, so #components <= #primes <= #ideals.
                 gcds only -- no factorization, so it runs at h = 64.
  ORBITADD(N')   = min over c' of KMINLB
  RATE(N')       = 2N' / ORBITADD(N')   [extra centers bought per odd ideal]
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
    """#connected components of the gcd-graph on odds (all > 1)."""
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
    """multiply by x in Z[x]/(x^h+1)."""
    return [-v[h - 1]] + list(v[:h - 1])


def pair_cost(cp, h, cvec):
    """odd-ideal LOWER BOUND for F = {0} u orbit(c) u orbit(c')."""
    odds = []
    o = oddpart(tower_norm(list(cp)))
    if o > 1:
        odds.append(o)
    cur = list(cvec)
    for _ in range(h):
        for sgn in (-1, 1):
            d = [cur[t] + sgn * cp[t] for t in range(h)]
            if any(d):
                o = oddpart(tower_norm(d))
                if o > 1:
                    odds.append(o)
        cur = shift(cur, h)
    return comps_of(odds), len(odds)


def valid_center(v, h):
    return (h - sum(1 for t in v if t != 0)) % 2 == 0


def main():
    hs = [int(t) for t in sys.argv[1].split(",")]
    trials = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
    rng = random.Random(20260807)

    print("== ORBITADD: price of the CHEAPEST SECOND ORBIT, in odd prime ideals ==")
    print("%-5s %-6s %-7s %-8s %-11s %-9s %-24s" %
          ("h", "N'", "|F|", "REPS", "ORBITADD", "RATE", "search class"))
    for h in hs:
        N = 2 * h
        c = [0] * h
        c[0] = 1
        c[1] = 1
        O1 = set()
        cur = list(c)
        for _ in range(h):
            O1.add(tuple(cur))
            O1.add(tuple(-t for t in cur))
            cur = shift(cur, h)

        if h <= 8:
            cands = [v for v in itertools.product((-1, 0, 1), repeat=h)
                     if valid_center(v, h) and any(v) and tuple(v) not in O1]
            mode = "EXHAUSTIVE over C(N')"
        else:
            cands = []
            seen = set()
            # structured low-weight and all-ones-like candidates first
            for w in range(1, h + 1):
                v = [0] * h
                for t in range(w):
                    v[t] = 1
                if valid_center(v, h) and tuple(v) not in O1:
                    cands.append(tuple(v))
                    seen.add(tuple(v))
                v2 = [0] * h
                for t in range(w):
                    v2[t] = 1 if t % 2 == 0 else -1
                if valid_center(v2, h) and tuple(v2) not in O1:
                    cands.append(tuple(v2))
                    seen.add(tuple(v2))
            while len(cands) < trials:
                v = tuple(rng.choice((-1, 0, 1)) for _ in range(h))
                if not any(v) or not valid_center(v, h) or v in seen or v in O1:
                    continue
                seen.add(v)
                cands.append(v)
            mode = "SAMPLED %d + structured" % trials

        best = None
        bestc = None
        for cp in cands:
            k, nn = pair_cost(cp, h, c)
            if best is None or k < best:
                best = k
                bestc = cp
        rate = (2.0 * N) / best if best else float('inf')
        print("%-5d %-6d %-7d %-8d %-11d %-9.3f %-24s" %
              (h, N, 1 + 2 * N, 2 * h + 2, best, rate, mode))
        print("      cheapest c' = %s" % (bestc,))
    print()
    print("RATE = extra centers per odd prime ideal.")


if __name__ == "__main__":
    main()
