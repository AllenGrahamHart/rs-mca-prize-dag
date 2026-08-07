#!/usr/bin/env python3
"""Red 2 (l1_fpc5_ratehalf_m4_t3_split_slice_payment): the guarded LS6 atom,
its canonical-owner distribution, and the same core-choosable adversary.

LS6 (pma_ratehalf_complement_linear_slice_reduction statement.md:59-61):
  {D monic : D|L_C, deg D = 2ell-a,
             deg rem_(L_2L_3)(D Etilde) <= ell-a,
             gcd(D, rem_(L_2L_3)(D Etilde)) = 1}
with Etilde == L_1^{-1} mod L_2 and == lambda L_1^{-1} mod L_3, deg < 2ell.

Note the guard does NOT involve C.  So, exactly as for the m4_t2 flat, an
adversary who may place the core enumerates the unguarded slice
W_(lambda,a)^{<=j} (projective dimension r = ell-2a+1) and packs the split
members into |C| = 4ell+b-2 points.

Canonical owner (l1_fpc5_ratehalf_ls6_canonical_owner_packing (CO2)):
  G = gcd(D_0,H) = gcd(D_0,D_H),  g = deg G,  h = ell-2a,  c = h-g.
For split squarefree locators g = |Z(D_0) cap Z(D_H)|.
"""
from __future__ import annotations

import json
import random
import sys
from itertools import combinations
from math import comb

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from rh_m4t2_census import (  # noqa: E402
    locator, peval, pinvmod, pmul, prem, pdegree,
)


def build_ls6(petals3, labels3, ell, a, q):
    L1 = locator(petals3[0], q)
    L2 = locator(petals3[1], q)
    L3 = locator(petals3[2], q)
    c1, c2, c3 = labels3
    lam = (c3 - c1) * pow((c2 - c1) % q, q - 2, q) % q
    assert lam not in (0, 1)
    M = pmul(L2, L3, q)
    inv1_2 = pinvmod(L1, L2, q)
    inv1_3 = pinvmod(L1, L3, q)
    e2 = pmul(L3, pinvmod(L3, L2, q), q)
    e3 = pmul(L2, pinvmod(L2, L3, q), q)
    r3 = prem([lam * c % q for c in inv1_3], L3, q)
    t2 = pmul(inv1_2, e2, q)
    t3 = pmul(r3, e3, q)
    E = [0] * max(len(t2), len(t3))
    for i, c in enumerate(t2):
        E[i] = (E[i] + c) % q
    for i, c in enumerate(t3):
        E[i] = (E[i] + c) % q
    E = prem(E, M, q)
    j = 2 * ell - a
    rows = ell + a - 1                      # coeffs of degree ell-a+1..2ell-1
    T = [[0] * (j + 1) for _ in range(rows)]
    degM = 2 * ell
    cur = E[:] + [0] * (degM - len(E))
    for m in range(j + 1):
        for r in range(rows):
            idx = ell - a + 1 + r
            T[r][m] = cur[idx] if idx < len(cur) else 0
        nxt = [0] + cur[:-1]
        top = cur[degM - 1]
        if top:
            f = top * pow(M[degM], q - 2, q) % q
            for i in range(degM + 1):
                if i < len(nxt):
                    nxt[i] = (nxt[i] - f * M[i]) % q
        cur = nxt[:degM]
    return T, M, E, j, lam


def kernel_basis(T, j, q):
    rows = [r[:] for r in T]
    m, ncol = len(rows), j + 1
    piv, rk = [], 0
    for col in range(ncol):
        p = None
        for r in range(rk, m):
            if rows[r][col] % q:
                p = r
                break
        if p is None:
            continue
        rows[rk], rows[p] = rows[p], rows[rk]
        inv = pow(rows[rk][col], q - 2, q)
        rows[rk] = [c * inv % q for c in rows[rk]]
        for r in range(m):
            if r != rk and rows[r][col]:
                f = rows[r][col]
                rows[r] = [(x - f * y) % q for x, y in zip(rows[r], rows[rk])]
        piv.append(col)
        rk += 1
    free = [c for c in range(ncol) if c not in piv]
    basis = []
    for fc in free:
        v = [0] * ncol
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-rows[i][fc]) % q
        basis.append(v)
    return basis


def main():
    ell = int(sys.argv[1])
    b = int(sys.argv[2])
    a = int(sys.argv[3])
    q = int(sys.argv[4])
    trials = int(sys.argv[5])
    seed = int(sys.argv[6]) if len(sys.argv) > 6 else 20260807
    budget = int(sys.argv[7]) if len(sys.argv) > 7 else 0
    n = 8 * ell + 2 * b - 2
    k = 4 * ell + b - 1
    N = 4 * ell + b - 2
    j = 2 * ell - a
    h = ell - 2 * a
    J = ell * (4 * a - b + 2) + a * a + 2 * a * b - 4 * a
    rng = random.Random(seed)
    best = {"packed": 0}
    stats = []
    owner_hist = {}
    for tr in range(trials):
        pts = rng.sample(range(1, q), 4 * ell + b)
        petals = [pts[i * ell:(i + 1) * ell] for i in range(4)]
        bg = pts[4 * ell:]
        labels = rng.sample(range(1, q), 4)
        lam_try = (labels[2] - labels[0]) * pow((labels[1] - labels[0]) % q,
                                                q - 2, q) % q
        if lam_try in (0, 1):
            continue
        T, M, E, jj, lam = build_ls6(petals[:3], labels[:3], ell, a, q)
        basis = kernel_basis(T, j, q)
        rexp = ell - 2 * a + 2
        allowed = set(range(1, q)) - set(pts)
        lead = [v[j] for v in basis]
        nz = [i for i, c in enumerate(lead) if c]
        if not nz:
            continue
        i0 = nz[0]
        inv = pow(lead[i0], q - 2, q)
        v0 = [c * inv % q for c in basis[i0]]
        dirs = []
        for i, v in enumerate(basis):
            if i == i0:
                continue
            f = lead[i]
            dirs.append([(x - f * y) % q for x, y in zip(v, v0)])
        splitters = []

        def test(F):
            roots = [x for x in allowed if peval(F, x, q) == 0]
            if len(roots) != j:
                return
            V = prem(pmul(F, E, q), M, q)
            if pdegree(V) > ell - a:
                return
            if any(peval(V, x, q) == 0 for x in roots):
                return                       # gcd(D, rem) = 1
            splitters.append(frozenset(roots))

        def enum(idx, cur):
            if idx == len(dirs):
                test(cur)
                return
            for c in range(q):
                if c == 0:
                    enum(idx + 1, cur)
                else:
                    enum(idx + 1, [(x + c * y) % q
                                   for x, y in zip(cur, dirs[idx])])

        size = q ** len(dirs)
        if budget and size > budget:
            for _ in range(budget):
                cur = v0[:]
                for dv in dirs:
                    c = rng.randrange(q)
                    if c:
                        cur = [(x + c * y) % q for x, y in zip(cur, dv)]
                test(cur)
            sampled = budget
        else:
            enum(0, v0)
            sampled = size
        S = list(set(splitters))
        # canonical owner distribution against a fixed base
        if len(S) >= 2:
            D0 = S[0]
            for D in S[1:]:
                g = len(D0 & D)
                owner_hist[g] = owner_hist.get(g, 0) + 1
        packed, packset = (1, [sorted(S[0])]) if S else (0, None)
        cap = S[:80]
        for sz in range(2, 8):
            found = None
            for combo in combinations(range(len(cap)), sz):
                u = set()
                ok = True
                for i in combo:
                    u |= cap[i]
                    if len(u) > N:
                        ok = False
                        break
                if ok and len(u) <= N:
                    found = combo
                    break
            if found is None:
                break
            packed = sz
            packset = [sorted(cap[i]) for i in found]
        stats.append({"trial": tr, "basis_dim": len(basis),
                      "expected_dim": rexp, "sampled": sampled,
                      "split_members": len(S), "max_packed": packed})
        if packed > best["packed"]:
            best = {"packed": packed, "trial": tr, "split_members": len(S),
                    "petals": petals, "bg": bg, "labels": labels,
                    "lambda": lam, "root_sets": packset}
    tot = [s["split_members"] for s in stats]
    print(json.dumps({
        "mode": "ls6_owner", "ell": ell, "b": b, "a": a, "q": q,
        "n": n, "k": k, "N_core": N, "j": j, "h_overlap_cap": h,
        "J": J, "J_sign": "PAID (J>0)" if J > 0 else "LIVE TAIL (J<=0)",
        "off_tail": J > 0,
        "two_power_n": (n & (n - 1)) == 0,
        "proj_dim_r_expected": ell - 2 * a + 1,
        "slice_dim_expected": ell - 2 * a + 2,
        "basis_dims_observed": sorted({s["basis_dim"] for s in stats}),
        "codim_sigma": ell + a - 1,
        "first_moment_binomN_j_over_q_sigma":
            comb(N, j) / q ** (ell + a - 1),
        "trials": len(stats),
        "split_members_mean": sum(tot) / len(tot) if tot else 0,
        "split_members_max": max(tot) if tot else 0,
        "max_packed": best["packed"],
        "owner_degree_histogram_g": dict(sorted(owner_hist.items())),
        "owner_hist_note": "g=deg gcd(D_0,D_H); c=h-g; packing pays bounded c",
        "best": best,
        "per_trial": stats[:12],
    }))


if __name__ == "__main__":
    main()
