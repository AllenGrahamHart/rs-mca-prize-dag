#!/usr/bin/env python3
"""Exact fixtures for the primitive Pade-pencil router."""


def trim(poly):
    out = poly[:]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(a, b, q):
    out = [0] * max(len(a), len(b))
    for i in range(len(out)):
        out[i] = ((a[i] if i < len(a) else 0)
                  + (b[i] if i < len(b) else 0)) % q
    return trim(out)


def scale(a, c, q):
    return trim([(c * x) % q for x in a])


def mul(a, b, q):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % q
    return trim(out)


def evaluate(a, x, q):
    out = 0
    for c in reversed(a):
        out = (out * x + c) % q
    return out


def roots(a, domain, q):
    return {x for x in domain if evaluate(a, x, q) == 0}


q = 17
H = [pow(3, i, q) for i in range(16)]
assert len(set(H)) == 16
checks = 0

# A nonzero determinant of degree at most 2d-2 cannot vanish on r' points.
d, rprime = 3, 9
U = ([1], [0, 1])
V = ([0, 1], [1])
det = add(mul(U[0], V[1], q), scale(mul(U[1], V[0], q), -1, q), q)
assert len(det) - 1 <= 2 * d - 2
assert len(roots(det, H, q)) <= len(det) - 1 < rprime
checks += 3

# Primitive multiplier normal form and forced roots.
P, Q = [1, 1], [0, 1]
G = H[2:4]
locator = mul([(-G[0]) % q, 1], [(-G[1]) % q, 1], q)
kernel = [(mul(locator, P, q), mul(locator, Q, q))]
forced = set.intersection(*(
    roots(A, H, q) & roots(B, H, q) for A, B in kernel
))
ell, d2, g = 1, 4, len(G)
assert forced == set(G)
assert ell + g == d2 - 1
assert len(kernel) <= d2 - ell - g
checks += 3

# The primitive law and affine-family cancellation.
f0, g0 = [2, 3], [5, 4]
tau1, tau2 = [1, 2, 1], [3, 1]
f1 = add(f0, mul(Q, tau1, q), q)
g1 = add(g0, scale(mul(P, tau1, q), -1, q), q)
f2 = add(f0, mul(Q, tau2, q), q)
g2 = add(g0, scale(mul(P, tau2, q), -1, q), q)
assert add(mul(P, f1, q), mul(Q, g1, q), q) == add(
    mul(P, f0, q), mul(Q, g0, q), q
)
assert add(mul(P, f2, q), mul(Q, g2, q), q) == add(
    mul(P, f0, q), mul(Q, g0, q), q
)
dtau = add(tau1, scale(tau2, -1, q), q)
assert len(roots(dtau, H, q)) <= len(dtau) - 1 <= 4 - ell - 1
checks += 3

# Official endpoint inequality r'>2d-2 at the largest allowed depth.
rows = (
    (2**41, 2**39, 2**33 + 1),
    (2**41, 2**38, 2**33 + 1),
    (2**41, 2**37, 2**32 + 1),
)
for n, k, h in rows:
    depth = h - 2
    assert n - k - depth > 2 * depth - 2
    assert n - k - 3 * h + 8 > 0
    checks += 2

# Heavy forced roots occupy only the upper third of the high band.
for h in range(5, 40):
    for depth in range((h + 1) // 2, h - 1):
        possible = 2 * (h - depth) <= depth - 2
        cutoff = 3 * depth >= 2 * h + 2
        assert possible == cutoff
        if possible:
            assert 3 * depth - 2 * h - 1 >= 1
        checks += 1

print(f"XR_DEFICIENT_WINDOW_PRIMITIVE_PADE_PENCIL_ROUTER_PASS checks={checks}")
