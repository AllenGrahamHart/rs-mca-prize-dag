#!/usr/bin/env python3
"""D4 -- THE CJ2/CJ3 CHART AUDIT AT M >= 5.

Registered at notes/pilots_20260809/m7_complement_repose/PREREG.md R3/P9.

Round 24 left this as "the named next probe":
  critical/nodes/l1_fpc5_large_source_payment/statement.md:108-110
  "(CJ2)/(CJ3) of l1_joint_core_background_johnson_bound is proved at
   arbitrary h and would rescue 71 residual rows -- its chart hypotheses
   at M >= 5 are UNAUDITED (the named next probe)."

This script (i) REPLAYS the round-24 arithmetic verbatim
(tpetal_cj3_probe.probe_a) and (ii) re-derives it independently while
CHECKING, row by row and d by d, every hypothesis the two node
statements actually impose:

  H-b   background capacity        0 <= b < ell     (JB statement:16)
  H-b0  (CJ3) needs                b > 0            (CJ proof:44)
  H-g   g = ell - b >= 1                             (JB statement:17)
  H-lt  list threshold             h >= d + g        (JB statement:18)
  H-u   canonical background pick  0 <= u <= b       (CJ1 + CJ proof:32)
  H-r   pairwise budget            r = 2d - h >= 0   (CJ2)
  H-dis core / petal / background pairwise disjoint  (CJ proof:16)
  H-N   N = |C| = k-1                                (JB statement:13)
  H-CJ4 the delivered bound        m <= N b ell / J  (CJ4)

and reports which of them is BINDING on the 71-row rescue.

Stdlib only.  Run via tools/ramguard local -- python3 from repo root.
"""
from __future__ import annotations

import json
import sys
from math import isqrt

ROOT = "/home/u2470931/smooth-read-solomin/prize"
sys.path.insert(0, ROOT + "/notes/pilots_20260807/fpc5_diag")
sys.path.insert(0, ROOT + "/notes/pilots_20260808/t_petal_lemma")
from fpc5_exact import p7_large_source_sieve          # noqa: E402
from tpetal_cj3_probe import probe_a, neg_interval    # noqa: E402


def audit(k=2 ** 40):
    N = k - 1
    rows = p7_large_source_sieve()
    fail = {h: 0 for h in ["H-b", "H-b0", "H-g", "H-lt", "H-u", "H-r",
                           "H-dis", "H-N"]}
    rescued, rescued_d, total_d = [], 0, 0
    b_values, ell_values = set(), set()
    window_widths = []
    for r in rows:
        t, ell, M, b = r["t"], r["ell"], r["M"], r["b"]
        rate = int(r["rate"].split("/")[1])
        S = (rate - 1) * k + 1
        h = t * ell
        g = ell - b
        dlo, dhi = r["residual_d_window"]
        total_d += dhi - dlo + 1
        b_values.add(b)
        ell_values.add(ell)
        # ---- static chart hypotheses
        if not (0 <= b < ell):
            fail["H-b"] += 1
            continue
        if b <= 0:
            fail["H-b0"] += 1
            continue
        if g < 1:
            fail["H-g"] += 1
            continue
        # core + source partition the ambient domain: (k-1) + S = rate*k
        if (k - 1) + S != rate * k:
            fail["H-dis"] += 1
            continue
        if S != M * ell + b:
            fail["H-dis"] += 1
            continue
        # ---- per-d hypotheses.  H-lt (h >= d+g) and H-u (u <= b) are the
        # SAME inequality: u = d-(t-1)ell <= b  <=>  d <= (t-1)ell+b
        #                                        <=>  t*ell >= d + ell - b.
        d_lo_u = (t - 1) * ell                    # u >= 0
        d_hi_u = (t - 1) * ell + b                # u <= b  ==  h >= d+g
        d_lo_r = (h + 1) // 2                     # r = 2d-h >= 0
        lo = max(dlo, d_lo_u, d_lo_r)
        hi = min(dhi, d_hi_u)
        if lo > hi:
            fail["H-u"] += 1
            continue
        window_widths.append(hi - lo + 1)
        # ---- (CJ3) J = (b+N)d^2 - 2N((t-1)ell+b)d + N[(t-1)^2 ell^2 + b t ell]
        A = b + N
        B = -2 * N * ((t - 1) * ell + b)
        Cc = N * ((t - 1) ** 2 * ell ** 2 + b * t * ell)
        bad = neg_interval(A, B, Cc)
        if bad is None:
            glo, ghi = lo, hi
        else:
            blo, bhi = bad
            if blo <= lo and bhi >= hi:
                continue
            glo, ghi = (bhi + 1, hi) if bhi < hi else (lo, blo - 1)
            glo = max(glo, lo)
        if ghi < glo:
            continue
        cnt = ghi - glo + 1
        rescued_d += cnt
        dv = glo
        u = dv - (t - 1) * ell
        rj = 2 * dv - h
        J = A * dv * dv + B * dv + Cc
        rescued.append({
            "rate": r["rate"], "M": M, "t": t, "tag": r["tag"],
            "ell": ell, "b": b, "g": g,
            "residual_window": [dlo, dhi],
            "residual_width": dhi - dlo + 1,
            "CJ_admissible_window": [lo, hi],
            "CJ_admissible_width": hi - lo + 1,
            "rescued_window": [glo, ghi], "rescued_width": cnt,
            "d": dv, "u": u, "r_2d_minus_h": rj,
            "J_plain_d2_minus_N_rJ": dv * dv - N * rj,
            "J_CJ": J,
            "CJ4_bound_m_le": N * b * ell // J if J > 0 else None,
            "CJ4_le_n_cubed": (N * b * ell) <= (rate * k) ** 3 * max(J, 1),
        })
    return {
        "k": k, "N": N, "rows_total": len(rows),
        "hypothesis_failures": fail,
        "rows_RESCUED": len(rescued),
        "residual_d_values_total": total_d,
        "d_values_rescued": rescued_d,
        "fraction_of_residual_d_mass_rescued":
            round(rescued_d / total_d, 8) if total_d else None,
        "b_range": [min(b_values), max(b_values)],
        "ell_range": [min(ell_values), max(ell_values)],
        "CJ_admissible_window_widths": {
            "min": min(window_widths), "max": max(window_widths),
            "n": len(window_widths)} if window_widths else None,
        "rescued_rows_sample": rescued[:2],
        "rows_FULLY_rescued":
            sum(1 for x in rescued
                if x["rescued_width"] == x["residual_width"]),
        "rescued_t_hist": _hist(rescued, "t"),
        "rescued_M_hist": _hist(rescued, "M"),
        "rescued_rate_hist": _hist(rescued, "rate"),
        "rescued_g_eq_1_rows": sum(1 for x in rescued if x["g"] == 1),
        "CJ4_bound_range": [min(x["CJ4_bound_m_le"] for x in rescued),
                            max(x["CJ4_bound_m_le"] for x in rescued)],
        "all_CJ4_le_n_cubed": all(x["CJ4_le_n_cubed"] for x in rescued),
        "rescued_width_over_residual_width_max":
            max(x["rescued_width"] / x["residual_width"] for x in rescued),
    }


def _hist(rows, field):
    h = {}
    for x in rows:
        h[str(x[field])] = h.get(str(x[field]), 0) + 1
    return dict(sorted(h.items()))


def main():
    out = audit()
    replay = probe_a()
    print(json.dumps({
        "ROUND24_REPLAY_verbatim_probe_a": {
            k: v for k, v in replay.items() if k != "samples"},
        "ROUND24_REPLAY_samples": replay["samples"],
        "D4_INDEPENDENT_AUDIT": out,
    }, indent=1))


if __name__ == "__main__":
    main()
