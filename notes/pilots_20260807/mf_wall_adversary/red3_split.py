#!/usr/bin/env python3
"""D1/S3 bookkeeping for red 3 (l1_fpc5_large_source_payment).

The (MF) statement can only be INSTANTIATED on a cell whose contributors
are proved to inject into a linear flat.  That injection exists at t = 2
(two-full-petal slice reduction, envelope dim 2s+2) and at t = 3
(pma_three_petal_mu_basis_reduction).  For t >= 4 NO such reduction is
proved -- round 23's own cross-lane matrix, fpc5_diag/REPORT.md:229:
"three-petal mu-basis / projective Johnson | APPLIES ONLY at t=3 | the
t>=4 generalization does not exist".

So the question "is red 3 on the (MF) wall?" is only WELL-POSED on the
t in {2,3} part of its residual.  This script re-runs the round-23
Johnson sieve (reusing fpc5_diag/fpc5_exact.py verbatim) and splits the
408 residual rows by t, giving the exact size of the part of red 3 on
which the one-wall question cannot even be asked.

Stdlib only.  Run via tools/ramguard.
"""
from __future__ import annotations

import json
import sys

sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/"
                   "notes/pilots_20260807/fpc5_diag")
from fpc5_exact import p7_large_source_sieve            # noqa: E402


def main():
    rows = p7_large_source_sieve()
    inst = [r for r in rows if r["t"] <= 3]
    noninst = [r for r in rows if r["t"] >= 4]
    by_rate = {}
    for r in rows:
        key = r["rate"]
        d = by_rate.setdefault(key, {"total": 0, "t_le_3": 0, "t_ge_4": 0})
        d["total"] += 1
        d["t_le_3" if r["t"] <= 3 else "t_ge_4"] += 1
    maxe_i = max((r["e_range"][1] for r in inst), default=0)
    maxe_n = max((r["e_range"][1] for r in noninst), default=0)
    print(json.dumps({
        "mode": "red3_instantiability_split",
        "source": "fpc5_diag/fpc5_exact.py p7_large_source_sieve (verbatim)",
        "total_residual_rows": len(rows),
        "rows_t_le_3_MF_INSTANTIABLE": len(inst),
        "rows_t_ge_4_MF_NOT_INSTANTIABLE": len(noninst),
        "fraction_not_instantiable": round(len(noninst) / len(rows), 4),
        "by_rate": by_rate,
        "max_e_instantiable": maxe_i,
        "max_e_not_instantiable": maxe_n,
        "t_values_present": sorted({r["t"] for r in rows}),
        "sample_t_ge_4_row": noninst[0] if noninst else None,
    }, indent=1))


if __name__ == "__main__":
    main()
