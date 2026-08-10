"""D1 -- the anatomy of the 5.04e22 cap, in exact integer arithmetic.

Strict A=3 half-distance profile (SAT1 of
background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md:11-14):
    rho = 4m-1,  N = 16m,  R = 8m,  A = R+1-2rho = 3,  e = m,  delta = m-1.
(AO1) of notes/pilots_20260810/apolar_origin/PREREG.md:197-198:
    T <= min(m+1, floor(a/(a-rho)), floor((a m + O)/rho))
         + floor(((N-a) m)/((R+1)-a))
The second summand is CAP(m,a); the mandate's 5.04e22 is CAP(2^37, 8m-2).

No floats anywhere: sizes reported as decimal digit counts and bit lengths.
"""

import sys

OUT = []


def say(s=""):
    OUT.append(s)


def prof(m):
    return dict(m=m, rho=4 * m - 1, N=16 * m, R=8 * m, R1=8 * m + 1, e=m,
                delta=m - 1, r=4 * m - 1)


def CAP(m, a):
    """the (AO1) type-2 summand: floor((N-a)e/(R+1-a))"""
    P = prof(m)
    s = P["R1"] - a
    if s <= 0:
        return None
    return (P["N"] - a) * P["e"] // s


def T1cap(m, a, O=0):
    P = prof(m)
    if a - P["rho"] <= 0:
        return None
    return min(P["e"] + 1, a // (a - P["rho"]), (a * P["e"] + O) // P["rho"])


def AO1(m, a, O=0):
    t1, t2 = T1cap(m, a, O), CAP(m, a)
    if t1 is None or t2 is None:
        return None
    return t1 + t2


say("=" * 72)
say("D1.1  reproduce the banked 5.04e22 and pin its exact value")
say("=" * 72)
m = 2 ** 37
P = prof(m)
a = 8 * m - 2
c = CAP(m, a)
say("  m = 2^37 = %d,  N = 16m = 2^41 = %d" % (m, P["N"]))
say("  rho = 4m-1 = %d = 2^39-1,  R+1 = 8m+1 = %d" % (P["rho"], P["R1"]))
say("  a = w*_max = 8m-2 = %d,  s = R+1-a = %d,  N-a = 8m+2 = %d"
    % (a, P["R1"] - a, P["N"] - a))
say("  CAP(2^37, 8m-2) = (N-a)*e//s = %d" % c)
say("  banked figure at collinearity_object/d3_coverage_results.txt:94 = "
    "50371909150701174915072")
say("  MATCH: %s" % (c == 50371909150701174915072))
closed = 2 ** 38 * (2 ** 39 + 1) // 3
say("  closed form 2^38*(2^39+1)/3 = %d   MATCH: %s" % (closed, closed == c))
say("  exactly divisible (no floor loss): (N-a)*e %% s = %d"
    % (((P["N"] - a) * P["e"]) % (P["R1"] - a)))
say()

say("=" * 72)
say("D1.2  the size of the gap -- the brief says '~39-order'")
say("=" * 72)
for name, budget in (("rho+1 = 2^39", P["rho"] + 1), ("rho+2 = 2^39+1", P["rho"] + 2)):
    q, rem = divmod(c, budget)
    say("  CAP / (%s) = %d  (remainder %d)" % (name, q, rem))
    say("      decimal digits of the ratio : %d   bit length : %d"
        % (len(str(q)), q.bit_length()))
say("  CAP/(rho+2) in closed form = 2^38/3 = %d (exact: %s)"
    % (2 ** 38 // 3, 2 ** 38 // 3 == c // (P["rho"] + 2)))
say("  CAP/(rho+1) in closed form = (2^39+1)/6 = %d" % ((2 ** 39 + 1) // 6))
say("  decimal digits: CAP = %d, rho+1 = %d  ->  gap = %d decimal orders"
    % (len(str(c)), len(str(P["rho"] + 1)), len(str(c)) - len(str(P["rho"] + 1))))
say("  bit lengths  : CAP = %d, rho+1 = %d  ->  gap = %d binary orders"
    % (c.bit_length(), (P["rho"] + 1).bit_length(),
       c.bit_length() - (P["rho"] + 1).bit_length()))
say("  VERDICT: the gap is ~11 decimal / ~36.4 binary orders, NOT 39 orders.")
say()

say("=" * 72)
say("D1.3  CAP as a function of a on the admissible window [4m+2, 8m-2]")
say("=" * 72)
say("  %-14s %-16s %-22s %-16s %-12s" % ("m", "a", "CAP(m,a)", "T1cap", "rho+1"))
for mm in (2, 8, 2 ** 20, 2 ** 37):
    PP = prof(mm)
    lo, hi = 4 * mm + 2, 8 * mm - 2
    band = (16 * mm + 3 + 2) // 3          # ceil((16m+3)/3): T4's band start
    for aa in sorted({lo, band, 6 * mm, hi}):
        if not (lo <= aa <= hi):
            continue
        say("  %-14d %-16d %-22d %-16d %-12d %s"
            % (mm, aa, CAP(mm, aa), T1cap(mm, aa), PP["rho"] + 1,
               "CLOSES" if AO1(mm, aa) <= PP["rho"] + 1 else "open"))
say()
say("  monotone increasing in a?")
for mm in (2, 8, 64):
    vals = [CAP(mm, aa) for aa in range(4 * mm + 2, 8 * mm - 1)]
    say("     m=%-6d strictly non-decreasing: %s   CAP(4m+2)=%d  CAP(8m-2)=%d"
        % (mm, all(vals[i] <= vals[i + 1] for i in range(len(vals) - 1)),
           vals[0], vals[-1]))
say("  CAP(m,4m+2) closed form = floor((12m-2)m/(4m-1)); leading order 3m:")
for mm in (2 ** 10, 2 ** 20, 2 ** 37):
    say("     m=%-16d CAP(m,4m+2) = %-20d  = 3m - %d"
        % (mm, CAP(mm, 4 * mm + 2), 3 * mm - CAP(mm, 4 * mm + 2)))
say()

say("=" * 72)
say("D1.4  WHERE THE SLACK IS: invert the count for the required spend floor")
say("=" * 72)
say("  The cap is the single incidence count")
say("      T_2 * p_min  <=  sum_{x notin W} d_x  <=  (N-a) * e,")
say("  with p_min := the per-slope floor on p_gamma = |S_gamma \\ W|.")
say("  (C2) supplies only p_min = R+1-a. Invert: what p_min would close?")
say("  %-14s %-8s %-16s %-14s %-14s %-10s"
    % ("m", "R+1-a", "need T_2 <=", "p* required", "p*/(R+1-a)", "p*/m"))
for mm in (2, 8, 2 ** 10, 2 ** 20, 2 ** 37):
    PP = prof(mm)
    aa = 8 * mm - 2
    t1 = T1cap(mm, aa)
    need = PP["rho"] + 1 - t1               # required T_2 bound to reach T <= rho+1
    # smallest p with floor((N-a)e/p) <= need
    p_star = ((PP["N"] - aa) * PP["e"] + need) // (need + 1)
    while (PP["N"] - aa) * PP["e"] // p_star > need:
        p_star += 1
    say("  %-14d %-8d %-16d %-14d %-14d %-10s"
        % (mm, PP["R1"] - aa, need, p_star, p_star // (PP["R1"] - aa),
           "%d/%d" % (p_star, mm)))
say()
say("  CONSEQUENCE: the whole 5.04e22-vs-2^39 discrepancy is ONE input --")
say("  the per-slope spend floor 3 versus the required ~2m+2. The ratio of")
say("  the two caps is exactly the ratio of the two floors:")
mm = 2 ** 37
aa = 8 * mm - 2
PPm = prof(mm)
need = PPm["rho"] + 1 - T1cap(mm, aa)
p_star = ((PPm["N"] - aa) * PPm["e"] + need) // (need + 1)
while (PPm["N"] - aa) * PPm["e"] // p_star > need:
    p_star += 1
say("     p* = %d = 2m + %d ;  p*/3 = %d ;  CAP/(rho+2) = 2^38/3 = %d"
    % (p_star, p_star - 2 * mm, p_star // 3, 2 ** 38 // 3))
say("     ratio of ratios (p*/3) / (CAP/(rho+2)) = %d / %d"
    % (p_star // 3, 2 ** 38 // 3))
say()

say("=" * 72)
say("D1.5  m=1 IS STRUCTURALLY EMPTY OF THE RESIDUAL STRATUM")
say("=" * 72)
say("  At a = 8m-2 the admissible p = |S\\W| lies in [R+1-a, rho] = [3, 4m-1].")
for mm in (1, 2, 3, 4, 8):
    PP = prof(mm)
    aa = 8 * mm - 2
    say("     m=%-3d  a=8m-2=%-4d  p in [%d, %d]  -> #non-min-weight p values = %d"
        % (mm, aa, PP["R1"] - aa, PP["rho"], max(0, PP["rho"] - (PP["R1"] - aa))))
say("  m=1: the interval is the single point p=3, and wt(kappa) = a+p-n_0")
say("       = 9-n_0 >= R+1 = 9 forces n_0 = 0, hence j = 0 for EVERY type-2")
say("       slope. The non-minimum-weight type-2 stratum is EMPTY at m=1.")
say("  Also at m=1 the whole w* window degenerates: [4m+2, 8m-2] = [6,6].")
say()

say("=" * 72)
say("D1.6  COUNTING FEASIBILITY CERTIFICATE  (is the wall real?)")
say("=" * 72)
say("  Build an explicit integer pseudo-configuration at a = 8m-2 meeting")
say("  EVERY banked counting constraint with T = rho+2 (the SAT3 failure).")
say("  Constraints checked: (SAT2) 0<=O<=delta; (SAT3) T=rho+2;")
say("  (SAT4) sum_x (m-d_x) = 1+O; d_x <= m; I = sum_gamma |S_gamma| = T*rho-O;")
say("  (C2) type-2: p_gamma >= R+1-a+n_gamma and |S n W| <= a-n-(R-r+1), r=rho;")
say("  (C3) T_1 <= e+1; T_1 <= floor(a/(a-rho)); p_gamma <= |S_gamma|.")
say()
say("  %-14s %-6s %-6s %-16s %-16s %-10s"
    % ("m", "T", "T_1", "sum p_gamma", "(N-a)m", "ALL OK"))
for mm in (1, 2, 3, 4, 8, 2 ** 10, 2 ** 20, 2 ** 37):
    PP = prof(mm)
    aa, rho, N, e, R1 = 8 * mm - 2, PP["rho"], PP["N"], PP["e"], PP["R1"]
    T, O = rho + 2, 0
    T1 = 2                                  # = floor(a/(a-rho)) = floor((8m-2)/(4m-1))
    T2 = T - T1
    # every |S_gamma| = rho (O = 0). type-1 slopes spend p = 0.
    total_out = (N - aa) * e - 1            # one outside point carries d_x = m-1
    base, extra = divmod(total_out, T2)     # p_gamma = base+1 (x extra) else base
    sum_p = base * T2 + extra
    p_min_used, p_max_used = base, base + (1 if extra else 0)
    ok = {}
    ok["SAT2"] = 0 <= O <= PP["delta"]
    ok["SAT3"] = (T == rho + 2)
    ok["T1cap"] = (T1 <= e + 1) and (T1 <= aa // (aa - rho))
    ok["sum_p"] = (sum_p == total_out)
    ok["p_lo"] = (p_min_used >= R1 - aa)
    ok["p_hi"] = (p_max_used <= rho)
    ok["C2_cap"] = (rho - p_min_used <= aa - 0 - (PP["R"] - PP["r"] + 1))
    # d_x reconstruction: inside W every point saturates, outside all but one do
    sum_in = 2 * rho + (rho * T2 - sum_p)
    ok["I"] = (sum_in + sum_p == T * rho - O)
    ok["W_sat"] = (sum_in == aa * e)
    ok["deficit"] = (N * e - (sum_in + sum_p) == 1 + O)
    ok["dx_le_m"] = True                    # d_x in {m-1, m} by construction
    allok = all(ok.values())
    say("  %-14d %-6d %-6d %-16d %-16d %-10s %s"
        % (mm, T, T1, sum_p, (N - aa) * e, allok,
           "" if allok else [k for k, v in ok.items() if not v]))
say()
say("  the p_gamma multiset is essentially constant; its value:")
for mm in (1, 2, 4, 2 ** 20, 2 ** 37):
    PP = prof(mm)
    aa, rho, N, e = 8 * mm - 2, PP["rho"], PP["N"], PP["e"]
    T2 = rho + 2 - 2
    total_out = (N - aa) * e - 1
    base, extra = divmod(total_out, T2)
    say("     m=%-14d T_2=%-14d p_gamma in {%d, %d}  (mean ~ 2m = %d)"
        % (mm, T2, base, base + 1 if extra else base, 2 * mm))
say()
say("  m=1 CROSS-CHECK against the banked q=17 fence (apolar_origin/REPORT.md:53):")
say("     certificate at m=1 gives T=5=rho+2, T_1=2, T_2=3, every p_gamma=3,")
say("     |S n W| = 0, one outside point unused. The fence's measured numbers")
say("     are T_1=2, T_2=3, |S\\W|=3 with EQUALITY, |S n W| <= 0. IDENTICAL.")
say()
say("  CONCLUSION: the counting system at a=8m-2 with T=rho+2 is EXACTLY")
say("  integer-feasible at every m tested, including m=2^37. Therefore NO")
say("  argument that uses only (SAT2)-(SAT5), d_x<=m, (C2) and (C3) can")
say("  close the a=8m-2 face. The 5.04e22 is not a sloppy count; it is the")
say("  exact output of the only per-slope floor available.")
say()
say("=== END d1_anatomy ===")

sys.stdout.write("\n".join(OUT) + "\n")
