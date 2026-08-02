#!/usr/bin/env python3
"""Independent validation that the stored representative sets COVER every
affine orbit of w-subsets of Z/N (which is all the maximisation needs).

Slow, independent implementation: for a random subset S, enumerate the FULL
affine orbit {u S + c} explicitly with python sets, and check that at least one
member is present in the stored rep array.  Also checks the uint64 full-mask.
"""
import json, os, random, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from affine import affine_reps

def orbit(S, N):
    out = set()
    for u in range(1, N, 2):
        for c in range(N):
            T = frozenset(((u*i + c) % N) for i in S)
            m = 0
            for i in T: m |= (1 << i)
            out.add(m)
    return out

if __name__ == "__main__":
    rng = random.Random(1234)
    rep = {"full_mask_check": {}, "coverage": {}}
    for N in (16, 32, 64):
        full_np = int((np.uint64(1) << np.uint64(N)) - np.uint64(1)) if N < 64 else None
        rep["full_mask_check"][str(N)] = {
            "python_full": (1 << N) - 1,
            "numpy_expr": int(((np.uint64(1) << np.uint64(N % 64)) - np.uint64(1))
                              if N < 64 else np.uint64(0xFFFFFFFFFFFFFFFF)),
        }
    for N, ws in ((16, [4, 6, 8]), (32, [4, 6, 8, 9]), (64, [3, 4, 5, 6])):
        for w in ws:
            path = None
            for cand in ("results/n%d/reps_N%02d_w%02d.npy" % (N, N, w),
                         "results/n%dbig/reps_N%02d_w%02d.npy" % (N, N, w),
                         "results/calib/reps_N%02d_w%02d.npy" % (N, w)):
                p = os.path.join(os.path.dirname(HERE), cand)
                if os.path.exists(p): path = p; break
            reps = np.load(path) if path else affine_reps(N, w)
            rset = set(int(v) for v in reps)
            miss = 0; tested = 0
            for _ in range(300):
                S = rng.sample(range(N), w)
                tested += 1
                if not (orbit(S, N) & rset): miss += 1
            rep["coverage"]["N%d_w%d" % (N, w)] = {
                "reps_file": path, "n_reps": len(rset),
                "random_subsets_tested": tested, "uncovered": miss,
                "COVERS_ALL": miss == 0}
    rep["ALL_COVERED"] = all(v["COVERS_ALL"] for v in rep["coverage"].values())
    print(json.dumps(rep, indent=1))
