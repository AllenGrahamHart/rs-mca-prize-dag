#!/usr/bin/env python3
"""EXACT chart enumeration + core-choosable packing for FPC5 red 1
(rate-half M=4, t=2), by last-coordinate bucketing.

Round 23 (notes/pilots_20260807/fpc5_diag/rh_pack_adversary.py) enumerated
the monic guarded chart by BRUTE FORCE over q^(ell-2) points, which forced
it to SAMPLE at ell=5 (3e5 of 2,048,383) and to time out at ell>=6.  Its
headline -- a "hard, q-invariant, ell-invariant cap of 4" -- therefore rests
on a SAMPLE at ell=5.

This script ports the last-coordinate bucketing trick of
fpc5_diag/ls6_bucket.py to the m4_t2 guarded chart, which makes the ell=5
chart EXACTLY enumerable in q^(ell-3)*|pool| work instead of q^(ell-2)*|pool|.

Two matched arms (registered W1 / S4-P2 power control):
  ARM guarded : V_F = the guarded congruence kernel (round 23's object)
  ARM random  : V = a UNIFORMLY RANDOM (ell-1)-dim subspace of F_q[X]_{<=d}
Both arms use the SAME (q, d, allowed point set, core budget N) and the
SAME split-only filter, so any difference in the cap is attributable to
the guarded structure alone.

Registered functionals (CATCH-19C):
  NSPLIT   = # distinct root sets of monic degree-d chart members split on
             `allowed`
  MAXPACK  = max m with m distinct such root sets unioning to <= N points
  BONF     = min{m : m*d - C(m,2)*lam > N} - 1   (inf if none)
  CLIQUE   = clique number of the graph {members}, edge iff they share a root
             (the H3 criterion at ell=4)

Stdlib only.  Run via tools/ramguard.
"""
from __future__ import annotations

import json
import random
import sys
import time
from itertools import product

sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/"
                   "notes/pilots_20260807/fpc5_diag")
from rh_m4t2_census import (  # noqa: E402
    build_flat, domain, peval, pgcd, pdegree, pmul, prem,
)


# ------------------------------------------------------------------ linalg
def rref_kernel(rows_in, ncol, q):
    """Basis of the kernel of the matrix with rows `rows_in`."""
    rows = [r[:] for r in rows_in]
    m = len(rows)
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


def rank_of(rows_in, ncol, q):
    rows = [r[:] for r in rows_in]
    m, rk = len(rows), 0
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
        rk += 1
    return rk


def monic_chart(basis, d, q):
    """(v0, dirs): affine monic chart of the subspace spanned by `basis`."""
    lead = [v[d] for v in basis]
    nz = [i for i, c in enumerate(lead) if c]
    if not nz:
        return None, None
    i0 = nz[0]
    inv = pow(lead[i0], q - 2, q)
    v0 = [c * inv % q for c in basis[i0]]
    dirs = []
    for i, v in enumerate(basis):
        if i == i0:
            continue
        f = lead[i]
        dirs.append([(a - f * c) % q for a, c in zip(v, v0)])
    return v0, dirs


# ------------------------------------------------- exact bucketed enumeration
def enumerate_split(v0, dirs, pool, d, q):
    """EXACT: every monic chart member with exactly d roots in `pool`.

    Returns the set of root sets (frozensets) together with a representative
    coefficient vector for each, and the exact number of chart points swept.
    """
    r = len(dirs)
    e0 = {x: peval(v0, x, q) for x in pool}
    Ev = [{x: peval(dv, x, q) for x in pool} for dv in dirs]
    if r == 0:
        roots = [x for x in pool if e0[x] == 0]
        return ({frozenset(roots): tuple()} if len(roots) == d else {}), 1
    last = Ev[-1]
    invlast = {x: (pow(last[x], q - 2, q) if last[x] else 0) for x in pool}
    found = {}
    swept = 0
    for prefix in product(range(q), repeat=r - 1):
        swept += q
        A = {}
        for x in pool:
            v = e0[x]
            for i, c in enumerate(prefix):
                if c:
                    v += c * Ev[i][x]
            A[x] = v % q
        Z0 = [x for x in pool if last[x] == 0 and A[x] == 0]
        nz0 = len(Z0)
        if nz0 > d:
            continue
        if nz0 == d:
            found.setdefault(frozenset(Z0), prefix + (0,))
        buckets = {}
        for x in pool:
            if last[x]:
                cv = (-A[x] * invlast[x]) % q
                buckets.setdefault(cv, []).append(x)
        need = d - nz0
        if need <= 0:
            continue
        for cv, xs in buckets.items():
            if len(xs) == need:
                found.setdefault(frozenset(xs + Z0), prefix + (cv,))
    return found, swept


def maxpack(rootsets, N, node_cap=4_000_000):
    """Exhaustive branch-and-bound max packing with union <= N.

    SOUND optimistic bound only (a member may add ZERO new points, so a
    'new points' bound would be unsound -- this is round 23's own
    self-correction, kept).  Returns (best, witness, exhaustive_flag).
    """
    S = sorted(rootsets, key=lambda z: sorted(z))
    m = len(S)
    best = [0, None]
    nodes = [0]
    trunc = [False]

    def bb(i, chosen, u):
        nodes[0] += 1
        if nodes[0] > node_cap:
            trunc[0] = True
            return
        if len(chosen) > best[0]:
            best[0] = len(chosen)
            best[1] = [sorted(S[t]) for t in chosen]
        if i == m or len(chosen) + (m - i) <= best[0]:
            return
        for t in range(i, m):
            if trunc[0]:
                return
            nu = u | S[t]
            if len(nu) <= N:
                chosen.append(t)
                bb(t + 1, chosen, nu)
                chosen.pop()

    if S:
        bb(0, [], set())
    return best[0], best[1], (not trunc[0])


def clique_stats(rootsets, cap_nodes=2_000_000):
    """Edge count and clique number of the 'share >= 1 root' graph."""
    S = [set(z) for z in rootsets]
    m = len(S)
    if m == 0:
        return {"n_vertices": 0, "n_edges": 0, "clique_number": 0,
                "max_pair_overlap": 0}
    adj = [set() for _ in range(m)]
    edges = 0
    maxov = 0
    for i in range(m):
        for j in range(i + 1, m):
            ov = len(S[i] & S[j])
            maxov = max(maxov, ov)
            if ov >= 1:
                adj[i].add(j)
                adj[j].add(i)
                edges += 1
    best = [0]
    nodes = [0]

    def expand(R, P):
        nodes[0] += 1
        if nodes[0] > cap_nodes:
            return
        if not P:
            best[0] = max(best[0], len(R))
            return
        if len(R) + len(P) <= best[0]:
            return
        for v in sorted(P):
            expand(R + [v], P & adj[v])
            P = P - {v}

    expand([], set(range(m)))
    return {"n_vertices": m, "n_edges": edges, "clique_number": best[0],
            "max_pair_overlap": maxov, "clique_search_exhaustive":
            nodes[0] <= cap_nodes}


def bonferroni(N, d, lam):
    """min{m : m*d - C(m,2)*lam > N} - 1, or None when it never fires."""
    for m in range(2, 400):
        if m * d - m * (m - 1) // 2 * lam > N:
            return m - 1
    return None


# ---------------------------------------------------------------- the driver
def run(ell, q, nconfig, seed, arm, outfile, want_clique, filters="split"):
    d = 2 * ell - 3
    n = 10 * ell - 8
    N = 5 * ell - 5              # core budget |C| = k-1
    b = ell - 3
    lam_sharp = ell - 3          # round-23 sharpened cap |D cap D'| <= 2s-b
    lam_proved = 2 * (ell - 3)   # (JD1)/(RH0a) cap 2s
    rng = random.Random(seed)
    recs = []
    t0 = time.time()
    for ci in range(nconfig):
        if time.time() - t0 > 250:
            break
        pts = rng.sample(range(1, q), b + 4 * ell)
        bg = pts[:b]
        petals = [pts[b + i * ell:b + (i + 1) * ell] for i in range(4)]
        allowed = sorted(set(range(1, q)) - set(pts))
        labels = rng.sample(range(1, q), 4)
        pair = (0, 1)
        if arm == "guarded":
            T, P, G, dd, L0, L1, L2, c1, c2 = build_flat(
                [], bg, petals, labels, pair, ell, q)
            basis = rref_kernel(T, d + 1, q)
            if len(basis) != ell - 1:
                continue
        else:                                   # random matched flat
            while True:
                rows = [[rng.randrange(q) for _ in range(d + 1)]
                        for _ in range(ell - 1)]
                if rank_of(rows, d + 1, q) == ell - 1:
                    break
            basis = rows
            G = P = None
        v0, dirs = monic_chart(basis, d, q)
        if v0 is None:
            continue
        assert len(dirs) == ell - 2
        # FLAT-WIDE COMMON GCD.  l1_fpc5_ratehalf_m4_t2_sharp_gcd_triviality
        # (GT2) proves this is 1 for the sharp official cell; a config with
        # deg gcd > 0 is OUTSIDE the object and is reported separately.
        gflat = v0[:]
        for dv in dirs:
            gflat = pgcd(gflat, dv, q)
        wgcd = max(pdegree(gflat), 0)
        found, swept = enumerate_split(v0, dirs, allowed, d, q)
        # FULL exact-contributor filters (primitivity + untouched-petal
        # nonagreement), applied only in the guarded arm; the `split` filter
        # level is what the matched random-flat control compares against.
        keep = {}
        for rs, coefs in found.items():
            if filters == "full" and arm == "guarded":
                F = v0[:]
                for i, c in enumerate(coefs):
                    if c:
                        F = [(u + c * w) % q for u, w in zip(F, dirs[i])]
                W = prem(pmul(F, G, q), P, q)
                if any(peval(W, x, q) == 0 for x in rs):
                    continue                       # gcd(F,W_F) != 1
                bad = False
                for u in (2, 3):                   # untouched petals
                    cu = labels[u]
                    for x in petals[u]:
                        if (peval(W, x, q) - cu * peval(F, x, q)) % q == 0:
                            bad = True
                            break
                    if bad:
                        break
                if bad:
                    continue
            keep[rs] = coefs
        rootsets = list(keep.keys())
        maxov = 0
        for i in range(len(rootsets)):
            for j2 in range(i + 1, len(rootsets)):
                ov = len(rootsets[i] & rootsets[j2])
                if ov > maxov:
                    maxov = ov
        mp, wit, exh = maxpack(rootsets, N)
        # BUDGET ELASTICITY: MAXPACK as the core budget is relaxed.  If the
        # cap is a knife-edge counting fact it jumps at N+1; if it is
        # structural it needs a large relaxation.
        curve = [mp]
        for extra in range(1, 6):
            curve.append(maxpack(rootsets, N + extra)[0])
        rec = {"arm": arm, "filters": filters, "ell": ell, "q": q, "d": d,
               "budget_curve_N_to_N5": curve,
               "N_core": N, "n_official": n, "pool": len(allowed),
               "flat_common_gcd_deg": wgcd,
               "chart_points_total": q ** (ell - 2),
               "chart_points_swept": swept,
               "EXACT_full_chart": swept == q ** (ell - 2),
               "NSPLIT": len(rootsets), "MAXPACK": mp,
               "MAX_PAIR_OVERLAP": maxov,
               "maxpack_exhaustive": exh, "config": ci}
        if want_clique and len(rootsets) <= 400:
            rec.update({"graph": clique_stats(rootsets)})
        if arm == "guarded" and mp >= 5:
            rec["WITNESS_5PACK"] = {"bg": bg, "petals": petals,
                                    "labels": labels, "rootsets": wit}
        recs.append(rec)
    clean = [r for r in recs if r["flat_common_gcd_deg"] == 0]
    dirty = [r for r in recs if r["flat_common_gcd_deg"] > 0]
    summary = {
        "mode": "rh_bucket", "arm": arm, "filters": filters,
        "ell": ell, "q": q, "d": d,
        "N_core": N, "seed": seed, "configs": len(recs),
        "configs_gcd_trivial_GT2_clean": len(clean),
        "configs_flat_gcd_nontrivial_EXCLUDED_by_GT2": len(dirty),
        "MAXPACK_max_GCD_TRIVIAL_ONLY": max((r["MAXPACK"] for r in clean),
                                            default=0),
        "MAXPACK_max_gcd_nontrivial": max((r["MAXPACK"] for r in dirty),
                                          default=0),
        "MAX_PAIR_OVERLAP_gcd_trivial": max((r["MAX_PAIR_OVERLAP"]
                                             for r in clean), default=0),
        "proved_cap_2s": 2 * (ell - 3),
        "sharpened_cap_ell_minus_3": ell - 3,
        "BONF_sharpened_lam": {"lam": lam_sharp,
                               "first_failure_minus_1": bonferroni(
                                   N, d, lam_sharp)},
        "BONF_proved_lam": {"lam": lam_proved,
                            "first_failure_minus_1": bonferroni(
                                N, d, lam_proved)},
        "NSPLIT_mean": (sum(r["NSPLIT"] for r in recs) / len(recs)
                        if recs else 0),
        "NSPLIT_max": max((r["NSPLIT"] for r in recs), default=0),
        "MAXPACK_max": max((r["MAXPACK"] for r in recs), default=0),
        "MAXPACK_hist": {},
        "BUDGET_ELASTICITY_max_over_configs": [
            max((r["budget_curve_N_to_N5"][i] for r in clean), default=0)
            for i in range(6)],
        "all_exact": all(r["EXACT_full_chart"] for r in recs),
        "all_bb_exhaustive": all(r["maxpack_exhaustive"] for r in recs),
        "elapsed_s": round(time.time() - t0, 1),
    }
    for r in recs:
        k = str(r["MAXPACK"])
        summary["MAXPACK_hist"][k] = summary["MAXPACK_hist"].get(k, 0) + 1
    if want_clique:
        cl = [r["graph"]["clique_number"] for r in recs if "graph" in r]
        ed = [r["graph"]["n_edges"] for r in recs if "graph" in r]
        ov = [r["graph"]["max_pair_overlap"] for r in recs if "graph" in r]
        summary["CLIQUE_max"] = max(cl, default=0)
        summary["CLIQUE_hist"] = {str(c): cl.count(c) for c in sorted(set(cl))}
        summary["edges_mean"] = sum(ed) / len(ed) if ed else 0
        summary["MAX_PAIR_OVERLAP_observed"] = max(ov, default=0)
    summary["witnesses_5pack"] = [r for r in recs if "WITNESS_5PACK" in r][:2]
    if outfile:
        with open(outfile, "a") as fh:
            fh.write(json.dumps({"summary": summary, "recs": recs}) + "\n")
    print(json.dumps(summary, indent=1))


def main():
    ell = int(sys.argv[1])
    q = int(sys.argv[2])
    nconfig = int(sys.argv[3])
    seed = int(sys.argv[4])
    arm = sys.argv[5] if len(sys.argv) > 5 else "guarded"
    outfile = sys.argv[6] if len(sys.argv) > 6 else ""
    want_clique = (len(sys.argv) > 7 and sys.argv[7] == "clique")
    filters = sys.argv[8] if len(sys.argv) > 8 else "split"
    run(ell, q, nconfig, seed, arm, outfile, want_clique, filters)


if __name__ == "__main__":
    main()
