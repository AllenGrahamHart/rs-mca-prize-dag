#!/usr/bin/env python3
"""F2-A3b (floor campaign, Modal): the b = 16 widest-window census at
N = 32, t = 2 — key-bucket-sharded MITM (completes F2's third family).

Cell: all 16-subsets of mu_32 in F_p with p_1 = p_2 = 0; the b=16 window
is the WIDEST (C(32,16) = 601,080,390) — the last place a dichotomy
violation could hide. Shard: bucket the (p1 mod p) key by residue class
mod NSHARDS; each shard enumerates both halves (numpy-chunked C(32,8) =
10,518,300 sums) keeping only its bucket, joins, dedupes subsets, and
classifies extras (non-coset-union). Global balance marker: q^t vs 2^32
(the regime the dichotomy and the floor actually claim — catch #5).
"""
import json
import math

import modal

app = modal.App("rs-mca-f2a3b-b16")
image = modal.Image.debian_slim().pip_install("numpy")

N, T, B = 32, 2, 16
NSHARDS = 10
PRIMES = [40961, 65537, 87041, 114689, 163841, 786433]  # straddle global balance 65536


@app.function(image=image, cpu=2, memory=3072, timeout=60)
def b16_shard(payload):
    import itertools
    import numpy as np
    p, shard = payload
    # pinned mu_32
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
    pts = np.array([pow(zeta, i, p) for i in range(N)], dtype=np.int64)
    sq = pts * pts % p

    h = B // 2
    combos = np.fromiter(itertools.chain.from_iterable(
        itertools.combinations(range(N), h)), dtype=np.int64).reshape(-1, h)

    def keys_of(cc):
        return (pts[cc].sum(axis=1) % p, sq[cc].sum(axis=1) % p)

    # left: bucket by p1 % NSHARDS == shard
    left = {}
    CH = 1_000_000
    for lo in range(0, len(combos), CH):
        cc = combos[lo:lo + CH]
        k1, k2 = keys_of(cc)
        sel = (k1 % NSHARDS) == shard
        for i in np.nonzero(sel)[0]:
            left.setdefault((int(k1[i]), int(k2[i])), []).append(lo + int(i))
    # right: need (-k1) % NSHARDS == shard
    blocks = set()
    for lo in range(0, len(combos), CH):
        cc = combos[lo:lo + CH]
        k1, k2 = keys_of(cc)
        nk1 = (-k1) % p
        nk2 = (-k2) % p
        sel = (nk1 % NSHARDS) == shard
        for i in np.nonzero(sel)[0]:
            key = (int(nk1[i]), int(nk2[i]))
            for li in left.get(key, ()):
                a = frozenset(int(x) for x in combos[li])
                bset = frozenset(int(x) for x in cc[i])
                if not (a & bset):
                    fs2 = a | bset
                    if len(fs2) == B:
                        blocks.add(fs2)

    def is_coset_union(idxs):
        rem = set(idxs)
        ch = True
        while ch and rem:
            ch = False
            for Mc in [m for m in range(2, N + 1) if N % m == 0]:
                step = N // Mc
                for j in range(step):
                    cos = set(range(j, N, step))
                    if cos <= rem and len(cos) == Mc:
                        rem -= cos
                        ch = True
        return not rem
    extras = [sorted(bl) for bl in blocks if not is_coset_union(bl)]
    return {"p": p, "shard": shard, "blocks": len(blocks),
            "extras": len(extras), "extra_examples": extras[:2]}


@app.local_entrypoint()
def main():
    payloads = [(p, s) for p in PRIMES for s in range(NSHARDS)]
    results = [r for r in b16_shard.map(payloads, return_exceptions=True)
               if isinstance(r, dict)]
    agg = {}
    for r in results:
        a = agg.setdefault(r["p"], {"shards": 0, "blocks": 0, "extras": 0, "ex": []})
        a["shards"] += 1
        a["blocks"] += r["blocks"]
        a["extras"] += r["extras"]
        a["ex"] += r["extra_examples"]
    for p, a in sorted(agg.items()):
        gw = math.comb(N, B) / p**T
        marker = "GLOBAL-SUBBALANCE" if p**T >= 2**N else "window"
        flag = "  <-- SUBBALANCE EXTRAS" if a["extras"] and p**T >= 2**N else ""
        print(f"p={p:>7} [{marker:>17}] shards {a['shards']}/{NSHARDS} "
              f"blocks={a['blocks']:>6} extras={a['extras']:>5} "
              f"log2W_b16={math.log2(gw):+.2f}{flag}")
    with open("/tmp/f2a3b_results.json", "w") as f:
        json.dump({str(p): a for p, a in agg.items()}, f, indent=1, default=list)
