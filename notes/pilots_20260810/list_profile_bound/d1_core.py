#!/usr/bin/env python3
"""d1_core.py -- list_profile_bound (round 29), exact arithmetic core.

Every functional named in PREREG R0.  Integers exact; only the final
log2 displays use floats.  No mean-model quantity is computed here
(F3 zero-power declaration).
"""
from fractions import Fraction
import math

n = 2 ** 41
k = 2 ** 40
R = n - k
SIG = 2 ** 34


def lg(x):
    if isinstance(x, Fraction):
        return math.log2(x.numerator) - math.log2(x.denominator)
    return math.log2(x)


print("=" * 72)
print("PARAMETERS   n=2^41=%d  k=2^40=%d  R=n-k=%d" % (n, k, R))
print("=" * 72)

# ---------------------------------------------------------------- PRED-3
# DEFICIT(q): floor value M = L(q-n)/(q-n+kL) vs budget B* = floor(q/2^128).
# L is the (256,1) rung's count, banked as 2^242.6503 by round 28.
print()
print("--- PRED-3  DEFICIT(q) = log2( B_CAFAR_floor(k+2^34-1) / B*(q) ) ---")
L = 2 ** 242 * 3 // 2  # 2^242.585, a deliberate UNDER-estimate of 2^242.6503
L_exact_lo = L
for name, q in [("q ~ 2^167 (bracket bottom)", 2 ** 167 + 1),
                ("q ~ 2^200", 2 ** 200 + 1),
                ("q ~ 2^256 (razor top)", 2 ** 256 - 1)]:
    M = Fraction(L_exact_lo * (q - n), (q - n) + k * L_exact_lo)
    Bstar = q // 2 ** 128
    print("  %-28s log2 M = %10.4f   log2 B* = %10.4f   DEFICIT = %8.4f"
          % (name, lg(M), lg(Bstar), lg(M) - lg(Bstar)))
print("  saturation cap (q-n)/k -> DEFICIT -> 2^128/k = 2^%d, q-free"
      % (128 - 40))

# ---------------------------------------------------------------- PRED-4
print()
print("--- PRED-4  SIGMA_JOHN: least sigma with a^2/n > k-1 (Johnson entry) ---")
lo, hi = 0, k
while lo < hi:
    mid = (lo + hi) // 2
    a = k + mid
    if a * a > n * (k - 1):
        hi = mid
    else:
        lo = mid + 1
SIGMA_JOHN = lo
print("  SIGMA_JOHN = %d = 2^%.4f" % (SIGMA_JOHN, lg(SIGMA_JOHN)))
print("  SIGMA_JOHN / 2^34 = %.4f   (registered window [30,36])" % (SIGMA_JOHN / SIG))
print("  a_John / n = %.7f   (= 1/sqrt(2) at rate 1/2)" % ((k + SIGMA_JOHN) / n))

# ---------------------------------------------------------------- PRED-5
print()
print("--- PRED-5  F_JOHN(theta) at sigma = 2^34 (Fisher sub-stratum, T3) ---")
a = k + SIG
r = n - a
theta_star = Fraction(a * a, n)
print("  a = %d   r = %d" % (a, r))
print("  THETA_STAR = a^2/n = %s  (exact integer: %s)"
      % (theta_star, theta_star.denominator == 1))
print("           = 2^39 + 2^34 + 2^27 = %d  check %s"
      % (2 ** 39 + 2 ** 34 + 2 ** 27, theta_star == 2 ** 39 + 2 ** 34 + 2 ** 27))
for name, th in [("theta = n/4 = 2^39", n // 4),
                 ("theta = THETA_STAR - 1", int(theta_star) - 1)]:
    val = Fraction(a - th, theta_star - th)
    print("  %-24s F_JOHN = %s = %.4f -> floor %d"
          % (name, val, float(val), int(val)))
THETA_ALG = k - 1
GAP_FISHER = THETA_ALG - int(theta_star)
print("  THETA_ALG = k-1 = %d" % THETA_ALG)
print("  GAP_FISHER = THETA_ALG - THETA_STAR = %d = 2^%.4f"
      % (GAP_FISHER, lg(GAP_FISHER)))
print("  bracket span 3n/4 - (k+2^34) = %d" % (3 * n // 4 - a))
print("  GAP_FISHER / bracket span = %.6f" % (GAP_FISHER / (3 * n // 4 - a)))

# ------------------------------------------------------- PRED-6 / PRED-7
print()
print("--- PRED-6  GAMMA_ONELINE: least a with 3a-2n >= k (T4, one line) ---")
a_one = -(-(2 * n + k) // 3)          # ceil((2n+k)/3)
print("  a_oneline = ceil((2n+k)/3) = %d   a/n = %.7f" % (a_one, a_one / n))
print("  bound there: B_CAFAR <= n-a+1 = %d = 2^%.4f"
      % (n - a_one + 1, lg(n - a_one + 1)))
print("  sigma there = %d = 2^%.4f" % (a_one - k, lg(a_one - k)))
print("  registered PRED-6 value was 366,503,875,926 (n/6+1, non-integral n/6)")

print()
print("--- PRED-7  GAMMA_FISHLINE: least a with (2a-n)^2/a > k-1 ---")
lo, hi = n // 2 + 1, n
while lo < hi:
    mid = (lo + hi) // 2
    if (2 * mid - n) ** 2 > mid * (k - 1):
        hi = mid
    else:
        lo = mid + 1
a_fish = lo
print("  a_fishline = %d   a/n = %.7f" % (a_fish, a_fish / n))
print("  closed form (9+sqrt(17))/16 = %.7f" % ((9 + math.sqrt(17)) / 16))
print("  sigma there = %d = 2^%.4f" % (a_fish - k, lg(a_fish - k)))

print()
print("--- the three thresholds, as sigma ---")
print("  TARGET                       sigma = 2^34            = %d" % SIG)
print("  in-repo Hankel layer (a>3n/4) sigma = 2^39            = %d" % (3 * n // 4 - k))
print("  my T4 Fisher-line threshold   sigma = %d = 2^%.4f" % (a_fish - k, lg(a_fish - k)))
print("  my T4 one-line threshold      sigma = %d = 2^%.4f" % (a_one - k, lg(a_one - k)))
print("  gap target->Hankel: %d units = 2^%.4f, factor %.4f in sigma"
      % (3 * n // 4 - k - SIG, lg(3 * n // 4 - k - SIG), (3 * n // 4 - k) / SIG))

# ---------------------------------------------------------------- PRED-9
print()
print("--- PRED-9  UB_RIDER(2^34) = 1 + (r+1) L_2(2 sigma), (RR2)/(RR4) ---")
two_sig = 2 * SIG
print("  2*sigma = %d   k = %d   2*sigma/k = 2^%.1f" % (two_sig, k, lg(Fraction(two_sig, k))))
# L_2(e) >= q^{2(k-e)} : fix any common set S of size e; u,v free on the rest.
for qlog in (167, 256):
    lo_log2 = 2 * (k - two_sig) * qlog
    print("  log2 q = %3d :  L_2(2sigma) >= q^{2(k-2sigma)} = 2^%.4e" % (qlog, lo_log2))
    print("                  log2 UB_RIDER >= %.4e   (need <= 128)" % lo_log2)
print("  registered window for log2 UB_RIDER: [5e14, 6e14] at log2 q = 256")

# --------------------------------------------------------------- PRED-11
print()
print("--- PRED-11  decay -> c map (88 unsafe bits at the bracket bottom) ---")
for name, dec in [("family cliff        126.5240 b/u", 126.5240),
                  ("ratio transport, fastest 175.7440 b/u", 175.7440),
                  ("ratio transport, slowest  37.1456 b/u", 37.1456),
                  ("absolute transport   2.8074 b/u", 2.8074),
                  ("brief's slow figure  0.4074 b/u", 0.4074)]:
    print("  %-42s c = ceil(88/dec) = %d" % (name, math.ceil(88.0 / dec)))

# --------------------------------------------------------------- PRED-13
print()
print("--- PRED-13  falsifier power: (UB-far at c) vs (RH-AC-hi) ---")
span = 3 * n // 4 - (k + SIG) + 1
hi_rate = 114.6503 / span
print("  span (RH-AC-hi) must stay flat over : %d agreements" % span)
print("  (RH-AC-hi) allowed average decay    : %.6e bits/unit" % hi_rate)
for c in (0, 1, 32, 216, 1000):
    need = 88.0 / (c + 1)
    print("  (UB-far) at c=%-5d needs >= %10.4f bits/unit over %5d units"
          "   power ratio = 2^%.4f" % (c, need, c + 1, math.log2(need / hi_rate)))
print("  NESTING: (UB-far) at small c is a WEAKER demand than the negation of")
print("  (RH-AC-hi); refuting -hi does not supply (UB-far).")

# --------------------------------------------------------------- bracket
print()
print("--- D4  the unconditional bracket ---")
print("  F_LMAX(a) = 1 exactly when 2a-n > k-1, i.e. a >= %d = 3n/4"
      % (-(-(n + k - 1) // 2) + ((n + k - 1) % 2 == 0)))
a_triv = (n + k - 1) // 2 + 1
print("  least such a = %d ; 3n/4 = %d ; equal: %s"
      % (a_triv, 3 * n // 4, a_triv == 3 * n // 4))
print("  => c_uncond (from the PROVED bracket top) = %d" % (3 * n // 4 - k - SIG))
print("=" * 72)
