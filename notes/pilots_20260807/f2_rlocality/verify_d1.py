"""D1 -- THE DEFICIT MADE EXACT.  Round-22 f2_rlocality pilot, DRAFT ONLY."""

import math
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_lib as R

PASS = []
FAIL = []


def chk(tag, cond, msg):
    (PASS if cond else FAIL).append(tag)
    print(("PASS " if cond else "FAIL ") + tag + " :: " + msg)


L = R.L_OFF
cs = R.CSTAR

print("=" * 78)
print("D1.0  THE ROW OF RECORD")
print("=" * 78)
print("p        = %d" % R.P_OFF)
print("S        = 2^38 = %d      R = %d (banked)" % (R.S_OFF, R.R_OFF))
print("L        = log2 p = %.9f" % L)
print("R/S      = %.15f      1/L = %.15f" % (R.R_OFF / R.S_OFF, 1.0 / L))
print("c*       = 1/ln2 - 1 = %.10f" % cs)
chk("D1.0a", abs(R.R_OFF / R.S_OFF - 1.0 / L) < 1e-9,
    "saturation R/S = 1/log2 p holds to 1e-9 at the banked R")
chk("D1.0b", abs(L - 63.999999355) < 5e-9, "log2 p = 63.999999355 reproduced")

print()
print("=" * 78)
print("D1.1  THE 8.60 REPRODUCED, AND WHAT IT IS")
print("=" * 78)
eight = L / math.log2(math.e * L)
print("L / log2(e L)                  = %.6f" % eight)
print("log2(e L)                      = %.6f   (= log2 L + log2 e)" % math.log2(math.e * L))
print("   split: log2 L = %.6f  +  log2 e = %.6f" % (math.log2(L), R.LOG2E))
chk("D1.1a", abs(eight - 8.60) < 0.005,
    "P1 CONFIRMED: L/log2(eL) = %.4f reproduces the node's 8.60" % eight)

# Corollary 8's inequality, tern_route_b/PROOFS.md:409 :  log2(e log2 p) >= log2 p
c8_lhs = math.log2(math.e * L)
print("COROLLARY 8 inequality  log2(e log2 p) >= log2 p :  %.6f >= %.6f  -> %s"
      % (c8_lhs, L, c8_lhs >= L))
print("multiplicative failure margin of COROLLARY 8    = L/log2(eL) = %.6f" % (L / c8_lhs))
chk("D1.1b", abs(L / c8_lhs - eight) < 1e-12,
    "8.60 IS the multiplicative failure margin of COROLLARY 8's inequality")

# the instrument's own exponent, layer by layer
i1 = R.I_INSTR(1.0, L)
istar = R.I_INSTR(cs, L)
print()
print("I_INSTR(1)   = (1/L) log2(e L)          = %.6f   ( = the node's '0.116 S')" % i1)
print("I_INSTR(c*)  = (1/L) log2(e eta_c*^2 L) = %.6f" % istar)
print("eta_c*       = 2^c* - 1                 = %.6f" % R.eta_of_c(cs))
chk("D1.1c", abs(i1 - 0.116292) < 5e-5,
    "the node's 0.116 S is I_INSTR(1) = %.6f, NOT I_INSTR(c*)" % i1)
chk("D1.1d", abs(istar - 0.0701) < 5e-4,
    "P4 CONFIRMED: I_INSTR(c*) = %.6f (predicted 0.0701 +- 0.0005)" % istar)

print()
print("THE THREE NUMBERS THE NODE CONFLATES")
print("  (a) DEF_INSTR(1)   = 1 / I_INSTR(1)     = %.4f   <- the node's 8.60" % (1.0 / i1))
print("  (b) c* / I_INSTR(1)                     = %.4f   <- the ratio the node's own"
      % (cs / i1))
print("                                                       sentence computes (0.443/0.116)")
print("  (c) DEF_INSTR(c*)  = c* / I_INSTR(c*)   = %.4f   <- the deficit AT THE BINDING LAYER"
      % (cs / istar))
chk("D1.1e", abs(1.0 / i1 - eight) < 1e-9,
    "8.60 = DEF_INSTR(1) exactly: it is a c = 1 constant")
chk("D1.1f", abs(cs / i1 - 3.807) < 0.01,
    "the node's own two numbers have ratio %.4f, which is neither 8.60 nor (c)"
    % (cs / i1))
chk("D1.1g", abs(cs / istar - 6.32) < 0.03,
    "P3 CONFIRMED: DEF_INSTR(c*) = %.4f (predicted 6.32 +- 0.03)" % (cs / istar))

print()
print("=" * 78)
print("D1.2  THE FOUR-FACTOR DECOMPOSITION  DEF = THETA * AMGM * GAUSS * CAP")
print("=" * 78)
print("%-8s %10s %10s %10s %10s %12s %12s" %
      ("c", "THETA", "AMGM", "GAUSS", "CAP", "product", "DEF_INSTR"))
worst = None
for c in [0.15, 0.20, 0.25, 0.30, 0.35, 0.40, cs, 0.50, 0.60, 0.80, 0.95, 1.0]:
    th, am, ga, ca = R.THETA(c, L), R.AMGM(c, L), R.GAUSS(c, L), R.CAP(c, L)
    prod = th * am * ga * ca
    dd = R.DEF_INSTR(c, L)
    tag = " <- c*" if abs(c - cs) < 1e-9 else (" <- c=1" if c == 1.0 else "")
    print("%-8.4f %10.5f %10.5f %10.5f %10.5f %12.5f %12.5f%s"
          % (c, th, am, ga, ca, prod, dd, tag))
    if abs(prod - dd) > 0.02 * dd:
        worst = (c, prod, dd)
chk("D1.2a", worst is None,
    "the four-factor product reproduces DEF_INSTR at every tabulated layer "
    "to better than 2% (falsifier F2 not triggered)")

th1, am1, ga1, ca1 = R.THETA(1.0, L), R.AMGM(1.0, L), R.GAUSS(1.0, L), R.CAP(1.0, L)
print()
print("AT c = 1 (where 8.60 lives):")
print("  THETA(1) = c/I_FLAT(1) = 1/L          = %.6f   (the criterion's OWN slack at c=1)" % th1)
print("  AMGM(1)  = I_FLAT(1)/J_FLAT(1)        = %.6f   (AM-GM is LOSSLESS at c=1)" % am1)
print("  GAUSS(1) = J_FLAT(1)/(log2(e))        = %.6f   (moment-shape loss)" % ga1)
print("  CAP(1)   = log2(e) L / log2(e L)      = %.6f   (locality cap loss)" % ca1)
print("  product                               = %.6f" % (th1 * am1 * ga1 * ca1))
chk("D1.2b", abs(th1 * am1 * ga1 * ca1 - eight) < 0.005 * eight,
    "P5 CONFIRMED: 8.60 = (1/64) x 1.000 x %.2f x %.2f" % (ga1, ca1))
chk("D1.2c", abs(am1 - 1.0) < 1e-9,
    "AMGM(1) = 1 exactly: at c = 1 both events are {all c_s = 0}")
chk("D1.2d", abs(ga1 - 44.36) < 0.5 and abs(ca1 - 12.41) < 0.05,
    "P5's per-factor predictions GAUSS(1)=44.36+-0.5, CAP(1)=12.41+-0.05 hold")

ths, ams, gas, cas = R.THETA(cs, L), R.AMGM(cs, L), R.GAUSS(cs, L), R.CAP(cs, L)
print()
print("AT c = c* (the binding layer, ZERO flat margin):")
print("  THETA(c*) = c*/I_FLAT(c*)             = %.6f   (COROLLARY ZM: exactly 1)" % ths)
print("  AMGM(c*)                              = %.6f" % ams)
print("  GAUSS(c*)                             = %.6f" % gas)
print("  CAP(c*)                               = %.6f" % cas)
print("  product                               = %.6f   vs DEF_INSTR(c*) = %.6f"
      % (ths * ams * gas * cas, cs / istar))
chk("D1.2e", abs(ths - 1.0) < 1e-6,
    "THETA(c*) = 1.000000 -- COROLLARY ZM's zero margin, measured")
chk("D1.2f", abs(ams - 2.29) < 0.06 and abs(gas - 1.04) < 0.02 and abs(cas - 2.65) < 0.05,
    "P6 CONFIRMED: AMGM=%.3f GAUSS=%.3f CAP=%.3f at c*" % (ams, gas, cas))
fac = {"AMGM": ams, "GAUSS": gas, "CAP": cas}
loss = max(fac, key=fac.get)
print("  LOSSIEST SINGLE STEP AT c*: %s (factor %.4f)" % (loss, fac[loss]))
chk("D1.2g", loss == "CAP",
    "P7: the lossiest step at the binding layer is the LOCALITY CAP")

print()
print("=" * 78)
print("D1.3  THE INSTRUMENT DEFICIT ACROSS LAYERS")
print("=" * 78)
best, bc = 1e30, None
for i in range(11, 1000):
    c = i / 1000.0
    v = R.DEF_INSTR(c, L)
    if v < best:
        best, bc = v, c
print("min_c DEF_INSTR(c) = %.4f attained at c = %.3f" % (best, bc))
print("DEF_INSTR(c*)      = %.4f" % (cs / istar))
print("DEF_INSTR(1)       = %.4f" % (1.0 / i1))
chk("D1.3a", abs(best - 5.97) < 0.10 and abs(bc - 0.30) < 0.05,
    "P8 CONFIRMED: min_c DEF_INSTR = %.3f near c = %.2f (non-monotone)" % (best, bc))

print()
print("=" * 78)
print("D1.4  SANITY CONTROLS AGAINST THE BANK")
print("=" * 78)
# COROLLARY ZM: Lambda(1) = 0, Lambda'(1) = c*
chk("D1.4a", abs(R.Lambda_flat(1.0)) < 1e-12,
    "Lambda(1) = %.3e = 0 (tail_count THEOREM 7)" % R.Lambda_flat(1.0))
chk("D1.4b", abs(R.Lambda_flat_prime(1.0) - cs) < 1e-9,
    "Lambda'(1) = %.10f = 1/ln2 - 1 (COROLLARY ZM)" % R.Lambda_flat_prime(1.0))
chk("D1.4c", abs(R.I_FLAT(cs, L) - cs) < 1e-8,
    "I_FLAT(c*) = %.10f = c*: the flat model saturates the criterion" % R.I_FLAT(cs, L))
margins = [(c, R.I_FLAT(c, L) - c) for c in [0.0, 0.2, 0.3, 0.4, cs, 0.5, 0.6, 0.8]]
print("flat margin profile I_FLAT(c) - c :")
for c, m in margins:
    print("    c = %-8.4f margin = %.6f" % (c, m))
chk("D1.4d", all(m >= -1e-9 for _, m in margins) and abs(margins[4][1]) < 1e-8,
    "margin >= 0 everywhere, EXACTLY 0 at c* -- COROLLARY ZM reproduced")
# COROLLARY 8's threshold recovered
lo, hi = 1.0, 64.0
for _ in range(200):
    mid = 0.5 * (lo + hi)
    if math.log2(math.e * mid) >= mid:
        lo = mid
    else:
        hi = mid
print("COROLLARY 8 threshold: log2 p <= %.4f  i.e.  p <= %.3f" % (lo, 2.0 ** lo))
chk("D1.4e", abs(lo - 3.0529) < 0.001 and abs(2.0 ** lo - 8.30) < 0.01,
    "COROLLARY 8's log2 p <= 3.0529, p <= 8.30 reproduced independently")
vd = R.var_d_flat()
print("Var(d) under the flat model = %.6f" % vd)

print()
print("D1 SUMMARY: %d PASS, %d FAIL" % (len(PASS), len(FAIL)))
sys.exit(1 if FAIL else 0)
