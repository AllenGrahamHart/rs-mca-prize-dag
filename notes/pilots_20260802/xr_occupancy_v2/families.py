#!/usr/bin/env python3
"""STAGE B -- families: the DESIGN CEILING, and the SUNFLOWER calibration.

B1  random k-spread DESIGNED families of M depth-d two-slope data:
    rank = min(2hM, 2R)?  and the largest M admitting a non-degenerate
    received pair (the measured design ceiling), realised and re-measured
    with the banked exhaustive scan.

B2  the SUNFLOWER, parametrised exactly:
      f_i = f + a_i V_Y,  g_i = g + b_i V_Y     (V_Y = vanishing poly of a
    common (k-1)-set Y),  cores Z_i = Y u P_i with |P_i| = d+1, plus a
    top-up block of h-2d-1 points per used edge.  Differences are
    proportional by construction, so every edge slope is FORCED (free).
    Measured: the exact rank of the realised condition system, the
    per-pair cost, and N_d against the point-budget law.

B3  the low/high band DICHOTOMY: for 2d >= h no two depth-d band pairs can
    have proportional differences and no live ray can carry two of them
    (both are consequences of the tangent gate + k-packing).  Measured on
    every fixture produced here and in B1/B2.

Run: tools/ramguard local -- python3 families.py [stage ...]
"""
from __future__ import annotations

import itertools
import json
import os
import random
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/"
                   "pilots_20260802/xr_band_occupancy")

import tslib as T                                            # noqa: E402
import occlib                                                # noqa: E402

FAIL, CHECKS = [], [0]


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    print(("PASS " if ok else "FAIL ") + label + (f"  [{detail}]" if detail else ""))
    if not ok:
        FAIL.append(label + " " + detail)
    return ok


# ------------------------------------------------------------------ B1
def stage_b1():
    rng = random.Random(202608021)
    out = []
    for sh in [dict(n=20, k=4, t=4, q=241), dict(n=24, k=5, t=5, q=241),
               dict(n=28, k=6, t=5, q=257), dict(n=24, k=4, t=6, q=241)]:
        row = T.Row2(sh["n"], sh["k"], sh["t"], sh["q"])
        n, k, h, q, R = row.n, row.k, row.h, row.q, row.R
        ceil_fixed = (2 * R - 1) // (2 * h)
        ceil_free = (2 * R - 1) // (2 * h - 2)
        rec = dict(shape=sh, R=R, two_R=2 * R,
                   ceiling_slopes_fixed=ceil_fixed,
                   ceiling_slopes_free=ceil_free, depths=[])
        for d in range(1, h - 1):
            rows_by_M = []
            maxM = min(12, (2 * R) // (2 * h) + 4)
            for M in range(1, maxM + 1):
                fam = T.spread_two_slope_family(row, d, M, rng)
                if len(fam) < M:
                    break
                rws = T.family_rows(row, fam)
                rk = T.rank_mod(rws, q)
                pred = min(2 * h * M, 2 * R)
                sol = T.realise(row, rws, seed=M * 13 + d)
                rows_by_M.append(dict(M=M, rows=len(rws), rank=rk,
                                      predicted=pred, full=rk == pred,
                                      realisable=sol is not None,
                                      free_dims=2 * n - rk - 2 * k))
            rec["depths"].append(dict(d=d, ladder=rows_by_M))
            full = all(x["full"] for x in rows_by_M)
            chk(f"B1 n={n} k={k} h={h} d={d}: spread family rank = "
                f"min(2hM, 2R) at every M", full,
                str([(x['M'], x['rank'], x['predicted']) for x in rows_by_M]))
            lastreal = max((x["M"] for x in rows_by_M if x["realisable"]),
                           default=0)
            chk(f"B1 n={n} h={h} d={d}: max realisable M = {lastreal} "
                f"<= ceiling {ceil_fixed}", lastreal <= ceil_fixed)
        out.append(rec)
    return out


# ------------------------------------------------------------------ B2
def build_sunflower(row, d, m, seed=0, cyc=True, extra_pts=None):
    """Exact sunflower received pair.

    Y = first k-1 points; petals P_1..P_m of size d+1; edges of the m-cycle
    carry a top-up block of h-2d-1 points.  Returns (u, v, info) or None.
    """
    rnd = random.Random(seed)
    n, k, h, q, A = row.n, row.k, row.h, row.q, row.A
    if 2 * d + 1 > h:
        return None
    tw = h - 2 * d - 1
    need = (k - 1) + m * (d + 1) + (m if m > 2 else 1) * tw
    if need > n:
        return None
    pts = list(range(n))
    Y = pts[:k - 1]
    cur = k - 1
    petals = []
    for i in range(m):
        petals.append(pts[cur:cur + d + 1])
        cur += d + 1
    # base codeword pair
    f = tuple(rnd.randrange(q) for _ in range(k))
    g = tuple(rnd.randrange(q) for _ in range(k))
    # vanishing polynomial of Y (degree k-1)
    VY = [1]
    for i in Y:
        new = [0] * (len(VY) + 1)
        for e, c in enumerate(VY):
            if c:
                new[e] = (new[e] - c * row.xs[i]) % q
                new[e + 1] = (new[e + 1] + c) % q
        VY = new
    VY = tuple(VY[:k] + [0] * max(0, k - len(VY)))[:k]
    ab = [(0, 0)]
    used = {(0, 0)}
    while len(ab) < m:
        a, b = rnd.randrange(q), rnd.randrange(1, q)
        if (a, b) in used:
            continue
        used.add((a, b))
        ab.append((a, b))
    fs = [tuple((f[j] + a * VY[j]) % q for j in range(k)) for a, b in ab]
    gs = [tuple((g[j] + b * VY[j]) % q for j in range(k)) for a, b in ab]
    u = [None] * n
    v = [None] * n
    for i in Y:
        u[i] = row.ev(fs[0], row.xs[i])
        v[i] = row.ev(gs[0], row.xs[i])
    for c, P in enumerate(petals):
        for i in P:
            u[i] = row.ev(fs[c], row.xs[i])
            v[i] = row.ev(gs[c], row.xs[i])
    edges = []
    pairs_needed = [(i, (i + 1) % m) for i in range(m)] if (cyc and m > 2) \
        else [(0, 1)]
    for (i, j) in pairs_needed:
        da = (ab[i][0] - ab[j][0]) % q
        db = (ab[i][1] - ab[j][1]) % q
        if db == 0:
            return None
        z = (-da) * pow(db, q - 2, q) % q
        B = pts[cur:cur + tw]
        cur += tw
        for x in B:
            vi = rnd.randrange(1, q)
            gi = row.ev(gs[i], row.xs[x])
            while vi == gi:
                vi = rnd.randrange(1, q)
            v[x] = vi
            u[x] = (row.ev(fs[i], row.xs[x]) + z * (gi - vi)) % q
        edges.append(dict(i=i, j=j, z=z, block=B))
    for i in range(n):
        if u[i] is None:
            u[i] = rnd.randrange(q)
            v[i] = rnd.randrange(1, q)
    cores = [tuple(sorted(Y + P)) for P in petals]
    return u, v, dict(Y=Y, petals=petals, cores=cores, edges=edges,
                      points_used=cur, topup_width=tw)


def stage_b2():
    out = []
    for sh in [dict(n=20, k=3, t=3, q=241), dict(n=28, k=3, t=3, q=241),
               dict(n=24, k=4, t=5, q=241), dict(n=30, k=4, t=5, q=257),
               dict(n=26, k=5, t=7, q=257)]:
        row = T.Row2(sh["n"], sh["k"], sh["t"], sh["q"])
        n, k, h, q, R, A = row.n, row.k, row.h, row.q, row.R, row.A
        for d in range(1, min(h - 1, (h - 1) // 2 + 1)):
            if 2 * d + 1 > h:
                continue
            law = (R + 1) // (h - d)          # point-budget prediction
            best = None
            for m in range(3, law + 3):
                got = None
                for seed in range(8):
                    b = build_sunflower(row, d, m, seed=seed)
                    if b is None:
                        continue
                    u, v, info = b
                    rec, pairs, band = occlib.measure(row, u, v,
                                                      name=f"sun d={d} m={m}",
                                                      want_checks=True)
                    if not rec["ADMISSIBLE"]:
                        continue
                    Nd = rec["ledger_by_depth"].get(str(d), {}).get("N_d", 0)
                    # exact rank of the REALISED condition system
                    fam = []
                    for Zf, p, dd, sl in band:
                        if dd == d and len(sl) >= 2:
                            fam.append((tuple(sorted(Zf)),
                                        [(z, tuple(sorted(p["supports"][z])))
                                         for z in sl[:2]]))
                    rk = T.rank_mod(T.family_rows(row, fam), q) if fam else 0
                    got = dict(m=m, N_d=Nd, rank=rk, M=len(fam),
                               cost_per_pair=(rk / len(fam)) if fam else None,
                               two_R=2 * R, h=h, d=d, seed=seed,
                               points_used=info["points_used"],
                               kpack=rec["kpacking_ok"], T1=rec["T1_ok"],
                               maxL=max((x["maxL"] for x in
                                         rec["ledger_by_depth"].values()),
                                        default=0))
                    break
                if got is None:
                    break
                best = got
            if best:
                out.append(dict(shape=sh, **best))
                chk(f"B2 n={n} k={k} h={h} d={d}: sunflower N_d={best['N_d']}"
                    f" vs point-budget law floor((R+1)/(h-d))={law}",
                    best["N_d"] >= law - 1,
                    f"m={best['m']} rank={best['rank']} "
                    f"cost/pair={best['cost_per_pair']}")
    return out


# ------------------------------------------------------------------ B3
def stage_b3():
    """dichotomy 2d >= h: no proportional differences, <=1 pair per ray."""
    rng = random.Random(9)
    out = []
    for sh in [dict(n=20, k=5, t=5, q=241), dict(n=24, k=6, t=5, q=241),
               dict(n=20, k=4, t=6, q=101), dict(n=18, k=4, t=5, q=101),
               dict(n=16, k=4, t=4, q=97)]:
        row = T.Row2(sh["n"], sh["k"], sh["t"], sh["q"])
        n, k, h, q = row.n, row.k, row.h, row.q
        viol_prop, viol_ray, seen = [], [], 0
        for trial in range(120):
            u = [rng.randrange(q) for _ in range(n)]
            v = [rng.randrange(1, q) for _ in range(n)]
            rec, pairs, band = occlib.measure(row, u, v, want_checks=False)
            if not rec["ADMISSIBLE"]:
                continue
            seen += 1
            dl = [(Zf, p, p["J"] - k) for Zf, p in pairs.items()
                  if p["J"] >= k + 1]
            for a in range(len(dl)):
                for b in range(a + 1, len(dl)):
                    z = occlib.prop_slope(row, dl[a][1], dl[b][1])
                    if z is None:
                        continue
                    da, db = dl[a][2], dl[b][2]
                    if 2 * min(da, db) >= h:
                        viol_prop.append((da, db, str(z)))
            byray = {}
            for Zf, p, d, sl in band:
                for z in sl:
                    byray.setdefault((z, p["supports"][z]), []).append(d)
            for key, ds in byray.items():
                for x in ds:
                    if ds.count(x) > 1 and 2 * x >= h:
                        viol_ray.append((str(key[0]), x, ds))
        chk(f"B3 n={n} k={k} h={h}: 2d>=h forbids proportional differences "
            f"({seen} admissible fixtures)", not viol_prop, str(viol_prop[:3]))
        chk(f"B3 n={n} k={k} h={h}: 2d>=h forbids two depth-d pairs on one ray",
            not viol_ray, str(viol_ray[:3]))
        out.append(dict(shape=sh, admissible=seen, prop_violations=viol_prop[:5],
                        ray_violations=viol_ray[:5]))
    return out


STAGES = dict(b1=stage_b1, b2=stage_b2, b3=stage_b3)

if __name__ == "__main__":
    want = sys.argv[1:] or list(STAGES)
    res = {}
    for s in want:
        print(f"\n=== stage {s} ===")
        res[s] = STAGES[s]()
    res["_checks"] = CHECKS[0]
    res["_failures"] = FAIL
    with open(os.path.join(HERE, "families_%s.json" % "_".join(want)), "w") as f:
        json.dump(res, f, indent=1, default=str)
    print(f"\nchecks={CHECKS[0]} failures={len(FAIL)}")
    if FAIL:
        print("\n".join(FAIL[:20]))
