#!/usr/bin/env python3
"""F2 campaign L3/M1 calibration (Modal): exact census moments at the
calibration rows — the pre-registered M1 experiment (F2_L3_DESIGN.md).

Per cell (q, n, b): exact integer DP gives the FULL census
{N_b(s)}_{s in F_q^2}. Report M_k = sum_s N(s)^k for k = 1,2,3,4,
the flat-model predictions (multinomial: M_2 ~ mean*M_1 + M_1 with
mean = C(n,b)/q^2), the 0-fiber N(0) and its share of M_2, and the
max fiber. PRE-REGISTERED READ (immutable): M1 is VIABLE at this
scale if, in sub-balance cells, the moment ratios M_2/M_1 and the max
fiber are O(1) (census near-flat in L^2/L^4 away from the structured
value 0) AND the 0-fiber is exactly the structured (coset-union +
known-accident) count — i.e. the ladder's obligation is confined to
s = 0. M1 is DEAD at this scale if sub-balance cells show heavy
NON-ZERO fibers (max fiber >> 1 at generic s), which no 0-specialness
argument could price. Any DP/assertion failure refutes the packet.
"""
import json
from math import comb

import modal

app = modal.App("rs-mca-f2-l3-m1")
image = modal.Image.debian_slim()

CELLS = [(97, 32, 3), (97, 32, 4), (97, 32, 5), (97, 32, 6),
         (193, 32, 4), (193, 32, 6), (257, 32, 4), (257, 32, 6),
         (97, 16, 4), (97, 16, 6)]


@app.function(image=image, cpu=2, memory=3072, timeout=280)
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
    dp = {(0, 0): [1] + [0] * b}
    for x in D:
        x2 = x * x % q
        new = {}
        for (a1, a2), vec in dp.items():
            tgt = new.setdefault((a1, a2), [0] * (b + 1))
            for w in range(b + 1):
                tgt[w] += vec[w]
            k1, k2 = (a1 + x) % q, (a2 + x2) % q
            t2 = new.setdefault((k1, k2), [0] * (b + 1))
            for w in range(b):
                if vec[w]:
                    t2[w + 1] += vec[w]
        dp = new
    N = {s: vec[b] for s, vec in dp.items() if vec[b]}
    M1 = sum(N.values())
    assert M1 == comb(n, b)
    M2 = sum(v * v for v in N.values())
    M3 = sum(v ** 3 for v in N.values())
    M4 = sum(v ** 4 for v in N.values())
    N0 = N.get((0, 0), 0)
    mx = max(N.values())
    # argmax fiber and whether the max is at 0
    argmax_at_0 = (N0 == mx)
    mean = M1 / q ** 2
    flat_M2 = M1 * (1 + mean)          # Poisson-ish flat prediction
    return {"q": q, "n": n, "b": b, "W_mean": round(mean, 4),
            "N0": N0, "max_fiber": mx, "argmax_at_0": argmax_at_0,
            "M2_over_flat": round(M2 / flat_M2, 3),
            "M2": M2, "M3": M3, "M4": M4,
            "N0sq_share_of_M2": round(N0 * N0 / M2, 4) if M2 else 0}


@app.local_entrypoint()
def main():
    res = list(cell.map(CELLS, return_exceptions=True))
    fails = 0
    rows = []
    print(f"{'cell':>14} {'mean':>8} {'N0':>6} {'maxN':>6} {'at0':>5} "
          f"{'M2/flat':>8} {'N0^2/M2':>8}")
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:200])
            continue
        rows.append(r)
        print(f"  ({r['q']},{r['n']},b={r['b']})".rjust(14) +
              f" {r['W_mean']:>8} {r['N0']:>6} {r['max_fiber']:>6} "
              f"{str(r['argmax_at_0']):>5} {r['M2_over_flat']:>8} "
              f"{r['N0sq_share_of_M2']:>8}")
    with open("/tmp/f2_l3_m1.json", "w") as f:
        json.dump(rows, f, indent=1)
    if fails:
        raise SystemExit(f"F2_L3_M1_CALIBRATION_FAIL ({fails})")
    print("\nF2_L3_M1_CALIBRATION_PASS")
