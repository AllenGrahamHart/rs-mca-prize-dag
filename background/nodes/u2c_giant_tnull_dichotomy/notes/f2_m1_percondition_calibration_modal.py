#!/usr/bin/env python3
"""F2 campaign M1 per-condition calibration (Modal): MEASUREMENT ONLY
(no claims banked from this run — data for the session-2 lemma).

Object: N^(j)_b(0) = #{S in mu_n, |S| = b : p_1(S) = ... = p_j(S) = 0}
by exact integer DP over F_q^j states. Observed per-condition loss

    L_obs(j) = N^(j)(0) * q / N^(j-1)(0)     (flat contraction = 1),

at mid-band b = n/2, for j = 1..J (J limited by q^J state space).
The lemma target says: L <= ~2^15 per condition wins the floor.

PRE-REGISTERED READ (immutable): L_obs(j) <= 32 across all rows and j
(where N^(j-1) > 0) = VIABLE datum; localized blowups map where
structured (coset) mass enters the condition ladder; N^(j)(0) = 0
rows terminate their ladder (report). Frobenius discipline (catch #6):
skip j divisible by q (redundant conditions, L_obs = q trivially).
Gates: N^(0)(0) = C(n, b); DP total = C(n, b) at every level.
"""
import json
from math import comb

import modal

app = modal.App("rs-mca-f2-m1-percond")
image = modal.Image.debian_slim()

# (q, n, J): J = max conditions; q^J DP states must stay < ~3e6
ROWS = [(17, 16, 5), (31, 30, 4), (61, 30, 3), (97, 32, 3),
        (193, 32, 2), (113, 16, 3), (257, 16, 3)]


@app.function(image=image, cpu=2, memory=3072, timeout=280)
def row(job):
    q, n, J = job
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
    b = n // 2
    counts = [comb(n, b)]     # j = 0
    for j in range(1, J + 1):
        # DP over (p_1..p_j) states
        dp = {(0,) * j: [1] + [0] * b}
        for x in D:
            pw = [pow(x, e, q) for e in range(1, j + 1)]
            new = {}
            for st, vec in dp.items():
                t = new.setdefault(st, [0] * (b + 1))
                for w in range(b + 1):
                    t[w] += vec[w]
                st2 = tuple((st[e] + pw[e]) % q for e in range(j))
                t2 = new.setdefault(st2, [0] * (b + 1))
                for w in range(b):
                    if vec[w]:
                        t2[w + 1] += vec[w]
            dp = new
        total = sum(v[b] for v in dp.values())
        assert total == comb(n, b), ("DP total gate", j)
        counts.append(dp.get((0,) * j, [0] * (b + 1))[b])
    ratios = []
    for j in range(1, J + 1):
        if counts[j - 1] > 0:
            ratios.append(round(counts[j] * q / counts[j - 1], 3))
        else:
            ratios.append(None)
    return {"q": q, "n": n, "b": b, "counts": counts, "L_obs": ratios}


@app.local_entrypoint()
def main():
    res = list(row.map(ROWS, return_exceptions=True))
    fails = 0
    print(f"{'row':>12} {'b':>4}  N^(0..J)(0)  ->  L_obs per condition")
    viable = True
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:200])
            continue
        print(f"  ({r['q']},{r['n']})".rjust(12) + f" {r['b']:>4}  "
              f"{r['counts']}  ->  {r['L_obs']}")
        for L in r["L_obs"]:
            if L is not None and L > 32:
                viable = False
    if fails:
        raise SystemExit(f"F2_M1_PERCOND_CALIBRATION_FAIL ({fails})")
    print(f"\npre-registered read: all L_obs <= 32: {viable}")
    print("F2_M1_PERCOND_CALIBRATION_PASS")
