#!/usr/bin/env python3
"""Primitive vs imprimitive maxima, weight by weight, at N = 4, 8, 16 (and 32).

A ternary f is IMPRIMITIVE iff supp(f) lies in a coset of 2Z/N, i.e. all support
indices have the same parity; then f = (unit) * iota(g) and Norm_N(f) =
Norm_{N/2}(g)^2.  This property is invariant under the affine support group
(i -> u i + c, u odd), so it is a property of the orbit representative.
"""
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/c1_norm_ladder/scripts")
from affine import affine_reps, masks_to_positions, sign_patterns, build_block
from norm_core import norm_batch_crt3

def row(N, w, outdir):
    reps = affine_reps(N, w)
    pos = masks_to_positions(reps, N, w)
    imp = (pos % 2).max(axis=1) == (pos % 2).min(axis=1)   # all same parity
    S = sign_patterns(w - 1)
    T = S.shape[0]
    out = {}
    for name, sel in (("imprimitive", imp), ("primitive", ~imp)):
        if sel.sum() == 0:
            out[name] = None
            continue
        best, arg = -1, None
        P = pos[sel]
        step = max(1, (1 << 17) // T)
        for s in range(0, P.shape[0], step):
            flat = build_block(P[s:s+step], S, N)
            v = norm_batch_crt3(flat)
            i = int(np.argmax(v))
            if int(v[i]) > best:
                best, arg = int(v[i]), [int(z) for z in flat[i]]
        out[name] = {"max": str(best), "argmax": arg, "n_orbits": int(sel.sum())}
    return out

if __name__ == "__main__":
    # args: N w_lo w_hi outfile
    N, wlo, whi, outf = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    res = {}
    for w in range(wlo, whi + 1):
        assert w ** (N // 2) < 1152921504606846976
        res[str(w)] = row(N, w, None)
        print(json.dumps({"w": w, **{k: (v["max"] if v else None) for k, v in res[str(w)].items()}}), flush=True)
    json.dump(res, open(outf, "w"), indent=1)
