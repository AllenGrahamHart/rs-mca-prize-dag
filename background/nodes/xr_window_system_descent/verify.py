#!/usr/bin/env python3
"""Small exact checks for W, D, rank scope, and official liveness L."""

from itertools import combinations


def mul(a, b, q):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % q
    return out


def locator(points, q):
    out = [1]
    for x in points:
        out = mul(out, [-x % q, 1], q)
    return out


def cyclic(poly, n, q):
    out = [0] * n
    for i, x in enumerate(poly):
        out[i % n] = (out[i % n] + x) % q
    return out


def monic_divmod(poly, divisor, q):
    out = poly[:]
    while out and not out[-1]:
        out.pop()
    quotient = [0] * max(0, len(out) - len(divisor) + 1)
    while len(out) >= len(divisor):
        shift = len(out) - len(divisor)
        coeff = out[-1]
        quotient[shift] = coeff
        for i, x in enumerate(divisor):
            out[shift + i] = (out[shift + i] - coeff * x) % q
        while out and not out[-1]:
            out.pop()
    return quotient, out


def rank(rows, q):
    a = [row[:] for row in rows]
    r = 0
    for c in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        z = pow(a[r][c], q - 2, q)
        a[r] = [x * z % q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                z = a[i][c]
                a[i] = [(x - z * y) % q for x, y in zip(a[i], a[r])]
        r += 1
    return r


checks = 0

# W: direct interpolation on k+d points agrees with the top-window test.
q, n, k, d = 17, 8, 4, 2
H = [pow(2, i, q) for i in range(n)]  # 2 has order 8 mod 17
u = [3, 1, 4, 1, 5, 9, 2, 6]
for T in combinations(H, n - k - d):
    E = locator(T, q)
    rem = cyclic(mul(u, E, q), n, q)
    quotient, remainder = monic_divmod(rem, E, q)
    while quotient and not quotient[-1]:
        quotient.pop()
    assert not remainder
    assert (not any(rem[n - d:])) == (len(quotient) <= k)
    checks += 1

# D: a union of M-cosets has locator coefficients only in M-degrees.
M = 2
T = [H[0], H[4], H[1], H[5]]
E = locator(T, q)
assert all(not c for i, c in enumerate(E) if i % M)
checks += 1

# Rank scope: each matrix can have rank d while stacking identical systems
# still has rank d, not 2d.
rows = [[1, 0, 2], [0, 1, 3]]
assert rank(rows, 17) == 2
assert rank(rows + rows, 17) == 2
checks += 2

# L: all official sub-depth powers M>=2^21 are excluded at their largest
# admissible multiple d. Smaller scales are deliberately not called proved.
rows = (
    ("1/4", 2**41, 2**39, 2**33 + 1, 31),
    ("1/8", 2**41, 2**38, 2**33 + 1, 31),
    ("1/16", 2**41, 2**37, 2**32 + 1, 30),
)
for name, n, k, h, top_j in rows:
    for j in range(21, top_j + 1):
        M = 1 << j
        dmax = ((h - 2) // M) * M
        cap = (n - k - dmax) // (h - dmax)
        assert M > cap, (name, j, dmax, cap)
        checks += 1

print(f"XR_WINDOW_SYSTEM_DESCENT_ALL_PASS checks={checks}")
