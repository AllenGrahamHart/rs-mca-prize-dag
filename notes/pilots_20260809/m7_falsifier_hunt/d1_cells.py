#!/usr/bin/env python3
"""D1 -- THE CHART FAMILY: which M >= 5 large-source cells are (i) inside
the node's OWN admissibility and (ii) exactly enumerable at small q.

Registered at notes/pilots_20260809/m7_falsifier_hunt/PREREG.md R1.

Admissibility (each condition with its node source, see PREREG R1 table):
  A1  M >= Mmin(rate)                     large_source statement:8-13
  A2  2 <= t < 2M-4                       large_source statement:18
  A3  d < ell*(M-2)                       large_source statement:19
  A4  e = 2d+1-t*ell >= 1                 large_source statement:20 (finite
                                          reading of "-> infinity")
  A5  t <= M                              large_source statement:37-38
  A6  0 <= b < ell and b > 0              JB statement:16 / CJ proof:44
  A7  g = ell-b >= 1                      JB statement:17
  A8  u = d-(t-1)ell, 0 <= u <= b         CJ1 + CJ proof:32 (= h >= d+g)
  A9  r_J = 2d-h >= 0                     CJ2 / JB2
  A10 N = k-1, S = n-k+1 = M*ell+b        JB statement:13 / CJ proof:16
  A11 ell = floor(S/M) (the sieve's own ell-window)

Derived labels, reported not imposed:
  LIVE  = [J_plain = d^2-N(e-1) <= 0]   (inside the 408-row residual)
  CJ3   = [b d^2 + N u^2 - N b r_J > 0] (the CJ rescue fires)

Stdlib only.  Run via tools/ramguard tiny -- python3 from repo root.
"""
from __future__ import annotations

import json
from math import comb

MMIN = {2: 5, 4: 5, 8: 7, 16: 15}


def is_prime(m):
    if m < 2:
        return False
    if m % 2 == 0:
        return m == 2
    f = 3
    while f * f <= m:
        if m % f == 0:
            return False
        f += 2
    return True


def next_prime(m):
    c = m + 1
    while not is_prime(c):
        c += 1
    return c


def cell(rate, M, t, ell, b, u):
    """Full admissibility ledger for one cell.  rate = the DENOMINATOR."""
    out = {"rate": f"1/{rate}", "M": M, "t": t, "ell": ell, "b": b, "u": u}
    fails = []
    S = M * ell + b
    num = S - 1
    if rate == 2:
        k = num
    else:
        if num % (rate - 1):
            out["fails"] = ["A10_k_not_integer"]
            return out
        k = num // (rate - 1)
    n = rate * k
    N = k - 1
    d = (t - 1) * ell + u
    h = t * ell
    e = 2 * d + 1 - h
    rJ = 2 * d - h
    g = ell - b
    out.update({"k": k, "n": n, "N": N, "d": d, "h": h, "e": e,
                "r_J": rJ, "g": g, "S": S})
    if M < MMIN[rate]:
        fails.append("A1_M_too_small")
    if not (2 <= t < 2 * M - 4):
        fails.append("A2_t_window")
    if not (d < ell * (M - 2)):
        fails.append("A3_d_cap")
    if e < 1:
        fails.append("A4_e_positive")
    if t > M:
        fails.append("A5_t_le_M")
    if not (0 < b < ell):
        fails.append("A6_background_capacity")
    if g < 1:
        fails.append("A7_g")
    if not (0 <= u <= b):
        fails.append("A8_u_window")
    if rJ < 0:
        fails.append("A9_rJ")
    if N + b + M * ell != n or S != n - k + 1:
        fails.append("A10_partition")
    if ell != S // M:
        fails.append("A11_ell_window")
    if N < d:
        fails.append("A10_core_smaller_than_d")
    out["fails"] = fails
    if fails:
        return out
    q = next_prime(n)
    chartdim = (t - 2) * ell + u + 1
    # registered identity: codim = u + t*ell - d - 1 == ell-1
    codim = u + h - d - 1
    out["codim"] = codim
    out["codim_is_ell_minus_1"] = (codim == ell - 1)
    out["CHARTDIM"] = chartdim
    out["dim_V"] = d - ell + 2
    out["q"] = q
    out["mu"] = comb(N, d) / q ** (ell - 1)
    out["cost_evals"] = q ** (chartdim - 1) * N
    Jp = d * d - N * (e - 1)
    out["J_plain"] = Jp
    out["LIVE"] = Jp <= 0
    Jcj = b * d * d + N * u * u - N * b * rJ
    out["J_CJ"] = Jcj
    out["CJ3_fires"] = Jcj > 0
    out["n_is_2power"] = (n & (n - 1)) == 0
    return out


REGISTERED = [
    ("C1", 2, 5, 2, 2, 1, 1), ("C2", 2, 8, 2, 2, 1, 1),
    ("C3", 2, 16, 2, 2, 1, 1), ("C4", 2, 5, 2, 3, 2, 2),
    ("C5", 2, 8, 2, 3, 2, 2), ("C6", 2, 5, 2, 4, 3, 3),
    ("C7", 2, 6, 2, 4, 3, 3), ("C8", 2, 5, 3, 2, 1, 1),
    ("C9", 2, 8, 3, 2, 1, 1), ("C10", 4, 18, 2, 2, 1, 1),
    ("C11", 4, 24, 2, 2, 1, 1), ("C12", 8, 42, 2, 2, 1, 1),
    ("C13", 16, 120, 2, 2, 1, 1),
]


def main():
    reg = []
    for cid, rate, M, t, ell, b, u in REGISTERED:
        r = cell(rate, M, t, ell, b, u)
        r["id"] = cid
        reg.append(r)
    # ---- independent broad scan for any admissible cell I may have missed
    scan = []
    for rate in (2, 4, 8, 16):
        for ell in range(2, 8):
            for b in range(1, ell):
                for M in range(MMIN[rate], 260):
                    S = M * ell + b
                    if rate != 2 and (S - 1) % (rate - 1):
                        continue
                    k = (S - 1) // (rate - 1) if rate != 2 else S - 1
                    if rate * k > 600:
                        break
                    for t in range(2, M + 1):
                        for u in range(1, b + 1):
                            r = cell(rate, M, t, ell, b, u)
                            if r.get("fails"):
                                continue
                            if r["CHARTDIM"] > 4 or r["mu"] < 0.5:
                                continue
                            if r["cost_evals"] > 3.0e7:
                                continue
                            scan.append(r)
    scan.sort(key=lambda r: (r["cost_evals"], -r["mu"]))
    keyset = {(r["rate"], r["M"], r["t"], r["ell"], r["b"], r["u"])
              for r in scan}
    regkeys = {(r["rate"], r["M"], r["t"], r["ell"], r["b"], r["u"])
               for r in reg if not r["fails"]}
    print(json.dumps({
        "REGISTERED_CELLS": reg,
        "registered_admissible": sum(1 for r in reg if not r["fails"]),
        "registered_failing": [(r["id"], r["fails"]) for r in reg
                               if r["fails"]],
        "codim_identity_holds_all": all(r.get("codim_is_ell_minus_1")
                                        for r in reg if not r["fails"]),
        "LIVE_all": all(r.get("LIVE") for r in reg if not r["fails"]),
        "CJ3_fires_any": any(r.get("CJ3_fires") for r in reg
                             if not r["fails"]),
        "BROAD_SCAN_total_accessible": len(scan),
        "BROAD_SCAN_not_in_registered": len(keyset - regkeys),
        "BROAD_SCAN_cheapest_20": scan[:20],
        "BROAD_SCAN_max_e": max((r["e"] for r in scan), default=None),
        "BROAD_SCAN_max_rJ_over_d": max(
            (r["r_J"] / r["d"] for r in scan), default=None),
    }, indent=1))


if __name__ == "__main__":
    main()
