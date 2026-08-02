#!/usr/bin/env python3
"""EXPERIMENT D -- does (SF-SELFCOLLISION) still kill Gamma_lo when a/F -> 0?

(SF-SELFCOLLISION) proves  |S_J ^ S_J'| = g + m|J ^ J'|,  max = A - m >= K.
The maximum is attained ONLY by ADJACENT label sets (|J ^ J'| = a-1).  A
slope leaves Gamma_lo only if the support SELECTED at that slope has an
adjacent partner that is itself SELECTED (one support per slope).  Since
adjacency changes sigma_1, adjacent members always sit at DIFFERENT slopes,
so the kill is not automatic: it depends on the selector.

At official RowC 1/4 the split-fibre family is the whole witness set (mean
random supply per slope 2^-127 in the exposed window), so the selection at
each slope is a choice among planted label sets only -- exactly the model
here.  The control parameter is

     nu := a(b-a) * (#slopes) / C(b,a)      (expected SELECTED neighbours
                                             of a member under a UNIFORM
                                             selector)

RowC 1/4 official: a=65, b=255, C=2^204, q=2^192  ->  nu = 3.01.
Under a uniform selector Gamma_lo ~ q*e^{-nu}; the banked claim Gamma_lo = 0
therefore needs the SELECTOR, not the identity.  This measures both.

Run:  tools/ramguard local -- python3 expD.py
"""
from __future__ import annotations

import json
import math
import os
import random
import sys
from itertools import combinations

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import core

HERE = os.path.dirname(os.path.abspath(__file__))

# (n, m, g, a, b) with m<=h<2m, A = g+m*a, K = A-h;  q swept
SHAPES = [
    dict(n=64, m=2, g=1, a=6, b=31, h=3),     # A=13, K=10, C(31,6)=736281
    dict(n=64, m=2, g=1, a=5, b=31, h=3),     # A=11, K=8,  C(31,5)=169911
    dict(n=32, m=2, g=1, a=5, b=15, h=3),     # A=11, K=8,  C(15,5)=3003
]


def next_prime_1modn(x, n):
    c = x + (n - (x - 1) % n) % n
    if (c - 1) % n:
        c += n - (c - 1) % n
    while True:
        if core.is_prime(c):
            return c
        c += n


def run_shape(sh, seeds=3):
    n, m, g, a, b, h = sh["n"], sh["m"], sh["g"], sh["a"], sh["b"], sh["h"]
    A = g + m * a
    K = A - h
    assert m <= h < 2 * m and g + m * (a - 2) <= K - 1
    C = math.comb(b, a)
    Js = list(combinations(range(b), a))
    assert len(Js) == C
    rows = []
    # target nu values -> q  (q = nu*C/(a*(b-a)))
    for nu_t in (0.05, 0.3, 1.0, 3.0, 8.0, 30.0):
        qq = max(int(nu_t * C / (a * (b - a))), n + 1)
        q = next_prime_1modn(qq, n)
        w = core.root_of_unity(q, n)
        lab = [pow(w, m * j, q) for j in range(b)]
        # slopes
        byz = {}
        for J in Js:
            z = sum(lab[j] for j in J) % q
            byz.setdefault(z, []).append(J)
        nslopes = len(byz)
        nu = a * (b - a) * nslopes / C

        def gamma_lo_of(sel):
            """sel: list of label sets, one per slope.  A member is in
            Gamma_lo iff no OTHER selected member is adjacent to it."""
            idx = {}
            for J in sel:
                for T in combinations(J, a - 1):
                    idx.setdefault(T, 0)
                    idx[T] += 1
            lo = 0
            for J in sel:
                if all(idx[T] == 1 for T in combinations(J, a - 1)):
                    lo += 1
            return lo

        lex = [min(v) for v in byz.values()]
        lo_lex = gamma_lo_of(lex)
        colex = [max(v) for v in byz.values()]
        lo_colex = gamma_lo_of(colex)
        rnds = []
        for s in range(seeds):
            rng = random.Random(1000 + s)
            rnds.append(gamma_lo_of([rng.choice(v) for v in byz.values()]))
        rows.append(dict(q=q, nu_target=nu_t, nu=nu, slopes=nslopes,
                         candidates=C, per_slope=C / nslopes,
                         gamma_lo_lex=lo_lex, gamma_lo_colex=lo_colex,
                         gamma_lo_uniform=rnds,
                         gamma_lo_uniform_mean=sum(rnds) / len(rnds),
                         predicted_uniform=nslopes * math.exp(-nu),
                         budget_8n3=8 * n ** 3))
        print(f"   q={q:<8d} nu={nu:7.3f} slopes={nslopes:<7d} "
              f"cand/slope={C/nslopes:9.2f} | Gamma_lo: lex={lo_lex:<7d} "
              f"colex={lo_colex:<7d} uniform={sum(rnds)/len(rnds):9.1f} "
              f"(pred {nslopes*math.exp(-nu):9.1f})")
    return dict(shape=dict(n=n, m=m, g=g, a=a, b=b, h=h, A=A, K=K, C=C),
                rows=rows)


if __name__ == "__main__":
    out = []
    for sh in SHAPES:
        A = sh["g"] + sh["m"] * sh["a"]
        print(f"[shape n={sh['n']} m={sh['m']} g={sh['g']} a={sh['a']} "
              f"b={sh['b']} A={A} K={A-sh['h']} C={math.comb(sh['b'],sh['a'])}]")
        out.append(run_shape(sh))
    p = os.path.join(HERE, "EXPD.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(f"-> {p}")
