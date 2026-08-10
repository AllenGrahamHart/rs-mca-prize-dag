"""td_global.py -- EXACT maximum of F_LIST over ALL received words.

F_LIST(y) = #{f in C : agree(y,f) >= a} = #{e : wt(e) <= m = n-a, e = y mod C}.
So  MAXWORD_LIST(n,sigma) = max over syndrome classes of the number of
weight-<=m error patterns in the class.  Syndrome S_j = sum_x e_x x^j,
j = 1..n-k; the word class's polynomial degree is n - min{j : S_j != 0},
so the SLACK delta = m - j_min is read straight off the syndrome.

Scaling e -> lambda e maps buckets bijectively, so we enumerate only
NORMALIZED e (first nonzero value = 1) and bucket by the CANONICAL syndrome
(divided by its own first nonzero coordinate); the resulting bucket size
equals the true F_LIST of that word class exactly.

Two passes with a coarse saturating counter keep RAM flat.

Usage: tools/ramguard local -- python3 <this> n q sigma[,sigma..] out [logP] [thr]
"""
import json
import sys
from array import array
from itertools import combinations
from math import comb

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from td_core import mu, qcore_count  # noqa: E402


def run_cell(n, q, k, sigma, logP=25, thr=2):
    xs = mu(n, q)
    a = k + sigma
    m = n - a
    ns = n - k                      # number of syndrome coordinates
    inv = [0] * q
    for v in range(1, q):
        inv[v] = pow(v, q - 2, q)
    # pw[i][j] = x_i^(j+1), j = 0..ns-1
    pw = []
    for i in range(n):
        row = []
        cur = xs[i]
        for _ in range(ns):
            row.append(cur)
            cur = cur * xs[i] % q
        pw.append(row)
    qp = [q ** j for j in range(ns)]
    P = 1 << logP
    coarse = array("B", bytes(P))
    total = 0

    def walk(collect):
        """DFS over normalized error patterns of weight 1..m."""
        nonlocal total
        acc = {}
        S = [0] * ns
        def rec(pos_idx, supp_left, first):
            nonlocal total
            if supp_left == 0:
                # canonicalise
                jz = -1
                for j in range(ns):
                    if S[j]:
                        jz = j
                        break
                if jz < 0:
                    return
                iv = inv[S[jz]]
                key = 0
                for j in range(jz, ns):
                    key += (S[j] * iv % q) * qp[j]
                if collect:
                    if coarse[key & (P - 1)] >= thr:
                        acc[key] = acc.get(key, 0) + 1
                else:
                    total += 1
                    c = key & (P - 1)
                    if coarse[c] < 255:
                        coarse[c] += 1
                return
            for i in range(pos_idx, n - supp_left + 1):
                row = pw[i]
                vals = (1,) if first else range(1, q)
                for v in vals:
                    for j in range(ns):
                        S[j] = (S[j] + v * row[j]) % q
                    rec(i + 1, supp_left - 1, False)
                    for j in range(ns):
                        S[j] = (S[j] - v * row[j]) % q
        for w in range(1, m + 1):
            rec(0, w, True)
        return acc

    walk(False)
    acc = walk(True)
    best = max(acc.values()) if acc else 1
    maxcoarse = max(coarse)
    per_slack = {}
    argmax = None
    for key, c in acc.items():
        # unpack canonical syndrome -> j_min -> slack
        kk, j0 = key, -1
        for j in range(ns):
            if kk % q:
                j0 = j
                break
            kk //= q
        d = m - (j0 + 1)
        if c > per_slack.get(d, 0):
            per_slack[d] = c
        if c == best and argmax is None:
            argmax = (key, d)
    qc, qbest = qcore_count(n, k, sigma)
    return {
        "n": n, "q": q, "k": k, "sigma": sigma, "a": a, "m": m,
        "normalized_patterns": total,
        "C(n,a)": comb(n, a),
        "pigeonhole_avg": comb(n, a) / q ** sigma,
        "MAXWORD_LIST": best,
        "max_slack_of_argmax": argmax[1] if argmax else None,
        "max_per_slack": {str(d): v for d, v in sorted(per_slack.items())},
        "slack_strata_below_threshold": thr,
        "qcore_count": qc, "qcore_best_M_N_km": qbest,
        "coarse_max": maxcoarse, "logP": logP, "threshold": thr,
        "surviving_keys": len(acc),
    }


def main():
    n, q = int(sys.argv[1]), int(sys.argv[2])
    sigmas = [int(s) for s in sys.argv[3].split(",")]
    out = sys.argv[4]
    logP = int(sys.argv[5]) if len(sys.argv) > 5 else 25
    thr = int(sys.argv[6]) if len(sys.argv) > 6 else 2
    k = n // 2
    res = {"n": n, "q": q, "k": k, "cells": []}
    for sigma in sigmas:
        cell = run_cell(n, q, k, sigma, logP, thr)
        res["cells"].append(cell)
        print(json.dumps(cell), flush=True)
        with open(out, "w") as fh:
            json.dump(res, fh, indent=1)


if __name__ == "__main__":
    main()
