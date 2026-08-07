#!/usr/bin/env python3
"""D3 ADVERSARIAL (strong form): the guarded flat does NOT depend on the
core C.  Fix (B, T_1..T_4, labels) -> the flat V_F and its monic chart A_F
are already determined.  The adversary may then CHOOSE the core to contain
the roots of as many split members of A_F as fit in |C| = 5*ell-5 points.

So the real question is a set-packing question on the chart:
    given  Sigma = {F in A_F : F squarefree, fully split over F_q,
                    Z(F) disjoint from B and all petals},
    maximise  #{F in Sigma' subset Sigma}  subject to |union Z(F)| <= 5*ell-5.

Two regimes reported:
  FREE-DOMAIN : the n-point evaluation domain is chosen by the adversary
                (a RELAXATION -- the official domain is mu_n).
  MU-DOMAIN   : layout must partition mu_n; then Sigma is computed with
                roots restricted to the 5*ell-5 leftover mu_n points, which
                is the honest official-shaped object.
"""
from __future__ import annotations

import json
import random
import sys
from itertools import combinations

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from rh_m4t2_census import (  # noqa: E402
    build_flat, domain, locator, peval, pmul, prem,
)


def chart_members(T, d, q):
    """Basis of ker(T) inside K[X]_{<=d}, then the monic affine chart."""
    rows = [row[:] for row in T]
    m, ncol = len(rows), d + 1
    piv = []
    rk = 0
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
                rows[r] = [(a - f * b) % q for a, b in zip(rows[r], rows[rk])]
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
    q = int(sys.argv[2])
    trials = int(sys.argv[3])
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 20260807
    regime = sys.argv[5] if len(sys.argv) > 5 else "free"
    d = 2 * ell - 3
    n = 10 * ell - 8
    ncore = 5 * ell - 5
    b = ell - 3
    rng = random.Random(seed)
    mupts, cyc = domain(n, q)
    best = {"packed": 0}
    stats = []
    for tr in range(trials):
        if regime == "mu":
            pool = mupts[:]
            rng.shuffle(pool)
            bg = pool[:b]
            petals = [pool[b + i * ell:b + (i + 1) * ell] for i in range(4)]
            allowed = set(pool[b + 4 * ell:])           # exactly ncore points
        else:
            pts = rng.sample(range(1, q), b + 4 * ell)
            bg = pts[:b]
            petals = [pts[b + i * ell:b + (i + 1) * ell] for i in range(4)]
            used = set(pts)
            allowed = set(range(1, q)) - used
        labels = rng.sample(range(1, q), 4)
        pair = (0, 1)
        T, P, G, dd, L0, L1, L2, c1, c2 = build_flat(
            [], bg, petals, labels, pair, ell, q)
        basis = chart_members(T, d, q)
        if len(basis) != ell - 1:
            continue
        # monic chart: coefficient of X^d equals 1
        lead = [v[d] for v in basis]
        nz = [i for i, c in enumerate(lead) if c]
        if not nz:
            continue
        i0 = nz[0]
        inv = pow(lead[i0], q - 2, q)
        v0 = [c * inv % q for c in basis[i0]]           # monic member
        dirs = []
        for i, v in enumerate(basis):
            if i == i0:
                continue
            f = lead[i]
            dirs.append([(a - f * c) % q for a, c in zip(v, v0)])
        # dirs spans the (ell-2)-dim direction space of the monic chart
        assert len(dirs) == ell - 2
        splitters = []
        untouched = [2, 3]
        # enumerate the chart
        def enum(idx, cur):
            if idx == len(dirs):
                F = cur
                roots = [x for x in allowed if peval(F, x, q) == 0]
                if len(roots) != d:
                    return
                W = prem(pmul(F, G, q), P, q)
                if any(peval(W, x, q) == 0 for x in roots):
                    return                              # primitivity
                for u in untouched:                     # nonagreement
                    cu = labels[u]
                    for x in petals[u]:
                        if (peval(W, x, q) - cu * peval(F, x, q)) % q == 0:
                            return
                splitters.append(frozenset(roots))
                return
            for a in range(q):
                if a == 0:
                    enum(idx + 1, cur)
                else:
                    enum(idx + 1, [(c + a * e) % q for c, e in zip(cur, dirs[idx])])
        budget = int(sys.argv[6]) if len(sys.argv) > 6 else 0
        if budget and q ** (ell - 2) > budget:
            for _ in range(budget):
                cur = v0[:]
                for dv in dirs:
                    a = rng.randrange(q)
                    if a:
                        cur = [(c + a * e) % q for c, e in zip(cur, dv)]
                enum(len(dirs), cur)
            sampled = budget
        else:
            enum(0, v0)
            sampled = q ** (ell - 2)
        # max packing: greedy over pairs/triples then a bounded exhaustive
        # EXHAUSTIVE max-packing by depth-first branch and bound over ALL
        # split members (no candidate cap): maximise |chosen| with
        # |union of root sets| <= ncore.
        S = list(set(splitters))
        packed = 0
        packset = None
        m = len(S)
        bestlocal = [0, None]

        def bb(i, chosen, u):
            if len(chosen) > bestlocal[0]:
                bestlocal[0] = len(chosen)
                bestlocal[1] = [sorted(S[t]) for t in chosen]
            # SOUND optimistic bound: at most all remaining members.
            # (a member may add ZERO new points, so a "new points" bound
            #  would be unsound -- self-correction after a first buggy run)
            if i == m or len(chosen) + (m - i) <= bestlocal[0]:
                return
            for t in range(i, m):
                nu = u | S[t]
                if len(nu) <= ncore:
                    chosen.append(t)
                    bb(t + 1, chosen, nu)
                    chosen.pop()

        if S:
            bb(0, [], set())
            packed, packset = bestlocal[0], bestlocal[1]
        stats.append({"trial": tr, "n_split_members": len(S),
                      "max_packed": packed})
        if packed > best["packed"]:
            best = {"packed": packed, "trial": tr,
                    "n_split_members": len(S),
                    "bg": bg, "petals": petals, "labels": labels,
                    "root_sets": packset}
    thr = 4 * (ell - 2)
    tot = [s["n_split_members"] for s in stats]
    print(json.dumps({
        "mode": "pack_adversary", "regime": regime,
        "ell": ell, "q": q, "n": n, "d": d, "core": ncore, "b": b,
        "trials": len(stats),
        "chart_size_q_pow": q ** (ell - 2),
        "split_members_mean": sum(tot) / len(tot) if tot else 0,
        "split_members_max": max(tot) if tot else 0,
        "max_packed_over_trials": best["packed"],
        "escape_threshold_N_exact": thr,
        "ESCAPE_RH_a_FIRED": best["packed"] >= thr,
        "best": best,
        "per_trial": stats[:20],
    }))


if __name__ == "__main__":
    main()
