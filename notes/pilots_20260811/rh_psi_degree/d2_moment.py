#!/usr/bin/env python3
"""D1/D2 -- the SECOND MOMENT of the X_gamma family, exactly.

Question the brief asks: "is there a second moment / product identity the
pencil forces?"

Two second-moment objects, both exact:

 (M2a) sum_{gamma supported} X_gamma^2 = sum_{x,y in W} d_xy,
       d_xy = #{gamma : x,y in S_gamma}.  The counting layer (C4) fixes the
       DIAGONAL (d_xx = d_x <= e, sum_x (m-d_x) = 1+O) but says NOTHING
       about the off-diagonal restricted to W x W.  We evaluate it at the
       globally regular value
          dbar = sum_gamma u(u-1) / (N(N-1)) = (rho+2)rho(rho-1)/(N(N-1))
       and compare against the Cauchy-Schwarz equality case
          CS = (sum_{type-2} X)^2 / T_2 .
       If regular == CS the second moment is exactly the zero-variance case
       and carries NO information about the maximum.

 (M2b) the DUAL pair count, which IS forced:
       sum_{x in W} d_x(d_x-1) = sum_{gamma != gamma'} |S_g ^ S_g' ^ W|
       LHS >= (a-(1+O)) m(m-1)          [saturation (C4)]
       RHS <= T(T-1)(2rho - a)          [banked (OV), w* = a]
       -> a contradiction (hence closure) when
          (a-1-O) m(m-1) > (rho+2)(rho+1)(2rho-a).
       This is a genuinely different instrument from (C2)/(FR); we compute
       exactly where it bites and whether it reaches the open band.
"""
from fractions import Fraction as F

out = []
P = out.append

P("=" * 78)
P("(M2a) the second moment at the globally regular pair degree")
P("=" * 78)
P("  dbar = (rho+2)rho(rho-1)/(N(N-1));  T_1 = 2, T_2 = rho, O = 0, def = 0")
P("  S2reg = a*m + a(a-1)*dbar - 2rho^2        (type-2 second moment)")
P("  CS    = (a*m - 2rho)^2 / rho              (Cauchy-Schwarz equality)")
P("")
P("        m            a     S2reg/CS float   reading")
for m in [4, 8, 64, 1024, 1 << 20, 1 << 37]:
    rho, N = 4 * m - 1, 16 * m
    dbar = F((rho + 2) * rho * (rho - 1), N * (N - 1))
    for a in [(20 * m - 2) // 3, 7 * m - 1]:
        S2 = F(a * m) + F(a * (a - 1)) * dbar - 2 * rho * rho
        CS = F((a * m - 2 * rho) ** 2, rho)
        r = S2 / CS
        if r == 1:
            rd = "regular == CS: variance exactly 0, max = mean"
        elif r > 1:
            rd = "regular > CS: variance %.4f*CS available" % float(r - 1)
        else:
            rd = ("regular < CS by %.4f: the TRUE W-pair degree is forced ABOVE"
                  " the global mean (a lower bound on the 2nd moment, i.e. a"
                  " lower bound on max -- the WRONG direction)" % float(1 - r))
        P("%9d %12d %13.7f   %s" % (m, a, float(r), rd))
P("")
P("  LIMIT: dbar -> m/4, S2reg -> a^2 m/4, CS -> a^2 m/4, ratio -> 1.")
P("  So at the regular pair degree the second moment sits EXACTLY on the")
P("  Cauchy-Schwarz equality case: variance 0, all X_gamma equal, max = mean.")
P("  At finite m the regular value sits BELOW CS, so the only thing the second")
P("  moment forces is that W-internal pair degrees EXCEED the global mean --")
P("  a LOWER bound on max, useless for an upper bound.")
P("  A second-moment instrument therefore has to beat the regular pair degree")
P("  by a positive amount before it says anything at all about the maximum.")
P("")
P("  And no moment bound can ever reach the target: max >= mean always, while")
P("  the target need_X = mean_X - (4m - def_in + o_g + o_h)/rho < mean_X.")
P("  Chebyshev/Cauchy-Schwarz give max <= mean + sqrt(V(T_2-1)) >= mean.")

P("")
P("=" * 78)
P("(M2b) the DUAL pair count: saturation vs the banked (OV) overlap bound")
P("=" * 78)
P("  closes when (a-1-O) m(m-1) > (rho+2)(rho+1)(2rho-a)")
P("  asymptotic threshold: a m^2 > 16m^2(8m-a)  <=>  a > 128m/17 = 7.5294 m")
P("")
P("        m   a_min(M2b closes)   a_min/m   band top 7m-1   reaches band?   2rho")
for m in [2, 3, 4, 8, 64, 1024, 1 << 20, 1 << 37]:
    rho = 4 * m - 1
    lo, hi = 4 * m + 2, 2 * rho
    amin = None
    # LHS increasing in a, RHS decreasing in a -> monotone predicate, bisect
    def ok(a):
        return (a - 1) * m * (m - 1) > (rho + 2) * (rho + 1) * (2 * rho - a)
    if ok(hi):
        a0, b0 = lo, hi
        if ok(lo):
            amin = lo
        else:
            while a0 < b0:
                mid = (a0 + b0) // 2
                if ok(mid):
                    b0 = mid
                else:
                    a0 = mid + 1
            amin = a0
    P("%9d %19s %9s %15d %15s %6d" %
      (m, str(amin), ("%.5f" % (amin / m)) if amin else "-", 7 * m - 1,
       "YES" if (amin is not None and amin <= 7 * m - 1) else "NO", 2 * rho))
P("")
P("  VERDICT (M2b): a real, independent instrument -- and it is SUBSUMED.")
P("  It caps a at 128m/17 = 7.5294m, weaker than the banked (NEWCAP)")
P("  a* <= 7m-1, so it never reaches the open band (16m/3, 7m-1].")

txt = "\n".join(out)
with open("notes/pilots_20260811/rh_psi_degree/d2_moment_results.txt", "w") as fh:
    fh.write(txt + "\n")
print(txt)
