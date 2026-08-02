#!/usr/bin/env python3
"""P-B |Gamma| exposure: the exact q-pin ledger and per-row exposure arithmetic.

Lane P-B, pilot pb_gamma_exposure (2026-08-02).  REPORT ONLY -- no
adjudication, no status change, nothing written outside this directory.

Run from the repo root under the compute law:

    tools/ramguard local -- python3 \
        notes/pilots_20260802/pb_gamma_exposure/qpin_ledger.py

Everything that enters a verdict is exact integer arithmetic.  The only
approximations are (a) the binary-entropy bracket used for log2 C(n,A) at the
prize rows (where the exact binomial is not representable), and it is a
RIGOROUS two-sided bracket, and (b) the Poisson heuristic for |Gamma|, which
is measured separately in gamma_law.py.
"""

from __future__ import annotations

import json
import os
from decimal import Decimal, getcontext
from fractions import Fraction
from math import comb

getcontext().prec = 80

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "QPIN_LEDGER.json")

# ---------------------------------------------------------------------------
# THE SIX CLEAN-RATE CANDIDATE ROWS
#
# (n, k, A) banked at, e.g.
#   critical/nodes/dyadic_profile_evaluation/proof.md:80-86  (the canonical
#       six-row table: row, rho, n, k, A, t, M_*, N_*, h)
#   critical/nodes/xr_smallcore_spread_count/notes/
#       audit_consumption_replay_20260710.py:98  BANKED_A
#   notes/pro_briefs_20260801/responses/
#       verify_brief4_lowcore_program_arithmetic.py:64-66 (RowC),
#       :67-69 (prize)
# h = A - k is the excess ("H" in the brief-4 script is h+1).
# ---------------------------------------------------------------------------
ROWS = [
    ("RowC 1/4",   1 << 10, 1 << 8,  261),
    ("RowC 1/8",   1 << 10, 1 << 7,  133),
    ("RowC 1/16",  1 << 10, 1 << 6,   67),
    ("prize 1/4",  1 << 41, 1 << 39, 558345748481),
    ("prize 1/8",  1 << 41, 1 << 38, 283467841537),
    ("prize 1/16", 1 << 41, 1 << 37, 141733920769),
]

EPS_BITS = 128          # tools/prize_row_descriptor.py:17 EPSILON_BITS
FIELD_CAP = 1 << 256    # tools/prize_row_descriptor.py:18 FIELD_CAP
K_CAP = 1 << 40         # tools/prize_row_descriptor.py:19 K_CAP

# The two banked ENVELOPE q-pins (numerator budget B* = floor(q / 2^128)).
#   RowC :  B* = 2^122
#     background/nodes/tangent_clean_anchor_route_classification/
#         statement.md:38  "RowC fixes B*=2^122"
#     background/nodes/e1_clean_anchor_exact_collision_allowance/verify.py:16
#         ROWC_BUDGET = 1 << 122
#     background/nodes/qfloor_clean_anchor_norm_threshold_route_cut/verify.py:23
#     background/nodes/identity_prefix_clean_anchor_route_classification/
#         verify.py:22
#   prize:  B* = 317494674775468773183020924238786383963
#     background/nodes/e1_prize_field_floor_even_norm_exclusion/statement.md:15
#     background/nodes/tangent_clean_anchor_route_classification/statement.md:40
# The induced intervals are banked verbatim at
#   background/nodes/e1_pair_feasible_prime_field_reduction/proof.md:20-22
#       I_C = [2^250, 2^250 + 2^128 - 1]
#   background/nodes/e1_pair_feasible_prime_field_reduction/proof.md:38-41
#       I_P = [B_P 2^128, (B_P+1) 2^128 - 1]
BSTAR_ROWC = 1 << 122
BSTAR_PRIZE = 317494674775468773183020924238786383963


def log2_floor(x: int) -> int:
    return x.bit_length() - 1


def dlog2(x: Decimal) -> Decimal:
    return x.ln() / Decimal(2).ln()


def entropy_bracket(n: int, a: int) -> tuple[Decimal, Decimal]:
    """Rigorous two-sided bracket on log2 C(n, a).

    Standard:  2^{n H(a/n)} / (n+1)  <=  C(n,a)  <=  2^{n H(a/n)}.
    Returns (lo, hi) with lo <= log2 C(n,a) <= hi.
    """
    p = Decimal(a) / Decimal(n)
    one = Decimal(1)
    h = -(p * dlog2(p) + (one - p) * dlog2(one - p))
    hi = Decimal(n) * h
    lo = hi - dlog2(Decimal(n + 1))
    return lo, hi


def integer_kth_root(x: int, k: int) -> int:
    """floor(x ** (1/k)) exactly, for x >= 0, k >= 1."""
    if x < 0:
        raise ValueError
    if x == 0:
        return 0
    r = 1 << ((x.bit_length() + k - 1) // k)
    while True:
        nr = ((k - 1) * r + x // r ** (k - 1)) // k
        if nr >= r:
            return r
        r = nr


def ceil_kth_root(x: int, k: int) -> int:
    r = integer_kth_root(x, k)
    return r if r ** k >= x else r + 1


def row_record(name: str, n: int, k: int, a: int) -> dict:
    h = a - k
    budget8 = 8 * n ** 3
    budget16 = 16 * n ** 3
    # n is a power of two on every official row, so log2(8 n^3) is an
    # EXACT integer and every comparison below stays in exact arithmetic.
    assert n & (n - 1) == 0
    lg_n = n.bit_length() - 1
    lg_b8 = 3 + 3 * lg_n
    assert budget8 == 1 << lg_b8
    lg_b16 = lg_b8 + 1

    exact_binom = n <= 4096
    if exact_binom:
        C = comb(n, a)
        lgC_lo = lgC_hi = Decimal(C.bit_length() - 1)   # floor(log2 C)
        lgC_exact = True
    else:
        C = None
        lgC_lo, lgC_hi = entropy_bracket(n, a)
        lgC_exact = False

    # -----------------------------------------------------------------
    # The three q-thresholds.  All are stated as EXPONENT inequalities so
    # that they can be decided exactly when C is exact, and via the
    # entropy bracket otherwise.
    #
    #  L1  soundness floor      q^h  >= C * 2^128     (mean live slopes
    #                                                  <= B* = q/2^128)
    #  L2  no-competition       q^h  >= C             (mean |W_z| <= 1)
    #  L3  P-B supply floor     q^{h-1} >= C / 8n^3   (mean live slopes
    #                                                  <= 8 n^3)
    #
    # EXPOSED WINDOW = [L1, L3).  It is non-empty iff L3 > L1 iff
    #      C > (8 n^3)^h * 2^{128 (h-1)}                            (*)
    # which for n a power of two is the exact integer comparison
    #      log2 C  >  h * lg_b8 + 128 * (h - 1).
    # -----------------------------------------------------------------
    rhs_exp = h * lg_b8 + EPS_BITS * (h - 1)
    if lgC_exact:
        exposed = C > (1 << rhs_exp)
        exposed_certain = True
    else:
        exposed = lgC_lo > Decimal(rhs_exp)
        safe = lgC_hi < Decimal(rhs_exp)
        exposed_certain = exposed or safe

    rec: dict = dict(
        row=name, n=n, k=k, A=a, h=h,
        rate=f"{Fraction(k, n).numerator}/{Fraction(k, n).denominator}",
        budget_8n3=budget8, budget_16n3=budget16,
        log2_budget_8n3=lg_b8, log2_budget_16n3=lg_b16,
        log2_C_lo=str(lgC_lo), log2_C_hi=str(lgC_hi),
        log2_C_is_exact=lgC_exact,
        exposure_criterion_rhs_log2=rhs_exp,
        exposure_criterion="C(n,A) > (8n^3)^h * 2^(128(h-1))",
        EXPOSED_WINDOW_NONEMPTY=bool(exposed),
        verdict_certain=bool(exposed_certain),
    )

    if lgC_exact:
        rec["C_exact_bitlen"] = C.bit_length()
        rec["margin_bits_log2C_minus_rhs"] = (C.bit_length() - 1) - rhs_exp
        # exact thresholds
        q_L1 = ceil_kth_root(C << EPS_BITS, h)
        q_L2 = ceil_kth_root(C, h)
        q_L3 = ceil_kth_root(-(-C // budget8), h - 1) if h >= 2 else None
        rec["q_L1_soundness_floor"] = q_L1
        rec["q_L1_log2"] = log2_floor(q_L1)
        rec["q_L2_no_competition_floor"] = q_L2
        rec["q_L2_log2"] = log2_floor(q_L2)
        rec["q_L3_pb_supply_floor"] = q_L3
        rec["q_L3_log2"] = log2_floor(q_L3) if q_L3 else None
        if q_L3 and q_L3 > q_L1:
            rec["exposed_window"] = [q_L1, q_L3 - 1]
            rec["exposed_window_log2"] = [log2_floor(q_L1),
                                          log2_floor(q_L3 - 1)]
            # worst-case generic |Gamma| inside the window (at q = L1)
            worst = C // q_L1 ** (h - 1)
            rec["generic_live_slopes_at_L1"] = worst
            rec["generic_live_slopes_at_L1_over_8n3"] = worst // budget8
            rec["generic_live_slopes_at_L1_log2"] = log2_floor(worst)
    else:
        rec["margin_bits_log2C_minus_rhs_lo"] = str(lgC_lo - Decimal(rhs_exp))
        rec["margin_bits_log2C_minus_rhs_hi"] = str(lgC_hi - Decimal(rhs_exp))
        rec["q_L1_log2_approx"] = str((lgC_hi + EPS_BITS) / h)
        rec["q_L2_log2_approx"] = str(lgC_hi / h)
        rec["q_L3_log2_approx"] = str((lgC_hi - lg_b8) / (h - 1))

    # ---- the banked ENVELOPE pin -------------------------------------
    if name.startswith("RowC"):
        bstar, lo, hi = BSTAR_ROWC, BSTAR_ROWC << EPS_BITS, \
            ((BSTAR_ROWC + 1) << EPS_BITS) - 1
        pin_src = ("background/nodes/e1_pair_feasible_prime_field_reduction/"
                   "proof.md:20-22")
    else:
        bstar, lo, hi = BSTAR_PRIZE, BSTAR_PRIZE << EPS_BITS, \
            ((BSTAR_PRIZE + 1) << EPS_BITS) - 1
        pin_src = ("background/nodes/e1_pair_feasible_prime_field_reduction/"
                   "proof.md:38-41")
    rec["envelope_Bstar"] = bstar
    rec["envelope_Bstar_log2_floor"] = log2_floor(bstar)
    rec["envelope_q_interval"] = [lo, hi]
    rec["envelope_q_log2_floor"] = log2_floor(lo)
    rec["envelope_q_pin_source"] = pin_src
    rec["envelope_q_under_2^256"] = hi < FIELD_CAP
    rec["Bstar_over_8n3"] = Fraction(bstar, budget8).limit_denominator(10**9)
    rec["Bstar_over_8n3_str"] = str(Fraction(bstar, budget8))
    rec["Bstar_over_8n3_float"] = float(bstar) / float(budget8)
    rec["k_le_2^40"] = k <= K_CAP

    # ---- the smallest P-B-style constant valid at EVERY admissible q ----
    # sup over q >= L1 of the first-moment live-slope count C/q^(h-1) is
    # attained at q = L1 = (C 2^128)^(1/h) and equals
    #     2^{(log2 C - 128(h-1)) / h}.
    # The row is EXPOSED iff this exceeds 8 n^3 (same criterion as above).
    req_lo = (lgC_lo - Decimal(EPS_BITS * (h - 1))) / Decimal(h)
    req_hi = (lgC_hi - Decimal(EPS_BITS * (h - 1))) / Decimal(h)
    rec["required_constant_log2_lo"] = str(req_lo)
    rec["required_constant_log2_hi"] = str(req_hi)
    rec["required_constant_over_8n3_log2_hi"] = str(req_hi - Decimal(lg_b8))

    # supply at the pinned q (log2, always negative at admissible pins)
    lo_lg = Decimal(log2_floor(lo))
    rec["log2_mean_witnesses_total_at_pin"] = str(lgC_hi - (h - 1) * lo_lg)
    rec["log2_mean_Wz_at_pin"] = str(lgC_hi - h * lo_lg)
    return rec


def main() -> None:
    recs = [row_record(*r) for r in ROWS]

    print("=" * 78)
    print("PART 1  --  THE SIX ROWS, EXACT")
    print("=" * 78)
    print(f"{'row':<11}{'n':>14}{'k':>14}{'A':>14}{'h':>12}"
          f"{'lg 8n^3':>9}{'lg 16n^3':>10}")
    for r in recs:
        print(f"{r['row']:<11}{r['n']:>14}{r['k']:>14}{r['A']:>14}"
              f"{r['h']:>12}{r['log2_budget_8n3']:>9}"
              f"{r['log2_budget_16n3']:>10}")

    print()
    print("8n^3 and 16n^3 exact:")
    for r in recs:
        print(f"  {r['row']:<11} 8n^3 = {r['budget_8n3']:<40}"
              f" 16n^3 = {r['budget_16n3']}")

    print()
    print("=" * 78)
    print("PART 2  --  THE BANKED ENVELOPE q-PIN  (B* = floor(q/2^128))")
    print("=" * 78)
    for r in recs:
        print(f"  {r['row']:<11} B* = 2^{r['envelope_Bstar_log2_floor']}"
              f"  q in [2^{r['envelope_q_log2_floor']}, ...]"
              f"   q<2^256: {r['envelope_q_under_2^256']}"
              f"   B*/8n^3 = {r['Bstar_over_8n3_float']:.5g}")
    print()
    print("  RowC  q-interval  I_C = "
          f"[{recs[0]['envelope_q_interval'][0]},")
    print(f"                        {recs[0]['envelope_q_interval'][1]}]")
    print("  prize q-interval  I_P = "
          f"[{recs[3]['envelope_q_interval'][0]},")
    print(f"                        {recs[3]['envelope_q_interval'][1]}]")

    print()
    print("=" * 78)
    print("PART 3  --  THE EXPOSURE CRITERION   C(n,A) > (8n^3)^h 2^(128(h-1))")
    print("=" * 78)
    print(f"{'row':<11}{'log2 C(n,A)':>22}{'rhs log2':>18}"
          f"{'margin':>18}  verdict")
    for r in recs:
        if r["log2_C_is_exact"]:
            lgc = f"{r['C_exact_bitlen'] - 1}"
            marg = f"{r['margin_bits_log2C_minus_rhs']:+d}"
        else:
            lgc = f"[{Decimal(r['log2_C_lo']):.6E}]"
            marg = f"{Decimal(r['margin_bits_log2C_minus_rhs_hi']):+.6E}"
        v = "EXPOSED" if r["EXPOSED_WINDOW_NONEMPTY"] else "safe-by-supply"
        if not r["verdict_certain"]:
            v += " (UNDECIDED by bracket)"
        print(f"{r['row']:<11}{lgc:>22}{r['exposure_criterion_rhs_log2']:>18}"
              f"{marg:>18}  {v}")

    print()
    print("=" * 78)
    print("PART 4  --  THE THREE q-THRESHOLDS (exact where n <= 4096)")
    print("=" * 78)
    print("  L1 soundness floor      q^h     >= C 2^128   (E[#live] <= B*)")
    print("  L2 no-competition floor q^h     >= C         (E[|W_z|] <= 1)")
    print("  L3 P-B supply floor     q^(h-1) >= C / 8n^3  (E[#live] <= 8n^3)")
    print()
    print(f"{'row':<11}{'lg L1':>10}{'lg L2':>10}{'lg L3':>10}"
          f"{'lg q_pin':>11}   exposed window")
    for r in recs:
        if r["log2_C_is_exact"]:
            w = r.get("exposed_window_log2")
            ws = (f"[2^{w[0]}, 2^{w[1]}]" if w else "EMPTY")
            print(f"{r['row']:<11}{r['q_L1_log2']:>10}{r['q_L2_log2']:>10}"
                  f"{r['q_L3_log2']:>10}{r['envelope_q_log2_floor']:>11}"
                  f"   {ws}")
        else:
            print(f"{r['row']:<11}"
                  f"{Decimal(r['q_L1_log2_approx']):>10.5g}"
                  f"{Decimal(r['q_L2_log2_approx']):>10.5g}"
                  f"{Decimal(r['q_L3_log2_approx']):>10.5g}"
                  f"{r['envelope_q_log2_floor']:>11}   EMPTY (L3 < L1)")

    print()
    print("=" * 78)
    print("PART 5  --  SUPPLY AT THE BANKED PIN  (log2, mean over pencils)")
    print("=" * 78)
    print(f"{'row':<11}{'lg E[#witnesses]':>22}{'lg E[|W_z|]':>22}")
    for r in recs:
        print(f"{r['row']:<11}"
              f"{Decimal(r['log2_mean_witnesses_total_at_pin']):>22.6E}"
              f"{Decimal(r['log2_mean_Wz_at_pin']):>22.6E}")

    print()
    print("=" * 78)
    print("PART 5b --  SMALLEST P-B CONSTANT VALID AT EVERY ADMISSIBLE q")
    print("            sup_{q >= L1} C(n,A)/q^(h-1) = "
          "2^((log2 C - 128(h-1))/h)")
    print("=" * 78)
    print(f"{'row':<11}{'log2 required':>18}{'log2 8n^3':>12}"
          f"{'excess bits':>14}   verdict")
    for r in recs:
        req = Decimal(r["required_constant_log2_hi"])
        exc = req - Decimal(r["log2_budget_8n3"])
        v = "EXPOSED" if exc > 0 else "fits 8n^3"
        print(f"{r['row']:<11}{req:>18.4f}{r['log2_budget_8n3']:>12}"
              f"{exc:>+14.4f}   {v}")

    print()
    print("=" * 78)
    print("PART 6  --  EXPOSED-ROW DETAIL")
    print("=" * 78)
    for r in recs:
        if not r["EXPOSED_WINDOW_NONEMPTY"]:
            continue
        print(f"  {r['row']}:")
        print(f"    exposed window q in [{r['exposed_window'][0]},")
        print(f"                         {r['exposed_window'][1]}]")
        print(f"    i.e. [2^{r['exposed_window_log2'][0]}, "
              f"2^{r['exposed_window_log2'][1]}]  "
              f"(width {r['exposed_window_log2'][1] - r['exposed_window_log2'][0]}"
              f" binary orders)")
        print(f"    at the window floor q = L1 = {r['q_L1_soundness_floor']}")
        print(f"      mean generic live slopes = {r['generic_live_slopes_at_L1']}")
        print(f"      = 2^{r['generic_live_slopes_at_L1_log2']}"
              f" = {r['generic_live_slopes_at_L1_over_8n3']} x 8n^3")
        print(f"    the banked envelope pin q ~ 2^{r['envelope_q_log2_floor']}"
              f" lies ABOVE L3 = 2^{r['q_L3_log2']}: pinned row is"
              f" supply-safe")

    payload = []
    for r in recs:
        d = {k: (str(v) if isinstance(v, Fraction) else v)
             for k, v in r.items()}
        payload.append(d)
    with open(OUT, "w") as fh:
        json.dump(payload, fh, indent=1, sort_keys=True)
    print()
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
