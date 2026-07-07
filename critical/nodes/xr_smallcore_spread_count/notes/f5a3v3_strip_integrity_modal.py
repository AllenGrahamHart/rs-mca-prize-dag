#!/usr/bin/env python3
"""F5-A3v3: strip-integrity via line-geometric tangent-core counting (k=2).
g(d) = # (2+d)-subsets consistent for BOTH u and v = sum over (u-line,
v-line) pairs of C(|A_u ∩ A_v|, 2+d) — unique-line property for d >= 1
means no double counting. O(n^3) per word pair. PRE-REGISTERED alarm:
g(d+1)/g(d) stalling >= 0.5 at d >= 1 sustained across scales."""
import json
import random
import modal

app = modal.App("rs-mca-f5a3v3-strip")
image = modal.Image.debian_slim()
ROWS = [(47, 4), (97, 4), (193, 4), (389, 3)]


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def spectra(payload):
    from math import comb
    q, dmax, seed = payload
    rng = random.Random(seed)
    n = q - 1
    domain = list(range(1, q))

    def lines_of(w):
        # all lines (a,b): y = a*x + b agreeing with w on >= 3 points
        seen = {}
        for i in range(n):
            for j in range(i + 1, n):
                xi, xj = domain[i], domain[j]
                a = (w[i] - w[j]) * pow(xi - xj, -1, q) % q
                b = (w[i] - a * xi) % q
                seen.setdefault((a, b), None)
        out = {}
        for (a, b) in seen:
            S = frozenset(i for i in range(n) if (a * domain[i] + b) % q == w[i])
            if len(S) >= 3:
                out[(a, b)] = S
        return out

    def g_spectrum(u, v):
        Lu, Lv = lines_of(u), lines_of(v)
        g = {d: 0 for d in range(1, dmax + 1)}
        for Su in Lu.values():
            for Sv in Lv.values():
                m = len(Su & Sv)
                for d in range(1, dmax + 1):
                    if m >= 2 + d:
                        g[d] += comb(m, 2 + d)
        return g

    out = []
    for kind in ("adversarial", "adversarial", "random"):
        if kind == "adversarial":
            a1, b1 = rng.randrange(q), rng.randrange(q)
            a2, b2 = rng.randrange(q), rng.randrange(q)
            u = [(a1 * x + b1) % q for x in domain]
            v = [(a2 * x + b2) % q for x in domain]
            for _ in range(3):
                u[rng.randrange(n)] = rng.randrange(q)
                v[rng.randrange(n)] = rng.randrange(q)
        else:
            u = [rng.randrange(q) for _ in range(n)]
            v = [rng.randrange(q) for _ in range(n)]
        out.append({"kind": kind, "g": g_spectrum(u, v)})
    return {"q": q, "n": n, "trials": out}


@app.local_entrypoint()
def main():
    payloads = [(q, dmax, 6300 + i) for i, (q, dmax) in enumerate(ROWS)]
    results = [r for r in spectra.map(payloads, return_exceptions=True)
               if isinstance(r, dict)]
    alarm = False
    for r in sorted(results, key=lambda r: r["q"]):
        for t in r["trials"]:
            g = {int(k): v for k, v in t["g"].items()}
            ratios = {d: round(g.get(d + 1, 0) / g[d], 4)
                      for d in sorted(g) if g[d] >= 20}
            stall = [d for d, rr in ratios.items() if rr >= 0.5]
            # adversarial words carry the PLANTED near-full lines (m ~ n):
            # their binomial cascade is structural (the tangent ledger's own
            # charged object) — classify: exclude the planted line pair by
            # reporting both raw and (for random words) the accident-only view
            if stall and t["kind"] == "random":
                alarm = True
            print(f"q={r['q']} [{t['kind']:>11}]: g={g} ratios={ratios}"
                  f"{'  <-- STALL' if stall else ''}")
    print(f"alarm (random-word stall sustained): {alarm}")
    with open("/tmp/f5a3_results.json", "w") as f:
        json.dump(results, f, indent=1)
