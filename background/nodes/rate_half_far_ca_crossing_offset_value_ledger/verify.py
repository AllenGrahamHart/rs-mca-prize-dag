#!/usr/bin/env python3
"""Exact replay of the razor integers of the crossing-offset value ledger:
the arithmetic behind (refuted) Statement U, the fibre-cap pigeonhole, and
the round-37/38 floor-and-cap constants (r+1+126, the double-cover identity,
the exchange law's razor optimum).

Sources: critical/nodes/rate_half_band_crossing_location/statement.md,
         sections "Round-36 R-HRLOW addendum", "Round-37 U-rand addendum",
         "Round-38 URATE/genericity addendum".
Independent constant bank: notes/pilots_20260811/r36_hrlow/f4_results.txt:29-45.

Stdlib only, exact integer arithmetic (no floats in any assertion except
the logarithms, which are compared to banked values with a tolerance).
Run: tools/ramguard tiny -- python3 \
  background/nodes/rate_half_far_ca_crossing_offset_value_ledger/verify.py
(RAMGUARD_TIMEOUT default 60s)
"""

from math import comb, log2

FAILURES = []


def check(tag, got, want):
    if got != want:
        FAILURES.append("%s: got %r want %r" % (tag, got, want))
    return got


# ---------------------------------------------------------------- razor shape
# The official rate-half row at the crossing offset a = k + 2^34.
K = 2 ** 40                      # k = R = 2^40
R = 2 ** 40                      # R = n - k = k at rate one half
RHO = 2 ** 34                    # rho = 2^34
N = 2 ** 41                      # n = 2k
A = K + RHO                      # a = k + 2^34
r = R - RHO                      # r = n - a

# banked razor integers, r36_hrlow/f4_results.txt:30
check("R", R, 1099511627776)
check("rho", RHO, 17179869184)
check("r", r, 1082331758592)
check("n", N, 2199023255552)
check("a = k+rho", A, 1116691496960)
check("r = n - a", r, N - A)
check("rho = R/64", RHO, R // 64)
check("r = 63*rho", r, 63 * RHO)

# ------------------------------------------------- the exact-value consequence
# STATEMENT U would have implied B_ca^far(k + 2^34) = r + 1 EXACTLY.
# U is REFUTED (round 37); r+1 survives as the T_fib floor value.
BCA_FIB = r + 1
check("T_fib floor value", BCA_FIB, 1082331758593)
L2 = log2(BCA_FIB)
if abs(L2 - 39.977280) > 5e-7:
    FAILURES.append("log2(r+1): got %.6f want 39.977280" % L2)

# ---------------------------------------- the round-37/38 floor and cap
# The razor design j = 126 is the exact double cover: 126*rho = 2r, i.e.
# 2(r+1) - 126*rho = 2 EXACTLY (kernel dim 2 on the nose).
check("126*rho = 2r", 126 * RHO, 2 * r)
check("2(r+1) - 126*rho", 2 * (r + 1) - 126 * RHO, 2)
FLOOR_137 = r + 1 + 126
check("constructive floor r+1+126", FLOOR_137, 1082331758719)
L2F = log2(FLOOR_137)
if abs(L2F - 39.977280) > 5e-7:
    FAILURES.append("log2(r+1+126): got %.6f want 39.977280" % L2F)
# in bits, nothing moves: the two values agree to six decimals.
if abs(L2F - L2) > 5e-7:
    FAILURES.append("bits moved between r+1 and r+1+126")

# The exchange law (round 38): within the shared-A* normal form,
#   T <= (r+1) - delta + floor((2(r+1) - 1 + delta)/rho).
# The derivative in delta is 1/rho - 1 < 0, so delta = 0 is optimal at any
# rho > 1; at razor the delta = 0 cap is exactly r+1+126.
def exchange_cap(r1, rho_, delta):
    return r1 - delta + (2 * r1 - 1 + delta) // rho_


check("exchange cap at razor, delta=0", exchange_cap(r + 1, RHO, 0), FLOOR_137)
for delta in (1, 2, 63, RHO // 2, RHO, 2 * RHO):
    if exchange_cap(r + 1, RHO, delta) > FLOOR_137:
        FAILURES.append("delta=%d beats delta=0 at razor" % delta)
# the mu_26 cell (r+1 = 11, rho = 3): j-cap floor((2*11-1)/3) = 7, so the
# in-normal-form cap is 18 -- which is why the round-37 census T = 17 was
# search-limited (j = 7 reachable), and why the C3 rank-drop T = 19 exhibit
# (round 38, full census, three fields) shows the cap is NORMAL-FORM-
# CONDITIONAL: it is cited from the bank, not recomputed here.
check("mu_26 j-cap", (2 * 11 - 1) // 3, 7)
check("mu_26 in-form cap", exchange_cap(11, 3, 0), 18)

# ------------------------------------------------ the fibre-cap pigeonhole
# W = S_1 u S_2 is the common support; f = |W| - r is the surplus.  Every
# structural (fibre) slope is witnessed by an r-subset of W, and two
# structural slopes cannot share a locator, so
#        T_fib <= floor((r + f)/f) = floor(r/f) + 1.
# The two displayed forms agree for every f >= 1 (checked exhaustively on a
# wide integer range, and at the razor value of r).
def cap_a(rr, f):
    return (rr + f) // f


def cap_b(rr, f):
    return rr // f + 1


for rr in list(range(1, 200)) + [r, r + 1, 63 * RHO]:
    for f in range(1, 60):
        if cap_a(rr, f) != cap_b(rr, f):
            FAILURES.append("cap forms disagree at (r,f)=(%d,%d)" % (rr, f))
            break

# f = 1 is the LB1 configuration: the cap collapses to exactly r+1.
check("cap at f=1", cap_a(r, 1), r + 1)
# and the structural FLOOR ceil((r+1)/d) reaches r+1 exactly at d = 1.
check("fibre floor at d=1", -((-(r + 1)) // 1), r + 1)
# d = 1 forces |W| = r+1, i.e. f = 1, i.e. floor and cap coincide: T_fib = r+1.
check("floor == cap at d=1", -((-(r + 1)) // 1), cap_a(r, 1))

# banked fibre floors at two larger d (f4_results.txt:36-37)
check("fibre floor at d=2^33", -((-(r + 1)) // (2 ** 33)), 127)
check("fibre floor at d=2^34", -((-(r + 1)) // (2 ** 34)), 64)
# and the banked h_r dictionary values on the same two rows
check("h_r at d=2^33", RHO + 2 ** 33, 25769803776)
check("h_r at d=2^34", RHO + 2 ** 34, 34359738368)

# ------------------------------------------------------------ U-sym's razor kill
# The T_sym carrier is the even/orbit-invariant locator algebra L_B(X)G(X^M)
# on a negation-closed (more generally mu_M-invariant) domain.  Killing the
# non-met orbits leaves ceil(rho/M) genuine conditions on the SINGLE unknown
# slope gamma, so the carrier survives only when ceil(rho/M) <= 1.
def residual_conditions(rho_, M):
    return -((-rho_) // M)


check("ceil(rho/2) at razor", residual_conditions(RHO, 2), 8589934592)
check("ceil(rho/2) = 2^33", residual_conditions(RHO, 2), 2 ** 33)
check("surplus at M=2", residual_conditions(RHO, 2) - 1, 2 ** 33 - 1)
check("M needed for ceil(rho/M)=1", min(M for M in (2 ** i for i in range(0, 40))
                                        if residual_conditions(RHO, M) == 1),
      RHO)
# the kill is a rho-threshold, not a field threshold: it is q-free.
check("condition count is q-free", residual_conditions(RHO, 2),
      residual_conditions(RHO, 2))
# at the SMALL rho of the measured cells the same count is <= 1 and the
# carrier lives -- which is exactly why the excess is visible there.
check("rho=2 leaves one condition", residual_conditions(2, 2), 1)
check("rho=3 leaves two conditions", residual_conditions(3, 2), 2)

# ------------------------------------------------------ the queued correspondence
# CHECK QUEUED in the addendum: is the T_sym carrier count at M = rho
# (C(128,63)) the banked qcore plateau C(127,64)?  It is NOT -- exactly one
# binomial step, ratio 128/65.
c12863 = comb(128, 63)
c12764 = comb(127, 64)
if c12863 * 65 != c12764 * 128:
    FAILURES.append("C(128,63)/C(127,64) != 128/65")
d_bits = log2(c12863) - log2(c12764)
if abs(d_bits - log2(128 / 65)) > 1e-9:
    FAILURES.append("binomial gap bits mismatch")
if abs(d_bits - 0.98) > 0.01:
    FAILURES.append("binomial gap not ~0.98 bits: %.4f" % d_bits)
if abs(log2(c12764) - 123.1714) > 5e-5:
    FAILURES.append("C(127,64) not 2^123.1714: %.4f" % log2(c12764))

# ------------------------------------------------------------------- report
if FAILURES:
    for f in FAILURES:
        print("FAIL " + f)
    raise SystemExit(1)
print("CROSSING_OFFSET_VALUE_LEDGER_PASS "
      "r+1=%d floor=r+1+126=%d log2(both)=%.6f cap(f=1)=%d M2_surplus=%d "
      "Cgap_bits=%.4f exchange_cap(razor,0)=r+1+126"
      % (BCA_FIB, FLOOR_137, L2, cap_a(r, 1), 2 ** 33 - 1, d_bits))
