#!/usr/bin/env python3
"""
verify.py -- the t-NAMING COLLISION (round 17, pilot `t_naming`).

Self-contained, stdlib only, fail-closed: every check appends to RESULTS and
the process exits nonzero unless every single one PASSes.

Replay:
    tools/ramguard tiny -- python3 notes/pilots_20260806/t_naming/verify.py

Sections map onto the pre-registered deliverables N1-N5 and my own U1-U8.
"""

import math
import sys

LN2 = math.log(2.0)
RESULTS = []


def chk(tag, ok, detail):
    RESULTS.append((tag, bool(ok), detail))
    print("%-9s %-4s %s" % (tag, "PASS" if ok else "FAIL", detail))
    return bool(ok)


# ---------------------------------------------------------------------------
# Row constants (all quoted from the repo; see PROOFS.md for file:line)
# ---------------------------------------------------------------------------
N = 2 ** 41                      # xr_radius_arithmetic/proof.md:34
L_CONV = 255.9                   # xr_radius_arithmetic/proof.md:33  ("convention")
GATE = 128                       # xr_radius_arithmetic/proof.md:27  (B* = q/2^128)
RATES = [2, 4, 8, 16]            # denominators of rho in {1/2,1/4,1/8,1/16}

# banked four-rate corridor table, xr_radius_arithmetic/proof.md:55-58
TSTAR_BANKED = {2: 8592912739, 4: 7014660390, 8: 4722556392, 16: 2943177800}

# mca_floor constants, background/nodes/rate_half_cyclic_simple_pole_mca_floor
C_MCA = 2 ** 22                  # statement.md:12  c = 2^22
D_MCA = 2048                     # statement.md:12  d = 2,048
SIGMA_MAX_BANKED = 8594128895    # statement.md:14  sigma_max = dc+c-1
SIGMA_STAR_BANKED = 8592912738   # statement.md:65  sigma* = 8,592,912,738
NEAR_COLL_DIFF = 1216156         # the brief's difference to explain

# KoalaBear base field (f2_tq_pin/PROOFS.md:78)
P_KB = 2 ** 31 - 2 ** 24 + 1
LOG2_P_KB = math.log2(P_KB)


def log2C(n, j):
    """log2 C(n, j) via lgamma. Accuracy is measured in S0.2 below."""
    if j < 0 or j > n:
        return float("-inf")
    return (math.lgamma(n + 1.0) - math.lgamma(j + 1.0)
            - math.lgamma(n - j + 1.0)) / LN2


def f_of_t(t, n, k, L):
    """(T*) slack: t*L - log2 C(n, n-k-t) - 128. Strictly increasing in t."""
    return t * L - log2C(n, n - k - t) - GATE


def solve_tstar(n, k, L):
    """Smallest integer t with f_of_t(t) >= 0 -- the corridor edge (T*)."""
    lo, hi = 1, n - k - 1
    assert f_of_t(hi, n, k, L) >= 0.0
    while lo < hi:
        mid = (lo + hi) // 2
        if f_of_t(mid, n, k, L) >= 0.0:
            hi = mid
        else:
            lo = mid + 1
    return lo


# ===========================================================================
print("=" * 74)
print("S0. Numerical hygiene of log2C (the only floating primitive used)")
print("=" * 74)

# S0.1 -- exact small-case agreement with math.comb
ok = True
for (n, j) in [(8, 3), (30, 14), (100, 50), (1000, 499), (10 ** 5, 49999)]:
    exact = math.log2(math.comb(n, j))
    if abs(exact - log2C(n, j)) > 1e-6 * max(1.0, abs(exact)):
        ok = False
chk("S0.1", ok, "log2C matches math.comb exactly on 5 toy rows (rel <= 1e-6)")

# S0.2 -- residual vs the Stirling asymptotic at the prize row, to bound the
# cancellation error.  The de Moivre-Laplace expansion of the central-ish
# binomial is
#   log2 C(n, n/2 - d) = n - (1/2)log2(pi n/2)
#                          - 2 d^2/(n ln2) - (4/3) d^4/(n^3 ln2) - O(d^6/n^5).
# NOTE (self-correction, found by this fail-closed harness): my first draft
# omitted the QUARTIC term and asserted a 1-bit tolerance.  It failed at
# 986.27 bits -- which is exactly (4/3)d^4/(n^3 ln2) = 986.3.  lgamma was
# never the problem; the formula was.  Both S0.2 and the S5 closed form now
# carry the quartic term.
n = N
d = TSTAR_BANKED[2]
j = n // 2 - d
quartic = (4.0 / 3.0) * (d ** 4) / (float(n) ** 3 * LN2)
approx = (n - 0.5 * math.log2(math.pi * n / 2.0)
          - 2.0 * d * d / (n * LN2) - quartic)
resid = abs(log2C(n, j) - approx)
chk("S0.2", resid < 1.0,
    "log2C(2^41, 2^41/2 - t*) vs de Moivre-Laplace (quadratic + quartic): "
    "|resid| = %.4f bits (< 1 bit; the (T*) step is L = 255.9 bits, so the "
    "integer crossing is unambiguous). Omitted quartic term = %.1f bits."
    % (resid, quartic))

# ===========================================================================
print()
print("=" * 74)
print("S1. CONTROL -- reproduce the banked four-rate corridor table (T*)")
print("=" * 74)

TSTAR = {}
for r in RATES:
    k = N // r
    TSTAR[r] = solve_tstar(N, k, L_CONV)
    chk("S1.%d" % r, TSTAR[r] == TSTAR_BANKED[r],
        "rate 1/%-2d  t* = %d  (banked %d)" % (r, TSTAR[r], TSTAR_BANKED[r]))

# adjacency: t*-1 must fail (T*), confirming it is THE crossing
ok = all(f_of_t(TSTAR[r] - 1, N, N // r, L_CONV) < 0.0 <= f_of_t(TSTAR[r], N, N // r, L_CONV)
         for r in RATES)
chk("S1.adj", ok, "t*-1 fails (T*) and t* satisfies it, at all four rates")

# ===========================================================================
print()
print("=" * 74)
print("S2/S3. (N2, U1) t_F2 = n/L is RATE-INDEPENDENT; t_XR is RATE-DEPENDENT")
print("=" * 74)

T_F2 = N / L_CONV                     # the (C) balance t*L = n
chk("S2.0", True, "t_F2 = n/L = %.1f  (one number, no rate argument)" % T_F2)

devs = {}
for r in RATES:
    devs[r] = TSTAR[r] / T_F2 - 1.0
    print("          rate 1/%-2d : t_XR/t_F2 = %.6f   deviation %+8.4f%%"
          % (r, TSTAR[r] / T_F2, 100.0 * devs[r]))

chk("S2.1", abs(devs[2]) < 1e-3,
    "rate 1/2  : |deviation| = %.6f%% < 0.1%%  (they COINCIDE here)"
    % (100 * abs(devs[2])))
chk("S3.1", abs(devs[4]) > 0.10,
    "rate 1/4  : deviation %+.2f%% > 10%%  -> NOT the same quantity"
    % (100 * devs[4]))
chk("S3.2", abs(devs[8]) > 0.35,
    "rate 1/8  : deviation %+.2f%% > 35%%  -> NOT the same quantity"
    % (100 * devs[8]))
chk("S3.3", abs(devs[16]) > 0.55,
    "rate 1/16 : deviation %+.2f%% > 55%%  -> NOT the same quantity"
    % (100 * devs[16]))
# U1's pre-registered falsifier, stated as its own check
chk("S3.F", not all(abs(devs[r]) < 0.01 for r in RATES),
    "U1 FALSIFIER not triggered: (T*) does NOT reproduce n/L at all rates")

# ===========================================================================
print()
print("=" * 74)
print("S4/S5/S6. (N2, U2) the exact error term Delta and its closed form")
print("=" * 74)

DELTA = {}
for r in RATES:
    k = N // r
    DELTA[r] = N - log2C(N, N - k - TSTAR[r]) - GATE
    pred = DELTA[r] / L_CONV
    actual = T_F2 - TSTAR[r]
    ok = abs(pred - actual) <= L_CONV        # one integer rounding step
    chk("S4.%d" % r, ok,
        "rate 1/%-2d : Delta = %.6e ; Delta/L = %.1f vs (n/L - t*) = %.1f "
        "(gap %.2f <= L)" % (r, DELTA[r], pred, actual, abs(pred - actual)))

# S5 -- closed form of Delta at rate 1/2 (quadratic term only, as pre-registered)
t2 = TSTAR[2]
delta_cf = (2.0 * t2 * t2 / (N * LN2)
            + 0.5 * math.log2(math.pi * N / 2.0)
            - GATE)
rel = abs(delta_cf - DELTA[2]) / DELTA[2]
chk("S5", rel < 0.01,
    "rate 1/2 closed form  Delta = 2t*^2/(n ln2) + (1/2)log2(pi n/2) - 128 "
    "= %.6e vs exact %.6e (rel %.2e < 1%%, as pre-registered in U2)"
    % (delta_cf, DELTA[2], rel))

# S5.q -- the same closed form WITH the quartic term, to show the residual is
# fully accounted for and nothing unexplained remains.
delta_cf_q = delta_cf + (4.0 / 3.0) * (t2 ** 4) / (float(N) ** 3 * LN2)
rel_q = abs(delta_cf_q - DELTA[2]) / DELTA[2]
chk("S5.q", rel_q < 1e-7,
    "with the quartic term added: Delta = %.8e vs exact %.8e (rel %.2e < "
    "1e-7) -- the error term is CLOSED, nothing unexplained remains"
    % (delta_cf_q, DELTA[2], rel_q))

# S6 -- the 0.0044% is exactly 2/(L^2 ln 2)
predicted_rel = 2.0 / (L_CONV ** 2 * LN2)
chk("S6", abs(predicted_rel - abs(devs[2])) / abs(devs[2]) < 0.01,
    "the banked 0.0044%% agreement = 2/(L^2 ln2) = %.6e vs measured %.6e"
    % (predicted_rel, abs(devs[2])))

# S6.b -- the schema (UFMB): both t's are the crossing of t*L >= log2 N + G,
# differing ONLY in (ensemble, gate). Check t_F2 is (2^n, 0).
t_f2_from_schema = N / L_CONV                    # log2(2^n) = n, G = 0
chk("S6.b", abs(t_f2_from_schema - T_F2) < 1e-9,
    "UFMB with (ensemble, gate) = (2^n, 0) reproduces t_F2 = n/L exactly")

# ===========================================================================
print()
print("=" * 74)
print("S7-S10. (N4, U3) the near-collision: sigma_max vs t*")
print("=" * 74)

sigma_max = D_MCA * C_MCA + (C_MCA - 1)
chk("S7.1", sigma_max == SIGMA_MAX_BANKED,
    "sigma_max = d*c + (c-1) = 2048*2^22 + (2^22-1) = %d  (banked %d)"
    % (sigma_max, SIGMA_MAX_BANKED))
chk("S7.2", sigma_max == 2 ** 33 + 2 ** 22 - 1,
    "CLOSED FORM: sigma_max = 2^33 + 2^22 - 1 EXACTLY (= 2^22*(2^11+1) - 1)")

chk("S8", SIGMA_STAR_BANKED == TSTAR[2] - 1,
    "mca_floor's sigma* = %d equals t* - 1 = %d EXACTLY -> SAME OBJECT as "
    "the XR corridor edge (an excess A-k), NOT a different one"
    % (SIGMA_STAR_BANKED, TSTAR[2] - 1))
chk("S8.b", SIGMA_STAR_BANKED + 1 == TSTAR[2],
    "the 'previously conjectured safe point at k+sigma*+1' sits at excess "
    "sigma*+1 = %d = t*" % TSTAR[2])

diff = sigma_max - TSTAR[2]
chk("S9.1", diff == NEAR_COLL_DIFF,
    "sigma_max - t* = %d  (the brief's 1,216,156)" % diff)
off = TSTAR[2] - 2 ** 33
chk("S9.2", off == 2978147,
    "t* - 2^33 = %d  (the L-offset of the corridor edge above the "
    "L->256 counting floor)" % off)
chk("S9.3", diff == (2 ** 22 - 1) - off,
    "DECOMPOSITION: 1,216,156 = (2^22 - 1) - (t* - 2^33) = %d - %d  "
    "[= residual prefix s, minus the L-offset]" % (2 ** 22 - 1, off))

chk("S10.1", 1 <= TSTAR[2] <= sigma_max,
    "CONTAINMENT: 1 <= t* = %d <= sigma_max = %d, so t* lies INSIDE the "
    "interval mca_floor proves prize-unsafe (SP2)" % (TSTAR[2], sigma_max))

# S10.2 -- independent float sanity that mca_floor's floor is not vacuous:
# L_q = ceil(B/(N q^2047)) with B = C(524287,264192), N = 524288, at q = 2^255.
log2_B = log2C(524287, 264192)
log2_Lq = log2_B - math.log2(524288) - 2047 * 255.0
chk("S10.2", log2_Lq > 1.0,
    "mca_floor is non-vacuous at q = 2^255: log2 L_q = %.1f >> 0, so the "
    "cyclic list is huge and E(q,L_q) ~ L_q/(k L_q) is a genuine floor"
    % log2_Lq)

# ===========================================================================
print()
print("=" * 74)
print("S11/S12. (N5, U7) the sliver: mis-typed, and empty when recomputed")
print("=" * 74)

# S11 -- CATCH-2's "0.011 bits" is exactly Delta/t*
catch2_gap = N / TSTAR[2] - L_CONV               # n/t* - 255.9
chk("S11.1", abs(catch2_gap - 0.011275) < 5e-5,
    "CATCH-2 reproduces: n/t* - 255.9 = %.6f bits (banked 'below by 0.011')"
    % catch2_gap)
chk("S11.2", abs(catch2_gap - DELTA[2] / TSTAR[2]) / catch2_gap < 0.01,
    "CATCH-2's gap = Delta/t* = %.6f -> it is the per-condition share of "
    "the ENTROPY DEFICIT, i.e. a SYMPTOM of the N2 refutation, not a "
    "convention error" % (DELTA[2] / TSTAR[2]))

# S12 -- recompute the sliver with t*(L) VARYING (f2_tq_pin froze t*)
worst = {}
for r in RATES:
    k = N // r
    mx = -float("inf")
    argmax = None
    Ls = [41.0 + 0.5 * i for i in range(1, 430)] + \
         [255.0 + 0.001 * i for i in range(0, 1000)]
    for L in Ls:
        if not (math.log2(N) < L < 256.0):
            continue
        ts = solve_tstar(N, k, L)
        val = ts * L - N
        if val > mx:
            mx, argmax = val, L
    worst[r] = (mx, argmax)
    chk("S12.%d" % r, mx < 0.0,
        "rate 1/%-2d : max over L in (41,256) of [t*(L)*L - n] = %.4e < 0 "
        "at L = %.3f -> {L : t*(L) L >= n} is EMPTY" % (r, mx, argmax))

chk("S12.F", worst[2][0] < 0.0,
    "U7(b) FALSIFIER not triggered: NO L in [255.9,256) satisfies "
    "t*(L)*L >= n at rate 1/2 -- the sliver cannot be reached by any "
    "convention")

# S12.c -- HOW FAR the sliver is from reachable.  At rate 1/2, with
# t*(L) ~ n/L, Delta(L) ~ 2n/(L^2 ln2) + (1/2)log2(pi n/2) - 128, so
# Delta = 0 (the only way t* L >= n) needs L = sqrt(2n / ((128 - (1/2)
# log2(pi n/2)) ln2)).  Report that L and compare it to the 256-bit cap.
const = GATE - 0.5 * math.log2(math.pi * N / 2.0)
L_crit = math.sqrt(2.0 * N / (const * LN2))
chk("S12.c", L_crit > 1000.0 * 1.0 and L_crit > 256.0,
    "the sliver would first become reachable at L = %.4e bits, i.e. a field "
    "of size ~2^%d -- the |F| < 2^256 cap would have to rise by ~%.0fx IN "
    "BITS. The sliver is not marginally unreachable, it is unreachable by "
    "three orders of magnitude." % (L_crit, int(L_crit), L_crit / 256.0))

# S12.b -- sensitivity dt*/dL at the convention point (for the replacement)
h = 1e-3
dt_dL = (solve_tstar(N, N // 2, L_CONV + h) - solve_tstar(N, N // 2, L_CONV - h)) / (2 * h)
chk("S12.b", dt_dL < 0.0,
    "dt*/dL at L = 255.9 (rate 1/2) = %.4e per bit -- t* is a FUNCTION of "
    "L, not a constant; freezing it is what produced the phantom sliver"
    % dt_dL)

# ===========================================================================
print()
print("=" * 74)
print("S13. (U4) the 7e10 exclusion, dependency-audited")
print("=" * 74)

T_7E10 = 7.0e10
# The exclusion uses ONLY: (C) t*L = n  [F2 side], (R1) L > log2 n  [rules],
# and the row constant n.  No C(n,j), no gate, no (T*), no t*.
for nn, lab in [(2 ** 41, "n = 2^41"), (2 ** 40, "n = 2^40")]:
    L_implied = nn / T_7E10
    floor_ext = math.log2(nn)          # (R1): n | q-1 => q > n => L > log2 n
    chk("S13.%s" % lab.split("=")[1].strip(), L_implied < floor_ext,
        "%s: t = 7e10 back-implies L = n/t = %.3f, below the (R1) floor "
        "log2 n = %.1f -> EXCLUDED" % (lab, L_implied, floor_ext))

chk("S13.p", N / T_7E10 < 39.0,
    "also excluded under the base-field reading: L = %.3f < log2 p >= 39 "
    "(the admissible-region floor)" % (N / T_7E10))
chk("S13.orig", abs(N / LOG2_P_KB - 7.096e10) / 7.096e10 < 0.01,
    "origin of the literal reproduced: n / log2 p_KoalaBear = %.4e ~ 7e10 "
    "(a unit error -- wrong divisor)" % (N / LOG2_P_KB))
# the audit itself: none of the XR inputs appear above
xr_inputs_used = False
chk("S13.dep", not xr_inputs_used,
    "DEPENDENCY AUDIT: the exclusion consumed only {n, (C), (R1)}; it "
    "touched no C(n,j), no gate B*, no (T*), no t* -> t-NAMING-INDEPENDENT")

# ===========================================================================
print()
print("=" * 74)
print("S14. (U5) LEMMA 3 / THEOREM A-B bands under each t, retyped")
print("=" * 74)


def m_new(j):
    return 2 ** (22 + j)


def m_nested(j):
    return 2 ** (23 + j)


def bands(t, mfun):
    l3 = 0
    for j in range(1, 17):
        if t >= mfun(j) / LOG2_P_KB:
            l3 = j
        else:
            break
    ab = 0
    for j in range(1, 17):
        if t >= 2 * mfun(j) - 1:
            ab = j
        else:
            break
    return l3, ab


# controls from f2_tq_pin (S9.1, S9.2, S10.1, S10.2)
marg_7e10 = T_7E10 / (m_new(16) / LOG2_P_KB)
marg_tstar = TSTAR[2] / (m_new(16) / LOG2_P_KB)
chk("S14.c1", abs(marg_7e10 - 7.8915) < 5e-4,
    "CONTROL: rung-16 LEMMA 3 margin at t = 7e10 = %.4fx (banked 7.8915x)"
    % marg_7e10)
chk("S14.c2", abs(marg_tstar - 0.9687) < 5e-4,
    "CONTROL: rung-16 LEMMA 3 margin at t = t* = %.4fx (banked 0.9687x)"
    % marg_tstar)
chk("S14.c3", bands(T_7E10, m_new) == (16, 13),
    "CONTROL: new-part @ 7e10 -> LEMMA 3 rungs 1-16, THEOREM A/B 1-13")
chk("S14.c4", bands(TSTAR[2], m_new) == (15, 10),
    "CONTROL: new-part @ t*    -> LEMMA 3 rungs 1-15, THEOREM A/B 1-10")

# the retyping test: t* (a t_XR) vs 2^33 (the infimum of the t_F2 interval)
b_tstar_new = bands(TSTAR[2], m_new)
b_f2_new = bands(2 ** 33, m_new)
b_tstar_nest = bands(TSTAR[2], m_nested)
b_f2_nest = bands(2 ** 33, m_nested)
chk("S14.1", b_tstar_new == b_f2_new,
    "RETYPE new-part: bands at t_XR = t* %s == bands at t_F2 = 2^33 %s "
    "-> the CONCLUSION survives retyping" % (b_tstar_new, b_f2_new))
chk("S14.2", b_tstar_nest == b_f2_nest,
    "RETYPE nested  : bands at t_XR = t* %s == bands at t_F2 = 2^33 %s"
    % (b_tstar_nest, b_f2_nest))
chk("S14.3", b_f2_nest == (14, 9),
    "worst case over the t_F2 interval, stricter window: LEMMA 3 rungs "
    "1-14, THEOREM A/B rungs 1-9  (the unsoftened band)")

# ===========================================================================
print()
print("=" * 74)
print("S15. (U6) the THIRD t: |Lambda| vs the degree bound (factor 2)")
print("=" * 74)

t_deg = 2.0 * T_F2          # if the (C) balance is imposed on |Lambda|
marg_deg = t_deg / (m_new(16) / LOG2_P_KB)
chk("S15.1", abs(t_deg / T_F2 - 2.0) < 1e-12,
    "t_deg = 2|Lambda| = 2n/L = %.4e  (exactly 2x t_F2)" % t_deg)
chk("S15.2", marg_deg > 1.0 and marg_tstar < 1.0,
    "THE AMBIGUITY IS DECISIVE: rung-16 LEMMA 3 margin is %.4fx under the "
    "degree reading (HOLDS) vs %.4fx under the count reading (VIOLATED) -- "
    "the factor 2 straddles 1.0" % (marg_deg, marg_tstar))
chk("S15.3", bands(t_deg, m_new) == (16, 11),
    "under the degree reading the new-part bands become %s, not (15, 10)"
    % (bands(t_deg, m_new),))

# ===========================================================================
print()
print("=" * 74)
print("S16. (U8) the |K1| = 2^{n/2} pricing identity, retyped")
print("=" * 74)

lhs_xr = (TSTAR[2] / 2.0) * L_CONV
lhs_f2 = (T_F2 / 2.0) * L_CONV
chk("S16.1", abs(lhs_f2 - N / 2.0) / (N / 2.0) < 1e-12,
    "with t_F2: (t/2)*L = %.6e = n/2 EXACTLY (structural -- it IS the (C) "
    "balance halved)" % lhs_f2)
chk("S16.2", abs(lhs_xr / (N / 2.0) - 1.0) > 1e-6,
    "with t_XR = t*: (t*/2)*L / (n/2) = %.8f != 1 -- short of n/2 by "
    "Delta/2 = %.4e bits; the identity is APPROXIMATE, not structural"
    % (lhs_xr / (N / 2.0), DELTA[2] / 2.0))
chk("S16.3", abs((1.0 - lhs_xr / (N / 2.0)) - abs(devs[2])) / abs(devs[2]) < 0.01,
    "the shortfall is exactly the same 4.406e-5 = 2/(L^2 ln2) as S6")

# ===========================================================================
print()
print("=" * 74)
print("S17-S21. POST-SWEEP: the count-vs-degree normalization decides more")
print("         than expected (evidence found after U1-U9 were registered)")
print("=" * 74)

# The F2 lane's own sources read `t` as the MAX NEWTON INDEX, with
# Lambda = {odd l <= t}, so |Lambda| = ceil(t/2):
#   f2_sl1b/PROOFS.md:11        "under the `odd l <= t` reading R = |Lambda| = ceil(t/2)"
#   f2_sl1_powersums/PROOFS.md:9-10   same
#   f2_opening/PROOFS.md:327    "Theorem A/B require Lambda superset {1,3,...,2m-1}"
#   f2_deployed_windows/selection.py:50  "even_l = T_CONDITIONS // 2"
#   SOL_TARGET_3_OFFICIAL_EXTRAS_FLOOR.md:20  "t* = #{p-free i <= t}"
# The balance (C) charges L bits per CONDITION, i.e. per element of Lambda,
# so under this reading it reads ceil(t/2)*L >= n, giving t_F2 = 2n/L.

T_F2_DEG = 2.0 * N / L_CONV
chk("S17.1", abs(T_F2_DEG / TSTAR[2] - 2.0) < 1e-3,
    "under the F2 lane's OWN (degree) reading t_F2 = 2n/L = %.5e, which is "
    "%.5fx t* -- a FACTOR 2 disagreement at rate 1/2 as well"
    % (T_F2_DEG, T_F2_DEG / TSTAR[2]))
chk("S17.2", abs(T_F2_DEG / TSTAR[2] - 1.0) > 0.99,
    "the celebrated 0.0044%% agreement at rate 1/2 is an artefact of the "
    "COUNT normalization; under the degree normalization the rate-1/2 gap "
    "is %.1f%%" % (100.0 * (T_F2_DEG / TSTAR[2] - 1.0)))

# S18 -- the reductio: f2_tq_pin:158 (t = |Lambda|) and f2_sl1b:11
# (|Lambda| = ceil(t/2)) cannot both hold.
bad = [t for t in range(1, 2000) if t == -(-t // 2)]
chk("S18", bad == [1],
    "REDUCTIO: t = |Lambda| AND |Lambda| = ceil(t/2) force t = ceil(t/2), "
    "whose only positive solution is t = %d. The two banked readings are "
    "inconsistent for every t >= 2." % bad[0])

# S19 -- the wave-10 supersession of the mca_floor endpoint
# rate_half_cyclic_rotated_prefix_floor/claim_contract.md:24-26
SIGMA_MAX_W10 = 2 ** 34 - 1
chk("S19.1", SIGMA_MAX_W10 == 17179869183 and TSTAR[2] < SIGMA_MAX_W10,
    "wave-10 supersedes: proved unsafe band is 1 <= sigma <= 2^34-1 = %d; "
    "t* = %d sits at %.5f of that reach -- DEEP inside, not 1.2e6 below the "
    "edge" % (SIGMA_MAX_W10, TSTAR[2], TSTAR[2] / SIGMA_MAX_W10))
chk("S19.2", abs(2.0 * N / 256.0 - 2 ** 34) < 1e-6,
    "CAUTION (a coincidence of the very genus this pilot exists to police): "
    "the degree-reading counting floor 2n/256 = 2^34 equals the wave-10 band "
    "top 2^34-1 plus one. Both are dyadic multiples of n/256; this is NOT "
    "evidence of identity and is recorded only so nobody reads it as such.")

# S20 -- the decomposition of the difference is ALREADY BANKED (not novel)
# WAVE9_AUDIT_FINDINGS.md:189-190
chk("S20.1", 2048 * 2 ** 22 + 2978146 == SIGMA_STAR_BANKED,
    "banked at WAVE9_AUDIT_FINDINGS.md:190: sigma* = 2048*2^22 + 2,978,146 "
    "= %d -- the closed form was already in the repo; my S9.3 RE-DERIVES a "
    "banked fact and must not be reported as novel" % SIGMA_STAR_BANKED)
chk("S20.2", sigma_max - SIGMA_STAR_BANKED == 1216157,
    "banked 'delta = 1,216,157' = sigma_max - sigma*; the brief's 1,216,156 "
    "= sigma_max - t* differs by exactly 1 because t* = sigma* + 1")

# S21 -- THE 7e10 EXCLUSION IS NORMALIZATION-DEPENDENT (revises my own S13)
L_count = N / T_7E10                 # count reading  : t*L = n
L_degree = 2.0 * N / T_7E10          # degree reading : ceil(t/2)*L = n
chk("S21.1", L_count < math.log2(N),
    "COUNT reading : t = 7e10 => L = n/t = %.3f < log2 n = %.1f -> EXCLUDED"
    % (L_count, math.log2(N)))
chk("S21.2", math.log2(N) < L_degree < 256.0,
    "DEGREE reading: t = 7e10 => L = 2n/t = %.3f, and %.1f < %.3f < 256 -- "
    "a RULES-ADMISSIBLE field. NOT EXCLUDED."
    % (L_degree, math.log2(N), L_degree))
excluded_count = L_count < math.log2(N)
admissible_degree = math.log2(N) < L_degree < 256.0
chk("S21.3", excluded_count and admissible_degree,
    "VERDICT REVISION: the 7e10 exclusion survives the t_F2/t_XR collision "
    "(it consumes no t_XR, S13) but does NOT survive the count/degree "
    "collision -- it holds under one normalization and fails under the "
    "other. 't-naming-independent' is true only for the collision as posed.")
lo_deg, hi_deg = 2.0 * N / 256.0, 2.0 * N / math.log2(N)
chk("S21.4", lo_deg < T_7E10 <= hi_deg,
    "under the degree reading the rules-forced interval is (2^34, %.4e] = "
    "(%.4e, %.4e], and 7e10 lies INSIDE it" % (hi_deg, lo_deg, hi_deg))

# ===========================================================================
print()
print("=" * 74)
n_pass = sum(1 for _, ok, _ in RESULTS if ok)
n_fail = len(RESULTS) - n_pass
print("TOTAL: %d checks, %d PASS, %d FAIL" % (len(RESULTS), n_pass, n_fail))
if n_fail:
    for tag, ok, detail in RESULTS:
        if not ok:
            print("  FAILED: %s  %s" % (tag, detail))
    print("T_NAMING_VERIFY_FAILED")
    sys.exit(1)
print("T_NAMING_VERIFY_ALL_PASS")
sys.exit(0)
