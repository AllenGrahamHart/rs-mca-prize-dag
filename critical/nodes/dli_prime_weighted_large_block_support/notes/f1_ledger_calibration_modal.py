#!/usr/bin/env python3
"""FALSIFICATION ROUND F1 (Modal): calibrate the ledger-conditioned re-pose C1'.

C1-as-frozen (uniform K <= 3.34 x iid) is REFUTED by the natural cluster
rows (K up to 23 at j=20). The candidate re-pose C1' says the excess
near-peak MASS is explained by the row's exhibited low-weight vanisher
ledger:

    Sum_{lambda != 0} T(lambda)  <=  K' * r * (1 + W_cl(row)),
    W_cl(row) = sum over primitive vanisher ORBITS (weights L+1..w_max,
                all orbits — clusters/shadows/additive members included
                at their own weights) of 2N * 2^-w.

This job: for each of the four measured rows, enumerate ALL primitive
vanisher orbits up to weight 7 at the pinned embedding (sharded by weight
across Modal workers), compute W_cl, and compare K'_measured =
(E - 1) / (r * (1 + W_cl)) using the exact E from the local dyadic scans.
If K' lands in [0.5, 4] across rows, C1' is calibrated; if the excess
exceeds the ledger by orders of magnitude, C1' is ALSO dead and the core
needs re-thinking.

Every shard: one (row, weight) pair; w = 7 is the largest at
C(32,7)*2^6 = 2.15e8 sign-evals ~ 30 s with chunked numpy.
"""
import json
import math

import modal

app = modal.App("dli-f1-ledger")
image = modal.Image.debian_slim().pip_install("numpy")

ROWS = {
    204353: {"E": 1.01039744},
    110849: {"E": 1.00040196},
    100609: {"E": 1.00031445},
    65089:  {"E": None},  # computed in-shard below (cheap) if needed
}
NP, N = 64, 32
WEIGHTS = [3, 4, 5, 6, 7]


def spr_omega(q, nprime):
    n = q - 1
    fs = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            fs.add(d)
            n //= d
        d += 1
    if n > 1:
        fs.add(n)
    g = 2
    while any(pow(g, (q - 1) // p, q) == 1 for p in fs):
        g += 1
    return pow(g, (q - 1) // nprime, q)


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def count_orbits(payload):
    """Count primitive vanisher orbits of one weight at one row."""
    import itertools
    import numpy as np
    q, w = payload
    omega = spr_omega(q, NP)
    powers = np.array([pow(omega, e, q) for e in range(N)], dtype=np.int64)
    combos = np.fromiter(itertools.chain.from_iterable(
        itertools.combinations(range(N), w)), dtype=np.int64).reshape(-1, w)
    # sign patterns, first sign +1
    signs = np.array(list(itertools.product((1, -1), repeat=w - 1)))
    signs = np.hstack([np.ones((signs.shape[0], 1), dtype=np.int64), signs])
    orbit_reps = set()
    CH = 200_000
    for lo in range(0, len(combos), CH):
        cc = combos[lo:lo + CH]
        vals = powers[cc]                          # (chunk, w)
        tot = vals @ signs.T % q                   # (chunk, nsigns)
        hits = np.argwhere(tot == 0)
        for ci, si in hits:
            sup = tuple(int(x) for x in cc[ci])
            sgn = tuple(int(x) for x in signs[si])
            # primitivity: no proper subsum vanishes
            items = [(e, s) for e, s in zip(sup, sgn)]
            prim = True
            for mask in range(1, (1 << w) - 1):
                sub = sum(s * pow(omega, e, q)
                          for k, (e, s) in enumerate(items) if (mask >> k) & 1) % q
                if sub == 0:
                    prim = False
                    break
            if not prim:
                continue
            # signed-shift orbit key
            best = None
            vec = [0] * N
            for e, s in items:
                vec[e] = s
            for sh in range(2 * N):
                out = [0] * N
                for e, c in enumerate(vec):
                    if c:
                        ee = (e + sh) % (2 * N)
                        if ee >= N:
                            out[ee - N] -= c
                        else:
                            out[ee] += c
                t = tuple(out)
                if best is None or t < best:
                    best = t
            orbit_reps.add(best)
    return {"q": q, "w": w, "orbits": len(orbit_reps)}


@app.local_entrypoint()
def main():
    payloads = [(q, w) for q in ROWS for w in WEIGHTS]
    results = list(count_orbits.map(payloads, return_exceptions=True))
    table = {}
    for r in results:
        if isinstance(r, dict):
            table.setdefault(r["q"], {})[r["w"]] = r["orbits"]
        else:
            print("SHARD ERROR:", r)
    print(json.dumps(table, indent=1))
    for q, wcounts in sorted(table.items()):
        W_cl = sum(cnt * 2 * N * 2.0 ** -w for w, cnt in wcounts.items())
        r = q / 2.0 ** N
        E = ROWS[q]["E"]
        if E is None:
            continue
        excess = E - 1.0
        ledger = r * (1.0 + W_cl)
        print(f"q={q}: orbits by w: {wcounts}  W_cl={W_cl:.2f}  "
              f"r={r:.3e}  excess={excess:.5f}  r(1+W_cl)={ledger:.5f}  "
              f"K'={excess/ledger:.2f}")
    with open("/tmp/f1_ledger.json", "w") as f:
        json.dump(table, f)
