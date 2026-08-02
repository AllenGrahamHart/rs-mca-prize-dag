#!/usr/bin/env python3
"""The official-scale budget arithmetic for the fixed-sector absorption question.

Pure arithmetic on the banked official parameters -- no model, no extrapolation.
Every quantity is an exact Fraction / integer except the labelled `_float` logs.

Official parameters (citations in REPORT):
  p = KoalaBear = 2^31 - 2^24 + 1, p-1 = 2^24 * 127, e = v_2(p-1) = 24
      [notes/f2_campaign/F2_CAMPAIGN_LOG.md:2036; deployed-windows tower.py:87]
  n = 2^40 (subgroup order at prize-max; ambient N = 2^41)
      [deployed-windows REPORT.md:17]
  FIXED sector  n_0 = gcd(n, p-1) = 2^24, in the analytic regime
      (n_0 = 2^24 >= 3 sqrt(p) = 2^17.1) [F2_CAMPAIGN_LOG.md:1400-1402]
  RUNG j (j = 1..16): n_j = 2^{24+j}, moving elements 2^{23+j},
      m_j = 2^{22+j} antipodal pairs  [F2_CAMPAIGN_LOG.md:1412-1430; tower.py:15-20]
  slice budgets eta = 1/43 (viable variant) and eta = 1/3
      [F2_SLICE_THEOREM_DRAFT.md:63-73]
  deployed parity-pure ceiling: log2 p bits per rung at K1, 0 bits at K2
      [deployed-windows REPORT.md:39,51; E4_budget_per_rung.json]
  per-coordinate slice ceiling Lambda_max(beta) = log2(1/max(beta,1-beta)) <= 1
      [F2_SLICE_THEOREM_DRAFT.md:64-65]
"""
from __future__ import annotations

import json
import math
import os
import sys
from fractions import Fraction

sys.dont_write_bytecode = True
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import core as C  # noqa: E402

KOALABEAR = (1 << 31) - (1 << 24) + 1
E = 24
N_GROUP = 1 << 40
RUNGS = range(1, 17)
LOG2P = math.log2(KOALABEAR)


def main():
    p = KOALABEAR
    n0 = 1 << E
    assert math.gcd(N_GROUP, p - 1) == n0
    out = {"p": p, "log2_p_float": LOG2P, "e": E, "n": N_GROUP, "n0": n0,
           "fixed_share_of_group": str(Fraction(n0, N_GROUP)),
           "fixed_share_float": n0 / N_GROUP, "rows": []}

    # ---- fixed-sector CAPACITY: three honest upper bounds, all exact --------
    # (i) size cap: at most Lambda_max <= 1 bit per element (beta = 1/2)
    cap_size = n0
    # (ii) proved-currency cap: the k=1 contraction theorem gives per-condition
    #      rho <= 3.71/p, i.e. log2(p/3.71) bits per p-free condition, and the
    #      sector's total entropy is n0 bits, so at most n0/log2(p/3.71)
    #      conditions can be paid before the sector is exhausted.
    bits_per_condition = math.log2(p / 3.71)
    max_conditions = n0 / bits_per_condition
    # (iii) slice-statistic cap: the fixed sector enters a rung's V_b only
    #      through the scalar `base` in Z/2p -> exactly 0 bits (see REPORT).
    cap_slice = 0
    out["fixed_capacity"] = {
        "size_cap_bits": cap_size,
        "proved_bits_per_pfree_condition_float": bits_per_condition,
        "max_conditions_before_exhaustion_float": max_conditions,
        "slice_statistic_cap_bits": cap_slice,
    }

    tot_m = 0
    for j in RUNGS:
        m_j = 1 << (22 + j)
        tot_m += m_j
        row = {"rung": j, "n_j": 1 << (24 + j), "m_pairs": m_j,
               "budget_1_43_bits": str(Fraction(m_j, 43)),
               "budget_1_43_float": m_j / 43,
               "budget_1_3_bits": str(Fraction(m_j, 3)),
               "budget_1_3_float": m_j / 3,
               "K1_ceiling_bits_float": LOG2P,
               "K2_ceiling_bits": 0,
               "deficit_K1_1_43_float": m_j / 43 - LOG2P,
               "deficit_K2_1_43_float": m_j / 43,
               "fixed_capacity_covers_this_rung_1_43":
                   (m_j / 43 - LOG2P) <= cap_size,
               "deficit_over_fixed_capacity_float":
                   (m_j / 43 - LOG2P) / cap_size}
        out["rows"].append(row)

    assert tot_m == (1 << 39) - (1 << 23)
    tot_budget_43 = Fraction(tot_m, 43)
    tot_budget_3 = Fraction(tot_m, 3)
    tot_ceiling_K1 = 16 * LOG2P
    out["totals"] = {
        "sum_m_pairs": tot_m,
        "sum_m_pairs_exact": str(Fraction(tot_m)),
        "check_elements": n0 + 2 * tot_m,
        "budget_1_43_bits_float": float(tot_budget_43),
        "budget_1_3_bits_float": float(tot_budget_3),
        "K1_total_delivered_bits_float": tot_ceiling_K1,
        "K2_total_delivered_bits": 0,
        "deficit_K1_1_43_float": float(tot_budget_43) - tot_ceiling_K1,
        "deficit_K2_1_43_float": float(tot_budget_43),
        "shortfall_ratio_K1_1_43_float":
            (float(tot_budget_43) - tot_ceiling_K1) / cap_size,
        "shortfall_ratio_K2_1_43_float": float(tot_budget_43) / cap_size,
        "shortfall_ratio_K1_1_3_float":
            (float(tot_budget_3) - tot_ceiling_K1) / cap_size,
        "first_rung_whose_deficit_exceeds_whole_fixed_capacity":
            min(j for j in RUNGS if (1 << (22 + j)) / 43 - LOG2P > cap_size),
    }

    # ---- the annealed (alignment-bound) reading -----------------------------
    # generic annealed constant per element: 4/pi ; per antipodal PAIR (4/pi)^2
    # parity-pure per pair: E[|1+psi|^2] = 2 exactly.
    per_pair_generic = (4 / math.pi) ** 2
    per_pair_pure = 2.0
    excess_bits_per_pair = math.log2(per_pair_pure / per_pair_generic)
    n_pairs = N_GROUP // 2
    out["annealed"] = {
        "per_pair_generic_float": per_pair_generic,
        "per_pair_parity_pure": per_pair_pure,
        "excess_bits_per_pair_float": excess_bits_per_pair,
        "total_excess_bits_float": excess_bits_per_pair * n_pairs,
        "generic_annealed_exponent_float": math.log2(4 / math.pi),
        "parity_pure_annealed_exponent_float": 0.5,
        "note": ("the alignment bound's RHS is 2^{o(n)} sqrt(sum exp(2S)) ~ "
                 "2^{o(n)} q^{t/2} 2^{n/2}; the parity-pure class has "
                 "population q^{t/2} and first-moment mass 2^{n/2} EXACTLY -- "
                 "a dead heat with zero structural margin, payable only out of "
                 "the consumer's 2^{o(n)} tolerance"),
    }

    C.dump("C5_official_budget.json", out)

    print(f"p = {p} (log2 = {LOG2P:.4f}), e = {E}, n = 2^40, n0 = 2^24")
    print(f"fixed share of the group: 2^-16 = {n0/N_GROUP:.3e}")
    print(f"fixed-sector capacity (1 bit/element hard cap): {cap_size} bits "
          f"= 2^{math.log2(cap_size):.0f}")
    print()
    print(f"{'rung':>4} {'m_j':>14} {'need 1/43':>14} {'K1 gets':>9} "
          f"{'deficit':>14} {'deficit/cap':>12}")
    for r in out["rows"]:
        print(f"{r['rung']:>4} 2^{math.log2(r['m_pairs']):>4.0f}{'':>8} "
              f"{r['budget_1_43_float']:>14.4e} {LOG2P:>9.2f} "
              f"{r['deficit_K1_1_43_float']:>14.4e} "
              f"{r['deficit_over_fixed_capacity_float']:>12.4f}")
    t = out["totals"]
    print()
    print(f"TOTAL 1/43 budget over the 16 rungs : "
          f"{t['budget_1_43_bits_float']:.6e} bits")
    print(f"K1 delivers (16 x log2 p)          : "
          f"{t['K1_total_delivered_bits_float']:.2f} bits")
    print(f"K2 delivers                        : 0 bits (rho_b = 1 exactly)")
    print(f"fixed-sector capacity              : {cap_size} bits")
    print(f"shortfall ratio (K1, 1/43)         : "
          f"{t['shortfall_ratio_K1_1_43_float']:.2f} x the whole fixed sector")
    print(f"shortfall ratio (K2, 1/43)         : "
          f"{t['shortfall_ratio_K2_1_43_float']:.2f} x")
    print(f"shortfall ratio (K1, 1/3)          : "
          f"{t['shortfall_ratio_K1_1_3_float']:.2f} x")
    print(f"first rung whose OWN 1/43 deficit exceeds the entire fixed sector: "
          f"j = {t['first_rung_whose_deficit_exceeds_whole_fixed_capacity']}")
    print()
    a = out["annealed"]
    print(f"annealed: parity-pure mass 2^(n/2) vs generic (4/pi)^n = "
          f"2^({a['generic_annealed_exponent_float']:.4f} n); excess "
          f"{a['excess_bits_per_pair_float']:.5f} bits/pair = "
          f"{a['total_excess_bits_float']:.4e} bits at n = 2^40")


if __name__ == "__main__":
    main()
