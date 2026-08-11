#!/usr/bin/env python3
"""e3_razor.py -- rh_moving_kernel (round 33): razor arithmetic for D1/D4."""
import math

N = 2 ** 41
k = 2 ** 40
R = N - k
a = k + 2 ** 34
r = N - a
rho = R - r
L = []


def emit(s):
    L.append(s)
    with open("notes/pilots_20260811/rh_moving_kernel/e3_razor_results.txt",
              "w") as fh:
        fh.write("\n".join(L) + "\n")


emit("N=%d k=%d R=%d a=%d r=%d rho=R-r=%d  (2^%.4f)"
     % (N, k, R, a, r, rho, math.log2(rho)))
emit("wide regime r > R/2 : %s   (r/R = %.9f)" % (r > R / 2, r / R))
emit("r+1-rho  = dim ker M(gamma) = %d  (2^%.6f)"
     % (r + 1 - rho, math.log2(r + 1 - rho)))
emit("r+1-2rho = generic dim K_0    = %d  (2^%.6f)"
     % (r + 1 - 2 * rho, math.log2(r + 1 - 2 * rho)))
emit("moving increment m = h_r - rho <= rho = %d = 2^%.1f"
     % (rho, math.log2(rho)))
emit("(r+1-rho)/rho = %.6f   [PR-2 window was [62.9,64.1]]"
     % ((r + 1 - rho) / rho))
p_gen = (R + 1) // 2
p_star = (2 * R - 1) // 3 + 1
emit("generic low apolar degree p_gen = floor((R+1)/2) = %d = 2^%.6f"
     % (p_gen, math.log2(p_gen)))
emit("generic minimal COMMON apolar degree p* = floor((2R-1)/3)+1 = %d "
     "= 2^%.6f" % (p_star, math.log2(p_star)))
emit("p* > p_gen at the razor (=> low generator MOVES generically): %s"
     % (p_star > p_gen))
emit("m_P = r+1-p_gen = %d = 2^%.6f  ;  m_Q = r+p_gen-R = %d = 2^%.6f"
     % (r + 1 - p_gen, math.log2(r + 1 - p_gen),
        r + p_gen - R, math.log2(r + p_gen - R)))
emit("round-32 naive test m_P > rho : %s  (ratio %.6f = 2^%.4f)"
     % (r + 1 - p_gen > rho, (r + 1 - p_gen) / rho,
        math.log2((r + 1 - p_gen) / rho)))
emit("Forney gap at the razor: shift-basis Z-degree sum >= m_P+m_Q = %d "
     "= 2^%.6f, but sum of minimal indices <= rho = 2^%.1f ; gap factor "
     "2^%.4f" % (r + 1 - rho, math.log2(r + 1 - rho), math.log2(rho),
                 math.log2((r + 1 - rho) / rho)))
emit("fixed-generator stratum bracket: rho < p = h_r <= 2rho, i.e. "
     "%d < p <= %d (2^%.1f .. 2^%.1f)" % (rho, 2 * rho, math.log2(rho),
                                          math.log2(2 * rho)))
emit("razor target B* = 2^128 = %d" % (2 ** 128))
emit("rho = 2^%.1f is %0.1f bits under 2^128" % (math.log2(rho),
                                                 128 - math.log2(rho)))
emit("2rho = 2^%.1f is %0.1f bits under 2^128"
     % (math.log2(2 * rho), 128 - math.log2(2 * rho)))
emit("banked unconditional far bound C(n,r): log2 = %.1f"
     % (math.lgamma(N + 1) / math.log(2) - math.lgamma(r + 1) / math.log(2)
        - math.lgamma(N - r + 1) / math.log(2)))
