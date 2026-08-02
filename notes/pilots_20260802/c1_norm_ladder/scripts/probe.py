#!/usr/bin/env python3
"""(a) certificates for the sandwich-proved entries, (b) a NON-EXHAUSTIVE probe at
2N = 64, w = 8 -- the weight at which the doubling law broke one level down.

(a) For every weight closed by the Lemma A + Lemma B sandwich we exhibit an
    explicit witness f attaining the proved maximum: the doubling embedding of
    the (exhaustively found) argmax one level down.  Its norm is recomputed by
    the independent Bareiss determinant.

(b) 2N = 64, w = 8 has C(31,7)*2^7 = 336,585,600 slice members -- out of budget.
    We run a steepest-ascent hill climb (neighbourhood: move one nonzero to any
    empty position with either sign, or flip one sign) from many random starts,
    plus uniform random sampling, and report the best norm found.  The climber is
    CALIBRATED on 2N = 32, w = 8, where the exhaustive answer 14760962 is known.
    A probe can only FALSIFY, never confirm; this is stated as such.
"""

from __future__ import annotations

import argparse
import json

import numpy as np

from norm_core import norm_bareiss, norm_batch_crt3, norm_descent_py


def embed(f):
    out = [0] * (2 * len(f))
    for i, c in enumerate(f):
        out[2 * i] = c
    return out


def neighbours(f: list[int]) -> np.ndarray:
    N = len(f)
    nz = [i for i, c in enumerate(f) if c]
    z = [i for i, c in enumerate(f) if not c]
    rows = []
    for i in nz:                       # sign flip
        g = list(f)
        g[i] = -g[i]
        rows.append(g)
    for i in nz:                       # move a nonzero to an empty slot
        for j in z:
            for s in (1, -1):
                g = list(f)
                g[i] = 0
                g[j] = s
                rows.append(g)
    return np.array(rows, dtype=np.int64)


def climb(N: int, w: int, restarts: int, rng: np.random.Generator, use_crt: bool):
    best = -1
    bestf = None
    for _ in range(restarts):
        pos = rng.choice(N, size=w, replace=False)
        f = [0] * N
        for p in pos:
            f[int(p)] = int(rng.choice([-1, 1]))
        cur = int(norm_batch_crt3(np.array([f], dtype=np.int64))[0])
        while True:
            nb = neighbours(f)
            vals = norm_batch_crt3(nb)
            i = int(np.argmax(vals))
            if int(vals[i]) > cur:
                cur = int(vals[i])
                f = [int(x) for x in nb[i]]
            else:
                break
        if cur > best:
            best = cur
            bestf = f
    return best, bestf


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--restarts32", type=int, default=300)
    ap.add_argument("--restarts64", type=int, default=1200)
    ap.add_argument("--random64", type=int, default=4000000)
    args = ap.parse_args()
    rng = np.random.default_rng(20260802)
    out: dict = {}

    # ---- (a) certificates for the sandwich-proved entries at 2N = 64 ----------
    # argmaxes found exhaustively at 2N = 32 (N = 16)
    arg32 = {
        1: [1] + [0] * 15,
        2: [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        3: [1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
        7: [1, 0, 1, 0, -1, 0, 1, 0, 1, 0, 1, 0, -1, 0, 0, 0],
    }
    certs = []
    for w, f in arg32.items():
        lo = norm_descent_py(f)
        assert lo == w ** 8, (w, lo)
        g = embed(f)
        hi = norm_descent_py(g)
        certs.append({
            "twoN": 64, "N": 32, "w": w,
            "witness_f": g,
            "Norm_f": str(hi),
            "Norm_f_bareiss_recheck": str(norm_bareiss(g)),
            "proved_maximum_w_pow_16": str(w ** 16),
            "attains_amgm_ceiling": hi == w ** 16,
            "source_argmax_at_2N32": f, "its_norm": str(lo),
        })
        assert hi == w ** 16 == norm_bareiss(g)
    out["sandwich_certificates_2N64"] = certs

    # ---- (b) calibrate the climber at 2N = 32, w = 8 (exhaustive answer known) -
    b32, f32 = climb(16, 8, args.restarts32, rng, True)
    out["calibration_2N32_w8"] = {
        "exhaustive_max": "14760962", "climber_best": str(b32),
        "climber_found_the_true_max": b32 == 14760962,
        "climber_best_f": f32, "restarts": args.restarts32,
        "bareiss_recheck": str(norm_bareiss(f32)),
    }

    # ---- (b) probe 2N = 64, w = 8 --------------------------------------------
    emb = embed([1, 1, -1, 0, -1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0])
    emb_norm = norm_descent_py(emb)
    assert emb_norm == 14760962 ** 2

    b64, f64 = climb(32, 8, args.restarts64, rng, True)

    # uniform random sampling on the weight-8 slice
    K = args.random64
    rbest = -1
    rbestf = None
    step = 200000
    for _ in range(0, K, step):
        d = np.zeros((step, 32), dtype=np.int64)
        for r in range(step):
            pass
        # vectorised: pick 8 positions per row by argsort of random keys
        keys = rng.random((step, 32))
        idx = np.argsort(keys, axis=1)[:, :8]
        sg = rng.integers(0, 2, size=(step, 8)) * 2 - 1
        np.put_along_axis(d, idx, sg, axis=1)
        vals = norm_batch_crt3(d)
        i = int(np.argmax(vals))
        if int(vals[i]) > rbest:
            rbest = int(vals[i])
            rbestf = [int(x) for x in d[i]]

    best = max(b64, rbest, emb_norm)
    out["probe_2N64_w8"] = {
        "EXHAUSTIVE": False,
        "slice_size_not_enumerated": 336585600,
        "law_prediction_maxnorm_2N32_w8_squared": str(14760962 ** 2),
        "embedding_witness_f": emb,
        "embedding_witness_norm": str(emb_norm),
        "embedding_witness_bareiss": str(norm_bareiss(emb)),
        "hill_climb_restarts": args.restarts64,
        "hill_climb_best": str(b64), "hill_climb_best_f": f64,
        "random_samples": K, "random_best": str(rbest), "random_best_f": rbestf,
        "best_found_overall": str(best),
        "beats_law_prediction": best > 14760962 ** 2,
        "amgm_ceiling_8_pow_16": str(8 ** 16),
        "verdict": ("PROBE FALSIFIES the law at 2N=64 w=8" if best > 14760962 ** 2
                    else "probe found nothing above the law prediction "
                         "(non-exhaustive: consistent with, does not prove, the law)"),
    }
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({"calibration": out["calibration_2N32_w8"]["climber_found_the_true_max"],
                      "climb_best": out["calibration_2N32_w8"]["climber_best"]}))
    print(json.dumps(out["probe_2N64_w8"], indent=1))


if __name__ == "__main__":
    main()
