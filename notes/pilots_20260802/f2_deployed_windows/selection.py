#!/usr/bin/env python3
"""The COST of the frequency-selection step, per rung.  Exact integers.

The deployed rung-j window is degenerate exactly when the EVEN part of the
frequency vanishes on the sector (moment.py).  In coordinates:

  y ranges over the 2^{e+j} - 2^{e+j-1} = 2^{e+j-1} genuine elements of
  mu_{n_j}, i.e. over y_0 * mu_{2^{e+j-1}};  for EVEN l, y^l lies in the
  subfield fixed by the descent's Frobenius, so

      A(y) = Tr(f_even(y)) = sum_{l even} Tr(c_l) * y^l,

  an F_p-linear combination of the F_p-valued functions y -> y^l.  Even-l
  characters of mu_{2^{e+j-1}} span a space of F_p-dimension
  m_j = 2^{e+j-2} (they are exactly the functions invariant under y -> -y).

  A == 0  is therefore  codim_j := min( m_j , #{even l <= t} )  independent
  F_p-conditions on the frequency, so the DEGENERATE CLASS has density
  p^{-codim_j} inside the q^t frequency population.

  Excluding it by counting is worth  codim_j * log2 p  bits.  It pays for
  itself only if that exceeds the whole consumer allowance
  TOLERANCE_BITS = 1.05e12 (verify_brief5_f2_myerson_program_arithmetic.py:24),
  because inside the class the moving sector contributes NO sign cancellation
  at all (the sign is constant there -- antipodal pairs give |1+psi|^2 >= 0
  and the b-resolved statistic is pinned at rho_b >= 1/p).
"""
from __future__ import annotations

import math
import os
import sys
from fractions import Fraction

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import deployed as DP  # noqa: E402
import tower as TW  # noqa: E402

TOLERANCE_BITS = 1_050_000_000_000        # brief-5 verifier :24
FREQUENCY_BITS_PROXY = 2_150_000_000_000  # t * log2 q, brief-5 verifier :244
T_CONDITIONS = 70_000_000_000             # t ~ 7e10 (F2_NEWTON_EMPTY_EXTREMES)
LOG2_P = 31                               # KoalaBear p ~ 2^31
E = 24                                    # v_2(p-1) = 24


def main():
    rows = []
    even_l = T_CONDITIONS // 2
    for j in TW.OFFICIAL_RUNGS:
        rp = TW.rung_params(E, j)
        m_j = rp["m_pairs"]
        codim = min(m_j, even_l)
        saving = codim * LOG2_P
        rows.append({
            "rung": j,
            "n_ord": rp["n_ord"], "log2_n_ord": E + j,
            "m_pairs": m_j, "log2_m": math.log2(m_j),
            "codim_Fp_conditions": codim,
            "degenerate_density_log2": -saving,
            "exclusion_saving_bits": saving,
            "allowance_bits": TOLERANCE_BITS,
            "selection_pays_for_itself": saving >= TOLERANCE_BITS,
            "shortfall_bits": TOLERANCE_BITS - saving,
            "budget_1_43_bits_on_m": Fraction(m_j, 43),
            "budget_1_43_bits_on_n": Fraction(rp["n_ord"], 43),
            "deployed_ceiling_bits": LOG2_P,
        })
    DP.dump("E7_selection_cost.json",
            {"rows": rows, "tolerance_bits": TOLERANCE_BITS,
             "t_conditions": T_CONDITIONS, "log2_p": LOG2_P, "e": E})

    print(f"{'rung':>4} {'log2 n_j':>9} {'log2 m_j':>9} {'codim (F_p)':>14} "
          f"{'exclusion saving':>18} {'>= 1.05e12?':>12}")
    for r in rows:
        print(f"{r['rung']:>4} {r['log2_n_ord']:>9} {r['log2_m']:>9.0f} "
              f"{r['codim_Fp_conditions']:>14.4e} "
              f"{r['exclusion_saving_bits']:>18.4e} "
              f"{'YES' if r['selection_pays_for_itself'] else 'no':>12}")
    first = next((r["rung"] for r in rows if r["selection_pays_for_itself"]),
                 None)
    print(f"\nfirst rung at which frequency-selection pays for itself by "
          f"counting alone: j = {first}")
    tot_m = sum(r["m_pairs"] for r in rows)
    tot_n = sum(r["n_ord"] for r in rows)
    print(f"sum of m_j = {tot_m} = 2^39 - 2^23 (exact: "
          f"{tot_m == (1 << 39) - (1 << 23)})")
    print(f"sum of n_j = {tot_n} = 2^41 - 2^25 (exact: "
          f"{tot_n == (1 << 41) - (1 << 25)})")
    print(f"1/43 budget on the PAIR count: {float(Fraction(tot_m,43)):.4e} bits "
          f"(fits allowance: {Fraction(tot_m,43) < TOLERANCE_BITS})")
    print(f"1/43 budget on the SUBGROUP count: {float(Fraction(tot_n,43)):.4e} "
          f"bits (fits allowance: {Fraction(tot_n,43) < TOLERANCE_BITS})")
    print(f"what the DEGENERATE deployed window delivers, all 16 rungs "
          f"together: 16 x {LOG2_P} = {16*LOG2_P} bits")
    print(f"shortfall factor at rung 1 (1/43 on pairs): "
          f"{float(Fraction((1<<23),43))/LOG2_P:.4e}x")


if __name__ == "__main__":
    main()
