#!/usr/bin/env python3
"""Exact full-chart LS6 enumeration by last-coordinate bucketing.

For the monic chart D = v0 + sum_i c_i dir_i, evaluation at a pool point x
is AFFINE in (c_1..c_r).  Fixing all but the last coordinate, each pool
point x prescribes the unique last coordinate c_last(x) that makes x a root.
Bucketing the pool by c_last(x) therefore enumerates, in one pass, every
chart member with exactly j roots in the pool -- i.e. the whole split locus,
exactly, with no sampling.

Outputs the canonical-owner histogram g = |Z(D_0) cap Z(D_H)| (= deg of the
canonical owner G for split squarefree locators, l1_fpc5_ratehalf_ls6_
canonical_owner_packing (CO2)-(CO3)) and the max core packing.
"""
from __future__ import annotations

import json
import random
import sys
from math import comb

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from ls6_owner import build_ls6, kernel_basis  # noqa: E402
from rh_m4t2_census import peval, pdegree, pmul, prem  # noqa: E402


def main():
    ell, b, a, q, trials = (int(sys.argv[i]) for i in range(1, 6))
    seed = int(sys.argv[6]) if len(sys.argv) > 6 else 20260807
    n = 8 * ell + 2 * b - 2
    N = 4 * ell + b - 2
    j = 2 * ell - a
    h = ell - 2 * a
    J = ell * (4 * a - b + 2) + a * a + 2 * a * b - 4 * a
    rng = random.Random(seed)
    owner = {}
    sizes = []
    packs = []
    best = {"members": -1}
    for tr in range(trials):
        pts = rng.sample(range(1, q), 4 * ell + b)
        petals = [pts[i * ell:(i + 1) * ell] for i in range(4)]
        labels = rng.sample(range(1, q), 4)
        lam = (labels[2] - labels[0]) * pow((labels[1] - labels[0]) % q,
                                            q - 2, q) % q
        if lam in (0, 1):
            continue
        T, M, E, jj, lam = build_ls6(petals[:3], labels[:3], ell, a, q)
        basis = kernel_basis(T, j, q)
        if len(basis) != ell - 2 * a + 2:
            continue
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
        r = len(dirs)                       # = ell-2a+1
        pool = sorted(set(range(1, q)) - set(pts))
        e0 = {x: peval(v0, x, q) for x in pool}
        Ev = [{x: peval(dv, x, q) for x in pool} for dv in dirs]
        last = Ev[-1]
        invlast = {x: (pow(last[x], q - 2, q) if last[x] else 0) for x in pool}
        members = []

        def sweep(prefix):
            A = {}
            for x in pool:
                v = e0[x]
                for i, c in enumerate(prefix):
                    if c:
                        v += c * Ev[i][x]
                A[x] = v % q
            Z0 = [x for x in pool if last[x] == 0 and A[x] == 0]
            buckets = {}
            for x in pool:
                if last[x]:
                    cv = (-A[x] * invlast[x]) % q
                    buckets.setdefault(cv, []).append(x)
            cands = []
            if len(Z0) == j:
                cands.append((None, Z0))    # whole line splits (flagged)
            for cv, xs in buckets.items():
                if len(xs) + len(Z0) == j:
                    cands.append((cv, sorted(xs + Z0)))
            for cv, roots in cands:
                if cv is None:
                    continue
                F = v0[:]
                for i, c in enumerate(list(prefix) + [cv]):
                    if c:
                        F = [(u + c * w) % q for u, w in zip(F, dirs[i])]
                V = prem(pmul(F, E, q), M, q)
                if pdegree(V) > ell - a:
                    continue
                if any(peval(V, x, q) == 0 for x in roots):
                    continue
                members.append(frozenset(roots))

        def rec(i, prefix):
            if i == r - 1:
                sweep(prefix)
                return
            for c in range(q):
                rec(i + 1, prefix + [c])

        rec(0, [])
        S = list(set(members))
        sizes.append(len(S))
        if len(S) >= 2:
            D0 = S[0]
            for D in S[1:]:
                g = len(D0 & D)
                owner[g] = owner.get(g, 0) + 1
        # exhaustive branch-and-bound core packing
        m = len(S)
        bl = [0, None]

        def bb(i, chosen, u):
            if len(chosen) > bl[0]:
                bl[0] = len(chosen)
                bl[1] = [sorted(S[t]) for t in chosen]
            if i == m or len(chosen) + (N - len(u)) <= bl[0]:
                return
            for t in range(i, m):
                nu = u | S[t]
                if len(nu) <= N:
                    chosen.append(t)
                    bb(t + 1, chosen, nu)
                    chosen.pop()
        if S:
            bb(0, [], set())
        packs.append(bl[0])
        if len(S) > best["members"]:
            best = {"members": len(S), "trial": tr, "packed": bl[0],
                    "petals": petals, "labels": labels, "lambda": lam,
                    "packset": bl[1]}
    print(json.dumps({
        "mode": "ls6_bucket_exact", "ell": ell, "b": b, "a": a, "q": q,
        "n": n, "N_core": N, "j": j, "h_overlap_cap": h, "J": J,
        "regime": "OFF-TAIL (Johnson-paid)" if J > 0 else "LIVE TAIL",
        "two_power_n": (n & (n - 1)) == 0,
        "proj_dim_r": ell - 2 * a + 1,
        "codim_sigma": ell + a - 1,
        "chart_enumerated_exactly": q ** (ell - 2 * a + 1),
        "first_moment_binomN_j_over_q_sigma": comb(N, j) / q ** (ell + a - 1),
        "trials": len(sizes),
        "atom_size_mean": sum(sizes) / len(sizes) if sizes else 0,
        "atom_size_max": max(sizes) if sizes else 0,
        "atom_sizes": sizes,
        "max_core_packing": max(packs) if packs else 0,
        "packings": packs,
        "owner_degree_histogram_g": dict(sorted(owner.items())),
        "owner_pairs_total": sum(owner.values()),
        "best": best,
    }))


if __name__ == "__main__":
    main()
