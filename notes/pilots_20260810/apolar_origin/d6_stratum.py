"""D2 pricing: how much of the strict e=m endpoint the (AO1) bound closes,
and the uniqueness check that makes C1 legal on both official profiles.

Stdlib only.  Run under tools/ramguard.
"""


def say(s=""):
    print(str(s), flush=True)


def ao1(N, R, rho, e, a, O):
    if a <= rho or a >= R + 1:
        return None
    t1 = min(e + 1, a // (a - rho), (a * e + O) // rho)
    t2 = ((N - a) * e) // (R + 1 - a)
    return t1 + t2


say("=== uniqueness of the minimum-weight coset representative ===")
say("  needs 2*rho < d(K) = R+1 on the profile in question.")
m = 2 ** 37
say("  strict A=3 (budget 2^39): rho = 4m-1 = %d, R+1 = 8m+1 = %d, "
    "2rho = %d  ->  %s" % (4 * m - 1, 8 * m + 1, 2 * (4 * m - 1),
                           "UNIQUE" if 2 * (4 * m - 1) < 8 * m + 1 else "NOT"))
say("  half-dist A=1 (budget 2^39+1): rho = h = 4m = %d, R+1 = %d, "
    "2rho = %d  ->  %s" % (4 * m, 8 * m + 1, 8 * m,
                           "UNIQUE" if 8 * m < 8 * m + 1 else "NOT"))
say("  => C0/C1 are legal on BOTH residual profiles (by exactly 3 and 1).")
say()

say("=== forced lower bound on w* ===")
say("  an unsupported generic-rank slope has coset weight >= R+1-rho = 4m+2,")
say("  and coset weight <= w*, so w* >= 4m+2 whenever some slope is")
say("  unsupported (always, since T <= rho+2 < q).")
say("  and w* <= |S_i u S_j| <= 2rho = 8m-2 whenever T >= 2.")
say("  => w* lives in [4m+2, 8m-2], a window of width 4m-3.")
say()

say("=== the (AO1)-closed sub-stratum, priced ===")
say("   m     w* window      closed w* sub-window     closed fraction  a_max/m")
for mm in [2, 3, 4, 8, 16, 32, 64, 128, 1024, 2 ** 20]:
    Nn, Rr, rr, ee = 16 * mm, 8 * mm, 4 * mm - 1, mm
    lo, hi = 4 * mm + 2, 8 * mm - 2
    good = [a for a in range(lo, hi + 1)
            if (ao1(Nn, Rr, rr, ee, a, 0) or 10 ** 9) <= rr + 1]
    if good:
        say("  %-6d [%d, %d]%s[%d, %d]%s %-16.4f %.4f"
            % (mm, lo, hi, " " * max(1, 14 - len("[%d, %d]" % (lo, hi))),
               min(good), max(good),
               " " * max(1, 22 - len("[%d, %d]" % (min(good), max(good)))),
               len(good) / (hi - lo + 1), max(good) / mm))
    else:
        say("  %-6d [%d, %d]  EMPTY (no closure)" % (mm, lo, hi))
say("  m=1 control:")
mm = 1
lo, hi = 4 * mm + 2, 8 * mm - 2
good = [a for a in range(lo, max(hi, lo) + 1)
        if (ao1(16, 8, 3, 1, a, 0) or 10 ** 9) <= 4]
say("    m=1: w* window [%d, %d] (degenerate), closed set = %s ; the fence"
    " has w* = 6, closed? %s" % (lo, hi, good, 6 in good))
say()
say("  asymptotic: a_max/m -> 16/3 = %.4f, so the closed sub-stratum is"
    " w* in [4m+2, ~16m/3]," % (16 / 3))
say("  i.e. about (16/3-4)/(8-4) = %.4f of the admissible w* range."
    % ((16 / 3 - 4) / 4))
say("  The UNCLOSED stratum is large-w* (spread-out supports), which is")
say("  where the average pair sits: mean |S_i n S_j| ~ m-1 gives")
say("  mean |S_i u S_j| ~ 7m-1 > 16m/3.")
say("=== END part 6 ===")
