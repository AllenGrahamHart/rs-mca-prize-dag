#!/usr/bin/env python3
"""E3: UB -- an upper bound on RET that is UNIFORM over received words.

For every mixed floor-band candidate S let g = g^{(0)}(S) be its s=0 gamma
row (PREREG R1).  A degree-<k interpolant on S exists only if g . c = 0.
Hence for every word c

        RET(c)  <=  FILT(c)  <=  UB(c) := #{S : g(S) . c = 0}.

g does not depend on c, so ONE pass over the cell gives the histogram of g
over F_97^t, and UB(c) is then a sum over the hyperplane c^perp.  When
t <= 3 the legal word space has 96 or 9,216 projective points, so
`max_c UB(c)` is EXHAUSTIVE over every received word of the chart family --
not a search.  Any word with UB > 10*BOX/q is then exact-evaluated, which
settles F-w1 at that cell for ALL words.

usage: ub_scan.py N ELL LAYOUT [NWORDS]     (NWORDS used only when t >= 4)
"""
import itertools
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sweep_engine import (build, subsets, mixed_mask,               # noqa: E402
                          consec, geom5, mindeg_word)
from cf_cells import shells                                        # noqa: E402

P = int(os.environ.get("SWEEPQ", 97))
CAP = 1_000_000
OUT = os.path.join(HERE, "ub_results.jsonl")


def scan(n, ell, lay, chunk=600_000):
    c = build(n, P, ell, lay)
    p, tl, t, b = c.p, c.tl, c.t, c.b
    pw = (P ** np.arange(t)).astype(np.int64)
    dense = np.zeros(P ** t, dtype=np.int64) if t <= 3 else None
    keys_acc = np.zeros(0, dtype=np.int64)
    cnts_acc = np.zeros(0, dtype=np.int64)
    allzero, box = 0, 0
    t0 = time.time()
    for a in range(0, c.Lam + 1):
        Karr = subsets(c.core, a)
        NK = Karr.shape[0]
        RK = np.ones((NK, tl), dtype=np.int32)
        for i in range(a):
            RK = RK * c.DINV[c.P[:, None], Karr[:, i][None, :]].T % p
        RKf = RK.astype(np.float64)
        for nb in range(0, b + 1):
            for Bp in itertools.combinations(c.bgs, nb):
                Brest = [y for y in c.bgs if y not in Bp]
                prodbg = np.ones(tl, dtype=np.int32)
                for y in Brest:
                    prodbg = prodbg * c.DIFF[c.P, y] % p
                for om in range(1, min(tl, a + nb - b) + 1):
                    Oall = subsets(range(tl), om)
                    Oall = Oall[mixed_mask(Oall, t, ell, tl)]
                    NO = Oall.shape[0]
                    if NO == 0 or NK == 0:
                        continue
                    box += NK * NO
                    V0 = np.broadcast_to(c.A0 * prodbg % p, (NO, tl)).copy()
                    for i in range(om):
                        V0 = V0 * c.DIFF[c.P[:, None],
                                         c.P[Oall[:, i]][None, :]].T % p
                    V0f = V0.astype(np.float64)
                    step = max(1, int(chunk // max(NO, 1)))
                    for s0 in range(0, NK, step):
                        A = RKf[s0:s0 + step]
                        m = A.shape[0] * NO
                        key = np.zeros(m, dtype=np.int64)
                        Gcols = []
                        for i in range(t):
                            sl = slice(i * ell, (i + 1) * ell)
                            gi = ((A[:, sl] @ V0f[:, sl].T)
                                  .astype(np.int32) % p).reshape(-1)
                            key += gi.astype(np.int64) * int(pw[i])
                            if dense is None:
                                Gcols.append(gi)
                        if dense is not None:
                            dense += np.bincount(key, minlength=P ** t)
                            del key
                            continue
                        G = np.stack(Gcols)
                        del Gcols
                        nzc = (G != 0).any(axis=0)
                        allzero += int(m - nzc.sum())
                        if not nzc.any():
                            continue
                        Gs = G[:, nzc]
                        first = np.argmax(Gs != 0, axis=0)
                        lead = Gs[first, np.arange(Gs.shape[1])]
                        Gn = (Gs * c.INV[lead]) % p
                        k2 = (Gn.astype(np.int64) * pw[:, None]).sum(axis=0)
                        u, cn = np.unique(k2, return_counts=True)
                        keys_acc = np.concatenate([keys_acc, u])
                        cnts_acc = np.concatenate([cnts_acc, cn])
                        if len(keys_acc) > 1_200_000:
                            keys_acc, iv = np.unique(keys_acc,
                                                     return_inverse=True)
                            cnts_acc = np.bincount(
                                iv, weights=cnts_acc,
                                minlength=len(keys_acc)).astype(np.int64)
                            if len(keys_acc) > CAP:
                                return None, f"distinct gammas exceed {CAP:,}"
    if dense is None:
        keys_acc, iv = np.unique(keys_acc, return_inverse=True)
        cnts_acc = np.bincount(iv, weights=cnts_acc,
                               minlength=len(keys_acc)).astype(np.int64)
        D = len(keys_acc)
        Ghat = np.zeros((D, t), dtype=np.int64)
        kk = keys_acc.copy()
        for i in range(t):
            Ghat[:, i] = kk % P
            kk //= P
        payload = ("sparse", Ghat, cnts_acc, allzero)
    else:
        payload = ("dense", dense, None, int(dense[0]))
    return (c, box, payload, time.time() - t0), None


def ub_dense(dense, t, Cw):
    """Exhaustive UB via the hyperplane c^perp, for t = 2 or 3."""
    out = np.zeros(len(Cw), dtype=np.int64)
    inv = np.array([0] + [pow(i, P - 2, P) for i in range(1, P)])
    rng = np.arange(P, dtype=np.int64)
    for w, cvec in enumerate(Cw):
        i0 = int(inv[int(cvec[0]) % P])
        if t == 2:
            u0 = (-int(cvec[1]) * i0) % P
            key = (rng * u0 % P) * P + rng
        else:
            u0 = (-int(cvec[1]) * i0) % P
            v0 = (-int(cvec[2]) * i0) % P
            A = rng[:, None]
            B = rng[None, :]
            key = ((A * u0 + B * v0) % P) * (P * P) + A * P + B
        out[w] = int(dense[key.ravel()].sum())
    return out


def ub_sparse(Ghat, hist, allzero, Cw):
    W = Cw.shape[0]
    out = np.zeros(W, dtype=np.int64)
    hf = hist.astype(np.float64)
    D = len(Ghat)
    dstep = max(1, min(D, 300_000))
    wstep = max(1, int(4_000_000 // dstep))
    for w0 in range(0, W, wstep):
        Cf = Cw[w0:w0 + wstep].astype(np.float64).T
        acc = np.zeros(Cf.shape[1], dtype=np.float64)
        for s0 in range(0, D, dstep):
            M = Ghat[s0:s0 + dstep].astype(np.float64) @ Cf
            Z = (M.astype(np.int64) % P) == 0
            acc += (Z * hf[s0:s0 + dstep, None]).sum(axis=0)
        out[w0:w0 + wstep] = acc.astype(np.int64)
    return out + allzero


def legal_proj_words(t):
    """All projective words with every c_i in F_97^*  (c_0 normalised to 1)."""
    return np.array([[1] + list(tail) for tail in
                     itertools.product(range(1, P), repeat=t - 1)],
                    dtype=np.int64)


def main():
    n, ell, lay = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    nwords = int(sys.argv[4]) if len(sys.argv) > 4 else 5000
    got, err = scan(n, ell, lay)
    if err:
        print(f"n={n} ell={ell} L{lay}: SKIP -- {err}")
        return
    c, box, payload, scan_s = got
    t = c.t
    assert box == sum(shells(n, ell).values()), box
    exhaustive = (payload[0] == "dense")
    if exhaustive:
        Cw = legal_proj_words(t)
        tag = f"EXHAUSTIVE over all {len(Cw):,} legal projective words"
    else:
        rng = np.random.default_rng(20260807 + n * 100 + ell)
        Cw = rng.integers(1, P, size=(nwords, t))
        extra = [consec(t, P), geom5(t, P), mindeg_word(c)[0].tolist()]
        Cw = np.concatenate([np.array(extra, dtype=np.int64), Cw])
        tag = f"SEARCH over {len(Cw):,} words (NOT exhaustive)"
    t1 = time.time()
    if exhaustive:
        ub = ub_dense(payload[1], t, Cw)
    else:
        ub = ub_sparse(payload[1], payload[2], payload[3], Cw)
    ub_s = time.time() - t1
    thr = 10.0 * box / P
    over = np.flatnonzero(ub > thr)
    order = over[np.argsort(-ub[over])][:60]
    ordtop = np.argsort(-ub)[:12]
    i = int(np.argmax(ub))
    rec = {"n": n, "ell": ell, "layout": lay, "t": t, "b": c.b,
           "Lambda": c.Lam, "BOX": int(box), "allzero_gamma": int(payload[3]),
           "exhaustive": bool(exhaustive), "nwords": int(len(Cw)),
           "maxUB": int(ub.max()), "argmax_word": Cw[i].tolist(),
           "meanUB": float(ub.mean()), "minUB": int(ub.min()),
           "F_w1_threshold_10BOXoverq": thr,
           "maxUB_over_threshold": float(ub.max() / thr),
           "n_words_over_threshold": int(len(over)),
           "over_threshold_words": [Cw[j].tolist() for j in order],
           "top12_by_UB": [[Cw[j].tolist(), int(ub[j])] for j in ordtop],
           "scan_s": round(scan_s, 1), "ub_s": round(ub_s, 1)}
    with open(OUT, "a") as f:
        f.write(json.dumps(rec) + "\n")
    print(f"n={n} ell={ell} L{lay} t={t} b={c.b} Lam={c.Lam} BOX={box:,}")
    print(f"   {tag}; always-zero gammas {payload[3]:,}")
    print(f"   UB: min {ub.min():,} mean {ub.mean():,.1f} MAX {ub.max():,} "
          f"at c={Cw[i].tolist()}")
    print(f"   F-w1 threshold 10*BOX/q = {thr:,.1f}   "
          f"maxUB/threshold = {ub.max()/thr:.4f}")
    print(f"   words with UB > threshold: {len(over):,} of {len(Cw):,}"
          + (f"  -> exact-evaluate: {[Cw[j].tolist() for j in order[:6]]}"
             if len(over) else ("  -> NONE: F-w1 cannot fire at this cell "
                                "for ANY word" if exhaustive
                                else "  -> none on the search")))
    print(f"   scan {scan_s:.1f}s  ub {ub_s:.1f}s")


if __name__ == "__main__":
    main()
