#!/usr/bin/env python3
"""F2 campaign R5 (Modal): C(3) SCALING CHECK — exhaustive-up-to-
symmetry adversarial max at n = 64, 128 (the n <= 32 rows were fully
exhaustive; this decides whether C(3) is constant or grows with n
BEFORE the proof is attempted — falsification-first).

Symmetry: x -> ux (u in mu_n) maps (a2, a3) -> (a2 u^{d2}, a3 u^{d3})
preserving Z. For each (d2, d3) we take a2 over a transversal of
F_q^x / (mu_n)^{d2} (size (q-1) gcd(d2,n)/n) and a3 over ALL of
F_q^x — this covers every orbit at least once (overcounting is
harmless for a maximum).

PRE-REGISTERED READ: C(3) observed <= 5 at n = 64, 128 => the
constant-C(3) conjecture holds across two more octaves and the proof
target 'C(3) <= C absolute' stands. C(3) growing (>= 7 at n = 128)
=> re-pose R5's theorem with n-dependence before any proof work.
"""
import modal
from math import gcd

app = modal.App("rs-mca-f2-r5-c3scale")
image = modal.Image.debian_slim()

# (q, n, shard, n_shards) — shard over the (d2, d3) pair list
JOBS = ([(193, 64, i, 6) for i in range(6)] +
        [(257, 128, i, 16) for i in range(16)])


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
    xp = [[pow(x, dd, q) for dd in range(n)] for x in D]
    pairs = [(d2, d3) for d2 in range(1, n) for d3 in range(1, n)
             if d2 != d3 and gcd(gcd(d2, d3), n) == 1]
    mypairs = pairs[si::ns]
    # mu_n as subgroup of F_q^x: image of u -> u^{d} is mu_{n/gcd(d,n)};
    # transversal of F_q^x / mu_{n/g}: powers of g with exponents
    # 0 .. (q-1)*g/n - 1 ... precisely cosets of the subgroup of order
    # n/g2: index = (q-1)*g2/n; reps = g^j, j in [0, index)
    best = 0
    wit = None
    for (d2, d3) in mypairs:
        g2 = gcd(d2, n)
        index = (q - 1) * g2 // n
        for j in range(index):
            a2 = pow(g, j, q)
            for a3 in range(1, q):
                z = 0
                for i in range(n):
                    if (1 + a2 * xp[i][d2] + a3 * xp[i][d3]) % q == 0:
                        z += 1
                if z > best:
                    best = z
                    wit = (a2, a3, d2, d3)
    return {"q": q, "n": n, "shard": si, "max": best, "witness": wit,
            "n_pairs": len(mypairs)}


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
        cur = agg.setdefault(key, {"max": 0, "witness": None, "pairs": 0})
        cur["pairs"] += r["n_pairs"]
        if r["max"] > cur["max"]:
            cur["max"] = r["max"]
            cur["witness"] = r["witness"]
    if fails:
        raise SystemExit(f"F2_R5_C3SCALE_FAIL ({fails})")
    for (q, n), v in sorted(agg.items()):
        print(f"  (q={q}, n={n}): exhaustive-up-to-symmetry C(3) = "
              f"{v['max']}  (over {v['pairs']} exponent pairs; witness "
              f"{v['witness']})")
    print("\nF2_R5_C3SCALE_PASS")
