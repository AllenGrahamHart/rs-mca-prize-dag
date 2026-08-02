#!/usr/bin/env python3
"""FM2 supplement — what does the SELECTED support actually look like?

For one case: witness-polynomial degrees, fibre content, and how large the
split-fibre-shaped subpopulation of W_z is compared with the whole of W_z.

    tools/ramguard local -- python3 \
        notes/pilots_20260802/pb_split_fibre_selector/fm2_shape_probe.py P4
"""

from __future__ import annotations

import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pb_split_fibre_pilot as P  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else "P4"
    case = P.Case(name, P.CASES[name])
    case.build_family()
    n, q, A, K, m = case.n, case.q, case.A, case.K, case.m

    # fibre-shaped supports: core + a complete fibres drawn from the b labels
    core = set(case.core_idx)
    fibre_of = {}
    for j, fib in enumerate(case.fibre_idx):
        for i in fib:
            fibre_of[i] = j

    fz_cache: dict = {}
    per_slope_total: Counter = Counter()
    per_slope_fibre_shaped: Counter = Counter()
    best_key: dict = {}
    best_mask: dict = {}
    deg_hist_all: Counter = Counter()

    def fibre_shaped(mask: int) -> bool:
        idx = set(P.idx_of(mask, n))
        if not core <= idx:
            return False
        rest = idx - core
        js = {fibre_of[i] for i in rest}
        return len(rest) == m * len(js) and all(
            set(case.fibre_idx[j]) <= rest for j in js)

    def on_sol(z: int, mask: int):
        per_slope_total[z] += 1
        if fibre_shaped(mask):
            per_slope_fibre_shaped[z] += 1
        k = P.key_lex(mask, n)
        if best_key.get(z) is None or k < best_key[z]:
            best_key[z] = k
            best_mask[z] = mask

    P.enumerate_all_witnesses(case, on_sol)

    def wdeg(z: int, mask: int) -> int:
        fz = fz_cache.get(z)
        if fz is None:
            fz = P.padd(case.U, P.pscal(case.V, z, q), q)
            fz_cache[z] = fz
        loc = P.locator([case.D[i] for i in P.idx_of(mask, n)], q)
        return P.deg(P.padd(fz, P.pneg(loc, q), q))

    sel_deg = Counter(wdeg(z, best_mask[z]) for z in best_mask)
    int_deg = Counter(c["degp"] for c in case.cand)
    sel_fibre = sum(1 for z in best_mask if fibre_shaped(best_mask[z]))
    sel_complete_fibres = Counter()
    for z, msk in best_mask.items():
        idx = set(P.idx_of(msk, n))
        sel_complete_fibres[sum(1 for fib in case.fibre_idx
                                if set(fib) <= idx)] += 1

    tot = sum(per_slope_total.values())
    fsh = sum(per_slope_fibre_shaped.values())
    out = dict(
        case=name,
        parameters=dict(n=n, q=q, m=m, K=K, h=case.h, A=A, g=case.g,
                        a=case.a, b=case.b),
        total_witnesses=tot,
        fibre_shaped_witnesses=fsh,
        fibre_shaped_fraction_num=fsh,
        fibre_shaped_fraction_den=tot,
        candidate_family_size=len(case.cand),
        lex_selected_fibre_shaped=sel_fibre,
        lex_selected_witness_degree_histogram={str(k): v for k, v
                                               in sorted(sel_deg.items())},
        intended_witness_degree_histogram={str(k): v for k, v
                                           in sorted(int_deg.items())},
        lex_selected_complete_fibre_count_histogram={
            str(k): v for k, v in sorted(sel_complete_fibres.items())},
        max_witness_degree_possible=K - 1,
        intended_degree_cap=A - 2 * m,
    )
    path = os.path.join(HERE, f"shape_{name}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(json.dumps(out, indent=1, sort_keys=True))
    print(f"-> {path}")


if __name__ == "__main__":
    main()
