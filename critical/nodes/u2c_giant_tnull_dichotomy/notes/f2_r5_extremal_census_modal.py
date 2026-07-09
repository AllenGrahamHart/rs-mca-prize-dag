#!/usr/bin/env python3
"""F2 campaign R5 (Modal): EXTREMAL CENSUS — enumerate ALL gcd-1
3-sparse instances achieving the exhaustive maximum root count, and
classify their structure (measurement; feeds the C(3) proof).

Per row: collect every (a2, a3, d2, d3) with Z >= Zmax_known and
record: the root set R, its symmetry invariants (closed under
x -> 1/x? under x -> -x? a coset of a subgroup? ratios structure:
the multiset {r_i / r_j}), and the exponent-pair orbit ((d2, d3) up
to the symmetries d -> d + multiples-of-n-in-effect, unit scaling
x -> ux which shifts (a2, a3) but not (d2, d3), and x -> x^k for
k coprime to n which maps (d2, d3) -> (k d2, k d3) mod n).

Read: if the extremals form a single orbit under these symmetries
(or few orbits), the C(3) proof has an explicit extremal family to
permit; report orbits and root-set invariants.
"""
import modal
from math import gcd

app = modal.App("rs-mca-f2-r5-extremal")
image = modal.Image.debian_slim()

JOBS = [(17, 16, 3, 0, 2), (17, 16, 3, 1, 2),
        (31, 30, 4, 0, 4), (31, 30, 4, 1, 4), (31, 30, 4, 2, 4),
        (31, 30, 4, 3, 4),
        (97, 32, 4, 0, 12)] + [(97, 32, 4, i, 12) for i in range(1, 12)]


@app.function(image=image, cpu=2, memory=1024, timeout=280)
def shard(job):
    q, n, zmax, si, ns = job
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
    dlog_mu = {D[i]: i for i in range(n)}
    xp = [[pow(x, dd, q) for dd in range(n)] for x in D]
    pairs = [(d2, d3) for d2 in range(1, n) for d3 in range(1, n)
             if d2 != d3 and gcd(gcd(d2, d3), n) == 1]
    hits = []
    for a2 in range(1 + si, q, ns):
        for a3 in range(1, q):
            for (d2, d3) in pairs:
                roots = [i for i in range(n)
                         if (1 + a2 * xp[i][d2] + a3 * xp[i][d3]) % q == 0]
                if len(roots) >= zmax:
                    R = [D[i] for i in roots]
                    inv_closed = all(pow(x, q - 2, q) in set(R) for x in R)
                    neg_closed = all((q - x) % q in set(R) for x in R)
                    # root index set in mu_n and its difference structure
                    idx = sorted(dlog_mu[x] for x in R)
                    diffs = sorted({(idx[j] - idx[i]) % n
                                    for i in range(len(idx))
                                    for j in range(len(idx)) if i != j})
                    hits.append({"a2": a2, "a3": a3, "d2": d2, "d3": d3,
                                 "root_idx": idx, "inv": inv_closed,
                                 "neg": neg_closed, "diffs": diffs})
    return {"q": q, "n": n, "hits": hits}


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
        agg.setdefault((r["q"], r["n"]), []).extend(r["hits"])
    if fails:
        raise SystemExit(f"F2_R5_EXTREMAL_FAIL ({fails})")
    for (q, n), hits in sorted(agg.items()):
        # orbit reduction: (d2,d3) ~ (k d2 mod n, k d3 mod n), k coprime n
        orbits = {}
        for hit in hits:
            best = None
            for k in range(1, n):
                if gcd(k, n) != 1:
                    continue
                key = (hit["d2"] * k % n, hit["d3"] * k % n)
                key = tuple(sorted(key))
                if best is None or key < best:
                    best = key
            orbits.setdefault(best, []).append(hit)
        print(f"(q={q}, n={n}): {len(hits)} extremal instances, "
              f"{len(orbits)} exponent orbits:")
        for key, hs in sorted(orbits.items()):
            invf = sum(1 for x in hs if x["inv"]) / len(hs)
            negf = sum(1 for x in hs if x["neg"]) / len(hs)
            sample_diffs = hs[0]["diffs"]
            print(f"   orbit {key}: {len(hs)} instances; inv-closed "
                  f"{invf:.2f}, neg-closed {negf:.2f}; sample root "
                  f"idx-diffs {sample_diffs[:8]}")
    print("\nF2_R5_EXTREMAL_CENSUS_PASS")
