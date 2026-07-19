#!/usr/bin/env python3
"""F2 campaign (Modal): RUNG-2 LADDER STUDY (cycle 86) — does the
struct/extras dichotomy propagate up the alphabet ladder?

Rung 2 = the weighted signed-trade census C''_j (alphabet {0,+-1},
weights 2^{#zeros}) from the ladder identity (satellite 21).
RUNG-2 STRUCT (proved by construction): sign patterns CONSTANT ON
MOD-4 EXPONENT CLASSES (each class in {0,+1,-1}; class moment
vectors vanish for j <= 3, and any +-combination of vanishing
vectors vanishes); total weight (2^4 + 1 + 1)^{n/4} = 18^{n/4}.
Rung-2 extras deviation (same algebra as rung 1):
    extras2_dev = (q^j C'' - 4^n) - 18^{n/4} (q^j - 1)
Comparison scale = rung 3: sqrt(sum_{c != 0} e^{4 S_c}) — computed
as a DIRECT POSITIVE float frequency sum (rungs >= 2 are positive-
sum problems: no cancellation, floats sound — unlike rung 1).

PRE-REGISTERED READS:
  (1) C'' >= 18^{n/4} at every row (struct is real);
  (2) deep-row exactness: rows with rung-1 extras = 0 should show
      C'' = 18^{n/4} EXACTLY (the dichotomy at rung 2) — sharp
      prediction at (113,16,3) from the cycle-85 output;
  (3) ratio2 = |extras2_dev| / sqrt(sum e^{4S}) across 9 rows:
      slope of log(ratio2) vs log(population) <= 0.1 stabilization,
      >= 0.25 danger, else inconclusive (same thresholds as rung 1
      for comparability; rung-2 terms are positive so this measures
      fluctuation-vs-scale, not sign alignment).
If rung-2 extras are random-like with stable O(1) ratio, the
INDUCTION SHAPE is real: each rung's extras controlled by the next
rung's positive count — the summit's proof strategy in ladder form.
"""
import math

import modal

app = modal.App("rs-mca-f2-rung2")
image = modal.Image.debian_slim().pip_install("numpy")

JOBS = [
    (97, 32, 2), (97, 32, 3), (113, 16, 2), (113, 16, 3),
    (193, 64, 2), (257, 64, 2), (353, 32, 2), (353, 32, 3),
    (449, 64, 2),
]


@app.function(image=image, cpu=2, memory=10240, timeout=280)
def cell(job):
    q, n, j = job
    assert (q - 1) % n == 0 and n % 4 == 0
    import numpy as np

    def pf(x):
        out, d = [], 2
        while d * d <= x:
            while x % d == 0:
                out.append(d)
                x //= d
            d += 1
        if x > 1:
            out.append(x)
        return out

    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // r, q) != 1 for r in set(pf(q - 1))))
    h = pow(g, (q - 1) // n, q)
    D = [pow(h, i, q) for i in range(n)]
    xbar = [[pow(x, i, q) for i in range(1, j + 1)] for x in D]
    Q = q ** j
    ar = np.arange(Q, dtype=np.int64)
    cdig = [((ar // q ** i) % q).astype(np.int64) for i in range(j)]

    ups, dns = [], []
    for xi in range(n):
        xb = xbar[xi]
        ups.append(sum(((cdig[i] + xb[i]) % q) * q ** i for i in range(j)))
        dns.append(sum(((cdig[i] - xb[i]) % q) * q ** i for i in range(j)))

    # rung-2 census DP (weights 2/1/1), exact
    if n <= 32:
        counts = np.zeros(Q, dtype=np.int64)
        counts[0] = 1
        for xi in range(n):
            t1 = np.zeros_like(counts)
            t1[ups[xi]] = counts
            t2 = np.zeros_like(counts)
            t2[dns[xi]] = counts
            counts = 2 * counts + t1 + t2
        assert int(counts.max()) < (1 << 62)
        Cpp = int(counts[0])
    else:
        counts = [0] * Q
        counts[0] = 1
        for xi in range(n):
            up = ups[xi].tolist()
            dn = dns[xi].tolist()
            t1 = [0] * Q
            t2 = [0] * Q
            for i2 in range(Q):
                t1[up[i2]] = counts[i2]
                t2[dn[i2]] = counts[i2]
            counts = [2 * c + a + b for c, a, b in zip(counts, t1, t2)]
        Cpp = counts[0]

    struct2 = 18 ** (n // 4)
    extras2_dev = (Q * Cpp - 4 ** n) - struct2 * (Q - 1)

    # rung-3 scale: direct positive float sum of e^{4S}
    theta = math.pi / q
    l4 = np.array([4 * math.log(2.0)] +
                  [4 * math.log(abs(2 * math.cos(theta * s)))
                   for s in range(1, q)])
    S4 = np.zeros(Q)
    for xi in range(n):
        xb = xbar[xi]
        sidx = sum(cdig[i] * xb[i] for i in range(j)) % q
        S4 += l4[sidx]
    S4[0] = -1e30
    denom = math.sqrt(float(np.exp(S4).sum()))
    ratio2 = abs(float(extras2_dev)) / denom
    return {"q": q, "n": n, "j": j, "Q": Q, "Cpp_over_struct":
            float(Cpp) / struct2, "struct_exact": Cpp == struct2,
            "ge_struct": Cpp >= struct2,
            "extras2_dev": float(extras2_dev), "ratio2": ratio2}


@app.local_entrypoint()
def main():
    res = list(cell.map(JOBS, return_exceptions=True))
    fails = 0
    pts = []
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:300])
            continue
        if not r["ge_struct"]:
            fails += 1
        print(f"(q={r['q']:>4}, n={r['n']:>3}, j={r['j']}) "
              f"|c|={r['Q']:>9}: C''/18^(n/4) = "
              f"{r['Cpp_over_struct']:12.4f}"
              f"{' (STRUCT EXACT)' if r['struct_exact'] else ''}  "
              f"extras2_dev = {r['extras2_dev']:+.3e}  "
              f"ratio2 = {r['ratio2']:7.2f}  "
              f"{'OK' if r['ge_struct'] else 'FLAG: census < struct!'}")
        pts.append((math.log(r["Q"] - 1),
                    math.log(max(r["ratio2"], 1e-9))))
    if len(pts) >= 6:
        mx = sum(p[0] for p in pts) / len(pts)
        my = sum(p[1] for p in pts) / len(pts)
        num = sum((p[0] - mx) * (p[1] - my) for p in pts)
        den = sum((p[0] - mx) ** 2 for p in pts)
        slope = num / den
        print(f"\nPRIMARY READ: slope of log(ratio2) vs log(population)"
              f" = {slope:.3f} over {len(pts)} rows")
        if slope <= 0.1:
            print("=> RUNG-2 STABILIZATION (the ladder induction shape "
                  "is real at reachable scales)")
        elif slope >= 0.25:
            print("=> RUNG-2 GROWTH — bank loudly")
            fails += 1
        else:
            print("=> INCONCLUSIVE — add scales")
    if fails:
        raise SystemExit(f"F2_RUNG2_FAIL ({fails})")
    print("\nF2_RUNG2_LADDER_PASS")
