#!/usr/bin/env python3
"""dli_norm_gate -- LN2/LN4/LN5 tested at DEEPER junctions of the real DLI tower.

Junction j of the C2'' tower: level-(j+1) state M in {0..2^{j+1}}^{h_{j+1}},
skew d_i in {-c_i, -c_i+2, ..., c_i} with c_i = min(M_i, 2^{j+1}-M_i), and the
junction constraint  sum_i d_i zeta_{h_j}^{u i} = 0  for every u in U_j.

The skew element is  delta = sum_{i < h_{j+1}} d_i zeta_{h_j}^i  in Z[zeta_{h_j}],
and i runs over exactly the basis range 0..phi(h_j)-1 = 0..h_{j+1}-1, so there
are NO opposite pairs and delta = 0 only for d = 0.  Predictions:

  LN2 : every nonzero solution has  q^{L_j} | Norm(delta),
  LN4 : 1 <= Norm(delta) <= E^{h_{j+1}/2},  E = sum_i d_i^2,
  LN5 : hence every nonzero solution has  E^{h_{j+1}/2} >= q^{L_j}.
"""

from __future__ import annotations

import json
import random
import sys
from itertools import product as iproduct
from pathlib import Path

sys.dont_write_bytecode = True

from core import get_zeta, norm_cyclotomic

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def blocks(t):
    out, j = [], 0
    while 2**j <= t:
        out.append([u for u in range(1, t // 2**j + 1, 2)])
        j += 1
    return out


def junction_scan(n, t, q, j, n_states, seed=20260802):
    B = blocks(t)
    U = B[j]
    L = len(U)
    hj = n // 2**j                     # order of the level-j root
    cells = hj // 2                    # = phi(h_j) = h_{j+1}
    z = get_zeta(q, n)
    zj = pow(z, 2**j, q)               # primitive h_j-th root
    cols = [tuple(pow(zj, (u * i) % hj, q) for u in U) for i in range(cells)]
    rnd = random.Random(seed)
    rows = []
    tot_sol = tot_states = 0
    viol_ln2 = viol_ln4 = viol_ln5 = 0
    excl_states = excl_sol = 0
    for _ in range(n_states):
        M = [rnd.randrange(0, 2**(j + 1) + 1) for _ in range(cells)]
        c = [min(m, 2**(j + 1) - m) for m in M]
        doms = [list(range(-ci, ci + 1, 2)) for ci in c]
        size = 1
        for d in doms:
            size *= len(d)
        if size > 200000:
            continue
        tot_states += 1
        Emax = sum(ci * ci for ci in c)
        excluded = Emax ** (cells // 2) < q**L
        nsol = 0
        for d in iproduct(*doms):
            if any(sum(d[i] * cols[i][a] for i in range(cells)) % q
                   for a in range(L)):
                continue
            if not any(d):
                continue                      # d = 0 is the trivial solution
            nsol += 1
            E = sum(v * v for v in d)
            Nz = norm_cyclotomic(list(d), cells)
            if Nz % q**L != 0:
                viol_ln2 += 1
            if not (1 <= Nz <= E ** (cells // 2)):
                viol_ln4 += 1
            if E ** (cells // 2) < q**L:
                viol_ln5 += 1
        tot_sol += nsol
        if excluded:
            excl_states += 1
            excl_sol += nsol
    return {"n": n, "t": t, "q": q, "j": j, "L_j": L, "cells_phi": cells,
            "root_order_h_j": hj, "states_scanned": tot_states,
            "nonzero_solutions_found": tot_sol,
            "LN2_violations_qL_divides_Norm": viol_ln2,
            "LN4_violations_norm_in_1_to_E_pow_phi_half": viol_ln4,
            "LN5_violations_E_pow_phi_half_ge_q_pow_L": viol_ln5,
            "states_predicted_empty_by_router": excl_states,
            "nonzero_solutions_in_predicted_empty_states": excl_sol,
            "router_prediction_holds": excl_sol == 0}


def main():
    out = []
    jobs = [(32, 8, 97, 0, 400), (32, 8, 97, 1, 400), (32, 8, 97, 2, 800),
            (32, 8, 193, 1, 400), (32, 8, 257, 1, 400),
            (64, 8, 193, 1, 200), (64, 8, 193, 2, 400),
            (32, 16, 97, 1, 400), (32, 16, 97, 2, 600)]
    for (n, t, q, j, ns) in jobs:
        r = junction_scan(n, t, q, j, ns)
        out.append(r)
        print(f"n={n} t={t} q={q} j={j}: L={r['L_j']} cells={r['cells_phi']} "
              f"states={r['states_scanned']} sols={r['nonzero_solutions_found']} "
              f"LN2v={r['LN2_violations_qL_divides_Norm']} "
              f"LN4v={r['LN4_violations_norm_in_1_to_E_pow_phi_half']} "
              f"LN5v={r['LN5_violations_E_pow_phi_half_ge_q_pow_L']} "
              f"router-empty states={r['states_predicted_empty_by_router']} "
              f"sols-there={r['nonzero_solutions_in_predicted_empty_states']}")
    ok = all(r["LN2_violations_qL_divides_Norm"] == 0
             and r["LN4_violations_norm_in_1_to_E_pow_phi_half"] == 0
             and r["LN5_violations_E_pow_phi_half_ge_q_pow_L"] == 0
             and r["router_prediction_holds"] for r in out)
    print("\nALL TOWER-JUNCTION PREDICTIONS HOLD:", ok)
    (ROOT / "results" / "tower.json").write_text(
        json.dumps({"all_hold": ok, "rows": out}, indent=1))


if __name__ == "__main__":
    main()
