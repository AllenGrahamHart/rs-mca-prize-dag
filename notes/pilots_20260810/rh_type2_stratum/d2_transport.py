"""D2 -- structure transport into the non-minimum-weight type-2 stratum,
and the resulting SHARPENED cap.  Exact integer arithmetic only.

THE TRANSPORTED INGREDIENT (OV).  w* is the MINIMUM joint support of the
pair.  For any two DISTINCT supported slopes gamma, gamma', the pair
(v_gamma, v_gamma') is itself a representation of the syndrome pair (the two
slopes are distinct points of the pencil line, so they span the same 2-space
mod K; and joint support is GL_2-invariant).  Hence

    w* <= |S_gamma u S_gamma'|   FOR EVERY PAIR,          (OV)
    i.e.  |S_gamma ^ S_gamma'| <= (rho-o_gamma)+(rho-o_gamma') - w*.

apolar_origin/REPORT.md:57 banks "w* <= |S_i u S_j| <= 2rho"; the load-bearing
step here is the EVERY-PAIR quantifier plus the second-moment pairing below.

THE SECOND MOMENT.  Double-counting root-slope incidences,
    sum_{gamma<gamma'} |S_gamma ^ S_gamma'| = sum_x C(d_x,2),
and under (SAT3)/(SAT4) the deficit sum_x (m-d_x) = 1+O <= m, d_x <= m, so by
convexity
    sum_x C(d_x,2) >= (N-1-O)*C(m,2) + (1+O)*C(m-1,2) =: Lmin(O).
Combining with (OV) summed over all C(T,2) pairs gives the W-INDEPENDENT cap

    w* <= 2rho - ( Lmin(O) + (T-1)*O ) / C(T,2).            (NEWCAP)

apolar_origin/REPORT.md:63 computes exactly this quantity ("sum_x C(d_x,2)
forces mean |S_i n S_j| ~ m-1, i.e. mean |S_i u S_j| ~ 7m-1") but reads it as
the LOCATION of the average configuration; (OV) turns the same number into an
upper bound on w*, because w* <= min <= mean.
"""

import sys

OUT = []


def say(s=""):
    OUT.append(s)


def C2(n):
    return n * (n - 1) // 2


def prof(m):
    return dict(m=m, rho=4 * m - 1, N=16 * m, R=8 * m, R1=8 * m + 1, e=m,
                delta=m - 1, T=4 * m + 1)


def CAP(m, a):
    P = prof(m)
    s = P["R1"] - a
    return None if s <= 0 else (P["N"] - a) * P["e"] // s


def T1cap(m, a, O=0):
    P = prof(m)
    if a - P["rho"] <= 0:
        return None
    return min(P["e"] + 1, a // (a - P["rho"]), (a * P["e"] + O) // P["rho"])


def Lmin(m, O):
    P = prof(m)
    return (P["N"] - 1 - O) * C2(m) + (1 + O) * C2(m - 1)


def newcap_a(m):
    """largest a admitting some O in [0,delta] -- the bound is monotone in O."""
    P = prof(m)
    T, rho = P["T"], P["rho"]
    best, bestO = None, None
    for O in (0, 1, P["delta"]):
        if O < 0 or O > P["delta"]:
            continue
        num = Lmin(m, O) + (T - 1) * O
        den = C2(T)
        # a <= 2rho - num/den   ->   a <= floor((2rho*den - num)/den)
        a = (2 * rho * den - num) // den
        if best is None or a > best:
            best, bestO = a, O
    return best, bestO


say("=" * 74)
say("D2.1  the O-monotonicity of (NEWCAP)  (justifies evaluating at O=0)")
say("=" * 74)
say("  d/dO of [Lmin(O) + (T-1)O] = (T-1) - (C(m,2)-C(m-1,2)) = 4m - (m-1)")
say("                             = 3m+1 > 0, so the cap is tightest at O=0.")
for mm in (2, 4, 8, 64):
    P = prof(mm)
    say("     m=%-4d  T-1=%-6d  C(m,2)-C(m-1,2)=%-6d  slope=%d"
        % (mm, P["T"] - 1, C2(mm) - C2(mm - 1), (P["T"] - 1) - (C2(mm) - C2(mm - 1))))
say()

say("=" * 74)
say("D2.2  THE SHARPENED w* CEILING AND THE SHARPENED TYPE-2 CAP")
say("=" * 74)
say("  %-14s %-10s %-12s %-12s %-24s %-14s"
    % ("m", "old a_max", "NEW a_max", "T4 band lo", "CAP(m,NEW a_max)", "rho+1"))
rows = []
for mm in (1, 2, 3, 4, 8, 64, 2 ** 10, 2 ** 20, 2 ** 37):
    P = prof(mm)
    old = 8 * mm - 2
    new, O = newcap_a(mm)
    new = min(new, old)
    band = (16 * mm + 3 + 2) // 3
    cnew = CAP(mm, new)
    say("  %-14d %-10d %-12d %-12d %-24d %-14d"
        % (mm, old, new, band, cnew, P["rho"] + 1))
    rows.append((mm, old, new, band, cnew, P["rho"] + 1, CAP(mm, old)))
say()
say("  the same table as a REDUCTION of the mandate's 5.04e22:")
say("  %-14s %-26s %-22s %-12s" % ("m", "old CAP(m,8m-2)", "new CAP(m,a_max)", "shrink x"))
for (mm, old, new, band, cnew, budget, cold) in rows:
    say("  %-14d %-26d %-22d %-12d" % (mm, cold, cnew, cold // max(1, cnew)))
say()
say("  residual factor still open (new cap vs budget rho+1):")
for (mm, old, new, band, cnew, budget, cold) in rows:
    t1 = T1cap(mm, new) or 0
    say("     m=%-14d  AO1(new) = %d + %d = %-22d  rho+1 = %-14d  ratio %d.%02d"
        % (mm, t1, cnew, t1 + cnew, budget,
           (t1 + cnew) // budget, ((t1 + cnew) * 100 // budget) % 100))
say()
say("  asymptotics: a_max -> 7m (leading order), s = R+1-a -> m, so")
say("  CAP -> 9m and AO1 -> 9m+2 against rho+1 = 4m: residual factor 9/4 = 2.25.")
for mm in (2 ** 10, 2 ** 20, 2 ** 37):
    new, _ = newcap_a(mm)
    say("     m=%-16d a_max = %-16d = 7m - %-10d  s = %-16d = m + %d"
        % (mm, new, 7 * mm - new, 8 * mm + 1 - new, (8 * mm + 1 - new) - mm))
say()

say("=" * 74)
say("D2.3  THE OFFICIAL NUMBER")
say("=" * 74)
mm = 2 ** 37
P = prof(mm)
old = 8 * mm - 2
new, O = newcap_a(mm)
cold, cnew = CAP(mm, old), CAP(mm, new)
t1 = T1cap(mm, new)
say("  m = 2^37, rho+1 = 2^39 = %d" % (P["rho"] + 1))
say("  banked cap  CAP(m, 8m-2)   = %d   (%d decimal digits)"
    % (cold, len(str(cold))))
say("  sharpened   a_max          = %d   (= 7m - %d)" % (new, 7 * mm - new))
say("  sharpened   CAP(m, a_max)  = %d   (%d decimal digits)"
    % (cnew, len(str(cnew))))
say("  sharpened   AO1(m, a_max)  = %d + %d = %d" % (t1, cnew, t1 + cnew))
say("  shrink factor              = %d  (%d decimal orders of the %d-order gap)"
    % (cold // cnew, len(str(cold // cnew)) - 1,
       len(str(cold)) - len(str(P["rho"] + 1))))
say("  STILL OPEN by the factor    = %d / %d = 2.25..."
    % (t1 + cnew, P["rho"] + 1))
say()

say("=" * 74)
say("D2.4  SELF-CORRECTION: the D1.6 feasibility certificate was INCOMPLETE")
say("=" * 74)
say("  d1_anatomy.py D1.6 exhibited an integer-feasible pseudo-configuration")
say("  at a = 8m-2 for every m.  That certificate omitted (OV).  Re-test it:")
say("  in it |S_gamma ^ W| = rho - p_gamma, and W = S_1 u S_2 with S_1,S_2")
say("  disjoint of size rho, so max(|S_gamma^S_1|,|S_gamma^S_2|) >= ceil((rho-p)/2)")
say("  and then |S_gamma u S_1| <= 2rho - ceil((rho-p)/2) < a whenever p < rho.")
say("  %-14s %-10s %-14s %-16s %-10s"
    % ("m", "p_gamma", "|S^W|=rho-p", "min pair union", "a = 8m-2"))
for mm in (1, 2, 3, 4, 8, 2 ** 20):
    P = prof(mm)
    rho, N, e = P["rho"], P["N"], P["e"]
    aa = 8 * mm - 2
    T2 = P["T"] - 2
    total_out = (N - aa) * e - 1
    p = total_out // T2
    inW = rho - p
    half = (inW + 1) // 2
    say("  %-14d %-10d %-14d %-16d %-10d %s"
        % (mm, p, inW, 2 * rho - half, aa,
           "OK" if 2 * rho - half >= aa else "VIOLATES (OV): w* < a"))
say()
say("  So a = 8m-2 is NOT realizable for m >= 2, and the 5.04e22 is evaluated")
say("  at a VACUOUS point of the window.  At m=1 the certificate survives")
say("  (p = rho = 3, |S ^ W| = 0, all supports disjoint) -- and it is exactly")
say("  the banked q=17 fence.  Disjointness needs T*rho <= N, i.e.")
for mm in (1, 2, 3, 4):
    P = prof(mm)
    say("     m=%-3d  T*rho = %-8d  N = %-8d  %s"
        % (mm, P["T"] * P["rho"], P["N"],
           "feasible" if P["T"] * P["rho"] <= P["N"] else "IMPOSSIBLE"))
say("  (this is apolar_origin/REPORT.md:78 R4 -- ported, not discovered;")
say("   what is new is that a = 2rho FORCES the disjointness it refutes.)")
say()

say("=" * 74)
say("D2.5  RE-RUN OF THE COUNTING CERTIFICATE WITH (OV) ADDED")
say("=" * 74)
say("  Same construction, now at a = NEW a_max, with all pairwise overlaps")
say("  set to the (OV) ceiling 2rho-a and the second moment forced to Lmin(0).")
say("  %-14s %-14s %-20s %-20s %-8s"
    % ("m", "a", "C(T,2)*(2rho-a)", "Lmin(0)", "feasible"))
for mm in (1, 2, 3, 4, 8, 64, 2 ** 20, 2 ** 37):
    P = prof(mm)
    new, _ = newcap_a(mm)
    new = min(new, 8 * mm - 2)
    lhs = C2(P["T"]) * (2 * P["rho"] - new)
    rhs = Lmin(mm, 0)
    say("  %-14d %-14d %-20d %-20d %-8s"
        % (mm, new, lhs, rhs, lhs >= rhs))
say()
say("  and one integer BELOW-the-ceiling check (a = a_max+1 must fail):")
for mm in (2, 3, 4, 8, 64, 2 ** 20):
    P = prof(mm)
    new, _ = newcap_a(mm)
    aa = min(new, 8 * mm - 2) + 1
    lhs = C2(P["T"]) * (2 * P["rho"] - aa)
    rhs = Lmin(mm, 0)
    say("     m=%-10d a=%-14d C(T,2)(2rho-a)=%-20d Lmin=%-20d %s"
        % (mm, aa, lhs, rhs, "INFEASIBLE (correct)" if lhs < rhs else "still feasible"))
say()

say("=" * 74)
say("D2.6  WHAT (OV)+second moment DOES NOT SUPPLY (the named residual)")
say("=" * 74)
say("  The type-2 count is T_2 <= (N-a)e / (R+1-a).  To reach rho+1 the")
say("  per-slope spend floor must be p* ~ 2m+2 (d1_anatomy D1.4).  (OV)")
say("  raises the floor from R+1-a = 3 to R+1-a_max ~ m+2 -- a factor ~ (m+2)/3")
say("  -- but 2m+2 needs ANOTHER factor of ~2.  Exactly:")
for mm in (2 ** 10, 2 ** 20, 2 ** 37):
    P = prof(mm)
    new, _ = newcap_a(mm)
    floor_now = P["R1"] - new
    need = P["rho"] + 1 - (T1cap(mm, new) or 0)
    pstar = ((P["N"] - new) * P["e"] + need) // (need + 1)
    while (P["N"] - new) * P["e"] // pstar > need:
        pstar += 1
    say("     m=%-16d floor now = %-16d needed = %-16d shortfall x %d.%02d"
        % (mm, floor_now, pstar, pstar // floor_now,
           (pstar * 100 // floor_now) % 100))
say()
say("  THE MISSING INGREDIENT, named: a lower bound |S_gamma \\ W| >= ~2m for")
say("  NON-minimum-weight type-2 slopes, i.e. |S_gamma ^ W| <= ~2m.  Equivalently")
say("  a bound on how much of a type-2 locator can sit inside the MINIMUM joint")
say("  support.  (OV) gives it pairwise against a single other locator; what is")
say("  missing is the same statement against the whole of W at once.")
say()
say("=== END d2_transport ===")

sys.stdout.write("\n".join(OUT) + "\n")
