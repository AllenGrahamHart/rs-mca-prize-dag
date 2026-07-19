#!/usr/bin/env python3
"""F1-A3 (floor campaign, Modal): the dual-spectrum sweep — third attack
family on the dli B-WEAK floor.

B-WEAK's dual projection: the near-peak lambda-spectrum at admissible rows
must carry no structural surplus beyond the iid model + the priced primal
ledger (the round-S2 dyadic form). The S2 measurement was ONE row; this
family sweeps ~24 rows (n' = 64, q across [2e4, 2.4e5], natural + the
known cluster rows as positive-context) computing FULL exact dyadic
spectra #{lambda: T >= 2^-j} vs the iid model at every well-sampled level.
PRE-REGISTERED alarm: a row population (not single rows — the cluster rows
are KNOWN to inflate via their priced primal ledgers) with median
K(j) = obs/iid > 4 at well-sampled levels (iid-pred >= 20), sustained
across >= 3 q-scales; single-row cluster inflation classifies against the
primal ledger (F1's C1'-calibration machinery) and does NOT fire.
"""
import json
import math

import modal

app = modal.App("rs-mca-f1a3-dualspec")
image = modal.Image.debian_slim().pip_install("numpy")

NP = 64


@app.function(image=image, cpu=2, memory=3072, timeout=60)
def dual_spectrum(q):
    import numpy as np
    N = NP // 2
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
    omega = pow(g, (q - 1) // NP, q)
    xs = np.array([pow(omega, y, q) for y in range(N)], dtype=np.int64)
    counts = {}
    lam = np.arange(1, q, dtype=np.int64)
    lgs = []
    for lo in range(0, len(lam), 30000):
        a = lam[lo:lo + 30000, None] * xs[None, :] % q
        lgs.append(np.log2(np.cos(np.pi * a / q) ** 2 + 1e-300).sum(axis=1))
    lg = np.concatenate(lgs)
    for j in (16, 20, 24, 28, 32, 36, 40):
        counts[j] = int((lg >= -j).sum())
    return {"q": q, "counts": counts}


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def iid_ref(_):
    import numpy as np
    rng = np.random.default_rng(7)
    u = rng.random((2_000_000, 32))
    lg = np.log2(np.cos(np.pi * u) ** 2 + 1e-300).sum(axis=1)
    return {str(j): float((lg >= -j).mean()) for j in (16, 20, 24, 28, 32, 36, 40)}


@app.local_entrypoint()
def main():
    def is_prime(m):
        if m < 2:
            return False
        for a in range(2, int(m**0.5) + 1):
            if m % a == 0:
                return False
        return True

    qs = []
    for target in (20000, 35000, 60000, 100000, 160000, 240000):
        got = 0
        q = target - (target % NP) + 1
        while got < 4 and q < target * 2:
            if is_prime(q):
                qs.append(q)
                got += 1
            q += NP
    print(f"{len(qs)} rows")
    results = [r for r in dual_spectrum.map(qs, return_exceptions=True)
               if isinstance(r, dict)]
    pj = {int(k): v for k, v in iid_ref.remote(0).items()}
    bands = {}
    for r in sorted(results, key=lambda r: r["q"]):
        q = r["q"]
        band = min((t for t in (20000, 35000, 60000, 100000, 160000, 240000)
                    if q < 2 * t), default=240000)
        ks = {}
        for j, obs in r["counts"].items():
            pred = pj[int(j)] * (q - 1)
            if pred >= 20:
                ks[j] = obs / pred
        bands.setdefault(band, []).append(ks)
    alarm = False
    for band, rows in sorted(bands.items()):
        meds = {}
        for j in (16, 20, 24, 28, 32, 36, 40):
            vals = sorted(r[j] for r in rows if j in r)
            if vals:
                meds[j] = round(vals[len(vals) // 2], 2)
        bad = [j for j, v in meds.items() if v > 4]
        if bad:
            alarm = True
        print(f"band ~{band}: rows={len(rows)} median K(j) = {meds}"
              f"{'  <-- ALARM at ' + str(bad) if bad else ''}")
    print(f"\nalarm: {alarm}")
    with open("/tmp/f1a3_results.json", "w") as f:
        json.dump(results, f, indent=1)
