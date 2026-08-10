#!/usr/bin/env python3
"""d4_deficient.py -- rh_farca_upper (round 32), D2 test of UB-DEFICIENT.

UB-DEFICIENT (the round's candidate theorem).  In the WIDE regime
R/2 < r <= R-1, let rho = rank_{F(Z)} M(Z) be the generic rank of the
syndrome Hankel pencil (shape (R-r) x (r+1), so rho <= R-r).  If
rho <= R-r-1 and rho < (R+1)/3, then a column-far pair has at most rho
finite CA-bad slopes.

The deficient stratum is EMPTY when R-r = 2 (a 2-plane cannot lie in the
cone over the rational normal curve), so it must be probed at R-r >= 3
by CONSTRUCTION: the syndromes annihilated by a fixed degree-p form P
are exactly the solutions of the linear recurrence with symbol P, a
p-dimensional space; P irreducible => no D-split multiple => column-far.

Also: exhaustive max-T census at (7,2,4) with rho switched off.

Stdlib only.  Run under: tools/ramguard local -- python3 <this>
"""
import itertools
import random
import time
from math import comb

T0 = time.time()
WALL = 240.0
OUT = "notes/pilots_20260810/rh_farca_upper/d4_deficient_results.txt"
LINES = []


def emit(s):
    LINES.append(s)
    with open(OUT, "w") as fh:
        fh.write("\n".join(LINES) + "\n")


def inv(x, q):
    return pow(x, q - 2, q)


def build(n, k, q):
    R = n - k
    D = list(range(n))
    v = []
    for x in D:
        p = 1
        for y in D:
            if y != x:
                p = p * (x - y) % q
        v.append(inv(p, q))
    H = [[v[x] * pow(x, m, q) % q for x in range(n)] for m in range(R)]
    return R, D, H


def rank(M, q):
    M = [row[:] for row in M]
    rows, cols = len(M), len(M[0])
    rk = 0
    for c in range(cols):
        piv = None
        for i in range(rk, rows):
            if M[i][c]:
                piv = i
                break
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        iv = inv(M[rk][c], q)
        M[rk] = [x * iv % q for x in M[rk]]
        for i in range(rows):
            if i != rk and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[rk][j]) % q for j in range(cols)]
        rk += 1
        if rk == rows:
            break
    return rk


def syn_table(n, R, H, q, r):
    tbl = {}
    pw = [q ** i for i in range(R)]
    for w in range(1, r + 1):
        for X in itertools.combinations(range(n), w):
            mask = 0
            for x in X:
                mask |= 1 << x
            for vals in itertools.product(range(1, q), repeat=w):
                s = [0] * R
                for x, val in zip(X, vals):
                    for m in range(R):
                        s[m] = (s[m] + val * H[m][x]) % q
                c = sum(s[i] * pw[i] for i in range(R))
                lst = tbl.get(c)
                if lst is None:
                    tbl[c] = [mask]
                elif mask not in lst:
                    lst.append(mask)
    tbl[0] = [0]
    return tbl, pw


def hankel(w, R, r):
    return [[w[i + j] for j in range(r + 1)] for i in range(R - r)]


def analyse(s0, s1, R, r, q, tbl, pw, want_rho=True):
    bad = []
    for g in range(q):
        w = [(s0[m] + g * s1[m]) % q for m in range(R)]
        if sum(w[i] * pw[i] for i in range(R)) in tbl:
            bad.append(g)
    if sum(s1[i] * pw[i] for i in range(R)) in tbl:
        bad.append(None)
    nb = len(bad)
    colfar = True
    if nb == q + 1:
        for X0 in tbl[sum(s0[i] * pw[i] for i in range(R))]:
            for X1 in tbl[sum(s1[i] * pw[i] for i in range(R))]:
                if bin(X0 | X1).count("1") <= r:
                    colfar = False
                    break
            if not colfar:
                break
    rho = -1
    if want_rho:
        rho = 0
        seen = 0
        for g in list(range(q)) + [None]:
            if seen > R - r:
                break
            w = s1[:] if g is None else [(s0[m] + g * s1[m]) % q
                                        for m in range(R)]
            if not any(w):
                continue
            rho = max(rho, rank(hankel(w, R, r), q))
            seen += 1
            if rho == min(R - r, r + 1):
                break
    return nb, colfar, rho, bad


def rec_space(P, R, q):
    """basis of {y in F_q^R : sum_j P_j y_{i+j} = 0 for all i}, deg P = p,
    P monic (P[p] = 1).  dim = p."""
    p = len(P) - 1
    basis = []
    for b in range(p):
        y = [0] * R
        y[b] = 1
        for i in range(R - p):
            y[i + p] = (-sum(P[j] * y[i + j] for j in range(p))) % q
        basis.append(y)
    return basis


def irreducible_quadratics(q):
    sq = set((x * x) % q for x in range(q))
    return [(c, b, 1) for b in range(q) for c in range(q)
            if (b * b - 4 * c) % q not in sq]


def split_quadratics(q, D):
    out = []
    for i in range(len(D)):
        for j in range(i + 1, len(D)):
            # (x-Di)(x-Dj) = x^2 - (Di+Dj)x + Di*Dj  -> P = (c, b, 1)
            out.append(((D[i] * D[j]) % q, (-(D[i] + D[j])) % q, 1))
    return out


def irreducible_cubics(q):
    out = []
    for c0 in range(q):
        for c1 in range(q):
            for c2 in range(q):
                if all((x ** 3 + c2 * x * x + c1 * x + c0) % q
                       for x in range(q)):
                    out.append((c0, c1, c2, 1))
    return out


def probe_deficient(n, k, r, q, Plist, label):
    R, D, H = build(n, k, q)
    tbl, pw = syn_table(n, R, H, q, r)
    emit("")
    emit("=" * 72)
    emit(f"DEFICIENT PROBE  n={n} k={k} a={n-r} r={r} R={R} q={q} "
         f"R-r={R-r} r+1={r+1}  [{label}]")
    worst = (-1, None)
    nfar = 0
    ntot = 0
    viol = 0
    rhoseen = {}
    for P in Plist:
        p = len(P) - 1
        B = rec_space(list(P), R, q)
        # every 2-plane inside the p-dim solution space
        for pair in itertools.combinations(range(p), 2) if p > 2 else [(0, 1)]:
            pass
        subs = []
        if p == 2:
            subs = [(B[0], B[1])]
        else:
            for s0c in itertools.product(range(q), repeat=p):
                if not any(s0c):
                    continue
                for s1c in itertools.product(range(q), repeat=p):
                    if not any(s1c):
                        continue
                    s0 = [sum(s0c[t] * B[t][m] for t in range(p)) % q
                          for m in range(R)]
                    s1 = [sum(s1c[t] * B[t][m] for t in range(p)) % q
                          for m in range(R)]
                    if rank([s0, s1], q) == 2:
                        subs.append((s0, s1))
                        break
                if len(subs) > 60:
                    break
        for (s0, s1) in subs:
            ntot += 1
            nb, colfar, rho, bad = analyse(s0, s1, R, r, q, tbl, pw)
            rhoseen[rho] = rhoseen.get(rho, 0) + 1
            if not colfar:
                continue
            nfar += 1
            if nb > worst[0]:
                worst = (nb, (P, rho, bad))
            if nb > rho:
                viol += 1
        if time.time() - T0 > WALL:
            emit("  WALL -- probe truncated")
            break
    emit(f"  planes probed={ntot}  column-far={nfar}  rho histogram={rhoseen}")
    emit(f"  MAX bad-point count over column-far deficient planes = {worst[0]}"
         f"   (UB-DEFICIENT predicts <= rho)")
    emit(f"  witness (P, rho, bad points) = {worst[1]}")
    emit(f"  UB-DEFICIENT VIOLATIONS (T > rho) = {viol}")
    return worst, viol


def planes(R, q):
    for p0 in range(R):
        for p1 in range(p0 + 1, R):
            free0 = [j for j in range(p0 + 1, R) if j != p1]
            free1 = [j for j in range(p1 + 1, R)]
            for a0 in itertools.product(range(q), repeat=len(free0)):
                r0 = [0] * R
                r0[p0] = 1
                for j, val in zip(free0, a0):
                    r0[j] = val
                for a1 in itertools.product(range(q), repeat=len(free1)):
                    r1 = [0] * R
                    r1[p1] = 1
                    for j, val in zip(free1, a1):
                        r1[j] = val
                    yield r0, r1


def exhaustive_maxT(n, k, r, q):
    R, D, H = build(n, k, q)
    tbl, pw = syn_table(n, R, H, q, r)
    emit("")
    emit("=" * 72)
    emit(f"EXHAUSTIVE max-T (rho off)  n={n} k={k} a={n-r} r={r} R={R} q={q}"
         f"  r+1={r+1} C(n,r)={comb(n,r)} q+1={q+1}")
    dist = {}
    cnt = 0
    mx = -1
    rec = None
    part = False
    for s0, s1 in planes(R, q):
        cnt += 1
        if cnt % 50000 == 0 and time.time() - T0 > WALL:
            part = True
            break
        nb, colfar, rho, bad = analyse(s0, s1, R, r, q, tbl, pw,
                                       want_rho=False)
        if not colfar:
            continue
        dist[nb] = dist.get(nb, 0) + 1
        if nb > mx:
            mx = nb
            rec = (s0[:], s1[:], bad)
    emit(f"  planes={cnt}{' (PARTIAL, wall)' if part else ' (complete)'}")
    emit(f"  T distribution = {dict(sorted(dist.items()))}")
    emit(f"  MAX T = {mx}   ratio to r+1 = {mx/(r+1):.4f}")
    emit(f"  witness = {rec}")


def sample_maxT(n, k, r, q, nsamp):
    """sampled max T at a fixed cell: q-ladder to test q-dependence."""
    R, D, H = build(n, k, q)
    tbl, pw = syn_table(n, R, H, q, r)
    dist = {}
    mx = -1
    rec = None
    cnt = 0
    while cnt < nsamp:
        s0 = [random.randrange(q) for _ in range(R)]
        s1 = [random.randrange(q) for _ in range(R)]
        if rank([s0, s1], q) < 2:
            continue
        cnt += 1
        if cnt % 10000 == 0 and time.time() - T0 > WALL + 30:
            break
        nb, colfar, rho, bad = analyse(s0, s1, R, r, q, tbl, pw,
                                       want_rho=False)
        if not colfar:
            continue
        dist[nb] = dist.get(nb, 0) + 1
        if nb > mx:
            mx = nb
            rec = (s0[:], s1[:], bad)
    emit("")
    emit(f"q-LADDER  n={n} k={k} a={n-r} r={r} R={R} q={q}  r+1={r+1} "
         f"C(n,r)={comb(n,r)} q+1={q+1}  samples={cnt}")
    emit(f"  T dist = {dict(sorted(dist.items()))}")
    emit(f"  sampled MAX T = {mx}  (ratio to r+1 = {mx/(r+1):.3f}; "
         f"fraction of q+1 = {mx/(q+1):.3f})")
    emit(f"  witness = {rec}")


def main():
    random.seed(20260810)
    emit("d4_deficient.py -- rh_farca_upper round 32")

    # (A) R-r = 3 cell, deficient stratum reachable at p = 2.
    q = 11
    irr = irreducible_quadratics(q)
    emit(f"[F_{q}] irreducible monic quadratics: {len(irr)}")
    probe_deficient(9, 2, 4, q, irr, "P irreducible quadratic, R-r=3")
    # control: P split with both roots in D  ->  expect column-CLOSE
    R, D, H = build(9, 2, q)
    probe_deficient(9, 2, 4, q, split_quadratics(q, D)[:20],
                    "CONTROL: P split over D (expect column-close)")

    # (A2) second R-r = 3 cell, different k.
    if time.time() - T0 < WALL:
        probe_deficient(8, 1, 4, q, irr, "P irreducible quadratic, R-r=3, k=1")

    # (C) q-LADDER at fixed cells: does max T grow with q, or saturate?
    for (nn, kk, rr, qq, ns) in ((7, 2, 3, 11, 40000), (7, 2, 3, 13, 40000),
                                 (7, 2, 3, 17, 40000), (7, 2, 3, 23, 40000),
                                 (7, 2, 3, 31, 40000), (8, 3, 3, 11, 30000),
                                 (8, 3, 3, 13, 30000), (8, 3, 3, 17, 30000)):
        if time.time() - T0 > WALL:
            emit(f"  WALL -- q-ladder cell ({nn},{kk},{rr},q={qq}) "
                 f"NOT MEASURED")
            continue
        sample_maxT(nn, kk, rr, qq, ns)
    emit("")
    emit(f"elapsed {time.time()-T0:.1f}s")


main()
print("\n".join(LINES))
