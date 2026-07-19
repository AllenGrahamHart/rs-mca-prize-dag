#!/usr/bin/env python3
"""F5 P7-V (Modal): machine-check the P7.1 REDUCTION LEMMA bijection.

Same construction as E3 (seeds shared), but counted on the OTHER side of
the bijection: enumerate all completely-split-over-D' monic polynomials
of degree k-1 (i.e. all root sets Z), and test membership in the
codim-(t-1) subspace V_T = eval_T^{-1}(span(du|_T, dv|_T)) by a 3x(t+1)
rank condition — NO slope solving, NO gamma. The lemma predicts:

    #split-in-V_T (with [c'|_T] != [dv|_T], the z = infinity direction,
    and c'|_T != 0)  ==  E3's hit count (same trial seeds), before the
    validity filter; and == E3's valid hits after it.

Any mismatch refutes the reduction as stated."""
import itertools
import json
import random

import modal

app = modal.App("rs-mca-f5-p7v")
image = modal.Image.debian_slim()

ROWS = [(24, 73, 5, 7001), (24, 193, 5, 7002)]   # E3 seeds reused


@app.function(image=image, cpu=2, memory=2048, timeout=280)
def check(row):
    n, q, n_trials, seed = row
    rng = random.Random(seed)
    k, t = n // 2, 3
    A = k + t
    sT = t + 1

    def inv(a):
        return pow(a % q, q - 2, q)

    def _f(x):
        out, d = [], 2
        while d * d <= x:
            while x % d == 0:
                out.append(d); x //= d
            d += 1
        if x > 1:
            out.append(x)
        return out

    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // r, q) != 1 for r in set(_f(q - 1))))
    h = pow(g, (q - 1) // n, q)
    D = sorted(pow(h, i, q) for i in range(n))

    def ev(cf, x):
        acc = 0
        for c in reversed(cf):
            acc = (acc * x + c) % q
        return acc

    def interp_coeffs(pts, vals):
        m = len(pts)
        coeffs = [0] * m
        for i, (xi, yi) in enumerate(zip(pts, vals)):
            num = [1]; den = 1
            for j, xj in enumerate(pts):
                if j == i:
                    continue
                new = [0] * (len(num) + 1)
                for d2, cc in enumerate(num):
                    new[d2] = (new[d2] - cc * xj) % q
                    new[d2 + 1] = (new[d2 + 1] + cc) % q
                num = new
                den = den * (xi - xj) % q
            w = yi * inv(den) % q
            for d2, cc in enumerate(num):
                coeffs[d2] = (coeffs[d2] + cc * w) % q
        return coeffs

    out = []
    for _ in range(n_trials):
        # identical draw order to E3
        c0 = [rng.randrange(q) for _ in range(k)]
        w0 = [rng.randrange(q) for _ in range(k)]
        z0 = rng.randrange(q)
        T = sorted(rng.sample(D, sT))
        Tset = set(T)
        unpert = [x for x in D if x not in Tset]
        du = {x: rng.randrange(1, q) for x in T}
        dv = {x: rng.randrange(1, q) for x in T}
        v = {x: (ev(w0, x) + dv.get(x, 0)) % q for x in D}
        n_inV = 0
        n_valid = 0
        for Z in itertools.combinations(unpert, A - sT):
            # c' = ell_Z; values at T
            lz = []
            for x in T:
                val = 1
                for zt in Z:
                    val = val * (x - zt) % q
                lz.append(val)
            # rank([lz; du; dv]) <= 2 with lz not in span(dv) alone
            # solve alpha*du + beta*dv = lz? (2 unknowns, 4 eqs)
            x0, x1 = 0, 1
            det = (du[T[x0]] * dv[T[x1]] - du[T[x1]] * dv[T[x0]]) % q
            if det == 0:
                continue
            alpha = (lz[x0] * dv[T[x1]] - lz[x1] * dv[T[x0]]) % q * inv(det) % q
            beta = (du[T[x0]] * lz[x1] - du[T[x1]] * lz[x0]) % q * inv(det) % q
            if all((alpha * du[T[i]] + beta * dv[T[i]] - lz[i]) % q == 0
                   for i in range(2, sT)):
                if alpha == 0:      # [c'|_T] = [dv]: z = infinity direction
                    continue
                n_inV += 1
                S = sorted(set(Z) | Tset)
                vc = interp_coeffs(S, [v[x] for x in S])
                if any(vc[d2] % q for d2 in range(k, A)):
                    n_valid += 1
        out.append({"split_in_V": n_inV, "valid": n_valid})
    return {"n": n, "q": q, "trials": out}


@app.local_entrypoint()
def main():
    res = list(check.map(ROWS, return_exceptions=True))
    print("E3 reference hits: (24,73): [27,25,29,33,37]  (24,193): [2,4,5,4,7]")
    for r in res:
        if not isinstance(r, dict):
            print("worker error:", str(r)[:140]); continue
        print(f"  ({r['n']},{r['q']}) c'-side counts: "
              f"in-V = {[tr['split_in_V'] for tr in r['trials']]}, "
              f"valid = {[tr['valid'] for tr in r['trials']]}")
    with open("/tmp/f5_p7v.json", "w") as f:
        json.dump([r for r in res if isinstance(r, dict)], f, indent=1)
