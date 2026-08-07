#!/usr/bin/env python3
"""Independent checks of gelib's exact arithmetic before any measurement."""
import itertools
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from gelib import (tower_norm, centers, sigma, pgcd, plcm, pdivides,
                   mult_order, spf_sieve, factor_with, is_pow2)


def brute_norm(v):
    """Norm via the multiplication-matrix determinant (Bareiss), independent
    of the tower recursion -- this is round-21's exact_norm, reimplemented."""
    n = len(v)
    mat = [[0] * n for _ in range(n)]
    for j in range(n):
        for i in range(n):
            s = i + j
            if s < n:
                mat[s][j] += v[i]
            else:
                mat[s - n][j] -= v[i]
    m = [r[:] for r in mat]
    sign, prev = 1, 1
    for k in range(n - 1):
        if m[k][k] == 0:
            piv = None
            for r in range(k + 1, n):
                if m[r][k] != 0:
                    piv = r
                    break
            if piv is None:
                return 0
            m[k], m[piv] = m[piv], m[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                m[i][j] = (m[i][j] * m[k][k] - m[i][k] * m[k][j]) // prev
        prev = m[k][k]
    return sign * m[n - 1][n - 1]


ok = True

# 1. tower_norm vs the independent Bareiss determinant, full box at h=2,4
for h in (2, 4):
    for v in itertools.product((-2, -1, 0, 1, 2), repeat=h):
        a, b = tower_norm(list(v)), brute_norm(list(v))
        if a != b:
            print("NORM MISMATCH", h, v, a, b)
            ok = False
print("[1] tower_norm == Bareiss determinant on the FULL box at h=2,4:", ok)

# 1b. spot checks at h=8 against Bareiss
import random
random.seed(7)
bad = 0
for _ in range(300):
    v = [random.randint(-2, 2) for _ in range(8)]
    if tower_norm(v) != brute_norm(v):
        bad += 1
print("[1b] h=8, 300 random box vectors, mismatches:", bad)
ok = ok and bad == 0

# 2. known algebraic values
checks = [
    ([1, 1, 0, 0], 2, "Norm(1+zeta_8) = Phi_8(-1) = 2"),
    ([1, 1, 0, 0, 0, 0, 0, 0], 2, "Norm(1+zeta_16) = Phi_16(-1) = 2"),
    ([2] + [0] * 3, 16, "Norm(2) = 2^4 at h=4"),
    ([2] + [0] * 7, 256, "Norm(2) = 2^8 at h=8"),
    ([1, 0, 0, 0], 1, "Norm(1) = 1"),
    ([-1, 1, 0, 0], 2, "Norm(zeta_8 - 1) = 2"),
]
for v, want, why in checks:
    got = tower_norm(list(v))
    if got != want:
        print("  FAIL", why, "got", got)
        ok = False
print("[2] algebraic spot values:", ok)

# 3. |C(N')| = (3^h+1)/2
for h in (2, 3, 4, 8):
    n = len(centers(h))
    want = (3 ** h + 1) // 2
    if n != want:
        print("  FAIL |C| at h=%d: %d vs %d" % (h, n, want))
        ok = False
print("[3] |C(N')| = (3^h+1)/2 at h=2,3,4,8:", ok)

# 4. sigma/lcm/divides sanity + the residue-degree invariant deg(sigma) % f == 0
spf = spf_sieve(1 << 20)
h = 4
bad = 0
for v in itertools.product((-2, -1, 0, 1, 2), repeat=h):
    if not any(v):
        continue
    nm = abs(tower_norm(list(v)))
    o = nm
    while o % 2 == 0:
        o //= 2
    for p in factor_with(spf, o):
        f = mult_order(p, 2 * h)
        s = sigma(v, p, h)
        if len(s) == 1:
            bad += 1            # gcd trivial but p | Norm -> impossible
        if (len(s) - 1) % f:
            bad += 1
print("[4] h=4: every odd p | Norm(d) yields deg(sigma) a positive multiple "
      "of f_p; violations:", bad)
ok = ok and bad == 0

# 5. lcm / divides
p = 17
h = 4
a = sigma([1, 1, 0, 0], p, h)
b = sigma([-1, 1, 0, 0], p, h)
l = plcm(a, b, p)
print("[5] lcm/divides:", pdivides(a, l, p) and pdivides(b, l, p))
ok = ok and pdivides(a, l, p) and pdivides(b, l, p)

print("SELFTEST", "PASS" if ok else "FAIL")
