#!/usr/bin/env python3
"""D3 - is there an obstruction ABOVE the conductor?

(1) SURJECTIVITY TEST.  Local CFT for K_2 = Q_2(zeta_128)/Q_2 (totally
    ramified, degree 64) gives N(K_2^*) = <2> x (1 + 128 Z_2), hence
    N(K_2^*) cap Z_2^* = 1 + 128 Z_2 EXACTLY and SURJECTIVELY.  If that is
    right, box norms must hit EVERY residue class of 1 + 128 Z_2 mod 2^M,
    uniformly.  Chi-square tested at M = 14 (128 classes) and M = 17.
(2) ORBIT VERIFICATION.  |{+-x^j sigma_a(w)}| = 2h^2 = 8192 and all have the
    same Norm -- the divisor that converts a per-vector hit rate into a count
    of DISTINCT bad primes.
(3) The nodd=1 TENSION CURVE: max attainable LOGNORM subject to
    v_2(Norm-1) >= L, measured by placing k zeros.
"""
import random
import sys
from collections import Counter
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K  # noqa: E402

H = 64
rng = random.Random(20260809)


def v2(n):
    return (n & -n).bit_length() - 1


# ---------------------------------------------------- (1) surjectivity
print("(1) box norms mod 2^M, restricted to the predicted image 1 + 128 Z_2")
for M in (14, 17):
    cnt = Counter()
    tot = 0
    NS = 30000
    for _ in range(NS):
        w = K.fam_C(H, rng, 3)
        n = abs(K.tower_norm(w))
        if n % 2 == 0:
            continue
        tot += 1
        cnt[n % (1 << M)] += 1
    classes = 1 << (M - 7)
    seen = len(cnt)
    outside = sum(v for k, v in cnt.items() if k % 128 != 1)
    exp = tot / classes
    chi2 = sum((cnt.get(1 + 128 * i, 0) - exp) ** 2 / exp for i in range(classes))
    print("   M=%2d: %d classes in 1+128Z_2, %d hit, %d norms outside the image, "
          "chi2 = %.1f (df %d, exp %.1f/class)"
          % (M, classes, seen, outside, chi2, classes - 1, exp))

# ------------------------------------------------------- (2) orbit 2h^2
print("\n(2) orbit verification (2h^2 = %d)" % (2 * H * H))
w0 = K.fam_B(H, rng)
n0 = abs(K.tower_norm(w0))
orb = set()
badn = 0
for a in range(1, 2 * H, 2):            # Galois: x -> x^a, a odd mod 2h
    wa = [0] * H
    for i in range(H):
        t = (a * i) % (2 * H)
        if t < H:
            wa[t] += w0[i]
        else:
            wa[t - H] -= w0[i]
    for s in (1, -1):
        for j in range(H):
            wj = [0] * H
            for i in range(H):
                t = i + j
                if t < H:
                    wj[t] += s * wa[i]
                else:
                    wj[t - H] -= s * wa[i]
            orb.add(tuple(wj))
            if abs(K.tower_norm(wj)) != n0:
                badn += 1
print("   distinct vectors in the orbit: %d ; norm mismatches: %d" % (len(orb), badn))

# ------------------------------------------- (3) nodd = 1 tension curve
print("\n(3) nodd=1 with k zeros: v_2(Norm-1) reach vs LOGNORM cost")
print("    k   S     med LOGNORM   max v_2(Norm-1)   v_2 histogram")
for k in (0, 1, 2, 3, 4, 6, 8, 12, 16):
    best = 0
    lg = []
    hist = Counter()
    for _ in range(1200):
        j = rng.randrange(H)
        w = [rng.choice((-2, 2)) for _ in range(H)]
        w[j] = rng.choice((-1, 1))
        for z in rng.sample([i for i in range(H) if i != j], k):
            w[z] = 0
        n = abs(K.tower_norm(w))
        if n % 2 == 0 or n == 0:
            continue
        g = v2(n - 1)
        hist[g] += 1
        best = max(best, g)
        lg.append(n.bit_length())
    lg.sort()
    S = 4 * (H - 1 - k) + 1
    print("   %2d  %4d   %6d        %3d            %s"
          % (k, S, lg[len(lg) // 2], best, dict(sorted(hist.items()))))
