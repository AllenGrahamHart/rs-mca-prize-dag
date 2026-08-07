#!/usr/bin/env python3
"""A5: exact retained counts at n=32 for random, structured and filter-optimal
words -- the scale half of the pre-registered adversarial falsifier test."""
from __future__ import annotations

import itertools
import sys
import numpy as np

P, N, K = 97, 32, 16


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


xs = np.array(domain(P, N), dtype=np.int64)
core, bg, petals = layout(N)
T = len(petals)
petal_points = [pt for pr in petals for pt in pr]
pidx = {pt: i for i, pr in enumerate(petals) for pt in pr}
LC = np.ones(N, dtype=np.int64)
for pt in range(N):
    v = 1
    for r in core:
        v = v * int((xs[pt] - xs[r]) % P) % P
    LC[pt] = v

# ---- candidate supports + the single dual filter form (as in a1_a3) --------
alpha = {pt: int(xs[pt]) * int(LC[pt]) % P * int(LC[pt]) % P for pt in pidx}
rows, sup_arr = [], []
threshold = 2 * (T - 2)
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
                    m = cc + use_bg - om
                    droppable = list(Kc) + ([bg] if use_bg else [])
                    R = set(droppable[:m - 1])
                    Kp = [x for x in Kc if x not in R]
                    bp = use_bg - (1 if bg in R else 0)
                    g = [0] * T
                    for pt, pi in pidx.items():
                        if pt in O:
                            continue
                        v = alpha[pt]
                        for y in O:
                            v = v * int((xs[pt] - xs[y]) % P) % P
                        if bp == 0:
                            v = v * int((xs[pt] - xs[bg]) % P) % P
                        den = 1
                        for y in Kp:
                            den = den * int((xs[pt] - xs[y]) % P) % P
                        v = v * pow(den, P - 2, P) % P
                        g[pi] = (g[pi] + v) % P
                    rows.append(g)
                    s = np.zeros(N, dtype=np.int8)
                    s[petal_points] = 1
                    s[list(O)] = 0
                    s[list(Kc)] = 1
                    if use_bg:
                        s[bg] = 1
                    sup_arr.append(s)
G = np.array(rows, dtype=np.int64)
SUP = np.array(sup_arr, dtype=np.int8)
NC = G.shape[0]
print(f"candidates {NC:,} (expect 386,640); gamma {G.shape}")
assert NC == 386640

SUPIDX = [np.flatnonzero(SUP[i]) for i in range(NC)]


def word_values(c):
    v = np.zeros(N, dtype=np.int64)
    for pt, i in pidx.items():
        v[pt] = int(c[i]) * int(LC[pt]) % P
    return v


def exact_count(c, batch=800):
    """Full census semantics, vectorised: interpolate from the first K points
    of each filter survivor, require the complete agreement set to equal S."""
    c = np.asarray(c, dtype=np.int64) % P
    U = word_values(c)
    hits = np.flatnonzero((G @ c) % P == 0)
    kept, hist = 0, {}
    for s0 in range(0, len(hits), batch):
        idx = hits[s0:s0 + batch]
        H = len(idx)
        Pm = np.stack([SUPIDX[i][:K] for i in idx])          # (H,K)
        xp = xs[Pm]                                          # (H,K)
        D = ((xs[None, None, :] - xp[:, :, None]) % P).astype(np.int32)
        # Lambda(x) = prod_j (x - p_j)
        Lam = np.ones((H, N), dtype=np.int64)
        for j in range(K):
            Lam = Lam * D[:, j, :] % P
        # Lambda'(p_j) = prod_{l != j} (p_j - p_l)
        DD = (xp[:, :, None] - xp[:, None, :]) % P
        eye = np.eye(K, dtype=bool)
        DD = np.where(eye[None, :, :], 1, DD)
        Lp = np.ones((H, K), dtype=np.int64)
        for l in range(K):
            Lp = Lp * DD[:, :, l] % P
        w = U[Pm] * pow_inv(Lp) % P                          # (H,K)
        Dinv = pow_inv(np.where(D == 0, 1, D))
        val = (w[:, :, None] * Dinv).sum(axis=1) % P
        f = Lam * val % P
        onpts = np.zeros((H, N), dtype=bool)
        np.put_along_axis(onpts, Pm, True, axis=1)
        agree = np.where(onpts, True, f == U[None, :])
        want = SUP[idx].astype(bool)
        ok = np.all(agree == want, axis=1)
        kept += int(ok.sum())
        for a in agree[ok].sum(axis=1):
            hist[int(a)] = hist.get(int(a), 0) + 1
    return kept, hist, len(hits)


_INV = np.array([0] + [pow(i, P - 2, P) for i in range(1, P)], dtype=np.int64)


def pow_inv(a):
    return _INV[a % P]


def consec():
    return [(i + 1) % P for i in range(T)]


def geom5():
    out, g = [], 1
    for _ in range(T):
        out.append(g)
        g = g * 5 % P
    return out


print()
print("=" * 78)
print("A1 gate at n=32 (vectorised checker) + A5 scale search")
print("=" * 78)
for name, c in (("consec", consec()), ("geom5", geom5())):
    k, h, nf = exact_count(c)
    want = 2879 if name == "consec" else 2857
    print(f"   banked {name:7s}: filter {nf:6,d} exact {k:6,d} (banked {want}) "
          f"{'PASS' if k == want else '*** FAIL ***'} {h}")
    if k != want:
        sys.exit(1)

rng = np.random.default_rng(20260807)
vals = []
for _ in range(12):
    c = rng.integers(1, P, size=T)
    while len(set(c.tolist())) != T:
        c = rng.integers(1, P, size=T)
    k, _, _ = exact_count(c)
    vals.append(k)
vals = np.array(vals)
print(f"   12 random legal words: mean {vals.mean():.1f} sd {vals.std():.1f} "
      f"min {vals.min()} max {vals.max()}")

xbg2 = int(xs[bg]) * int(xs[bg]) % P
sc_min = [(int(xs[a]) * int(xs[a]) - xbg2) % P for (a, b) in petals]
k, h, nf = exact_count(sc_min)
print(f"   minimal-degree word (c_i = x_i^2-x_bg^2): filter {nf} exact {k} {h}")
best = max(int(vals.max()), k)

# filter-optimal words (the n=16 lesson: filter max != exact max, but test it)
print("   RANSAC filter-maximising words (exactness applied):")
bestv, cands = 0, []
for _ in range(1500):
    idx = rng.choice(NC, size=T - 1, replace=False)
    A = G[idx].copy() % P
    piv, where = 0, []
    for col in range(T):
        sel = None
        for r in range(piv, A.shape[0]):
            if A[r, col] % P:
                sel = r
                break
        if sel is None:
            continue
        A[[piv, sel]] = A[[sel, piv]]
        A[piv] = A[piv] * pow(int(A[piv, col]), P - 2, P) % P
        for r in range(A.shape[0]):
            if r != piv and A[r, col] % P:
                A[r] = (A[r] - A[r, col] * A[piv]) % P
        where.append(col)
        piv += 1
    free = [c2 for c2 in range(T) if c2 not in where]
    if not free:
        continue
    v = np.zeros(T, dtype=np.int64)
    v[free[0]] = 1
    for i, col in enumerate(where):
        v[col] = (-A[i, free[0]]) % P
    cnt = int(np.count_nonzero((G @ v) % P == 0))
    cands.append((cnt, v.copy()))
cands.sort(key=lambda z: -z[0])
for cnt, v in cands[:6]:
    kk, hh, nfk = exact_count(v)
    print(f"      filter {cnt:6,d} -> exact {kk:6,d}  scalars {v.tolist()[:6]}...")
    best = max(best, kk)

print()
print("=" * 78)
print("PRE-REGISTERED ADVERSARIAL FALSIFIER TEST (registered in PREREG R2)")
print("=" * 78)
MAX16, mean16 = 66, 32.145      # exhaustive over all 830,490 legal words
MAX32, mean32 = best, vals.mean()
print(f"   n=16 EXHAUSTIVE: MAX16 = {MAX16}, mean16 = {mean16}")
print(f"   n=32 SEARCH    : MAX32 = {MAX32} (best found), mean32 = {mean32:.1f}")
lhs = MAX32 / MAX16
rhs = 3 * (mean32 / mean16)
print(f"   MAX32/MAX16 = {lhs:.2f}    3*(mean32/mean16) = {rhs:.2f}")
print(f"   ESCAPE TEST 1 (growth):  {'FIRES' if lhs > rhs else 'does NOT fire'}")
print(f"   ESCAPE TEST 2 (MAX16 > 10*mean16 = {10*mean16:.1f}): "
      f"{'FIRES' if MAX16 > 10*mean16 else 'does NOT fire'}")
print(f"   worst-word overshoot: n=16 {MAX16/mean16:.2f}x (exhaustive), "
      f"n=32 {MAX32/mean32:.2f}x (search only -- a lower bound on the true max)")
