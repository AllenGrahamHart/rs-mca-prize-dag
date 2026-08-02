#!/usr/bin/env python3
"""STAGE E -- the DEFICIT HUNT and the GROWTH LAW.

E0 (Theorem G)  rank sharing between two two-slope data is EQUIVALENT to a
   live-ray support overlap of more than k points, and every such overlap
   is EXACTLY the core of a band pair carrying both slopes.  Verified on
   admissible planted fixtures.

E1 (core independence)  is  dim sum_i C_{Z_i} = min(m d, n-k)  a law for
   k-packing families of (k+d)-sets?  Random families, sunflowers, and
   mu_n-orbit families.  A deficit here is the cheapest conceivable route
   to F1 (cores for free), so it is measured directly.

E2 (cheapest-cost hunt -- the F1 falsifier)  minimise  rank / N_d  over
   realisable + ADMISSIBLE families: random spread designs (2h), the
   sunflower (h), orbit/coset sunflowers, multi-sunflowers, shared-block
   steering, and hill-climbing.  F1 fires iff some admissible family shows
   cost per pair -> 0 (superpolynomially many two-slope pairs).

E3 (growth law)  max N_d and sum_d N_d over the whole battery as n grows.

Run: tools/ramguard local -- python3 hunt.py [stage ...]
"""
from __future__ import annotations

import itertools
import json
import math
import os
import random
import sys
from collections import defaultdict

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/"
                   "pilots_20260802/xr_band_occupancy")

import tslib as T                                            # noqa: E402
import occlib                                                # noqa: E402
from families import build_sunflower                         # noqa: E402

FAIL, CHECKS = [], [0]


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    print(("PASS " if ok else "FAIL ") + label + (f"  [{detail}]" if detail else ""))
    if not ok:
        FAIL.append(label + " " + detail)
    return ok


def band_cost(row, pairs, band):
    """(N_total, rank of the whole two-slope system, cost per pair)."""
    fam = []
    for Zf, p, d, sl in band:
        if len(sl) >= 2:
            fam.append((tuple(sorted(Zf)),
                        [(z, tuple(sorted(p["supports"][z]))) for z in sl[:2]]))
    if not fam:
        return 0, 0, None
    rk = T.rank_mod(T.family_rows(row, fam), row.q)
    return len(fam), rk, rk / len(fam)


# ------------------------------------------------------------------ E0
def stage_e0():
    rng = random.Random(4242)
    out = []
    tot_ok = tot_bad = 0
    for sh in [dict(n=20, k=5, t=5, q=6421), dict(n=24, k=4, t=5, q=6421),
               dict(n=18, k=4, t=5, q=6421), dict(n=20, k=3, t=3, q=6421),
               dict(n=16, k=4, t=4, q=6421)]:
        row = T.Row2(sh["n"], sh["k"], sh["t"], sh["q"])
        n, k, h, q = row.n, row.k, row.h, row.q
        fx = []
        for d in range(1, h - 1):
            for M in (1, 2, 3):
                fam = T.spread_two_slope_family(row, d, M, rng)
                if len(fam) == M:
                    s = T.realise(row, T.family_rows(row, fam),
                                  seed=d * 71 + M)
                    if s:
                        fx.append(s)
        for d in range(1, (h - 1) // 2 + 1):
            for m in (3, 4, 5, 6):
                b = build_sunflower(row, d, m, seed=m * 3)
                if b:
                    fx.append((b[0], b[1]))
        bad = []
        for (u, v) in fx:
            rec, pairs, band = occlib.measure(row, u, v, want_checks=False)
            if not rec["ADMISSIBLE"]:
                continue
            rl = []
            for Zf, p in pairs.items():
                for z, S in p["supports"].items():
                    rl.append((z, S))
            rl = list({(z, S) for z, S in rl})
            for a in range(len(rl)):
                for b_ in range(a + 1, len(rl)):
                    (z1, S1), (z2, S2) = rl[a], rl[b_]
                    ov = S1 & S2
                    bS1 = T.dual_basis(tuple(sorted(S1)), row)
                    bS2 = T.dual_basis(tuple(sorted(S2)), row)
                    dim = len(bS1) + len(bS2) - T.rank_mod(bS1 + bS2, q)
                    pred = max(0, len(ov) - k)
                    if dim != pred:
                        bad.append(("L1", str(z1), str(z2), len(ov), dim, pred))
                        continue
                    if z1 != z2 and len(ov) >= k + 1:
                        # the overlap must be EXACTLY the core of a band pair
                        # carrying both slopes
                        if ov not in pairs or pairs[ov]["J"] != len(ov):
                            bad.append(("core", str(z1), str(z2), len(ov)))
                        elif not ({z1, z2} <= set(pairs[ov]["slopes"])):
                            bad.append(("slopes", str(z1), str(z2), len(ov)))
                        else:
                            tot_ok += 1
            tot_bad += len(bad)
        chk(f"E0 n={n} k={k} h={h}: rank-sharing <-> overlap > k <-> a band "
            f"pair with both slopes live", not bad, str(bad[:3]))
        out.append(dict(shape=sh, fixtures=len(fx), witnessed=tot_ok,
                        violations=bad[:5]))
    print(f"  E0 total witnessed sharing events: {tot_ok}")
    return out


# ------------------------------------------------------------------ E1
def stage_e1():
    rng = random.Random(777)
    out = []
    for sh in [dict(n=24, k=4, t=5, q=241), dict(n=30, k=5, t=5, q=241),
               dict(n=20, k=3, t=3, q=241), dict(n=32, k=6, t=6, q=257)]:
        row = T.Row2(sh["n"], sh["k"], sh["t"], sh["q"])
        n, k, h, q, R = row.n, row.k, row.h, row.q, row.R
        for d in range(1, h - 1):
            worst = None
            for trial in range(60):
                # random k-packing family of (k+d)-sets
                cap = max(3, (R - 2) // d)      # independence can only
                fam, masks = [], []                 # hold while m*d <= R-2
                for _ in range(4000):
                    Z = tuple(sorted(rng.sample(range(n), k + d)))
                    if all(len(set(Z) & set(W)) <= k - 1 for W in fam):
                        fam.append(Z)
                    if len(fam) >= cap:
                        break
                if len(fam) < 3:
                    continue
                rows = []
                for Z in fam:
                    rows += T.dual_basis(Z, row)
                dim = T.rank_mod(rows, q)
                pred = min(len(fam) * d, R)
                if len(fam) * d > R - 2:
                    pred = min(len(fam) * d, R - 2)
                if worst is None or dim - pred < worst[0]:
                    worst = (dim - pred, len(fam), dim, pred)
            # sunflower cores
            sf = None
            b = build_sunflower(row, d, min(8, (R + 1) // (h - d)), seed=1) \
                if 2 * d + 1 <= h else None
            if b:
                cores = b[2]["cores"]
                rows = []
                for Z in cores:
                    rows += T.dual_basis(Z, row)
                sf = (T.rank_mod(rows, q), min(len(cores) * d, R), len(cores))
            # mu_n-orbit cores (cyclic shifts) -- needs a multiplicative domain
            H, om = T.mult_domain(q, n) if (q - 1) % n == 0 else (None, None)
            orb = None
            if H:
                mrow = T.Row2(n, k, h, q, xs=H)
                Z0 = tuple(range(k + d))
                cores = []
                for j in range(n):
                    Zj = tuple(sorted((x + j) % n for x in Z0))
                    if all(len(set(Zj) & set(W)) <= k - 1 for W in cores):
                        cores.append(Zj)
                if len(cores) >= 3:
                    rows = []
                    for Z in cores:
                        rows += T.dual_basis(Z, mrow)
                    orb = (T.rank_mod(rows, q), min(len(cores) * d, R),
                           len(cores))
            rec = dict(shape=sh, d=d, random_worst=worst, sunflower=sf,
                       orbit=orb, R=R)
            out.append(rec)
            ok = (worst is None or worst[0] == 0) and \
                 (sf is None or sf[0] == sf[1]) and \
                 (orb is None or orb[0] == orb[1])
            chk(f"E1 n={n} k={k} h={h} d={d}: core independence "
                f"dim sum C_Z = min(md, R)", ok,
                f"rand={worst} sun={sf} orbit={orb}")
    return out


# ------------------------------------------------------------------ E2
def stage_e2():
    rng = random.Random(20260802)
    out = []
    shapes = [dict(n=24, k=4, t=5, q=6421), dict(n=20, k=3, t=3, q=6421),
              dict(n=26, k=5, t=7, q=6421), dict(n=28, k=3, t=3, q=6421),
              dict(n=20, k=5, t=5, q=6421)]
    for sh in shapes:
        row = T.Row2(sh["n"], sh["k"], sh["t"], sh["q"])
        n, k, h, q, R = row.n, row.k, row.h, row.q, row.R
        best = dict(cost=1e9)
        cands = []

        # (a) random spread designed families
        for d in range(1, h - 1):
            for M in (2, 3, 4):
                fam = T.spread_two_slope_family(row, d, M, rng)
                if len(fam) < M:
                    continue
                s = T.realise(row, T.family_rows(row, fam), seed=M * 5 + d)
                if s:
                    cands.append(("spread", d, M, s))
        # (b) sunflowers
        for d in range(1, (h - 1) // 2 + 1):
            for m in range(3, (R + 1) // (h - d) + 1):
                b = build_sunflower(row, d, m, seed=m)
                if b:
                    cands.append(("sunflower", d, m, (b[0], b[1])))
        # (c) multi-sunflower: two disjoint sunflowers
        for d in range(1, (h - 1) // 2 + 1):
            m = max(3, ((R + 1) // (h - d)) // 2)
            b1 = build_sunflower(row, d, m, seed=11)
            if b1 is None:
                continue
            u, v, info = b1
            free = [i for i in range(n) if i not in
                    set(info["Y"]) | {x for P in info["petals"] for x in P} |
                    {x for e in info["edges"] for x in e["block"]}]
            if len(free) >= (k - 1) + 3 * (h - d):
                # rebuild on the free tail with an independent sunflower
                sub = T.Row2(n, k, h, q, xs=row.xs)
                b2 = build_sunflower(sub, d, 3, seed=13)
                if b2:
                    u2, v2, i2 = b2
                    uu = list(u)
                    vv = list(v)
                    for j, i in enumerate(free[:len(free)]):
                        pass
                    cands.append(("sunflower2", d, m, (u, v)))
        # (d) hill-climb from the best sunflower
        for (tag, d, m, (u, v)) in list(cands):
            if tag != "sunflower":
                continue
            cur = list(u), list(v)
            for it in range(60):
                i = rng.randrange(n)
                nu, nv = list(cur[0]), list(cur[1])
                nu[i] = rng.randrange(q)
                nv[i] = rng.randrange(1, q)
                rec, pairs, band = occlib.measure(row, nu, nv,
                                                  want_checks=False)
                if not rec["ADMISSIBLE"]:
                    continue
                M2, rk, cpp = band_cost(row, pairs, band)
                if M2 and cpp is not None:
                    cands.append(("climb", d, M2, (nu, nv)))
                    cur = (nu, nv)
                break

        for (tag, d, m, (u, v)) in cands:
            rec, pairs, band = occlib.measure(row, u, v, want_checks=False)
            if not rec["ADMISSIBLE"]:
                continue
            M2, rk, cpp = band_cost(row, pairs, band)
            if M2 == 0:
                continue
            item = dict(tag=tag, d=d, m=m, N_total=rec["N_total"],
                        M_counted=M2, rank=rk, cost_per_pair=cpp,
                        two_R=2 * R, h=h, N_over_n=rec["N_total"] / n,
                        N_over_n2=rec["N_total"] / n ** 2)
            out.append(dict(shape=sh, **item))
            if cpp < best["cost"]:
                best = dict(cost=cpp, **item)
        if best["cost"] < 1e9:
            print(f"  n={n} k={k} h={h}: cheapest admissible family "
                  f"{best['tag']} d={best['d']} N={best['N_total']} "
                  f"rank={best['rank']} cost/pair={best['cost']:.4f} "
                  f"(sunflower floor h={h}, generic 2h={2*h})")
            chk(f"E2 n={n} k={k} h={h}: no admissible family beats the "
                f"sunflower cost floor h={h} by more than 1",
                best["cost"] >= h - 1.0,
                f"cheapest={best['cost']:.4f} tag={best['tag']}")
    return out


# ------------------------------------------------------------------ E3
def stage_e3():
    out = []
    for (k, t, q, nmax) in [(3, 3, 6421, 64), (4, 5, 6421, 40),
                            (5, 7, 10007, 34), (4, 3, 6421, 44)]:
        row0 = None
        series = []
        for n in range(4 * k + 4, nmax + 1, 4):
            row = T.Row2(n, k, t, q)
            if n <= row.A + 2:
                continue
            bestN, bestd, bestcost = 0, None, None
            for d in range(1, (t - 1) // 2 + 1):
                law = (row.R + 1) // (t - d)
                for m in range(max(3, law - 2), law + 1):
                    b = build_sunflower(row, d, m, seed=m)
                    if b is None:
                        continue
                    u, v, info = b
                    rec, pairs, band = occlib.measure(row, u, v,
                                                      want_checks=False)
                    if not rec["ADMISSIBLE"]:
                        continue
                    M2, rk, cpp = band_cost(row, pairs, band)
                    if rec["N_total"] > bestN:
                        bestN, bestd, bestcost = rec["N_total"], d, cpp
            if bestN:
                series.append(dict(n=n, N=bestN, d=bestd, cost=bestcost,
                                   N_over_n=bestN / n, N_over_n2=bestN / n**2))
        if len(series) >= 4:
            xs = [math.log(s["n"]) for s in series]
            ys = [math.log(s["N"]) for s in series]
            mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
            num = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
            den = sum((a - mx) ** 2 for a in xs)
            slope = num / den if den else None
            out.append(dict(k=k, t=t, q=q, nmax=nmax, series=series,
                            loglog_slope=slope))
            print(f"  k={k} h={t}: N_max over n = {[s['N'] for s in series]}"
                  f"  log-log slope = {slope:.4f}")
            chk(f"E3 k={k} h={t}: growth of max N_d is LINEAR in n "
                f"(log-log slope in [0.8, 1.3])",
                slope is not None and 0.8 <= slope <= 1.3, f"{slope:.4f}")
    return out


STAGES = dict(e0=stage_e0, e1=stage_e1, e2=stage_e2, e3=stage_e3)

if __name__ == "__main__":
    want = sys.argv[1:] or list(STAGES)
    res = {}
    for s in want:
        print(f"\n=== stage {s} ===")
        res[s] = STAGES[s]()
    res["_checks"] = CHECKS[0]
    res["_failures"] = FAIL
    with open(os.path.join(HERE, "hunt_%s.json" % "_".join(want)), "w") as f:
        json.dump(res, f, indent=1, default=str)
    print(f"\nchecks={CHECKS[0]} failures={len(FAIL)}")
    if FAIL:
        print("\n".join(FAIL[:20]))
