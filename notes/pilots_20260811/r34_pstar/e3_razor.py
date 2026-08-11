"""r34_pstar E3: exact razor arithmetic for the p* question.

Razor shape (round 33 PR-5 / e3_razor): R = k = 2^40, rho = 2^34,
r = R - rho, r/R = 1 - 2^-6, rate-half so n = 2R = 2^41, q >= n.
Exact integers where exact; float logs (lgamma / binary entropy) only for
binomials that cannot be materialised, flagged as such.
Stdlib only.  Run under tools/ramguard.
"""
import sys, math
from fractions import Fraction


def h2(x):
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)


def main():
    out = open(sys.argv[1], "w")

    def emit(s):
        out.write(s + "\n")
        out.flush()
        print(s)

    R = 2 ** 40
    rho = 2 ** 34
    r = R - rho
    n = 2 * R
    k = R

    emit("# r34_pstar E3 -- exact razor arithmetic")
    emit("R  = %d = 2^40" % R)
    emit("rho= %d = 2^34" % rho)
    emit("r  = R-rho = %d ; r/R = %s = %.9f" % (r, Fraction(r, R), r / R))
    emit("n  = 2R = %d ; k = %d ; r/n = %s" % (n, k, Fraction(r, n)))
    emit("")
    emit("-- the three thresholds --")
    emit("FG bracket   : rho < p <= 2rho          2rho      = %d = 2^35" % (2 * rho))
    emit("lemma bracket: p* + p_gen <= R  <=>  p* <= R/2 :  R//2      = %d = 2^39"
         % (R // 2))
    emit("generic p*   : ceil(2R/3) = floor((2R-1)/3)+1  = %d"
         % ((2 * R - 1) // 3 + 1))
    emit("generic p_gen: floor((R+1)/2)                  = %d" % ((R + 1) // 2))
    emit("ratio (R/2)/(2rho) = %d   <-- the two brackets differ by this factor"
         % ((R // 2) // (2 * rho)))
    emit("brief's generic miss factor (2R/3 + R/2)/R = 7/6 = %.6f" % (7 / 6))
    emit("")
    emit("-- dimension count in Gr(2,R) (NAIVE COUNT, see caveat) --")
    emit("dim Gr(2,R) = 2R-4 = %d" % (2 * R - 4))
    for label, p in [("p = 2rho (top of FG)", 2 * rho),
                     ("p = R/2 (lemma)", R // 2),
                     ("p = ceil(2R/3) (generic)", (2 * R - 1) // 3 + 1)]:
        emit("  %-26s dim{p*<=p} = 3p-4 = %-16d codim = 2R-3p = %d"
             % (label, 3 * p - 4, 2 * R - 3 * p))
    emit("  codim{p*<=2rho} = 61*2^35 = %d ; check %s"
         % (61 * 2 ** 35, 61 * 2 ** 35 == 2 * R - 3 * (2 * rho)))
    emit("  #admissible FG degrees p in (rho,2rho] = %d = 2^34" % rho)
    emit("  F_q-point count of the FG locus ~ q^(3p-4) with p=2rho : "
         "exponent %d" % (3 * (2 * rho) - 4))
    emit("")
    emit("-- FG profile at p = 2rho --")
    emit("h_r      = p          = %d" % (2 * rho))
    emit("dim K_0  = r+1-2rho   = %d" % (r + 1 - 2 * rho))
    emit("m_P      = r+1-p      = %d" % (r + 1 - 2 * rho))
    emit("m_Q      = p-rho      = %d  (= rho, saturating m_Q <= rho)"
         % (2 * rho - rho))
    emit("m_P+m_Q  = r+1-rho    = %d" % (r + 1 - rho))
    emit("deg Q'   = R+1-p      = %d" % (R + 1 - 2 * rho))
    emit("")
    emit("-- EXPLICIT WITNESS A (non-squarefree P* = x^{2rho}) --")
    emit("y0_m = 1 iff m = 2rho-1 = %d ; y1_m = 1 iff m = rho-1 = %d ; else 0"
         % (2 * rho - 1, rho - 1))
    emit("K_0 = x^{2rho} F[x]_{<= r-2rho} , dim = %d ; every element has a "
         "repeated root => column-far unconditionally" % (r + 1 - 2 * rho))
    emit("")
    emit("-- EXPLICIT WITNESS B (squarefree P* = P1 P2) --")
    emit("P1 irreducible of degree rho = %d over F_q  (exists: #irred of "
         "degree d over F_q >= (q^d - 2q^(d/2))/d > 0)" % rho)
    emit("P2 any squarefree degree-rho poly coprime to P1")
    emit("y0 = impulse response of P1, y1 = impulse response of P2 (length R)")
    emit("K_0 = P1P2 F[x]_{<= r-2rho}, dim = %d ; P1 irreducible of degree "
         ">= 2 has no root in D => column-far unconditionally"
         % (r + 1 - 2 * rho))
    emit("")
    emit("-- first-moment parameters at the razor (float logs, flagged) --")
    Hr = h2(r / n)
    emit("log2 C(n,r) ~ n*H2(r/n) = %d * %.9f = %.6e  [float; r/n = 63/128 "
         "exactly]" % (n, Hr, n * Hr))
    for lq in (41, 48, 56, 64, 72):
        emit("  q = 2^%2d : log2 q^rho = %.6e ; log2 q^(2rho) = %.6e ; "
             "log2 mu1 = %.6e ; log2 mu2 = %.6e"
             % (lq, lq * rho, lq * 2 * rho, n * Hr - lq * rho,
                n * Hr - lq * 2 * rho))
    crit = n * Hr / (2 * rho)
    emit("  column-farness first-moment threshold: log2 q = n*H2(r/n)/(2rho) "
         "= %.6f  (q_crit ~ 2^%.4f)" % (crit, crit))
    emit("  mu1 = C(n,r)/q^rho   > 1  =>  first moment predicts EVERY slope "
         "bad (T = q) at q = 2^41.")
    emit("  mu2 = C(n,r)/q^(2rho)> 1  =>  first moment predicts NO column-far "
         "pencils at q = 2^41 -- REFUTED by witnesses A and B, which are "
         "column-far unconditionally.")
    Hp = h2((2 * rho) / n)
    emit("")
    emit("-- fraction of monic degree-2rho P* that are D-split squarefree --")
    emit("log2 C(n,2rho) ~ n*H2(2rho/n) = %.6e ; log2 q^(2rho) at q=2^41 = "
         "%.6e ; log2 fraction = %.6e"
         % (n * Hp, 41 * 2 * rho, n * Hp - 41 * 2 * rho))
    emit("  => almost every P* of degree 2rho is NOT D-split-squarefree, so "
         "on the low-p* locus column-farness is FREE, not an extra condition.")
    out.close()


if __name__ == "__main__":
    main()
