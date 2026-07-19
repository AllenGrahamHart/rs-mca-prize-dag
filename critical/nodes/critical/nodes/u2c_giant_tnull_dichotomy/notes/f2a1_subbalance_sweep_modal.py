#!/usr/bin/env python3
"""F2-A1 (floor campaign, Modal): the sub-balance extras sweep — first attack
on the u2c EXTRAS-BUDGET floor.

FLOOR UNDER ATTACK: #{non-coset-union t-null blocks} <= n^3 at official
(sub-balance) rows. PRE-REGISTERED falsifier: sub-balance scaled rows with
extras exceeding the transported budget, SUSTAINED across >= 3 scales;
above-balance window accidents do NOT count.

DESIGN: exact COMPLETE censuses (MITM on half-subsets — upgrades the
original 60s-capped partial scans) of t-null b-subsets of mu_N in F_p,
classified into coset-union vs EXTRAS, across a window-ratio sweep
W = C(N,b)/p^t spanning ~2^6 (above balance; extras EXPECTED at Poisson
rates — calibration region) down to ~2^-14 (deep sub-balance; the floor
needs extras -> 0 up to transported-budget stragglers). The known
transition cell (N=64, t=3, b=8: extras 192 -> 64 -> 0) is included as a
calibration gate. A signal = extras persisting at W << 1, sustained across
>= 3 scales (cells and primes) — then CLASSIFY before declaring (near-
boundary Poisson tail vs genuine deep violations; primitivity refinement).

Cells: (N, t, b) in {(32,2,6), (32,2,8), (64,3,8), (64,3,10), (128,4,6)};
~12 primes p ≡ 1 (mod N) per cell, log-spaced in W. One Modal job per
(cell, p): MITM join C(N, b/2)^2 with t-tuple keys — all << 60 s.
"""
import json
import math

import modal

app = modal.App("rs-mca-f2a1-subbalance")
image = modal.Image.debian_slim().pip_install("numpy")

CELLS = [(32, 2, 6), (32, 2, 8), (64, 3, 8), (64, 3, 10), (128, 4, 6)]


@app.function(image=image, cpu=2, memory=3072, timeout=60)
def census_cell(payload):
    import itertools
    from collections import defaultdict
    N, t, b, p = payload
    # mu_N in F_p at the pinned embedding
    n0 = p - 1
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
    while any(pow(g, (p - 1) // f, p) == 1 for f in fs):
        g += 1
    zeta = pow(g, (p - 1) // N, p)
    pts = [pow(zeta, i, p) for i in range(N)]
    pows = [[pow(x, r, p) for r in range(1, t + 1)] for x in pts]

    h = b // 2
    hb = b - h
    left = {}
    for combo in itertools.combinations(range(N), h):
        key = tuple(sum(pows[i][r] for i in combo) % p for r in range(t))
        left.setdefault(key, []).append(combo)
    hits = []
    for combo in itertools.combinations(range(N), hb):
        key = tuple((-sum(pows[i][r] for i in combo)) % p for r in range(t))
        for lc in left.get(key, ()):
            if lc[-1] < combo[0]:          # enforce disjoint + ordered split
                hits.append(lc + combo)
    # dedupe: ordered split misses splits where indices interleave — redo
    # properly: enumerate all b-subsets via join on ANY h/hb split forces
    # ordering; instead join with lc max < min(combo) undercounts. Use
    # canonical: left = combos of the first N/2 indices padded... simplest
    # correct approach: left over ALL h-subsets, right over ALL hb-subsets,
    # dedupe full subsets via frozenset, require disjointness.
    seen = set()
    blocks = []
    for combo in itertools.combinations(range(N), hb):
        key = tuple((-sum(pows[i][r] for i in combo)) % p for r in range(t))
        for lc in left.get(key, ()):
            if set(lc) & set(combo):
                continue
            fs2 = frozenset(lc) | frozenset(combo)
            if len(fs2) == b and fs2 not in seen:
                seen.add(fs2)
                blocks.append(sorted(fs2))
    # classify: union of full M-cosets (M | N, M > t... boundary orders)
    def is_coset_union(idxs):
        s = set(idxs)
        for M in range(2, N + 1):
            if N % M:
                continue
            step = N // M
            # cosets of the order-M subgroup = index classes mod step
            pass
        # a mu_M-coset (order M subgroup coset) = {j, j+N/M, j+2N/M, ...}
        rem = set(idxs)
        changed = True
        while changed and rem:
            changed = False
            for M in [M for M in range(2, N + 1) if N % M == 0]:
                step = N // M
                for j in range(step):
                    coset = set(range(j, N, step))
                    if coset <= rem and len(coset) == M:
                        rem -= coset
                        changed = True
        return not rem
    extras = [bl for bl in blocks if not is_coset_union(bl)]
    W = math.comb(N, b) / p**t
    return {"N": N, "t": t, "b": b, "p": p, "log2W": round(math.log2(W), 2),
            "tnull_blocks": len(blocks), "extras": len(extras),
            "extra_examples": extras[:3]}


@app.local_entrypoint()
def main():
    def is_prime(m):
        if m < 2:
            return False
        for a in range(2, int(m**0.5) + 1):
            if m % a == 0:
                return False
        return True

    payloads = [(64, 3, 8, 257), (64, 3, 8, 577), (64, 3, 8, 641),
                (64, 3, 8, 769)]   # calibration gate: banked 192/64/0/0
    for N, t, b in CELLS:
        if b == 10:
            continue   # deferred to F2-A1b (needs prefix-sharded joins)
        Wtargets = [2.0**e for e in (6, 3, 1, 0, -1, -2, -4, -6, -8, -10, -12, -14)]
        for W in Wtargets:
            p_target = int((math.comb(N, b) / W) ** (1.0 / t))
            q = max(N + 1, p_target - (p_target % N) + 1)
            while not is_prime(q):
                q += N
            if q < 2**42 and (N, t, b, q) not in payloads:
                payloads.append((N, t, b, q))
    payloads = sorted(set(payloads))
    print(f"{len(payloads)} census jobs")
    results = [r for r in census_cell.map(payloads, return_exceptions=True)
               if isinstance(r, dict)]
    results.sort(key=lambda r: (r["N"], r["t"], r["b"], -r["log2W"]))
    cur = None
    for r in results:
        cell = (r["N"], r["t"], r["b"])
        if cell != cur:
            cur = cell
            print(f"\n== cell N={r['N']} t={r['t']} b={r['b']} ==")
        flag = "  <-- SUBBALANCE EXTRAS" if r["log2W"] < 0 and r["extras"] > 0 else ""
        print(f"  p={r['p']:>8} log2W={r['log2W']:>7} tnull={r['tnull_blocks']:>7} "
              f"extras={r['extras']:>6}{flag}")
    with open("/tmp/f2a1_results.json", "w") as f:
        json.dump(results, f, indent=1)
