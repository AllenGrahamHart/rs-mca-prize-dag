#!/usr/bin/env python3
"""F5-A3v2 (floor campaign, Modal): strip-integrity via direct tangent-core
counting. g(d) = #(k+d)-subsets C where BOTH u|C and v|C are deg<k
interpolation-consistent (the rung-2b two-slope-identity core object);
first-moment decay q^-2d per extra point. PRE-REGISTERED alarm: g(d+1)/g(d)
stalling >= 0.5 at d >= 1 sustained across scales (model rate ~ (n/q)^2)."""
import json
import random
import modal

app = modal.App("rs-mca-f5a3v2-strip")
image = modal.Image.debian_slim()
ROWS = [(2, 47, 3), (2, 97, 3), (2, 193, 2)]


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def tangent_cores(payload):
    import itertools
    k, q, dmax, seed = payload
    rng = random.Random(seed)
    n = q - 1
    domain = list(range(1, q))

    def consistent(vals_pts):
        # deg<k consistency of (pts, vals): interpolate first k, check rest
        pts = [p for p, _ in vals_pts]
        vals = [v for _, v in vals_pts]
        coeffs = [0] * k
        for xi, yi in zip(pts[:k], vals[:k]):
            num = [1]; den = 1
            for xj in pts[:k]:
                if xj == xi: continue
                new = [0] * (len(num) + 1)
                for t, a in enumerate(num):
                    new[t] = (new[t] - a * xj) % q
                    new[t + 1] = (new[t + 1] + a) % q
                num = new
                den = den * (xi - xj) % q
            s = yi * pow(den, -1, q) % q
            for t in range(len(num)):
                coeffs[t] = (coeffs[t] + s * num[t]) % q
        for xi, yi in zip(pts[k:], vals[k:]):
            acc = 0
            for a in reversed(coeffs):
                acc = (acc * xi + a) % q
            if acc != yi: return False
        return True

    def spectrum(u, v):
        g = {}
        for d in range(1, dmax + 1):
            cnt = 0
            for idxs in itertools.combinations(range(n), k + d):
                pu = [(domain[i], u[i]) for i in idxs]
                if not consistent(pu): continue
                pv = [(domain[i], v[i]) for i in idxs]
                if consistent(pv): cnt += 1
            g[d] = cnt
        return g

    out = []
    for kind in ("adversarial", "adversarial", "random"):
        if kind == "adversarial":
            c1 = [rng.randrange(q) for _ in range(k)]
            c2 = [rng.randrange(q) for _ in range(k)]
            def ev(c, x):
                acc = 0
                for a in reversed(c): acc = (acc * x + a) % q
                return acc
            u = [ev(c1, x) for x in domain]
            v = [ev(c2, x) for x in domain]
            for _ in range(3):
                u[rng.randrange(n)] = rng.randrange(q)
                v[rng.randrange(n)] = rng.randrange(q)
        else:
            u = [rng.randrange(q) for _ in range(n)]
            v = [rng.randrange(q) for _ in range(n)]
        out.append({"kind": kind, "g": spectrum(u, v)})
    return {"k": k, "q": q, "n": n, "trials": out}


@app.local_entrypoint()
def main():
    payloads = [(k, q, dmax, 6200 + i) for i, (k, q, dmax) in enumerate(ROWS)]
    results = [r for r in tangent_cores.map(payloads, return_exceptions=True)
               if isinstance(r, dict)]
    alarm = False
    for r in sorted(results, key=lambda r: r["q"]):
        merged = {}
        for t in r["trials"]:
            for d, c in t["g"].items():
                merged[int(d)] = merged.get(int(d), 0) + c
        model = {d: round((r["n"] / r["q"]) ** 2, 5) for d in merged}
        ratios = {d: round(merged.get(d + 1, 0) / merged[d], 4)
                  for d in sorted(merged) if merged[d] >= 20}
        stall = [d for d, rr in ratios.items() if rr >= 0.5]
        if stall: alarm = True
        print(f"k={r['k']} q={r['q']}: g = {dict(sorted(merged.items()))} "
              f"ratios = {ratios} (model rate ~ {(r['n']/r['q'])**2:.3f})"
              f"{'  <-- STALL' if stall else ''}")
    print(f"alarm: {alarm}")
    with open("/tmp/f5a3_results.json", "w") as f:
        json.dump(results, f, indent=1)
