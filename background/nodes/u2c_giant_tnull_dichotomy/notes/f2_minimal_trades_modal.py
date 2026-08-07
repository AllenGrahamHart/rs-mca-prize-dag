#!/usr/bin/env python3
"""F2 campaign (Modal): MINIMAL TRADE SIZE experiment — the trade
decomposition question (log #55; the true final object).

A trade of size h: disjoint h-sets (R1, R2) in mu_n with equal power
sums p_1..p_t. MINIMAL: no proper sub-pair (equal sizes h' < h,
R1' subset R1, R2' subset R2) is itself a trade.

Per cell (q, n, t, h_max): bucket h-subsets by moment vector, collect
trades (capped), test minimality exhaustively per trade. Report the
count of minimal trades per h.

PRE-REGISTERED READ: if minimal trades exist only at h <= t + 1
across all n (bounded minimal size), the decomposition theorem is
supported and the M2 lane re-enters effective range. If minimal
trades of growing h appear (h scaling with n), decomposition is
FALSE — bank the negative; the flatness route is the path.
"""
import modal
from itertools import combinations

app = modal.App("rs-mca-f2-mintrades")
image = modal.Image.debian_slim()

CELLS = [(97, 32, 2, 5), (193, 64, 2, 4), (97, 32, 3, 5), (113, 16, 2, 6)]
CAP = 4000


@app.function(image=image, cpu=2, memory=3072, timeout=280)
def cell(job):
    q, n, t, hmax = job
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
    h_ = pow(g, (q - 1) // n, q)
    D = [pow(h_, i, q) for i in range(n)]
    pw = {x: [pow(x, j, q) for j in range(t + 1)] for x in D}

    def mom(R):
        return tuple(sum(pw[x][j] for x in R) % q for j in range(1, t + 1))

    def is_trade(R1, R2):
        return mom(R1) == mom(R2)

    results = {}
    for h in range(2, hmax + 1):
        buckets = {}
        for R in combinations(D, h):
            buckets.setdefault(mom(R), []).append(R)
        trades = []
        for key, lst in buckets.items():
            for i in range(len(lst)):
                for j in range(i + 1, len(lst)):
                    if not (set(lst[i]) & set(lst[j])):
                        trades.append((lst[i], lst[j]))
                        if len(trades) >= CAP:
                            break
                if len(trades) >= CAP:
                    break
            if len(trades) >= CAP:
                break
        minimal = 0
        for (R1, R2) in trades:
            is_min = True
            for hp in range(1, h):
                found = False
                for A in combinations(R1, hp):
                    for B in combinations(R2, hp):
                        if mom(A) == mom(B):
                            found = True
                            break
                    if found:
                        break
                if found:
                    is_min = False
                    break
            if is_min:
                minimal += 1
        results[h] = {"trades_seen": len(trades), "minimal": minimal,
                      "capped": len(trades) >= CAP}
    return {"q": q, "n": n, "t": t, "res": results}


@app.local_entrypoint()
def main():
    res = list(cell.map(CELLS, return_exceptions=True))
    fails = 0
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:200])
            continue
        print(f"(q={r['q']}, n={r['n']}, t={r['t']}):")
        for h, v in sorted(r["res"].items(), key=lambda kv: int(kv[0])):
            print(f"   h={h}: trades sampled {v['trades_seen']}"
                  f"{' (capped)' if v['capped'] else ''}, "
                  f"MINIMAL = {v['minimal']}")
    if fails:
        raise SystemExit(f"F2_MINTRADES_FAIL ({fails})")
    print("\nF2_MINIMAL_TRADES_PASS")
