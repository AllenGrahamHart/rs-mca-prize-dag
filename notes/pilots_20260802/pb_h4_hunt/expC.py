#!/usr/bin/env python3
"""EXPERIMENT C -- the counting / degrees-of-freedom theorem, exactly.

WORD MODEL (the node's "received pair (u,v)").  S is a witness at slope z iff
  sigma_S(u) + z sigma_S(v) = 0,  sigma_S(w)_t = sum_{i in S} lam^S_i x_i^t w_i.
Planting a PRESCRIBED family {(S_i,z_i)}_{i<M} is therefore a LINEAR system
on (u,v) in F_q^{2n} with rows

      R_i = { (c, z_i c) : c in C_{S_i} },   dim C_{S_i} = h,

C_S = the dual code shortened to S.  Two exact facts drive everything:

  (L1)  dim(C_S ^ C_T) = max(0, |S ^ T| - K)         [MDS shortening]
        so a SPREAD family has pairwise-transverse condition spaces;
  (L2)  RS_K x RS_K always lies in the kernel, so rank <= 2(n-K) =: 2r,
        and a prescribed family is realisable by a NON-codeword pair only
        if rank < 2r.  Generic rows give rank = min(Mh, 2r), whence the

        DESIGN CEILING   M <= (2r-1)/h            (slopes prescribed)
        M <= (2r-1)/(h-1)                          (slopes free: the
                                                    determinantal count)

This script measures all of it exactly and then builds real fixtures.

Run:  tools/ramguard local -- python3 expC.py STAGE
"""
from __future__ import annotations

import json
import os
import random
import sys
from itertools import combinations

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import core

HERE = os.path.dirname(os.path.abspath(__file__))

CFG = dict(n=20, q=241, K=4, h=3)          # A=7, r=16, 2r=32
CFG_ORB = dict(n=20, q=41, K=4, h=3)


def setup(cfg):
    n, q, K, h = cfg["n"], cfg["q"], cfg["K"], cfg["h"]
    A = K + h
    D = core.domain(q, n)
    return n, q, K, h, A, D


def cond_rows(fam, D, h, q, n):
    rows = []
    for S, z in fam:
        for c in core.dual_basis(S, D, h, q):
            rows.append(list(c) + [z * x % q for x in c])
    return rows


def rand_spread(n, A, K, M, rng, tries=200000):
    fam, masks = [], []
    for _ in range(tries):
        S = tuple(sorted(rng.sample(range(n), A)))
        m = core.mask_of(S)
        if all(core.popcount(m & o) <= K - 1 for o in masks):
            fam.append(S)
            masks.append(m)
            if len(fam) == M:
                return fam
    return fam


def all_witnesses(u, v, D, n, K, h, q, A):
    """every (z, S): exact, over all A-subsets."""
    out = []
    xp = [[pow(D[i], t, q) for t in range(h)] for i in range(n)]
    for S in combinations(range(n), A):
        L = core.lam(S, D, q)
        su = [0] * h
        sv = [0] * h
        for k, i in enumerate(S):
            a, b = L[k] * u[i] % q, L[k] * v[i] % q
            for t in range(h):
                su[t] = (su[t] + a * xp[i][t]) % q
                sv[t] = (sv[t] + b * xp[i][t]) % q
        # rank <= 1 of [su; sv], and z = -su_t / sv_t
        if all(x == 0 for x in sv):
            continue
        t0 = next(t for t in range(h) if sv[t])
        z = (-su[t0]) * pow(sv[t0], q - 2, q) % q
        if all((su[t] + z * sv[t]) % q == 0 for t in range(h)):
            out.append((z, S))
    return out


def stage_lemma():
    """(L1) dim(C_S ^ C_T) = max(0,|S^T|-K), over many pairs & shapes."""
    rng = random.Random(20260802)
    res = []
    for cfg in [dict(n=16, q=97, K=4, h=3), dict(n=20, q=241, K=4, h=3),
                dict(n=16, q=97, K=8, h=3), dict(n=24, q=73, K=6, h=3)]:
        n, q, K, h, A, D = setup(cfg)
        ok = 0
        bad = []
        for _ in range(400):
            S = tuple(sorted(rng.sample(range(n), A)))
            T = tuple(sorted(rng.sample(range(n), A)))
            if S == T:
                continue
            bS = core.dual_basis(S, D, h, q)
            bT = core.dual_basis(T, D, h, q)
            d = 2 * h - core.rank_mod(bS + bT, q)
            c = core.popcount(core.mask_of(S) & core.mask_of(T))
            pred = max(0, c - K)
            if d == pred:
                ok += 1
            else:
                bad.append((S, T, c, d, pred))
        res.append(dict(cfg=cfg, pairs=ok + len(bad), agree=ok,
                        disagree=bad[:5]))
        print(f"  (L1) n={n} q={q} K={K} h={h}: {ok}/{ok+len(bad)} exact")
    return res


def stage_rank():
    """rank of the planting system: random-spread vs split-fibre."""
    rng = random.Random(11)
    n, q, K, h, A, D = setup(CFG)
    r = n - K
    out = []
    for M in [1, 2, 3, 5, 8, 10, 11, 12, 16, 20, 24]:
        fam = rand_spread(n, A, K, M, rng)
        if len(fam) < M:
            break
        zs = rng.sample(range(1, q), M)
        rows = cond_rows(list(zip(fam, zs)), D, h, q, n)
        rk = core.rank_mod(rows, q)
        out.append(dict(M=M, rows=M * h, rank=rk, cap=2 * r,
                        predicted=min(M * h, 2 * r),
                        full=rk == min(M * h, 2 * r),
                        kernel_beyond_codewords=2 * n - rk - 2 * K))
        print(f"  random spread M={M:2d} rows={M*h:3d} rank={rk:3d} "
              f"(pred {min(M*h,2*r)}) free-dims-beyond-codewords="
              f"{2*n-rk-2*K}")
    # split-fibre family at the same scale: n=20, m=2 -> F=10, A=7=g+2a
    m, g, a = 2, 1, 3
    nf = n // m
    fib = [[j + t * nf for t in range(m)] for j in range(nf)]
    corei = [nf - 1]                      # one point of the last fibre
    pool = [j for j in range(nf - 1)]
    sf, zs = [], []
    for J in combinations(pool, a):
        S = tuple(sorted(set(corei) | {i for j in J for i in fib[j]}))
        assert len(S) == A
        sf.append(S)
        zs.append(sum(D[m * j] for j in J) % q)
    rows = cond_rows(list(zip(sf, zs)), D, h, q, n)
    rk = core.rank_mod(rows, q)
    masks = [core.mask_of(S) for S in sf]
    sfout = dict(M=len(sf), rows=len(sf) * h, rank=rk, cap=2 * r,
                 max_pair_core=core.max_pair_core(masks), K=K,
                 gamma_lo=len(core.gamma_lo(masks, K)),
                 distinct_slopes=len(set(zs)),
                 kernel_beyond_codewords=2 * n - rk - 2 * K)
    print(f"  SPLIT-FIBRE  M={len(sf)} rows={len(sf)*h} rank={rk} "
          f"(cap {2*r}) maxcore={sfout['max_pair_core']} (K={K}) "
          f"Gamma_lo={sfout['gamma_lo']} free-dims={sfout['kernel_beyond_codewords']}")
    return dict(random_spread=out, split_fibre=sfout, two_r=2 * r,
                ceiling_slopes_fixed=(2 * r - 1) // h,
                ceiling_slopes_free=(2 * r - 1) // (h - 1))


def stage_plant():
    """explicit linear planting at the ceiling + exact verification."""
    rng = random.Random(7)
    n, q, K, h, A, D = setup(CFG)
    r = n - K
    Mmax = (2 * r - 1) // h
    best = None
    for attempt in range(12):
        fam = rand_spread(n, A, K, Mmax, rng)
        zs = rng.sample(range(1, q), Mmax)
        rows = cond_rows(list(zip(fam, zs)), D, h, q, n)
        rk = core.rank_mod(rows, q)
        ns = core.nullspace_mod(rows, 2 * n, q)
        # discard the trivial RS_K x RS_K part: keep solutions whose v is not
        # a codeword.
        cand = None
        for _ in range(60):
            coef = [rng.randrange(q) for _ in ns]
            w = [0] * (2 * n)
            for cf, b in zip(coef, ns):
                if cf:
                    for i in range(2 * n):
                        w[i] = (w[i] + cf * b[i]) % q
            u, v = w[:n], w[n:]
            if not any(v):
                continue
            # v a codeword?  interpolate and check degree
            Pv = interpolate(D, v, q)
            if core.deg(Pv) < K:
                continue
            Pu = interpolate(D, u, q)
            cand = (u, v, Pu, Pv)
            break
        if cand is None:
            continue
        u, v, Pu, Pv = cand
        W = all_witnesses(u, v, D, n, K, h, q, A)
        got = {(z, S) for z, S in W}
        planted_ok = all((z, tuple(S)) in got for S, z in zip(fam, zs))
        byz = {}
        for z, S in W:
            byz.setdefault(z, []).append(S)
        sel = [core.mask_of(min(v2)) for v2 in byz.values()]
        lo = core.gamma_lo(sel, K)
        best = dict(M_planted=Mmax, rank=rk, two_r=2 * r,
                    nullspace_dim=len(ns),
                    planted_all_verified=planted_ok,
                    deg_u=core.deg(Pu), deg_v=core.deg(Pv), K=K,
                    v_nowhere_zero=all(x % q for x in v),
                    total_witnesses=len(W), live_slopes=len(byz),
                    mean_supply=len(list(combinations(range(n), A)))
                    / q ** (h - 1),
                    gamma_lo_lex=len(lo),
                    planted_in_gamma_lo=sum(
                        1 for S, z in zip(fam, zs)
                        if core.mask_of(S) in [sel[i] for i in lo]),
                    planted_is_first_match=sum(
                        1 for S, z in zip(fam, zs)
                        if min(byz[z]) == tuple(S)),
                    max_pair_core_planted=core.max_pair_core(
                        [core.mask_of(S) for S in fam]),
                    planted_supports=[list(S) for S in fam],
                    planted_slopes=zs)
        break
    print(f"  planted M={best['M_planted']} verified={best['planted_all_verified']} "
          f"| deg u={best['deg_u']} deg v={best['deg_v']} (K={K}) "
          f"| total witnesses={best['total_witnesses']} "
          f"live={best['live_slopes']} (mean supply {best['mean_supply']:.3g}) "
          f"| Gamma_lo(lex)={best['gamma_lo_lex']} "
          f"planted-first-match={best['planted_is_first_match']}/{best['M_planted']}")
    return best


def interpolate(D, w, q):
    """unique poly of degree < n through (D_i, w_i)."""
    n = len(D)
    P = [0] * n
    for i in range(n):
        if w[i] == 0:
            continue
        num = [1]
        den = 1
        for j in range(n):
            if j != i:
                num = core.pmul(num, [(-D[j]) % q, 1], q)
                den = den * (D[i] - D[j]) % q
        c = w[i] * pow(den, q - 2, q) % q
        for t in range(len(num)):
            P[t] = (P[t] + c * num[t]) % q
    return core.ptrim(P)


def stage_orbit():
    """F2 exhibit: mu_n-orbit of the monomial pencil U=X^A, V=-X^{A-1}.

    Witness set = {S : h_j(S) = h_1(S)^j} is mu_n-invariant, so it splits
    into orbits of size n, each carrying n distinct slopes -- a family whose
    planting system has M*h = n*h rows against a cap of 2(n-K): a guaranteed
    rank deficit, with NO self-collision if the orbit is spread.
    """
    n, q, K, h, A, D = setup(CFG_ORB)
    U = [0] * (A + 1)
    U[A] = 1
    V = [0] * A
    V[A - 1] = (-1) % q
    u = [core.peval(U, x, q) for x in D]
    v = [core.peval(V, x, q) for x in D]
    W = all_witnesses(u, v, D, n, K, h, q, A)
    bym = {}
    for z, S in W:
        bym[core.mask_of(S)] = z
    # orbits under x -> omega x  (index shift by 1)
    def shift(mask):
        r = ((mask << 1) | (mask >> (n - 1))) & ((1 << n) - 1)
        return r
    seen, orbits = set(), []
    for msk in bym:
        if msk in seen:
            continue
        orb, cur = [], msk
        while cur not in seen:
            seen.add(cur)
            orb.append(cur)
            cur = shift(cur)
            if cur not in bym:
                break
        orbits.append(orb)
    full = [o for o in orbits if len(o) == n]
    spread_orbits = []
    for o in full:
        if core.max_pair_core(o) <= K - 1:
            spread_orbits.append(o)
    res = dict(n=n, q=q, K=K, h=h, A=A, witnesses=len(W),
               distinct_supports=len(bym),
               mean_supply=len(list(combinations(range(n), A))) / q ** (h - 1),
               orbits=len(orbits), full_orbits=len(full),
               orbit_closed=all(shift(m) in bym for m in bym),
               spread_full_orbits=len(spread_orbits),
               two_r=2 * (n - K), rows_for_one_orbit=n * h,
               ceiling_slopes_fixed=(2 * (n - K) - 1) // h)
    if spread_orbits or full:
        o = spread_orbits[0] if spread_orbits else full[0]
        res["example_orbit_is_spread"] = bool(spread_orbits)
        res["example_orbit_maxcore"] = core.max_pair_core(o)
        res["example_orbit_gamma_lo"] = len(core.gamma_lo(o, K))
        res["example_orbit_greedy_spread"] = len(core.greedy_spread(o, K))
        fam_o = [(tuple(i for i in range(n) if (m >> i) & 1), bym[m])
                 for m in o]
        rows = cond_rows(fam_o, D, h, q, n)
        res["orbit_rank"] = core.rank_mod(rows, q)
    print(f"  monomial pencil U=X^{A}, V=-X^{A-1}: witnesses={len(W)} "
          f"(mean supply {res['mean_supply']:.4g}) orbit-closed="
          f"{res['orbit_closed']} full orbits={len(full)} "
          f"spread full orbits={len(spread_orbits)}")
    if full:
        print(f"   example orbit: maxcore={res['example_orbit_maxcore']} "
              f"(K={K}) Gamma_lo={res['example_orbit_gamma_lo']} "
              f"greedy-spread={res['example_orbit_greedy_spread']} "
              f"rank={res['orbit_rank']} rows={n*h} cap={2*(n-K)}")
    return res


def quad_roots(c2, c1, c0, q, SQ):
    """exact roots of c2 t^2 + c1 t + c0 over F_q (q odd prime)."""
    if c2 == 0:
        if c1 == 0:
            return []
        return [(-c0) * pow(c1, q - 2, q) % q]
    inv2a = pow(2 * c2 % q, q - 2, q)
    disc = (c1 * c1 - 4 * c2 * c0) % q
    if disc == 0:
        return [(-c1) * inv2a % q]
    s = SQ.get(disc)
    if s is None:
        return []
    return sorted({(-c1 + s) * inv2a % q, (-c1 - s) * inv2a % q})


def stage_extend():
    """the NONLINEAR design ceiling.

    Planting M supports at PRESCRIBED slopes costs Mh linear conditions, so
    M <= (2r-1)/h.  Leaving the slopes free makes each witness only h-1
    determinantal conditions, so the true ceiling should be

        M* = (2r-1)/(h-1).

    Test: plant M0 = (2r-1)//h supports linearly (kernel = codewords + a
    2-dim space -> a projective LINE of q+1 admissible pencils), then scan
    that whole 1-parameter family EXACTLY and record, for each member, the
    largest spread witness family it carries.
    """
    rng = random.Random(3)
    n, q, K, h, A, D = setup(CFG)
    r = n - K
    M0 = (2 * r - 1) // h
    fam = rand_spread(n, A, K, M0, rng)
    zs = rng.sample(range(1, q), M0)
    rows = cond_rows(list(zip(fam, zs)), D, h, q, n)
    ns = core.nullspace_mod(rows, 2 * n, q)
    # pick two solutions independent modulo RS_K x RS_K
    base = []
    for bvec in ns:
        u, v = bvec[:n], bvec[n:]
        Pu, Pv = interpolate(D, u, q), interpolate(D, v, q)
        if core.deg(Pu) >= K or core.deg(Pv) >= K:
            base.append((u, v))
        if len(base) == 2:
            break
    assert len(base) == 2, "need a 1-parameter family"
    (u0, v0), (u1, v1) = base

    SQ = {}
    for x in range(1, q):
        SQ.setdefault(x * x % q, x)
    xp = [[pow(D[i], t, q) for t in range(h)] for i in range(n)]
    hits = {}                       # t -> list of (z, mask)
    for S in combinations(range(n), A):
        L = core.lam(S, D, q)
        sa = [0] * h; sb = [0] * h; sc = [0] * h; sd = [0] * h
        for k, i in enumerate(S):
            l = L[k]
            ca, cb = l * u0[i] % q, l * u1[i] % q
            cc, cd = l * v0[i] % q, l * v1[i] % q
            for t in range(h):
                xt = xp[i][t]
                sa[t] = (sa[t] + ca * xt) % q
                sb[t] = (sb[t] + cb * xt) % q
                sc[t] = (sc[t] + cc * xt) % q
                sd[t] = (sd[t] + cd * xt) % q
        # sigma_S(u)=sa+t*sb, sigma_S(v)=sc+t*sd; need all 2x2 minors = 0
        quads = []
        for i2 in range(h):
            for j2 in range(i2 + 1, h):
                c2 = (sb[i2] * sd[j2] - sb[j2] * sd[i2]) % q
                c1 = (sa[i2] * sd[j2] + sb[i2] * sc[j2]
                      - sa[j2] * sd[i2] - sb[j2] * sc[i2]) % q
                c0 = (sa[i2] * sc[j2] - sa[j2] * sc[i2]) % q
                quads.append((c2, c1, c0))
        if all(c == 0 for qd in quads for c in qd):
            roots = list(range(q))          # witness for every t
        else:
            roots = None
            for (c2, c1, c0) in quads:
                if c2 == 0 and c1 == 0 and c0 == 0:
                    continue
                rs = quad_roots(c2, c1, c0, q, SQ)
                roots = set(rs) if roots is None else roots & set(rs)
                if not roots:
                    break
            roots = sorted(roots or [])
        msk = core.mask_of(S)
        for t in roots:
            uu = [(u0[i] + t * u1[i]) % q for i in range(n)]
            vv = [(v0[i] + t * v1[i]) % q for i in range(n)]
            sv = [0] * h
            su = [0] * h
            for k, i in enumerate(S):
                a2, b2 = L[k] * uu[i] % q, L[k] * vv[i] % q
                for tt in range(h):
                    su[tt] = (su[tt] + a2 * xp[i][tt]) % q
                    sv[tt] = (sv[tt] + b2 * xp[i][tt]) % q
            if all(x == 0 for x in sv):
                continue
            t0 = next(x for x in range(h) if sv[x])
            z = (-su[t0]) * pow(sv[t0], q - 2, q) % q
            if all((su[x] + z * sv[x]) % q == 0 for x in range(h)):
                hits.setdefault(t, []).append((z, msk))

    best = (0, None)
    tbl = []
    for t, lst in sorted(hits.items()):
        byz = {}
        for z, msk in lst:
            byz.setdefault(z, min(byz.get(z, msk), msk))
        sel = list(byz.values())
        sp = len(core.greedy_spread(sel, K))
        lo = len(core.gamma_lo(sel, K))
        tbl.append(dict(t=t, witnesses=len(lst), live=len(byz),
                        greedy_spread=sp, gamma_lo=lo))
        if sp > best[0]:
            best = (sp, t)
    res = dict(n=n, q=q, K=K, h=h, A=A, two_r=2 * r,
               M0_linear=M0, ceiling_slopes_fixed=(2 * r - 1) // h,
               ceiling_slopes_free=(2 * r - 1) // (h - 1),
               family_members=len(hits),
               max_greedy_spread=best[0], argmax_t=best[1],
               mean_supply=len(list(combinations(range(n), A))) / q ** (h - 1),
               table=sorted(tbl, key=lambda d: -d["greedy_spread"])[:15])
    print(f"  1-parameter family of {len(hits)} pencils, each planting the "
          f"same M0={M0} spread supports")
    print(f"  max spread witness family over the family = {best[0]} "
          f"(ceiling: slopes-fixed {(2*r-1)//h}, slopes-free "
          f"{(2*r-1)//(h-1)}); mean supply {res['mean_supply']:.3g}")
    return res


STAGES = dict(lemma=stage_lemma, rank=stage_rank, plant=stage_plant,
              orbit=stage_orbit, extend=stage_extend)

if __name__ == "__main__":
    acc = {}
    for st in (sys.argv[1:] or ["lemma"]):
        print(f"[{st}]")
        acc[st] = STAGES[st]()
        p = os.path.join(HERE, f"EXPC_{st}.json")
        with open(p, "w") as fh:
            json.dump(acc[st], fh, indent=1, sort_keys=True, default=str)
        print(f"   -> {p}")
