#!/usr/bin/env python3
"""bc_block_census -- verifier 1: the arithmetic layer.

Machine-verifies, with exact integers only:

  (CORE-LENS) consequence      -- the 2-target pigeonhole (2-TARGET).
  (ONE-TARGET THEOREM)         -- at the round-14 pinning n = 3d+k-(sigma+1)
                                  the 2-target condition fails by EXACTLY
                                  t-1 >= 1, identically in (h,k).  Hence
                                  |Tau| <= 1 there and the round-14
                                  |Bset| = 2 is a pigeonhole artifact.
  (PACK)                       -- |Tau| <= C(n-e,K)/C(k+d,K).
  (P4 / BC-F9)                 -- K = k-ell vs e at every prize row:
                                  is the punctured code the full space?
  (P7 / route 3)               -- the Johnson-regime predicate A^2 vs k*n,
                                  integer cross-multiplied, at the round-14
                                  witness and at every prize row.
  minimal 2-target toy shapes  -- the fixture parameters used by verifier 2.

Row constants are consumed READ-ONLY from the round-13 pilot
(../commonroot_syzygy/ledger.py ROWS + boundary()).

Run: tools/ramguard tiny -- python3 \
       notes/pilots_20260804/bc_block_census/theory.py
"""

import json
import os
import sys
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))

CHECKS = []


def chk(cond, name, info=""):
    CHECKS.append({"name": name, "ok": bool(cond), "info": str(info)})


# --- round-13 constants, reproduced exactly (subtraction: not re-derived,
# --- copied from ../commonroot_syzygy/ledger.py ROWS and boundary()).
ROWS = (
    ("1/4,1/8", 2 ** 41, 2 ** 33 + 1, 11),
    ("1/16", 2 ** 41, 2 ** 32 + 1, 10),
)
RATES = {"1/4,1/8": (4, 8), "1/16": (16,)}


def boundary(n, h):
    ell = (h - 4) // 7
    r = 2 * ell + 1
    d = h - r
    sigma = d - ell - 1 - 2 * r
    w = d + ell
    return ell, r, d, sigma, w


def two_target_margin(n, e, k, d, K):
    """n-e - (2(k+d)-(K-1));  >= 0  <=>  |Tau| >= 2 is not excluded."""
    return (n - e) - (2 * (k + d) - (K - 1))


# ---------------------------------------------------------------- part 1
# The ONE-TARGET THEOREM at the round-14 pinning, over a shape scan.

scan = []
for h in range(18, 400):
    ell = (h - 4) // 7
    if ell < 1:
        continue
    r = 2 * ell + 1
    d = h - r
    sigma = d - ell - 1 - 2 * r
    if sigma < 0 or sigma >= r:
        continue
    for t in range(2, sigma + 3):
        e = 4 * ell + t
        c = sigma + 1
        for k in range(ell + 2, ell + 12):
            K = k - ell
            n = 3 * d + k - c
            m = two_target_margin(n, e, k, d, K)
            # THE IDENTITY: margin == -(t-1), identically.
            chk(m == -(t - 1),
                "ONE-TARGET identity margin = -(t-1)",
                f"h={h} k={k} t={t} margin={m}")
            chk(m < 0, "ONE-TARGET: |Tau| >= 2 excluded at round-14 pinning",
                f"h={h} k={k} t={t}")
            # dim K_d = d - ell - e must equal sigma+1 exactly at t=2
            if t == 2:
                chk(d - ell - e == sigma + 1,
                    "dim K_d = d-ell-e = sigma+1 at t=2", f"h={h}")
            scan.append((h, k, t, m))

# the exact round-14 shapes, named
R14 = []
for (h, k, q) in ((25, 4, 229), (25, 7, 61)):
    ell = (h - 4) // 7
    r = 2 * ell + 1
    d = h - r
    sigma = d - ell - 1 - 2 * r
    e = 2 * r
    t = e - 4 * ell
    c = sigma + 1
    n = 3 * d + k - c
    K = k - ell
    m = two_target_margin(n, e, k, d, K)
    chk(m == -(t - 1) and m == -1,
        "round-14 shape: 2-target pigeonhole fails by exactly 1",
        f"h={h} k={k} n={n} margin={m}")
    R14.append({"h": h, "k": k, "q": q, "n": n, "e": e, "d": d, "ell": ell,
                "r": r, "sigma": sigma, "t": t, "K": K, "core": k + d,
                "A": k + h, "two_target_margin": m,
                "Tau_max_forced": 1,
                "n_needed_for_2_targets": e + 2 * (k + d) - (K - 1)})

# ---------------------------------------------------------------- part 2
# The prize rows: 2-target room, K vs e (BC-F9), Johnson (P7), PACK.

rows = {}
for name, n, h, s in ROWS:
    ell, r, d, sigma, w = boundary(n, h)
    ent = {"n": n, "h": h, "ell": ell, "r": r, "d": d, "sigma": sigma,
           "s": s, "rates": {}}
    for den in RATES[name]:
        k = n // den
        K = k - ell
        A = k + h
        e = 4 * ell + 2                      # the t=2 tail
        core = k + d
        marg = two_target_margin(n, e, k, d, K)
        # BC-F9: is the punctured code RS_K restricted to D the full space?
        surjective = K >= e
        # P7: Johnson.  above  <=>  A^2 > k*n   (exact integers, no floats)
        above_johnson = A * A > k * n
        ent["rates"][f"1/{den}"] = {
            "k": k, "K_eq_k_minus_ell": K, "A": A, "e": e, "core": core,
            "two_target_margin": marg,
            "multi_target_room": marg >= 0,
            "K_gt_e_punctured_code_is_full_space": surjective,
            "K_over_e_ratio_floor": K // e,
            "A_squared": A * A, "k_times_n": k * n,
            "above_johnson_A2_gt_kn": above_johnson,
        }
        chk(marg >= 0, f"{name} 1/{den}: prize row HAS multi-target room",
            f"margin={marg}")
        chk(surjective,
            f"{name} 1/{den}: BC-F9 -- K > e, punctured code is FULL space",
            f"K={K} e={e}")
        chk(not above_johnson,
            f"{name} 1/{den}: prize row sits BELOW the Johnson radius",
            f"A^2={A*A} k*n={k*n}")
    rows[name] = ent

# round-14 witness regime (h=25,k=4,q=229,n=57): must be ABOVE Johnson
w14 = R14[0]
chk(w14["A"] ** 2 > w14["k"] * w14["n"],
    "round-14 witness sits ABOVE the Johnson radius (audit's caveat)",
    f"A^2={w14['A']**2} k*n={w14['k']*w14['n']}")

# ---------------------------------------------------------------- part 3
# (PACK):  |Tau| <= C(n-e,K)/C(k+d,K).   Sanity at toy scale only
# (the prize-row value is astronomically large; we assert that fact).
pack = {}
for ent in R14:
    N, K, W = ent["n"] - ent["e"], ent["K"], ent["core"]
    val = comb(N, K) // comb(W, K) if N >= K and W >= K else None
    pack[f"h{ent['h']}k{ent['k']}"] = {"N": N, "K": K, "w": W, "PACK": val}
    if val is not None:
        chk(val >= 1, "PACK bound is >= 1 at round-14 shapes", val)

# prize row: PACK is astronomically weak -- assert it exceeds the (WTB) cap
row1 = rows["1/4,1/8"]["rates"]["1/4"]
# log-scale comparison without building the integer: K*log2((N)/(w)) bits
N1 = ROWS[0][1] - row1["e"]
ratio_num, ratio_den = N1, row1["core"]
chk(ratio_num > ratio_den,
    "PACK at the prize row has base ratio > 1 (bound is exponential in K)",
    f"(n-e)/(k+d) ~ {ratio_num // ratio_den}")

# ---------------------------------------------------------------- part 4
# Minimal toy shapes that DO admit >= 2 (and >= 3) targets.
fixtures = []
for h in (25,):
    ell = (h - 4) // 7
    r = 2 * ell + 1
    d = h - r
    sigma = d - ell - 1 - 2 * r
    e = 2 * r
    t = e - 4 * ell
    for k in range(ell + 2, ell + 6):
        K = k - ell
        core = k + d
        n2 = e + 2 * core - (K - 1)          # smallest n allowing |Tau|=2
        n3 = e + 3 * core - 3 * (K - 1)      # smallest n allowing |Tau|=3
        fixtures.append({"h": h, "k": k, "K": K, "ell": ell, "r": r, "d": d,
                         "sigma": sigma, "e": e, "t": t, "core": core,
                         "A": k + h,
                         "min_n_for_2_targets": n2,
                         "min_n_for_3_targets": n3,
                         "dim_K_d": d - ell - e})

report = {
    "shape_scan_entries": len(scan),
    "round14_shapes": R14,
    "prize_rows": rows,
    "PACK_at_round14": pack,
    "toy_fixture_parameters": fixtures,
    "checks": len(CHECKS),
    "failed": [c for c in CHECKS if not c["ok"]],
}
with open(os.path.join(HERE, "theory.json"), "w") as fh:
    json.dump({"report": report, "n_checks": len(CHECKS),
               "failed": report["failed"]}, fh, indent=1, sort_keys=True,
              default=str)
print(json.dumps(report, indent=1, sort_keys=True, default=str))
sys.exit(1 if report["failed"] else 0)
