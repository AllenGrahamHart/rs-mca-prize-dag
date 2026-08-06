#!/usr/bin/env python3
"""F2 campaign R5 falsification test (Modal): root counts of sparse
polynomials on mu_n, n a 2-power (pre-registered in the target brief
and log #23 — MEASUREMENT before proof).

Per cell (q, n, s): sample random s-sparse functions on mu_n
(s distinct exponents mod n, nonzero coefficients), count mu_n-roots
by direct evaluation. Report the root-count histogram tail (max,
99.9th percentile) vs the structured benchmark (binomial-collapsible
samples are counted separately by detecting exponent-difference
2-adic collapse).

PRE-REGISTERED READ (immutable, log #23): if random NON-collapsible
s-sparse samples routinely achieve root counts >= n/4 at s = 3, 4,
route R5 is DEAD (generic sparse polynomials would carry many roots
and no structure dichotomy exists). If non-collapsible root counts
stay O(s)-ish while only collapsible samples reach n/2^j-scale
counts, R5's dichotomy target is supported.
"""
import random
from math import gcd

import modal

app = modal.App("rs-mca-f2-r5-sparse")
image = modal.Image.debian_slim()

CELLS = [(97, 16, 3), (97, 16, 4), (97, 32, 3), (97, 32, 4),
         (97, 32, 6), (193, 64, 3), (193, 64, 4), (193, 64, 6),
         (257, 64, 8), (257, 128, 4)]
N_SAMPLES = 20000


@app.function(image=image, cpu=2, memory=1024, timeout=280)
def cell(job):
    q, n, s = job
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
    D = [pow(h, i, q) for i in range(n)]
    rng = random.Random(4000 + n + s)
    # precompute powers table: pw[i][e] = D[i]^e for e < n
    pw = [[pow(x, e, q) for e in range(n)] for x in D]
    hist_nc = {}   # non-collapsible
    hist_c = {}    # collapsible (all exponent diffs share a 2-power
                   # factor with n beyond gcd 1 — the binomial shadow)
    for _ in range(N_SAMPLES):
        exps = rng.sample(range(n), s)
        coefs = [rng.randrange(1, q) for _ in range(s)]
        # collapsibility: gcd of all pairwise exponent diffs with n
        gg = 0
        for i in range(1, s):
            gg = gcd(gg, exps[i] - exps[0])
        gg = gcd(gg, n)
        collapsible = gg > 1   # function factors through mu_{n/gg}
        roots = 0
        for i in range(n):
            v = 0
            for a, e in zip(coefs, exps):
                v = (v + a * pw[i][e]) % q
            if v == 0:
                roots += 1
        tgt = hist_c if collapsible else hist_nc
        tgt[roots] = tgt.get(roots, 0) + 1
    def summarize(hist):
        if not hist:
            return None
        total = sum(hist.values())
        mx = max(hist)
        # 99.9th percentile
        acc = 0
        p999 = mx
        for k in sorted(hist):
            acc += hist[k]
            if acc >= 0.999 * total:
                p999 = k
                break
        return {"n_samples": total, "max": mx, "p999": p999}
    return {"q": q, "n": n, "s": s,
            "noncollapsible": summarize(hist_nc),
            "collapsible": summarize(hist_c)}


@app.local_entrypoint()
def main():
    res = list(cell.map(CELLS, return_exceptions=True))
    fails = 0
    dead = 0
    print(f"{'cell':>13}  non-collapsible (max/p999/N)   collapsible (max/p999/N)")
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:200])
            continue
        nc, co = r["noncollapsible"], r["collapsible"]
        ncs = (f"{nc['max']}/{nc['p999']}/{nc['n_samples']}" if nc else "-")
        cos = (f"{co['max']}/{co['p999']}/{co['n_samples']}" if co else "-")
        print(f" ({r['q']},{r['n']},s={r['s']})".rjust(13) +
              f"  {ncs:>28}   {cos:>24}")
        if nc and r["s"] in (3, 4) and nc["max"] >= r["n"] // 4:
            dead += 1
    if fails:
        raise SystemExit(f"F2_R5_SPARSE_ROOTS_FAIL ({fails})")
    print(f"\nR5 kill events (non-collapsible max >= n/4 at s=3,4): {dead}")
    print("F2_R5_SPARSE_ROOTS_PASS")
