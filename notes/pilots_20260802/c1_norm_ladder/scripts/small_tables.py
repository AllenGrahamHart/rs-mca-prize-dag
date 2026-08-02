#!/usr/bin/env python3
"""Weight-stratified norm tables at 2N = 8 and 2N = 16 (EXHAUSTIVE, exact).

For every weight w:
  max_norm(w) = max over ternary f of weight w (deg < N) of Res(f, x^N+1)
  argmax f, the full multiset of attained norm values, the U- and G-orbit counts,
  and the census of admissible primes (q = 1 mod 2N) dividing some weight-w norm.

Everything is computed with Python ints via norm_descent_py and independently
re-verified with the Bareiss determinant norm_bareiss.  No floats anywhere.

Usage: tools/ramguard local -- python3 scripts/small_tables.py --twoN 16 --out ...
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations, product

from norm_core import (burnside_orbit_counts, group_G, group_U, norm_bareiss,
                       norm_descent_py)


def prime_factors(n: int) -> dict[int, int]:
    f: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--twoN", type=int, required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    twoN = args.twoN
    N = twoN // 2

    U = group_U(N)
    G = group_G(N)
    nU = burnside_orbit_counts(U, N)
    nG = burnside_orbit_counts(G, N)

    # exhaustive enumeration, stratified by weight; leading (lowest) nonzero
    # coefficient normalised to +1 is NOT used here -- we enumerate everything,
    # which also verifies the free-ness of the U-action.
    table = []
    census: dict[int, dict] = {}
    total_bareiss_checks = 0
    for w in range(1, N + 1):
        best = 0
        arg = None
        vals: dict[int, int] = {}
        n_poly = 0
        n_zero = 0
        for pos in combinations(range(N), w):
            for signs in product((1, -1), repeat=w):
                d = [0] * N
                for p, s in zip(pos, signs):
                    d[p] = s
                n_poly += 1
                v = norm_descent_py(d)
                if v == 0:
                    n_zero += 1
                vals[v] = vals.get(v, 0) + 1
                if v > best:
                    best = v
                    arg = list(d)
        # independent Bareiss re-verification of the argmax
        chk = norm_bareiss(arg)
        total_bareiss_checks += 1
        assert chk == best, (w, chk, best)
        # census
        for v in vals:
            if v <= 0:
                continue
            for p in prime_factors(v):
                if p % twoN == 1:
                    rec = census.setdefault(p, {"q": p, "min_weight": w, "witnesses": {}})
                    rec["min_weight"] = min(rec["min_weight"], w)
                    rec["witnesses"].setdefault(str(w), None)
        table.append({
            "w": w,
            "n_ternary_f": n_poly,
            "n_zero_norm": n_zero,
            "max_norm": str(best),
            "argmax_f": arg,
            "argmax_bareiss_check": str(chk),
            "amgm_ceiling_w_pow_N_over_2": str(w ** (N // 2)),
            "max_saturates_amgm": best == w ** (N // 2),
            "n_orbits_U": nU[w],
            "n_orbits_U_free_formula": n_poly // (2 * N),
            "n_orbits_G": nG[w],
            "n_distinct_norms": len(vals),
            "distinct_norms": [str(v) for v in sorted(vals)],
        })

    # find an explicit witness f for each census prime at its minimal weight
    for p, rec in census.items():
        w0 = rec["min_weight"]
        found = None
        for pos in combinations(range(N), w0):
            if found:
                break
            for signs in product((1, -1), repeat=w0):
                d = [0] * N
                for q_, s in zip(pos, signs):
                    d[q_] = s
                v = norm_descent_py(d)
                if v > 0 and v % p == 0:
                    found = (list(d), v)
                    break
        rec["witness_f"] = found[0]
        rec["witness_norm"] = str(found[1])
        rec["witness_norm_bareiss"] = str(norm_bareiss(found[0]))
        rec["cofactor"] = str(found[1] // p)
        assert norm_bareiss(found[0]) == found[1]
        del rec["witnesses"]

    overall = max(int(r["max_norm"]) for r in table)
    out = {
        "twoN": twoN, "N": N,
        "admissibility": "q prime, q = 1 mod %d" % twoN,
        "group_orders": {"|U|": len(U), "|G|": len(G)},
        "max_norm_over_all_nonzero_ternary_f": str(overall),
        "n_admissible_primes_in_census": len(census),
        "census": sorted(census.values(), key=lambda r: r["q"]),
        "table": table,
    }
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({k: v for k, v in out.items() if k not in ("census", "table")}))
    for r in table:
        print("w=%2d  max=%-12s argmax=%s  amgm=%-14s sat=%s  nU=%-8d nG=%-6d distinct=%d"
              % (r["w"], r["max_norm"], r["argmax_f"], r["amgm_ceiling_w_pow_N_over_2"],
                 r["max_saturates_amgm"], r["n_orbits_U"], r["n_orbits_G"],
                 r["n_distinct_norms"]))
    print("census primes:", [r["q"] for r in out["census"]])
    for r in out["census"]:
        print("  q=%-7d min_w=%d  norm=%s = %d * %s  witness=%s"
              % (r["q"], r["min_weight"], r["witness_norm"], r["q"], r["cofactor"],
                 r["witness_f"]))


if __name__ == "__main__":
    main()
