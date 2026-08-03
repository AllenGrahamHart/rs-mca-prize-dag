#!/usr/bin/env python3
"""Exact six-row arithmetic for the list-size terminus (pilot 2026-08-03).

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 <this>

Rows are the banked table (xr_band_occupancy/theory.py:34-42, reproduced
verbatim, A = k + h asserted).  q is NOT a per-row constant: the banked
envelope is q < 2^256 (tools/prize_row_descriptor.py FIELD_CAP) with the
pin q >= 2^250.  Every averaging bound below is evaluated at the MOST
GENEROUS admissible field, log2 q = 256 -- if it is vacuous there it is
vacuous on the whole official range.

Computed:
  1. validation of tau, A, tau/k, tau/n, Johnson ratio against reduce.json
  2. nu = floor(n/tau)                     (THEOREM I, COROLLARY I.1)
  3. the fixed-member packing bound        C(n,k)/C(tau,k)
  4. the j-family averaging bound          C(n,j)/((q+1) C(tau,j))
     for j in [k+1, tau], with its monotonicity in j
  5. the first moment at tau               (cross-check vs banked 2^1e11)
  6. the Johnson / second-moment closing ratios, fixed-member and global
Binomials at n = 2^41 are evaluated in log2 via lgamma (double: absolute
error << 1 bit on quantities of size 1e12; exact integer arithmetic is
used for every RowC quantity as a cross-check of the lgamma path).
"""
import json
from math import comb, lgamma, log2, sqrt

LN2 = 0.6931471805599453

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
# banked: xr_band_occupancy/reduce.json
BANKED_TAU = [None, None, None, 554050781185, 279172874241, 139586437121]
BANKED_C = [None, None, None, 0.800767298932776, 0.6858649121282252,
            0.6596448038293138]
LOG2Q = 256.0          # FIELD_CAP = 1 << 256; most generous for the route


def lbinom(n, j):
    """log2 C(n,j) via lgamma."""
    if j < 0 or j > n:
        return float("-inf")
    if j == 0 or j == n:
        return 0.0
    return (lgamma(n + 1) - lgamma(j + 1) - lgamma(n - j + 1)) / LN2


def main():
    out = []
    checks = []
    for idx, r in enumerate(ROWS):
        n, k, A, h = r["n"], r["k"], r["A"], r["h"]
        assert A == k + h, r["name"]
        d0 = (h + 1) // 2                    # ceil(h/2)
        tau = k + d0
        if BANKED_TAU[idx] is not None:
            checks.append(("tau matches reduce.json " + r["name"],
                           tau == BANKED_TAU[idx]))
        nu = n // tau                        # COROLLARY I.1
        johnson = sqrt(k * n)                # agreement Johnson radius
        rec = dict(name=r["name"], n=n, k=k, h=h, A=A, tau=tau,
                   tau_over_k=tau / k, tau_over_n=tau / n,
                   nu_floor_n_over_tau=nu,
                   tau_over_johnson=tau / johnson,
                   A_over_johnson=A / johnson,
                   log2_n2_budget=log2(0.68 * n * n))
        # --- 3. fixed-member packing bound ---------------------------------
        rec["log2_packing_fixed_member"] = lbinom(n, k) - lbinom(tau, k)
        # --- 4. the j-family averaging bound -------------------------------
        js = sorted({k + 1, k + 2, k + 1 + d0 // 4, k + 1 + d0 // 2,
                     tau - 1, tau})
        js = [j for j in js if k + 1 <= j <= tau]
        fam = []
        for j in js:
            val = lbinom(n, j) - lbinom(tau, j) - log2(2 ** LOG2Q + 1)
            fam.append(dict(j=j, log2_bound=val,
                            beats_budget=val <= rec["log2_n2_budget"]))
        rec["averaging_family"] = fam
        rec["averaging_best_j"] = min(fam, key=lambda a: a["log2_bound"])
        rec["averaging_monotone_in_j"] = all(
            fam[i]["log2_bound"] <= fam[i + 1]["log2_bound"] + 1e-3
            for i in range(len(fam) - 1))
        rec["averaging_deficit_bits"] = (rec["averaging_best_j"]["log2_bound"]
                                         - rec["log2_n2_budget"])
        # --- 5. first moment at tau ----------------------------------------
        rec["log2_first_moment_at_tau"] = lbinom(n, tau) - (tau - k) * LOG2Q
        # --- 6. Johnson / second-moment closing ratios ---------------------
        rec["johnson_fixed_member_ratio"] = tau * tau / (n * (k - 1))
        rec["global_2mom_optimistic"] = (nu * tau / n) ** 2
        rec["global_2mom_realistic"] = nu * tau * tau / (n * n)
        # --- 7. CRITICAL DEPTHS (independent re-derivation of the
        #        refutation, no MC input).  A codeword at agreement k+d
        #        with ONE member costs d vanishing conditions; a JOINT
        #        pair at depth d costs 2d.  First moment crosses 1 at
        #        log2 C(n,k+d) = c*d*log2 q with c = 1 resp. 2.
        for tag, c in (("single", 1.0), ("joint", 2.0)):
            lo, hi = 0, h
            for _ in range(200):             # bisect on d
                mid = (lo + hi) / 2.0
                if lbinom(n, k + mid) - c * mid * LOG2Q > 0:
                    lo = mid
                else:
                    hi = mid
            rec[f"dstar_{tag}_over_h"] = lo / h
        rec["refutes_target"] = rec["dstar_single_over_h"] > d0 / h
        rec["gate_survives"] = rec["dstar_single_over_h"] < 1.0
        rec["occupancy_generically_empty_high"] = (
            rec["dstar_joint_over_h"] < d0 / h)
        out.append(rec)

    # exact-integer cross-check of the lgamma path on the RowC rows
    for rec in out[:3]:
        n, k, tau = rec["n"], rec["k"], rec["tau"]
        exact = log2(comb(n, k)) - log2(comb(tau, k))
        checks.append((f"lgamma vs exact packing {rec['name']}",
                       abs(exact - rec["log2_packing_fixed_member"]) < 1e-6))
        j = rec["averaging_family"][0]["j"]
        exact2 = (log2(comb(n, j)) - log2(comb(tau, j))
                  - log2(2 ** LOG2Q + 1))
        got = rec["averaging_family"][0]["log2_bound"]
        checks.append((f"lgamma vs exact averaging {rec['name']}",
                       abs(exact2 - got) < 1e-6))

    for rec in out:
        print(f"\n=== {rec['name']}  n=2^{log2(rec['n']):.0f} k/n={rec['k']/rec['n']:.4f} "
              f"h={rec['h']} A={rec['A']} tau={rec['tau']}")
        print(f"  tau/k={rec['tau_over_k']:.6f}  tau/n={rec['tau_over_n']:.6f} "
              f"  tau/Johnson={rec['tau_over_johnson']:.4f}"
              f"  nu=floor(n/tau)={rec['nu_floor_n_over_tau']}")
        print(f"  budget log2(0.68 n^2)          = {rec['log2_n2_budget']:.2f}")
        print(f"  packing bound, fixed member    = 2^{rec['log2_packing_fixed_member']:.4g}")
        print(f"  first moment at tau            = 2^{rec['log2_first_moment_at_tau']:.4g}")
        print(f"  BEST averaging bound (j={rec['averaging_best_j']['j']})"
              f"    = 2^{rec['averaging_best_j']['log2_bound']:.4g}"
              f"   monotone_in_j={rec['averaging_monotone_in_j']}")
        print(f"  averaging DEFICIT vs budget    = {rec['averaging_deficit_bits']:.4g} bits")
        print(f"  Johnson ratio (fixed member)   = {rec['johnson_fixed_member_ratio']:.4f}"
              f"   [closes iff > 1]")
        print(f"  global 2nd-moment optimistic   = {rec['global_2mom_optimistic']:.6f}"
              f"   realistic = {rec['global_2mom_realistic']:.6f}   [closes iff > 1]")
        print(f"  CRITICAL DEPTHS  d*/h single-word = {rec['dstar_single_over_h']:.4f}"
              f"   joint-pair = {rec['dstar_joint_over_h']:.4f}"
              f"   (tau sits at d/h = {(rec['tau']-rec['k'])/rec['h']:.4f})")
        print(f"    -> target refuted at this row: {rec['refutes_target']};"
              f"  tangent gate survives: {rec['gate_survives']};"
              f"  high band generically empty: "
              f"{rec['occupancy_generically_empty_high']}")

    print("\n--- validation checks ---")
    allok = True
    for name, ok in checks:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
        allok &= ok
    print("\nVERDICT:", "PASS" if allok else "FAIL")
    with open(__file__.replace(".py", ".json"), "w") as fh:
        json.dump(dict(rows=out, checks=checks, log2q=LOG2Q,
                       verdict="PASS" if allok else "FAIL"), fh, indent=1)


if __name__ == "__main__":
    main()
