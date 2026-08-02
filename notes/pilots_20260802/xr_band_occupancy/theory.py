#!/usr/bin/env python3
"""Band-occupancy pilot: exact six-row arithmetic for the proof attack.

Sections
  1. row table + validation against the banked band_arith pricing
  2. Johnson-radius regime map (six rows vs the toy battery shapes)
  3. first-moment exponents (log2) for the gate events and for the band
     population, as a function of log2 q; the q-thresholds
  4. combinatorial per-slope line caps (complement-packing) by depth
  5. where the ledger mass sits: low band (d < h/2) vs high band
  6. candidate occupancy bounds vs the 13 n^3 headroom

All logs are base 2 and computed with lgamma (abs error << 1 against
magnitudes of order 1e11).

Run: tools/ramguard tiny -- python3 <this>
"""
import json
import math
from math import lgamma, log2, sqrt

LN2 = math.log(2.0)


def lbinom(n, k):
    """log2 C(n,k) for possibly astronomical n."""
    if k < 0 or k > n:
        return float("-inf")
    if k == 0 or k == n:
        return 0.0
    return (lgamma(n + 1.0) - lgamma(k + 1.0) - lgamma(n - k + 1.0)) / LN2


ROWS = [
    dict(name="RowC 1/4", n=1024, k=256, A=261, h=5),
    dict(name="RowC 1/8", n=1024, k=128, A=133, h=5),
    dict(name="RowC 1/16", n=1024, k=64, A=67, h=3),
    dict(name="prize 1/4", n=2199023255552, k=549755813888,
         A=558345748481, h=8589934593),
    dict(name="prize 1/8", n=2199023255552, k=274877906944,
         A=283467841537, h=8589934593),
    dict(name="prize 1/16", n=2199023255552, k=137438953472,
         A=141733920769, h=4294967297),
]
# banked headroom (band_arith.json: floor(s_lo/n^3) = 29 on prize rows,
# 16 n^3 spent, 13 n^3 left; RowC headroom astronomically larger).
HEADROOM_CUBIC = 13

OUT = {}


def L(row, d):
    """line cap floor((R-d)/(h-d))."""
    return (row["R"] - d) // (row["h"] - d)


def sum_floor(M, a, b):
    """sum_{j=a}^{b} floor(M/j) in O(sqrt(M)) by divisor blocks."""
    if a > b:
        return 0
    tot = 0
    j = a
    while j <= b:
        v = M // j
        if v == 0:
            break
        jmax = min(b, M // v)
        tot += v * (jmax - j + 1)
        j = jmax + 1
    return tot


def sumL(row, d0, d1):
    """sum_{d=d0}^{d1} floor((R-d)/(h-d)); j = h-d in [h-d1, h-d0]."""
    if d0 > d1:
        return 0
    M = row["R"] - row["h"]
    a, b = row["h"] - d1, row["h"] - d0
    return (d1 - d0 + 1) + sum_floor(M, a, b)


def main():
    for r in ROWS:
        r["R"] = r["n"] - r["k"]
        r["r"] = r["n"] - r["A"]
        assert r["A"] == r["k"] + r["h"]

    # ---------------- 1. validation against the banked pricing -----------
    val = []
    for r in ROWS:
        h, n = r["h"], r["n"]
        SL = sumL(r, 1, h - 2)
        need = HEADROOM_CUBIC * n ** 3 / SL if SL else None
        val.append(dict(row=r["name"], h=h, band_depths=h - 2, sumL=SL,
                        printed_tangent=n - r["A"] + 1,
                        fits_printed=SL <= n - r["A"] + 1,
                        required_uniform_N_d=need,
                        required_over_n2=need / n ** 2))
    OUT["validation_pricing"] = val

    # ---------------- 2. Johnson regime map ------------------------------
    toy = [dict(name="banked V1", n=14, k=5, t=4), dict(name="banked S1/M2", n=16, k=5, t=4),
           dict(name="banked depth", n=16, k=4, t=5), dict(name="banked M1", n=20, k=5, t=4),
           dict(name="banked M3", n=27, k=5, t=4), dict(name="banked search", n=12, k=3, t=4),
           dict(name="sub-J k3t3 n=24", n=24, k=3, t=3),
           dict(name="sub-J k3t3 n=40", n=40, k=3, t=3),
           dict(name="sub-J k3t3 n=64", n=64, k=3, t=3),
           dict(name="sub-J k3t4 n=48", n=48, k=3, t=4),
           dict(name="sub-J k4t4 n=40", n=40, k=4, t=4)]
    jm = []
    for r in ROWS:
        jm.append(dict(row=r["name"], n=r["n"], k=r["k"], A=r["A"],
                       johnson_agreement=sqrt(r["k"] * r["n"]),
                       ratio_A_over_johnson=r["A"] / sqrt(r["k"] * r["n"]),
                       rate=r["k"] / r["n"], h_over_n=r["h"] / r["n"]))
    for s in toy:
        A = s["k"] + s["t"]
        jm.append(dict(row=s["name"], n=s["n"], k=s["k"], A=A,
                       johnson_agreement=sqrt(s["k"] * s["n"]),
                       ratio_A_over_johnson=A / sqrt(s["k"] * s["n"]),
                       rate=s["k"] / s["n"], h_over_n=s["t"] / s["n"]))
    OUT["johnson_regime"] = jm

    # ---------------- 3. first-moment exponents --------------------------
    # model: u,v uniform in F_q^n.  Leading-order first moments:
    #   E[# rays with agreement >= A+1]      = q^{k+1-(A+1)} C(n,A+1) (over
    #        z in F_q, codewords c): log2 = lb C(n,A+1) - h*lq
    #   E[# codeword pairs with |Z| >= k+d]  = q^{2k-2(k+d)} C(n,k+d)
    #   E[# (pair, unordered live slope pair) at depth d]
    #        = C(n,k+d) C(R-d,h-d)^2 q^{2-2h} / 2
    fm = []
    for r in ROWS:
        n, k, A, h, R = r["n"], r["k"], r["A"], r["h"], r["R"]
        for d in sorted(set([1, 2, max(1, h // 2), h - 2])):
            if not (1 <= d <= h - 2):
                continue
            c1 = lbinom(n, k + d)
            c2 = lbinom(R - d, h - d)
            rec = dict(row=r["name"], d=d,
                       lb_C_n_kd=c1, lb_C_Rd_hd=c2)
            for lq in (41, 64, 96, 128, 192, 256):
                rec[f"pairs_lq{lq}"] = c1 - 2 * d * lq
                rec[f"pairs2slopes_lq{lq}"] = c1 + 2 * c2 - (2 * h - 2) * lq - 1
            # thresholds
            rec["lq_for_pairs2slopes_below_1"] = (c1 + 2 * c2 - 1) / (2 * h - 2)
            rec["lq_for_pairs2slopes_below_n2"] = (c1 + 2 * c2 - 1 - 2 * log2(n)) / (2 * h - 2)
            rec["lq_for_pairs_below_1"] = c1 / (2 * d)
            fm.append(rec)
        cg = lbinom(n, A + 1)
        OUT.setdefault("gate_first_moment", []).append(dict(
            row=r["name"], lb_C_n_Ap1=cg,
            lq_for_no_overagreement_ray=cg / h,
            **{f"overagreement_lq{lq}": cg - h * lq
               for lq in (41, 64, 96, 128, 192, 256)}))
    OUT["band_first_moment"] = fm

    # ---------------- 4. per-slope complement packing --------------------
    # cores through one slope z: complements in S_z have size h-d and
    # pairwise intersections <= h-d_i-d_j-1; at equal depth d this is a
    # constant-weight packing:  p_d(z) <= C(A, h-2d) / C(h-d, h-2d).
    pk = []
    for r in ROWS:
        A, h = r["A"], r["h"]
        for d in sorted(set([1, 2, max(1, h // 4), max(1, (h - 1) // 2),
                             h // 2, h - 2])):
            if not (1 <= d <= h - 2):
                continue
            s = h - 2 * d
            if s <= 0:
                bound, note = 1, "forced unique (h-2d <= 0)"
            else:
                lg = lbinom(A, s) - lbinom(h - d, s)
                bound = (2.0 ** lg) if lg < 900 else float("inf")
                note = "complement packing"
            pk.append(dict(row=r["name"], d=d, h_minus_2d=s,
                           log2_bound=(0.0 if s <= 0 else
                                       lbinom(A, s) - lbinom(h - d, s)),
                           bound=bound, note=note))
    OUT["per_slope_line_cap"] = pk

    # ---------------- 5. where the ledger mass sits ----------------------
    lm = []
    for r in ROWS:
        h, n = r["h"], r["n"]
        lo = sumL(r, 1, min(h - 2, (h + 1) // 2 - 1))
        hi = sumL(r, (h + 1) // 2, h - 2)
        tot = lo + hi
        lm.append(dict(row=r["name"], h=h, split_at=(h + 1) // 2,
                       sumL_low=lo, sumL_high=hi, sumL=tot,
                       high_fraction=(hi / tot if tot else 0.0),
                       need_N_low=(HEADROOM_CUBIC * n ** 3 / lo if lo else None),
                       need_N_low_over_n2=(HEADROOM_CUBIC * n ** 3 / lo / n ** 2
                                           if lo else None),
                       need_N_high_over_n2=(HEADROOM_CUBIC * n ** 3 / hi / n ** 2
                                            if hi else None)))
    OUT["ledger_mass_split"] = lm

    # ---------------- 6. candidate occupancy bounds ----------------------
    cb = []
    for r in ROWS:
        n, h, k = r["n"], r["h"], r["k"]
        SL = sumL(r, 1, h - 2)
        cands = dict(one=1, n_over_k=n // (k + 1), n=n,
                     n32=int(n ** 1.5), half_n2=n * (n - 1) // 2, n2=n * n)
        row = dict(row=r["name"])
        for nm, val_ in cands.items():
            row[nm] = val_ * SL / n ** 3
            row[nm + "_fits13"] = (val_ * SL <= HEADROOM_CUBIC * n ** 3)
        cb.append(row)
    OUT["candidate_columns"] = cb

    # -------- print -------------------------------------------------------
    print("=" * 78)
    print("1. PRICING VALIDATION (reproduces band_arith.json)")
    for v in val:
        print(f"  {v['row']:<11} h={v['h']:<11} sumL={v['sumL']:<16} "
              f"printed={v['printed_tangent']:<14} fits={v['fits_printed']} "
              f"required N_d = {v['required_over_n2']:.4g} n^2")
    print()
    print("2. JOHNSON REGIME MAP  (A / sqrt(kn); >1 = above Johnson radius)")
    for v in jm:
        print(f"  {v['row']:<18} n={v['n']:<14} k={v['k']:<13} A={v['A']:<13} "
              f"A/sqrt(kn)={v['ratio_A_over_johnson']:.3f}  rate={v['rate']:.4f}"
              f"  h/n={v['h_over_n']:.5f}")
    print()
    print("3a. GATE FIRST MOMENT: log2 E[# rays with agreement >= A+1]")
    for v in OUT["gate_first_moment"]:
        print(f"  {v['row']:<11} log2C(n,A+1)={v['lb_C_n_Ap1']:.4g}   "
              f"gate plausible iff log2 q > {v['lq_for_no_overagreement_ray']:.1f}"
              f"   [lq=128: 2^{v['overagreement_lq128']:.4g}, "
              f"lq=256: 2^{v['overagreement_lq256']:.4g}]")
    print()
    print("3b. BAND FIRST MOMENT: log2 E[# (depth-d pair, live slope pair)]")
    for v in fm:
        print(f"  {v['row']:<11} d={v['d']:<11} "
              f"lq=128: 2^{v['pairs2slopes_lq128']:.5g}   "
              f"lq=256: 2^{v['pairs2slopes_lq256']:.5g}   "
              f"< n^2 iff log2 q > {v['lq_for_pairs2slopes_below_n2']:.1f}")
    print()
    print("4. PER-SLOPE LINE CAP (complement packing)")
    for v in pk:
        print(f"  {v['row']:<11} d={v['d']:<11} h-2d={v['h_minus_2d']:<12} "
              f"p_d(z) <= 2^{v['log2_bound']:.4g}   {v['note']}")
    print()
    print("5. LEDGER MASS SPLIT (low band d < ceil(h/2) vs high band)")
    for v in lm:
        print(f"  {v['row']:<11} sumL_low={v['sumL_low']:<16} "
              f"sumL_high={v['sumL_high']:<16} high={100*v['high_fraction']:.2f}%"
              f"  need N_low <= {v['need_N_low_over_n2'] or 0:.4g} n^2"
              f", N_high <= {v['need_N_high_over_n2'] or 0:.4g} n^2")
    print()
    print("6. CANDIDATE COLUMNS (units of n^3; must be <= 13)")
    for v in cb:
        print(f"  {v['row']:<11} N<=n/k:{v['n_over_k']:.3g}  N<=n:{v['n']:.3g}  "
              f"N<=n^1.5:{v['n32']:.4g}  N<=n(n-1)/2:{v['half_n2']:.4g} "
              f"({v['half_n2_fits13']})  N<=n^2:{v['n2']:.4g} ({v['n2_fits13']})")

    path = ("/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/"
            "xr_band_occupancy/theory.json")
    with open(path, "w") as fh:
        json.dump(OUT, fh, indent=1, default=str)
    print(f"\ncheckpoint: {path}")


if __name__ == "__main__":
    main()
