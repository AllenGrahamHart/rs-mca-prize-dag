#!/usr/bin/env python3
"""Exceptional-prime census: every admissible q = 1 (mod 2N) dividing a weight-w norm.

Pass 1: factor every ATTAINED distinct norm value at each weight (exact, sympy).
Pass 2: re-enumerate the weight and pull out an explicit witness f for every
        census prime at its minimal weight; re-verify with the Bareiss determinant.

No floats.  All norms and cofactors are emitted as decimal strings.
"""

from __future__ import annotations

import argparse
import json
import os
from itertools import combinations

import numpy as np
from sympy import factorint

from enum_weight import sign_matrix
from norm_core import norm_bareiss, norm_batch_crt3, norm_batch_int64


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, required=True)
    ap.add_argument("--dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--crt", action="store_true")
    args = ap.parse_args()
    N = args.N
    twoN = 2 * N

    per_weight = []
    prime_min_w: dict[int, int] = {}
    prime_norm: dict[int, int] = {}
    need: dict[int, dict[int, list]] = {}     # w -> {norm_value: [primes]}
    all_primes: set[int] = set()

    ws = []
    for w in range(1, N + 1):
        f = os.path.join(args.dir, "N%02d_w%02d_norms.npy" % (N, w))
        if os.path.exists(f):
            ws.append(w)

    for w in ws:
        vals = np.load(os.path.join(args.dir, "N%02d_w%02d_norms.npy" % (N, w)))
        primes_w = {}
        for v in vals.tolist():
            if v <= 1:
                continue
            for p in factorint(int(v)):
                if p % twoN == 1:
                    if p not in primes_w or int(v) < primes_w[p]:
                        primes_w[p] = int(v)
        for p, v in primes_w.items():
            if p not in prime_min_w:
                prime_min_w[p] = w
                prime_norm[p] = v
                need.setdefault(w, {}).setdefault(v, []).append(p)
        all_primes |= set(primes_w)
        per_weight.append({
            "w": w,
            "n_distinct_norms": int(vals.size),
            "max_norm": str(int(vals.max())),
            "n_admissible_primes_at_this_weight": len(primes_w),
            "n_admissible_primes_first_seen_at_this_weight":
                sum(1 for p in primes_w if prime_min_w[p] == w),
            "cumulative_distinct_admissible_primes": len(all_primes),
            "largest_admissible_prime_at_this_weight": max(primes_w) if primes_w else None,
            "primes_at_this_weight": sorted(primes_w),
        })
        print(json.dumps({k: v for k, v in per_weight[-1].items()
                          if k != "primes_at_this_weight"}))

    # ---------------- pass 2: witnesses ----------------
    witness: dict[int, list] = {}
    for w in sorted(need):
        want = set(need[w])
        found: dict[int, list] = {}
        S = sign_matrix(w - 1)
        T = S.shape[0]
        sup_all = list(combinations(range(1, N), w - 1))
        per_block = max(1, 300000 // T)
        for s0 in range(0, len(sup_all), per_block):
            if not want:
                break
            blk = sup_all[s0:s0 + per_block]
            Sb = len(blk)
            d = np.zeros((Sb, T, N), dtype=np.int8)
            d[:, :, 0] = 1
            if w > 1:
                pos = np.array(blk, dtype=np.int64)
                rows = np.arange(Sb)[:, None, None]
                cols = np.arange(T)[None, :, None]
                d[rows, cols, pos[:, None, :]] = S[None, :, :]
            flat = d.reshape(Sb * T, N)
            vals = norm_batch_crt3(flat) if args.crt else norm_batch_int64(flat)
            hit = np.isin(vals, np.array(sorted(want), dtype=np.int64))
            for i in np.flatnonzero(hit):
                v = int(vals[i])
                if v in want:
                    found[v] = [int(x) for x in flat[i]]
                    want.discard(v)
        assert not want, (w, sorted(want)[:5])
        for v, fvec in found.items():
            chk = norm_bareiss(fvec)
            assert chk == v, (v, chk)
            for p in need[w][v]:
                witness[p] = fvec

    census = []
    for p in sorted(all_primes):
        v = prime_norm[p]
        fvec = witness[p]
        assert v % p == 0
        census.append({
            "q": p, "min_weight": prime_min_w[p],
            "witness_f": fvec,
            "Norm_f": str(v),
            "Norm_f_bareiss_recheck": str(norm_bareiss(fvec)),
            "cofactor": str(v // p),
            "q_mod_2N": p % twoN,
        })

    out = {
        "twoN": twoN, "N": N,
        "admissibility": "q prime, q = 1 mod %d" % twoN,
        "weights_covered": ws,
        "complete": ws == list(range(1, N + 1)),
        "n_admissible_primes_total": len(all_primes),
        "largest_admissible_prime": max(all_primes) if all_primes else None,
        "smallest_admissible_prime": min(all_primes) if all_primes else None,
        "per_weight": per_weight,
        "census": census,
    }
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({k: v for k, v in out.items()
                      if k not in ("census", "per_weight")}))


if __name__ == "__main__":
    main()
