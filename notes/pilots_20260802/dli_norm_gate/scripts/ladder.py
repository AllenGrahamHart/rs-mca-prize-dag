#!/usr/bin/env python3
"""dli_norm_gate -- the skew-norm ladder, the ENERGY ceiling, and official pricing.

CEILING (LN4).  For alpha = sum_{i<h} a_i zeta_n^i in Z[zeta_n], n = 2^s,
h = phi(n) = n/2, alpha != 0:

    1 <= Norm(alpha) <= E(alpha)^{h/2},    E(alpha) := sum_i a_i^2 .

This is the C1 sandwich node's Claim 2 with `w` replaced by the ENERGY -- the
proof (conjugate-pair positivity + negacyclic Parseval + AM-GM) never used
ternariness, only sum_i a_i^2.  For a C2'' junction-j skew d with |d_i| <= c_i
on the effective support S_j, E = sum_{i in S_j} d_i^2 <= sum c_i^2; at j = 0
the domain is {+-1}^{S_0} so E = |S_0| exactly and the ceiling is |S_0|^{h/2}.

ROUTER (LN5).  A junction-j skew solution forces q^{L_j} | Norm(d), hence

    q^{L_j} > E^{phi(h_j)/2}   =>   NO junction-j solution of energy E,
    i.e. every solution has  E >= q^{2 L_j / phi(h_j)} .

MULTIPLICITY (LN6).  m(alpha) <= v_q(Norm(alpha)) <= (h/2) log E / log q.
"""

from __future__ import annotations

import json
import random
import sys
from fractions import Fraction
from itertools import product as iproduct
from math import comb, log2
from pathlib import Path

sys.dont_write_bytecode = True

import numpy as np

from core import norm_cyclotomic, norm_sympy
from bridge import norms_batch, ternary_weight_block

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

BANKED_MAXNORM = {
    16: {1: 1, 2: 16, 3: 81, 4: 196, 5: 529, 6: 1154, 7: 2401, 8: 2176},
    32: {1: 1, 2: 256, 3: 6561, 4: 38416, 5: 279841, 6: 1331716, 7: 5764801,
         8: 14760962},
}


# ------------------------------------------------------------------ ceiling
def ceiling_checks():
    out = {}
    # (1) exhaustive, general integer coefficients (energy version), h = 4
    h = 4
    bad, tested, tight = 0, 0, 0
    for c in iproduct(range(-3, 4), repeat=h):
        if not any(c):
            continue
        tested += 1
        E = sum(v * v for v in c)
        Nz = norm_cyclotomic(list(c), h)
        if not (1 <= Nz <= E ** (h // 2)):
            bad += 1
        if Nz == E ** (h // 2):
            tight += 1
    out["h4_coeffs_-3..3_exhaustive"] = {
        "tested": tested, "violations": bad, "attained_ceiling": tight}

    # (2) exhaustive ternary at h = 8, plus the energy version with coeffs -2..2
    h = 8
    A = np.array([list(c) for c in iproduct((-1, 0, 1), repeat=h) if any(c)],
                 dtype=np.int64)
    Nz = norms_batch(A)
    E = (A * A).sum(axis=1)
    ceil8 = np.array([int(e) ** (h // 2) for e in E], dtype=object)
    viol = sum(1 for i in range(len(A)) if not (1 <= int(Nz[i]) <= ceil8[i]))
    out["h8_ternary_exhaustive"] = {"tested": int(len(A)), "violations": viol,
                                    "min_norm": int(Nz.min()),
                                    "max_norm": int(Nz.max())}
    rnd = random.Random(20260802)
    bad2, mx = 0, 0
    for _ in range(20000):
        c = [rnd.randint(-4, 4) for _ in range(h)]
        if not any(c):
            continue
        Ee = sum(v * v for v in c)
        Nz2 = norm_cyclotomic(c, h)
        if not (1 <= Nz2 <= Ee ** (h // 2)):
            bad2 += 1
        mx = max(mx, Fraction(Nz2, Ee ** (h // 2)))
    out["h8_coeffs_-4..4_random20000"] = {"violations": bad2,
                                          "max_norm_over_ceiling": str(mx)}

    # (3) h = 16 ternary, weights 1..6 (exhaustive) -- the skew-norm ladder
    ladder = {}
    for w in range(1, 7):
        Aw = ternary_weight_block(16, w)
        Nw = norms_batch(Aw)
        ladder[w] = {"maxnorm": int(Nw.max()), "ceiling": w ** 8,
                     "saturates": int(Nw.max()) == w ** 8,
                     "banked": BANKED_MAXNORM[32][w],
                     "matches_banked": int(Nw.max()) == BANKED_MAXNORM[32][w],
                     "min_norm": int(Nw.min())}
    out["h16_ternary_ladder_w1to6"] = ladder

    # (4) the ladder at h = 8 (all weights) vs banked
    lad8 = {}
    wts = (A != 0).sum(axis=1)
    for w in range(1, 9):
        sel = Nz[wts == w]
        lad8[w] = {"maxnorm": int(sel.max()), "ceiling": w ** 4,
                   "saturates": int(sel.max()) == w ** 4,
                   "banked": BANKED_MAXNORM[16][w],
                   "matches_banked": int(sel.max()) == BANKED_MAXNORM[16][w]}
    out["h8_ternary_ladder"] = lad8

    # (5) sympy cross-check of the two extreme values
    out["sympy_crosscheck"] = {
        "h8_w7_argmax_norm": norm_sympy([1, 1, 1, -1, -1, 1, -1, 0], 8),
        "h16_w3_example": norm_sympy(
            [1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0], 16)}
    return out


# ------------------------------------------------------------------ pricing
def official_pricing():
    """C2''-pinned official schedule (banked official_scale.json, verbatim):
    n = 2^41, t = 2^33, 34 blocks, 33 junctions j = 0..32,
    ell_j = 2^{32-j} (j <= 32), N_j = h_{j+1} = 2^{40-j}, ratio N_j/ell_j = 256.

    EXACT criterion (all integer):  a junction-j skew solution of energy E needs
        q^{L_j} <= Norm <= E^{N_j/2} = E^{128 L_j},   i.e.   q <= E^128 ,
    independently of j.  So E >= E_min(q) := min{E : E^128 >= q}.
    """
    n_log2 = 41
    rows = []
    for j in range(0, 33):
        Lj = 2 ** (32 - j)
        hj = 2 ** (n_log2 - j)
        Nj = hj // 2
        rows.append({"j": j, "L_j": Lj, "root_order_h_j": hj,
                     "field_degree_phi(h_j)": Nj, "cells_N_j": Nj,
                     "ratio_N_over_L": int(Fraction(Nj, Lj)),
                     "exclusion_exponent_2L/phi": str(Fraction(2 * Lj, Nj))})
    assert all(r["ratio_N_over_L"] == 256 for r in rows)

    def emin(q):
        E = 1
        while E ** 128 < q:
            E += 1
        return E

    exhibit = 2**256 - 191315023233023
    qs = [("2^41+1 (smallest admissible)", 2**41 + 1),
          ("2^128", 2**128), ("3^128 (exact E=4 threshold)", 3**128),
          ("3^128+1", 3**128 + 1), ("2^250", 2**250),
          ("2^256-191315023233023 (C2'' named exhibit)", exhibit),
          ("2^256 (cap)", 2**256),
          ("6597069766657 (C2'' small-q row)", 6597069766657)]
    pricing = [{"q": lab, "log2_q_floor": q.bit_length() - 1,
                "E_min": emin(q), "excluded_energies": f"1..{emin(q)-1}",
                "exact_witness": f"{emin(q)-1}^128 = "
                                 f"{(emin(q)-1)**128} < q <= {emin(q)}^128"}
               for lab, q in qs]
    # single-constraint (o=1) contrast: E >= q^{2/N_j}
    o1 = []
    lgq = 256.0                                  # log2 of the named exhibit
    for j in (0, 16, 32):
        Nj = rows[j]["cells_N_j"]
        # need E^{N_j/2} >= q, i.e. log2 E >= 2 log2 q / N_j
        need = 2 ** (2.0 * lgq / Nj)
        o1.append({"j": j, "N_j": Nj,
                   "E_min_single_constraint_at_exhibit": need,
                   "excludes_only_E=1": need <= 2.0})
    return {"full_schedule_head": rows[:3], "full_schedule_tail": rows[-3:],
            "n_junctions": len(rows), "uniform_ratio_N_over_L": 256,
            "exact_criterion": "q <= E^128 at EVERY official junction",
            "pricing_full_block_L_j": pricing,
            "pricing_single_constraint_o1": o1,
            "constants": {"3^128": str(3**128), "3^128_bits": (3**128).bit_length(),
                          "4^128": str(4**128), "4^128_bits": (4**128).bit_length()}}


def wcl_fence():
    """THE WCL NORM FENCE.

    The banked WCL slot family is: omega of exact order M = 512*ell, relation P
    reduced signed of weight w with P(omega^u) = 0 for u = 1,3,...,2ell-1.
    So n = M, phi(n) = M/2 = 256*ell, o = ell.  LN5 gives the fence

        q^ell > maxnorm(256 ell, w)   =>   slot (ell,w) EMPTY.

    UNCONDITIONAL (AM-GM, LN4):  maxnorm <= w^{128 ell}  =>  fence  q > w^128.
    CONDITIONAL (C1 stable doubling law maxnorm(N,w) = c_w^{N/4}):
                                  maxnorm  = c_w^{64 ell}  =>  fence  q > c_w^64.
    BOTH ARE INDEPENDENT OF ell.  The official cap |F| < 2^256 = 4^128 therefore
    sits exactly one weight above the unconditional fence and strictly between
    c_4^64 and c_5^64 for the conditional one.
    """
    c_w = {1: 1, 2: 4, 3: 9, 4: 14, 5: 23, 6: None, 7: 49}   # C1 stable bases
    c6_sq = 1154                                             # c_6 = sqrt(1154)
    rows = []
    for w in range(1, 9):
        amgm = w ** 128
        if w == 6:
            cond = c6_sq ** 32
        elif c_w.get(w):
            cond = c_w[w] ** 64
        elif w == 8:
            cond = 14760962 ** 16          # stable from N=16 (one ladder point)
        else:
            cond = None
        rows.append({
            "w": w,
            "AMGM_fence_q_gt": str(amgm), "AMGM_bits": amgm.bit_length() - 1,
            "AMGM_closes_official_2^256": amgm < 2**256,
            "conditional_fence_q_gt": str(cond) if cond else None,
            "conditional_bits": (cond.bit_length() - 1) if cond else None,
            "conditional_closes_official_2^256": (cond < 2**256) if cond else None,
            "conditional_closes_production_2^255": (cond < 2**255) if cond else None,
        })
    return {"law": "fence q > w^128 (unconditional) / q > c_w^64 (C1 doubling law), "
                   "INDEPENDENT of the window index ell",
            "official_cap": "2^256 = 4^128 exactly",
            "rows": rows,
            "banked_slots_reproved_free": [
                "dli_wcl_weight3_ambient_exclusion (ell=1,w=3, order 512): "
                "AM-GM fence 3^128 = 2^202.875 < q",
                "dli_wcl_ell2_weight3_ambient_exclusion (ell=2,w=3, order 1024): "
                "same fence"],
            "banked_slot_reachable_only_conditionally": [
                "dli_wcl_weight4_ambient_exclusion (ell=1,w=4): AM-GM fence is "
                "4^128 = 2^256 EXACTLY (just misses); C1 doubling law gives "
                "14^64 = 2^243.66 which DOES cover the production window"],
            "open_slots_unreachable": [
                "(1,5),(1,6),(1,7),(1,8),(2,7),(2,8),(2,9),(4,10),(4,11) -- all "
                "have w >= 5, fence >= c_5^64 = 23^64 = 2^289.5 > 2^256"]}


def wcl_dictionary():
    """the same router at the banked WCL setting: order-1024 root, ell = 2."""
    n = 1024
    phi = 512
    rows = []
    for ell in (1, 2, 3):
        for lg in (41.0, 203.0, 250.0, 256.0):
            Estar = 2 ** (lg * 2 * ell / phi)
            rows.append({"ell(o)": ell, "log2_q": lg, "E_star": Estar,
                         "max_excluded_weight": int(Estar - 1e-9)})
    return {"setting": "omega of exact order 1024, q = 1 mod 1024, "
                       "P(omega^u) = 0 for u in U, |U| = ell",
            "phi(n)": phi, "rows": rows,
            "banked_certificates_cover": "(ell,w) = (2,5) and (2,6) "
                                         "[dli_wcl_ell2_weight5_norm_gcd_exclusion, "
                                         "dli_wcl_ell2_weight6_recursive_norm_exclusion]"}


def main():
    out = {"ceiling": ceiling_checks(),
           "official_pricing": official_pricing(),
           "wcl_fence": wcl_fence(),
           "wcl_dictionary": wcl_dictionary()}
    c = out["ceiling"]
    print("energy ceiling violations:",
          c["h4_coeffs_-3..3_exhaustive"]["violations"],
          c["h8_ternary_exhaustive"]["violations"],
          c["h8_coeffs_-4..4_random20000"]["violations"])
    print("h=16 ladder vs banked:",
          {w: v["matches_banked"] for w, v in c["h16_ternary_ladder_w1to6"].items()})
    print("h=8 ladder vs banked:",
          {w: v["matches_banked"] for w, v in c["h8_ternary_ladder"].items()})
    print("\nOFFICIAL PRICING (exact, criterion q <= E^128 at every junction):")
    for p in out["official_pricing"]["pricing_full_block_L_j"]:
        print(f"  q={p['q']:<44} E_min={p['E_min']}  (excluded energies "
              f"{p['excluded_energies']})")
    print("\nWCL NORM FENCE (fence is independent of ell):")
    for r in out["wcl_fence"]["rows"]:
        print(f"  w={r['w']}: AM-GM q>2^{r['AMGM_bits']} closes<2^256={r['AMGM_closes_official_2^256']}"
              f" | conditional q>2^{r['conditional_bits']} closes<2^256="
              f"{r['conditional_closes_official_2^256']}")
    (ROOT / "results" / "ladder.json").write_text(json.dumps(out, indent=1,
                                                            default=str))


if __name__ == "__main__":
    main()
