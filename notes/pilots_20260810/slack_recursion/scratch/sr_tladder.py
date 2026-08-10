#!/usr/bin/env python3
"""sr_tladder: the two supply families at general t, EXACT, by direct
enumeration of all a-subsets A of mu_n (a = k+t).

 SLACK0(n,t)  = max over (v_1..v_t) of #{A : e_i(A) = v_i, i = 1..t}
                (the slack-0 / plateau family: Y of degree exactly a)
 PRODW(n,t)   = max over (p, v_1..v_{t-1}) of
                #{A : prod_{x in A} x = p, e_i(A) = v_i, i = 1..t-1}
                (the maximal-slack PRODUCT WORD family
                 Y = x^{-1} + sum_{i<t} c_i x^{a-1-i})

Both families have all agreements EXACTLY a (single-swap argument), so both
counts are F_LIST = F_SUBSET exactly.
"""
import json, sys, math
from itertools import combinations
from math import comb


def find_gen(q, n):
    co = (q - 1) // n
    for g0 in range(2, 100000):
        g = pow(g0, co, q)
        if pow(g, n // 2, q) != 1 and pow(g, n, q) == 1:
            if len({pow(g, i, q) for i in range(n)}) == n:
                return g
    raise RuntimeError


def run(n, q, tmax, out=None):
    k = n // 2
    g = find_gen(q, n)
    D = [pow(g, i, q) for i in range(n)]
    res = []
    for t in range(1, tmax + 1):
        a = k + t
        if a > n - 1:
            break
        c0 = {}
        c1 = {}
        for A in combinations(range(n), a):
            e = [1]
            for i in A:
                x = D[i]
                ne = e + [0]
                for j in range(len(e) - 1, -1, -1):
                    ne[j + 1] = (ne[j + 1] + e[j] * x) % q
                e = ne
            ks0 = tuple(e[j] for j in range(1, t + 1))
            c0[ks0] = c0.get(ks0, 0) + 1
            ks1 = tuple([e[a]] + [e[j] for j in range(1, t)])
            c1[ks1] = c1.get(ks1, 0) + 1
        s0 = max(c0.values())
        p0 = max(c1.values())
        row = dict(n=n, q=q, t=t, a=a, n_subsets=comb(n, a),
                   SLACK0=s0, PRODW=p0,
                   SLACK0_classes=len(c0), PRODW_classes=len(c1),
                   ratio_prod_over_slack0=p0 / s0,
                   bits=math.log2(p0 / s0))
        res.append(row)
        print(json.dumps(row), flush=True)
        if out:
            with open(out, "w") as f:
                json.dump(res, f, indent=1)
    return res


if __name__ == "__main__":
    run(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]),
        sys.argv[4] if len(sys.argv) > 4 else None)
