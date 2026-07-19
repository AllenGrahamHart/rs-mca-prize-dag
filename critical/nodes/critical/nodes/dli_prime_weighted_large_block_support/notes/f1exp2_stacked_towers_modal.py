#!/usr/bin/env python3
"""F1-exp2 (floor campaign, Modal): engineered stacked towers vs the
lift-aware ledger — second attack family on the dli B-WEAK floor.

MECHANISM UNDER TEST: one engineered norm-coincidence at level n'=32
(q | N(P), P weight-5) automatically structures level n'=64 through the
PROVED lift identity (e -> 2e maps vanishers identically). B-WEAK's
transported arithmetic prices the lift shadow ONCE at its weights with
per-level r-dilution. ATTACK: engineer many such q, measure EXACT per-level
costs E32(q), E64(q) (full D3 lambda-sums), and compare the measured JOINT
cost log2 E32 + log2 E64 against the lift-aware ledger prediction
  E_level <= 1 + r_level * W_cl(level)   (r = q / 2^{n'/2}),
with W_cl computed from the ACTUAL enumerated vanisher orbits at each
level (census machinery, weights <= 7). PRE-REGISTERED: alarm = measured
joint cost exceeding the ledger prediction by > 2x (in excess mass) at a
SUSTAINED fraction of engineered rows (not single Poisson accidents);
matching costs = survival +1 for the engineered-stacking family.

Per-q Modal job: engineer (factor a weight-5 norm), enumerate vanisher
orbits at n'=32 and n'=64 (w <= 7, MITM-free direct: C(16,w), C(32,w)
windows are small), compute exact E at both levels, ledger comparison.
"""
import json
import math
import random
from pathlib import Path

import modal

app = modal.App("rs-mca-f1exp2-stacked")
image = modal.Image.debian_slim().pip_install("numpy")

N_TRIALS = 120


@app.function(image=image, cpu=2, memory=3072, timeout=60)
def stacked_trial(seed):
    import itertools
    import numpy as np
    from fractions import Fraction
    rng = random.Random(seed)

    def resultant(f, g):
        f = [Fraction(c) for c in f]
        g = [Fraction(c) for c in g]
        def deg(p):
            d = len(p) - 1
            while d >= 0 and p[d] == 0:
                d -= 1
            return d
        res = Fraction(1)
        F, G = f, g
        while True:
            dF, dG = deg(F), deg(G)
            if dG < 0:
                return 0
            if dG == 0:
                return res * G[0] ** dF
            R = F[:]
            while deg(R) >= dG:
                dR = deg(R)
                c = R[dR] / G[dG]
                for i in range(dG + 1):
                    R[dR - dG + i] -= c * G[i]
            dR = deg(R)
            res *= G[dG] ** (dF - max(dR, 0)) * (-1) ** (dF * dG)
            if dR < 0:
                return 0
            F, G = G, R[:dR + 1]

    def is_prime(m):
        if m < 2 or m % 2 == 0:
            return m == 2
        d, s = m - 1, 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            if a % m == 0:
                continue
            x = pow(a, d, m)
            if x in (1, m - 1):
                continue
            for _ in range(s - 1):
                x = x * x % m
                if x == m - 1:
                    break
            else:
                return False
        return True

    def factor_small(n, cap=10**6):
        out = []
        d = 2
        while d * d <= n and d < cap:
            while n % d == 0:
                out.append(d)
                n //= d
            d += 1
        if n > 1 and (n < cap**2) and is_prime(n):
            out.append(n)
        return out

    # 1. engineer: weight-5 ternary at n'=32 (N=16), admissible q ≡ 1 mod 64
    N16 = 16
    sup = tuple(sorted(rng.sample(range(N16), 5)))
    sgn = (1,) + tuple(rng.choice((1, -1)) for _ in range(4))
    poly = [0] * N16
    for e, s in zip(sup, sgn):
        poly[e] = s
    xN1 = [1] + [0] * (N16 - 1) + [1]
    norm = abs(int(resultant(xN1, poly)))
    if norm == 0:
        return {"skip": "zero norm"}
    qs = [p for p in set(factor_small(norm))
          if p % 64 == 1 and 20_000 <= p < 2_000_000]
    if not qs:
        return {"skip": "no admissible engineered q"}
    q = min(qs)

    def spr_omega(q, nprime):
        n0 = q - 1
        fs = set()
        d = 2
        while d * d <= n0:
            while n0 % d == 0:
                fs.add(d)
                n0 //= d
            d += 1
        if n0 > 1:
            fs.add(n0)
        g = 2
        while any(pow(g, (q - 1) // f, q) == 1 for f in fs):
            g += 1
        return pow(g, (q - 1) // nprime, q)

    def orbits_and_E(q, nprime, wmax=7):
        N = nprime // 2
        omega = spr_omega(q, nprime)
        pw = np.array([pow(omega, e, q) for e in range(N)], dtype=np.int64)
        # vanisher orbits (weights 3..wmax), primitive not enforced (mass ledger)
        W_cl = 0.0
        n_orb = 0
        for w in range(3, wmax + 1):
            combos = np.fromiter(itertools.chain.from_iterable(
                itertools.combinations(range(N), w)), dtype=np.int64).reshape(-1, w)
            signs = np.array(list(itertools.product((1, -1), repeat=w - 1)))
            signs = np.hstack([np.ones((signs.shape[0], 1), dtype=np.int64), signs])
            CH = 300_000
            cnt = 0
            for lo in range(0, len(combos), CH):
                vals = pw[combos[lo:lo + CH]]
                tot = vals @ signs.T % q
                cnt += int((tot == 0).sum())
            # each vanishing ELEMENT contributes 2^-w to W (elementwise ledger)
            W_cl += cnt * 2.0 ** -w
            n_orb += cnt
        # exact E via D3
        xs = pw
        E = 0.0
        lam = np.arange(q, dtype=np.int64)
        for lo in range(0, q, 40000):
            a = lam[lo:lo + 40000, None] * xs[None, :] % q
            E += float(np.exp(np.log(np.cos(np.pi * a / q) ** 2 + 1e-300)
                              .sum(axis=1)).sum())
        r = q / 2.0 ** N
        return {"E": E, "excess": E - 1.0, "r": r, "W_cl": W_cl,
                "ledger_excess": r * W_cl, "n_vanishing_elements": n_orb}

    lv32 = orbits_and_E(q, 32)
    lv64 = orbits_and_E(q, 64, wmax=6)
    joint_measured = (math.log2(max(lv32["E"], 1.0))
                      + math.log2(max(lv64["E"], 1.0)))
    joint_ledger = (math.log2(1.0 + 2 * lv32["ledger_excess"])
                    + math.log2(1.0 + 2 * lv64["ledger_excess"]))
    return {"q": q, "P_sup": list(sup), "P_sgn": list(sgn),
            "lv32": lv32, "lv64": lv64,
            "joint_measured_bits": joint_measured,
            "joint_ledger_bits_2x": joint_ledger,
            "alarm": joint_measured > max(2 * joint_ledger, 1e-4)}


@app.local_entrypoint()
def main():
    results = [r for r in stacked_trial.map(range(41, 41 + N_TRIALS),
                                            return_exceptions=True)
               if isinstance(r, dict)]
    rows = [r for r in results if "q" in r]
    print(f"{len(rows)} engineered stacked rows (of {len(results)} trials)")
    alarms = [r for r in rows if r["alarm"]]
    for r in sorted(rows, key=lambda r: -r["joint_measured_bits"])[:8]:
        print(f"q={r['q']:>8}: E32={r['lv32']['E']:.6f} E64={r['lv64']['E']:.6f} "
              f"joint={r['joint_measured_bits']:.5f}b ledger2x={r['joint_ledger_bits_2x']:.5f}b "
              f"{'ALARM' if r['alarm'] else ''}")
    print(f"alarms: {len(alarms)}/{len(rows)}")
    with open("/tmp/f1exp2_results.json", "w") as f:
        json.dump(results, f, indent=1)
