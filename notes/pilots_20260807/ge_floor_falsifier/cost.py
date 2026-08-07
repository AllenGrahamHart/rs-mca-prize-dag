#!/usr/bin/env python3
"""TIGHT, RIGOROUS lower bound on the odd prime-IDEAL cost of a family, and the
ESCAPE-RATE law it yields -- evaluated up to the prize cell N' = 128.

COST(F) := # distinct odd prime ideals dividing some nonzero difference of F.
We bound it below by splitting each difference norm at 10^6:

  small part : trial-divided exactly; for each small prime p we take the LCM
               of the sigma_p = gcd(d mod p, x^h+1) over the whole family, and
               count deg(lcm)/f_p ideals.  EXACT.
  large part : cofactors > 10^6.  Components of their gcd-graph use pairwise
               DISJOINT prime sets, so #components is a rigorous lower bound
               on the number of additional primes, hence of ideals.

COST_LB = exact_small + comps_large   <=   COST(F).
A lower bound on COST is an UPPER bound on RATE = centers/ideal, which is the
direction that matters for a route-killing verdict.

EXACT UNIT REDUCTION: for F = {0} u orbit(c_1) u ... u orbit(c_m) with
orbit(z) = {+- x^r z} (size N'), every nonzero difference is a unit times one
of   c_i ,  c_i(x^t - 1) ,  x^t c_i +- c_j  (i<j, 0<=t<h);  ideals are
unit-invariant, so those m + m(m-1)/2*2h elements carry the whole support.
"""
import itertools
import math
import random
import sys

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from gelib import tower_norm, sigma, plcm, mult_order

import os
SMALL = int(os.environ.get("GE_SMALL", 10 ** 6))


def small_primes(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    return [i for i in range(2, limit + 1) if sieve[i]]


PR = small_primes(SMALL)
# product of the small primes: one gcd extracts the whole small-prime radical
# of a 200-bit norm, instead of 78498 trial divisions.
PRODSMALL = 1
for _p in PR:
    PRODSMALL *= _p


def oddpart(x):
    x = abs(x)
    while x and x % 2 == 0:
        x >>= 1
    return x


def cost_lb(vecs, h, detail=False):
    """vecs: iterable of ring elements (as coefficient lists).  Returns
    (COST_LB, exact_small_ideals, comps_large, n_odd)."""
    N = 2 * h
    lcms = {}
    cofs = []
    n_odd = 0
    for v in vecs:
        o = oddpart(tower_norm(list(v)))
        if o == 1:
            continue
        n_odd += 1
        rem = o
        rad = math.gcd(o, PRODSMALL)
        if rad > 1:
            for p in PR:
                if p > rad:
                    break
                if rad % p == 0:
                    while rem % p == 0:
                        rem //= p
                    rad //= p
                    s = sigma(v, p, h)
                    lcms[p] = plcm(lcms[p], s, p) if p in lcms else s
                    if rad == 1:
                        break
        if rem > 1:
            if rem < SMALL * SMALL:
                # no prime factor below SMALL survives, so rem < SMALL^2 forces
                # rem PRIME.  Place it exactly.
                s = sigma(v, rem, h)
                lcms[rem] = plcm(lcms[rem], s, rem) if rem in lcms else s
            else:
                cofs.append(rem)
    exact = 0
    for p, s in lcms.items():
        exact += (len(s) - 1) // mult_order(p, N)
    # components of the gcd-graph on the large cofactors
    n = len(cofs)
    par = list(range(n))

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a
    for i in range(n):
        for j in range(i + 1, n):
            if find(i) != find(j) and math.gcd(cofs[i], cofs[j]) > 1:
                par[find(i)] = find(j)
    comps = len({find(i) for i in range(n)})
    return exact + comps, exact, comps, n_odd


def shift(v, h):
    return [-v[h - 1]] + list(v[:h - 1])


def orbit_reps(chosen, cand, h):
    """the ring elements carrying the whole odd support of
    {0} u orbits(chosen + [cand])"""
    out = [list(cand)]
    for c in chosen:
        cur = list(c)
        for _ in range(h):
            for sgn in (-1, 1):
                d = [cur[t] + sgn * cand[t] for t in range(h)]
                if any(d):
                    out.append(d)
            cur = shift(cur, h)
    return out


def valid(v, h):
    return (h - sum(1 for t in v if t != 0)) % 2 == 0


def main():
    hs = [int(t) for t in sys.argv[1].split(",")]
    mmax = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    trials = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    rng = random.Random(770807)

    print("== ESCAPE-RATE LAW: ORBCOST(m, N') with the TIGHT lower bound ==")
    print("   |F_m| = 1 + m*N' centers (orbits have exactly N' elements)")
    for h in hs:
        N = 2 * h
        c1 = [0] * h
        c1[0] = 1
        c1[1] = 1
        chosen = [c1]
        acc = [list(c1)]
        base_cost = cost_lb(acc, h)[0]
        print("\n N' = %-4d (h = %-3d)" % (N, h))
        print("  %-4s %-9s %-10s %-9s %-9s %-8s %-16s %s" %
              ("m", "|F_m|", "COST_LB", "exact_sm", "comps_lg", "n_odd",
               "centers/ideal", "pool"))
        print("  %-4d %-9d %-10d %-9d %-9d %-8d %-16s %s" %
              (1, 1 + N, base_cost, 0, 0, 0, "inf (free)", "-"))
        for m in range(2, mmax + 1):
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
                mode = "GREEDY/SAMPLED %d" % len(pool)
            used = set()
            for c in chosen:
                cur = list(c)
                for _ in range(h):
                    used.add(tuple(cur))
                    used.add(tuple(-t for t in cur))
                    cur = shift(cur, h)
            best = None
            for v in pool:
                if tuple(v) in used:
                    continue
                trial = acc + orbit_reps(chosen, v, h)
                r = cost_lb(trial, h)
                if best is None or r[0] < best[0]:
                    best = r
                    bestv = v
                    besttrial = trial
            chosen.append(bestv)
            acc = besttrial
            nf = 1 + m * N
            print("  %-4d %-9d %-10d %-9d %-9d %-8d %-16.3f %s" %
                  (m, nf, best[0], best[1], best[2], best[3],
                   (nf - 1.0) / best[0] if best[0] else float('inf'), mode))


if __name__ == "__main__":
    main()
