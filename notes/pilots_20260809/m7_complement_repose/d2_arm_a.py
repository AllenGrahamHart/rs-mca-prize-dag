#!/usr/bin/env python3
"""D2 ARM A -- THE VERTEX-VS-HULL TEST at the FPC5 rate-half m4_t2 cells.

Registered at notes/pilots_20260809/m7_complement_repose/PREREG.md R2/R3.

The round-25a calibration measured the complement structure on EXHIBITED
VERTICES only.  Here we measure the FULL pairwise-overlap distribution over
ALL enumerated split members of our own guarded chart, and compare it with
the distribution restricted to a MAXIMUM core packing (= "the vertices").

REUSES, unchanged:
  notes/pilots_20260807/fpc5_diag/rh_m4t2_census.py   (exact F_q arithmetic,
                                                       build_flat)
  notes/pilots_20260807/mf_wall_adversary/rh_bucket.py (rref_kernel,
                                                       monic_chart,
                                                       enumerate_split,
                                                       maxpack)

Registered functionals (CATCH-19C): OVL_HIST_ALL, OVL_HIST_VERT,
KCORE_ALL, KCORE_VERT, UNION_ALL, UNION_VERT, DELTA, ANN_SIGMA, ANN_A,
ANN_ACO, AC_DIRECT, AC_COMP, AC_OLD.

Stdlib only.  Run via tools/ramguard local -- python3 ... from repo root.
"""
from __future__ import annotations

import json
import random
import sys
import time
from math import comb

ROOT = "/home/u2470931/smooth-read-solomin/prize"
sys.path.insert(0, ROOT + "/notes/pilots_20260807/fpc5_diag")
sys.path.insert(0, ROOT + "/notes/pilots_20260807/mf_wall_adversary")
from rh_m4t2_census import (build_flat, pgcd, pdegree,      # noqa: E402
                            peval, pmul, prem)
from rh_bucket import (rref_kernel, monic_chart,            # noqa: E402
                       enumerate_split, maxpack)


def pencil_stats(rootsets, d):
    """PENCIL_MAX (added measured functional, CATCH-19C): the largest
    number of members sharing a COMMON (d-1)-subset of roots -- i.e. the
    largest sunflower stratum, the exact object the common-core
    orientation of (PC3') is supposed to price."""
    from itertools import combinations
    cnt = {}
    for z in rootsets:
        for sub in combinations(sorted(z), d - 1):
            cnt[sub] = cnt.get(sub, 0) + 1
    best = max(cnt.values()) if cnt else 0
    return {"PENCIL_MAX": best,
            "n_cores_with_ge2": sum(1 for v in cnt.values() if v >= 2)}


# ------------------------------------------------------- the R1 instrument
def anticode(sigma, a, delta):
    """(PC3') in the annulus: sets of size `a` in a `sigma`-set, pairwise
    intersection <= a-delta.  Returns None when the exponent is out of
    range (instrument not applicable), else the floor of the ratio."""
    e = a - delta + 1
    if a <= 0 or e <= 0 or e > sigma:
        return None
    return comb(sigma, e) // comb(a, e)


def annulus(rootsets, ambient_size):
    """R1 parameters + the two orientations, for a family of equal-size
    root sets sitting inside an ambient set of size `ambient_size`."""
    S = [set(z) for z in rootsets]
    if len(S) < 2:
        return None
    j = len(S[0])
    K = set.intersection(*S)
    U = set.union(*S)
    kappa, sigma_ann = len(K), len(U) - len(K)
    a = j - kappa
    aco = sigma_ann - a
    ov = max(len(S[i] & S[k]) for i in range(len(S))
             for k in range(i + 1, len(S)))
    delta = j - ov
    return {
        "M_truth": len(S), "j": j, "kappa": kappa, "UNION": len(U),
        "ANN_SIGMA": sigma_ann, "ANN_A": a, "ANN_ACO": aco,
        "OVL_MAX": ov, "DELTA": delta,
        "sigma_lt_2a_COMPLEMENT_WINS": sigma_ann < 2 * a,
        "AC_DIRECT": anticode(sigma_ann, a, delta),
        "AC_COMP": anticode(sigma_ann, aco, delta),
        "AC_AMBIENT_no_annulus": anticode(ambient_size, j, delta),
    }


def hist(pairs):
    h = {}
    for v in pairs:
        h[v] = h.get(v, 0) + 1
    return h


def main():
    ell = int(sys.argv[1])
    q = int(sys.argv[2])
    nconfig = int(sys.argv[3])
    seed = int(sys.argv[4])
    outfile = sys.argv[5] if len(sys.argv) > 5 else ""
    tlimit = float(sys.argv[6]) if len(sys.argv) > 6 else 240.0
    filters = sys.argv[7] if len(sys.argv) > 7 else "split"

    d = 2 * ell - 3
    N = 5 * ell - 5                 # core budget |C| = k-1
    b = ell - 3
    rng = random.Random(seed)
    recs = []
    t0 = time.time()
    for ci in range(nconfig):
        if time.time() - t0 > tlimit:
            break
        pts = rng.sample(range(1, q), b + 4 * ell)
        bg = pts[:b]
        petals = [pts[b + i * ell:b + (i + 1) * ell] for i in range(4)]
        allowed = sorted(set(range(1, q)) - set(pts))
        labels = rng.sample(range(1, q), 4)
        pair = (0, 1)
        T, P, G, dd, L0, L1, L2, c1, c2 = build_flat(
            [], bg, petals, labels, pair, ell, q)
        basis = rref_kernel(T, d + 1, q)
        if len(basis) != ell - 1:
            continue
        v0, dirs = monic_chart(basis, d, q)
        if v0 is None:
            continue
        gflat = v0[:]
        for dv in dirs:
            gflat = pgcd(gflat, dv, q)
        if max(pdegree(gflat), 0) > 0:      # excluded by (GT2)
            continue
        found, swept = enumerate_split(v0, dirs, allowed, d, q)
        # FULL exact-contributor filters, copied verbatim in effect from
        # rh_bucket.run (primitivity gcd(F,W_F)=1 + untouched-petal
        # nonagreement).  `filters == "split"` reproduces the split-only
        # object; `full` is the actual FPC5 contributor object.
        if filters == "full":
            keep = {}
            for rs, coefs in found.items():
                F = v0[:]
                for i, c in enumerate(coefs):
                    if c:
                        F = [(u + c * w) % q for u, w in zip(F, dirs[i])]
                W = prem(pmul(F, G, q), P, q)
                if any(peval(W, x, q) == 0 for x in rs):
                    continue
                bad = False
                for u in (2, 3):
                    cu = labels[u]
                    for x in petals[u]:
                        if (peval(W, x, q) - cu * peval(F, x, q)) % q == 0:
                            bad = True
                            break
                    if bad:
                        break
                if bad:
                    continue
                keep[rs] = coefs
            found = keep
        rootsets = [set(z) for z in found]
        n_all = len(rootsets)
        if n_all < 2:
            continue

        # ---- OVL_HIST_ALL : the FULL pairwise distribution (the hull)
        ovl_all = []
        for i in range(n_all):
            Si = rootsets[i]
            for k in range(i + 1, n_all):
                ovl_all.append(len(Si & rootsets[k]))
        h_all = hist(ovl_all)
        K_all = set.intersection(*rootsets)
        U_all = set.union(*rootsets)

        # ---- the VERTICES : one maximum core packing
        mp, wit, exh = maxpack(list(found.keys()), N)
        vert = [set(z) for z in wit] if wit else []
        ovl_v = []
        for i in range(len(vert)):
            for k in range(i + 1, len(vert)):
                ovl_v.append(len(vert[i] & vert[k]))
        h_v = hist(ovl_v)

        rec = {
            "ell": ell, "q": q, "d": d, "N_core": N, "config": ci,
            "pool": len(allowed),
            "chart_points_total": q ** (ell - 2),
            "chart_points_swept": swept,
            "EXACT_full_chart": swept == q ** (ell - 2),
            "NSPLIT": n_all,
            "OVL_HIST_ALL": {str(k): v for k, v in sorted(h_all.items())},
            "OVL_MAX_ALL": max(ovl_all),
            "OVL_MEAN_ALL": round(sum(ovl_all) / len(ovl_all), 4),
            "FRAC_PAIRS_OVERLAP_0": round(h_all.get(0, 0) / len(ovl_all), 4),
            "KCORE_ALL": len(K_all), "UNION_ALL": len(U_all),
            "proved_cap_2s": 2 * (ell - 3),
            "sharpened_cap_ell_minus_3": ell - 3,
            "MAXPACK": mp, "maxpack_exhaustive": exh,
            "OVL_HIST_VERT": {str(k): v for k, v in sorted(h_v.items())},
            "OVL_MEAN_VERT": (round(sum(ovl_v) / len(ovl_v), 4)
                              if ovl_v else None),
            "OVL_MAX_VERT": max(ovl_v) if ovl_v else None,
            "KCORE_VERT": (len(set.intersection(*vert)) if len(vert) >= 2
                           else None),
            "UNION_VERT": (len(set.union(*vert)) if vert else None),
            "ANNULUS_HULL": annulus(rootsets, len(allowed)),
            "ANNULUS_VERT": annulus(vert, N) if len(vert) >= 2 else None,
            "PENCIL": pencil_stats(rootsets, d),
        }
        recs.append(rec)

    def agg(key):
        vals = [r[key] for r in recs if r.get(key) is not None]
        return {"min": min(vals), "max": max(vals),
                "mean": round(sum(vals) / len(vals), 4)} if vals else None

    merged_all, merged_v = {}, {}
    for r in recs:
        for k, v in r["OVL_HIST_ALL"].items():
            merged_all[k] = merged_all.get(k, 0) + v
        for k, v in r["OVL_HIST_VERT"].items():
            merged_v[k] = merged_v.get(k, 0) + v
    tot_all = sum(merged_all.values()) or 1
    tot_v = sum(merged_v.values()) or 1
    summary = {
        "mode": "d2_arm_a_vertex_vs_hull", "filters": filters,
        "ell": ell, "q": q, "d": d,
        "N_core": N, "seed": seed, "configs_used": len(recs),
        "all_exact_full_chart": all(r["EXACT_full_chart"] for r in recs),
        "all_maxpack_exhaustive": all(r["maxpack_exhaustive"] for r in recs),
        "NSPLIT": agg("NSPLIT"),
        "OVL_HIST_ALL_MERGED": dict(sorted(merged_all.items(),
                                           key=lambda t: int(t[0]))),
        "OVL_HIST_ALL_MERGED_FRAC": {k: round(v / tot_all, 5) for k, v in
                                     sorted(merged_all.items(),
                                            key=lambda t: int(t[0]))},
        "OVL_HIST_VERT_MERGED": dict(sorted(merged_v.items(),
                                            key=lambda t: int(t[0]))),
        "OVL_HIST_VERT_MERGED_FRAC": {k: round(v / tot_v, 5) for k, v in
                                      sorted(merged_v.items(),
                                             key=lambda t: int(t[0]))},
        "OVL_MEAN_ALL_over_configs": agg("OVL_MEAN_ALL"),
        "OVL_MEAN_VERT_over_configs": agg("OVL_MEAN_VERT"),
        "OVL_MAX_ALL": agg("OVL_MAX_ALL"),
        "KCORE_ALL": agg("KCORE_ALL"),
        "KCORE_VERT": agg("KCORE_VERT"),
        "UNION_ALL": agg("UNION_ALL"),
        "UNION_VERT": agg("UNION_VERT"),
        "MAXPACK": agg("MAXPACK"),
        "MAXPACK_hist": {},
        "PENCIL_MAX_hist": {},
        "configs_with_KCORE_ALL_positive":
            sum(1 for r in recs if r["KCORE_ALL"] > 0),
        "configs_with_COMPLEMENT_WINNING_hull":
            sum(1 for r in recs if r["ANNULUS_HULL"]
                and r["ANNULUS_HULL"]["sigma_lt_2a_COMPLEMENT_WINS"]),
        "configs_with_COMPLEMENT_WINNING_vert":
            sum(1 for r in recs if r["ANNULUS_VERT"]
                and r["ANNULUS_VERT"]["sigma_lt_2a_COMPLEMENT_WINS"]),
        "VERT_mean_gt_ALL_mean_count":
            sum(1 for r in recs if r["OVL_MEAN_VERT"] is not None
                and r["OVL_MEAN_VERT"] > r["OVL_MEAN_ALL"]),
        "elapsed_s": round(time.time() - t0, 1),
    }
    for r in recs:
        k = str(r["MAXPACK"])
        summary["MAXPACK_hist"][k] = summary["MAXPACK_hist"].get(k, 0) + 1
        k2 = str(r["PENCIL"]["PENCIL_MAX"])
        summary["PENCIL_MAX_hist"][k2] = summary["PENCIL_MAX_hist"].get(k2, 0) + 1
    if outfile:
        with open(outfile, "w") as fh:
            json.dump({"summary": summary, "recs": recs}, fh, indent=1)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
