#!/usr/bin/env python3
"""Analysis of the order-2N C1 doubling-orbit sweep: H-A / H-B / H-C verdicts.

Consumes the exact result JSONs written by orbit_spectrum.py and emits
results/analysis_<tag>.json plus a compact stdout summary.  All statistics are
computed from the exact integer fields (X_num/X_den, weight_profile); floats
are used only for ranking and display.
"""

from __future__ import annotations

import argparse
import glob
import json
import math
from fractions import Fraction

C16 = [math.comb(16, w) for w in range(17)]


def load(patterns: list[str]) -> list[dict]:
    rows: list[dict] = []
    for pat in patterns:
        for f in sorted(glob.glob(pat)):
            rows += json.load(open(f))["rows"]
    rows.sort(key=lambda r: r["q"])
    return rows


def spearman(xs: list[float], ys: list[float]) -> float:
    def rank(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        rk = [0.0] * len(v)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2.0
            for k in range(i, j + 1):
                rk[order[k]] = avg
            i = j + 1
        return rk
    rx, ry = rank(xs), rank(ys)
    n = len(xs)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    return num / den if den else float("nan")


def excess_by_weight(row: dict) -> list[Fraction]:
    """e_w = N_w 2^-w - C(16,w)/q  (exact); X = 1 - 1/q + sum_{w>=1} e_w."""
    q = row["q"]
    Nw = row["weight_profile"]
    return [Fraction(Nw[w], 1 << w) - Fraction(C16[w], q) for w in range(17)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--glob", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--tag", default="order32")
    ap.add_argument("--N", type=int, default=16)
    args = ap.parse_args()

    rows = load(args.glob)
    N = args.N
    for r in rows:
        r["X"] = Fraction(r["X_num"], r["X_den"])
        r["minw"] = r["min_relation_weight"] if r["min_relation_weight"] else N + 1

    out: dict = {"tag": args.tag, "n_rows": len(rows),
                 "q_range": [rows[0]["q"], rows[-1]["q"]]}

    # ---------------------------------------------------------------- checks
    out["exact_checks"] = {
        "profile_vs_subset_sum_all_match": all(r["profile_matches_SS"] for r in rows),
        "sumA_integer_all": all(r["sumA_is_integer"] for r in rows),
        "sumA_nonneg_all": all(r["sumA_nonneg"] for r in rows),
        "X_ge_flat_all": all(r["X"] >= Fraction(r["X_flat_num"], r["X_flat_den"])
                             for r in rows),
        "explicit_cycle_rows": sum(1 for r in rows if "explicit" in r),
        "explicit_cycle_all_uniform_and_match_r": all(
            r["explicit"]["cycle_lengths"] == [r["r"]] and
            r["explicit"]["n_cycles"] == r["n_cycles"]
            for r in rows if "explicit" in r),
    }

    # ------------------------------------------------------------- global X
    hard = [r for r in rows if r["hard_regime"]]
    xs = sorted(r["X"] for r in rows)
    out["X_stats_all"] = {
        "max": str(max(xs)), "max_float": float(max(xs)),
        "min": str(min(xs)), "min_float": float(min(xs)),
        "median_float": float(xs[len(xs) // 2]),
        "mean_float": float(sum(xs) / len(xs)),
        "n_above_1": sum(1 for x in xs if x > 1),
        "n_above_2": sum(1 for x in xs if x > 2),
        "n_above_3": sum(1 for x in xs if x > 3),
        "n_above_4": sum(1 for x in xs if x > 4),
        "target_X_le_4_holds": all(x <= 4 for x in xs),
    }
    xh = sorted(r["X"] for r in hard)
    out["X_stats_hard_regime"] = {
        "n": len(xh), "max_float": float(max(xh)), "min_float": float(min(xh)),
        "mean_float": float(sum(xh) / len(xh)), "median_float": float(xh[len(xh) // 2]),
        "note": "hard regime = q > 2^N so the Haar baseline 2^N/q < 1 and X ~ 1 + relmass",
    }

    # tail growth with q
    bins = []
    edges = [0, 65536, 100000, 200000, 400000, 700000, 1000000, 1500000,
             2000000, 2500000, 3000000, 10**9]
    for lo, hi in zip(edges, edges[1:]):
        sel = [r for r in rows if lo < r["q"] <= hi]
        if not sel:
            continue
        v = sorted(float(r["X"]) for r in sel)
        bins.append({"q_lo": lo, "q_hi": hi, "n": len(sel),
                     "max_X": v[-1], "p99_X": v[int(0.99 * (len(v) - 1))],
                     "median_X": v[len(v) // 2], "mean_X": sum(v) / len(v),
                     "argmax_q": max(sel, key=lambda r: r["X"])["q"]})
    out["tail_growth_by_q_bin"] = bins

    # ---------------------------------------------------------------- (H-B)
    small = sorted([r for r in rows if r["r"] <= 16], key=lambda r: (r["r"], r["q"]))
    out["H_B_small_orbit_rows"] = [{
        "q": r["q"], "r": r["r"], "n_cycles": r["n_cycles"], "ord2": r["ord2"],
        "X": str(r["X"]), "X_float": float(r["X"]),
        "X_flat": f'{r["X_flat_num"]}/{r["X_flat_den"]}',
        "avgA": r["avgA_float"], "exactly_flat": r["is_exactly_flat"],
        "min_relation_weight": r["min_relation_weight"],
        "hard_regime": r["hard_regime"],
    } for r in small]
    out["H_B_verdict"] = {
        "n_r_eq_1": sum(1 for r in rows if r["r"] == 1),
        "r_eq_1_all_exactly_flat": all(r["is_exactly_flat"] for r in rows if r["r"] == 1),
        "exactly_flat_rows": [r["q"] for r in rows if r["is_exactly_flat"]],
        "max_avgA_among_r_le_8": max((r["avgA_float"] for r in rows if 2 <= r["r"] <= 8),
                                     default=None),
        "max_X_among_r_le_8": max((float(r["X"]) for r in rows if 2 <= r["r"] <= 8),
                                  default=None),
    }

    # ---------------------------------------------------------------- (H-A)
    sel = hard if len(hard) > 50 else rows
    out["H_A"] = {
        "population": "hard regime (q > 2^N)" if sel is hard else "all rows",
        "n": len(sel),
        "spearman_X_vs_r": spearman([float(r["r"]) for r in sel],
                                    [float(r["X"]) for r in sel]),
        "spearman_X_vs_log_r": spearman([math.log(r["r"]) for r in sel],
                                        [float(r["X"]) for r in sel]),
        "spearman_X_vs_n_cycles": spearman([float(r["n_cycles"]) for r in sel],
                                           [float(r["X"]) for r in sel]),
        "spearman_X_vs_minw": spearman([float(r["minw"]) for r in sel],
                                       [float(r["X"]) for r in sel]),
        "spearman_X_vs_v2": spearman([float(r["v2_qm1"]) for r in sel],
                                     [float(r["X"]) for r in sel]),
        "spearman_X_vs_log_q": spearman([math.log(r["q"]) for r in sel],
                                        [float(r["X"]) for r in sel]),
    }
    # binned means of X by r-decile and by n_cycles
    def binned(key, getter, nb=8):
        vals = sorted(sel, key=getter)
        chunk = max(1, len(vals) // nb)
        res = []
        for i in range(0, len(vals), chunk):
            c = vals[i:i + chunk]
            if len(c) < 5:
                continue
            res.append({"key": key, "lo": getter(c[0]), "hi": getter(c[-1]),
                        "n": len(c),
                        "mean_X": sum(float(r["X"]) for r in c) / len(c),
                        "max_X": max(float(r["X"]) for r in c)})
        return res
    out["H_A_binned_by_r"] = binned("r", lambda r: r["r"])
    out["H_A_binned_by_n_cycles"] = binned("n_cycles", lambda r: r["n_cycles"])
    out["H_A_binned_by_minw"] = binned("minw", lambda r: r["minw"])
    out["H_A_X_by_minw_value"] = [
        {"minw": w,
         "n": sum(1 for r in sel if r["minw"] == w),
         "mean_X": (sum(float(r["X"]) for r in sel if r["minw"] == w) /
                    max(1, sum(1 for r in sel if r["minw"] == w))),
         "max_X": max((float(r["X"]) for r in sel if r["minw"] == w), default=None)}
        for w in range(3, N + 2) if any(r["minw"] == w for r in sel)]
    out["H_A_X_by_n_cycles_value"] = [
        {"n_cycles": c,
         "n": sum(1 for r in sel if r["n_cycles"] == c),
         "mean_X": (sum(float(r["X"]) for r in sel if r["n_cycles"] == c) /
                    max(1, sum(1 for r in sel if r["n_cycles"] == c))),
         "max_X": max((float(r["X"]) for r in sel if r["n_cycles"] == c), default=None)}
        for c in sorted({r["n_cycles"] for r in sel})[:12]]

    # --------------------------------------------------- (H-C) K4 pattern
    # "no bounded owner": no short relation (minw >= wcut) and no short cycle
    # (r >= rcut), yet X large.
    hi_thresh = sorted(float(r["X"]) for r in sel)[int(0.999 * (len(sel) - 1))]
    out["H_C"] = {}
    for wcut in (6, 7, 8):
        for rcut in (16, 64):
            cand = [r for r in sel if r["minw"] >= wcut and r["r"] >= rcut]
            cand.sort(key=lambda r: -float(r["X"]))
            out["H_C"][f"minw_ge_{wcut}_and_r_ge_{rcut}"] = {
                "n": len(cand),
                "max_X": float(cand[0]["X"]) if cand else None,
                "top": [{"q": r["q"], "X": str(r["X"]), "X_float": float(r["X"]),
                         "minw": r["minw"], "r": r["r"], "n_cycles": r["n_cycles"],
                         "v2": r["v2_qm1"]} for r in cand[:8]],
            }
    out["H_C_p999_X_threshold"] = hi_thresh

    # weight-resolved excess for the extreme rows
    top = sorted(sel, key=lambda r: -float(r["X"]))[:12]
    bot = sorted(sel, key=lambda r: float(r["X"]))[:6]
    def profile_block(r):
        e = excess_by_weight(r)
        tot = sum(e[1:], Fraction(0))
        contrib = [{"w": w, "N_w": r["weight_profile"][w],
                    "haar_N_w": C16[w] * (1 << w) / r["q"],
                    "e_w": float(e[w]),
                    "share_of_excess": float(e[w] / tot) if tot else None}
                   for w in range(1, 17) if r["weight_profile"][w] or abs(float(e[w])) > 1e-9]
        return {"q": r["q"], "X": str(r["X"]), "X_float": float(r["X"]),
                "minw": r["minw"], "r": r["r"], "n_cycles": r["n_cycles"],
                "v2": r["v2_qm1"], "relmass": r["relmass_float"],
                "sum_e_w": float(tot),
                "n_kernel_nonzero": r["n_kernel_nonzero"],
                "haar_n_kernel_nonzero": (3 ** 16 - 1) / r["q"],
                "weight_excess": contrib}
    out["extreme_rows_top"] = [profile_block(r) for r in top]
    out["extreme_rows_bottom"] = [profile_block(r) for r in bot]

    # how much of the excess sits at weights <= 6 vs > 6, population-wide
    lowmass, highmass = [], []
    for r in sel:
        e = excess_by_weight(r)
        lo = float(sum(e[1:7], Fraction(0)))
        hi = float(sum(e[7:], Fraction(0)))
        lowmass.append(lo)
        highmass.append(hi)
    out["excess_split"] = {
        "mean_e_w_le_6": sum(lowmass) / len(lowmass),
        "mean_e_w_ge_7": sum(highmass) / len(highmass),
        "max_e_w_le_6": max(lowmass), "max_e_w_ge_7": max(highmass),
        "note": "X = 1 - 1/q + sum_w e_w; e_w = N_w 2^-w - C(16,w)/q",
    }

    # full key table (compact) for the report
    out["key_table"] = [{
        "q": r["q"], "v2": r["v2_qm1"], "ord2": r["ord2"], "r": r["r"],
        "n_cycles": r["n_cycles"], "max_cycle": r["r"],
        "X_num": r["X_num"], "X_den": r["X_den"], "X_float": float(r["X"]),
        "minw": r["min_relation_weight"], "avgA": r["avgA_float"],
        "hard": r["hard_regime"],
    } for r in rows]

    with open(args.out, "w") as f:
        json.dump(out, f)
    slim = {k: v for k, v in out.items() if k not in ("key_table",)}
    print(json.dumps(slim, indent=1)[:12000])


if __name__ == "__main__":
    main()
