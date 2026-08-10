#!/usr/bin/env python3
"""D2 - the exact (AO1) ledger with and without the canonical-W (FR) bound.

All integer arithmetic, closed form, no lists of length O(N) (the m=2^37
column must not materialise the domain).  Stdlib only.

Objects (round-31 notation, apolar_origin/PREREG.md:151-166):
  N=16m, rho=4m-1, R=8m, e=m, T=rho+2=4m+1, W a joint support, a=|W|.
  (C2)  p_gamma := |S_gamma\\W| >= (R+1)-a+n_gamma        [type-2]
  (FR)  X_gamma := |S_gamma^W| <= 4rho-2a  when W=S_g u S_h is a
        MINIMISING pair union (a = a* = min_pair union), because
        |S_gamma^S_g| <= u_gamma+u_g-a* <= 2rho-a*.
  CAP(a,p) = floor((N-a)e/p) is the type-2 count bound.
Run under tools/ramguard tiny.
"""


def newcap_mean_pair_union(m, O):
    """Exact upper bound on the MINIMUM pair union: the mean pair union
    with sum_x C(d_x,2) replaced by its convexity minimum Lmin(O)."""
    N, rho, T = 16 * m, 4 * m - 1, 4 * m + 1
    c2 = lambda n: n * (n - 1) // 2
    Lmin = (N - 1 - O) * c2(m) + (1 + O) * c2(m - 1)
    num = (T - 1) * (T * rho - O) - Lmin
    den = c2(T)
    return num, den, num // den


def t1cap(m, a, O=0):
    """(AO1) first term, apolar_origin/PREREG.md:197.  Equals 2 exactly for
    a >= 6m-1; larger for smaller a, which my first pass wrongly fixed at 2."""
    rho = 4 * m - 1
    return min(m + 1, a // (a - rho), (a * m + O) // rho)


def ledger(m, verbose_rows=None):
    N, rho, R, e, T = 16 * m, 4 * m - 1, 8 * m, m, 4 * m + 1
    rows = []
    for a in range(4 * m + 2, 7 * m):          # the admissible w* window, capped by (NEWCAP)
        x_c2 = a - (4 * m + 2)                 # (C2) at n_gamma=0, o=0
        x_fr = 4 * rho - 2 * a                 # canonical-W (FR)
        x_old = x_c2
        x_new = min(x_c2, x_fr)
        p_old, p_new = rho - x_old, rho - x_new
        cap_old = (N - a) * e // p_old if p_old > 0 else None
        cap_new = (N - a) * e // p_new if p_new > 0 else None
        t1 = t1cap(m, a)
        T2 = T - t1
        need_p = (N - a) * e // T2 + 1          # p_min needed to refute T=rho+2
        need_x = rho - need_p
        rows.append((a, x_c2, x_fr, x_new, p_new, cap_old, cap_new, t1 + cap_new,
                     need_p, need_x, (t1 + cap_new) / (rho + 1)))
    return rows


def main():
    out = []
    P = out.append
    P("=== D2  (AO1) ledger with the canonical-W (FR) bound ===")

    # 1. (NEWCAP) re-derivation: min pair union <= 7m-1, all O
    P("\n-- 1. (NEWCAP) exact: bound on the minimum pair union a* --")
    for m in (2, 3, 4, 8, 64, 1024):
        worst = None
        for O in range(0, m):                  # (SAT2) O <= delta = m-1
            num, den, val = newcap_mean_pair_union(m, O)
            if worst is None or val > worst[1]:
                worst = (O, val)
        P(f"  m={m:6d}: max over O in [0,m-1] of floor(mean pair union) = {worst[1]}"
          f"  at O={worst[0]}   7m-1={7*m-1}   OK={worst[1] <= 7*m-1}")

    # 2. the fence's own scale, full a-sweep
    P("\n-- 2. a-sweep at m=64 (the fence's scale): banked vs sharpened --")
    P("     a   X<=(C2)  X<=(FR)  X_new  p_new   CAP_old   CAP_new   AO1_new  need_p need_X  ratio")
    rows = ledger(64)
    for r in rows:
        if r[0] % 32 == 0 or r[0] in (4 * 64 + 2, 7 * 64 - 1):
            P("  {:5d} {:8d} {:8d} {:6d} {:6d} {:9d} {:9d} {:9d} {:6d} {:6d}  {:.4f}".format(*r))
    best = max(rows, key=lambda r: r[10])
    P(f"  ARGMAX ratio at a={best[0]} (= {best[0]/64:.4f} m): ratio={best[10]:.4f}"
      f"  [20m/3={20*64/3:.2f}]  AO1={best[7]} vs rho+1={4*64}")
    closes = [r[0] for r in rows if r[7] <= 4 * 64]
    P(f"  a-values where the sharpened (AO1) CLOSES (AO1<=rho+1): a<={max(closes) if closes else None}"
      f"   [16m/3={16*64/3:.2f}]  open band = ({max(closes) if closes else None}, {7*64-1}]")
    oldrows = [(r[0], t1cap(64, r[0]) + r[5]) for r in rows]
    oldclose = [a for a, v in oldrows if v <= 4 * 64]
    P(f"  banked ((C2) only) closes for a<={max(oldclose) if oldclose else None} -- the SAME threshold,"
      f" so (FR) does not move the band, only the factor inside it")

    # 3. official scale
    P("\n-- 3. official scale m=2^37 --")
    m = 2 ** 37
    N, rho, e, T = 16 * m, 4 * m - 1, m, 4 * m + 1
    for a, tag in ((7 * m - 1, "a=7m-1 (top of band, round-31 evaluation point)"),
                   ((20 * m - 2) // 3, "a=(20m-2)/3 (new argmax)"),
                   (16 * m // 3, "a=16m/3 (banked closure threshold)")):
        x_c2, x_fr = a - (4 * m + 2), 4 * rho - 2 * a
        x_new = min(x_c2, x_fr)
        p_old, p_new = rho - x_c2, rho - x_new
        cap_old, cap_new = (N - a) * e // p_old, (N - a) * e // p_new
        need_p = (N - a) * e // (T - 2) + 1
        P(f"  {tag}")
        P(f"    a={a}  X<=(C2)={x_c2}  X<=(FR)={x_fr}  ->  X<={x_new}")
        P(f"    p_min: banked {p_old} -> sharpened {p_new}   (needed to refute: {need_p})")
        P(f"    CAP:   banked {cap_old} -> sharpened {cap_new}")
        P(f"    AO1:   banked {2+cap_old} -> sharpened {2+cap_new}   vs rho+1={rho+1}")
        P(f"    residual factor: banked {(2+cap_old)/(rho+1):.6f} -> sharpened {(2+cap_new)/(rho+1):.6f}")

    # 4. asymptotic constants, exact rationals via integers at huge m
    P("\n-- 4. asymptotic constants (m=2^37, ratio to m) --")
    P(f"  X<=(FR) at a=7m-1 : {4*rho-2*(7*m-1)} = 2m-2 ? {4*rho-2*(7*m-1) == 2*m-2}")
    P(f"  crossing (C2)=(FR): a=(20m-2)/3={(20*m-2)//3}, X there = {(20*m-2)//3-(4*m+2)}"
      f" ~ (8m-8)/3 = {(8*m-8)//3}")
    P(f"  needed X at a=7m-1: {rho - ((N-(7*m-1))*e//(T-2)+1)}  ~ 7m/4 = {7*m//4}")
    P(f"  mean |S^W| at a=7m-1 over all T slopes: m*a/T = {m*(7*m-1)//T} ~ 7m/4 = {7*m//4}")

    # 5. the min<=mean audit of the counting instrument
    P("\n-- 5. counting-instrument audit (why a floor must beat the MEAN, not the MDS bound) --")
    for m in (2, 3, 4, 8, 64):
        N, rho, e, T = 16 * m, 4 * m - 1, m, 4 * m + 1
        a = 7 * m - 1
        tot = (N - a) * e                       # = sum_{type-2} p + def_out, def_out in [0,1+O]
        T2 = T - 2
        P(f"  m={m:3d} a={a:5d}: sum_(type-2) p = (N-a)e - def_out = {tot} - def_out ;"
          f" T_2={T2} ; mean p = {tot/T2:.4f} ; (C2) floor = {8*m+1-a} ; (FR) floor = {rho-(2*m-2)}")
    P("  A per-slope floor P refutes T=rho+2 iff P*T_2 > (N-a)e - def_out, i.e. iff P exceeds the")
    P("  MEAN spend.  (C2) gives m+2 (mean/floor = 9/4); (FR) gives 2m+1 (mean/floor = 9/8).")

    open("notes/pilots_20260810/rh_fr_algebraic/d2_budget_results.txt", "w").write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
