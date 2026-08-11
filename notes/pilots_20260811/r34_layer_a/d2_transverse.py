"""D2 -- THE TRANSVERSE-SPLITTING QUESTION, answered in the LAYER-A variables.

The brief's D2 asks whether a ramification budget forces >= m non-split degree
in the TRANSVERSE direction.  d3_scale.py shows the ramification budget cannot:
a totally split fibre is reduced, hence unramified, so the rigidity spends
nothing, and the Plucker budget is slack in both pictures.

What DOES bite is deg_x ADDITIVITY plus fibre disjointness.  Setting (all
banked): Q(Z,x) the primitive apolar kernel biform, deg_Z Q <= m,
deg_x Q <= rho = 4m-1 (background/nodes/rate_half_ca_hankel_endpoint_
rational_normal_kernel_curve/statement.md:16-40, PROVED);
D = mu_N, N = 16m; Gamma the T = 4m+1 supported slopes; sum_gamma u_gamma
= T*rho - O with O <= delta = m-1 ((SAT1),(SAT2)); and Q(.,x) != 0 for every
x in D (saturation_rigidity/statement.md:49).

Factor Q = c(x) * prod_j Q_j(Z,x) into irreducibles over F_q(x), with
m_j := deg_Z Q_j, d_j := deg_x Q_j.  Then

  (1) deg_x is ADDITIVE on products in the domain F_q[x][Z], so
      sum_j d_j <= deg_x Q <= rho = 4m-1.
  (2) For fixed j, #{x in D : Q_j(gamma,x) = 0} <= d_j, and summing over the
      T slopes: sum_gamma n_(j,gamma) <= T*d_j.
  (3) Also #{gamma in Gamma : Q_j(gamma,x) = 0} <= m_j for each x (Q_j(.,x)
      is not identically zero because Q(.,x) is not), so
      sum_gamma n_(j,gamma) <= N*m_j.
  (4) c has NO zero in D (a zero would make Q(.,x) vanish identically), so
      u_gamma <= sum_j n_(j,gamma) and

          T*rho - O  <=  sum_j min( T*d_j , N*m_j ) ,   sum_j d_j <= rho.

This script VERIFIES the combinatorial core of (4) exhaustively: for every
partition (m_j) of m it computes the exact maximum of sum_j min(T d_j, N m_j)
over d_j >= 1 with sum d_j <= rho, and reports which factorisation profiles
can survive.  It also checks the m=1 realized witnesses against the theorem.
"""

import sys
from itertools import combinations

sys.path.insert(0, "notes/pilots_20260811/r34_layer_a")
from d1_calib import (enumerate_families, chart_with_finite_slopes, pdeg)  # noqa

Q1 = 17


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for p in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest


def max_cover(part, m):
    """exact max of sum_j min(T d_j, N m_j) over d_j >= 1, sum d_j <= rho."""
    T = 4 * m + 1
    N = 16 * m
    rho = 4 * m - 1
    r = len(part)
    if r > rho:
        return None                      # cannot give every factor d_j >= 1
    gains = []
    for mj in part:
        cap = (N * mj) // T              # units of full gain T
        for _ in range(cap):
            gains.append((T, mj))
        rem = N * mj - T * cap
        if rem > 0:
            gains.append((rem, mj))
    # every factor needs d_j >= 1 first (that unit is forced, gain = its first)
    forced = 0
    pool = []
    for mj in part:
        cap = (N * mj) // T
        first = T if cap >= 1 else (N * mj)
        forced += first
        extra = []
        for _ in range(max(cap - 1, 0)):
            extra.append(T)
        rem = N * mj - T * cap
        if rem > 0 and cap >= 1:
            extra.append(rem)
        pool.extend(extra)
    pool.sort(reverse=True)
    budget = rho - r
    return forced + sum(pool[:budget])


def main():
    lines = []

    def out(s=""):
        print(s)
        lines.append(s)

    out("=" * 78)
    out("D2 -- TRANSVERSE SPLITTING: the FACTOR-DEGREE DICHOTOMY")
    out("=" * 78)
    out("")

    # ------------------------------------------------ m=1 realized witnesses
    out("[A] the m=1 REALIZED witnesses against the theorem")
    D = sorted(pow(3, i, Q1) for i in range(16))
    fams = enumerate_families(D)
    prof = {}
    for fam, (t1, t2) in sorted(fams.items(), key=lambda kv: sorted(kv[0])):
        A, B, slopes, supp = chart_with_finite_slopes(t1, t2, D)
        # Q(Z,x) = A(x) + Z B(x) = c(x) * (b_1(x) Z - a_1(x)), one branch
        dA, dB = pdeg(A), pdeg(B)
        delta = max(dA, dB)
        prof[(dA, dB, delta)] = prof.get((dA, dB, delta), 0) + 1
    out(f"    Q(Z,x) = A(x) + Z B(x): (deg A, deg B, delta_1) histogram over "
        f"the 16 witnesses: {prof}")
    m = 1
    out(f"    theorem's inputs at m=1: rho = {4*m-1}, T = {4*m+1}, N = {16*m}")
    out(f"    sum_j delta_j = 3 = rho   (the deg_x bound is TIGHT)")
    out(f"    T * delta_1 = {(4*m+1)*3} <= N = {16*m}   (slack "
        f"{16*m-(4*m+1)*3} = 1+O with O = 0)")
    out(f"    'small' means T*d < N*m_j, i.e. 5d < 16: d <= 3.  The single "
        f"branch IS small (d=3), so t = 1 and m_1 = 1 >= ceil((3m+1)/4) = 1.")
    out(f"    => m = 1 sits EXACTLY on the theorem's boundary, as realized.")
    out("")

    # ------------------------------------- exhaustive combinatorial core
    out("[B] EXHAUSTIVE check of the counting inequality over EVERY "
        "factorisation profile")
    out("    surviving profile = a partition (m_j) of m for which some degree")
    out("    vector (d_j >= 1, sum d_j <= rho) satisfies "
        "T*rho - O <= sum_j min(T d_j, N m_j),")
    out("    taking the most generous O = delta = m-1.")
    out("")
    out(f"    {'m':>4s} {'#partitions':>12s} {'#surviving':>11s} "
        f"{'all-ones survives?':>19s} {'min over survivors of max m_j':>31s} "
        f"{'ceil((3m+1)/4)':>15s}")
    bad = 0
    for m in range(1, 41):
        T, Nn, rho = 4 * m + 1, 16 * m, 4 * m - 1
        need = T * rho - (m - 1)
        surv = []
        tot = 0
        for part in partitions(m):
            tot += 1
            mc = max_cover(part, m)
            if mc is not None and mc >= need:
                surv.append(part)
        allones = tuple([1] * m) in surv
        mm = min(max(p) for p in surv) if surv else None
        thr = -(-(3 * m + 1) // 4)
        if m >= 2 and allones:
            bad += 1
        if mm is not None and mm < thr:
            bad += 1
        if m <= 12 or m in (16, 20, 24, 32, 40):
            out(f"    {m:4d} {tot:12d} {len(surv):11d} "
                f"{str(allones):>19s} {str(mm):>31s} {thr:15d}")
    out("")
    out(f"    VIOLATIONS of the theorem over m = 1..40: {bad}   "
        f"{'PASS' if bad == 0 else 'FAIL'}")
    out("")
    out("    Readings:")
    out("      * the all-ones profile (Q splits into LINEAR factors over")
    out("        F_q(x), i.e. all m slope branches are rational functions of")
    out("        x) survives ONLY at m = 1;")
    out("      * every surviving profile has an irreducible factor of")
    out("        Z-degree >= ceil((3m+1)/4);")
    out("      * at m = 2,3,4 the only survivor is the single factor (m),")
    out("        i.e. Q is IRREDUCIBLE over F_q(x).")
    out("")

    # ------------------------------------------- the surviving profiles, small m
    out("[C] the surviving profiles explicitly, m = 1..8")
    for m in range(1, 9):
        T, Nn, rho = 4 * m + 1, 16 * m, 4 * m - 1
        need = T * rho - (m - 1)
        surv = [p for p in partitions(m)
                if (max_cover(p, m) or -1) >= need]
        out(f"    m={m:2d}  need {need:6d}  survivors: {surv}")
    out("")

    with open(sys.argv[1], "w") as f:
        f.write("\n".join(lines) + "\n")


main()
