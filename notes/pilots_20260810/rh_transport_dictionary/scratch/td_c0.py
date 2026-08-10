"""td_c0.py -- EXACT CHARACTERISTIC-ZERO slack-0 maximum.

Same object as td_delta0.py but over Z[zeta_n] instead of F_q: the bucket key
is the exact tuple (e_1(A),...,e_sigma(A)) reduced modulo the cyclotomic
polynomial Phi_n, so two a-subsets collide iff their locators agree in the top
sigma coefficients AS ALGEBRAIC NUMBERS.  This is the object the banked
THEOREM CAP scopes ("within the coset/dressing/perturbation universe the
char-0 supply is capped at the plateau (Lam-Leung + NESTING)").

Usage: tools/ramguard local -- python3 <this> n sigma[,sigma..] outfile
"""
import json
import sys
from math import comb

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from td_core import divisors, qcore_count, qcore_family  # noqa: E402


def poly_div(num, den):
    """Exact division of integer polys (lists, low-to-high), den monic."""
    num = num[:]
    dn = len(den) - 1
    out = [0] * (len(num) - dn)
    for i in range(len(num) - 1, dn - 1, -1):
        c = num[i]
        if c:
            out[i - dn] = c
            for j in range(dn + 1):
                num[i - dn + j] -= c * den[j]
    assert all(v == 0 for v in num), "not divisible"
    return out


def cyclotomic(n, cache={}):
    if n in cache:
        return cache[n]
    poly = [-1] + [0] * (n - 1) + [1]          # x^n - 1
    for d in divisors(n):
        if d < n:
            poly = poly_div(poly, cyclotomic(d))
    cache[n] = poly
    return poly


def reduce_mod(vec, phi):
    """Remainder of sum vec[i] x^i modulo monic phi (integer coefficients)."""
    v = vec[:]
    dp = len(phi) - 1
    for i in range(len(v) - 1, dp - 1, -1):
        c = v[i]
        if c:
            v[i] = 0
            for j in range(dp):
                v[i - dp + j] -= c * phi[j]
    return tuple(v[:dp])


def max_bucket_c0(n, k, sigma):
    a = k + sigma
    phi = cyclotomic(n)
    # e[i] held as coefficient vectors in Z[x]/(x^n - 1)
    e = [[0] * n for _ in range(sigma + 1)]
    e[0][0] = 1
    cnt = {}
    nodes = 0

    def rec(idx, need):
        nonlocal nodes
        nodes += 1
        if need == 0:
            key = tuple(reduce_mod(e[i], phi) for i in range(1, sigma + 1))
            cnt[key] = cnt.get(key, 0) + 1
            return
        if n - idx < need:
            return
        for j in range(idx, n - need + 1):
            for i in range(sigma, 0, -1):
                src, dst = e[i - 1], e[i]
                for t in range(n):
                    dst[(t + j) % n] += src[t]
            rec(j + 1, need - 1)
            for i in range(1, sigma + 1):
                src, dst = e[i - 1], e[i]
                for t in range(n):
                    dst[(t + j) % n] -= src[t]

    sys.setrecursionlimit(10000)
    rec(0, a)
    best = max(cnt.values())
    hist = {}
    for v in cnt.values():
        hist[v] = hist.get(v, 0) + 1
    return best, len(cnt), hist, nodes


def main():
    n = int(sys.argv[1])
    sigmas = [int(s) for s in sys.argv[2].split(",")]
    out = sys.argv[3]
    k = n // 2
    res = {"n": n, "k": k, "char": 0, "cells": []}
    for sigma in sigmas:
        best, nkeys, hist, nodes = max_bucket_c0(n, k, sigma)
        qc, qbest = qcore_count(n, k, sigma)
        cell = {
            "sigma": sigma, "a": k + sigma, "C(n,a)": comb(n, k + sigma),
            "char0_delta0_max": best, "n_keys": nkeys,
            "bucket_hist_top": sorted(hist.items(), reverse=True)[:8],
            "qcore_count": qc, "qcore_best_M_N_km": qbest,
            "qcore_family": qcore_family(n, k, sigma), "dfs_nodes": nodes,
        }
        res["cells"].append(cell)
        print(json.dumps(cell), flush=True)
        with open(out, "w") as fh:
            json.dump(res, fh, indent=1)


if __name__ == "__main__":
    main()
