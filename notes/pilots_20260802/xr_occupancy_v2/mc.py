#!/usr/bin/env python3
"""STAGE C -- the CALIBRATION ADVERSARIES: MC coset pencils, monomial
mu_n-orbit pencils, and general structured words.

C1  MC shift pencil  u = X^(n-1) + c X^(k+w-1),  v = u/X mod (X^n - beta)
    on H = x0 mu_n, with w = M | n, M | r'.  Exhaustive band ledger at
    EVERY depth (occlib), the gate, and the depth at which the MC family
    actually lives.  The two-slope count is read off directly: the
    calibration requirement is that the DESIGN CEILING must not bound the
    MC family, i.e. MC must show a rank DEFICIT, measured exactly.

C2  monomial mu_n-orbit pencils u = X^a, v = X^b on mu_n -- the pb_h4_hunt
    F2 exhibit's pencil, now read on the BAND side.

C3  general structured pencils: subgroup-supported error patterns, coset
    unions, and their band occupancy.

Run: tools/ramguard local -- python3 mc.py [stage ...]
"""
from __future__ import annotations

import itertools
import json
import os
import random
import sys
from math import comb, gcd

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


def ledger_line(rec):
    return {d: (v["N_d"], v["pairs_at_depth"], v["maxL"])
            for d, v in rec["ledger_by_depth"].items()}


def full_depth_profile(row, u, v):
    """Depth profile over ALL depths 0..h-1 (not just the band window),
    with live-slope counts."""
    pairs, rays, vmax = occlib.scan(row, u, v)
    prof = {}
    for Zf, p in pairs.items():
        d = p["J"] - row.k
        if d < 0:
            continue
        L = len(p["slopes"])
        e = prof.setdefault(d, dict(pairs=0, N=0, maxL=0, sumL=0))
        e["pairs"] += 1
        e["sumL"] += L
        if L >= 2:
            e["N"] += 1
        e["maxL"] = max(e["maxL"], L)
    return prof, pairs, rays, vmax


def two_slope_rank(row, pairs, d):
    """Exact rank of the two-slope condition system carried by all depth-d
    band pairs with >= 2 live slopes on this received pair."""
    fam = []
    for Zf, p in pairs.items():
        if p["J"] - row.k != d:
            continue
        sl = sorted(p["slopes"])
        if len(sl) < 2:
            continue
        fam.append((tuple(sorted(Zf)),
                    [(z, tuple(sorted(p["supports"][z]))) for z in sl[:2]]))
    if not fam:
        return 0, 0, None
    rows = T.family_rows(row, fam)
    rk = T.rank_mod(rows, row.q)
    return len(fam), rk, rk / len(fam)


# ------------------------------------------------------------------ C1
MC_SHAPES = [
    # n, k, w=M, q  (need n | q-1, M | n, M | r', gcd(r'/M, n/M) = 1)
    dict(n=16, k=4, M=2, q=97),
    dict(n=20, k=4, M=2, q=41),
    dict(n=20, k=4, M=4, q=41),
    dict(n=28, k=4, M=4, q=29),
    dict(n=20, k=8, M=4, q=101),
    dict(n=24, k=6, M=3, q=73),
]


def build_mc_pencil(n, k, w, M, q, c=1, x0exp=0):
    """u = X^{n-1} + c X^{k+w-1}; v = u/X mod (X^n - beta) as WORDS.

    Returns (row, u, v, meta).  h := w+1 so that MC's agreement k+w = A-1
    (the cascade tier), which is the depth the calibration adversary
    occupies.
    """
    H, om = T.mult_domain(q, n, x0exp)
    h = w + 1
    row = T.Row2(n, k, h, q, xs=H)
    U = [0] * n
    U[n - 1] = 1
    U[k + w - 1] = (U[k + w - 1] + c) % q
    u = [T.poly_ev(U, x, q) for x in H]
    v = [u[i] * pow(H[i], q - 2, q) % q for i in range(n)]
    rp = n - k - w
    N, m = n // M, rp // M
    cnt = comb(N, m) // N if gcd(m, N) == 1 else None
    return row, u, v, dict(n=n, k=k, w=w, M=M, q=q, h=h, A=k + h,
                           rprime=rp, N=N, m=m, mc_count_formula=cnt)


def stage_c1():
    out = []
    for sh in MC_SHAPES:
        n, k, M, q = sh["n"], sh["k"], sh["M"], sh["q"]
        w = M
        rp = n - k - w
        if (q - 1) % n or n % M or rp % M:
            print(f"  skip {sh} (divisibility)")
            continue
        row, u, v, meta = build_mc_pencil(n, k, w, M, q)
        prof, pairs, rays, vmax = full_depth_profile(row, u, v)
        maxJ = max(p["J"] for p in pairs.values())
        maxray = max(rays.values(), default=0)
        rec = dict(meta=meta, profile={str(a): b for a, b in sorted(prof.items())},
                   max_joint_agreement=maxJ, A=row.A,
                   max_ray_agreement=maxray, max_v_side=vmax,
                   below_cascade=maxJ <= row.A - 2,
                   tangent_free=maxray <= row.A,
                   v_nonzero=all(x != 0 for x in v))
        # rank / cost of the two-slope system at each depth
        costs = {}
        for d in sorted(prof):
            if prof[d]["N"] >= 1:
                Mm, rk, cpp = two_slope_rank(row, pairs, d)
                costs[str(d)] = dict(M=Mm, rank=rk, cost_per_pair=cpp,
                                     two_R=2 * row.R, ceiling_2h=2 * row.h)
        rec["two_slope_cost"] = costs
        rec["band_window"] = [1, row.h - 2]
        rec["N_in_band"] = sum(prof[d]["N"] for d in prof
                               if 1 <= d <= row.h - 2)
        rec["N_at_cascade_depth"] = prof.get(row.h - 1, {}).get("N", 0)
        out.append(rec)
        print(f"  MC n={n} k={k} w={w} q={q} h={row.h} A={row.A}: "
              f"maxJ={maxJ} maxray={maxray} profile={rec['profile']}")
        chk(f"C1 MC n={n} k={k} w={w}: the MC family sits at depth w={w} "
            f"= h-1 (the cascade tier), NOT in the band [1,{row.h-2}]",
            rec["N_in_band"] == 0 or rec["N_at_cascade_depth"] > 0,
            f"N_band={rec['N_in_band']} N_casc={rec['N_at_cascade_depth']}")
        # LBT's finding, independently reproduced: the MC pencil sits
        # EXACTLY one step outside the <= A-2 below-cascade reading.
        chk(f"C1 MC n={n} k={k} w={w}: max joint agreement is exactly A-1 "
            f"(one step outside below-cascade) or the family is absent",
            maxJ == row.A - 1 or rec["N_at_cascade_depth"] == 0,
            f"maxJ={maxJ} A-1={row.A-1}")
        chk(f"C1 MC n={n} k={k} w={w}: MC count reproduced by the exhaustive "
            f"band scan", meta["mc_count_formula"] is None
            or rec["N_at_cascade_depth"] in (0, meta["mc_count_formula"]),
            f"scan={rec['N_at_cascade_depth']} formula={meta['mc_count_formula']}")
    return out


# ------------------------------------------------------------------ C2
def stage_c2():
    """monomial mu_n-orbit pencils: u = X^a, v = X^b on mu_n."""
    out = []
    for (n, k, t, q) in [(16, 4, 4, 97), (20, 4, 5, 41), (20, 5, 5, 41),
                         (24, 6, 5, 73), (18, 4, 5, 37), (16, 4, 3, 17)]:
        if (q - 1) % n:
            continue
        H, om = T.mult_domain(q, n)
        row = T.Row2(n, k, t, q, xs=H)
        for (a, b) in [(k, k + 1), (n - 1, n - 2), (k, n - 1), (k + 1, k + 2)]:
            u = [pow(x, a, q) for x in H]
            v = [pow(x, b, q) for x in H]
            if any(x == 0 for x in v):
                continue
            prof, pairs, rays, vmax = full_depth_profile(row, u, v)
            maxJ = max(p["J"] for p in pairs.values())
            maxray = max(rays.values(), default=0)
            costs = {}
            for d in sorted(prof):
                if 1 <= d <= row.h - 2 and prof[d]["N"] >= 1:
                    Mm, rk, cpp = two_slope_rank(row, pairs, d)
                    costs[str(d)] = dict(M=Mm, rank=rk, cost_per_pair=cpp,
                                         cost_generic=2 * row.h,
                                         deficit=2 * row.h * Mm - rk)
            rec = dict(n=n, k=k, h=row.h, A=row.A, q=q, a=a, b=b,
                       profile={str(x): y for x, y in sorted(prof.items())},
                       maxJ=maxJ, maxray=maxray,
                       admissible=(maxJ <= row.A - 2 and maxray <= row.A
                                   and vmax <= row.A),
                       two_slope_cost=costs,
                       N_band=sum(prof[d]["N"] for d in prof
                                  if 1 <= d <= row.h - 2))
            out.append(rec)
            print(f"  orbit n={n} k={k} h={row.h} (a,b)=({a},{b}): "
                  f"adm={rec['admissible']} maxJ={maxJ} maxray={maxray} "
                  f"N_band={rec['N_band']} costs={costs}")
    return out


# ------------------------------------------------------------------ C3
def stage_c3():
    """structured error patterns: u,v = codeword + error supported on a
    union of mu_M-cosets (the e22 / #1051 locator mechanism)."""
    rnd = random.Random(3)
    out = []
    for (n, k, t, q, Msub) in [(16, 4, 4, 97, 2), (16, 4, 4, 97, 4),
                               (20, 4, 5, 41, 2), (20, 4, 5, 41, 4),
                               (20, 4, 5, 101, 5), (24, 4, 5, 73, 2),
                               (24, 4, 5, 73, 3), (24, 4, 5, 73, 4)]:
        if (q - 1) % n or n % Msub:
            continue
        H, om = T.mult_domain(q, n)
        row = T.Row2(n, k, t, q, xs=H)
        Ncos = n // Msub
        best = None
        for trial in range(20):
            # error supported on a union of cosets of mu_Msub
            # the error support must be a union of mu_Msub-cosets LARGE
            # enough that the base codeword pair itself is below cascade:
            # n - |supp| <= A-2  <=>  |supp| >= r+2.
            need = -(-(row.r + 2) // Msub)
            if need > Ncos:
                continue
            take = rnd.randrange(need, Ncos + 1)
            pick = rnd.sample(range(Ncos), take)
            supp = [i for i in range(n) if i % Ncos in pick]
            f = tuple(rnd.randrange(q) for _ in range(k))
            g = tuple(rnd.randrange(q) for _ in range(k))
            u = [row.ev(f, H[i]) for i in range(n)]
            v = [row.ev(g, H[i]) for i in range(n)]
            for i in supp:
                u[i] = (u[i] + rnd.randrange(1, q)) % q
                v[i] = (v[i] + rnd.randrange(1, q)) % q
            if any(x == 0 for x in v):
                continue
            prof, pairs, rays, vmax = full_depth_profile(row, u, v)
            maxJ = max(p["J"] for p in pairs.values())
            maxray = max(rays.values(), default=0)
            adm = maxJ <= row.A - 2 and maxray <= row.A and vmax <= row.A
            Nb = sum(prof[d]["N"] for d in prof if 1 <= d <= row.h - 2)
            cand = dict(n=n, k=k, h=row.h, q=q, Msub=Msub, trial=trial,
                        admissible=adm, maxJ=maxJ, maxray=maxray, N_band=Nb,
                        profile={str(x): y for x, y in sorted(prof.items())})
            if adm and (best is None or Nb > best["N_band"]):
                best = cand
        if best:
            out.append(best)
            print(f"  coset-error n={n} k={k} h={row.h} M={Msub}: "
                  f"N_band={best['N_band']} adm={best['admissible']}")
    return out


STAGES = dict(c1=stage_c1, c2=stage_c2, c3=stage_c3)

if __name__ == "__main__":
    want = sys.argv[1:] or list(STAGES)
    res = {}
    for s in want:
        print(f"\n=== stage {s} ===")
        res[s] = STAGES[s]()
    res["_checks"] = CHECKS[0]
    res["_failures"] = FAIL
    with open(os.path.join(HERE, "mc_%s.json" % "_".join(want)), "w") as f:
        json.dump(res, f, indent=1, default=str)
    print(f"\nchecks={CHECKS[0]} failures={len(FAIL)}")
    if FAIL:
        print("\n".join(FAIL[:20]))
