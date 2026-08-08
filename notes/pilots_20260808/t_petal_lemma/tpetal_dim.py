#!/usr/bin/env python3
"""THE SLICE-DIMENSION THEOREM AT GENERAL t, machine-checked.

Round-23b's red-3 split (notes/pilots_20260807/mf_wall_adversary/
red3_split.py:5-11) rests on:

    "The (MF) statement can only be INSTANTIATED on a cell whose
     contributors are proved to inject into a linear flat.  That
     injection exists at t = 2 ... and at t = 3 ...  For t >= 4 NO
     such reduction is proved"

The overlap-cap lemma does NOT supply that by itself: the cap is a
pairwise fact, while (MF) needs the flat's DIMENSION.  This script
checks the missing dimension statement, which the same
cross-determinant proves:

  THEOREM (slice dimension, general t).  Let
  V = {(F,W): deg F,deg W <= d, L_i | (W-c_iF)}, h = sum_i deg L_i,
  e = 2d+1-h.  If V contains a SATURATED pair (F monic of degree
  exactly d, gcd(F,W) = 1), then
        dim_K V = e + 1   (and V = 0 has no saturated pair if e<=0).

  PROOF.  >= : the h evaluation conditions on 2(d+1) unknowns give
  dim V >= 2d+2-h = e+1.
  <= : fix a saturated (F,W) and send (G,B) in V to
  E(G,B) = (F B - G W)/Lambda.  Each L_i divides F B - G W (both
  pairs satisfy the same congruences), so E is a polynomial, and
  deg(F B - G W) <= 2d gives deg E <= 2d-h = e-1: the image sits in
  an e-dimensional space.  The kernel is {(G,B): F B = G W}; from
  gcd(F,W)=1, F | G, and deg G <= d = deg F force G = lambda F and
  then B = lambda W, so the kernel is the line K(F,W).  Hence
  dim V <= 1 + e.  QED

This is the general-t replacement for (TF3) at t=2
(critical/nodes/pma_two_full_petal_linear_slice_reduction/statement.md:31)
and for (HF)+(BAL) at t=3
(critical/nodes/pma_three_petal_mu_basis_reduction/statement.md:82,107).

CHECKS PERFORMED
  C-DIM   dim V measured exactly; compared to e+1.
  C-SAT   whether a saturated pair exists (exhaustive over the monic
          chart, early exit).
  C-KER   the kernel of E is exactly the line K(F,W)  (rank of E is
          dim V - 1).
  C-IMG   deg E <= e-1 for every basis vector (the image bound).
  C-NOSAT cells with NO saturated pair, reported separately: these
          are the only cells where dim V may exceed e+1, and the
          theorem makes no claim about them.

Stdlib only.  Run via tools/ramguard.
"""
from __future__ import annotations

import json
import random
import sys
from itertools import product

ROOT = "/home/u2470931/smooth-read-solomin/prize"
sys.path.insert(0, ROOT + "/notes/pilots_20260807/fpc5_diag")
sys.path.insert(0, ROOT + "/notes/pilots_20260807/mf_wall_adversary")
sys.path.insert(0, ROOT + "/notes/pilots_20260808/t_petal_lemma")
from rh_m4t2_census import locator, pdegree, pgcd, pmul, prem  # noqa: E402
from rh_bucket import rref_kernel, rank_of                     # noqa: E402
from tpetal_refute import monic_chart_at, slice_rows           # noqa: E402


def find_saturated(v0, dirs, d, q, cap=200_000):
    """First chart point with gcd(F,W)=1, or None.  Exhaustive if the
    chart fits under `cap`."""
    r = len(dirs)
    if q ** r > cap:
        return None, False
    for coefs in product(range(q), repeat=r):
        v = v0[:]
        for i, c in enumerate(coefs):
            if c:
                v = [(a + c * b) % q for a, b in zip(v, dirs[i])]
        f, w = v[:d + 1], v[d + 1:]
        if pdegree(f) == d and pdegree(pgcd(f, w, q)) == 0:
            return (f, w), True
    return None, True


def pdiv(a, m, q):
    a = a[:]
    dm = pdegree(m)
    inv = pow(m[dm], q - 2, q)
    da = pdegree(a)
    quo = [0] * max(1, da - dm + 1)
    while da >= dm:
        fq = a[da] * inv % q
        quo[da - dm] = fq
        if fq:
            for i in range(dm + 1):
                a[da - dm + i] = (a[da - dm + i] - fq * m[i]) % q
        a[da] = 0
        da = pdegree(a)
    return quo


def one_cell(t, ell, d, q, rng):
    h = t * ell
    e = 2 * d + 1 - h
    pts = rng.sample(range(1, q), h)
    petals = [pts[i * ell:(i + 1) * ell] for i in range(t)]
    labels = rng.sample(range(0, q), t)
    lam = [1]
    for pet in petals:
        lam = pmul(lam, locator(pet, q), q)
    basis = rref_kernel(slice_rows(petals, labels, d, q), 2 * d + 2, q)
    dimv = len(basis)
    v0, dirs = monic_chart_at(basis, d, q)
    rec = {"t": t, "ell": ell, "d": d, "q": q, "h": h, "e": e,
           "DIMV": dimv, "e_plus_1": e + 1,
           "DIMV_ge_e_plus_1": dimv >= e + 1}
    if v0 is None:
        rec.update({"SAT": False, "note": "no monic-F point in V"})
        return rec
    sat, exact = find_saturated(v0, dirs, d, q)
    rec["SAT_search_exhaustive"] = exact
    rec["SAT"] = sat is not None
    if sat is None:
        return rec
    f, w = sat
    # C-IMG / C-KER : the linear map E(G,B) = (F*B - G*W)/Lambda
    rows = []
    maxdeg = -1
    for v in basis:
        g, b = v[:d + 1], v[d + 1:]
        delta = pmul(f, b, q)
        sub = pmul(g, w, q)
        n = max(len(delta), len(sub))
        delta = delta + [0] * (n - len(delta))
        sub = sub + [0] * (n - len(sub))
        delta = [(x - y) % q for x, y in zip(delta, sub)]
        if pdegree(delta) < 0:
            rows.append([0] * max(1, e))
            continue
        assert pdegree(prem(delta, lam, q)) < 0, "Lambda does not divide"
        cof = pdiv(delta, lam, q)
        maxdeg = max(maxdeg, pdegree(cof))
        rows.append((cof + [0] * max(1, e))[:max(1, e)])
    rk = rank_of(rows, max(1, e), q)
    rec.update({"C_IMG_max_deg_cofactor": maxdeg, "C_IMG_bound_e_minus_1":
                e - 1, "C_IMG_ok": maxdeg <= e - 1,
                "C_KER_rank_of_E": rk, "C_KER_expected": dimv - 1,
                "C_KER_ok": rk == dimv - 1,
                "C_DIM_ok": dimv == e + 1})
    return rec


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 31337
    ncfg = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    rng = random.Random(seed)
    recs = []
    for t in (4, 5, 6, 7, 8):
        for ell in (1, 2, 3):
            h = t * ell
            for d in range((h + 1) // 2, h):
                e = 2 * d + 1 - h
                if not 1 <= e <= 6:
                    continue
                for q in (11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53):
                    if q - 1 >= h + 2:
                        break
                for _ in range(ncfg):
                    recs.append(one_cell(t, ell, d, q, rng))
    sat = [r for r in recs if r.get("SAT")]
    nosat = [r for r in recs if not r.get("SAT")]
    print(json.dumps({
        "cells": len(recs),
        "cells_with_a_SATURATED_pair": len(sat),
        "cells_with_NO_saturated_pair": len(nosat),
        "DIMV_ge_e_plus_1_ALWAYS": all(r["DIMV_ge_e_plus_1"] for r in recs),
        "THEOREM_dim_eq_e_plus_1_on_SATURATED_cells":
            all(r["C_DIM_ok"] for r in sat),
        "C_IMG_ok_all": all(r["C_IMG_ok"] for r in sat),
        "C_KER_ok_all": all(r["C_KER_ok"] for r in sat),
        "t_values": sorted({r["t"] for r in sat}),
        "e_values": sorted({r["e"] for r in sat}),
        "DIM_anomalies_on_saturated_cells":
            [r for r in sat if not r["C_DIM_ok"]][:5],
        "unsaturated_cells_DIMV_vs_e_plus_1":
            [[r["t"], r["ell"], r["d"], r["q"], r["DIMV"], r["e_plus_1"],
              r.get("SAT_search_exhaustive")] for r in nosat[:8]],
        "sample": sat[0] if sat else None,
    }, indent=1))


if __name__ == "__main__":
    main()
