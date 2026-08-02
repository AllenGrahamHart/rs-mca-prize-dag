#!/usr/bin/env python3
"""FM2 aggregation: read results_<case>.json, emit RESULTS.json + the tables
quoted in REPORT.md.

    tools/ramguard tiny -- python3 \
        notes/pilots_20260802/pb_split_fibre_selector/fm2_aggregate.py

Exact integer arithmetic throughout; the only floats are printed ratios,
which carry their exact numerator/denominator in RESULTS.json.
"""

from __future__ import annotations

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CASES = ["P1", "P2", "P3", "P4", "P5", "P6", "P7",
         "P4b", "P4c", "P4d"]
# competition depth threshold below which a case cannot test the question
DEEP = 50


def load(c):
    with open(os.path.join(HERE, f"results_{c}.json")) as fh:
        return json.load(fh)


def verdict(res) -> dict:
    """Pre-registered outcome adjudication for one case, per order."""
    K = res["parameters"]["K"]
    wc = res["witness_census"]
    cand = res["candidate_family"]
    deep = wc["min_witnesses_per_live_slope"] >= DEEP
    out = {}
    for o, st in res["selected_family"].items():
        cf = st["counterfactual_intended_normative"]
        collapse_num = st["gamma_lo_size"]
        collapse_den = cf["candidate_slopes_in_gamma_lo"]
        if not deep:
            v = "OUTCOME-U (no competition: selector has (almost) no choice)"
        elif collapse_den and collapse_num * 4 <= collapse_den:
            v = "OUTCOME-A (selector compresses)"
        elif st["sidon"] and st["gamma_lo_size"] * 2 >= st["live_slopes"]:
            v = "OUTCOME-K1 (selector retains a low-core Sidon family)"
        else:
            v = "OUTCOME-U (indeterminate at this scale)"
        out[o] = dict(
            verdict=v,
            gamma_lo_selected=collapse_num,
            gamma_lo_counterfactual=collapse_den,
            live_slopes=st["live_slopes"],
            candidate_family_size=cand["size"],
            intended_is_first_match=st["intended_is_first_match"],
            selected_is_sidon=st["sidon"],
            selected_max_difference_multiplicity=st["max_multiplicity"],
            selected_max_pairwise_core=st["max_pairwise_intersection"],
            K_minus_1=K - 1,
            greedy_lowcore_subfamily=st["greedy_lowcore_subfamily"],
            common_prefix_len=st["common_prefix_len"],
            full_initial_block_slopes=st["full_initial_block_slopes"],
            initial_block_size=st["initial_block_size"],
            window_width=st["window_width"],
            unallocated_slopes_bridge_gap=st["unallocated_slopes_bridge_gap"],
            pairs_core_above_K=st["pairs_core_above_K"],
        )
    return out


def main() -> None:
    agg = {"cases": {}, "notes": {
        "selector": "pilot orders, see SELECTOR_MANIFEST.md (NOT ratified)",
        "deep_competition_threshold": DEEP,
        "outcome_A_rule": "gamma_lo(selected) <= gamma_lo(counterfactual)/4",
        "outcome_K1_rule": ("selected family Sidon AND gamma_lo >= half the "
                            "live slopes"),
    }}
    rows = []
    for c in CASES:
        res = load(c)
        v = verdict(res)
        agg["cases"][c] = dict(parameters=res["parameters"],
                               witness_census={
                                   k: res["witness_census"][k] for k in
                                   ("total_exact_A_witnesses", "live_slopes",
                                    "dead_slopes",
                                    "min_witnesses_per_live_slope",
                                    "max_witnesses_per_live_slope")},
                               budget=res["budget"],
                               candidate_family={
                                   k: res["candidate_family"][k] for k in
                                   ("size", "sidon", "distinct_differences",
                                    "ordered_pairs", "additive_energy",
                                    "max_pairwise_intersection",
                                    "gamma_lo_size")},
                               per_order=v,
                               checks_passed=sum(1 for x in res["checks"]
                                                 if x["ok"]),
                               checks_total=len(res["checks"]))
        for o, d in v.items():
            rows.append((c, o, d))

    with open(os.path.join(HERE, "RESULTS.json"), "w") as fh:
        json.dump(agg, fh, indent=1, sort_keys=True)

    hdr = (f"{'case':4s} {'order':22s} {'M':>4s} {'live':>5s} "
           f"{'wit/slope':>10s} {'lo_sel':>7s} {'lo_cf':>6s} {'1st':>6s} "
           f"{'sidon':>6s} {'mult':>5s} {'cap':>4s} {'blk':>7s} {'win':>4s} "
           f"{'gap':>4s}  verdict")
    print(hdr)
    print("-" * len(hdr))
    for c, o, d in rows:
        res = agg["cases"][c]
        wc = res["witness_census"]
        print(f"{c:4s} {o:22s} {d['candidate_family_size']:4d} "
              f"{d['live_slopes']:5d} "
              f"{wc['min_witnesses_per_live_slope']:4d}-"
              f"{wc['max_witnesses_per_live_slope']:<5d} "
              f"{d['gamma_lo_selected']:7d} {d['gamma_lo_counterfactual']:6d} "
              f"{d['intended_is_first_match']:6d} "
              f"{str(d['selected_is_sidon']):>6s} "
              f"{d['selected_max_difference_multiplicity']:5d} "
              f"{d['selected_max_pairwise_core']:4d} "
              f"{d['full_initial_block_slopes']:3d}/"
              f"{d['initial_block_size']:<3d} "
              f"{d['window_width']:4d} "
              f"{d['unallocated_slopes_bridge_gap']:4d}  {d['verdict']}")
    print()
    print("legend: M=candidate family size; lo_sel=|Gamma_lo| of the SELECTED "
          "family; lo_cf=|Gamma_lo| in the counterfactual where the intended "
          "witnesses ARE normative; 1st=# candidate slopes whose intended "
          "witness is the first match; mult=max oriented-difference "
          "multiplicity; cap=max pairwise core (K-1 is the low-core bar); "
          "blk=#slopes whose selected support contains the initial block "
          "{0..A-h-1}; win=width of the smallest index window containing "
          "every selected support; gap=#slopes with a core >= K+1 but none "
          "== K (outside the bridge's hi/lo dichotomy as literally written).")
    print(f"\n-> {os.path.join(HERE, 'RESULTS.json')}")


if __name__ == "__main__":
    main()
