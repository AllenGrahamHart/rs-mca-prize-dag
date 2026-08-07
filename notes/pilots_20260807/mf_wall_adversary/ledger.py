#!/usr/bin/env python3
"""The pairwise-overlap PACKING LEDGER, computed exactly, for both reds.

For m distinct split members of degree j inside a core budget N, with the
proved pairwise root-overlap cap lam:

    sum_x (mult(x)-1) >= m*j - N          (budget)
    sum_x C(mult(x),2) = sum_{i<j} |Z_i cap Z_j| <= C(m,2)*lam   (overlap cap)
    and  sum_x (mult(x)-1) <= sum_x C(mult(x),2)

so an m-packing is FORBIDDEN by the overlap cap alone iff

    C(m,2)*lam < m*j - N.                 (LEDGER)

This is what "the measured cap IS the Bonferroni/packing cap" means.  The
script prints, for each measured cell, the largest m the ledger PERMITS,
against the MEASURED max packing, so the two can be compared without
hand-waving.

Stdlib only.  Run via tools/ramguard.
"""
from __future__ import annotations

import json


def ledger_permits(N, j, lam, mmax=40):
    """Largest m not forbidden by (LEDGER); None = never forbids."""
    forbidden = [m for m in range(2, mmax + 1)
                 if m * (m - 1) // 2 * lam < m * j - N]
    if not forbidden:
        return None
    return min(forbidden) - 1


def main():
    rows = []
    # RED 1 (rate-half M=4,t=2 sharp): j=d=2ell-3, N=5ell-5,
    # proved cap 2s=2(ell-3); round-23 sharpened cap ell-3.
    measured1 = {4: 4, 5: 4, 6: 4}
    for ell in (4, 5, 6, 8, 12, 20):
        j, N = 2 * ell - 3, 5 * ell - 5
        rows.append({
            "red": 1, "cell": f"ratehalf_m4_t2 ell={ell}", "j": j, "N": N,
            "lam_proved_2s": 2 * (ell - 3),
            "lam_sharpened_ell_minus_3": ell - 3,
            "ledger_permits_with_proved_lam":
                ledger_permits(N, j, 2 * (ell - 3)),
            "ledger_permits_with_sharpened_lam":
                ledger_permits(N, j, ell - 3),
            "MEASURED_maxpack": measured1.get(ell),
        })
    # RED 2 (LS6): j=2ell-a, N=4ell+b-2, proved cap h=ell-2a.
    measured2 = {(3, 1, 1): 2, (3, 2, 1): 3, (4, 1, 1): 3,
                 (4, 2, 1): 3, (4, 3, 1): 3}
    for (ell, b, a), mp in sorted(measured2.items()):
        j, N, h = 2 * ell - a, 4 * ell + b - 2, ell - 2 * a
        rows.append({
            "red": 2, "cell": f"LS6 (ell,b,a)=({ell},{b},{a})", "j": j,
            "N": N, "lam_proved_h": h,
            "ledger_permits_with_proved_lam": ledger_permits(N, j, h),
            "MEASURED_maxpack": mp,
        })
    print(json.dumps({
        "mode": "packing_ledger",
        "note": "ledger_permits = largest m NOT forbidden by the pairwise "
                "overlap cap; None means the cap forbids nothing at all",
        "rows": rows,
    }, indent=1))


if __name__ == "__main__":
    main()
