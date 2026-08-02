#!/usr/bin/env python3
"""Exhaustive scan at large N (norms beyond int64 CRT range).

Two-stage, rigorous:
  stage 1  float64 log-norm  log Norm(f) = sum_{j odd mod 2N} log|f(zeta^j)|
           via a dense DFT matmul.  Cheap.
  stage 2  EXACT Python-int field-norm descent on a shortlist consisting of
             (i) every candidate whose float log-norm exceeds  log(target)-MARGIN
             (ii) every candidate with min_j |f(zeta^j)|^2 < TAU  (numerically
                  untrustworthy -- guards against catastrophic cancellation)
             (iii) the top-K by float score, so the argmax is always exact.
  Any candidate not in the shortlist has min_j |f|^2 >= TAU, hence a float
  log-norm accurate to well under MARGIN, hence is certainly below target.

Usage: python3 scan_big.py --N 64 --w 4 --target <int> --outdir results/n64
"""
from __future__ import annotations
import argparse, json, math, os, sys, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/c1_norm_ladder/scripts")
from affine import affine_reps, masks_to_positions, sign_patterns, build_block
from norm_core import norm_descent_py, norm_bareiss, norm_batch_crt3

MARGIN = 1e-3        # in log units; float error is < 1e-9 when min|f|^2 >= TAU
TAU = 1e-4


def dft_mat(N: int) -> tuple[np.ndarray, np.ndarray]:
    j = np.arange(1, 2 * N, 2)
    ang = np.pi * np.outer(np.arange(N), j) / N     # (N pos, N freq)
    return np.cos(ang), np.sin(ang)


def scan(N: int, w: int, target: int, part: int, nparts: int, outdir: str,
         batch: int = 1 << 15, topk: int = 24) -> dict:
    t0 = time.time()
    os.makedirs(outdir, exist_ok=True)
    rp = os.path.join(outdir, "reps_N%02d_w%02d.npy" % (N, w))
    reps = np.load(rp) if os.path.exists(rp) else affine_reps(N, w)
    if not os.path.exists(rp):
        np.save(rp, reps)
    n_reps = int(reps.size)
    lo, hi = n_reps * part // nparts, n_reps * (part + 1) // nparts
    my = reps[lo:hi]
    S = sign_patterns(w - 1); T = S.shape[0]
    C, Sm = dft_mat(N)
    logt = math.log(target) if target else -1e18
    per = max(1, batch // T)
    blocks: list[np.ndarray] = []
    n_scanned = 0
    n_suspicious = 0
    best_f, best_score = None, -1e18
    scores_top: list[float] = []
    for s0 in range(0, my.size, per):
        pos = masks_to_positions(my[s0:s0 + per], N, w)
        flat = build_block(pos, S, N)
        D = flat.astype(np.float64)
        re = D @ C
        im = D @ Sm
        P = re * re + im * im
        mn = P.min(axis=1)
        lg = 0.5 * np.log(P).sum(axis=1)
        n_scanned += lg.size
        sel = (lg > logt - MARGIN) | (mn < TAU)
        n_suspicious += int((mn < TAU).sum())
        i = int(np.argmax(lg))
        if lg[i] > best_score:
            best_score = float(lg[i]); best_f = [int(z) for z in flat[i]]
        if sel.any():
            blocks.append(flat[sel].copy())          # numpy blocks, not python rows
        kk = min(topk, lg.size)
        idx = np.argpartition(lg, lg.size - kk)[lg.size - kk:]
        blocks.append(flat[idx].copy())
        scores_top.extend(float(v) for v in lg[idx])
    # exact stage: batch CRT3 when the AM-GM ceiling is inside its range,
    # else python-int descent.  Every reported value is re-checked by a second
    # independent path (Bareiss) below.
    allrows = (np.concatenate(blocks) if blocks
               else np.zeros((0, N), dtype=np.int8))
    uniq_rows = sorted({tuple(int(z) for z in r) for r in np.unique(allrows, axis=0)})
    del allrows, blocks
    exact = {}
    if uniq_rows:
        if w ** (N // 2) < 1152921504606846976:
            A = np.array(uniq_rows, dtype=np.int8)
            for s0 in range(0, A.shape[0], 1 << 15):
                blk = A[s0:s0 + (1 << 15)]
                vv = norm_batch_crt3(blk)
                for rr, v in zip(blk, vv):
                    exact[tuple(int(z) for z in rr)] = int(v)
        else:
            for r in uniq_rows:
                exact[tuple(r)] = norm_descent_py(list(r))
    if best_f is not None and tuple(best_f) not in exact:
        exact[tuple(best_f)] = norm_descent_py(best_f)
    bestv, bestarg = -1, None
    for k, v in exact.items():
        if v > bestv:
            bestv, bestarg = v, list(k)
    above = [(list(k), str(v)) for k, v in exact.items() if v > target]
    rec = {"N": N, "twoN": 2 * N, "w": w, "part": part, "nparts": nparts,
           "n_support_orbits_total": n_reps,
           "n_support_orbits_this_part": int(my.size),
           "n_polynomials_scanned": n_scanned,
           "expected_this_part": int(my.size) * T,
           "n_exactly_evaluated": len(exact),
           "n_numerically_suspicious": n_suspicious,
           "target": str(target),
           "max_norm_exact": str(bestv), "argmax_f": bestarg,
           "argmax_bareiss": str(norm_bareiss(bestarg)) if bestarg else None,
           "n_strictly_above_target": len(above),
           "above_target": above[:5],
           "amgm_ceiling": str(w ** (N // 2)),
           "float_margin": MARGIN, "tau": TAU,
           "seconds": round(time.time() - t0, 2)}
    assert rec["n_polynomials_scanned"] == rec["expected_this_part"]
    assert rec["argmax_bareiss"] == rec["max_norm_exact"]
    return rec


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, required=True)
    ap.add_argument("--w", type=int, required=True)
    ap.add_argument("--target", type=str, required=True)
    ap.add_argument("--part", type=int, default=0)
    ap.add_argument("--nparts", type=int, default=1)
    ap.add_argument("--outdir", required=True)
    a = ap.parse_args()
    rec = scan(a.N, a.w, int(a.target), a.part, a.nparts, a.outdir)
    suf = "" if a.nparts == 1 else "_p%03dof%03d" % (a.part, a.nparts)
    json.dump(rec, open(os.path.join(a.outdir, "N%02d_w%02d%s.json" % (a.N, a.w, suf)), "w"), indent=1)
    print(json.dumps({k: v for k, v in rec.items() if k != "above_target"}))
