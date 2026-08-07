#!/usr/bin/env python3
"""D4 pricing spec: the cost of a COMPLETE radius-16 Fincke-Pohst enumeration
of the folded kernel lattice at the prize cell.

SUBTRACTION FIRST (hard law 5).  The observation "lambda_1 = 31.67 > 16 at
N' = 128" is ALREADY BANKED --
background/nodes/e1_folded_no_vector_certificate_256_payload/
PRO_W3_e1_density.md:49.  The repo also already rules the BKZ evidence
INCOMPLETE (status_ruling.md:12, falsification_report_20260726.md).  Nothing
below claims that observation as new.  What is priced here is the COMPLETE
enumeration that would turn INCOMPLETE into CERTIFIED, in the model validated
against exhaustive brute force at h = 4, 8 by d4_cone.py.

Model (standard): a BKZ-reduced basis with root Hermite factor delta obeys the
GSA  ||b*_i|| = delta^(n-1-2i) * det^(1/n).  A Fincke-Pohst enumeration of the
ball of radius R visits, at depth k (the last k coordinates),
    H_k = V_k(R) / prod_{i=n-k}^{n-1} ||b*_i||
nodes, and FPCOST ~ sum_k H_k.  V_k(R) = pi^(k/2) R^k / Gamma(k/2+1).
"""
import math
import sys


def lgamma_half(k):
    return math.lgamma(k / 2.0 + 1.0)


def log2V(k, R):
    return ((k / 2.0) * math.log(math.pi) + k * math.log(R)
            - lgamma_half(k)) / math.log(2.0)


def fpcost(n, logdet2, R, delta):
    """log2 of the FP node count under the GSA."""
    ld = math.log2(delta)
    dn = logdet2 / n
    tot = -1e18
    peak = (0, -1e18)
    for k in range(1, n + 1):
        # sum of log2||b*_i|| for i = n-k .. n-1
        s = sum((n - 1 - 2 * i) * ld + dn for i in range(n - k, n))
        hk = log2V(k, R) - s
        if hk > peak[1]:
            peak = (k, hk)
        tot = max(tot, hk) + math.log2(1 + 2 ** (min(tot, hk) - max(tot, hk)))
    return tot, peak


def main():
    print("== D4 PRICE: complete radius-R enumeration of Lambda_p ==")
    print("Lambda_p = {w in Z^h : w(zeta) = 0 mod p}, dim n = h, det = p.")
    print("Certification target: NO nonzero w with ||w||_inf <= 2, i.e. no")
    print("lattice vector of Euclidean norm <= R = 2*sqrt(h).\n")
    print("%-6s %-8s %-10s %-11s %-11s %-11s %-12s" %
          ("N'", "n=h", "log2 p", "R=2sqrt(h)", "det^(1/n)", "GH lambda_1",
           "R/lambda_1"))
    cells = [(8, 4, math.log2(137)), (16, 8, math.log2(463249)),
             (16, 8, math.log2(12289)), (128, 64, 250.0), (256, 128, 250.0)]
    for (N, n, lp) in cells:
        R = 2.0 * math.sqrt(n)
        dn = 2 ** (lp / n)
        gh = math.sqrt(n / (2 * math.pi * math.e)) * dn
        print("%-6d %-8d %-10.3f %-11.3f %-11.3f %-11.3f %-12.3f" %
              (N, n, lp, R, dn, gh, R / gh))
    print("\n(R/lambda_1 < 1 means the box sits STRICTLY INSIDE the shortest")
    print(" vector under the Gaussian heuristic -- emptiness is the generic")
    print(" truth, and enumeration is the tool that CERTIFIES it.)")

    print("\n-- FPCOST (log2 nodes) under the GSA, prize cell N'=128, "
          "n=64, log2 p=250, R=16 --")
    print("%-14s %-14s %-16s %-12s" %
          ("BKZ delta", "block ~beta", "log2 FPCOST", "peak depth k"))
    for (delta, beta) in [(1.0219, "LLL"), (1.0128, "20"), (1.0109, "30"),
                          (1.0094, "45"), (1.0084, "60"), (1.0060, "90+")]:
        c, pk = fpcost(64, 250.0, 16.0, delta)
        print("%-14.4f %-14s 2^%-14.2f %-12d" % (delta, beta, c, pk[0]))

    print("\n-- the same model VALIDATED against d4_cone.py's exact counts --")
    for (n, lp, R, meas, why) in [(8, math.log2(463249), 2 * math.sqrt(8), 25,
                                   "N'=16 p=463249 (measured 25 nodes)"),
                                  (8, math.log2(12289), 2 * math.sqrt(8), 373,
                                   "N'=16 p=12289 (measured 373 nodes)"),
                                  (4, math.log2(401), 2 * math.sqrt(4), 5,
                                   "N'=8 p=401 (measured 5 nodes)")]:
        c, pk = fpcost(n, lp, R, 1.0219)
        print("   %-38s model 2^%-6.2f = %-10.1f  measured %d"
              % (why, c, 2 ** c, meas))

    print("\n-- N'=256 cell (the banked open TARGET), n=128, R=2sqrt(128) --")
    for (delta, beta) in [(1.0219, "LLL"), (1.0094, "45"), (1.0060, "90+")]:
        c, pk = fpcost(128, 250.0, 2 * math.sqrt(128), delta)
        print("   delta=%.4f (beta~%s): log2 FPCOST = %.2f, peak depth %d"
              % (delta, beta, c, pk[0]))
    R = 2 * math.sqrt(128)
    gh = math.sqrt(128 / (2 * math.pi * math.e)) * 2 ** (250.0 / 128)
    print("   R = %.2f vs GH lambda_1 = %.2f -> R/lambda_1 = %.3f  "
          "(box OUTSIDE the shortest vector: witnesses are EXPECTED, which is "
          "exactly what PRO_W3 says)" % (R, gh, R / gh))


if __name__ == "__main__":
    main()
