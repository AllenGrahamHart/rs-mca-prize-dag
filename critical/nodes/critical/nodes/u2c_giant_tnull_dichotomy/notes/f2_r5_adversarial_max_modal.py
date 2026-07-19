#!/usr/bin/env python3
"""F2 campaign R5 (Modal): EXHAUSTIVE ADVERSARIAL MAXIMUM of gcd-1
3-sparse root counts — the critical viability test for R5-official.

Object: Zmax(q, n) = max over ALL (a2, a3 in F_q^x, d2 != d3 in [1,n),
gcd(d2, d3, n) = 1) of #{x in mu_n : 1 + a2 x^{d2} + a3 x^{d3} = 0}
(a1 normalized to 1 by scaling f).

PRE-REGISTERED READ (immutable): if Zmax <= 2s + 1 = 7 at every row,
the s-scale truth is ADVERSARIALLY supported (random sampling showed
4-5; the sqrt(q)-scale tail does not exist) and R5-official stays
alive via the algebraic route. If Zmax reaches sqrt(q)-scale at any
row, R5-official is DEAD as a counting route — bank the negative and
the witnessing instance.
Gates: exhaustiveness accounting (instance counts printed); brute
force evaluation only (no formulas in the loop).
"""
import modal
from math import gcd

app = modal.App("rs-mca-f2-r5-advmax")
image = modal.Image.debian_slim()

# (q, n, shard_index, n_shards) — shard over a2
JOBS = ([(17, 16, i, 2) for i in range(2)] +
        [(31, 30, i, 4) for i in range(4)] +
        [(97, 32, i, 12) for i in range(12)])


@app.function(image=image, cpu=2, memory=1024, timeout=280)
def shard(job):
    q, n, si, ns = job
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
    # precompute x^d tables
    xp = [[pow(x, dd, q) for dd in range(n)] for x in D]
    pairs = [(d2, d3) for d2 in range(1, n) for d3 in range(1, n)
             if d2 != d3 and gcd(gcd(d2, d3), n) == 1]
    best = 0
    wit = None
    count = 0
    for a2 in range(1 + si, q, ns):
        for a3 in range(1, q):
            for (d2, d3) in pairs:
                z = 0
                for i in range(n):
                    if (1 + a2 * xp[i][d2] + a3 * xp[i][d3]) % q == 0:
                        z += 1
                count += 1
                if z > best:
                    best = z
                    wit = (a2, a3, d2, d3)
    return {"q": q, "n": n, "shard": si, "max": best, "witness": wit,
            "instances": count}


@app.local_entrypoint()
def main():
    res = list(shard.map(JOBS, return_exceptions=True))
    fails = 0
    agg = {}
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:200])
            continue
        key = (r["q"], r["n"])
        cur = agg.setdefault(key, {"max": 0, "witness": None, "instances": 0})
        cur["instances"] += r["instances"]
        if r["max"] > cur["max"]:
            cur["max"] = r["max"]
            cur["witness"] = r["witness"]
    if fails:
        raise SystemExit(f"F2_R5_ADVMAX_FAIL ({fails})")
    ok = True
    for (q, n), v in sorted(agg.items()):
        verdict = "s-scale" if v["max"] <= 7 else "TAIL FOUND"
        if v["max"] > 7:
            ok = False
        print(f"  (q={q}, n={n}): EXHAUSTIVE Zmax = {v['max']} over "
              f"{v['instances']} gcd-1 instances  [{verdict}]  "
              f"witness={v['witness']}")
    print(f"\npre-registered read: adversarial s-scale supported: {ok}")
    print("F2_R5_ADVMAX_PASS")
