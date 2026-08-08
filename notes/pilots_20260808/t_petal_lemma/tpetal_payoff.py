#!/usr/bin/env python3
"""(D3) THE PAYOFF: what the now-legal t-petal overlap cap buys in the
large-source Johnson sieve.

Reuses `p7_large_source_sieve` from the coordinator-replayed round-23
pilot VERBATIM (notes/pilots_20260807/fpc5_diag/fpc5_exact.py), which
is the sieve that consumes the lemma.  That function reports only the
rows it CANNOT pay (the ones whose d-window contains J<=0); the 408
headline is its `len(res)`.  To price the lemma we must also count the
rows it DOES pay, which the original function silently `continue`s
past.  This script re-implements the identical loop with the paid rows
instrumented, and ASSERTS that its residual list is byte-identical to
the verbatim function's, so the instrumentation is provably faithful.

Legality ledger:
  BEFORE the lemma, the pairwise overlap cap |Z(F) cap Z(F')| <= e-1
  was proved only at t=2 (cofactor determinant) and t=3 (mu-basis),
  so the sieve could only legally pay rows with t <= 3.
  AFTER the lemma (general t), every row it pays is legally paid.

Stdlib only.  Run via tools/ramguard.
"""
from __future__ import annotations

import json
import sys
from math import isqrt

ROOT = "/home/u2470931/smooth-read-solomin/prize"
sys.path.insert(0, ROOT + "/notes/pilots_20260807/fpc5_diag")
from fpc5_exact import p7_large_source_sieve            # noqa: E402


def instrumented(k=2 ** 40, rates=(2, 4, 8, 16)):
    """Byte-identical to p7_large_source_sieve, plus the PAID rows."""
    Mmin = {2: 5, 4: 5, 8: 7, 16: 15}
    N = k - 1
    paid, residual = [], []
    for r in rates:
        S = (r - 1) * k + 1
        for M in range(Mmin[r], Mmin[r] + 12):
            lo = S // (M + 1) + 1
            hi = S // M
            if lo > hi:
                continue
            for tag, ell in (("ell_min", lo), ("ell_max", hi),
                             ("ell_mid", (lo + hi) // 2)):
                b = S - M * ell
                if not (0 <= b < ell):
                    continue
                for t in range(2, min(M, 2 * M - 5) + 1):
                    dcap = min(ell * (M - 2) - 1, N)
                    dlo = (t * ell + 1) // 2
                    if dlo > dcap:
                        continue
                    disc = N * N - N * t * ell
                    if disc < 0:
                        jpos, dstar = True, None
                    else:
                        dstar = N - isqrt(disc)
                        jpos = dstar > dcap
                    row = {"rate": f"1/{r}", "M": M, "t": t, "tag": tag,
                           "ell": ell, "d_window": [dlo, dcap],
                           "window_width": dcap - dlo + 1}
                    if jpos:
                        paid.append(row)
                        continue
                    dres_lo = max(dlo, dstar)
                    row["residual_d_window"] = [dres_lo, dcap]
                    row["residual_width"] = dcap - dres_lo + 1
                    row["paid_prefix_width"] = max(0, dres_lo - dlo)
                    row["e_hi"] = 2 * dcap + 1 - t * ell
                    residual.append(row)
    return paid, residual


def split(rows):
    out = {"total": len(rows),
           "t_le_3": sum(1 for r in rows if r["t"] <= 3),
           "t_ge_4": sum(1 for r in rows if r["t"] >= 4)}
    by_rate = {}
    for r in rows:
        e = by_rate.setdefault(r["rate"], {"t_le_3": 0, "t_ge_4": 0})
        e["t_le_3" if r["t"] <= 3 else "t_ge_4"] += 1
    out["by_rate"] = by_rate
    out["t_values"] = sorted({r["t"] for r in rows})
    return out


def main():
    verbatim = p7_large_source_sieve()
    paid, residual = instrumented()
    # FAITHFULNESS ASSERTION: the instrumented loop must reproduce the
    # verbatim residual list exactly, row for row, in order.
    key = lambda r: (r["rate"], r["M"], r["t"], r["tag"], r["ell"])
    assert [key(r) for r in verbatim] == [key(r) for r in residual], \
        "instrumentation diverged from the verbatim round-23 sieve"
    total = len(paid) + len(residual)

    # d-mass: how much of the admissible d-window the sieve actually pays.
    win = sum(r["window_width"] for r in paid + residual)
    unpaid = sum(r["residual_width"] for r in residual)
    win4 = sum(r["window_width"] for r in paid + residual if r["t"] >= 4)
    unpaid4 = sum(r["residual_width"] for r in residual if r["t"] >= 4)

    out = {
        "sieve_source": "fpc5_diag/fpc5_exact.py p7_large_source_sieve",
        "k": "2**40",
        "GRID_total_rows": total,
        "RESIDUAL_rows_verbatim_round23": len(verbatim),
        "RESIDUAL_rows_instrumented": len(residual),
        "PAID_rows_by_the_Johnson_sieve": len(paid),
        "residual_split": split(residual),
        "paid_split": split(paid),
        "LEGALITY_LEDGER": {
            "before_lemma_legally_paid_rows_t_le_3":
                split(paid)["t_le_3"],
            "before_lemma_ILLEGALLY_claimed_rows_t_ge_4":
                split(paid)["t_ge_4"],
            "after_lemma_legally_paid_rows": len(paid),
            "residual_before_lemma_legal_accounting":
                len(residual) + split(paid)["t_ge_4"],
            "residual_after_lemma": len(residual),
            "rows_that_DIE_at_a_stroke": split(paid)["t_ge_4"],
        },
        "RESIDUAL_t_ge_4_rows_now_with_a_DEFINED_Johnson_functional":
            split(residual)["t_ge_4"],
        "d_mass": {
            "total_admissible_d_values_all_rows": win,
            "d_values_left_unpaid": unpaid,
            "fraction_of_d_mass_paid": round(1 - unpaid / win, 6),
            "t_ge_4_admissible_d_values": win4,
            "t_ge_4_d_values_left_unpaid": unpaid4,
            "t_ge_4_fraction_of_d_mass_paid": round(1 - unpaid4 / win4, 6),
        },
        "sample_rows_that_die": [r for r in paid if r["t"] >= 4][:4],
        "sample_residual_row": residual[0] if residual else None,
    }
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
