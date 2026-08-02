#!/usr/bin/env python3
"""Aggregate the K1-by-order runs into the comparison table.

    tools/ramguard local -- python3 \
        notes/pilots_20260802/pb_selector_orders/k1_summary.py

Reads k1_Q*.json written by k1_orders.py, emits K1_TABLE.json and prints the
table.  Also computes (exactly) the budget-testability frontier: the scale at
which |Gamma_lo| > 8n^3 could even in principle be observed for a split-fibre
pencil.
"""

from __future__ import annotations

import json
import os
from fractions import Fraction
from math import comb

_HERE = os.path.dirname(os.path.abspath(__file__))

ORDER_SEQ = ["ORD-LEX", "ORD-COLEX", "ORD-VALEX", "ORD-VALCOLEX", "ORD-ERRLEX",
             "ORD-POLYLEX", "ORD-POLYHI", "ORD-POLYCENT", "ORD-CODEWORD",
             "ORD-DEGLEX", "ORD-SLOPEMAJOR",
             "ORD-HASH-pb-null-01", "ORD-HASH-pb-null-02"]
NULLS = ["ORD-HASH-pb-null-01", "ORD-HASH-pb-null-02"]
CASE_SEQ = ["Q3", "Q1", "Q2", "Q7", "Q8", "Q4", "Q5", "Q6", "Q10", "Q9",
            "Q12", "Q11"]


def is_prime(x):
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def isqrt(x):
    r = int(x ** 0.5)
    while r * r > x:
        r -= 1
    while (r + 1) ** 2 <= x:
        r += 1
    return r


def budget_frontier():
    """Smallest split-fibre scale at which the P-B budget is even testable.

    |Gamma_lo| <= #live <= min(q, #witnesses), #witnesses ~ C(n,A)/q^(h-1).
    Testability needs min(q, C(n,A)/q^(h-1)) > 8n^3, hence q > 8n^3 and
    C(n,A) > (8n^3)^h.  h >= m >= 2 always for a split-fibre pencil, so
    C(n,A) > (8n^3)^2 is a hard NECESSARY condition -- an obstruction that
    no choice of order, rate or field can dodge.

    For h = 2 the reachable ceiling is max_q min(q, C(n,A)/q), attained at
    q ~ sqrt(C(n,A)); the scan below picks the best admissible prime
    q = 1 mod n with q > 8n^3.
    """
    rows = []
    for n in range(16, 73, 4):
        budget = 8 * n ** 3
        for rate_num, rate_den, tag in ((1, 4, "1/4"), (1, 2, "1/2")):
            K = n * rate_num // rate_den
            if K < 4:
                continue
            A = K + 2                       # h = m = 2, the densest shape
            if A > n:
                continue
            C = comb(n, A)
            target = max(budget + 1, isqrt(C))
            q = target
            while not (q % n == 1 and is_prime(q)):
                q += 1
            wit = C // q                    # ~ witnesses at h = 2
            cap = min(q, wit)
            rows.append(dict(n=n, rate=tag, K=K, A=A, budget_8n3=budget,
                             q_opt=q, C_n_A=C,
                             witnesses_at_q=wit,
                             max_gamma_lo=cap,
                             headroom=(cap / budget),
                             required_retention=(budget / cap if cap
                                                 else float("inf")),
                             testable=cap > budget,
                             half_table_entries=2 ** (n // 2)))
    return rows


def main():
    cases = {}
    for name in CASE_SEQ:
        p = os.path.join(_HERE, f"k1_{name}.json")
        if os.path.exists(p):
            with open(p) as fh:
                cases[name] = json.load(fh)

    table = {}
    print("=" * 118)
    print("SCALES")
    print("=" * 118)
    print(f"{'case':5s} {'n':>3s} {'q':>4s} {'K':>3s} {'h':>2s} {'m':>2s} "
          f"{'A':>3s} {'witnesses':>10s} {'live':>5s} {'per-slope':>10s} "
          f"{'cand M':>7s} {'candGlo':>7s} {'8n^3':>7s} {'testable':>8s}")
    for name in CASE_SEQ:
        if name not in cases:
            continue
        d = cases[name]
        pr = d["parameters"]
        wc = d["witness_census"]
        cf = d["candidate_family"]
        per = Fraction(wc["total_exact_A_witnesses"], wc["live_slopes"])
        print(f"{name:5s} {pr['n']:3d} {pr['q']:4d} {pr['K']:3d} {pr['h']:2d} "
              f"{pr['m']:2d} {pr['A']:3d} "
              f"{wc['total_exact_A_witnesses']:10d} {wc['live_slopes']:5d} "
              f"{float(per):10.1f} {cf['size']:7d} {cf['gamma_lo_size']:7d} "
              f"{d['budget']['budget_8n3']:7d} "
              f"{str(d['budget']['budget_testable']):>8s}")
        table[name] = dict(parameters=pr, census=wc,
                           candidate_family_size=cf["size"],
                           candidate_gamma_lo=cf["gamma_lo_size"],
                           candidate_sidon=cf["sidon"],
                           candidate_budget_ratio=cf["budget_ratio"],
                           budget=d["budget"],
                           checks_total=d["checks_total"],
                           checks_all_pass=d["checks_all_pass"],
                           slopemajor_degenerate=d["extra_checks"][
                               "slopemajor_equals_polylex"],
                           prior_crosscheck=d["prior_crosscheck"],
                           orders={})

    print()
    print("=" * 118)
    print("K1 COMPARISON TABLE   Glo/live (retention) | budget ratio "
          "Glo/8n^3 | class | K1-mech | contrast vs null")
    print("=" * 118)
    for name in CASE_SEQ:
        if name not in cases:
            continue
        d = cases[name]
        pr = d["parameters"]
        wc = d["witness_census"]
        nullret = [Fraction(d["orders"][o]["gamma_lo_size"], wc["live_slopes"])
                   for o in NULLS]
        nullmean = sum(nullret) / len(nullret)
        print(f"-- {name}  n={pr['n']} q={pr['q']} K={pr['K']} h={pr['h']} "
              f"m={pr['m']} A={pr['A']} live={wc['live_slopes']} "
              f"|W_z|~{wc['total_exact_A_witnesses']//wc['live_slopes']} "
              f"budget={d['budget']['budget_8n3']}")
        for o in ORDER_SEQ:
            s = d["orders"][o]
            glo = s["gamma_lo_size"]
            live = s["live_slopes"]
            ret = Fraction(glo, live)
            br = Fraction(glo, s["budget_8n3"])
            contrast = (float(ret / nullmean) if nullmean > 0
                        else float("nan"))
            print(f"   {o:22s} {glo:4d}/{live:<4d} ({float(ret):5.3f}) "
                  f"| {str(br):>12s} ({float(br):9.3e}) "
                  f"| {s['selected_class']:17s} | {s['k1_verdict']:5s} "
                  f"| x{contrast:6.3f} "
                  f"| sidon={str(s['sidon']):5s} mult={s['max_multiplicity']:3d}"
                  f" greedy={s['greedy_lowcore_subfamily']:4d}"
                  f" pref={s['common_prefix_len']:2d}"
                  f" intended1st={s['intended_is_first_match']}"
                  f"/{s['candidate_family_size']}")
            table[name]["orders"][o] = dict(
                gamma_lo=glo, live=live,
                retention=f"{glo}/{live}", retention_float=float(ret),
                budget_ratio=f"{glo}/{s['budget_8n3']}",
                budget_ratio_float=float(br),
                budget_violated=s["budget_violated"],
                selected_class=s["selected_class"],
                k1_mech_verdict=s["k1_verdict"],
                contrast_vs_null=contrast,
                sidon=s["sidon"], max_multiplicity=s["max_multiplicity"],
                greedy_lowcore_subfamily=s["greedy_lowcore_subfamily"],
                max_pairwise_intersection=s["max_pairwise_intersection"],
                common_prefix_len=s["common_prefix_len"],
                intended_is_first_match=s["intended_is_first_match"],
                candidate_family_size=s["candidate_family_size"],
                counterfactual_gamma_lo=s[
                    "counterfactual_intended_normative"]["gamma_lo_size"],
                counterfactual_candidate_slopes_in_gamma_lo=s[
                    "counterfactual_intended_normative"][
                        "candidate_slopes_in_gamma_lo"],
            )
        print()

    # density trend, support-keyed vs polynomial-keyed vs null
    print("=" * 118)
    print("DENSITY TREND (retention; support-keyed should FALL as |W_z| grows)")
    print("=" * 118)
    groups = {"rate 1/4, h=2 (m=2)": ["Q4", "Q5", "Q6"],
              "rate 1/4, h=3 (m=2)": ["Q7", "Q8"],
              "rate 1/2, h=2 (m=2)": ["Q9", "Q12"],
              "n=16, rate 1/4": ["Q1", "Q2", "Q3"]}
    trends = {}
    for gname, members in groups.items():
        print(f"-- {gname}")
        rows = []
        for name in members:
            if name not in cases:
                continue
            d = cases[name]
            wc = d["witness_census"]
            dens = wc["total_exact_A_witnesses"] // wc["live_slopes"]
            r = {o: Fraction(d["orders"][o]["gamma_lo_size"],
                             wc["live_slopes"]) for o in ORDER_SEQ}
            supp = max(r[o] for o in ORDER_SEQ[:5])
            poly = min(r[o] for o in ("ORD-POLYLEX", "ORD-POLYCENT"))
            nul = sum(r[o] for o in NULLS) / 2
            print(f"   {name:4s} q={d['parameters']['q']:4d} "
                  f"|W_z|~{dens:6d}  worst support-keyed={float(supp):5.3f}  "
                  f"best-of-polylex/cent={float(poly):5.3f}  "
                  f"null={float(nul):5.3f}  "
                  f"contrast={float(supp/nul) if nul else float('nan'):6.3f}")
            rows.append(dict(case=name, q=d["parameters"]["q"],
                             witnesses_per_slope=dens,
                             worst_support_keyed=float(supp),
                             polynomial_keyed=float(poly),
                             null=float(nul),
                             contrast=(float(supp / nul) if nul else None)))
        trends[gname] = rows
        print()

    print("=" * 118)
    print("BUDGET TESTABILITY FRONTIER (h = m = 2, the densest split-fibre "
          "shape)")
    print("=" * 118)
    fr = budget_frontier()
    print(f"{'n':>3s} {'rate':>5s} {'K':>3s} {'A':>3s} {'8n^3':>9s} "
          f"{'q_opt':>10s} {'C(n,A)':>20s} {'witnesses':>14s} "
          f"{'max|Glo|':>12s} {'headroom':>9s} {'need ret':>9s} "
          f"{'testable':>8s} {'half-table':>12s}")
    for r in fr:
        print(f"{r['n']:3d} {r['rate']:>5s} {r['K']:3d} {r['A']:3d} "
              f"{r['budget_8n3']:9d} {r['q_opt']:10d} {r['C_n_A']:20d} "
              f"{r['witnesses_at_q']:14d} {r['max_gamma_lo']:12d} "
              f"{r['headroom']:9.3f} {r['required_retention']:9.4f} "
              f"{str(r['testable']):>8s} {r['half_table_entries']:12d}")
    first = [r for r in fr if r["testable"]]
    print(f"\nfirst testable split-fibre scale: "
          f"{first[0] if first else 'none in range'}")

    print()
    print("=" * 118)
    print("CONCENTRATION OF THE SELECTED SUPPORTS (mechanism evidence, "
          "n = 32 only)")
    print("=" * 118)
    print(f"{'case':5s} {'order':22s} {'common coords':>13s} "
          f"{'window':>7s} {'prefix':>7s} {'maxcore':>8s} {'K':>3s} "
          f"{'A':>3s} {'Glo/live':>10s}")
    conc = {}
    for name in CASE_SEQ:
        if name not in cases or cases[name]["parameters"]["n"] != 32:
            continue
        d = cases[name]
        pr = d["parameters"]
        for o in ORDER_SEQ:
            s = d["orders"][o]
            print(f"{name:5s} {o:22s} {s['common_coordinates']:13d} "
                  f"{s['window_width']:7d} {s['common_prefix_len']:7d} "
                  f"{s['max_pairwise_intersection']:8d} {pr['K']:3d} "
                  f"{pr['A']:3d} "
                  f"{s['gamma_lo_size']:4d}/{s['live_slopes']:<5d}")
            conc.setdefault(name, {})[o] = dict(
                common_coordinates=s["common_coordinates"],
                window_width=s["window_width"],
                common_prefix_len=s["common_prefix_len"],
                max_pairwise_intersection=s["max_pairwise_intersection"])
        print()

    out = dict(cases=table, density_trends=trends,
               budget_frontier=fr, concentration=conc,
               first_testable=(first[0] if first else None))
    path = os.path.join(_HERE, "K1_TABLE.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(f"\n-> {path}")


if __name__ == "__main__":
    main()
