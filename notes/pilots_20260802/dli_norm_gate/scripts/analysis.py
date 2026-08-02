#!/usr/bin/env python3
"""dli_norm_gate -- consolidate every splitting scan and audit the laws.

Checks, over ALL rows of every splitting_*.json:
  S1   phi(n) * #sol = sum |H_U|                                  (identity)
  S2   #sol / #{H_U != 0} = mbar / phi(n)                          (identity)
  LN6  max m <= floor( log(maxnorm(phi,w)) / log q )               (norm bound)
  LN6' max m <= floor( (phi/2) * log w / log q )                   (AM-GM bound)
  S3   q^{o+1} > maxnorm(phi,w)  =>  ratio is EXACTLY 1/phi(n)
"""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path

sys.dont_write_bytecode = True

from splitting import MAXNORM

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def main():
    rows = []
    for f in sorted((ROOT / "results").glob("splitting_*.json")):
        d = json.loads(f.read_text())
        for r in d["rows"]:
            r["_src"] = f.name
            rows.append(r)
    bad_S1 = [r for r in rows if not r["S1_identity_holds"]]
    bad_S2 = []
    bad_LN6 = []
    bad_LN6p = []
    bad_S3 = []
    dev = []
    for r in rows:
        if not r["n_H_nonempty"]:
            continue
        # S2 identity: ratio*phi == sum_H / n_H_nonempty
        lhs = Fraction(r["phi"] * r["n_solutions"], r["n_H_nonempty"])
        rhs = Fraction(r["sum_H"], r["n_H_nonempty"])
        if lhs != rhs:
            bad_S2.append(r)
        if lhs != 1:
            dev.append(r)
        mx = MAXNORM.get(r["n"], {}).get(r["w"])
        q, w, phi = r["q"], r["w"], r["phi"]
        o = len(r["U"])
        if mx:
            bnd = int(math.log(mx) / math.log(q) + 1e-12)
            if r["max_m"] > bnd:
                bad_LN6.append({"row": {k: r[k] for k in ("n", "q", "w", "U")},
                                "max_m": r["max_m"], "bound": bnd})
            if q ** (o + 1) > mx and lhs != 1:
                bad_S3.append(r)
        bnd2 = int((phi / 2) * math.log(w) / math.log(q) + 1e-12) if w > 1 else 0
        if r["max_m"] > bnd2:
            bad_LN6p.append({"row": {k: r[k] for k in ("n", "q", "w", "U")},
                             "max_m": r["max_m"], "amgm_bound": bnd2})
    summary = {
        "total_rows": len(rows),
        "rows_with_solutions": sum(1 for r in rows if r["n_H_nonempty"]),
        "sources": sorted({r["_src"] for r in rows}),
        "S1_violations": len(bad_S1),
        "S2_violations": len(bad_S2),
        "LN6_violations_exact_maxnorm": len(bad_LN6),
        "LN6_violations_amgm": len(bad_LN6p),
        "S3_violations": len(bad_S3),
        "rows_deviating_from_1_over_phi": len(dev),
        "deviation_table": sorted(
            [{"n": r["n"], "q": r["q"], "w": r["w"], "U": r["U"],
              "ratio_times_phi": str(Fraction(r["phi"] * r["n_solutions"],
                                              r["n_H_nonempty"])),
              "ratio_times_phi_float": r["phi"] * r["n_solutions"] / r["n_H_nonempty"],
              "max_m": r["max_m"], "max_H": r["max_H"],
              "maxnorm": MAXNORM.get(r["n"], {}).get(r["w"]),
              "q^(o+1)": r["q"] ** (len(r["U"]) + 1)}
             for r in dev],
            key=lambda x: -x["ratio_times_phi_float"]),
        "max_m_observed_by_config": sorted(
            {(r["n"], r["q"], r["w"], r["max_m"]) for r in rows
             if r["max_m"] > 1}),
    }
    (ROOT / "results" / "analysis.json").write_text(
        json.dumps(summary, indent=1, default=str))
    print(json.dumps({k: v for k, v in summary.items()
                      if k not in ("deviation_table",
                                   "max_m_observed_by_config")}, indent=1))
    print("\nDEVIATION TABLE (every row where the ratio is not exactly 1/phi):")
    for d in summary["deviation_table"]:
        print(f"  n={d['n']:<4} q={d['q']:<7} w={d['w']:<2} U={d['U']} "
              f"ratio*phi={d['ratio_times_phi']:<10} max_m={d['max_m']} "
              f"maxnorm={d['maxnorm']} q^(o+1)={d['q^(o+1)']}")


if __name__ == "__main__":
    main()
