#!/usr/bin/env python3
"""REFUTATION SEARCH for the t-petal overlap-cap lemma at t >= 4.

Registered in notes/pilots_20260808/t_petal_lemma/PREREG.md, section R2.

THE LEMMA UNDER ATTACK.  Let q be prime, let P_1..P_t be pairwise
disjoint ell-subsets of F_q^*, L_i = prod_{x in P_i}(X-x), let
c_1..c_t in F_q be distinct labels, and let the core C be disjoint from
every petal.  Put

    V = {(F,W) : deg F, deg W <= d,  L_i | (W - c_i F), i = 1..t},
    e = 2d + 1 - t*ell.

A MEMBER of the cell is a pair (F,W) in V with F monic of degree
exactly d, split with d distinct roots Z(F) inside C, and
gcd(F,W) = 1.  The lemma claims that for two DISTINCT members of the
SAME cell,

    |Z(F) cap Z(F')| <= e - 1.

ESCAPE TEST (binding, registered before any run): a pair of distinct
members of one cell with |Z(F) cap Z(F')| >= e refutes the lemma.

POWER CONTROL: the same searcher is run on three deliberately BROKEN
arms (BRK-PRIM / BRK-DISJ / BRK-LABEL).  If no broken arm ever
produces a violation, the search is reported as HAVING NO POWER
rather than as confirming the lemma.

Registered functionals (CATCH-19C): NMEM, MAXOVL, CAP=e-1,
SLACK=CAP-MAXOVL, DIMV, DIVOK, DEGCOF, NJOHN.

Machinery REUSED from the coordinator-replayed round-23 pilots:
  notes/pilots_20260807/fpc5_diag/rh_m4t2_census.py  (exact F_q poly
      arithmetic: pmul, pgcd, pdegree, prem, peval, locator)
  notes/pilots_20260807/mf_wall_adversary/rh_bucket.py  (rref_kernel,
      and the last-coordinate bucketing trick of enumerate_split,
      here generalised from the t=2 F-chart to the full (F,W) chart)

Stdlib only.  Run via tools/ramguard.
"""
from __future__ import annotations

import json
import random
import sys
import time
from itertools import product

ROOT = "/home/u2470931/smooth-read-solomin/prize"
sys.path.insert(0, ROOT + "/notes/pilots_20260807/fpc5_diag")
sys.path.insert(0, ROOT + "/notes/pilots_20260807/mf_wall_adversary")

from rh_m4t2_census import (  # noqa: E402
    locator, pdegree, peval, pgcd, pmul, prem,
)
from rh_bucket import rref_kernel  # noqa: E402


# ------------------------------------------------------------- the slice V
def slice_rows(petals, labels, d, q):
    """Linear conditions W(x) - c_i F(x) = 0 for x in petal i.

    Unknown vector layout: columns 0..d are F's coefficients (low to
    high), columns d+1..2d+1 are W's.  L_i is squarefree, so
    L_i | (W - c_i F) is equivalent to vanishing at each point of P_i.
    """
    rows = []
    for i, pet in enumerate(petals):
        c = labels[i]
        for x in pet:
            row = [0] * (2 * d + 2)
            xp = 1
            for j in range(d + 1):
                row[j] = (-c * xp) % q
                row[d + 1 + j] = xp
                xp = xp * x % q
            rows.append(row)
    return rows


def monic_chart_at(basis, idx, q):
    """Affine chart of {v in span(basis) : v[idx] = 1}."""
    lead = [v[idx] for v in basis]
    nz = [i for i, c in enumerate(lead) if c]
    if not nz:
        return None, None
    i0 = nz[0]
    inv = pow(lead[i0], q - 2, q)
    v0 = [c * inv % q for c in basis[i0]]
    dirs = []
    for i, v in enumerate(basis):
        if i == i0:
            continue
        f = lead[i]
        dirs.append([(a - f * c) % q for a, c in zip(v, v0)])
    return v0, dirs


def enumerate_members(v0, dirs, core, d, q, work_cap):
    """EXACT sweep of the monic chart for members split on `core`.

    Last-coordinate bucketing (round-23 trick): the sweep costs
    q^(r-1)*|core| instead of q^r*|core|, r = len(dirs).  Returns
    (members, swept, exhaustive) where members maps a root set to the
    full (F|W) coefficient vector.
    """
    r = len(dirs)
    e0 = {x: peval(v0[:d + 1], x, q) for x in core}
    ev = [{x: peval(dv[:d + 1], x, q) for x in core} for dv in dirs]

    def build(coefs):
        v = v0[:]
        for i, c in enumerate(coefs):
            if c:
                v = [(a + c * b) % q for a, b in zip(v, dirs[i])]
        return v

    if r == 0:
        roots = [x for x in core if e0[x] == 0]
        out = {frozenset(roots): build(())} if len(roots) == d else {}
        return out, 1, True
    total = q ** (r - 1)
    if total > work_cap:
        return {}, 0, False
    last = ev[-1]
    invlast = {x: (pow(last[x], q - 2, q) if last[x] else 0) for x in core}
    found = {}
    swept = 0
    for prefix in product(range(q), repeat=r - 1):
        swept += q
        acc = {}
        for x in core:
            v = e0[x]
            for i, c in enumerate(prefix):
                if c:
                    v += c * ev[i][x]
            acc[x] = v % q
        z0 = [x for x in core if last[x] == 0 and acc[x] == 0]
        nz0 = len(z0)
        if nz0 > d:
            continue
        if nz0 == d:
            found.setdefault(frozenset(z0), build(prefix + (0,)))
        buckets = {}
        for x in core:
            if last[x]:
                cv = (-acc[x] * invlast[x]) % q
                buckets.setdefault(cv, []).append(x)
        need = d - nz0
        if need <= 0:
            continue
        for cv, xs in buckets.items():
            if len(xs) == need:
                found.setdefault(frozenset(xs + z0), build(prefix + (cv,)))
    return found, swept, True


def members_of(petals, labels, core, d, q, want_prim, work_cap):
    """Full member list of one cell.  Returns (members, DIMV, class)."""
    rows = slice_rows(petals, labels, d, q)
    basis = rref_kernel(rows, 2 * d + 2, q)
    dimv = len(basis)
    v0, dirs = monic_chart_at(basis, d, q)
    if v0 is None:
        return [], dimv, "EMPTY"
    found, swept, exact = enumerate_members(v0, dirs, core, d, q, work_cap)
    if not exact:
        return [], dimv, "CLASS-S(skipped: over work cap)"
    out = []
    for rs, vec in found.items():
        f = vec[:d + 1]
        w = vec[d + 1:]
        assert pdegree(f) == d and f[d] == 1
        if want_prim and pdegree(pgcd(f, w, q)) != 0:
            continue
        out.append((f, w, rs))
    return out, dimv, "CLASS-E" if len(dirs) == 0 else "CLASS-B"


# ------------------------------------------------------------- the analysis
def analyse(members, lam, d, q, cap):
    """MAXOVL / DIVOK / DEGCOF over all distinct member pairs."""
    maxovl = -1
    degcof = -1
    divok = 1
    worst = None
    same_rootset_diff_w = 0
    m = len(members)
    for i in range(m):
        f1, w1, z1 = members[i]
        for j in range(i + 1, m):
            f2, w2, z2 = members[j]
            if f1 == f2 and w1 != w2:
                same_rootset_diff_w += 1
            ov = len(z1 & z2)
            if ov > maxovl:
                maxovl = ov
                worst = (i, j, sorted(z1 & z2))
            delta = [(a - b) % q for a, b in zip(
                pad(pmul(w1, f2, q), 2 * d + 1),
                pad(pmul(w2, f1, q), 2 * d + 1))]
            if pdegree(delta) < 0:
                divok = 0                       # Delta == 0: nonvanishing FAILS
                continue
            rem = prem(delta, lam, q)
            if pdegree(rem) >= 0:
                divok = 0
            else:
                cof = pdiv(delta, lam, q)
                degcof = max(degcof, pdegree(cof))
                li = locator(sorted(z1 & z2), q)
                rem2 = prem(delta, pmul(lam, li, q), q)
                if pdegree(rem2) >= 0:
                    divok = 0
    return {"MAXOVL": maxovl, "CAP": cap, "SLACK": cap - maxovl,
            "DIVOK": divok, "DEGCOF": degcof, "worst_pair": worst,
            "same_rootset_diff_W_pairs": same_rootset_diff_w}


def pad(p, n):
    return p + [0] * (n + 1 - len(p)) if len(p) < n + 1 else p[:n + 1]


def pdiv(a, m, q):
    """Exact quotient a/m (assumes m | a)."""
    a = a[:]
    dm = pdegree(m)
    inv = pow(m[dm], q - 2, q)
    da = pdegree(a)
    quo = [0] * max(1, da - dm + 1)
    while da >= dm:
        f = a[da] * inv % q
        quo[da - dm] = f
        if f:
            for i in range(dm + 1):
                a[da - dm + i] = (a[da - dm + i] - f * m[i]) % q
        a[da] = 0
        da = pdegree(a)
    return quo


# ------------------------------------------------------------------ driver
def one_config(t, ell, d, q, ncore, rng, arm, work_cap):
    h = t * ell
    e = 2 * d + 1 - h
    pts = rng.sample(range(1, q), h + ncore)
    petals = [pts[i * ell:(i + 1) * ell] for i in range(t)]
    core = sorted(pts[h:])
    labels = rng.sample(range(0, q), t)
    lam = [1]
    for pet in petals:
        lam = pmul(lam, locator(pet, q), q)
    want_prim = (arm != "BRK-PRIM")
    if arm == "BRK-DISJ":                 # core swallows one petal point
        core = sorted(set(core[:-1]) | {petals[0][0]})
    mem, dimv, cls = members_of(petals, labels, core, d, q, want_prim,
                                work_cap)
    if arm == "BRK-LABEL":                # SAME petals+core, DIFFERENT labels
        while True:
            lab2 = rng.sample(range(0, q), t)
            if lab2 != labels:
                break
        mem2, _, _ = members_of(petals, lab2, core, d, q, want_prim, work_cap)
        # cross-cell pairs only: tag so `analyse` compares across the union
        mem = mem + mem2
    res = analyse(mem, lam, d, q, e - 1)
    res.update({"t": t, "ell": ell, "d": d, "q": q, "N": len(core),
                "e": e, "h": h, "DIMV": dimv, "DIMV_minus_e_plus_1":
                dimv - (e + 1), "NMEM": len(mem), "class": cls, "arm": arm})
    den = d * d - len(core) * (e - 1)
    res["NJOHN"] = (len(core) * (d - (e - 1)) // den) if den > 0 else None
    return res


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "main"
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 20260808
    nconf = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    work_cap = int(sys.argv[4]) if len(sys.argv) > 4 else 400_000
    rng = random.Random(seed)
    cells = []
    for t in (4, 5, 6):
        for ell in (1, 2, 3):
            h = t * ell
            for d in range((h + 1) // 2, h):        # d < h <= 2d
                e = 2 * d + 1 - h
                if not 1 <= e <= 7:
                    continue
                for ncore in (d, d + 2, d + 4):
                    for q in (11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
                        if q - 1 >= h + ncore + 1:
                            cells.append((t, ell, d, q, ncore))
                            break
    arms = ["MAIN"] if mode == "main" else ["BRK-PRIM", "BRK-DISJ",
                                            "BRK-LABEL"]
    out = []
    viol = []
    t0 = time.time()
    for (t, ell, d, q, ncore) in cells:
        for arm in arms:
            agg = None
            for ci in range(nconf):
                if time.time() - t0 > 255:   # print before ramguard local's 5m
                    break
                r = one_config(t, ell, d, q, ncore, rng, arm, work_cap)
                if r["class"].startswith("CLASS-S"):
                    agg = r
                    break
                if r["SLACK"] < 0 or r["DIVOK"] == 0:
                    viol.append(dict(r, config=ci, seed=seed))
                if agg is None:
                    agg = r
                else:
                    for kk in ("MAXOVL", "NMEM", "DEGCOF"):
                        agg[kk] = max(agg[kk], r[kk])
                    agg["SLACK"] = min(agg["SLACK"], r["SLACK"])
                    agg["DIVOK"] = min(agg["DIVOK"], r["DIVOK"])
            if agg is not None:
                agg["configs"] = ci + 1
                out.append(agg)
    paired = [r for r in out if r["NMEM"] >= 2]
    skipped = [r for r in out if r["class"].startswith("CLASS-S")]
    summary = {
        "mode": mode, "seed": seed, "configs_per_cell": nconf,
        "cells_registered": len(cells), "rows": len(out),
        "elapsed_s": round(time.time() - t0, 1),
        "cells_CLASS_E_or_B_exhaustive": len(out) - len(skipped),
        "cells_skipped_over_work_cap": len(skipped),
        "cells_with_at_least_one_PAIR": len(paired),
        "total_members_seen": sum(r["NMEM"] for r in out),
        "n_violations": len(viol),
        "VIOLATIONS": viol[:6],
        "MIN_SLACK_over_paired_cells": min((r["SLACK"] for r in paired),
                                           default=None),
        "DIVOK_all": all(r["DIVOK"] == 1 for r in paired),
        "DEGCOF_le_CAP_all": all(r["DEGCOF"] <= r["CAP"] for r in paired),
        "DIMV_equals_e_plus_1_all": all(r["DIMV_minus_e_plus_1"] == 0
                                        for r in out),
        "DIMV_anomalies": [r for r in out
                           if r["DIMV_minus_e_plus_1"] != 0][:6],
        "t_values_with_pairs": sorted({r["t"] for r in paired}),
        "table": [[r["arm"], r["t"], r["ell"], r["d"], r["q"], r["N"],
                   r["e"], r["DIMV"], r["NMEM"], r["MAXOVL"], r["CAP"],
                   r["SLACK"], r["DEGCOF"], r["DIVOK"], r["NJOHN"],
                   r["class"]] for r in paired],
        "table_cols": ["arm", "t", "ell", "d", "q", "N", "e", "DIMV",
                       "NMEM", "MAXOVL", "CAP", "SLACK", "DEGCOF",
                       "DIVOK", "NJOHN", "class"],
    }
    with open(ROOT + "/notes/pilots_20260808/t_petal_lemma/"
              "out_%s_%d.json" % (mode, seed), "w") as fh:
        json.dump({"summary": summary, "rows": out}, fh, indent=1,
                  default=str)
    print(json.dumps(summary, indent=1, default=str))


if __name__ == "__main__":
    main()
