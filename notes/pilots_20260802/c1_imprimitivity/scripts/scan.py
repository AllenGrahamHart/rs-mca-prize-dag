#!/usr/bin/env python3
"""Exhaustive symmetry-reduced max-norm scan for ternary weight-w f in R_N.

Uses affine.affine_reps (Aff(N)-orbits of supports) x all sign patterns with the
least support index pinned to +1.  Norms by the exact 3-prime CRT field-norm
descent of the prior pilot (norm_core.norm_batch_crt3), valid while
0 <= Norm < 1.15e18; the AM-GM ceiling Norm <= w^(N/2) certifies validity
(checked at start-up).

Usage:
  tools/ramguard local -- python3 scripts/scan.py --N 32 --w 8 \
      --part 0 --nparts 8 --outdir results/n32
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/"
                   "pilots_20260802/c1_norm_ladder/scripts")

from affine import affine_reps, masks_to_positions, sign_patterns, build_block  # noqa: E402
from norm_core import norm_bareiss, norm_batch_crt3, norm_descent_py           # noqa: E402

CRT3_LIMIT = 1152921504606846976  # 1.15e18, safe bound for norm_batch_crt3


def reps_path(outdir: str, N: int, w: int) -> str:
    return os.path.join(outdir, "reps_N%02d_w%02d.npy" % (N, w))


def get_reps(N: int, w: int, outdir: str) -> np.ndarray:
    p = reps_path(outdir, N, w)
    if os.path.exists(p):
        return np.load(p)
    r = affine_reps(N, w)
    os.makedirs(outdir, exist_ok=True)
    np.save(p, r)
    return r


def scan(N: int, w: int, part: int, nparts: int, outdir: str,
         batch_target: int = 1 << 17, topk: int = 32,
         threshold: int | None = None) -> dict:
    ceiling = w ** (N // 2)
    assert ceiling < CRT3_LIMIT, "AM-GM ceiling %d exceeds CRT3 range" % ceiling
    t0 = time.time()
    reps = get_reps(N, w, outdir)
    n_reps = int(reps.size)
    lo = n_reps * part // nparts
    hi = n_reps * (part + 1) // nparts
    my = reps[lo:hi]
    S = sign_patterns(w - 1)
    T = S.shape[0]
    per = max(1, batch_target // T)
    best = -1
    arg = None
    n_scanned = 0
    top_vals: list[int] = []
    n_above = 0
    above: list[list[int]] = []
    for s0 in range(0, my.size, per):
        blk = my[s0:s0 + per]
        pos = masks_to_positions(blk, N, w)
        flat = build_block(pos, S, N)
        vals = norm_batch_crt3(flat)
        n_scanned += int(vals.size)
        i = int(np.argmax(vals))
        if int(vals[i]) > best:
            best = int(vals[i])
            arg = [int(x) for x in flat[i]]
        if threshold is not None:
            m = vals > threshold
            k = int(m.sum())
            if k:
                n_above += k
                for r in flat[m][:8]:
                    above.append([int(x) for x in r])
        if vals.size:
            kk = min(topk, vals.size)
            part_top = np.partition(vals, vals.size - kk)[vals.size - kk:]
            top_vals.extend(int(v) for v in part_top)
            top_vals = sorted(set(top_vals), reverse=True)[:topk]
    rec = {
        "N": N, "twoN": 2 * N, "w": w, "part": part, "nparts": nparts,
        "n_support_orbits_total": n_reps,
        "n_support_orbits_this_part": int(my.size),
        "n_polynomials_scanned": n_scanned,
        "expected_this_part": int(my.size) * T,
        "max_norm": str(best),
        "argmax_f": arg,
        "amgm_ceiling": str(ceiling),
        "saturates_amgm": best == ceiling,
        "top_values": [str(v) for v in top_vals],
        "seconds": round(time.time() - t0, 2),
    }
    if threshold is not None:
        rec["threshold"] = str(threshold)
        rec["n_above_threshold"] = n_above
        rec["above_samples"] = above[:8]
    if arg is not None:
        rec["argmax_bareiss"] = str(norm_bareiss(arg))
        rec["argmax_descent"] = str(norm_descent_py(arg))
        assert rec["argmax_bareiss"] == rec["max_norm"] == rec["argmax_descent"]
    assert rec["n_polynomials_scanned"] == rec["expected_this_part"]
    return rec


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, required=True)
    ap.add_argument("--w", type=int, required=True)
    ap.add_argument("--part", type=int, default=0)
    ap.add_argument("--nparts", type=int, default=1)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--threshold", type=str, default=None,
                    help="report every f with Norm strictly above this")
    ap.add_argument("--batch", type=int, default=1 << 17)
    args = ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)
    thr = int(args.threshold) if args.threshold else None
    rec = scan(args.N, args.w, args.part, args.nparts, args.outdir,
               batch_target=args.batch, threshold=thr)
    suffix = "" if args.nparts == 1 else "_p%03dof%03d" % (args.part, args.nparts)
    path = os.path.join(args.outdir, "N%02d_w%02d%s.json" % (args.N, args.w, suffix))
    with open(path, "w") as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps({k: v for k, v in rec.items() if k != "above_samples"}))


if __name__ == "__main__":
    main()
