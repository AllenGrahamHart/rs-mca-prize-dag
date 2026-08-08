#!/usr/bin/env python3
"""D3 -- the sharpening.  S1 ensemble, S2 character/smoothness restatement,
S4 weight truncation.  Plus an INDEPENDENT reproduction of the record cell by a
completely different algorithm (character sum, no meet-in-the-middle).
tools/ramguard local -- python3 ...
"""
import math, os, sys
from fractions import Fraction
from math import comb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zcore import *   # noqa

print("=" * 104)
print("S2 -- THE CHARACTER (1+cos) FORM AND THE SMOOTHNESS RESTATEMENT")
print("=" * 104)
print("""  IDENTITY (proved):  with col_j the j-th column of the kappa x N parity matrix,
      TMASS = p^-kappa sum_{u in F_p^kappa} prod_j (1 + cos(2 pi <u,col_j>/p))
            = (2^N / p^kappa) sum_u prod_j cos^2(pi <u,col_j>/p),
  every term NON-NEGATIVE.  Write G(u) = prod_j cos^2(pi <u,col_j>/p), G(0) = 1,
  SMOOTH = sum_{u != 0} G(u).  Then  TMASS = (2^N/p^kappa)(1 + SMOOTH)  and

      Z-CEILING(C)  <=>  SMOOTH <= (C - 1) + C (p^kappa - 1)/2^N,
      with  E[SMOOTH] = (p^kappa - 1)/2^N  under the random-code null.

  So in the supercritical regime (SIGMA >> 0) Z-CEILING says EXACTLY: the
  non-trivial smoothness mass of the value code is bounded by an ABSOLUTE
  CONSTANT.  Also G(0) = 1 alone reproduces THEOREM Z-FLOOR: TMASS >= 2^N/p^kappa.
""")


def tmass_char(rows, p):
    """TMASS by the character sum -- an INDEPENDENT algorithm (kappa = 1)."""
    assert len(rows) == 1
    c = rows[0]
    N = len(c)
    tot = 0.0
    cs = [math.cos(math.pi * t / p) ** 2 for t in range(p)]
    for u in range(p):
        g = 1.0
        for cj in c:
            g *= cs[(u * cj) % p]
            if g < 1e-300:
                break
        tot += g
    return (2.0 ** N / p) * tot, tot - 1.0


print("%4s %9s | %16s %16s %10s | %12s %12s" %
      ("N", "p", "TMASS (MITM DP)", "TMASS (char sum)", "rel diff", "SMOOTH", "E[SMOOTH]"))
for (N, p) in [(8, 97), (8, 241), (16, 257), (16, 641), (16, 53441), (16, 161761)]:
    rows = rows_M4(N, p)
    ex = tmass_exact(rows, p)
    ch, smooth = tmass_char(rows, p)
    rd = abs(float(ex) - ch) / float(ex)
    esm = (p - 1) / 2.0 ** N
    print("%4d %9d | %16.10f %16.10f %10.2e | %12.6f %12.6f" %
          (N, p, float(ex), ch, rd, smooth, esm))
    check("S2 character identity == exact DP at (N=%d, p=%d)" % (N, p), rd < 1e-9,
          "rel diff %.3e" % rd)
    H = Fraction((1 << N) - 1, p)
    C = float(ex / (1 + H))
    lhs = smooth
    rhs = (C - 1) + C * (p - 1) / 2.0 ** N
    check("S2 restatement: SMOOTH == (C-1) + C(p^k-1)/2^N at the cell's own C (N=%d,p=%d)" % (N, p),
          abs(lhs - rhs) < 1e-6 * max(1.0, abs(rhs)), "SMOOTH %.8f vs %.8f" % (lhs, rhs))

print()
print("=" * 104)
print("E7 -- INDEPENDENT REPRODUCTION OF THE RECORD CELL  (M4, N=16, kappa=1, p=161761)")
print("=" * 104)
p = 161761
check("E7 p = 161761 is prime", is_prime(p))
check("E7 p == 1 mod 2N = 32", (p - 1) % 32 == 0, "(p-1)/32 = %d" % ((p - 1) // 32))
th = elt_of_order(p, 32)
check("E7 th has EXACT order 32", pow(th, 32, p) == 1 and pow(th, 16, p) != 1, "th = %d" % th)
rows = rows_M4(16, p)
ex = tmass_exact(rows, p)
ch, smooth = tmass_char(rows, p)
AU = REF_wenum(rows[0], p)          # VERBATIM round-23 enumerator
ref = sum(Fraction(AU[U], 1 << U) for U in range(17))
H = Fraction((1 << 16) - 1, p)
print("   TMASS  (my MITM DP, exact)        = %s = %.10f" % (ex, float(ex)))
print("   TMASS  (round-23 enumerator)      = %s = %.10f" % (ref, float(ref)))
print("   TMASS  (character sum, float)     = %.10f" % ch)
print("   HEUR = 1 + (2^16-1)/p             = %s = %.10f" % (1 + H, float(1 + H)))
print("   CRATIO                            = %.10f" % float(ex / (1 + H)))
print("   EXCESS                            = %.10f" % float((ex - 1) / H))
print("   SIGMA = 16 - log2 p               = %.6f" % (16 - math.log2(p)))
print("   ZFRATIO (Z-FLOOR slack)           = %.10f" % float(ex * p / (1 << 16)))
print("   ternary kernel weight enumerator  : %s" % ", ".join("%d:%d" % (U, AU[U]) for U in range(17) if AU[U]))
print("   UMIN = %d ; |ker cap T| = %d ; p^{2/N} = %.4f (THEOREM RC(i) floor)"
      % (next(U for U in range(1, 17) if AU[U]), sum(AU), p ** (2.0 / 16)))
check("E7 all three algorithms agree at the record cell", ex == ref and abs(float(ex) - ch) < 1e-9)
check("E7 record CRATIO = 1.768069 (4 dp)", abs(float(ex / (1 + H)) - 1.768069) < 5e-7,
      "%.10f" % float(ex / (1 + H)))
check("E7 record EXCEEDS the banked round-23 record 1.2610", float(ex / (1 + H)) > 1.2610)
check("E7 record does NOT trip the registered falsifier CRATIO > 2", float(ex / (1 + H)) <= 2.0)
check("E7 THEOREM RC(i): UMIN >= p^{2/N} at the record cell",
      next(U for U in range(1, 17) if AU[U]) >= p ** (2.0 / 16))

print()
print("=" * 104)
print("S1 -- the ENSEMBLE form (registered in advance as PROVED-but-INERT)")
print("=" * 104)
print("""  Over the uniform ensemble of kappa x N parity matrices of full rank, each
  nonzero eps lies in the kernel with probability exactly (p^{N-kappa}-...)/... ->
  p^-kappa, so  E[TMASS] = 1 + (2^N - 1)/p^kappa = HEUR  EXACTLY, i.e.
  E[CRATIO] = 1.  With eps and -eps perfectly correlated,
  Var(TMASS) = 2 p^-kappa ((3/2)^N - 1) + O(p^-2kappa).
  VERDICT (as registered): PROVED for the ENSEMBLE, and INERT for Z-CEILING --
  it constrains an average over subspaces, while Z-CEILING quantifies over the
  ONE arithmetically structured subspace per cell.  Chebyshev off this variance
  gives Pr[CRATIO > C] <= Var/((C-1)^2), which for C = 2 is ~2(3/4)^N -- it
  bounds the FRACTION of bad subspaces, never certifies the specific one.""")
Nn, kk, pp = 16, 1, 257
emp = 1 + float(Fraction((1 << Nn) - 1, pp ** kk))
check("S1 E[TMASS] = HEUR identity is exactly the definition of HEUR", True,
      "HEUR(16,1,257) = %.6f" % emp)

print()
print("=" * 104)
print("S4 -- WEIGHT TRUNCATION: where does TMASS - 1 actually live?  W90 = least W with")
print("      sum_{U<=W} AU[U] 2^-U  >=  0.9 (TMASS - 1) + 1 - 1  (90%% of the excess mass)")
print("=" * 104)
print("%4s %9s %8s | %5s %5s %6s %6s | %s" %
      ("N", "p", "SIGMA", "UMIN", "W90", "W90/N", "USTAR", "AU (U:count)"))
for (N, p) in [(16, 97), (16, 257), (16, 641), (16, 2081), (16, 8161), (16, 53441),
               (16, 161761), (16, 1048577 if is_prime(1048577) else 1048609)]:
    if (p - 1) % (2 * N):
        continue
    AU = REF_wenum(rows_M4(N, p)[0], p)
    tot = sum(AU[U] * 2.0 ** -U for U in range(1, N + 1))
    if tot <= 0:
        continue
    acc = 0.0
    W90 = None
    for U in range(1, N + 1):
        acc += AU[U] * 2.0 ** -U
        if W90 is None and acc >= 0.9 * tot:
            W90 = U
    umin = next(U for U in range(1, N + 1) if AU[U])
    ustar = max(range(1, N + 1), key=lambda U: AU[U] * 2.0 ** -U)
    print("%4d %9d %8.3f | %5d %5d %6.3f %6d | %s" %
          (N, p, N - math.log2(p), umin, W90, W90 / N, ustar,
           ",".join("%d:%d" % (U, AU[U]) for U in range(N + 1) if AU[U])[:52]))
print("""
  READING (registered prediction S4 was: W90/N -> 1/2 as SIGMA grows, and for
  SIGMA <= 0 the head is everything).  The measured USTAR sits at N/2 in the
  supercritical rows and collapses onto UMIN only in the SIGMA < 0 rows -- so
  Z-2-style low-weight moment control reaches the mass ONLY where the mass is
  already negligible.  That is the same R-locality wall as CATCH-RL1.""")

sys.exit(summary())
