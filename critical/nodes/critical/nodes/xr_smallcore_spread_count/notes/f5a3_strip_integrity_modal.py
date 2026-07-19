#!/usr/bin/env python3
"""F5-A3 (floor campaign, Modal): strip-integrity — third attack family on
the xr_smallcore 16n^3 floor.

The floor's decomposition strips distinct-slope big-core pairs to the
GRADED TANGENT ledger (rung 2b: core r = k+d forces d interpolation
constraints on (u,v) — verified identity). The strip is sound only if the
depth SPECTRUM decays at the first-moment rate (each extra core point
costs ~1/q): a fat tangent tail would leak mass past the ledger back into
the residual. MEASUREMENT: exact depth histograms h(d) = #distinct-slope
aligned codeword pairs with common core k+d, for adversarial + random
(u,v) at three scales. PRE-REGISTERED alarm: the decay ratio
h(d+1)/h(d) stalling at >= 0.5 for d >= 1, sustained across all scales
(the first-moment rate is O(n^2/q) << 0.5 at these rows).
"""
import json
import random

import modal

app = modal.App("rs-mca-f5a3-strip")
image = modal.Image.debian_slim()

ROWS = [(2, 47), (2, 97), (2, 193)]


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def depth_spectrum(payload):
    import itertools
    k, q, seed = payload
    rng = random.Random(seed)
    n = q - 1
    domain = list(range(1, q))

    def interp_coeffs(pts, vals):
        coeffs = [0] * k
        for xi, yi in zip(pts, vals):
            num = [1]
            den = 1
            for xj in pts:
                if xj == xi:
                    continue
                new = [0] * (len(num) + 1)
                for t, a in enumerate(num):
                    new[t] = (new[t] - a * xj) % q
                    new[t + 1] = (new[t + 1] + a) % q
                num = new
                den = den * (xi - xj) % q
            s = yi * pow(den, -1, q) % q
            for t in range(len(num)):
                coeffs[t] = (coeffs[t] + s * num[t]) % q
        return tuple(coeffs)

    def ev(c, x):
        acc = 0
        for a in reversed(c):
            acc = (acc * x + a) % q
        return acc

    def spectrum(u, v):
        aligned = []                 # (z, coeffs, agreement frozenset)
        for z in range(q):
            w = [(u[i] + z * v[i]) % q for i in range(n)]
            seen = set()
            for idxs in itertools.combinations(range(n), k):
                c = interp_coeffs([domain[i] for i in idxs],
                                  [w[i] for i in idxs])
                if c in seen:
                    continue
                seen.add(c)
                agree = frozenset(i for i in range(n)
                                  if ev(c, domain[i]) == w[i])
                if len(agree) >= k:
                    aligned.append((z, c, agree))
        hist = {}
        for (z1, c1, S1), (z2, c2, S2) in itertools.combinations(aligned, 2):
            if z1 == z2:
                continue
            r = len(S1 & S2)
            if r >= k:
                d = r - k
                hist[d] = hist.get(d, 0) + 1
        return hist

    out = []
    for trial in range(3):
        # adversarial: two codewords + sparse noise (pencil through both)
        c1 = [rng.randrange(q) for _ in range(k)]
        c2 = [rng.randrange(q) for _ in range(k)]
        u = [ev(c1, x) for x in domain]
        v = [ev(c2, x) for x in domain]
        for _ in range(2):
            u[rng.randrange(n)] = rng.randrange(q)
        out.append({"kind": "adversarial", "hist": spectrum(u, v)})
    for trial in range(2):
        u = [rng.randrange(q) for _ in range(n)]
        v = [rng.randrange(q) for _ in range(n)]
        out.append({"kind": "random", "hist": spectrum(u, v)})
    return {"k": k, "q": q, "n": n, "trials": out}


@app.local_entrypoint()
def main():
    payloads = [(k, q, 5150 + i) for i, (k, q) in enumerate(ROWS)]
    results = [r for r in depth_spectrum.map(payloads, return_exceptions=True)
               if isinstance(r, dict)]
    alarm = False
    for r in sorted(results, key=lambda r: r["q"]):
        # merge histograms per row
        merged = {}
        for t in r["trials"]:
            for d, c in t["hist"].items():
                merged[int(d)] = merged.get(int(d), 0) + c
        ds = sorted(merged)
        ratios = {d: round(merged.get(d + 1, 0) / merged[d], 4)
                  for d in ds if merged[d] >= 20}
        stall = [d for d, rr in ratios.items() if d >= 1 and rr >= 0.5]
        if stall:
            alarm = True
        print(f"k={r['k']} q={r['q']}: depth hist {merged}  "
              f"decay ratios {ratios}{'  <-- STALL ' + str(stall) if stall else ''}")
    print(f"\nalarm: {alarm}")
    with open("/tmp/f5a3_results.json", "w") as f:
        json.dump(results, f, indent=1)
