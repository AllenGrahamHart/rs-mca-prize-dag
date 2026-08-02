#!/usr/bin/env python3
"""maxnorm(N, w | k) where k = min(w_even, w_odd) is the parity-split statistic.

k is an invariant of the affine support orbit: i -> u i + c with u odd maps
parity classes to parity classes (c even: fixes them; c odd: swaps them), so the
UNORDERED pair {w_e, w_o} -- hence k = min(w_e, w_o) -- is orbit-invariant.
k = 0 is exactly imprimitivity.

Tests the MONOTONICITY CLAIM:  k -> maxnorm(N, w | k) is non-increasing,
for 1 <= w <= N/2 - 1, and must FAIL at w = N/2 (the control).
"""
from __future__ import annotations
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/c1_norm_ladder/scripts")
from affine import affine_reps, masks_to_positions, sign_patterns, build_block
from norm_core import norm_batch_crt3

def table(N, w):
    reps = affine_reps(N, w)
    pos = masks_to_positions(reps, N, w)
    wodd = (pos % 2).sum(axis=1)
    k = np.minimum(wodd, w - wodd)
    S = sign_patterns(w - 1); T = S.shape[0]
    res = {}
    for kk in range(0, w//2 + 1):
        sel = k == kk
        if not sel.any():
            continue
        P = pos[sel]; best = -1; arg = None
        step = max(1, (1 << 17)//T)
        for s in range(0, P.shape[0], step):
            flat = build_block(P[s:s+step], S, N)
            v = norm_batch_crt3(flat)
            i = int(np.argmax(v))
            if int(v[i]) > best: best, arg = int(v[i]), [int(z) for z in flat[i]]
        res[str(kk)] = {"max": str(best), "argmax": arg, "n_orbits": int(sel.sum())}
    return res

if __name__ == "__main__":
    N, wlo, whi, outf = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    out = {}
    for w in range(wlo, whi+1):
        assert w ** (N//2) < 1152921504606846976
        r = table(N, w)
        out[str(w)] = r
        vals = [int(r[str(kk)]["max"]) for kk in range(0, w//2+1) if str(kk) in r]
        mono = all(vals[i] >= vals[i+1] for i in range(len(vals)-1))
        out[str(w)]["_monotone_decreasing_in_k"] = mono
        out[str(w)]["_values_by_k"] = [str(v) for v in vals]
        out[str(w)]["_argmax_k"] = int(np.argmax(vals))
        print(json.dumps({"N": N, "w": w, "vals_by_k": [str(v) for v in vals],
                          "monotone": mono, "argmax_k": int(np.argmax(vals))}), flush=True)
    json.dump(out, open(outf, "w"), indent=1)
