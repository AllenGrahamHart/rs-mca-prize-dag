#!/usr/bin/env python3
"""D4 -- APPLY THE PROVED BACKGROUND SIEVE TO THE 408 LARGE-SOURCE
RESIDUAL ROWS (PREREG R9 / P17-P18).

HARD LAW 5 SUBTRACTION, done BEFORE any claim: my (SING) re-derivation
is the PROVED node background/nodes/l1_background_overlap_singleton_payment
clause (BO2).  Nothing below claims new mathematics; the question is
purely BOOKKEEPING -- has (BO2), and the list threshold that (BO2) uses,
been charged against the 408 residual d-windows?

Two exact consequences of the node texts, applied per d:

  (E) EMPTY.      list threshold: h+|R_j| >= d+ell, R_j subset B, |B|=b
                  (l1_background_overlap_singleton_payment/proof.md:5-13;
                   = "the list threshold gives h>=d+g",
                   l1_fixed_support_defect_johnson_bound/statement.md:18)
                  so u = d-(t-1)ell > b  ==>  NO compatible codeword.
  (S) SINGLETON.  (BO2)  a+s < ell+g with a=N-d, s=h-d
                  ==> m <= 1.

Both are per (row, d).  Baseline for comparison: the round-25 CJ3 rescue
(d4_cj3_audit.py, 71 rows / 1.97% of residual d-mass), recomputed here
with the identical formula so the three are additive on one ledger.

Stdlib only.  Run via tools/ramguard local -- python3 from repo root.
"""
from __future__ import annotations

import json
import sys

ROOT = "/home/u2470931/smooth-read-solomin/prize"
sys.path.insert(0, ROOT + "/notes/pilots_20260807/fpc5_diag")
sys.path.insert(0, ROOT + "/notes/pilots_20260808/t_petal_lemma")
from fpc5_exact import p7_large_source_sieve            # noqa: E402
from tpetal_cj3_probe import neg_interval               # noqa: E402


def main(k=2 ** 40):
    N = k - 1
    rows = p7_large_source_sieve()
    tot = empty = singl = cj3 = both = 0
    rows_all_empty = rows_all_paid = 0
    per_rate = {}
    detail = []
    for r in rows:
        t, ell, M, b = r["t"], r["ell"], r["M"], r["b"]
        h = t * ell
        dlo, dhi = r["residual_d_window"]
        width = dhi - dlo + 1
        tot += width
        pr = per_rate.setdefault(r["rate"], {"rows": 0, "d": 0, "empty": 0,
                                             "singleton": 0, "cj3": 0,
                                             "left": 0})
        pr["rows"] += 1
        pr["d"] += width
        # ---- (E) EMPTY: u > b  <=>  d > (t-1)ell + b
        d_u_hi = (t - 1) * ell + b
        e_lo = max(dlo, d_u_hi + 1)
        n_empty = max(0, dhi - e_lo + 1)
        # ---- (S) SINGLETON on the NON-empty part: a+s < ell+g
        #      N-d + h-d < 2*ell-b   <=>   2d > N + h - 2ell + b
        s_lo = max(dlo, (N + h - 2 * ell + b) // 2 + 1)
        s_hi = min(dhi, d_u_hi)
        n_singl = max(0, s_hi - s_lo + 1)
        # ---- (CJ3) rescue, same formula as the round-25 audit
        lo = max(dlo, (t - 1) * ell, (h + 1) // 2)
        hi = min(dhi, d_u_hi)
        n_cj3 = 0
        if lo <= hi and 0 < b < ell:
            A = b + N
            B = -2 * N * ((t - 1) * ell + b)
            Cc = N * ((t - 1) ** 2 * ell ** 2 + b * t * ell)
            bad = neg_interval(A, B, Cc)
            if bad is None:
                glo, ghi = lo, hi
            else:
                blo, bhi = bad
                if blo <= lo and bhi >= hi:
                    glo, ghi = 1, 0
                else:
                    glo, ghi = (bhi + 1, hi) if bhi < hi else (lo, blo - 1)
                    glo = max(glo, lo)
            if ghi >= glo:
                n_cj3 = ghi - glo + 1
        # overlap of the singleton band with the CJ3 band (report, not add)
        empty += n_empty
        singl += n_singl
        cj3 += n_cj3
        left = width - n_empty - n_singl
        pr["empty"] += n_empty
        pr["singleton"] += n_singl
        pr["cj3"] += n_cj3
        pr["left"] += max(0, left)
        if n_empty == width:
            rows_all_empty += 1
        if n_empty + n_singl >= width:
            rows_all_paid += 1
        detail.append({"rate": r["rate"], "M": M, "t": t, "tag": r["tag"],
                       "ell": ell, "b": b, "width": width,
                       "EMPTY": n_empty, "SINGLETON": n_singl,
                       "CJ3": n_cj3, "left": max(0, left),
                       "frac_paid": round((n_empty + n_singl) / width, 6)})
    print(json.dumps({
        "k": k, "N": N, "rows": len(rows),
        "residual_d_total": tot,
        "d_EMPTY_by_list_threshold": empty,
        "frac_EMPTY": round(empty / tot, 8),
        "d_SINGLETON_by_BO2": singl,
        "frac_SINGLETON": round(singl / tot, 8),
        "d_CJ3_round25_baseline": cj3,
        "frac_CJ3": round(cj3 / tot, 8),
        "d_left_after_EMPTY_and_SINGLETON": tot - empty - singl,
        "frac_left": round((tot - empty - singl) / tot, 8),
        "rows_ENTIRELY_empty": rows_all_empty,
        "rows_ENTIRELY_paid_by_EMPTY_plus_SINGLETON": rows_all_paid,
        "per_rate": per_rate,
        "worst_rows_by_frac_paid": sorted(
            detail, key=lambda x: x["frac_paid"])[:6],
        "best_rows_by_frac_paid": sorted(
            detail, key=lambda x: -x["frac_paid"])[:6],
    }, indent=1))


if __name__ == "__main__":
    main()
