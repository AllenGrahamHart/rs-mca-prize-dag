#!/usr/bin/env python3
"""A3 (complete form): the EXACT retained count for EVERY legal word at n=16.

The census retention of a candidate support S under word c is
    [for all x in S \\ first_k(S):  L_x(c) = 0]  and
    [for all x not in S:            L_x(c) != 0]
where L_x(c) = f_c(x) - U_c(x) is LINEAR in the petal-scalar vector c
(interpolation is linear in U, and U is linear in c).  So for each S the
set of words retaining S is an intersection of m = |S|-k hyperplanes in
P^{t-1}(F_q) minus the n-|S| forbidden hyperplanes.  Enumerating that set
per S and accumulating gives the retained count of EVERY word exactly.

t=4, q=97 -> 922,180 projective words; this is exhaustive, not a sample.
"""
from __future__ import annotations

import itertools
import numpy as np

P = 97
N = 16
K = 8
T = 4


def domain(p, n):
    for g in range(2, p):
        z = pow(g, (p - 1) // n, p)
        if pow(z, n, p) == 1 and pow(z, n // 2, p) != 1:
            xs = [1] * n
            for j in range(1, n):
                xs[j] = xs[j - 1] * z % p
            return xs
    raise RuntimeError


def layout(n):
    k, half = n // 2, n // 2
    nf = (k - 1) // 2
    core = []
    for j in range(nf):
        core += [j, j + half]
    core.append(nf)
    return core, nf + half, [(j, j + half) for j in range(nf + 1, half)]


xs = domain(P, N)
core, bg, petals = layout(N)
petal_points = [pt for pr in petals for pt in pr]
pidx = {pt: i for i, pr in enumerate(petals) for pt in pr}
LC = {}
for pt in range(N):
    v = 1
    for r in core:
        v = v * ((xs[pt] - xs[r]) % P) % P
    LC[pt] = v

# projective index encoding for c in F_97^4
OFF = [0, P ** 3, P ** 3 + P ** 2, P ** 3 + P ** 2 + P]
TOTAL = P ** 3 + P ** 2 + P + 1


def proj_index(cs):
    """cs: (M,4) int array of nonzero vectors -> canonical projective index."""
    cs = cs % P
    out = np.zeros(cs.shape[0], dtype=np.int64)
    done = np.zeros(cs.shape[0], dtype=bool)
    for lead in range(T):
        sel = (~done) & (cs[:, lead] != 0)
        if not sel.any():
            continue
        sub = cs[sel]
        inv = np.array([pow(int(v), P - 2, P) for v in sub[:, lead]],
                       dtype=np.int64)
        nrm = (sub * inv[:, None]) % P
        idx = np.full(sub.shape[0], OFF[lead], dtype=np.int64)
        for j in range(lead + 1, T):
            idx = idx * P + nrm[:, j]
        # correct the base offset (idx built by repeated *P from OFF[lead])
        idx = idx - OFF[lead] * (P ** (T - 1 - lead)) + OFF[lead]
        out[sel] = idx
        done |= sel
    return out


def nullspace(rows):
    """Basis of the nullspace of rows (list of length-T vectors) over F_P."""
    A = [r[:] for r in rows]
    m, piv = len(A), []
    r = 0
    for col in range(T):
        s = next((i for i in range(r, m) if A[i][col] % P), None)
        if s is None:
            continue
        A[r], A[s] = A[s], A[r]
        iv = pow(A[r][col] % P, P - 2, P)
        A[r] = [x * iv % P for x in A[r]]
        for i in range(m):
            if i != r and A[i][col] % P:
                f = A[i][col]
                A[i] = [(A[i][j] - f * A[r][j]) % P for j in range(T)]
        piv.append(col)
        r += 1
    free = [c for c in range(T) if c not in piv]
    basis = []
    for fc in free:
        v = [0] * T
        v[fc] = 1
        for i, col in enumerate(piv):
            v[col] = (-A[i][fc]) % P
        basis.append(v)
    return basis


def proj_points(dim):
    """All projective points of P^{dim-1}(F_P) as coefficient rows."""
    pts = []
    for lead in range(dim):
        for tail in itertools.product(range(P), repeat=dim - lead - 1):
            pts.append([0] * lead + [1] + list(tail))
    return np.array(pts, dtype=np.int64)


PP = {d: proj_points(d) for d in (1, 2, 3)}

counts = np.zeros(TOTAL, dtype=np.int32)
n_cand = 0
threshold = 2 * (len(petals) - 2)
for cc in range(0, 4):
    if len(core) - cc < threshold:
        continue
    for Kc in itertools.combinations(core, cc):
        for use_bg in (0, 1):
            for om in (1, 2, 3):
                if K + cc + use_bg - om < K + 1:
                    continue
                for O in itertools.combinations(petal_points, om):
                    if not any(sum(pt in O for pt in pr) == 1 for pr in petals):
                        continue
                    sup = [False] * N
                    for pt in petal_points:
                        sup[pt] = True
                    for pt in O:
                        sup[pt] = False
                    for pt in Kc:
                        sup[pt] = True
                    if use_bg:
                        sup[bg] = True
                    S = [i for i in range(N) if sup[i]]
                    n_cand += 1
                    first = S[:K]
                    # Lagrange coefficients of the interpolant from `first`
                    Lforms = {}
                    for x in range(N):
                        if x in first:
                            continue
                        vec = [0] * T
                        for j, pj in enumerate(first):
                            num, den = 1, 1
                            for l, pl in enumerate(first):
                                if l == j:
                                    continue
                                num = num * ((xs[x] - xs[pl]) % P) % P
                                den = den * ((xs[pj] - xs[pl]) % P) % P
                            lam = num * pow(den, P - 2, P) % P
                            if pj in pidx:      # U_c(pj) = c_{i} * LC(pj)
                                vec[pidx[pj]] = (vec[pidx[pj]]
                                                 + lam * LC[pj]) % P
                        if x in pidx:
                            vec[pidx[x]] = (vec[pidx[x]] - LC[x]) % P
                        Lforms[x] = vec
                    must0 = [Lforms[x] for x in S if x not in first]
                    must1 = [Lforms[x] for x in range(N) if x not in S]
                    if must0:
                        basis = nullspace(must0)
                    else:
                        basis = [[1 if i == j else 0 for i in range(T)]
                                 for j in range(T)]
                    d = len(basis)
                    if d == 0:
                        continue
                    W = PP[d]                       # (npts, d)
                    B = np.array(basis, dtype=np.int64)   # (d, T)
                    C = (W @ B) % P                 # (npts, T) candidate words
                    ok = np.ones(C.shape[0], dtype=bool)
                    for vec in must1:
                        ok &= (C @ np.array(vec, dtype=np.int64)) % P != 0
                    if not ok.any():
                        continue
                    good = C[ok]
                    good = good[np.any(good != 0, axis=1)]
                    if good.size == 0:
                        continue
                    np.add.at(counts, proj_index(good), 1)

print(f"candidates enumerated: {n_cand} (expect 5096)")
assert n_cand == 5096, n_cand

# legality mask: distinct nonzero scalars (genuine 2-point value fibres)
allc = np.concatenate([PP[T - lead] if False else None for lead in []] or
                      [np.array([[0] * lead + [1] + list(tail)
                                 for tail in itertools.product(range(P),
                                                               repeat=T - lead - 1)],
                                dtype=np.int64) for lead in range(T)], axis=0)
idx_all = proj_index(allc)
order = np.argsort(idx_all)
allc = allc[order]
legal = np.ones(allc.shape[0], dtype=bool)
legal &= np.all(allc != 0, axis=1)
srt = np.sort(allc, axis=1)
legal &= np.all(srt[:, 1:] != srt[:, :-1], axis=1)

print()
print("=" * 78)
print("EXHAUSTIVE exact retained count over ALL 922,180 projective words")
print("=" * 78)
print(f"   all words   : mean {counts.mean():.3f}  median {np.median(counts):.0f}"
      f"  max {counts.max()}  min {counts.min()}")
lc = counts[legal]
print(f"   LEGAL words : {legal.sum():,} of {len(legal):,}   mean {lc.mean():.3f}"
      f"  median {np.median(lc):.0f}  max {lc.max()}  min {lc.min()}")
print(f"   99.9th pct (legal) = {np.percentile(lc, 99.9):.1f}; "
      f"99.99th = {np.percentile(lc, 99.99):.1f}")
top = np.argsort(-np.where(legal, counts, -1))[:8]
print("   worst legal words (scalar vector -> exact retained):")
for i in top:
    print(f"      {allc[i].tolist()} -> {counts[i]}")
banked = {"consec": [1, 2, 3, 4], "geom5": [1, 5, 25, 125 % P]}
for name, c in banked.items():
    j = int(proj_index(np.array([c], dtype=np.int64))[0])
    print(f"   banked {name:7s} {c} -> {counts[j]}")
print()
print(f"   MAX16_exact (legal) = {lc.max()}   mean = {lc.mean():.2f}   "
      f"ratio = {lc.max()/lc.mean():.2f}x")
