#!/usr/bin/env python3
"""Carry-DFT L1 mass: verify the logarithmic law and identify its constant.

Run:  tools/ramguard local -- python3 \
        notes/pilots_20260802/f2_carry_reachability/dft_mass.py

hhat_p(k) = 0 (k even), 4/(1 - e^{-i pi k/p}) (k odd), so
|hhat_p(k)| = 2 / |sin(pi k / 2p)| and

    L1(p) / (2p) = (1/p) * sum_{j=0}^{p-1} 1 / sin(pi (2j+1) / (2p)).

Claim (verified below): L1(p)/(2p) = (2/pi) (ln p + gamma + ln(8/pi))
                                    + O(1/p^2).
"""

from __future__ import annotations

import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results")

GAMMA = 0.57721566490153286060651209008240243104215933593992


def l1_normalized(p: int) -> float:
    two_p = 2 * p
    return sum(1.0 / math.sin(math.pi * (2 * j + 1) / two_p)
               for j in range(p)) / p


def predicted(p: int) -> float:
    return (2.0 / math.pi) * (math.log(p) + GAMMA + math.log(8.0 / math.pi))


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    rows = []
    ps = [7, 11, 13, 17, 31, 61, 101, 199, 401, 1009, 4001, 10007,
          40009, 100003, 400009, 1000003]
    print(f"{'p':>9} {'L1/(2p)':>12} {'predicted':>12} {'residual':>12}"
          f" {'resid*p^2':>12}")
    for p in ps:
        v = l1_normalized(p)
        pr = predicted(p)
        res = v - pr
        rows.append({"p": p, "l1_over_2p": v, "predicted": pr,
                     "residual": res})
        print(f"{p:9d} {v:12.8f} {pr:12.8f} {res:12.3e} {res*p*p:12.5f}")
    # the constant is (2/pi)(gamma + ln(8/pi))
    const = (2.0 / math.pi) * (GAMMA + math.log(8.0 / math.pi))
    print(f"\nconstant (2/pi)(gamma + ln(8/pi)) = {const:.10f}")
    print("law: L1(p)/(2p) = (2/pi) ln p + %.8f + O(p^-2)" % const)
    growth = [(rows[i + 1]["l1_over_2p"] - rows[i]["l1_over_2p"])
              / (math.log(rows[i + 1]["p"]) - math.log(rows[i]["p"]))
              for i in range(len(rows) - 1)]
    print(f"empirical d(L1/2p)/d(ln p): last = {growth[-1]:.8f}"
          f"  vs 2/pi = {2/math.pi:.8f}")
    with open(os.path.join(OUT, "carry_dft_mass.json"), "w") as f:
        json.dump({"constant_2_over_pi_times_gamma_plus_ln8overpi": const,
                   "slope_2_over_pi": 2 / math.pi,
                   "rows": rows}, f, indent=1)
    print("F2A2_DFT_MASS_DONE")


if __name__ == "__main__":
    main()
