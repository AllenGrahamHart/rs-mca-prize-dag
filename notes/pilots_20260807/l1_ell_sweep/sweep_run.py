#!/usr/bin/env python3
"""E2: one cell, one word-batch, per invocation (checkpointed via JSONL).

usage:  sweep_run.py N ELL LAYOUT SPEC [SPEC ...]
SPEC in {sched, mindeg, rand:A:B, ransac:TRIALS:TOP, full:A_CAP}
  full:A_CAP  = same cell but with the floor band relaxed to a <= A_CAP
                (A_CAP = -1 means no band at all) -- the PREREG P4 scope test.
Results append to results.jsonl in this directory.
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sweep_engine import (build, run, consec, geom5, mindeg_word,   # noqa: E402
                          subsets, mixed_mask, nullspace)
from cf_cells import shells, retpred                                # noqa: E402

P = int(os.environ.get("SWEEPQ", 97))
OUT = os.path.join(HERE, "results.jsonl")


def cell_seed(n, ell, lay):
    """PREREG R0.5 amendment (recorded): per-cell derived seed, because the
    cells run in separate ramguard invocations and a single stream would not
    be reproducible per cell."""
    return 20260807 + 1000 * n + 10 * ell + (0 if lay == "A" else 1)


def rand_words(c, lay, lo, hi):
    rng = np.random.default_rng(cell_seed(c.n, c.ell, lay))
    out = []
    for i in range(hi):
        w = rng.integers(1, P, size=c.t)
        while len(set(w.tolist())) != c.t:
            w = rng.integers(1, P, size=c.t)
        if i >= lo:
            out.append(w.tolist())
    return out


def sample_gamma(c, nsamp, rng):
    """Random r=1 candidates and their s=0 gamma rows (for RANSAC)."""
    p, tl, t, b, ell = c.p, c.tl, c.t, c.b, c.ell
    rows = []
    tries = 0
    while len(rows) < nsamp and tries < 60 * nsamp:
        tries += 1
        a = int(rng.integers(0, c.Lam + 1))
        nb = int(rng.integers(0, b + 1))
        om = a + nb - b
        if om < 1 or om > tl:
            continue
        K = rng.choice(len(c.core), size=a, replace=False)
        Kd = np.array(c.core, dtype=np.int64)[K]
        Bp = set(rng.choice(c.bgs, size=nb, replace=False).tolist()) if nb else set()
        O = np.sort(rng.choice(tl, size=om, replace=False))
        cnt = np.zeros(t, dtype=np.int64)
        for z in O:
            cnt[z // ell] += 1
        if not np.any((cnt > 0) & (cnt < ell)):
            continue
        v = c.A0.copy()
        for y in c.bgs:
            if y not in Bp:
                v = v * c.DIFF[c.P, y] % p
        for z in O:
            v = v * c.DIFF[c.P, c.P[z]] % p
        for u in Kd:
            v = v * c.DINV[c.P, u] % p
        g = np.zeros(t, dtype=np.int64)
        np.add.at(g, c.pid[c.P], v)
        rows.append((g % p).tolist())
    return np.array(rows, dtype=np.int64)


def ransac(c, trials, top, rng, nsamp=4000):
    G = sample_gamma(c, nsamp, rng)
    if len(G) < c.t:
        return []
    best = []
    seen = set()
    for _ in range(trials):
        idx = rng.choice(len(G), size=c.t - 1, replace=False)
        v = nullspace(G[idx].copy(), P)
        if v is None or not v.any():
            continue
        key = tuple((v * pow(int(next(x for x in v if x)), P - 2, P) % P).tolist())
        if key in seen:
            continue
        seen.add(key)
        cnt = int(np.count_nonzero((G @ v) % P == 0))
        best.append((cnt, v.tolist()))
    best.sort(key=lambda z: -z[0])
    return best[:top]


def main():
    n, ell, lay = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    specs = sys.argv[4:]
    c = build(n, P, ell, lay)
    N = shells(n, ell)
    box_cf, rp = sum(N.values()), retpred(n, N, P)
    rng = np.random.default_rng(cell_seed(n, ell, lay) + 7)
    names, words, extra = [], [], {}
    a_cap = None
    band = True
    for sp in specs:
        parts = sp.split(":")
        if parts[0] == "sched":
            names += ["consec", "geom5"]
            words += [consec(c.t, P), geom5(c.t, P)]
        elif parts[0] == "mindeg":
            md, deg = mindeg_word(c)
            names.append(f"mindeg(deg={deg})")
            words.append(md.tolist())
        elif parts[0] == "rand":
            lo, hi = int(parts[1]), int(parts[2])
            ws = rand_words(c, lay, lo, hi)
            names += [f"rand{lo+i}" for i in range(len(ws))]
            words += ws
        elif parts[0] == "ransac":
            tr, tp = int(parts[1]), int(parts[2])
            got = ransac(c, tr, tp, rng)
            names += [f"ransac(filt={cnt})" for cnt, _ in got]
            words += [w for _, w in got]
            extra["ransac_trials"] = tr
        elif parts[0] == "word":
            for wtxt in parts[1].split("/"):
                names.append(f"word({wtxt})")
                words.append([int(z) for z in wtxt.split(",")])
        elif parts[0] == "full":
            ac = int(parts[1])
            a_cap = None if ac < 0 else ac
            band = False
            names += ["consec", "geom5"]
            words += [consec(c.t, P), geom5(c.t, P)]
        else:
            raise SystemExit(f"bad spec {sp}")
    t0 = time.time()
    res, _ = run(c, words, band=band, a_cap=a_cap)
    wall = time.time() - t0
    rec = {"n": n, "ell": ell, "layout": lay, "t": c.t, "b": c.b,
           "Lambda": c.Lam, "C": c.C, "tl": c.tl, "q": P,
           "BOX_enum": res[0]["BOX"], "BOX_closed_form": box_cf,
           "N_k1": N.get(1, 0), "RETPRED": rp, "band": band, "a_cap": a_cap,
           "specs": specs, "wall_s": round(wall, 2), "words": [], **extra}
    for nm, w, d in zip(names, words, res):
        rec["words"].append({
            "name": nm, "c": list(map(int, w)), "FILT": d["FILT"],
            "RET": d["RET"],
            "hist_agr": {str(k): v for k, v in sorted(d["hist_agr"].items())},
            "hist_a": {str(k): v for k, v in sorted(d["hist_a"].items())},
            "EXC": (d["RET"] / rp) if rp else None,
            "RATIOBOX": d["RET"] / (res[0]["BOX"] / P),
            "RATIOSHELL": (d["RET"] / (N.get(1, 0) / P)) if N.get(1, 0) else None,
        })
    with open(OUT, "a") as f:
        f.write(json.dumps(rec) + "\n")
    print(f"n={n} ell={ell} L{lay} band={band} a_cap={a_cap} "
          f"BOX={rec['BOX_enum']:,} (cf {box_cf:,}) RETPRED={rp:,.1f} "
          f"wall={wall:.1f}s")
    for w in rec["words"]:
        print(f"   {w['name']:22s} FILT={w['FILT']:>10,} RET={w['RET']:>10,} "
              f"EXC={w['EXC']:.4f} RATIOBOX={w['RATIOBOX']:.4f} "
              f"RATIOSHELL={w['RATIOSHELL']:.4f}")


if __name__ == "__main__":
    main()
