#!/usr/bin/env python3
"""Assemble the weight-stratified norm ladder over 2N = 8, 16, 32, 64 and decide F1.

Also:
  * merges any part-files produced by enum_weight.py --nparts,
  * verifies LEMMA A (the doubling embedding squares the norm) exhaustively at
    small ring dimension,
  * applies the sandwich corollary (Lemma A + Lemma B) to close, WITHOUT
    enumeration, every weight whose maximum saturates the AM-GM ceiling.

LEMMA A.  N = 2M.  iota : Z[y]/(y^M+1) -> Z[x]/(x^N+1), g(y) |-> g(x^2) is an
  injective ring map preserving the coefficient multiset (hence weight and
  ternariness), and Norm_N(iota g) = Norm_M(g)^2.
  Proof: iota g has even part g and odd part 0, so one step of the field-norm
  descent gives g^2 - y*0 = g^2, whence Norm_N(iota g) = Norm_M(g^2) = Norm_M(g)^2.
  COROLLARY A':  maxnorm(N, w) >= maxnorm(N/2, w)^2   for every w <= N/2.

LEMMA B.  maxnorm(N, w) <= w^(N/2).
  Proof: Norm(f) = prod_{j odd} f(zeta^j) = prod over the N/2 conjugate pairs of
  |f(zeta^j)|^2 >= 0, and sum_{j odd} |f(zeta^j)|^2 = N*||f||_2^2 = N*w
  (negacyclic Parseval).  AM-GM on the N numbers |f(zeta^j)|^2 gives
  Norm(f)^2 <= w^N.
  COROLLARY B'.  If maxnorm(M, w) = w^(M/2) then maxnorm(2M, w) = w^M
  (>= by A', <= by B).  Saturation propagates upward for free, forever.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
from fractions import Fraction
from itertools import product

import numpy as np

from norm_core import norm_descent_py


def merge_parts(d: str) -> None:
    keys = set()
    for f in glob.glob(os.path.join(d, "N*_w*_p*of*.json")):
        base = os.path.basename(f)
        keys.add(base.split("_p")[0])
    for k in sorted(keys):
        parts = sorted(glob.glob(os.path.join(d, k + "_p*of*.json")))
        recs = [json.load(open(p)) for p in parts]
        nparts = recs[0]["nparts"]
        assert len(recs) == nparts, (k, len(recs), nparts)
        tot = sum(r["n_polynomials_scanned"] for r in recs)
        assert tot == recs[0]["slice_size_full_weight"], (k, tot)
        best = max(recs, key=lambda r: int(r["max_norm"]))
        arrs = [np.load(os.path.join(d, os.path.basename(p)[:-5] + "_norms.npy"))
                for p in parts]
        uniq = np.unique(np.concatenate(arrs))
        out = dict(best)
        out.update({"part": "merged", "nparts": nparts,
                    "n_polynomials_scanned": tot,
                    "slice_size_expected": recs[0]["slice_size_full_weight"],
                    "n_distinct_norms": int(uniq.size),
                    "seconds": round(sum(r["seconds"] for r in recs), 2)})
        np.save(os.path.join(d, k + "_norms.npy"), uniq)
        with open(os.path.join(d, k + ".json"), "w") as fh:
            json.dump(out, fh, indent=1)
        print("merged", k, "->", out["max_norm"])


def load_max(d: str, N: int) -> dict[int, dict]:
    out = {}
    for w in range(1, N + 1):
        f = os.path.join(d, "N%02d_w%02d.json" % (N, w))
        if os.path.exists(f):
            out[w] = json.load(open(f))
    return out


def verify_lemma_A() -> dict:
    """Exhaustive check of Norm_{2M}(g(x^2)) = Norm_M(g)^2 for M = 2, 4, 8."""
    res = []
    for M in (2, 4, 8):
        bad = 0
        n = 0
        for g in product((-1, 0, 1), repeat=M):
            f = [0] * (2 * M)
            for i, c in enumerate(g):
                f[2 * i] = c
            n += 1
            if norm_descent_py(list(f)) != norm_descent_py(list(g)) ** 2:
                bad += 1
        res.append({"M": M, "checked": n, "violations": bad})
        assert bad == 0
    return res


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    R = args.root

    for sub in ("n16", "n32"):
        if os.path.isdir(os.path.join(R, sub)):
            merge_parts(os.path.join(R, sub))

    maxima: dict[int, dict[int, int]] = {}
    argmax: dict[int, dict[int, list]] = {}
    src: dict[int, dict[int, str]] = {}

    for twoN, path in ((8, "table_2N8.json"), (16, "table_2N16.json")):
        t = json.load(open(os.path.join(R, path)))
        maxima[twoN] = {r["w"]: int(r["max_norm"]) for r in t["table"]}
        argmax[twoN] = {r["w"]: r["argmax_f"] for r in t["table"]}
        src[twoN] = {r["w"]: "exhaustive" for r in t["table"]}

    for N, twoN in ((16, 32), (32, 64)):
        d = os.path.join(R, "n%d" % N)
        recs = load_max(d, N)
        maxima[twoN] = {w: int(r["max_norm"]) for w, r in recs.items()}
        argmax[twoN] = {w: r["argmax_f"] for w, r in recs.items()}
        src[twoN] = {w: "exhaustive" for w in recs}

    # ---- sandwich corollary B': close saturating weights at the next level up --
    proved = []
    for twoN in (16, 32, 64, 128):
        lo = twoN // 2
        if lo not in maxima:
            continue
        maxima.setdefault(twoN, {})
        for w, v in maxima[lo].items():
            M = lo // 2
            if v == w ** (M // 2) and w <= M:            # saturates at level M
                pred = w ** (M)                           # = w^((2M)/2)
                if w in maxima[twoN]:
                    assert maxima[twoN][w] == pred, (twoN, w, maxima[twoN][w], pred)
                else:
                    maxima[twoN][w] = pred
                    src.setdefault(twoN, {})[w] = "proved by Lemma A + Lemma B (sandwich)"
                    argmax.setdefault(twoN, {})[w] = None
                    proved.append({"twoN": twoN, "w": w, "max_norm": str(pred),
                                   "reason": "maxnorm(N/2,w) = w^(N/4) saturates AM-GM"})

    # ---------------------------- F1 test ------------------------------------
    f1 = []
    for twoN in (16, 32, 64):
        lo = twoN // 2
        M = lo // 2                      # ring dimension at the lower level
        for w in sorted(set(maxima.get(twoN, {})) & set(maxima.get(lo, {}))):
            if src[twoN].get(w, "").startswith("proved"):
                pass
            a = maxima[lo][w]
            b = maxima[twoN][w]
            f1.append({
                "step": "2N=%d -> 2N=%d" % (lo, twoN), "w": w,
                "max_lower": str(a), "predicted_upper": str(a * a),
                "observed_upper": str(b),
                "law_holds": b == a * a,
                "w_equals_lower_ring_dim": w == M,
                "ratio_observed_over_predicted":
                    str(Fraction(b, a * a)) if a else None,
                "source_upper": src[twoN].get(w, "exhaustive"),
            })

    # -------------------- exponential-scaling fit (exact) ---------------------
    scaling = []
    for w in sorted({w for t in maxima.values() for w in t}):
        pts = [(twoN // 2, maxima[twoN][w]) for twoN in sorted(maxima)
               if w in maxima[twoN]]
        c_from = {}
        for N, v in pts:
            # exact c_w = v^(4/N) when it is an exact integer power, else None
            c_from[N] = None
            if v > 0 and N % 4 == 0:
                r = round(v ** (4.0 / N))
                for cand in (r - 1, r, r + 1):
                    if cand > 0 and cand ** (N // 4) == v:
                        c_from[N] = cand
            elif v == 1:
                c_from[N] = 1
        # the substantive law: log max is linear in N through the origin
        base = None
        linear_from = None
        for N, v in pts:
            if base is None:
                base, linear_from = (N, v), N
        ok = []
        for N, v in pts:
            b_N, b_v = base
            ok.append({"N": N, "max": str(v),
                       "equals_base_power": v == b_v ** (N // b_N)
                       if N % b_N == 0 else None})
        scaling.append({
            "w": w,
            "points": [{"N": N, "twoN": 2 * N, "max_norm": str(v),
                        "amgm_ceiling": str(w ** (N // 2)),
                        "saturates": v == w ** (N // 2),
                        "c_w_as_integer_Nover4_root": c_from[N]} for N, v in pts],
            "linear_in_N_from_smallest_point": ok,
        })

    out = {
        "definitions": {
            "admissibility": "q prime with q = 1 (mod 2N)",
            "relation": "d in {-1,0,1}^N (N = 2N/2), weight w = #nonzero, "
                        "sum_i d_i omega^i = 0 mod q for omega of exact order 2N",
            "norm": "Norm(f) = Res(f, x^N+1) = det(mult-by-f on Z[x]/(x^N+1))",
            "symmetry_U": "{+- x^i}, order 2N, acts FREELY, preserves Norm exactly",
            "symmetry_G": "<U, x -> x^u for u in (Z/2N)^*>, order 2N*phi(2N)",
        },
        "lemma_A_exhaustive_check": verify_lemma_A(),
        "closed_without_enumeration_by_sandwich": proved,
        "ladder": {str(twoN): {str(w): str(v) for w, v in sorted(maxima[twoN].items())}
                   for twoN in sorted(maxima)},
        "argmax": {str(twoN): {str(w): argmax[twoN].get(w)
                               for w in sorted(maxima[twoN])}
                   for twoN in sorted(maxima)},
        "source": {str(twoN): {str(w): src[twoN].get(w, "exhaustive")
                               for w in sorted(maxima[twoN])}
                   for twoN in sorted(maxima)},
        "F1_doubling_law_tests": f1,
        "F1_verdict": ("FALSIFIED as stated" if any(not r["law_holds"] for r in f1)
                       else "survives"),
        "F1_failures": [r for r in f1 if not r["law_holds"]],
        "scaling_by_weight": scaling,
    }
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)

    print("\n=== ladder: max Norm(f) over ternary f of weight w ===")
    hdr = sorted(maxima)
    allw = sorted({w for t in maxima.values() for w in t})
    print("  w | " + " | ".join("2N=%-15d" % t for t in hdr))
    for w in allw:
        cells = []
        for t in hdr:
            v = maxima[t].get(w)
            mark = "*" if src[t].get(w, "").startswith("proved") else " "
            cells.append(("%s%s" % (v, mark)).ljust(18) if v is not None else "-".ljust(18))
        print("%3d | %s" % (w, " | ".join(cells)))
    print("  (* = proved by the Lemma A + Lemma B sandwich, not enumerated)")
    print("\n=== F1 ===", out["F1_verdict"])
    for r in f1:
        if not r["law_holds"]:
            print("  FAIL %s w=%d: predicted %s, observed %s (ratio %s), w == lower ring dim: %s"
                  % (r["step"], r["w"], r["predicted_upper"], r["observed_upper"],
                     r["ratio_observed_over_predicted"], r["w_equals_lower_ring_dim"]))
    print("  passes: %d / %d" % (sum(1 for r in f1 if r["law_holds"]), len(f1)))


if __name__ == "__main__":
    main()
