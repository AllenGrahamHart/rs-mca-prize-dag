#!/usr/bin/env python3
"""SOL_TARGET_4 decisive rung (task #36): T_4(q, N) at N = 256, for
q = 257 (index 1, densest) and q = 769 (index 3, the maelcar-audit
row). Exact integer census, same algorithm as the audited replay
notes/pilots_20260803/maelcar_audit/replay/t4_ladder_vs_sol_target_4.py
(validated against the banked (32,97) = 792 and maelcar's n=128 row).

T_4(q,N) = #{ordered pairs (A,B): disjoint 4-subsets of mu_N with
p_i(A) = p_i(B), i = 1,2,3}. Conjecture at risk: T_4 <= C N^3.
"""
import hashlib
import json
from pathlib import Path

import modal

DIRECTORY = Path(__file__).parent
RESULT = DIRECTORY / "sol_target4_n256_result.json"

app = modal.App("rs-mca-sol-target4-n256")
image = modal.Image.debian_slim(python_version="3.12").pip_install("numpy==2.2.5")


@app.function(image=image, cpu=8.0, memory=49152, timeout=3500)
def t4(N: int, q: int):
    from itertools import chain, combinations
    import numpy as np

    def root_of_order(p, n):
        for c in range(2, p):
            z = pow(c, (p - 1) // n, p)
            if pow(z, n, p) == 1 and pow(z, n // 2, p) != 1:
                return z
        raise AssertionError

    roots = np.array([pow(root_of_order(q, N), e, q) for e in range(N)],
                     dtype=np.int64)
    total = N * (N - 1) * (N - 2) * (N - 3) // 24
    quad = np.fromiter(chain.from_iterable(combinations(range(N), 4)),
                       dtype=np.uint8, count=4 * total).reshape(-1, 4)
    key = np.empty(total, dtype=np.int64)
    for lo in range(0, total, 1 << 22):
        hi = min(lo + (1 << 22), total)
        c = quad[lo:hi].astype(np.int64)
        v0, v1, v2, v3 = (roots[c[:, i]] for i in range(4))
        e1 = (v0 + v1 + v2 + v3) % q
        e2 = (v0 * v1 + v0 * v2 + v0 * v3 + v1 * v2 + v1 * v3 + v2 * v3) % q
        e3 = (v0 * v1 * v2 + v0 * v1 * v3 + v0 * v2 * v3 + v1 * v2 * v3) % q
        key[lo:hi] = (e1 * q + e2) * q + e3
    order = np.argsort(key, kind="stable").astype(np.int64)
    ks = key[order]
    del key
    starts = np.flatnonzero(np.r_[True, ks[1:] != ks[:-1]]).astype(np.int64)
    del ks
    lengths = np.diff(np.r_[starts, np.int64(total)]).astype(np.int64)
    keep = lengths >= 2
    starts, lengths = starts[keep], lengths[keep]
    unordered = 0
    from itertools import combinations as comb2
    for L in np.unique(lengths):
        s = starts[lengths == L]
        blk = order[s[:, None] + np.arange(int(L), dtype=np.int64)]
        for a, b in comb2(range(int(L)), 2):
            A, B = quad[blk[:, a]], quad[blk[:, b]]
            d = np.ones(len(A), dtype=bool)
            for i in range(4):
                for j in range(4):
                    d &= (A[:, i] != B[:, j])
            unordered += int(d.sum())
        del blk
    t = 2 * unordered
    return dict(N=N, q=q, T4=t, N3=N ** 3, ratio=t / N ** 3,
                index=(q - 1) // N)


@app.local_entrypoint()
def main():
    rows = [(256, 257), (256, 769)]
    out = {}
    for r in t4.starmap(rows):
        out[f"N{r['N']}_q{r['q']}"] = r
        print(f"N={r['N']} q={r['q']} (index {r['index']}): "
              f"T4 = {r['T4']}  T4/N^3 = {r['ratio']:.4f}")
    payload = json.dumps(out, indent=1, sort_keys=True)
    RESULT.write_text(payload + "\n")
    print("sha256", hashlib.sha256(payload.encode()).hexdigest())
