#!/usr/bin/env python3
"""INDEPENDENT replay of maelcar #1147's (n=128, p=257) counterexample row.

Their note SS3 claims:  T_sm = 22476,  max K = 26,  max C_r = 5789.
That row exists ONLY in their C++ probe; it is in NO JSON certificate and no
Python auditor covers it.  This is a from-scratch reimplementation from their
NOTE's definitions, cross-checked on the (32,97) and (32,193) rows they DO
certify.

Method notes (all derived here, not copied):
  * smoothness is shift-invariant: under x -> x+s the roots scale by lambda,
    so (e1,e2,e3) -> (l e1, l^2 e2, l^3 e3), hence m,sigma,rho -> l m, l^2 s,
    l^3 r; rho != 0 and sigma^3-27rho^2 -> l^6(...) are both preserved.
  * the product cell (alpha-4y, beta-4y) is shift-INVARIANT (alpha -> alpha+4s,
    y -> y+s).  So every pair in a shift-orbit contributes the SAME 8 cells,
    and K(d,e) = (cell count over all pairs) / orbit_size.
  * Z/n is a cyclic 2-group, so any nontrivial stabiliser contains the unique
    involution s = n/2.  Testing s = n/2 alone detects all non-free orbits.
"""
import sys
from itertools import chain, combinations

import numpy as np


def root_of_order(p, n):
    for c in range(2, p):
        z = pow(c, (p - 1) // n, p)
        if pow(z, n, p) == 1 and pow(z, n // 2, p) != 1:
            return z
    raise AssertionError


def run(n, p, verbose=True):
    zeta = root_of_order(p, n)
    roots = np.array([pow(zeta, e, p) for e in range(n)], dtype=np.int64)

    total = 1
    for i in range(4):
        total = total * (n - i) // (i + 1)
    q = np.fromiter(chain.from_iterable(combinations(range(n), 4)),
                    dtype=np.uint8, count=4 * total).reshape(-1, 4)
    key = np.empty(total, dtype=np.int32)
    smooth = np.empty(total, dtype=bool)
    inv4, inv2, inv8 = pow(4, -1, p), pow(2, -1, p), pow(8, -1, p)

    step = 1 << 20
    for lo in range(0, total, step):          # chunked: keeps peak RAM low
        hi = min(lo + step, total)
        c = q[lo:hi].astype(np.int64)
        v0, v1, v2, v3 = (roots[c[:, i]] for i in range(4))
        e1 = (v0 + v1 + v2 + v3) % p
        e2 = (v0*v1 + v0*v2 + v0*v3 + v1*v2 + v1*v3 + v2*v3) % p
        e3 = (v0*v1*v2 + v0*v1*v3 + v0*v2*v3 + v1*v2*v3) % p
        key[lo:hi] = (e1 * p + e2) * p + e3
        m = e1 * inv4 % p
        sigma = (6 * m % p * m - e2) % p * inv2 % p
        m3 = m * m % p * m % p
        rho = (e3 - 4 * m3 + 4 * m % p * sigma) % p * inv8 % p
        sigma3 = sigma * sigma % p * sigma % p
        rho2 = rho * rho % p
        smooth[lo:hi] = (rho != 0) & ((sigma3 - 27 * rho2) % p != 0)
        del c, v0, v1, v2, v3, e1, e2, e3, m, sigma, m3, rho, sigma3, rho2

    order = np.argsort(key, kind="stable").astype(np.int32)
    ks = key[order]
    del key
    bnd = np.r_[True, ks[1:] != ks[:-1]]
    del ks
    starts = np.flatnonzero(bnd).astype(np.int32)
    del bnd
    lengths = np.diff(np.r_[starts, np.int32(total)]).astype(np.int32)
    keep = lengths >= 2
    starts, lengths = starts[keep], lengths[keep]
    del keep

    li_parts, ri_parts = [], []
    for L in np.unique(lengths):                 # vectorised per run-length
        s = starts[lengths == L]
        blk = order[s[:, None] + np.arange(L, dtype=np.int32)]
        for a, b in combinations(range(int(L)), 2):
            li_parts.append(blk[:, a])
            ri_parts.append(blk[:, b])
        del blk
    del starts, lengths, order
    li = np.concatenate(li_parts)
    ri = np.concatenate(ri_parts)
    del li_parts, ri_parts

    A, B = q[li], q[ri]
    disjoint = np.ones(len(A), dtype=bool)
    for i in range(4):
        for j in range(4):
            disjoint &= (A[:, i] != B[:, j])
    disjoint &= smooth[li]
    A = A[disjoint].astype(np.int16)
    B = B[disjoint].astype(np.int16)
    del li, ri, disjoint, q, smooth

    npairs = len(A)
    # free-orbit test: does shifting by n/2 map {A,B} to itself?
    h = n // 2
    As = np.sort((A + h) % n, axis=1)
    Bs = np.sort((B + h) % n, axis=1)
    fix = ((As == A).all(1) & (Bs == B).all(1)) | \
          ((As == B).all(1) & (Bs == A).all(1))
    nonfree = int(fix.sum())

    alpha = A.sum(1).astype(np.int32) % n
    beta = B.sum(1).astype(np.int32) % n
    counts = np.zeros(n * n, dtype=np.int64)
    for i in range(4):
        for (al, be, Y) in ((alpha, beta, B), (beta, alpha, A)):
            d = (al - 4 * Y[:, i].astype(np.int32)) % n
            e = (be - 4 * Y[:, i].astype(np.int32)) % n
            counts += np.bincount(d * n + e, minlength=n * n)

    orbit = n
    T_sm = npairs // orbit
    maxK = int(counts.max()) // orbit
    sumK = int(counts.sum()) // orbit
    cells = counts[counts > 0]

    if verbose:
        print(f"  n={n} p={p}")
        print(f"    smooth disjoint matched pairs : {npairs}")
        print(f"    non-free orbits detected      : {nonfree}"
              f"   {'(all orbits free)' if nonfree == 0 else '(!! adjust)'}")
        print(f"    T_sm = pairs/{orbit}            : {T_sm}"
              f"   exact-division={npairs % orbit == 0}")
        print(f"    sum K(d,e)                    : {sumK}"
              f"   == 8*T_sm? {sumK == 8 * T_sm}")
        print(f"    occupied cells                : {len(cells)}")
        print(f"    max K(d,e)                    : {maxK}")
    return T_sm, maxK, sumK


print("=== CONTROL ROWS (they certify these; our numbers must match) ===")
for n, p, eT, eK in ((32, 97, 9, 2), (32, 193, 1, 2)):
    T, K, _ = run(n, p)
    print(f"    -> expected T_sm={eT} maxK={eK} :"
          f" {'MATCH' if (T, K) == (eT, eK) else '**MISMATCH**'}\n")

print("=== TARGET ROW: their uncertified counterexample (n=128, p=257) ===")
T, K, S = run(128, 257)
print()
print(f"  their claim : T_sm = 22476,  max K = 26")
print(f"  our replay  : T_sm = {T},  max K = {K}")
print(f"  T_sm agrees : {T == 22476}")
print(f"  max K agrees: {K == 26}")
print(f"  K(d,e) <= 4 refuted by our own replay: {K > 4}")
print(f"  Paper-D smooth target T_sm <= n^2/2 = {128**2//2}: "
      f"{'HOLDS' if T <= 128**2//2 else 'FAILS (target itself false here)'}")
