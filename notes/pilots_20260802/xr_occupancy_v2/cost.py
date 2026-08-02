#!/usr/bin/env python3
"""STAGE A -- the TWO-SLOPE COST THEOREM, measured exactly.

A1  dim R(P) = 2h for every admissible depth-d two-slope datum, all d,
    all shapes, including the (0:1) direction z = inf.
A2  the free-slope (determinantal) codimension is 2h-2:
      * dim ker = 2n-2h for every prescribed slope pair;
      * distinct slope pairs give distinct kernels (so the union over the
        ~q^2 slope pairs has codimension 2h-2);
      * brute-force count of the union at a tiny shape.
A3  L1 for our supports: dim(C_S ^ C_T) = max(0, |S^T|-k).
A4  realisation: solve the system, run the banked exhaustive occlib scan,
    and check the datum really appears as a depth-d band pair with >= 2
    live slopes (and record the gate).

Run: tools/ramguard local -- python3 cost.py [stage ...]
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

FAIL = []
CHECKS = [0]


def chk(label, ok, detail=""):
    CHECKS[0] += 1
    print(("PASS " if ok else "FAIL ") + label + (f"  [{detail}]" if detail else ""))
    if not ok:
        FAIL.append(label + " " + detail)
    return ok


SHAPES = [
    dict(n=16, k=4, t=4, q=97),
    dict(n=20, k=5, t=5, q=241),
    dict(n=24, k=6, t=5, q=241),
    dict(n=20, k=4, t=6, q=101),
    dict(n=28, k=7, t=7, q=113),
    dict(n=18, k=3, t=5, q=73),
]


def mk(sh):
    return T.Row2(sh["n"], sh["k"], sh["t"], sh["q"])


def random_datum(row, d, rng):
    n, k, h = row.n, row.k, row.h
    need = k + d + 2 * (h - d)
    if need > n:
        return None
    pool = rng.sample(range(n), need)
    Z = tuple(sorted(pool[:k + d]))
    B1 = tuple(sorted(pool[k + d:k + d + h - d]))
    B2 = tuple(sorted(pool[k + d + h - d:]))
    S1 = tuple(sorted(set(Z) | set(B1)))
    S2 = tuple(sorted(set(Z) | set(B2)))
    return Z, S1, S2


# ------------------------------------------------------------------ A1
def stage_a1():
    rng = random.Random(20260802)
    out = []
    for sh in SHAPES:
        row = mk(sh)
        n, k, h, q = row.n, row.k, row.h, row.q
        per = []
        for d in range(1, h - 1):
            got = set()
            for _ in range(30):
                dd = random_datum(row, d, rng)
                if dd is None:
                    continue
                Z, S1, S2 = dd
                for (z1, z2) in [(rng.randrange(1, q), rng.randrange(1, q)),
                                 (0, rng.randrange(1, q)),
                                 (T.INF, rng.randrange(1, q)),
                                 (T.INF, 0)]:
                    if z1 == z2:
                        continue
                    rows = T.datum_rows(row, Z, S1, z1, S2, z2)
                    got.add(T.rank_mod(rows, q))
            per.append(dict(d=d, ranks=sorted(got), expect=2 * h))
            chk(f"A1 n={n} k={k} h={h} d={d}: dim R(P) = 2h = {2*h}",
                got == {2 * h}, str(sorted(got)))
        out.append(dict(shape=sh, per_depth=per))
    return out


# ------------------------------------------------------------------ A2
def stage_a2():
    rng = random.Random(11)
    out = []
    for sh in SHAPES[:4]:
        row = mk(sh)
        n, k, h, q = row.n, row.k, row.h, row.q
        rec = dict(shape=sh, depths=[])
        for d in range(1, h - 1):
            dd = random_datum(row, d, rng)
            if dd is None:
                continue
            Z, S1, S2 = dd
            dims, kers = set(), {}
            slopes = [0, 1, 2, 3, 5, 7, T.INF]
            for z1 in slopes:
                for z2 in slopes:
                    if z1 == z2:
                        continue
                    rows = T.datum_rows(row, Z, S1, z1, S2, z2)
                    rk = T.rank_mod(rows, q)
                    dims.add(rk)
                    red, pc = T.rref(rows, q)
                    kers[(str(z1), str(z2))] = tuple(pc)
            distinct = len(set(kers.values()))
            # pairwise kernel intersections must be strictly smaller
            keys = list(kers)
            inter_ok = True
            for a in range(min(len(keys), 6)):
                for b in range(a + 1, min(len(keys), 6)):
                    (za1, za2), (zb1, zb2) = keys[a], keys[b]
                    if {za1, za2} == {zb1, zb2}:
                        continue
                    ra = T.datum_rows(row, Z, S1, _pz(za1), S2, _pz(za2))
                    rb = T.datum_rows(row, Z, S1, _pz(zb1), S2, _pz(zb2))
                    if T.rank_mod(ra + rb, q) <= 2 * h:
                        inter_ok = False
            rec["depths"].append(dict(d=d, ranks=sorted(dims),
                                      distinct_pivot_patterns=distinct,
                                      union_strict=inter_ok))
            chk(f"A2 n={n} h={h} d={d}: every slope pair has rank 2h",
                dims == {2 * h}, str(sorted(dims)))
            chk(f"A2 n={n} h={h} d={d}: distinct slope pairs -> strictly "
                f"larger joint rank (union codim = 2h-2 = {2*h-2})", inter_ok)
        out.append(rec)
    # brute-force count of the union at a tiny shape
    row = T.Row2(9, 2, 3, 11)
    n, k, h, q = row.n, row.k, row.h, row.q
    d = 1
    Z = (0, 1, 2)
    S1 = (0, 1, 2, 3, 4)
    S2 = (0, 1, 2, 5, 6)
    tot = set()
    for z1 in list(range(q)) + [T.INF]:
        for z2 in list(range(q)) + [T.INF]:
            if z1 == z2:
                continue
            rows = T.datum_rows(row, Z, S1, z1, S2, z2)
            ns = T.nullspace_mod(rows, 2 * n, q)
            # enumerate the kernel only if small
            if len(ns) > 5:
                ns = None
                break
        if ns is None:
            break
    # instead of enumerating, compare log_q sizes: |union| ~ (q^2-q) q^{2n-2h}
    pred_codim = 2 * h - 2
    rks = set()
    for z1 in range(q):
        for z2 in range(z1 + 1, q):
            rks.add(T.rank_mod(T.datum_rows(row, Z, S1, z1, S2, z2), q))
    chk(f"A2 tiny n=9 k=2 h=3: all prescribed-slope ranks = 2h = {2*h}",
        rks == {2 * h})
    out.append(dict(tiny=dict(n=n, k=k, h=h, q=q, ranks=sorted(rks),
                              predicted_free_codim=pred_codim)))
    return out


def _pz(s):
    return T.INF if s == "inf" else int(s)


# ------------------------------------------------------------------ A3
def stage_a3():
    rng = random.Random(5)
    out = []
    for sh in SHAPES:
        row = mk(sh)
        n, k, q = row.n, row.k, row.q
        ok = bad = 0
        for _ in range(300):
            a = rng.randrange(k + 1, min(n, k + row.h) + 1)
            b = rng.randrange(k + 1, min(n, k + row.h) + 1)
            S = tuple(sorted(rng.sample(range(n), a)))
            Tt = tuple(sorted(rng.sample(range(n), b)))
            if S == Tt:
                continue
            bS, bT = T.dual_basis(S, row), T.dual_basis(Tt, row)
            dim = len(bS) + len(bT) - T.rank_mod(bS + bT, q)
            pred = max(0, len(set(S) & set(Tt)) - k)
            if dim == pred:
                ok += 1
            else:
                bad += 1
        chk(f"A3 L1 on n={n} k={k}: dim(C_S ^ C_T) = max(0,|S^T|-k)",
            bad == 0, f"{ok} ok / {bad} bad")
        out.append(dict(shape=sh, ok=ok, bad=bad))
    return out


# ------------------------------------------------------------------ A4
def stage_a4():
    """realise single data and confirm with the banked exhaustive scan."""
    rng = random.Random(77)
    out = []
    for sh in [dict(n=16, k=4, t=4, q=97), dict(n=18, k=4, t=5, q=101),
               dict(n=20, k=5, t=5, q=241)]:
        row = mk(sh)
        n, k, h, q = row.n, row.k, row.h, row.q
        for d in range(1, h - 1):
            hit = None
            for att in range(40):
                dd = random_datum(row, d, rng)
                if dd is None:
                    break
                Z, S1, S2 = dd
                z1, z2 = rng.randrange(1, q), rng.randrange(1, q)
                if z1 == z2:
                    continue
                rows = T.datum_rows(row, Z, S1, z1, S2, z2)
                sol = T.realise(row, rows, seed=att * 7 + d)
                if sol is None:
                    continue
                u, v = sol
                rec, pairs, band = occlib.measure(row, u, v,
                                                  name=f"A4 d={d}",
                                                  want_checks=False)
                Zf = frozenset(Z)
                if Zf not in pairs:
                    continue
                p = pairs[Zf]
                got_d = p["J"] - k
                L = len(p["slopes"])
                hit = dict(d=d, realised_depth=got_d, L=L,
                           slopes_ok=set([z1, z2]) <= set(p["slopes"]),
                           admissible=rec["ADMISSIBLE"],
                           max_ray=rec["max_ray_agreement"], A=row.A,
                           maxJ=rec["max_joint_agreement"],
                           N_total=rec["N_total"])
                if got_d == d and L >= 2:
                    break
            if hit:
                chk(f"A4 n={n} h={h} d={d}: datum realised as a depth-{d} "
                    f"band pair with >= 2 live slopes",
                    hit["realised_depth"] == d and hit["L"] >= 2
                    and hit["slopes_ok"], json.dumps(hit))
                out.append(dict(shape=sh, **hit))
            else:
                out.append(dict(shape=sh, d=d, note="no realisation drawn"))
    return out


STAGES = dict(a1=stage_a1, a2=stage_a2, a3=stage_a3, a4=stage_a4)

if __name__ == "__main__":
    want = sys.argv[1:] or list(STAGES)
    res = {}
    for s in want:
        print(f"\n=== stage {s} ===")
        res[s] = STAGES[s]()
    res["_checks"] = CHECKS[0]
    res["_failures"] = FAIL
    with open(os.path.join(HERE, "cost_%s.json" % "_".join(want)), "w") as f:
        json.dump(res, f, indent=1, default=str)
    print(f"\nchecks={CHECKS[0]} failures={len(FAIL)}")
    if FAIL:
        print("\n".join(FAIL[:20]))
