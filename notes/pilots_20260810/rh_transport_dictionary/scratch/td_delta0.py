"""td_delta0.py -- EXACT maximum of F_LIST over MINIMAL-SLACK received words.

A received word of degree exactly a (slack delta = 0) is, up to scaling and
mod C, a monic degree-a polynomial Y.  A codeword f is in its list iff
Y - f = c * L_A for an a-subset A of D, i.e. iff L_A matches Y in its top
sigma+1 coefficients.  Hence

    F_LIST(Y) = #{ A subset D, |A| = a : (e_1(A),..,e_sigma(A)) = signature(Y) }

and the slack-0 maximum over ALL received words is the MAX BUCKET of the map
A -> (e_1(A),...,e_sigma(A)).  This is exactly the stratum the banked razor
witness family (qcore, Y = X^k L_T0) lives in.

Usage: tools/ramguard local -- python3 <this> n q sigma[,sigma...] outfile
"""
import json
import sys
from array import array
from math import comb

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from td_core import mu, qcore_count, qcore_family, qcore_signature  # noqa: E402


def max_bucket(n, q, k, sigma):
    xs = mu(n, q)
    a = k + sigma
    keyspace = q ** sigma
    use_arr = keyspace <= 40_000_000
    cnt = array("i", bytes(4 * keyspace)) if use_arr else {}
    e = [0] * (sigma + 1)
    e[0] = 1
    pw = [q ** i for i in range(sigma)]
    nodes = 0

    def rec(idx, need):
        nonlocal nodes
        nodes += 1
        if need == 0:
            key = 0
            for i in range(1, sigma + 1):
                key += e[i] * pw[i - 1]
            if use_arr:
                cnt[key] += 1
            else:
                cnt[key] = cnt.get(key, 0) + 1
            return
        if n - idx < need:
            return
        for j in range(idx, n - need + 1):
            x = xs[j]
            for i in range(sigma, 0, -1):
                e[i] = (e[i] + x * e[i - 1]) % q
            rec(j + 1, need - 1)
            for i in range(1, sigma + 1):
                e[i] = (e[i] - x * e[i - 1]) % q

    sys.setrecursionlimit(10000)
    rec(0, a)
    if use_arr:
        best = max(cnt)
        nkeys = sum(1 for v in cnt if v)
        nbest = sum(1 for v in cnt if v == best)
        hist = {}
        for v in cnt:
            if v:
                hist[v] = hist.get(v, 0) + 1
    else:
        best = max(cnt.values())
        nkeys = len(cnt)
        nbest = sum(1 for v in cnt.values() if v == best)
        hist = {}
        for v in cnt.values():
            hist[v] = hist.get(v, 0) + 1
    return best, nkeys, nbest, hist, cnt, nodes


def main():
    n, q = int(sys.argv[1]), int(sys.argv[2])
    sigmas = [int(s) for s in sys.argv[3].split(",")]
    out = sys.argv[4]
    k = n // 2
    res = {"n": n, "q": q, "k": k, "cells": []}
    for sigma in sigmas:
        a = k + sigma
        best, nkeys, nbest, hist, cnt, nodes = max_bucket(n, q, k, sigma)
        qc, qbest = qcore_count(n, k, sigma)
        cell = {
            "sigma": sigma,
            "a": a,
            "C(n,a)": comb(n, a),
            "delta0_max": best,
            "n_keys_hit": nkeys,
            "n_keys_at_max": nbest,
            "bucket_hist_top": sorted(hist.items(), reverse=True)[:8],
            "qcore_count": qc,
            "qcore_best_M_N_km": qbest,
            "qcore_family": qcore_family(n, k, sigma),
            "dfs_nodes": nodes,
        }
        if qbest is not None:
            M = qbest[0]
            sig, A = qcore_signature(n, q, k, sigma, M)
            key = sum(sig[i] * q ** i for i in range(sigma))
            cell["qcore_signature"] = list(sig)
            cell["qcore_bucket_measured"] = int(cnt[key])
            cell["qcore_example_set"] = list(A)
        res["cells"].append(cell)
        print(json.dumps(cell), flush=True)
        with open(out, "w") as fh:
            json.dump(res, fh, indent=1)


if __name__ == "__main__":
    main()
