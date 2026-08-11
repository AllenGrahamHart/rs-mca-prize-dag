#!/usr/bin/env python3
"""D1 - the aggregate identity for the psi_gamma / X_gamma family.

Exact integer + Fraction arithmetic, closed form; no O(m) allocation and no
O(m) sweep at large m (bisection on the monotone part + a bounded window).

Objects (PREREG R0):
  N=16m, rho=4m-1, R+1=8m+1, e=m, A=3, s=0, T=rho+2 assumed (the failure
  configuration), T_1 type-1 slopes, T_2 = T - T_1 type-2 slopes.
  X_gamma = |S_gamma ^ W|, p_gamma = |S_gamma \\ W| = u_gamma - X_gamma.
  (C2) floor p >= (R+1)-a+n   ->  X <= a-(4m+2)-n
  (FR) floor p >= 2a-3rho     ->  X <= 4rho-2a          (round 32, D2.1)
  (AO1) T <= T1cap + floor((N-a)e/p_proved)

Identities tested:
 (AGG)   sum_{supported gamma} X_gamma = sum_{x in W} d_x = a*m - def_in
 (SPEND) sum_{type-2} p_gamma = (N-a)*m - def_out            [banked r32]
 (DEF)   def_in + def_out = 1 + O                            [banked (C4)]
 (R2.6)  (AO1) closure  <=>  T_2 * p_proved > (N-a)*m   (exact, not approx)
 (R2.4)  rho*(mean_X - need_X_real) = 4m - def_in + o_g + o_h  (a-independent)
"""
from fractions import Fraction as F

BIG = 1 << 62


def T1cap(m, a, O=0):
    rho = 4 * m - 1
    c = [m + 1, (a * m + O) // rho]
    if a > rho:
        c.append(a // (a - rho))
    return min(c)


def p_c2(m, a, n=0):
    return (8 * m + 1) - a + n


def p_fr(m, a, O=0):
    return 2 * a - 3 * (4 * m - 1) + O


def p_proved(m, a, sharpened=True):
    v = p_c2(m, a)
    return max(v, p_fr(m, a)) if sharpened else v


def AO1(m, a, sharpened=True, O=0):
    p = p_proved(m, a, sharpened)
    if p <= 0:
        return BIG
    return T1cap(m, a, O) + ((16 * m - a) * m) // p


def closes(m, a, sharpened=True, O=0):
    return AO1(m, a, sharpened, O) <= 4 * m


def agg_closes(m, a, sharpened=True, O=0):
    """aggregate form: the proved per-slope floor strictly beats the forced
    mean spend (N-a)m/T_2.  Derived, not assumed, to equal `closes`."""
    rho = 4 * m - 1
    T2 = rho + 2 - T1cap(m, a, O)
    p = p_proved(m, a, sharpened)
    return T2 * p > (16 * m - a) * m


def need_X(m, a, T2=None):
    rho = 4 * m - 1
    if T2 is None:
        T2 = rho
    return rho - ((16 * m - a) * m) // T2 - 1


def need_X_real(m, a, T2=None):
    rho = 4 * m - 1
    if T2 is None:
        T2 = rho
    return F(rho) - F((16 * m - a) * m, T2) - 1


def mean_X(m, a, O=0, def_in=0, o_g=0, o_h=0, T1=2):
    """forced mean of X over the T_2 = rho+2-T1 type-2 slopes."""
    rho = 4 * m - 1
    return F(a * m - def_in - T1 * rho + o_g + o_h, rho + 2 - T1)


def X_proved(m, a, sharpened=True):
    return (4 * m - 1) - p_proved(m, a, sharpened)


def amax(m, pred):
    """largest a in [4m+2, 8m] with pred(a).

    h(a) = floor((N-a)m/(R+1-a)) is strictly increasing on a < R+1 (the
    derivative sign is m(N-R-1) > 0) and T1cap >= 2 throughout the range,
    so every closing a satisfies h(a) <= 4m-2; bisect that, then scan a
    bounded window downward.  NOTE (run-1 finding): closure is NOT monotone
    in a -- T1cap steps down and can re-close a single larger a (m=8: a=41
    fails, a=42 closes) -- so a bare bisection would be wrong.
    """
    lo, hi = 4 * m + 2, 8 * m

    def h(a):
        return ((16 * m - a) * m) // (8 * m + 1 - a)

    if h(lo) > 4 * m - 2:
        return lo - 1
    a0, b0 = lo, hi
    while a0 < b0:
        mid = (a0 + b0 + 1) // 2
        if h(mid) <= 4 * m - 2:
            a0 = mid
        else:
            b0 = mid - 1
    a = a0
    lim = max(lo, a0 - 500)
    while a >= lim and not pred(a):
        a -= 1
    return a


out = []
P = out.append

P("=" * 78)
P("SECTION 1 -- (R2.6) (AO1) IS the aggregate criterion, exactly")
P("=" * 78)
P("  claim: T1cap + floor((N-a)m/p) <= rho+1   <=>   T_2 * p > (N-a)*m,")
P("         T_2 = rho+2-T1cap.  i.e. (AO1) says exactly `the proved per-slope")
P("         floor strictly beats the forced mean spend'.")
P("")
mism = 0
tot = 0
for m in [2, 3, 4, 8, 16, 64, 256, 1024]:
    for a in range(4 * m + 2, 8 * m + 1):
        for sh in (False, True):
            tot += 1
            if closes(m, a, sh) != agg_closes(m, a, sh):
                mism += 1
P("  pointwise m in {2,3,4,8,16,64,256,1024}, all a in [4m+2,8m], both floors:")
P("  checks = %d   MISMATCHES = %d" % (tot, mism))
P("")
P("    m     a_max via (AO1)   a_max via aggregate   equal?      16m/3   a_max/m")
for m in [2, 3, 4, 8, 16, 64, 256, 1024, 1 << 20, 1 << 37]:
    ab = amax(m, lambda a: closes(m, a, False))
    aa = amax(m, lambda a: agg_closes(m, a, False))
    P("%6d %17d %21d   %6s %10s %9.5f" %
      (m, ab, aa, ab == aa, str(F(16 * m, 3)), ab / m))

P("")
P("=" * 78)
P("SECTION 2 -- (R2.4) the shortfall  rho*(mean_X - need_X)  is a-INDEPENDENT")
P("=" * 78)
P("  mean_X = (a*m - def_in - 2rho)/rho   [T_1 = 2]")
P("  need_X_real = rho - (N-a)m/rho - 1")
P("  claim (CORRECTED after run 2 -- the registered R2.4 form 4m+O-def_in was")
P("  WRONG: O enters only through the two type-1 defects o_g, o_h):")
P("      rho*(mean_X - need_X_real) = 4m - def_in + o_g + o_h, for EVERY a.")
P("  def_in in [0,1+O], o_g+o_h in [0,O], O <= m-1, so the shortfall lies in")
P("  [4m-1-O, 4m+O] and is STRICTLY POSITIVE for every admissible O.")
P("")
P("      m            a   rho*(mean-need_real)      4m   verdict")
bad = 0
for m in [2, 8, 64, 1024, 1 << 20, 1 << 37]:
    for a in [4 * m + 2, (16 * m) // 3, (20 * m - 2) // 3, 7 * m - 1, 2 * (4 * m - 1)]:
        v = (4 * m - 1) * (mean_X(m, a) - need_X_real(m, a))
        ok = (v == 4 * m)
        bad += (not ok)
        P("%7d %12d %22s %7d   %s" % (m, a, str(v), 4 * m,
                                      "OK" if ok else "**MISMATCH**"))
P("  total mismatches: %d" % bad)
P("")
P("  with nonzero deficit/defect: claim 4m - def_in + o_g + o_h")
P("      m       a  def_in  o_g  o_h     value   4m-def_in+o_g+o_h   verdict")
for (m, a, di, og, oh) in [(64, 426, 1, 0, 0), (64, 426, 3, 2, 5),
                           (1024, 6826, 17, 11, 6), (1 << 20, 6990506, 2, 1, 1),
                           (1 << 37, 916259689812, 1, 0, 1)]:
    v = (4 * m - 1) * (mean_X(m, a, def_in=di, o_g=og, o_h=oh) - need_X_real(m, a))
    tgt = 4 * m - di + og + oh
    P("%7d %12d %6d %4d %4d %9s %19d   %s" %
      (m, a, di, og, oh, str(v), tgt, "OK" if v == tgt else "**MISMATCH**"))
P("")
P("  INTEGER form (what the ledger uses):")
P("  rho*(mean_X - need_X) = 4m - r0,  r0 = ((N-a)*m) mod rho in [0, rho-1],")
P("  so the integer shortfall lies in [2, 4m]: never zero, never negative.")
P("      m        a      r0    4m-r0   rho*(mean-need)")
for m in [64, 1024]:
    lo = amax(m, lambda a: closes(m, a, False)) + 1
    hi = 7 * m - 1
    for a in [lo, (lo + hi) // 2, (20 * m - 2) // 3, hi]:
        rho = 4 * m - 1
        r0 = ((16 * m - a) * m) % rho
        v = rho * (mean_X(m, a) - need_X(m, a))
        P("%7d %8d %7d %8d %17s" % (m, a, r0, 4 * m - r0, str(v)))

P("")
P("=" * 78)
P("SECTION 3 -- (R2.5) the argmax in closed form, and the 7/4 and the 8/5")
P("=" * 78)
P("  argmax = crossing of p_C2 = 8m+1-a with p_FR = 2a-3rho  ->  a = (20m-2)/3")
P("  factor there = mean_p / proved_p = (28m+2)m/((4m+5)(4m-1)) -> 7/4")
P("")
P("        m    argmax(sweep)   (20m-2)/3     factor(exact)     float    Xprv        Xned   ratio")
for m in [2, 3, 4, 8, 64, 1024, 1 << 20, 1 << 37]:
    lo = amax(m, lambda a: closes(m, a, False)) + 1
    hi = 7 * m - 1
    if hi - lo <= 40000:
        cand = list(range(lo, hi + 1))
    else:
        cand = sorted(set([lo, hi] + [(20 * m - 2) // 3 + d for d in range(-3, 4)]))
    ba, bf = None, None
    for a in cand:
        f = F(AO1(m, a, True), 4 * m)
        if bf is None or f > bf:
            ba, bf = a, f
    Xp, Xn = X_proved(m, ba), need_X(m, ba)
    P("%9d %13d %13d %17s %9.5f %8d %11d %7.4f" %
      (m, ba, (20 * m - 2) // 3, str(bf), float(bf), Xp, Xn, Xp / Xn))
P("")
P("  exact closed form at a = (20m-2)/3 (needs m = 1 mod 3 for integrality).")
P("  CORRECTED after run 2: the registered `7m/(4m-1)` was a sloppy asymptotic.")
P("  Exact:  p_C2 = p_FR = (4m+5)/3,  X_proved = (8m-8)/3,")
P("          mean_p/p_proved = (28m+2)m / ((4m+5)(4m-1))  ->  7/4.")
P("        m           a   p_C2   p_FR   X_proved   mean_p/p_proved(exact)     float")
for m in [4, 10, 100, 1024, 1 << 20]:
    if (20 * m - 2) % 3:
        continue
    a = (20 * m - 2) // 3
    rho = 4 * m - 1
    mp = F((16 * m - a) * m, rho)
    fac = mp / F(p_proved(m, a))
    cf = F((28 * m + 2) * m, (4 * m + 5) * (4 * m - 1))
    P("%9d %11d %6d %6d %10d %24s %9.6f   %s" %
      (m, a, p_c2(m, a), p_fr(m, a), X_proved(m, a), str(fac), float(fac),
       "closed-form OK" if fac == cf else "**MISMATCH**"))

P("")
P("=" * 78)
P("SECTION 4 -- EXCESS coordinates (R2.2/R2.3): X = (a-n-(4m+2)) - (o+j+cancel-ov)")
P("=" * 78)
P("  E := n + o + j + cancel - ov;  target X <= need_X  <=>  E >= Eneed")
P("  Eneed(a) = (a-(4m+2)) - need_X(a);  Emean(a) = (a-(4m+2)) - mean_X(a)")
P("  fibre budget sum_{g in P^1} n_g = a  =>  #{gamma : n_gamma >= Eneed} <= a//Eneed")
P("")
P("        m            a         Eneed     Eneed-Emean   a//Eneed      rho   Eneed/m")
for m in [4, 8, 64, 1024, 1 << 20, 1 << 37]:
    for a in [(20 * m - 2) // 3, 7 * m - 1]:
        En = (a - (4 * m + 2)) - need_X(m, a)
        Em = F(a - (4 * m + 2)) - mean_X(m, a)
        P("%9d %12d %13d %15s %10d %8d %9.5f" %
          (m, a, En, str(F(En) - Em), (a // En) if En > 0 else -1,
           4 * m - 1, En / m))

P("")
P("=" * 78)
P("SECTION 5 -- round-32 ledger replay (must reproduce REPORT.md:171-179)")
P("=" * 78)
P("       m   worst a(old)  factor_old   worst a(new)  factor_new         Xprv          Xned    gap")
for m in [2, 3, 4, 8, 64, 1024, 1 << 20, 1 << 37]:
    lo = amax(m, lambda a: closes(m, a, False)) + 1
    hi = 7 * m - 1
    if hi - lo <= 40000:
        cand = list(range(lo, hi + 1))
    else:
        cand = sorted(set([lo, hi] + [(20 * m - 2) // 3 + d for d in range(-3, 4)]))
    res = []
    for sh in (False, True):
        ba, bf = None, None
        for a in cand:
            f = F(AO1(m, a, sh), 4 * m)
            if bf is None or f > bf:
                ba, bf = a, f
        res.append((ba, bf))
    (ao, fo), (an, fn) = res
    Xp, Xn = X_proved(m, an), need_X(m, an)
    P("%8d %12d %11.5f %14d %11.5f %13d %13d %6.4f" %
      (m, ao, float(fo), an, float(fn), Xp, Xn, Xp / Xn))

txt = "\n".join(out)
with open("notes/pilots_20260811/rh_psi_degree/d1_aggregate_results.txt", "w") as fh:
    fh.write(txt + "\n")
print(txt)
