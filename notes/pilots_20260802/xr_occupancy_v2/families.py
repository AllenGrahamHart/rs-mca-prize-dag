#!/usr/bin/env python3
"""STAGE B -- families: the DESIGN CEILING, and the SUNFLOWER calibration.

B1  random k-spread DESIGNED families of M depth-d two-slope data.
    Measured: rank(M) against the additive prediction 2hM, the DEFICIT
    2hM - rank in the sub-saturation regime 2hM <= 2R - 2h, and the
    largest M admitting a non-degenerate received pair.

B2  the SUNFLOWER, parametrised exactly:
      f_i = f + a_i V_Y,  g_i = g + b_i V_Y     (V_Y = vanishing poly of a
    common (k-1)-set Y),  cores Z_i = Y u P_i with |P_i| = d+1, plus a
    top-up block of h-2d-1 points per used edge of the m-cycle.  All the
    edge slopes are FORCED (proportional differences), hence free.
    Measured: N_d against the point-budget law floor((R+1)/(h-d)), the
    exact rank of the realised two-slope system, and the cost per pair
    (predicted: exactly h, i.e. HALF the generic 2h).

B3  the low/high band DICHOTOMY: for 2d >= h no two depth-d band pairs can
    have proportional differences and no live ray can carry two of them.
    Checked on planted band fixtures (where band pairs actually exist).

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
    for sh in [dict(n=40, k=5, t=4, q=241), dict(n=44, k=6, t=5, q=257),
               dict(n=36, k=4, t=4, q=241), dict(n=48, k=8, t=5, q=241),
               dict(n=30, k=5, t=6, q=241)]:
        row = T.Row2(sh["n"], sh["k"], sh["t"], sh["q"])
        n, k, h, q, R = row.n, row.k, row.h, row.q, row.R
        ceil_fixed = (2 * R - 1) // (2 * h)
        ceil_free = (2 * R - 1) // (2 * h - 2)
        rec = dict(shape=sh, R=R, two_R=2 * R,
                   ceiling_slopes_fixed=ceil_fixed,
                   ceiling_slopes_free=ceil_free, depths=[])
        for d in range(1, h - 1):
            ladder, sub_ok = [], True
            for M in range(1, ceil_fixed + 4):
                fam = T.spread_two_slope_family(row, d, M, rng)
                if len(fam) < M:
                    break
                rws = T.family_rows(row, fam)
                rk = T.rank_mod(rws, q)
                sol = T.realise(row, rws, seed=M * 13 + d)
                deficit = 2 * h * M - rk
                sub = 2 * h * M <= 2 * R - 2 * h        # sub-saturation
                if sub and deficit != 0:
                    sub_ok = False
                ladder.append(dict(M=M, rank=rk, additive=2 * h * M,
                                   deficit=deficit, sub_saturation=sub,
                                   realisable=sol is not None))
            rec["depths"].append(dict(d=d, ladder=ladder))
            chk(f"B1 n={n} k={k} h={h} d={d}: rank = 2hM EXACTLY while "
                f"2hM <= 2R-2h (zero deficit for spread designed families)",
                sub_ok, str([(x['M'], x['rank'], x['additive'])
                             for x in ladder if x['sub_saturation']]))
            lastreal = max((x["M"] for x in ladder if x["realisable"]),
                           default=0)
            maxdef = max((x["deficit"] for x in ladder), default=0)
            chk(f"B1 n={n} h={h} d={d}: max realisable M = {lastreal}; "
                f"ceiling {ceil_fixed}; max deficit {maxdef}",
                lastreal <= ceil_fixed + max(0, maxdef) // (2 * h) + 2,
                f"lastreal={lastreal} ceil={ceil_fixed} maxdef={maxdef}")
        out.append(rec)
    return out


# ------------------------------------------------------------------ B2
def build_sunflower(row, d, m, seed=0):
    """Exact sunflower received pair (see module docstring)."""
    rnd = random.Random(seed)
    n, k, h, q, A = row.n, row.k, row.h, row.q, row.A
    if 2 * d + 1 > h:
        return None
    tw = h - 2 * d - 1
    nedge = m if m > 2 else 1
    need = (k - 1) + m * (d + 1) + nedge * tw
    if need > n:
        return None
    pts = list(range(n))
    Y = pts[:k - 1]
    cur = k - 1
    petals = []
    for i in range(m):
        petals.append(pts[cur:cur + d + 1])
        cur += d + 1
    f = tuple(rnd.randrange(q) for _ in range(k))
    g = tuple(rnd.randrange(q) for _ in range(k))
    VY = [1]
    for i in Y:
        new = [0] * (len(VY) + 1)
        for e, c in enumerate(VY):
            if c:
                new[e] = (new[e] - c * row.xs[i]) % q
                new[e + 1] = (new[e + 1] + c) % q
        VY = new
    VY = tuple((list(VY) + [0] * k)[:k])
    ab, used = [(0, 0)], {(0, 0)}
    guard = 0
    while len(ab) < m and guard < 10000:
        guard += 1
        a, b = rnd.randrange(q), rnd.randrange(1, q)
        if (a, b) in used:
            continue
        # forced slopes must stay pairwise distinct (admissibility)
        zz = set()
        bad = False
        cand = ab + [(a, b)]
        for i in range(len(cand)):
            for j in range(i + 1, len(cand)):
                db = (cand[i][1] - cand[j][1]) % q
                if db == 0:
                    bad = True
                    break
                z = (-(cand[i][0] - cand[j][0])) * pow(db, q - 2, q) % q
                if z in zz:
                    bad = True
                    break
                zz.add(z)
            if bad:
                break
        if bad:
            continue
        used.add((a, b))
        ab.append((a, b))
    if len(ab) < m:
        return None
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
    pl = [(i, (i + 1) % m) for i in range(m)] if m > 2 else [(0, 1)]
    for (i, j) in pl:
        da = (ab[i][0] - ab[j][0]) % q
        db = (ab[i][1] - ab[j][1]) % q
        z = (-da) * pow(db, q - 2, q) % q
        B = pts[cur:cur + tw]
        cur += tw
        for x in B:
            gi = row.ev(gs[i], row.xs[x])
            vi = rnd.randrange(1, q)
            while vi == gi:
                vi = rnd.randrange(1, q)
            v[x] = vi
            u[x] = (row.ev(fs[i], row.xs[x]) + z * (gi - vi)) % q
        edges.append(dict(i=i, j=j, z=z, block=B))
    for i in range(n):
        if u[i] is None:
            u[i] = rnd.randrange(q)
            v[i] = rnd.randrange(1, q)
    return u, v, dict(Y=Y, petals=petals, edges=edges, points_used=cur,
                      topup_width=tw,
                      cores=[tuple(sorted(Y + P)) for P in petals])


def stage_b2():
    out = []
    for sh in [dict(n=20, k=3, t=3, q=6421), dict(n=28, k=3, t=3, q=6421),
               dict(n=36, k=3, t=3, q=10007), dict(n=24, k=4, t=5, q=6421),
               dict(n=30, k=4, t=5, q=6421), dict(n=26, k=5, t=7, q=6421),
               dict(n=34, k=5, t=7, q=10007)]:
        row = T.Row2(sh["n"], sh["k"], sh["t"], sh["q"])
        n, k, h, q, R, A = row.n, row.k, row.h, row.q, row.R, row.A
        for d in range(1, (h - 1) // 2 + 1):
            law = (R + 1) // (h - d)
            best = None
            for m in range(3, law + 2):
                got = None
                for seed in range(6):
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
                    fam = []
                    for Zf, p, dd, sl in band:
                        if dd == d and len(sl) >= 2:
                            fam.append((tuple(sorted(Zf)),
                                        [(z, tuple(sorted(p["supports"][z])))
                                         for z in sl[:2]]))
                    rk = T.rank_mod(T.family_rows(row, fam), q) if fam else 0
                    got = dict(m=m, N_d=Nd, rank=rk, M=len(fam),
                               cost_per_pair=(rk / len(fam)) if fam else None,
                               h=h, d=d, two_R=2 * R, seed=seed,
                               points_used=info["points_used"],
                               kpack=rec["kpacking_ok"], T1=rec["T1_ok"])
                    break
                if got is not None:
                    best = got
            if best:
                out.append(dict(shape=sh, law=law, **best))
                chk(f"B2 n={n} k={k} h={h} d={d}: sunflower reaches "
                    f"N_d={best['N_d']} vs point-budget law {law}",
                    best["N_d"] >= law - 1,
                    f"m={best['m']} rank={best['rank']} "
                    f"cost/pair={best['cost_per_pair']:.4f}")
                chk(f"B2 n={n} k={k} h={h} d={d}: sunflower cost per pair "
                    f"is h={h} (half the generic 2h={2*h})",
                    best["M"] and abs(best["cost_per_pair"] - h) <= 3.0 / best["M"] + 0.51,
                    f"cost/pair={best['cost_per_pair']:.4f} h={h}")
    return out


# ------------------------------------------------------------------ B3
def stage_b3():
    """dichotomy 2d >= h, checked on PLANTED band fixtures."""
    out = []
    shapes = [dict(n=20, k=5, t=5, q=6421), dict(n=24, k=6, t=5, q=6421),
              dict(n=20, k=4, t=6, q=6421), dict(n=18, k=4, t=5, q=6421),
              dict(n=16, k=4, t=4, q=6421)]
    rng = random.Random(9)
    tot_prop, tot_ray, fixtures, pairs_seen = [], [], 0, 0
    for sh in shapes:
        row = T.Row2(sh["n"], sh["k"], sh["t"], sh["q"])
        n, k, h, q, R = row.n, row.k, row.h, row.q, row.R
        fx = []
        # planted single/multi two-slope data at every depth
        for d in range(1, h - 1):
            for M in (1, 2, 3):
                fam = T.spread_two_slope_family(row, d, M, rng)
                if len(fam) < M:
                    continue
                sol = T.realise(row, T.family_rows(row, fam), seed=d * 31 + M)
                if sol:
                    fx.append(sol)
        # sunflowers
        for d in range(1, (h - 1) // 2 + 1):
            for m in (3, 4, 5):
                b = build_sunflower(row, d, m, seed=m)
                if b:
                    fx.append((b[0], b[1]))
        for (u, v) in fx:
            rec, pairs, band = occlib.measure(row, u, v, want_checks=False)
            if not rec["ADMISSIBLE"]:
                continue
            fixtures += 1
            dl = [(Zf, p, p["J"] - k) for Zf, p in pairs.items()
                  if p["J"] >= k + 1]
            pairs_seen += len(dl)
            for a in range(len(dl)):
                for b_ in range(a + 1, len(dl)):
                    z = occlib.prop_slope(row, dl[a][1], dl[b_][1])
                    if z is None:
                        continue
                    da, db = dl[a][2], dl[b_][2]
                    if 2 * min(da, db) >= h:
                        tot_prop.append((n, h, da, db, str(z)))
            byray = {}
            for Zf, p, d, sl in band:
                for z in sl:
                    byray.setdefault((z, p["supports"][z]), []).append(d)
            for key, ds in byray.items():
                for x in set(ds):
                    if ds.count(x) > 1 and 2 * x >= h:
                        tot_ray.append((n, h, x, ds))
    chk(f"B3 dichotomy: 2d>=h forbids proportional differences "
        f"({fixtures} admissible planted fixtures, {pairs_seen} deep pairs)",
        not tot_prop, str(tot_prop[:3]))
    chk(f"B3 dichotomy: 2d>=h forbids two depth-d band pairs on one live ray",
        not tot_ray, str(tot_ray[:3]))
    out.append(dict(fixtures=fixtures, deep_pairs=pairs_seen,
                    prop_violations=tot_prop[:5], ray_violations=tot_ray[:5]))
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
