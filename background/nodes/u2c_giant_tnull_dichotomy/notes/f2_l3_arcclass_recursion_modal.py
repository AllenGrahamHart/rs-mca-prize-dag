#!/usr/bin/env python3
"""F2 campaign L3 (Modal): verification of the ARC-CLASS RECURSION
LEMMA (see F2_L3_ARCCLASS_RECURSION.md).

Gates per cell (q, n, b), all exact (< 1e-6 float-vs-integer):
  R1: (1/q^2) sum_{l1} E_b((l1,0)) = N^{p1}(0)/q
  R2: (1/q^2) sum_{l2} E_b((0,l2)) = N^{p2}(0)/q
  R3: (1/q^2) sum_lambda E_b = N^{(2)}(0)
  R4: the four-term regrouping reproduces N^{(2)}(0) exactly.
Integer censuses by DP; arc sums by the product-poly DP.
"""
import cmath
import math
from math import comb

import modal

app = modal.App("rs-mca-f2-l3-recursion")
image = modal.Image.debian_slim()

CELLS = [(97, 32, 4), (97, 32, 6), (193, 32, 6), (257, 32, 5),
         (97, 16, 4), (97, 16, 6)]


@app.function(image=image, cpu=2, memory=2048, timeout=280)
def cell(job):
    q, n, b = job
    def pf(x):
        out, d = [], 2
        while d * d <= x:
            while x % d == 0:
                out.append(d); x //= d
            d += 1
        if x > 1:
            out.append(x)
        return out
    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // r, q) != 1 for r in set(pf(q - 1))))
    h = pow(g, (q - 1) // n, q)
    D = sorted(pow(h, i, q) for i in range(n))

    # exact censuses by 1D / 2D DP
    def census1(power):
        dp = {0: [1] + [0] * b}
        for x in D:
            xv = pow(x, power, q)
            new = {}
            for a, vec in dp.items():
                t = new.setdefault(a, [0] * (b + 1))
                for w in range(b + 1):
                    t[w] += vec[w]
                k = (a + xv) % q
                t2 = new.setdefault(k, [0] * (b + 1))
                for w in range(b):
                    if vec[w]:
                        t2[w + 1] += vec[w]
            dp = new
        return dp.get(0, [0] * (b + 1))[b]
    Np1 = census1(1)
    Np2 = census1(2)
    dp = {(0, 0): [1] + [0] * b}
    for x in D:
        x2 = x * x % q
        new = {}
        for (a1, a2), vec in dp.items():
            t = new.setdefault((a1, a2), [0] * (b + 1))
            for w in range(b + 1):
                t[w] += vec[w]
            k1, k2 = (a1 + x) % q, (a2 + x2) % q
            t2 = new.setdefault((k1, k2), [0] * (b + 1))
            for w in range(b):
                if vec[w]:
                    t2[w + 1] += vec[w]
        dp = new
    N2 = dp.get((0, 0), [0] * (b + 1))[b]

    # arc sums
    two_pi_q = 2 * math.pi / q
    psi = [cmath.exp(1j * two_pi_q * v) for v in range(q)]
    def Eb(l1, l2):
        coef = [0j] * (b + 1)
        coef[0] = 1.0 + 0j
        for x in D:
            w = psi[(l1 * x + l2 * x * x) % q]
            for dd in range(b - 1, -1, -1):
                if coef[dd] != 0:
                    coef[dd + 1] += coef[dd] * w
        return coef[b]
    lin = sum(Eb(l1, 0) for l1 in range(q))
    quo = sum(Eb(0, l2) for l2 in range(q))
    gen = 0j
    for l1 in range(1, q):
        for l2 in range(1, q):
            gen += Eb(l1, l2)
    q2 = q * q
    r1 = lin.real / q2
    r2 = quo.real / q2
    tot = (lin + quo - comb(n, b) + gen).real / q2   # lambda=0 in both classes
    assert abs(lin.imag) / q2 < 1e-6 and abs(quo.imag) / q2 < 1e-6
    assert abs(r1 - Np1 / q) < 1e-6, ("R1", r1, Np1 / q)
    assert abs(r2 - Np2 / q) < 1e-6, ("R2", r2, Np2 / q)
    assert abs(tot - N2) < 1e-6, ("R3", tot, N2)
    # R4 regrouping
    mean = comb(n, b) / q2
    regroup = mean + (Np1 / q - mean) + (Np2 / q - mean) + gen.real / q2
    assert abs(regroup - N2) < 1e-6, ("R4", regroup, N2)
    return {"q": q, "n": n, "b": b, "Np1": Np1, "Np2": Np2, "N2": N2,
            "generic_mass": round(gen.real / q2, 6),
            "mean": round(mean, 4)}


@app.local_entrypoint()
def main():
    res = list(cell.map(CELLS, return_exceptions=True))
    fails = 0
    print(f"{'cell':>14} {'Np1':>7} {'Np2':>7} {'N2':>6} {'mean':>9} "
          f"{'generic mass':>13}")
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:200])
            continue
        print(f"  ({r['q']},{r['n']},b={r['b']})".rjust(14) +
              f" {r['Np1']:>7} {r['Np2']:>7} {r['N2']:>6} "
              f"{r['mean']:>9} {r['generic_mass']:>13}")
    if fails:
        raise SystemExit(f"F2_L3_ARCCLASS_RECURSION_FAIL ({fails})")
    print("\nF2_L3_ARCCLASS_RECURSION_PASS")
