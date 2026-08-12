#!/usr/bin/env python3
"""Independent audit path (coordinator, 2026-08-12): from-scratch replay
of the PR #1163 cancellation adapter on a self-built F_17 record, plus a
second-method recomputation of the walls.

The record is NOT the upstream packet's GF(17) atom. It is built here
via the converse embedding with different parameters:
(n,k,m) = (17,4,6), core C = {1,2} (c=2), slopes {3,5}, quadratic
shortened receive words (r'_1 = x^2 on each shortened maximal support,
so no affine pair explains any size-4 subset). All operative theorem
clauses are then checked on the ORIGINAL row by brute force:

  (a) maximal agreement supports and their intersection = C, c < k;
  (b) the degree-<c interpolants of r_j on C;
  (c) exact division by G_C: quotient degrees and pointwise match;
  (d) shortened maximal supports = S_hat_i minus C;
  (e) noncontainment in BOTH rows for EVERY size-(m-c) witness subset
      (exhaustive: C(5,4) per support per slope);
  (f) the parameter and two-cover-complexity identities.

Walls are recomputed by a different method than verify.py: the interface
wall by a windowed ceiling scan, the J boundary by pure-integer
cross-multiplication (no Fraction).

RAMGUARD_TIMEOUT: `tools/ramguard tiny -- python3 ...` (seconds).
"""

from itertools import combinations
from math import comb

P = 17
DFULL = list(range(P))
N, K, M, CSIZE = 17, 4, 6, 2
CORE = (1, 2)
DPRIME = [x for x in DFULL if x not in CORE]
GAMMAS = (3, 5)
A0 = (3, 1)   # a_0(X) = 3 + X
A1 = (1, 2)   # a_1(X) = 1 + 2X
A_SET1 = (4, 5, 6, 7, 13)     # shortened maximal support, slope 3
A_SET2 = (8, 9, 10, 11, 12)   # shortened maximal support, slope 5
H_PRIME = {3: (0,), 5: (1,)}  # shortened explanations, deg < k-c = 2


def ev(coeffs, x):
    acc = 0
    for co in reversed(coeffs):
        acc = (acc * x + co) % P
    return acc


def g_c(x):
    out = 1
    for r in CORE:
        out = out * (x - r) % P
    return out


def r_prime(x):
    x2 = x * x % P
    if x in A_SET1:
        return (-3 * x2) % P, x2
    if x in A_SET2:
        return (1 - 5 * x2) % P, x2
    return 2, 3


def r_orig(x):
    if x in CORE:
        return ev(A0, x), ev(A1, x)
    r0p, r1p = r_prime(x)
    g = g_c(x)
    return (ev(A0, x) + g * r0p) % P, (ev(A1, x) + g * r1p) % P


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] = (out[i + j] + ai * bj) % P
    return tuple(out)


def poly_add(a, b):
    ln = max(len(a), len(b))
    return tuple(((a[i] if i < len(a) else 0)
                  + (b[i] if i < len(b) else 0)) % P for i in range(ln))


G_POLY = poly_mul((-CORE[0] % P, 1), (-CORE[1] % P, 1))

H_ORIG = {}
for gs, hp in H_PRIME.items():
    base = poly_add(A0, tuple(gs * t % P for t in A1))
    H_ORIG[gs] = poly_add(base, poly_mul(G_POLY, hp))
    assert len(H_ORIG[gs]) <= K  # deg < k

# (a) maximal supports and their intersection
S_HAT = {}
for gs in GAMMAS:
    S_HAT[gs] = {x for x in DFULL
                 if ev(H_ORIG[gs], x)
                 == (r_orig(x)[0] + gs * r_orig(x)[1]) % P}
assert S_HAT[3] == set(A_SET1) | set(CORE)
assert S_HAT[5] == set(A_SET2) | set(CORE)
CO = S_HAT[3] & S_HAT[5]
assert CO == set(CORE)
assert len(CO) < K

# (b) the deg-<c interpolants of r_j on C are exactly a_0, a_1
for aj, idx in ((A0, 0), (A1, 1)):
    x0, x1 = CORE
    y0, y1 = r_orig(x0)[idx], r_orig(x1)[idx]
    slope = (y1 - y0) * pow(x1 - x0, P - 2, P) % P
    const = (y0 - slope * x0) % P
    assert (const, slope) == aj


# (c) exact division by G_C
def divmod_by_g(h):
    h = list(h) + [0] * (3 - len(h))
    q = [0] * max(1, len(h) - 2)
    for i in range(len(h) - 1, 1, -1):
        f = h[i]
        if f:
            q[i - 2] = f
            for j, gc in enumerate(G_POLY):
                h[i - 2 + j] = (h[i - 2 + j] - f * gc) % P
    return tuple(q), tuple(h[:2])


for gs in GAMMAS:
    base = poly_add(A0, tuple(gs * t % P for t in A1))
    num = poly_add(H_ORIG[gs], tuple(-t % P for t in base))
    quo, rem = divmod_by_g(num)
    assert rem == (0, 0)
    padded = H_PRIME[gs] + (0,) * (len(quo) - len(H_PRIME[gs]))
    assert quo == padded
    assert all(t == 0 for t in quo[K - CSIZE:])  # deg < k-c

for x in DPRIME:
    r0, r1 = r_orig(x)
    ginv = pow(g_c(x), P - 2, P)
    assert ((r0 - ev(A0, x)) * ginv % P,
            (r1 - ev(A1, x)) * ginv % P) == r_prime(x)

# (d) shortened maximal supports
for gs, aset in ((3, A_SET1), (5, A_SET2)):
    sup = {x for x in DPRIME
           if ev(H_PRIME[gs], x)
           == (r_prime(x)[0] + gs * r_prime(x)[1]) % P}
    assert sup == set(aset) == S_HAT[gs] - set(CORE)


# (e) noncontainment, both rows, every witness subset
def explained(points, values, kdeg):
    rows = [[pow(x, dd, P) for dd in range(kdeg)] + [val % P]
            for x, val in zip(points, values)]
    r = 0
    for cc in range(kdeg + 1):
        piv = next((rr for rr in range(r, len(rows))
                    if rows[rr][cc] % P), None)
        if piv is None:
            continue
        if cc == kdeg:
            return False
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = pow(rows[r][cc], P - 2, P)
        rows[r] = [(v * inv) % P for v in rows[r]]
        for rr in range(len(rows)):
            if rr != r and rows[rr][cc]:
                f = rows[rr][cc]
                rows[rr] = [(a - f * b) % P
                            for a, b in zip(rows[rr], rows[r])]
        r += 1
    return True


def contained(support, kdeg, word_fn):
    return (explained(support, [word_fn(x)[0] for x in support], kdeg)
            and explained(support, [word_fn(x)[1] for x in support], kdeg))


checked = 0
for gs, aset in ((3, A_SET1), (5, A_SET2)):
    for tp in combinations(aset, M - CSIZE):
        assert not contained(tp, K - CSIZE, r_prime)
        assert not contained(tuple(CORE) + tp, K, r_orig)
        checked += 1
assert checked == 2 * comb(len(A_SET1), M - CSIZE)

# (f) parameter and two-cover identities
NP, KP, MP = N - CSIZE, K - CSIZE, M - CSIZE
assert (MP - KP, NP - KP, NP - MP) == (M - K, N - K, N - M)
assert 3 * M - K + 3 == (3 * MP - KP + 3) + 2 * CSIZE

# ---- second-method wall recomputation at the official row ----
NB, KB, MB = 2097152, 1048576, 1116048
B_STAR = 274980728111395087
for c in range(4125, 4138):
    floor_ge_18 = (32 * (MB - c) + (NB - c) - 1) // (NB - c) >= 18
    assert floor_ge_18 == (c <= 4130)


def j_exact(s):
    num = den = 1
    for i in range(s + 1):
        num *= (NB - KB) + i
        den *= (MB - KB) + i
    return num // den


assert j_exact(13) == 47876303026096432
assert j_exact(14) == 743896698428332665
assert j_exact(13) < B_STAR < j_exact(14)

print("KB_COMMON_CORE_ADAPTER_AUDIT_OK",
      "toy=(17,4,6)->(15,2,4)", "witness_subsets_checked=", checked)
