#!/usr/bin/env python3
"""SPREAD-V: a two-slope family whose RAY COUNT is not capped by h.

The K_V family of stage 1 caps V at (h+1)/(d+1)+1 because all its cores run
through one common (k-1)-set Y.  SPREAD-V drops the common Y.

CONSTRUCTION.  Fix an auxiliary (k+h)-set S0 and put

    F0  subset S0,          |F0|  = h-2d-1        (common "inner" part)
    F_a subset S0 \\ F0,     |F_a| = d+1           pairwise DISJOINT
    E0  outside S0,         |E0|  = d+1           (common "outer" part)
    E_a outside S0 u E0,    |E_a| = h-2d-1        pairwise DISJOINT

    S_a := (S0 \\ (F0 u F_a))  u  E0  u  E_a          a = 0..V-1

Then, EXACTLY:
    |S_a|            = k+h                              = A
    |S_a ^ S_b|      = k+d       (= (S0\\(F0 u F_a u F_b)) u E0)   all DISTINCT
    |S_a ^ S_b ^ S_c| = k-1                          (k-packing, tight)
    T := union S_a,  m := |T|-k = 3d+2 + V(h-2d-1)

so every PAIR of rays is a depth-d two-slope datum with S_a ^ S_b = Z_ab
(banked T2 holds by construction) and M = C(V,2).

Budgets:  V(d+1) <= k+2d+1   (inside S0)  and  (d+1)+V(h-2d-1) <= n-k-h.
Realisability:  rank = V h  <=  2m-1  <=>  V(4d+2-h) <= 6d+3, i.e. AUTOMATIC
for h >= 4d+2.  Hence **V is bounded only by n, never by h**, and

    N_d  =  C(V,2)  =  Theta(n^2 / h^2).

Run under tools/ramguard.
"""
from __future__ import annotations

import random
import sys

sys.dont_write_bytecode = True

_V2 = ("/home/u2470931/smooth-read-solomin/prize/notes/"
       "pilots_20260802/xr_occupancy_v2")
if _V2 not in sys.path:
    sys.path.insert(0, _V2)
import tslib as T                                             # noqa: E402


def layout(k, h, d, V):
    """Point layout; returns dict or None if the budgets fail."""
    if h < 2 * d + 2:
        return None
    phi = h - 2 * d - 1              # |F0| = |E_a|
    psi = d + 1                      # |E0| = |F_a|
    if phi + V * psi > k + h:        # inside-S0 budget
        return None
    S0 = list(range(k + h))
    F0 = S0[:phi]
    Fa = [S0[phi + a * psi: phi + (a + 1) * psi] for a in range(V)]
    cur = k + h
    E0 = list(range(cur, cur + psi))
    cur += psi
    Ea = []
    for a in range(V):
        Ea.append(list(range(cur, cur + phi)))
        cur += phi
    n = cur
    S = []
    for a in range(V):
        Sa = (set(S0) - set(F0) - set(Fa[a])) | set(E0) | set(Ea[a])
        S.append(tuple(sorted(Sa)))
    return dict(n=n, k=k, h=h, d=d, V=V, A=k + h, phi=phi, psi=psi,
                S0=S0, F0=F0, Fa=Fa, E0=E0, Ea=Ea, S=S)


def combinatorics_ok(L):
    """Exact set-arithmetic verification of the design identities."""
    k, h, d, V, A = L["k"], L["h"], L["d"], L["V"], L["A"]
    S = [set(s) for s in L["S"]]
    rep = dict(sizes_ok=all(len(s) == A for s in S), pair_sizes=set(),
               triple_sizes=set(), pairs_distinct=True)
    seen = set()
    for a in range(V):
        for b in range(a + 1, V):
            I = frozenset(S[a] & S[b])
            rep["pair_sizes"].add(len(I))
            if I in seen:
                rep["pairs_distinct"] = False
            seen.add(I)
    for a in range(V):
        for b in range(a + 1, V):
            for c in range(b + 1, V):
                rep["triple_sizes"].add(len(S[a] & S[b] & S[c]))
    rep["pair_sizes"] = sorted(rep["pair_sizes"])
    rep["triple_sizes"] = sorted(rep["triple_sizes"])
    rep["pair_ok"] = rep["pair_sizes"] == [k + d]
    rep["triple_ok"] = all(t <= k - 1 for t in rep["triple_sizes"])
    Tset = set()
    for s in S:
        Tset |= s
    rep["m"] = len(Tset) - k
    rep["m_pred"] = 3 * d + 2 + V * (h - 2 * d - 1)
    rep["m_ok"] = rep["m"] == rep["m_pred"]
    return rep


def build(L, q, seed=0, tries=60):
    """Realise the SPREAD-V support system: pick slopes, solve the ray
    system, return (row, u, v, zs) with a NON-codeword solution."""
    rnd = random.Random(seed)
    row = T.Row2(L["n"], L["k"], L["h"], q)
    for _ in range(tries):
        zs = rnd.sample(range(1, q), L["V"])
        rows = []
        for a, S in enumerate(L["S"]):
            rows += T.ray_rows(row, S, zs[a])
        rk = T.rank_mod(rows, q)
        sol = T.realise(row, rows, seed=rnd.randrange(1 << 30), tries=80)
        if sol is None:
            continue
        u, v = sol
        return row, u, v, zs, rk
    return None


def verify_data(row, u, v, L, zs):
    """DIRECT verification: for each pair (a,b) recover the band pair and
    check depth, ray supports, k-packing.  No exhaustive scan needed."""
    q, k, n, A, d = row.q, row.k, row.n, row.A, L["d"]
    V = L["V"]
    psi = []
    ray_supp = []
    for a, S in enumerate(L["S"]):
        w = [(u[i] + zs[a] * v[i]) % q for i in range(n)]
        p = row.interp(tuple(S[:k]), [w[i] for i in S[:k]])
        psi.append(p)
        sup = tuple(i for i in range(n) if row.ev(p, row.xs[i]) == w[i])
        ray_supp.append(sup)
    rep = dict(ray_support_exact=all(set(ray_supp[a]) == set(L["S"][a])
                                     for a in range(V)),
               ray_sizes=sorted({len(s) for s in ray_supp}),
               A=A)
    cores, bad_depth, pairs = [], 0, set()
    for a in range(V):
        for b in range(a + 1, V):
            den = pow((zs[a] - zs[b]) % q, q - 2, q)
            g = tuple((x - y) * den % q for x, y in zip(psi[a], psi[b]))
            f = tuple((psi[a][j] - zs[a] * g[j]) % q for j in range(k))
            Z = tuple(i for i in range(n)
                      if row.ev(f, row.xs[i]) == u[i]
                      and row.ev(g, row.xs[i]) == v[i])
            cores.append(Z)
            pairs.add((f, g))
            if len(Z) != k + d:
                bad_depth += 1
    rep["M"] = len(cores)
    rep["M_pred"] = V * (V - 1) // 2
    rep["distinct_pairs"] = len(pairs)
    rep["bad_depth"] = bad_depth
    rep["depth_exact"] = bad_depth == 0
    worst = 0
    for i in range(len(cores)):
        for j in range(i + 1, len(cores)):
            m = len(set(cores[i]) & set(cores[j]))
            worst = max(worst, m)
    rep["kpacking_max"] = worst
    rep["kpacking_ok"] = worst <= k - 1
    fam = []
    for idx, (a, b) in enumerate([(a, b) for a in range(V)
                                  for b in range(a + 1, V)]):
        fam.append((cores[idx], [(zs[a], L["S"][a]), (zs[b], L["S"][b])]))
    rep["family_rank"] = T.rank_mod(T.family_rows(row, fam), q)
    rep["ray_only_rank"] = T.rank_mod(
        [r for a, S in enumerate(L["S"]) for r in T.ray_rows(row, S, zs[a])],
        q)
    rep["pred_rank"] = V * row.h
    rep["cost_per_datum"] = rep["family_rank"] / max(1, rep["M"])
    rep["two_R_minus_1"] = 2 * row.R - 1
    return rep, cores
