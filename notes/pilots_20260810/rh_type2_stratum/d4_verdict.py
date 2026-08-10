"""D4 -- verdict arithmetic: the residual w* window before/after (NEWCAP),
the pre-registered looseness fit, and the final ledger."""

import math
import sys

OUT = []


def say(s=""):
    OUT.append(s)


def C2(n):
    return n * (n - 1) // 2


def prof(m):
    return dict(rho=4 * m - 1, N=16 * m, R1=8 * m + 1, e=m, delta=m - 1,
                T=4 * m + 1)


def CAP(m, a):
    P = prof(m)
    s = P["R1"] - a
    return None if s <= 0 else (P["N"] - a) * P["e"] // s


def Lmin(m, O):
    P = prof(m)
    return (P["N"] - 1 - O) * C2(m) + (1 + O) * C2(m - 1)


def newcap_a(m):
    P = prof(m)
    den = C2(P["T"])
    return min(8 * m - 2, (2 * P["rho"] * den - Lmin(m, 0)) // den)


say("=" * 74)
say("D4.1  the residual (ii) w* window, before and after (NEWCAP)")
say("=" * 74)
say("  window = [4m+2, w*_max];  T4 closes weight-extremal type-2 for")
say("  w* >= ceil((16m+3)/3);  residual (ii) = non-min-weight type-2 on")
say("  [ceil((16m+3)/3), w*_max].")
say("  %-14s %-10s %-12s %-12s %-14s %-14s"
    % ("m", "T4 lo", "old top", "new top", "old share", "new share"))
for m in (2, 4, 8, 64, 2 ** 10, 2 ** 20, 2 ** 37):
    lo, old = 4 * m + 2, 8 * m - 2
    band = (16 * m + 3 + 2) // 3
    new = newcap_a(m)
    tot = old - lo + 1
    so = max(0, old - band + 1)
    sn = max(0, new - band + 1)
    say("  %-14d %-10d %-12d %-12d %-14s %-14s"
        % (m, band, old, new,
           "%d/%d=%.4f" % (so, tot, so / tot),
           "%d/%d=%.4f" % (sn, tot, sn / tot)))
say("  asymptotic shares: old 2/3 = 0.6667  ->  new 5/12 = 0.4167")
say()

say("=" * 74)
say("D4.2  PRE-REGISTERED looseness fit L(m) = CAP(m,8m-2)/max(1,TRUE(m))")
say("=" * 74)
say("  TRUE(m) = max T_2^{>} measured in ONE pencil (d3_census, both fields).")
meas = {1: 0, 2: 1, 3: 1, 4: 1}
xs, ys = [], []
say("  %-6s %-14s %-12s %-12s" % ("m", "CAP(m,8m-2)", "TRUE(m)", "L(m)"))
for m in (1, 2, 3, 4):
    c = CAP(m, 8 * m - 2)
    L = c / max(1, meas[m])
    say("  %-6d %-14d %-12d %-12.1f" % (m, c, meas[m], L))
    if m >= 2:
        xs.append(math.log(m))
        ys.append(math.log(L))
mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
sxx = sum((x - mx) ** 2 for x in xs)
p = sxy / sxx
say("  least-squares exponent over m in {2,3,4}: p = %.3f" % p)
say("  registered window P10: p in [1.0, 2.0], most likely [1.6, 2.0]")
say("  -> %s" % ("HIT (and in the narrow sub-window)" if 1.6 <= p <= 2.0 else "check"))
say("  NOTE (registered in advance, R6.2/R6.4): TRUE(m) is a MAX over a")
say("  SAMPLE of pencils, all of which have T = 3; it is a LOWER bound on the")
say("  true max and the fit has ZERO POWER as an extrapolation to m = 2^37.")
say("  The non-circular official-scale statement is the DERIVED shrink in D4.3.")
say()

say("=" * 74)
say("D4.3  FINAL LEDGER AT THE OFFICIAL PARAMETERS  (m = 2^37)")
say("=" * 74)
m = 2 ** 37
P = prof(m)
old, new = 8 * m - 2, newcap_a(m)
cold, cnew = CAP(m, old), CAP(m, new)
t1 = min(P["e"] + 1, new // (new - P["rho"]), (new * P["e"]) // P["rho"])
say("  budget rho+1                       = %d = 2^39" % (P["rho"] + 1))
say("  budget rho+2                       = %d = 2^39+1" % (P["rho"] + 2))
say("  banked residual-(ii) cap           = %d" % cold)
say("     = CAP(m, 8m-2) = 2^38(2^39+1)/3, exact, no floor loss")
say("  SHARPENED residual-(ii) cap        = %d" % cnew)
say("     = CAP(m, 7m-1),  a_max = 7m-1 = %d" % new)
say("  sharpened total AO1(m, a_max)      = %d + %d = %d" % (t1, cnew, t1 + cnew))
say("  shrink                             = %d x  (%.2f decimal orders)"
    % (cold // cnew, math.log10(cold / cnew)))
say("  remaining gap to rho+1             = %.4f x" % ((t1 + cnew) / (P["rho"] + 1)))
say("  gap that WAS there                 = %.4e x" % (cold / (P["rho"] + 1)))
say()
say("  what is closed : nothing (neither budget moves) -- see D4.4")
say("  what is shrunk : residual (ii)'s cap, by 10.6 decimal orders,")
say("                   and its w* window, from 2/3 to 5/12 of the range")
say("  what is named  : the exact missing inequality")
say("                   |S_gamma \\ W| >= ~2m for non-min-weight type-2,")
say("                   against the ~m+2 that (OV) now supplies -- a")
say("                   residual factor of exactly 9/4.")
say()

say("=" * 74)
say("D4.4  FALSIFIERS for (OV)+(NEWCAP)")
say("=" * 74)
say("  F1. A realizable strict-A=3 configuration with T = rho+2 and")
say("      w* > 2rho - Lmin(0)/C(T,2) (i.e. w* > 7m-1 at large m).")
say("  F2. Two distinct supported slopes gamma != gamma' with")
say("      |S_gamma u S_gamma'| < w*  (would break the GL_2-invariance of")
say("      joint support, or the claim that (v_gamma, v_gamma') represents")
say("      the same syndrome pair up to basis change).")
say("  F3. sum_{gamma<gamma'} |S_gamma ^ S_gamma'| != sum_x C(d_x,2) in any")
say("      measured configuration.")
say("  F4. A configuration with sum_x (m-d_x) = 1+O but")
say("      sum_x C(d_x,2) < (N-1-O)C(m,2) + (1+O)C(m-1,2).")
say("  F1 is the live one; F2-F4 are identity checks and were exercised in")
say("  d3_census (0 violations of the incidence identity in every cell).")
say()
say("=== END d4_verdict ===")

sys.stdout.write("\n".join(OUT) + "\n")
