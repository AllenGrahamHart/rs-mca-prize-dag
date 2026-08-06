#!/usr/bin/env python3
"""FULL-RANK leaf pilot: exact prize-row arithmetic.   (2026-08-04)

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 <this>

PREREG item P6 (+ the full-rank non-vacuity rule found in dualform.py).
Rows reproduced VERBATIM from notes/pilots_20260803/listsize_program/
rows.py (which reproduces xr_band_occupancy/theory.py); q is the pinned
envelope 2^250 <= q < 2^256.  All integer arithmetic is exact; only the
binomial logarithms use lgamma (error << 1 bit on quantities of size
1e12).

R1  FULL-RANK NON-VACUITY.  J_d is 2d x (r'+1), so rank J_d = 2d needs
    r' + 1 >= 2d, i.e. n-k >= 3d-1.  Checked at every band-proper depth
    of every row, with the margin.
R2  AFFINE WINDOW DIMENSION.  In the full-rank stratum the monic
    locators satisfying the joint window system form an affine space of
    dimension exactly r'-2d.  Reported at the band ends.
R3  STRUCTURED SURVIVAL TABLE.  h = 2^s+1 and M = 2^j | gcd(n,k) with
    M | d force h-d = jM+1 (j >= 1; j = 0 is the cascade tier d = h-1,
    outside the band).  THEOREM L (xr_window_system_descent, item 4)
    then requires M(h-d) <= n-k-d = r'.  The exact surviving (M,d)
    region is computed here for the first time.
R4  BUDGET / FIRST MOMENT.  17n^2/25 in bits; the raw first-moment
    exponent log2 C(n,r') - 2d log2 q at the band ends (cross-check of
    the banked ~3.6e11-bit margin); beta_d of the (WPR) reduction.
"""
import json
from math import lgamma, log2

LN2 = 0.6931471805599453

# verbatim from notes/pilots_20260803/listsize_program/rows.py
ROWS = [
    dict(name="RowC 1/4", n=1024, k=256, A=261, h=5),
    dict(name="RowC 1/8", n=1024, k=128, A=133, h=5),
    dict(name="RowC 1/16", n=1024, k=64, A=67, h=3),
    dict(name="prize 1/4", n=2199023255552, k=549755813888,
         A=558345748481, h=8589934593),
    dict(name="prize 1/8", n=2199023255552, k=274877906944,
         A=283467841537, h=8589934593),
    dict(name="prize 1/16", n=2199023255552, k=137438953472,
         A=141733920769, h=4294967297),
]
LOG2Q_MIN, LOG2Q_MAX = 250.0, 256.0
checks = []


def ck(name, tag, ok, extra=None):
    checks.append(dict(check=name, fixture=tag, ok=bool(ok), extra=extra))
    return bool(ok)


def lbinom(n, j):
    if j < 0 or j > n:
        return float("-inf")
    if j == 0 or j == n:
        return 0.0
    return (lgamma(n + 1) - lgamma(j + 1) - lgamma(n - j + 1)) / LN2


def main():
    out = []
    for r in ROWS:
        n, k, A, h = r["n"], r["k"], r["A"], r["h"]
        assert A == k + h
        prize = r["name"].startswith("prize")
        lo, hi = -(-h // 2), h - 2                       # band proper
        rec = dict(name=r["name"], n=n, k=k, h=h, A=A, band=[lo, hi],
                   prize=prize)

        # ---- R1: full-rank non-vacuity, worst case is the deepest d
        worst_d = hi
        rec["fullrank_needs"] = dict(
            rule="n-k >= 3d-1", n_minus_k=n - k, d=worst_d,
            need=3 * worst_d - 1, ok=(n - k >= 3 * worst_d - 1),
            margin_ratio=(n - k) / (3 * worst_d - 1))
        ck("R1: the full-rank stratum is non-vacuous at every band-proper "
           "depth (n-k >= 3d-1)", r["name"], n - k >= 3 * worst_d - 1,
           rec["fullrank_needs"])

        # ---- R2: affine window dimension at the band ends
        rec["affine_dim"] = {str(d): (n - k - d) - 2 * d
                             for d in (lo, hi)}
        ck("R2: affine window dimension r'-2d is positive across the band",
           r["name"], all(v > 0 for v in rec["affine_dim"].values()),
           rec["affine_dim"])

        # ---- R3: structured survival (only meaningful when h = 2^s+1)
        s = (h - 1).bit_length() - 1
        is_pow2_plus1 = (h - 1) == (1 << s)
        rec["h_is_2s_plus_1"] = is_pow2_plus1
        g = 1
        while (n % (2 * g) == 0) and (k % (2 * g) == 0):
            g *= 2
        rec["max_2power_dividing_gcd_nk"] = g
        # CLOSED FORM (the first pass looped over j with a 4096 guard,
        # which TRUNCATED the small-M rows; corrected here).
        # h = 2^s+1 and M | 2^s force h = 1 mod M, and M | d, so
        # h-d = jM+1 with j >= 1 (j = 0 is the cascade tier d = h-1).
        #   d <= h-2            <=>  j >= 1
        #   d >= ceil(h/2)      <=>  jM+1 <= floor(h/2)
        #   THEOREM L: M(h-d) <= n-k-d  <=>  jM(M-1) <= n-k-h+1-M
        survive = {}
        if is_pow2_plus1:
            M = 2
            while M <= g:
                j1 = (h // 2 - 1) // M
                j2 = (n - k - h + 1 - M) // (M * (M - 1))
                J = min(j1, j2)
                if J >= 1:
                    dmax = h - (1 * M + 1)
                    dmin = h - (J * M + 1)
                    band_depths = (hi - lo) // M + 1
                    survive[M] = dict(n_depths=J, d_max=dmax, d_min=dmin,
                                      h_minus_d_max=h - dmin,
                                      band_depths_at_scale=band_depths,
                                      L_bites=(J < band_depths),
                                      slice_frac=J / band_depths)
                M *= 2
        rec["structured_survivors"] = {str(m): v
                                       for m, v in survive.items()}
        rec["max_surviving_M"] = max(survive) if survive else None
        if prize:
            ck("R3: the maximal surviving coset scale is 2^20 "
               "(banked audit: M = 2^1..2^20)", r["name"],
               rec["max_surviving_M"] == 1 << 20,
               dict(max_M=rec["max_surviving_M"],
                    log2=None if not survive
                    else log2(max(survive))))
            # the thin-slice claim
            big = survive.get(1 << 20)
            ck("R3b: at the maximal scale the surviving depths are a THIN "
               "slice at the top of the band", r["name"],
               big is not None and big["n_depths"] == 1, big)

        # ---- R4: budget, first moment, beta_d
        budget = 17 * n * n // 25
        rec["budget_17n2_25"] = budget
        rec["log2_budget"] = log2(17 * n * n / 25)
        fm = {}
        for d in (lo, hi):
            rp = n - k - d
            fm[str(d)] = dict(
                rprime=rp,
                log2_divisors=lbinom(n, rp),
                log2_first_moment_qmin=lbinom(n, rp) - 2 * d * LOG2Q_MIN,
                log2_first_moment_qmax=lbinom(n, rp) - 2 * d * LOG2Q_MAX,
                beta_d=(rp // (h - d - 1)) if h - d - 1 > 0 else None)
        rec["first_moment"] = fm
        ck("R4: the raw first moment is astronomically below the budget "
           "at both band ends (evidence only, not a bound)", r["name"],
           all(v["log2_first_moment_qmax"] < 0 for v in fm.values()),
           {kk: vv["log2_first_moment_qmax"] for kk, vv in fm.items()})
        out.append(rec)

    bad = [c for c in checks if not c["ok"]]
    print(f"checks: {len(checks)}   failures: {len(bad)}")
    for b in bad:
        print("  FAIL", b["check"], b["fixture"], b.get("extra"))
    print()
    for rec in out:
        print(f"=== {rec['name']}  n={rec['n']} k={rec['k']} h={rec['h']}"
              f"  band={rec['band']}")
        fr = rec["fullrank_needs"]
        print(f"    R1 full-rank non-vacuity: n-k={fr['n_minus_k']} >= "
              f"3d-1={fr['need']}  -> {fr['ok']}  (margin x"
              f"{fr['margin_ratio']:.1f})")
        print(f"    R2 affine window dim r'-2d at band ends: "
              f"{rec['affine_dim']}")
        print(f"    R4 budget 17n^2/25 = 2^{rec['log2_budget']:.2f};  "
              f"first moment at d=band ends (log2, q=2^256): "
              + ", ".join(f"d={kk}: {vv['log2_first_moment_qmax']:.4g}"
                          for kk, vv in rec["first_moment"].items()))
        if rec["structured_survivors"]:
            mm = rec["max_surviving_M"]
            b = rec["structured_survivors"][str(mm)]
            print(f"    R3 surviving coset scales: M = 2..{mm} "
                  f"(=2^{log2(mm):.0f}); at M={mm}: {b['n_depths']} "
                  f"depth(s), d in [{b['d_min']},{b['d_max']}], "
                  f"h-d <= {b['h_minus_d_max']}, "
                  f"{b['slice_frac']:.3g} of the M-admissible depths")
            print("       per-scale surviving depths (THEOREM L): "
                  + ", ".join(
                      f"2^{log2(int(m)):.0f}:{v['n_depths']}"
                      f"{'*' if v['L_bites'] else ''}"
                      for m, v in rec["structured_survivors"].items()))
        else:
            print("    R3 no coset scale survives (h not 2^s+1 or no M)")
    with open(__file__.replace(".py", ".json"), "w") as fh:
        json.dump(dict(rows=out, checks=checks, n_checks=len(checks),
                       n_fail=len(bad),
                       verdict="PASS" if not bad else "FAIL"), fh,
                  indent=1)


if __name__ == "__main__":
    main()
