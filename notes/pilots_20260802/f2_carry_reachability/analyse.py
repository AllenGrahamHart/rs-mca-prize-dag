#!/usr/bin/env python3
"""Aggregate the F2A.2 sweep into the verdict table.

Run:  tools/ramguard local -- python3 \
        notes/pilots_20260802/f2_carry_reachability/analyse.py
"""

from __future__ import annotations

import collections
import json
import math
import os
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results")


def main() -> None:
    with open(os.path.join(OUT, "sweep.json")) as f:
        data = json.load(f)
    rows = data["rows"]
    print(f"rows = {len(rows)}")

    # --- classification of the terminal reachable set --------------------
    cls = collections.Counter()
    for r in rows:
        if r["terminal_is_full"]:
            key = "FULL Z/2p"
        elif r["terminal_size"] == 1:
            key = "TRIVIAL {0}"
        elif r["terminal_is_subgroup"]:
            key = f"subgroup index {r['terminal_index_in_Z2p']}"
        else:
            key = "non-subgroup proper"
        cls[(key, r["c_name"].split("(")[0])] += 1
    print("\n== terminal reachable set by frequency class ==")
    for (k, c), v in sorted(cls.items()):
        print(f"  {k:24s}  {c:20s}  {v}")

    # --- structural laws --------------------------------------------------
    print("\n== structural checks ==")
    bad = []
    capacity_limited = 0
    for r in rows:
        c_in_fp = r["c"][1] == 0
        trace_zero = r["c"][0] == 0
        m = r["m_pairs_total"]
        two_p = 2 * r["p"]
        if c_in_fp:
            if not (r["terminal_size"] == 1
                    and r["delta_zero_count"] == m):
                bad.append(("c in F_p not trivial", r["p"], r["n"],
                            r["c_name"]))
        else:
            if r["delta_zero_count"] != 0:
                bad.append(("nonzero c has zero delta", r["p"], r["n"],
                            r["c_name"]))
            if not r["terminal_is_full"]:
                if 2 ** m < two_p:
                    capacity_limited += 1     # |S| <= 2^m < 2p, no room
                else:
                    bad.append(("nondegenerate, room to fill, NOT full",
                                r["p"], r["n"], r["c_name"],
                                r["terminal_size"], m))
        if trace_zero and r["c"][1] != 0:
            if r["delta_odd_count"] != m:
                bad.append(("trace-zero c has even delta", r["p"], r["n"]))
    print(f"  rows with 2^m < 2p (capacity limited, cannot fill): "
          f"{capacity_limited}")
    print(f"  near-capacity rows (2^m >= 2p but m < log2(2p)+2) plus any "
          f"real violation: {len(bad)}")
    for b in bad[:20]:
        print("   ", b)

    # --- how close is |S_k| to the information-theoretic max min(2^k,2p) ---
    print("\n== doubling law: |S_k| vs min(2^k, 2p) ==")
    worst_def = []
    for r in rows:
        if r["c"][1] == 0:
            continue
        two_p = 2 * r["p"]
        cur = r["sumset_curve_prefix"]
        for k, s in enumerate(cur):
            cap = min(2 ** k, two_p)
            if cap >= 4:
                worst_def.append(s / cap)
    print(f"  |S_k| / min(2^k,2p) over all k>=2, non-degenerate rows: "
          f"min={min(worst_def):.3f} median={statistics.median(worst_def):.3f}")
    # k_full versus log2(2p)
    lr = [(r["k_full_2p"], math.log2(2 * r["p"])) for r in rows
          if r["c"][1] != 0 and r["k_full_2p"]]
    exc = [a - b for a, b in lr]
    print(f"  k_full - log2(2p): min={min(exc):.2f} "
          f"median={statistics.median(exc):.2f} max={max(exc):.2f}")
    print(f"  k_full / log2(2p): min={min(a/b for a,b in lr):.3f} "
          f"median={statistics.median([a/b for a,b in lr]):.3f} "
          f"max={max(a/b for a,b in lr):.3f}")

    # --- covering numbers -------------------------------------------------
    nd = [r for r in rows if r["c"][1] != 0]
    print(f"\n== covering numbers (non-degenerate rows: {len(nd)}) ==")
    kf = [r["k_full_2p"] for r in nd if r["k_full_2p"] is not None]
    print(f"  rows reaching FULL Z/2p: {len(kf)} / {len(nd)}")
    if kf:
        print(f"  k_full: min={min(kf)} median={statistics.median(kf)} "
              f"mean={statistics.fmean(kf):.2f} max={max(kf)}")
    byp = collections.defaultdict(list)
    for r in nd:
        if r["k_full_2p"] is not None:
            byp[r["p"]].append(r["k_full_2p"])
    print("\n  p   2p   min  med  max   k/sqrt(2p) (median)")
    for p in sorted(byp):
        v = byp[p]
        med = statistics.median(v)
        print(f"  {p:4d} {2*p:5d}  {min(v):3d} {med:5.1f} {max(v):4d}"
              f"    {med/math.sqrt(2*p):.3f}")

    ratios = [r["k_full_2p"] / math.sqrt(2 * r["p"]) for r in nd
              if r["k_full_2p"]]
    print(f"\n  k_full / sqrt(2p): min={min(ratios):.3f} "
          f"median={statistics.median(ratios):.3f} max={max(ratios):.3f}")

    # order-independence
    ordeps = 0
    spread = []
    for r in nd:
        vals = [v for v in [r["k_full_2p"]] + r["k_full_shuffled"] if v]
        if len(vals) < 2:
            continue
        spread.append(max(vals) - min(vals))
        if max(vals) > 2 * min(vals):
            ordeps += 1
    if spread:
        print(f"  k_full spread over 4 pair orderings: median={
              statistics.median(spread)} max={max(spread)}; "
              f"rows with >2x spread: {ordeps}")

    # --- Myhill-Nerode widths ---------------------------------------------
    print("\n== reachable-continuation Myhill-Nerode width ==")
    fullwidth = sum(1 for r in nd if r["mn_width_max"] == 2 * r["p"])
    print(f"  non-degenerate rows attaining the FULL 2p width: "
          f"{fullwidth} / {len(nd)}")
    degen = [r for r in rows if r["c"][1] == 0]
    print(f"  degenerate (c in F_p) rows, max MN width: "
          f"{max(r['mn_width_max'] for r in degen)}")
    ratio = [r["mn_width_max"] / (2 * r["p"]) for r in nd]
    print(f"  width/2p over non-degenerate rows: min={min(ratio):.4f} "
          f"median={statistics.median(ratio):.4f}")

    # --- carry DFT L1 ------------------------------------------------------
    print("\n== carry-DFT normalised L1 mass (float, display only) ==")
    seen = {}
    for r in rows:
        seen[r["p"]] = r["carry_dft_L1_over_2p"]
    for p in sorted(seen)[:6] + sorted(seen)[-4:]:
        print(f"  p={p:4d}  L1/(2p)={seen[p]:8.4f}  "
              f"(2/pi)ln p={2/math.pi*math.log(p):8.4f}  "
              f"diff={seen[p]-2/math.pi*math.log(p):7.4f}")

    # --- contraction dial --------------------------------------------------
    print("\n== local contraction dial 4ab/(a+b)^2 ==")
    med = [r["balance_stats"]["median"] for r in nd]
    mn_ = [r["balance_stats"]["min"] for r in nd]
    f05 = [r["balance_stats"]["frac_below_0.5"] for r in nd]
    f01 = [r["balance_stats"]["frac_below_0.1"] for r in nd]
    print(f"  median balance across rows: {statistics.median(med):.4f} "
          f"(min row {min(med):.4f}, max row {max(med):.4f})")
    print(f"  worst single pair balance: {min(mn_):.3e}")
    print(f"  frac pairs with balance<0.5: median {statistics.median(f05):.4f}")
    print(f"  frac pairs with balance<0.1: median {statistics.median(f01):.4f}")

    with open(os.path.join(OUT, "mode_contraction.json")) as f:
        modes = json.load(f)["rows"]
    print("\n== per-mode contraction bits (sample rows) ==")
    print("   p    n   c                 min_bits   med_bits  max_bits"
          "  worst_k  #dead_modes")
    for m in modes:
        print(f"  {m['p']:4d} {m['n']:4d} {m['c_name']:18s}"
              f" {m['bits_per_pair_min']:.5f}  {m['bits_per_pair_median']:.5f}"
              f"  {m['bits_per_pair_max']:.5f}  k={m['worst_mode_k']}"
              f"{' (=p)' if m['worst_mode_is_k_eq_p'] else '    '}"
              f"  {m['modes_with_bits_below_0.01']}/{m['n_odd_modes']}")
    gen = [m for m in modes if m["c"][0] != 0 and m["c"][1] != 0]
    tz = [m for m in modes if m["c"][0] == 0 and m["c"][1] != 0]
    print(f"\n  GENERIC c (both components nonzero): worst-mode bits/pair"
          f" min={min(m['bits_per_pair_min'] for m in gen):.4f}"
          f" median={statistics.median([m['bits_per_pair_min'] for m in gen]):.4f}")
    print(f"  dead modes (<0.01 bits/pair) over generic rows: "
          f"{sum(m['modes_with_bits_below_0.01'] for m in gen)}")
    print(f"  TRACE-ZERO c: dead modes per row = "
          f"{[m['modes_with_bits_below_0.01'] for m in tz]}, "
          f"always at k = p: {all(m['worst_mode_is_k_eq_p'] for m in tz)}")

    # --- the sharp law ----------------------------------------------------
    print("\n== SHARP LAW test ==")
    print("  law A: c not in F_p and m >= log2(2p)+s  =>  S_m = Z/2p")
    for slack in (2, 3, 4, 5, 6):
        viol = [r for r in rows if r["c"][1] != 0
                and r["m_pairs_total"] >= math.log2(2 * r["p"]) + slack
                and not r["terminal_is_full"]]
        n_in = sum(1 for r in rows if r["c"][1] != 0
                   and r["m_pairs_total"] >= math.log2(2 * r["p"]) + slack)
        print(f"    s={slack}: rows={n_in:4d}  violations={len(viol)}"
              + ("" if not viol else
                 "  e.g. " + str([(v['p'], v['n'], v['m_pairs_total'],
                                   v['terminal_size']) for v in viol[:3]])))
    print("  law B: c not in F_p and m >= 2*(log2(2p)+s) => MN width = 2p")
    for slack in (2, 3, 4, 5):
        sel = [r for r in rows if r["c"][1] != 0
               and r["m_pairs_total"] >= 2 * (math.log2(2 * r["p"]) + slack)]
        viol = [r for r in sel if r["mn_width_max"] != 2 * r["p"]]
        print(f"    s={slack}: rows={len(sel):4d}  violations={len(viol)}"
              + ("" if not viol else
                 "  e.g. " + str([(v['p'], v['n'], v['m_pairs_total'],
                                   v['mn_width_max']) for v in viol[:3]])))


if __name__ == "__main__":
    main()
