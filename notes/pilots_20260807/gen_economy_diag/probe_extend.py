#!/usr/bin/env python3
"""Probe: is MAXPOW2(N) = N+1 exactly, and is the extremal family {0} u orbit(c)?

(a) STRUCTURE: check that {0} u {x^r c} is a POW2 clique of size N+1 whenever
    Norm(c) is a power of 2 -- a constructive lower bound at every N.
(b) EXTENSION: at N = 32 (box too big to enumerate) search hard for an
    (N+2)-th center extending the canonical clique, and for any POW2 edge
    between two DIFFERENT unit orbits.
(c) INTEGER-FACTOR CONFINEMENT: the profile_covering_obstruction FREE class is
    "(integer) x (small element)"; check what integer factors a half-size-subset
    e_1 difference can actually carry.
"""
import itertools
import sys

import numpy as np

sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/"
                   "pilots_20260807/gen_economy_diag")
from toy_cap import exact_norm, is_pow2, sample_centers, all_centers  # noqa: E402


def mulx(v, n):
    return [-v[n - 1]] + list(v[:n - 1])


def orbit(c, n):
    o, cur = [], list(c)
    for _ in range(2 * n):
        o.append(tuple(cur))
        cur = mulx(cur, n)
    return o


def pow2_diff(a, b, n):
    d = [a[i] - b[i] for i in range(n)]
    if not any(d):
        return False
    return is_pow2(exact_norm(d, n))


def is_clique(S, n):
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            if not pow2_diff(S[i], S[j], n):
                return False, (i, j)
    return True, None


def canonical(n, rng, tries=4000):
    """Find a center c with 2-power norm; return {0} u orbit(c)."""
    zero = tuple([0] * n)
    for _ in range(tries):
        c = sample_centers(n, 1, rng)[0]
        nm = exact_norm(list(c), n)
        if nm != 0 and is_pow2(nm):
            return c, [zero] + orbit(c, n)
    return None, None


def main():
    rng = np.random.default_rng(2026)

    print("== (a) STRUCTURE: {0} u orbit(c) is a POW2 clique of size N+1 ==")
    for N in (8, 16, 32, 64):
        n = N // 2
        c, K = canonical(n, rng)
        if c is None:
            print("  N=%3d  no 2-power-norm center found in the sample" % N)
            continue
        ok, bad = is_clique(K, n)
        print("  N=%3d  |{0} u orbit(c)| = %d = N+1? %s   all-pairs POW2? %s"
              % (N, len(K), len(K) == N + 1, ok if bad is None else bad))

    print("\n== (b) EXTENSION PROBE at N=32: can any center extend the clique? ==")
    N, n = 32, 16
    c, K = canonical(n, rng)
    zero = tuple([0] * n)
    Kset = set(K)
    tested = 0
    hits = []
    # 1. random search
    for _ in range(120):
        batch = sample_centers(n, 2000, rng)
        for y in batch:
            if y in Kset:
                continue
            tested += 1
            if all(pow2_diff(y, k, n) for k in K[:4]):    # cheap prefilter
                if all(pow2_diff(y, k, n) for k in K):
                    hits.append(y)
        if hits:
            break
    print("  random: tested %d candidate centers, extensions found: %d"
          % (tested, len(hits)))

    # 2. structured search: every OTHER unit orbit's representatives
    cross = 0
    checked = 0
    for _ in range(400):
        d = sample_centers(n, 1, rng)[0]
        if d in Kset or not any(d):
            continue
        for y in orbit(d, n):
            checked += 1
            if pow2_diff(y, zero, n) and pow2_diff(y, c, n):
                cross += 1
    print("  structured: %d cross-orbit members checked, "
          "%d simultaneously POW2 against BOTH 0 and c" % (checked, cross))

    print("\n== (c) INTEGER-FACTOR CONFINEMENT (the FREE flat class) ==")
    print("  a center has folded coeffs in {-1,0,1}; a difference in {-2,..,2}.")
    for N in (8, 16, 32):
        n = N // 2
        cents = all_centers(n) if n <= 8 else sample_centers(n, 4000, rng)
        best = 1
        for i in range(min(len(cents), 700)):
            for j in range(i + 1, min(len(cents), 700)):
                d = [cents[i][k] - cents[j][k] for k in range(n)]
                if not any(d):
                    continue
                g = 0
                for t in d:
                    g = abs(t) if g == 0 else _gcd(g, abs(t))
                best = max(best, g)
        print("  N=%3d  max integer factor over sampled difference pairs = %d"
              % (N, best))
    print("  => an integer factor m >= 3 would force every coefficient into")
    print("     {0, +/-m} with |m| <= 2: impossible. So m in {1,2}, and 2 is")
    print("     itself an associate of lambda^(N/2). The integer freebie adds")
    print("     NOTHING outside the 2-adic class for e_1 differences.")


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    main()
