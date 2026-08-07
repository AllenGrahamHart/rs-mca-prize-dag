#!/usr/bin/env python3
"""S2 (instrument cross-response) + W3 (owner-concentration power control)
for FPC5 red 2, reusing the coordinator-replayed fpc5_diag machinery
(ls6_owner.build_ls6 / kernel_basis, ls6_bucket's exact last-coordinate
bucketing).

Adds three things round 23 did not do:
  (1) a RANDOM-FLAT arm matched on (chart dim, j, q, pool, N) -- the same
      power control as rh_bucket.py's `random` arm;
  (2) the HYPERGEOMETRIC reference for the canonical-owner histogram,
      both unconditioned and conditioned on the proved cap g <= h
      (registered W3: is the 52.4% trivial-owner mass an (MF)-parametric
      fact or a structural one?);
  (3) BONF(N,j,h) = min{m : m*j - C(m,2)*h > N} - 1, so the measured cap
      can be compared with the packing arithmetic at MATCHED parameters
      (registered S2 functional CAPDEF = BONF - MAXPACK).

Stdlib only.  Run via tools/ramguard.
"""
from __future__ import annotations

import json
import random
import sys
import time
from itertools import product
from math import comb

sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/"
                   "notes/pilots_20260807/fpc5_diag")
from ls6_owner import build_ls6, kernel_basis            # noqa: E402
from rh_m4t2_census import peval, pdegree, pmul, prem    # noqa: E402

sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/"
                   "notes/pilots_20260807/mf_wall_adversary")
from rh_bucket import maxpack, monic_chart, rank_of, bonferroni  # noqa: E402


def hypergeom_overlap(N, j):
    """P(|A cap B| = g) for two independent uniform j-subsets of [N]."""
    tot = comb(N, j)
    return {g: comb(j, g) * comb(N - j, j - g) / tot
            for g in range(0, j + 1) if comb(N - j, j - g)}


def main():
    ell, b, a, q, trials = (int(sys.argv[i]) for i in range(1, 6))
    seed = int(sys.argv[6]) if len(sys.argv) > 6 else 20260807
    arm = sys.argv[7] if len(sys.argv) > 7 else "guarded"
    n = 8 * ell + 2 * b - 2
    N = 4 * ell + b - 2
    j = 2 * ell - a
    h = ell - 2 * a
    J = ell * (4 * a - b + 2) + a * a + 2 * a * b - 4 * a
    rng = random.Random(seed)
    owner_base = {}          # g vs the base member D_0 (round-23 convention)
    owner_all = {}           # g over ALL pairs
    sizes, packs, curves = [], [], []
    t0 = time.time()
    ntr = 0
    for tr in range(trials):
        if time.time() - t0 > 240:
            break
        pts = rng.sample(range(1, q), 4 * ell + b)
        petals = [pts[i * ell:(i + 1) * ell] for i in range(4)]
        labels = rng.sample(range(1, q), 4)
        lam = (labels[2] - labels[0]) * pow((labels[1] - labels[0]) % q,
                                            q - 2, q) % q
        if lam in (0, 1):
            continue
        pool = sorted(set(range(1, q)) - set(pts))
        if arm == "guarded":
            T, M, E, jj, lam = build_ls6(petals[:3], labels[:3], ell, a, q)
            basis = kernel_basis(T, j, q)
            if len(basis) != ell - 2 * a + 2:
                continue
        else:
            dim = ell - 2 * a + 2
            while True:
                rows = [[rng.randrange(q) for _ in range(j + 1)]
                        for _ in range(dim)]
                if rank_of(rows, j + 1, q) == dim:
                    break
            basis = rows
            M = E = None
        v0, dirs = monic_chart(basis, j, q)
        if v0 is None:
            continue
        r = len(dirs)                                   # = ell-2a+1
        e0 = {x: peval(v0, x, q) for x in pool}
        Ev = [{x: peval(dv, x, q) for x in pool} for dv in dirs]
        last = Ev[-1]
        invlast = {x: (pow(last[x], q - 2, q) if last[x] else 0)
                   for x in pool}
        members = set()
        for prefix in product(range(q), repeat=r - 1):
            A = {}
            for x in pool:
                v = e0[x]
                for i, c in enumerate(prefix):
                    if c:
                        v += c * Ev[i][x]
                A[x] = v % q
            Z0 = [x for x in pool if last[x] == 0 and A[x] == 0]
            if len(Z0) > j:
                continue
            buckets = {}
            for x in pool:
                if last[x]:
                    cv = (-A[x] * invlast[x]) % q
                    buckets.setdefault(cv, []).append(x)
            cands = []
            if len(Z0) == j:
                cands.append((prefix + (0,), Z0))
            need = j - len(Z0)
            if need > 0:
                for cv, xs in buckets.items():
                    if len(xs) == need:
                        cands.append((prefix + (cv,), sorted(xs + Z0)))
            for coefs, roots in cands:
                if arm == "guarded":
                    F = v0[:]
                    for i, c in enumerate(coefs):
                        if c:
                            F = [(u + c * w) % q for u, w in zip(F, dirs[i])]
                    V = prem(pmul(F, E, q), M, q)
                    if pdegree(V) > ell - a:
                        continue
                    if any(peval(V, x, q) == 0 for x in roots):
                        continue
                members.add(frozenset(roots))
        S = sorted(members, key=lambda z: sorted(z))
        sizes.append(len(S))
        if len(S) >= 2:
            D0 = S[0]
            for D in S[1:]:
                g = len(D0 & D)
                owner_base[g] = owner_base.get(g, 0) + 1
            for i in range(len(S)):
                for k2 in range(i + 1, len(S)):
                    g = len(S[i] & S[k2])
                    owner_all[g] = owner_all.get(g, 0) + 1
        mp, wit, exh = maxpack(S, N)
        packs.append(mp)
        curves.append([maxpack(S, N + x)[0] for x in range(6)])
        ntr += 1
    hg = hypergeom_overlap(N, j)
    hg_cond_tot = sum(v for g, v in hg.items() if g <= h)
    hg_cond = {g: v / hg_cond_tot for g, v in hg.items() if g <= h}
    tot_base = sum(owner_base.values()) or 1
    tot_all = sum(owner_all.values()) or 1
    print(json.dumps({
        "mode": "ls6_probe", "arm": arm,
        "ell": ell, "b": b, "a": a, "q": q, "n": n, "N_core": N,
        "j": j, "h_proved_overlap_cap": h, "J": J,
        "regime": "OFF-TAIL (Johnson-paid)" if J > 0 else "LIVE TAIL",
        "chart_proj_dim_r": ell - 2 * a + 1,
        "codim_sigma": ell + a - 1,
        "chart_points_total": q ** (ell - 2 * a + 1),
        "EXACT_full_chart": True,
        "trials": ntr,
        "atom_size_mean": sum(sizes) / len(sizes) if sizes else 0,
        "atom_size_max": max(sizes) if sizes else 0,
        "MAXPACK_max": max(packs) if packs else 0,
        "MAXPACK_hist": {str(p): packs.count(p) for p in sorted(set(packs))},
        "BONF": bonferroni(N, j, h),
        "BUDGET_ELASTICITY_max_over_trials": [
            max((c[i] for c in curves), default=0) for i in range(6)],
        "owner_hist_vs_base_g": {str(g): owner_base.get(g, 0)
                                 for g in sorted(owner_base)},
        "owner_frac_vs_base_g": {str(g): round(owner_base.get(g, 0) / tot_base,
                                               4) for g in sorted(owner_base)},
        "owner_frac_all_pairs_g": {str(g): round(owner_all.get(g, 0) / tot_all,
                                                 4) for g in sorted(owner_all)},
        "HYPERGEOM_reference_g": {str(g): round(v, 4)
                                  for g, v in sorted(hg.items()) if v > 1e-6},
        "HYPERGEOM_conditioned_on_g_le_h": {str(g): round(v, 4)
                                            for g, v in sorted(hg_cond.items())},
        "elapsed_s": round(time.time() - t0, 1),
    }, indent=1))


if __name__ == "__main__":
    main()
