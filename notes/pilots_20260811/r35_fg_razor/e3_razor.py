#!/usr/bin/env python3
"""r35_fg_razor D2/D3: exact razor arithmetic, the type-2 ledger at razor
shape, the two first-moment thresholds, and the q_crit evaluation on the
official candidate row.  Stdlib only; every integer exact."""
import sys
from math import lgamma, log, log2, exp

LN2 = log(2.0)
OUT = []


def emit(s=""):
    OUT.append(str(s))
    print(s)
    sys.stdout.flush()


def H2(x):
    return -(x * log2(x) + (1 - x) * log2(1 - x))


def log2binom(n, r):
    """log2 C(n,r) via lgamma (accurate to ~0.02 bits at n ~ 2^41)."""
    return (lgamma(n + 1) - lgamma(r + 1) - lgamma(n - r + 1)) / LN2


def main():
    emit("=== r35_fg_razor  e3_razor  (exact razor arithmetic) ===")
    emit("")

    # ---------- E: razor integers ----------
    R = 1 << 40
    rho = 1 << 34
    r = R - rho
    n = 2 * R
    k = R
    a = n - r
    p = 2 * rho                      # deg P* at witnesses A and B
    m_P = r + 1 - p
    m_Q = p - rho
    degQp = R + 1 - p
    emit("---- E: pre-committed razor integers (R0-e) ----")
    E = [
        ("E1  R = n-k = 2^40", R),
        ("E2  rho = a-k = 2^34", rho),
        ("E3  2rho = 2^35", 2 * rho),
        ("E4  r = R-rho", r),
        ("E5  r+1", r + 1),
        ("E6  n = 2R = 2^41", n),
        ("E7  a = k+2^34", a),
        ("E8  n-a  (= r)", n - a),
        ("E9  p = deg P* = 2rho", p),
        ("E10 m_P = r+1-p = dim K_0", m_P),
        ("E11 m_Q = p-rho", m_Q),
        ("E12 deg Q' = R+1-p = m_P+m_Q = r+1-rho", degQp),
        ("E13 (r+1)+m_Q  [key-eq unknowns] = R+1", (r + 1) + m_Q),
        ("E14 p  [key-eq constraints]", p),
        ("E15 (r+1)+m_Q-p = R+1-p  [DOF surplus]", (r + 1) + m_Q - p),
        ("E16 codim{p*<=2rho} = 2R-3p", 2 * R - 3 * p),
        ("E17 dim{p*<=2rho} = 3p-4", 3 * p - 4),
        ("E18 codim U_gamma in Lambda = p-m_Q = rho", p - m_Q),
        ("E19 deg C_gamma <= p-1", p - 1),
        ("E20 (R+1)-a", (R + 1) - a),
        ("E21 r/R", "%d/%d" % (r // (R // 64), R // (R // 64))),
        ("E22 r/n", "%d/%d" % (r // (n // 128), n // (n // 128))),
    ]
    for lab, val in E:
        emit("  %-46s = %s" % (lab, val))
    emit("  CHECKS: (r+1)+m_Q == R+1 ? %s ;  m_P+m_Q == r+1-rho == R+1-p ? %s"
         % ((r + 1) + m_Q == R + 1,
            (m_P + m_Q == r + 1 - rho) and (r + 1 - rho == R + 1 - p)))
    emit("  CHECK : n-a == r ? %s ;  rho == a-k ? %s ;  r/R == 63/64 ? %s"
         % (n - a == r, rho == a - k, 64 * r == 63 * R))
    emit("")

    # ---------- F: entropy constants ----------
    emit("---- F: first-moment constants (razor shape r/n = 63/128) ----")
    h = H2(63.0 / 128.0)
    lgC_ent = n * h
    lgC_lg = log2binom(n, r)
    theta2 = n * h / (2 * rho)
    theta1 = n * h / rho
    emit("  F1  H2(63/128)                          = %.12f" % h)
    emit("  F2  log2 C(n,r) [entropy n*H2]          = %.6f" % lgC_ent)
    emit("      log2 C(n,r) [lgamma, exact-ish]     = %.6f" % lgC_lg)
    emit("      entropy - lgamma                    = %.6f bits"
         % (lgC_ent - lgC_lg))
    emit("  F3  theta_2 = n*H2/(2rho) = 64*H2       = %.6f   (q_crit^(2) ~ 2^64)"
         % theta2)
    emit("  F4  theta_1 = n*H2/rho    = 128*H2      = %.6f   (q_crit^(1) ~ 2^128)"
         % theta1)
    emit("      theta_1 == 2*theta_2 exactly ? %s" % (abs(theta1 - 2 * theta2) < 1e-9))
    for lq in (41, 128, 167, 256):
        lm1 = lgC_ent - rho * lq
        lm2 = lgC_ent - 2 * rho * lq
        emit("  q = 2^%-4d : log2 mu_1 = %+.6e   log2 mu_2 = %+.6e   "
             "mu_1<1:%s  mu_2<1:%s" % (lq, lm1, lm2, lm1 < 0, lm2 < 0))
    emit("  F7  log2 (fraction of deg-2rho P* that are D-split-squarefree)"
         " at q=2^41 = %+.6e" % (log2binom(n, 2 * rho) - 2 * rho * 41))
    emit("")

    # ---------- the LB1-C / mu_1 identity ----------
    emit("---- LB1 admissibility  IS  key-equation first-moment subcriticality ----")
    emit("  banked (LB1-C):  n < (a-k-1) * log2 q      [crossing_location:640-641]")
    emit("  key-eq mu_1<1 :  n*H2(r/n) < (a-k) * log2 q   [rho = a-k]")
    for lq in (167, 168, 128):
        marg_lb1 = (a - k - 1) * lq - n
        marg_mu1 = rho * lq - lgC_ent
        emit("   q=2^%-4d  LB1-C margin = %d   mu_1 margin = %.6f   "
             "difference = %.6f" % (lq, marg_lb1, marg_mu1, marg_mu1 - marg_lb1))
        emit("            predicted difference = log2 q + n(1-H2(r/n)) = %.6f"
             % (lq + n * (1 - h)))
    emit("  BANKED CONSTANT CHECK: LB1-C margin at q=2^167 should be"
         " 670,014,898,009 -> %d  (match: %s)"
         % ((a - k - 1) * 167 - n, (a - k - 1) * 167 - n == 670014898009))
    emit("")

    # ---------- type-2 ledger at razor shape ----------
    emit("---- the type-2 ledger at far-CA razor shape ----")
    emit("  (C2) [apolar_origin/PREREG.md:181-186, far-CA symbols]:")
    emit("     type-2 slope => |S_gamma \\ W| >= (R+1) - w* + n_gamma,")
    emit("     with w* = |W| a joint support of two bad locators, |S| = r.")
    emit("  admissible w* range: [r, min(2r,n)] = [%d, %d]" % (r, min(2 * r, n)))
    emit("  (R+1) - w* is POSITIVE only for w* <= R = %d," % R)
    emit("     i.e. only when |S_g ^ S_h| >= 2r-R = %d  (%.4f%% of r)"
         % (2 * r - R, 100.0 * (2 * r - R) / r))
    emit("  at the WORST case w* = 2r:  (R+1)-w* = %d   <-- VACUOUS (negative)"
         % (R + 1 - 2 * r))
    emit("  at the LB1 configuration w* = r+1: (R+1)-w* = R-r = rho = %d"
         % (R + 1 - (r + 1)))
    emit("     LB1 spends: S_gamma = W\\{gamma} subset W, so |S\\W| = 0 and")
    emit("     EVERY LB1 slope is type-1; T_2 = 0; the type-2 floor is unused.")
    emit("     d_x = r = %d for every x in W; e = r; (C3) T_1 <= e+1 = %d"
         " and LB1 has T_1 = r+1 = %d  -> TIGHT (equality)"
         % (r, r + 1, r + 1))
    cap_lb1 = ((n - (r + 1)) * r) // rho
    emit("     CAP = floor((n-w*)e/((R+1)-w*)) = floor(%d*%d/%d) = %d"
         % (n - (r + 1), r, rho, cap_lb1))
    emit("        = 2^%.4f ; T_2 = 0 <= CAP : SLACK by the whole cap"
         % log2(cap_lb1))
    emit("")

    # ---------- what would have to be true for FG to break a cap ----------
    emit("---- FG at razor: the budget, and what binds ----")
    emit("  key equation (FG4): gamma bad <=> exists sigma in D_r(D) with")
    emit("    sigma mod P* in U_gamma = C_gamma^{-1} Lambda_{<m_Q},")
    emit("    dim_Fq U_gamma = m_Q = %d,  dim_Fq Lambda = p = %d," % (m_Q, p))
    emit("    codim U_gamma = rho = %d  ->  exactly rho F_q-linear conditions."
         % rho)
    emit("  per-slope first moment = |D_r(D)| * q^{-rho} = C(n,r)/q^rho = mu_1.")
    for lq in (41, 128, 167, 256):
        lm1 = lgC_ent - rho * lq
        ET = lq + lm1 if lm1 < 0 else lq
        emit("    q=2^%-4d: log2 E[T] = log2 q + log2 min(1,mu_1) = %+.6e"
             % (lq, ET))
    emit("  BANKED LOWER BOUND (LB1, unconditional): B_ca^far(a) >= n-a+1"
         " = r+1 = %d = 2^%.4f   [crossing_location:635-637]" % (r + 1, log2(r + 1)))
    emit("  So at q = 2^167 the first moment predicts E[T] = 2^%.4e while the"
         % (167 + (lgC_ent - rho * 167)))
    emit("  proved floor is 2^%.4f: the first moment is WRONG BY %.6e BITS."
         % (log2(r + 1), log2(r + 1) - (167 + (lgC_ent - rho * 167))))
    emit("")

    # ---------- q_crit on the official candidate row ----------
    emit("---- D3 SECONDARY: q_crit on the official candidate row ----")
    emit("  official row admissibility [tools/prize_row_descriptor.py:16-84]:")
    emit("    q < 2^256, k <= 2^40, n = 2^subgroup_log2, rate in {1/2,...},")
    emit("    B*(q) = floor(q / 2^128).")
    emit("  first unresolved official rate-half candidate"
         " [split_pencil_equivalence/statement.md:44-46]: R = k = 2^40,")
    emit("    r = B*(q)-1 <= R/2, so B* in {2^39, 2^39+1} and"
         " q in [2^167, 2^167+2^129).   [crossing_location:62-64]")
    q_log = 167
    emit("  (A) razor-shape threshold applied at the official row's q:")
    emit("      theta_2 = %.6f ; log2 q = %d ; q > q_crit^(2) : %s ;"
         " margin = %.6f bits" % (theta2, q_log, q_log > theta2, q_log - theta2))
    emit("      => mu_2 = C(n,r)/q^{2rho} = 2^%+.6e  << 1 : the column-far"
         " random model is NOT void at the official row."
         % (lgC_ent - 2 * rho * q_log))
    emit("      theta_1 = %.6f ; q > q_crit^(1) : %s ; margin = %.6f bits"
         % (theta1, q_log > theta1, q_log - theta1))
    emit("      => mu_1 = 2^%+.6e << 1 : the KEY EQUATION is subcritical too."
         % (lgC_ent - rho * q_log))
    emit("  (B) the official row's OWN shape (r = B*-1 = 2^39-1, rho = R-r):")
    r_off = (1 << 39) - 1
    rho_off = R - r_off
    a_off = n - r_off
    h_off = H2(r_off / n)
    th2_off = n * h_off / (2 * rho_off)
    th1_off = n * h_off / rho_off
    emit("      r = %d, rho = %d, a = n-r = %d (= 3n/4 + 1 : %s)"
         % (r_off, rho_off, a_off, a_off == 3 * n // 4 + 1))
    emit("      H2(r/n) = %.9f ; n*H2 = %.4f" % (h_off, n * h_off))
    emit("      theta_2^own = %.6f ; theta_1^own = %.6f   <-- NOT ~2^64:"
         % (th2_off, th1_off))
    emit("      the '2^64' constant is a RAZOR-SHAPE constant (r/n = 63/128);")
    emit("      at the official row's own shape (r/n ~ 1/4) it collapses to"
         " ~2^%.2f." % th2_off)
    emit("      log2 mu_1^own at q=2^167 = %+.6e ; log2 mu_2^own = %+.6e"
         % (n * h_off - rho_off * q_log, n * h_off - 2 * rho_off * q_log))
    emit("  (C) two-field/two-row sanity: repeat at q = 2^167 + 2^129 - 1"
         " (top of the interval) and at the widened top q < 2^256:")
    for lq in (167, 255):
        emit("      log2 q = %d : razor-shape mu_2 = 2^%+.6e ; own-shape"
             " mu_2 = 2^%+.6e" % (lq, lgC_ent - 2 * rho * lq,
                                  n * h_off - 2 * rho_off * lq))
    emit("  VERDICT (q_crit): PASSES at every admissible official row, by"
         " >= %.4f bits on the razor-shape threshold and >= %.4f bits on the"
         " row's own threshold." % (128 - theta2, 128 - th2_off))
    emit("")

    # ---------- the B* comparison ----------
    emit("---- the budget comparison that actually binds ----")
    for lq in (167, 168, 200, 255):
        Bstar = (1 << lq) >> 128
        emit("  q=2^%-4d: B* = floor(q/2^128) = 2^%d = %d ; LB1 floor r+1 ="
             " %d ; LB1 <= B* ? %s" % (lq, lq - 128, Bstar, r + 1, r + 1 <= Bstar))
    emit("  crossover: r+1 <= floor(q/2^128) needs log2 q >= 128 + log2(r+1)"
         " = %.6f" % (128 + log2(r + 1)))
    emit("  banked: 'B_ca^far(k+2^34) >= 1,082,331,758,593 = 2^39.9773 -- 88.02"
         " bits below the 2^128 budget' [crossing_location:654-656]")
    emit("  reproduced here: r+1 = %d = 2^%.4f ; 128 - %.4f = %.2f bits"
         % (r + 1, log2(r + 1), log2(r + 1), 128 - log2(r + 1)))
    with open("notes/pilots_20260811/r35_fg_razor/e3_results.txt", "w") as fh:
        fh.write("\n".join(OUT) + "\n")


main()
