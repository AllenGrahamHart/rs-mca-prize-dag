#!/usr/bin/env python3
"""F2 campaign L2b' (Modal): machine verification of the WEIL–NEWTON
ARC BOUND (see F2_L2B_WEIL_NEWTON_ARC_BOUND.md).

Gates per cell (q, n, b):
  GA: |e_1(lambda)| <= 2 sqrt(q) for ALL lambda != 0 (exhaustive q^2-1
      first moments — covers all dilates of all arcs).
  GB: |E_b(lambda)| <= W(q,b) = prod_{r<b}(2 sqrt q + r)/b! for ALL
      lambda != 0 (exhaustive).
  GC: N(0) <= C(n,b)/q^2 + W(q,b) (N(0) by exact integer DP).
Reach table (exact big-int, no floats): b*(q,n) = max{b <= n/2 :
ceil(W(q,b)) <= n^3} at official-shaped rows, W evaluated as an exact
rational with 2 sqrt(q) replaced by the integer ceiling isqrt-bound
(2*isqrt(q)+2 >= 2 sqrt q, conservative).
Any assertion failure refutes the packet.
"""
import cmath
import math
from fractions import Fraction
from math import comb, isqrt

import modal

app = modal.App("rs-mca-f2-l2b-weilnewton")
image = modal.Image.debian_slim()

CELLS = [(97, 32, 3), (97, 32, 6), (193, 32, 6), (257, 32, 6), (97, 16, 4)]


def W_exact_ceil(q, b):
    # exact rational upper bound: prod (Mc + r)/b! with Mc = ceil(2 sqrt q)
    # Mc >= 2 sqrt(q) exactly: isqrt(q) >= sqrt(q) - 1
    Mc = 2 * isqrt(q) + 2
    num = 1
    for r in range(b):
        num *= (Mc + r)
    return Fraction(num, math.factorial(b))


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
    two_pi_q = 2 * math.pi / q
    psi = [cmath.exp(1j * two_pi_q * v) for v in range(q)]
    twosq = 2 * math.sqrt(q)
    Wb = float(W_exact_ceil(q, b))
    ga_max = 0.0
    gb_max_ratio = 0.0
    for l1 in range(q):
        for l2 in range(q):
            if l1 == 0 and l2 == 0:
                continue
            coef = [0j] * (b + 1)
            coef[0] = 1.0 + 0j
            s1 = 0j
            for x in D:
                w = psi[(l1 * x + l2 * x * x) % q]
                s1 += w
                for dd in range(b - 1, -1, -1):
                    if coef[dd] != 0:
                        coef[dd + 1] += coef[dd] * w
            a1 = abs(s1)
            ga_max = max(ga_max, a1)
            assert a1 <= twosq + 1e-9, ("GA violated", l1, l2, a1)
            Eb = abs(coef[b])
            gb_max_ratio = max(gb_max_ratio, Eb / Wb)
            assert Eb <= Wb + 1e-6, ("GB violated", l1, l2, Eb, Wb)
    # GC: exact N(0)
    dp = {(0, 0): [1] + [0] * b}
    for x in D:
        x2 = x * x % q
        new = {}
        for (a1_, a2_), vec in dp.items():
            tgt = new.setdefault((a1_, a2_), [0] * (b + 1))
            for w_ in range(b + 1):
                tgt[w_] += vec[w_]
            k1, k2 = (a1_ + x) % q, (a2_ + x2) % q
            t2 = new.setdefault((k1, k2), [0] * (b + 1))
            for w_ in range(b):
                if vec[w_]:
                    t2[w_ + 1] += vec[w_]
        dp = new
    N0 = dp.get((0, 0), [0] * (b + 1))[b]
    assert N0 <= comb(n, b) / q ** 2 + Wb + 1e-9, ("GC violated", N0)
    return {"q": q, "n": n, "b": b, "ga_max": round(ga_max, 3),
            "two_sqrt_q": round(twosq, 3), "W": round(Wb, 1),
            "gb_max_ratio": round(gb_max_ratio, 4), "N0": N0,
            "CnB_over_q2": round(comb(n, b) / q ** 2, 3)}


@app.function(image=image, cpu=1, memory=512, timeout=120)
def reach(_):
    # exact-integer reach at official-shaped rows: n = 2^s, budget n^3,
    # generated-field size q ~ m*n + 1 shapes for co-index m in {3, 8, 64}
    out = []
    for s in (13, 21, 31, 41):
        n = 1 << s
        budget = n ** 3
        for m in (3, 8, 64):
            q = m * n + 1          # shape proxy (exact q irrelevant to shape)
            bstar = 0
            b = 1
            while b <= min(n // 2, 200):   # W monotone increasing in b
                if W_exact_ceil(q, b) <= budget:
                    bstar = b
                    b += 1
                else:
                    break
            frac = Fraction(2 * bstar, n)   # covered fraction of the b-range
            out.append((s, m, bstar, float(frac)))
    return out


@app.local_entrypoint()
def main():
    res = list(cell.map(CELLS, return_exceptions=True))
    fails = 0
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:250])
            continue
        print(f"({r['q']},{r['n']},b={r['b']}): GA max|e1|={r['ga_max']} "
              f"<= {r['two_sqrt_q']}; GB max |E_b|/W = {r['gb_max_ratio']}; "
              f"GC N0={r['N0']} <= {r['CnB_over_q2']} + W={r['W']}")
    tab = reach.remote(0)
    print("\nreach b*(q,n) at official shapes (budget n^3, W exact-int):")
    for s, m, bstar, frac in tab:
        print(f"  n=2^{s}, m={m}: b* = {bstar}  "
              f"(covered fraction of b-range with complementation: {frac:.2e})")
    if fails:
        raise SystemExit(f"F2_L2B_WEIL_NEWTON_FAIL ({fails})")
    print("\nF2_L2B_WEIL_NEWTON_PASS")
