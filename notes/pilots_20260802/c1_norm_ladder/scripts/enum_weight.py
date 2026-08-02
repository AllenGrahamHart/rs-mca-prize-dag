#!/usr/bin/env python3
"""Weight-stratified exhaustive norm enumeration at 2N = 32 (N = 16) and beyond.

ENUMERATION REDUCTION (exact, not heuristic)
-------------------------------------------
Z[x]/(x^N+1) = Z[zeta_2N] is a domain, and U = {+- x^i} (order 2N) preserves
Norm exactly and acts freely on nonzero elements.  Every nonzero ternary f is
U-equivalent to exactly 2N ternary vectors, and exactly ONE of the 2N images
has its LOWEST nonzero coefficient equal to +1 at position 0... more precisely:
let i be minimal with d_i != 0; then x^(-i) f has nonzero constant term and,
after a sign, constant term +1.  Hence

    { Norm(f) : f ternary of weight w }  =  { Norm(f) : f ternary, w(f)=w, d_0=+1 }

and the maxima agree.  So we enumerate only the slice d_0 = +1, of size
C(N-1, w-1) * 2^(w-1)  (total over w: 3^(N-1)).

The claim "slice max = global max" is re-verified exhaustively at N = 4 and
N = 8 by scripts/slice_check.py.

Usage:
  tools/ramguard local -- python3 scripts/enum_weight.py --N 16 --w 11 --outdir results
"""

from __future__ import annotations

import argparse
import json
import os
import time
from itertools import combinations

import numpy as np

from norm_core import norm_bareiss, norm_batch_crt3, norm_batch_int64


def sign_matrix(k: int) -> np.ndarray:
    """(2^k, k) matrix of all +-1 patterns."""
    if k == 0:
        return np.zeros((1, 0), dtype=np.int8)
    idx = np.arange(1 << k, dtype=np.int64)
    bits = ((idx[:, None] >> np.arange(k)[None, :]) & 1).astype(np.int8)
    return (1 - 2 * bits).astype(np.int8)


def run_weight(N: int, w: int, use_crt: bool, block_target: int = 300000,
               part: int = 0, nparts: int = 1):
    sup_full = list(combinations(range(1, N), w - 1))
    lo = len(sup_full) * part // nparts
    hi = len(sup_full) * (part + 1) // nparts
    sup_all = sup_full[lo:hi]
    S = sign_matrix(w - 1)
    T = S.shape[0]
    per_block = max(1, block_target // T)
    best = -1
    arg = None
    uniq = np.zeros(0, dtype=np.int64)
    n_poly = 0
    n_zero = 0
    t0 = time.time()
    pending = []
    for s0 in range(0, len(sup_all), per_block):
        blk = sup_all[s0:s0 + per_block]
        Sb = len(blk)
        d = np.zeros((Sb, T, N), dtype=np.int8)
        d[:, :, 0] = 1
        if w > 1:
            pos = np.array(blk, dtype=np.int64)              # (Sb, w-1)
            rows = np.arange(Sb)[:, None, None]
            cols = np.arange(T)[None, :, None]
            d[rows, cols, pos[:, None, :]] = S[None, :, :]
        flat = d.reshape(Sb * T, N)
        vals = norm_batch_crt3(flat) if use_crt else norm_batch_int64(flat)
        n_poly += vals.size
        n_zero += int((vals == 0).sum())
        i = int(np.argmax(vals))
        if int(vals[i]) > best:
            best = int(vals[i])
            arg = [int(x) for x in flat[i]]
        pending.append(np.unique(vals))
        if len(pending) >= 24:
            uniq = np.unique(np.concatenate([uniq] + pending))
            pending = []
    if pending:
        uniq = np.unique(np.concatenate([uniq] + pending))
    return {
        "N": N, "twoN": 2 * N, "w": w,
        "part": part, "nparts": nparts,
        "slice_size_expected": len(sup_all) * T,
        "slice_size_full_weight": len(sup_full) * T,
        "n_polynomials_scanned": int(n_poly),
        "n_zero_norm": int(n_zero),
        "max_norm": str(best),
        "argmax_f": arg,
        "argmax_bareiss_check": str(norm_bareiss(arg)),
        "amgm_ceiling_w_pow_N_over_2": str(w ** (N // 2)),
        "max_saturates_amgm": best == w ** (N // 2),
        "n_distinct_norms": int(uniq.size),
        "seconds": round(time.time() - t0, 2),
        "arithmetic": "exact int64 field-norm descent" if not use_crt
        else "exact 2-prime CRT field-norm descent",
    }, uniq


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, required=True)
    ap.add_argument("--weights", required=True, help="e.g. 1-6 or 11")
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--crt", action="store_true")
    ap.add_argument("--part", type=int, default=0)
    ap.add_argument("--nparts", type=int, default=1)
    args = ap.parse_args()
    if "-" in args.weights:
        a, b = args.weights.split("-")
        ws = list(range(int(a), int(b) + 1))
    else:
        ws = [int(args.weights)]
    os.makedirs(args.outdir, exist_ok=True)
    for w in ws:
        rec, uniq = run_weight(args.N, w, args.crt, part=args.part, nparts=args.nparts)
        assert rec["argmax_bareiss_check"] == rec["max_norm"], rec
        assert rec["n_polynomials_scanned"] == rec["slice_size_expected"], rec
        suffix = "" if args.nparts == 1 else "_p%dof%d" % (args.part, args.nparts)
        base = os.path.join(args.outdir, "N%02d_w%02d%s" % (args.N, w, suffix))
        np.save(base + "_norms.npy", uniq)
        with open(base + ".json", "w") as fh:
            json.dump(rec, fh, indent=1)
        print(json.dumps(rec))


if __name__ == "__main__":
    main()
