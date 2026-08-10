#!/usr/bin/env python3
"""D4 - the verdict ledger: exactly what the canonical-W (FR) theorem buys.

Two admissible choices of joint support for the (AO1) counting cap:
  option 1 (banked): W = the true minimum joint support, |W| = w*,
                     spend floor (C2) = R+1-w*.
  option 2 (new):    W = S_g u S_h for a pair MINIMISING the union,
                     |W| = a* >= w*, spend floor max(R+1-a*, 2a*-3rho)
                     where the second term is the (FR) theorem
                     |S_gamma ^ W| <= 4rho-2a*.
The prover takes the min; the adversary maximises over w* <= a* <= 7m-1.
Because option 1 improves as w* falls, the adversary sets w* = a*, so the
one-parameter sweep in a = w* = a* is the exact worst case.
Framing B (T4 cross-check): T <= T_1 + (m+1) + CAP restricted to j>=1.
Run under tools/ramguard tiny.
"""


def candidates(m):
    """The ratio is increasing on the (C2) piece and decreasing on the (FR)
    piece, so the argmax is the crossing a0=(20m-2)/3 (new) or the top of
    the band (old).  Full enumeration is used as a control for m <= 64."""
    a0 = (20 * m - 2) // 3
    cs = {6 * m - 1, 7 * m - 1}
    for d in range(-3, 4):
        if 6 * m - 1 <= a0 + d <= 7 * m - 1:
            cs.add(a0 + d)
    return sorted(cs)


def sweep(m, full=False):
    N, rho, R, e, T = 16 * m, 4 * m - 1, 8 * m, m, 4 * m + 1
    best_old = best_new = None
    # for the two huge m the sweep is restricted to a >= 6m-1, where the
    # (AO1) first term is exactly 2; the full sweeps at m <= 1024 confirm the
    # argmax always lies in that range.
    rng = range(4 * m + 2, 7 * m) if full else candidates(m)
    for a in rng:
        x_old = a - (4 * m + 2)                       # (C2)
        x_new = min(x_old, 4 * rho - 2 * a)           # (C2) and (FR)
        p_old, p_new = rho - x_old, rho - x_new
        capA_old = (N - a) * e // p_old
        capA_new = (N - a) * e // p_new
        # framing B (T4 caps the j=0 family at m+1; counting only the j>=1)
        t1 = min(m + 1, a // (a - rho), (a * m) // rho)     # (AO1) first term
        capB_new = t1 + (m + 1) + (N - a) * e // p_new
        tot_old, tot_new = t1 + capA_old, min(t1 + capA_new, capB_new)
        need_p = (N - a) * e // (T - t1) + 1
        r_old, r_new = tot_old / (rho + 1), tot_new / (rho + 1)
        if best_old is None or r_old > best_old[1]:
            best_old = (a, r_old)
        if best_new is None or r_new > best_new[1]:
            best_new = (a, r_new, x_new, need_p, rho - need_p, p_new)
    return best_old, best_new


def main():
    out = []
    P = out.append
    P("=== D4  verdict ledger: banked (C2)-only vs (C2)+(FR at canonical W) ===")
    P("")
    P("   m        worst a (old)  factor_old   worst a (new)  factor_new   a_new/m"
      "   X_proved  X_needed  gap")
    for m in (2, 3, 4, 8, 64, 1024, 2 ** 20, 2 ** 37):
        bo, bn = sweep(m, full=(m <= 1024))
        if m <= 64:                                   # control: candidates == full
            co, cn = sweep(m, full=False)
            assert (co[1], cn[1]) == (bo[1], bn[1]), ("candidate set missed the argmax", m)
        P("  %-12d %12d %10.5f %14d %11.5f %8.4f %10d %9d %6.4f"
          % (m, bo[0], bo[1], bn[0], bn[1], bn[0] / m, bn[2], bn[4],
             bn[2] / max(1, bn[4])))
    P("")
    P("  columns: worst a = argmax over the admissible band [4m+2, 7m-1] of the")
    P("  residual factor (AO1)/(rho+1);  X_proved = the (C2)^(FR) bound at that a;")
    P("  X_needed = rho - (floor((N-a)e/(T-2))+1), the max-intersection bound that")
    P("  WOULD close;  gap = X_proved/X_needed  (the factor still missing).")
    P("")
    P("-- the three landmark a-values at m = 2^37 (exact integers) --")
    m = 2 ** 37
    N, rho, e, T = 16 * m, 4 * m - 1, m, 4 * m + 1
    for a, tag in ((6 * m, "6m     (where the (AO1) first term drops to 2)"),
                   ((20 * m - 2) // 3, "20m/3  (NEW argmax after (FR))"),
                   (7 * m - 1, "7m-1   (banked evaluation point, (NEWCAP) top)")):
        x_old = a - (4 * m + 2)
        x_new = min(x_old, 4 * rho - 2 * a)
        cap_old = (N - a) * e // (rho - x_old)
        cap_new = (N - a) * e // (rho - x_new)
        need_p = (N - a) * e // (T - 2) + 1
        P("  a=%d   %s" % (a, tag))
        P("    X<=  banked %d -> sharpened %d ; needed %d" % (x_old, x_new, rho - need_p))
        P("    AO1  banked %d -> sharpened %d ; rho+1 = %d" % (2 + cap_old, 2 + cap_new, rho + 1))
        P("    factor banked %.6f -> sharpened %.6f" % ((2 + cap_old) / (rho + 1),
                                                        (2 + cap_new) / (rho + 1)))
    P("")
    P("-- headline --")
    bo, bn = sweep(2 ** 37)
    P("  residual (ii) factor over the whole band: %.6f  ->  %.6f   (9/4 -> 7/4)"
      % (bo[1], bn[1]))
    P("  at the banked evaluation point a=7m-1 alone:      2.250000 -> 1.125000  (9/4 -> 9/8)")
    P("  the band itself is UNCHANGED: (16m/3, 7m-1].  NEITHER BUDGET CLOSES.")
    P("  what is still missing at the new argmax a=(20m-2)/3: X <= 5m/3, proved X <= 8m/3.")
    open("notes/pilots_20260810/rh_fr_algebraic/d4_verdict_results.txt", "w").write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
