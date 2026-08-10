"""td_scan.py -- exact F_LIST of STRUCTURED received words (few-term words).

For an explicit received word Y (deg <= n-1) the list is computed exactly:
an a-subset A is an agreement set iff Y mod L_A has degree < k, and the
listed codeword is that remainder.  Distinct remainders are deduped, so the
output is F_LIST, F_SUBSET, the agreement profile and the slack.

Scanned family: all one- and two-term words with both exponents in
[k, n-1] (the only coefficients that survive mod C), coefficient ratios
taken from a small explicit set.  This family contains round-29's
THEOREM A product word Y = X^(n-1) + c X^(n/2).

Usage: tools/ramguard local -- python3 <this> n q sigma[,sigma..] out
"""
import json
import sys
from math import comb

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from td_core import mu, qcore_count  # noqa: E402


def flist(n, q, k, a, xs, Y):
    """Exact F_LIST / F_SUBSET / profile of the word Y (coeff list, low->high)."""
    m = n - a
    deg = max([i for i, c in enumerate(Y) if c], default=-1)
    words = {}
    subs = 0
    L = [0] * (a + 1)
    L[0] = 1
    ln = [0]                      # current length-1 (degree of L)

    def rec(idx, need):
        nonlocal subs
        if need == 0:
            # remainder of Y mod L (L monic of degree a)
            r = Y[:]
            for i in range(len(r) - 1, a - 1, -1):
                c = r[i]
                if c:
                    r[i] = 0
                    base = i - a
                    for j in range(a):
                        r[base + j] = (r[base + j] - c * L[j]) % q
            if all(v == 0 for v in r[k:a]):
                subs += 1
                key = tuple(r[:k])
                words[key] = words.get(key, 0) + 1
            return
        if n - idx < need:
            return
        for j in range(idx, n - need + 1):
            x = xs[j]
            d = ln[0]
            L[d + 1] = 1
            for i in range(d, 0, -1):
                L[i] = (L[i - 1] - x * L[i]) % q
            L[0] = (-x * L[0]) % q
            ln[0] = d + 1
            rec(j + 1, need - 1)
            # undo: divide by (X - x)  (synthetic division, exact)
            d = ln[0]
            new = [0] * (a + 1)
            carry = 0
            for i in range(d - 1, -1, -1):
                carry = (L[i + 1] + x * carry) % q if i + 1 <= d else 0
                new[i] = carry
            for i in range(a + 1):
                L[i] = new[i] if i < d else 0
            ln[0] = d - 1

    sys.setrecursionlimit(10000)
    rec(0, a)
    prof = {}
    for key in words:
        agree = 0
        for x in xs:
            v = 0
            for c in reversed(key):
                v = (v * x + c) % q
            yv = 0
            for c in reversed(Y):
                yv = (yv * x + c) % q
            if v == yv:
                agree += 1
        prof[agree] = prof.get(agree, 0) + 1
    return len(words), subs, prof, deg


def main():
    n, q = int(sys.argv[1]), int(sys.argv[2])
    sigmas = [int(s) for s in sys.argv[3].split(",")]
    out = sys.argv[4]
    k = n // 2
    xs = mu(n, q)
    g = xs[1]
    ratios = sorted({1, q - 1, g % q, g * g % q, (g + 1) % q, 2 % q, 3 % q} - {0})
    res = {"n": n, "q": q, "k": k, "ratios": ratios, "cells": []}
    for sigma in sigmas:
        a = k + sigma
        qc, qbest = qcore_count(n, k, sigma)
        best = []
        for d1 in range(k, n):
            Y = [0] * n
            Y[d1] = 1
            fl, fs, prof, deg = flist(n, q, k, a, xs, Y)
            best.append((fl, fs, [d1], 1, deg - a, prof))
            for d2 in range(k, d1):
                for c in ratios:
                    Y = [0] * n
                    Y[d1] = 1
                    Y[d2] = c
                    fl, fs, prof, deg = flist(n, q, k, a, xs, Y)
                    best.append((fl, fs, [d1, d2], c, deg - a, prof))
        best.sort(reverse=True)
        cell = {
            "sigma": sigma, "a": a, "qcore_count": qc, "qcore_M_N_km": qbest,
            "C(n,a)/n": comb(n, a) / n,
            "C(n,a)/n^sigma": comb(n, a) / n ** sigma,
            "scanned_words": len(best),
            "top": [
                {"F_LIST": b[0], "F_SUBSET": b[1], "degrees": b[2],
                 "ratio": b[3], "slack": b[4], "profile": b[5]}
                for b in best[:6]
            ],
        }
        res["cells"].append(cell)
        print(json.dumps(cell), flush=True)
        with open(out, "w") as fh:
            json.dump(res, fh, indent=1)


if __name__ == "__main__":
    main()
