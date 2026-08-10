#!/usr/bin/env python3
"""d3_wide.py -- rh_farca_upper (round 32), D3 scaled measurements.

Measures, at small cells IN THE WIDE REGIME r > R/2 (= the open bracket's
analogue, a < (n+k)/2), the TRUE B_ca^far(a) = max over column-far
2-planes of the number of CA-bad slopes, together with the generic rank
rho of the syndrome Hankel pencil.

Conventions follow rate_half_ca_hankel_split_pencil_equivalence:
  v_x = 1/prod_{y!=x}(x-y),  y_m = sum_x e(x) v_x x^m  (0<=m<R),
  M_r(y) = (y_{i+j}), shape (R-r) x (r+1).
Column-farness is the plane invariant (HS2): W is NOT contained in
colspan(H_X) for any r-subset X.  Bad point [w]: w = H e, wt(e) <= r.

Stdlib only.  Run under: tools/ramguard local -- python3 <this>
"""
import itertools
import random
import sys
import time
from math import comb

T0 = time.time()
WALL = 250.0
OUT = "notes/pilots_20260810/rh_farca_upper/d3_wide_results.txt"
LINES = []


def emit(s):
    LINES.append(s)
    with open(OUT, "w") as fh:
        fh.write("\n".join(LINES) + "\n")


def inv(x, q):
    return pow(x, q - 2, q)


def build(n, k, q):
    """domain D = 0..n-1 in F_q; H[m][x] = v_x x^m, m=0..R-1."""
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
    """rank of a list-of-rows matrix over F_q (destructive on a copy)."""
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
    """map syndrome-code -> list of supports (bitmasks) of weight <= r."""
    tbl = {}
    pw = [q ** i for i in range(R)]

    def code(s):
        return sum(s[i] * pw[i] for i in range(R))

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
                c = code(s)
                lst = tbl.get(c)
                if lst is None:
                    tbl[c] = [mask]
                elif mask not in lst:
                    lst.append(mask)
    tbl[0] = [0]
    return tbl, pw, code


def planes(R, q):
    """all 2-dim subspaces of F_q^R, RREF Schubert cells."""
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


def hankel(w, R, r):
    return [[w[i + j] for j in range(r + 1)] for i in range(R - r)]


def analyse(s0, s1, R, r, q, tbl, pw, n, H, want_rho=True):
    """returns (n_bad, colfar, rho, bad_pts) for the plane span(s0,s1)."""
    bad = []
    for g in range(q):
        w = [(s0[m] + g * s1[m]) % q for m in range(R)]
        c = sum(w[i] * pw[i] for i in range(R))
        if c in tbl:
            bad.append((g, w))
    c = sum(s1[i] * pw[i] for i in range(R))
    if c in tbl:
        bad.append((None, s1[:]))
    nb = len(bad)
    colfar = True
    if nb == q + 1:
        # expensive check: is the whole plane inside some colspan(H_X)?
        for X0 in tbl[sum(s0[i] * pw[i] for i in range(R))]:
            for X1 in tbl[sum(s1[i] * pw[i] for i in range(R))]:
                u = X0 | X1
                if bin(u).count("1") <= r:
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


def census(n, k, r, q, mode, nsamp=0):
    a = n - r
    R, D, H = build(n, k, q)
    assert r > R / 2 and a > k, "cell not in the wide/interior regime"
    tbl, pw, code = syn_table(n, R, H, q, r)
    tag = f"cell n={n} k={k} a={a} r={r} R={R} q={q} [{mode}]"
    emit("")
    emit("=" * 72)
    emit(tag)
    emit(f"  wide: r>R/2 ({r}>{R/2}); a-k={a-k}; r+1={r+1}; R-r={R-r}; "
         f"C(n,r)={comb(n, r)}; |B_r|={len(tbl)}; q^R={q**R}")
    dist = {}
    maxT = -1
    maxrec = None
    defmax = -1
    defrec = None
    ndef = 0
    ncf = 0
    nviol = 0
    src = planes(R, q) if mode == "exhaustive" else None
    cnt = 0
    while True:
        if src is not None:
            try:
                s0, s1 = next(src)
            except StopIteration:
                break
        else:
            if cnt >= nsamp:
                break
            s0 = [random.randrange(q) for _ in range(R)]
            s1 = [random.randrange(q) for _ in range(R)]
            if rank([s0, s1], q) < 2:
                continue
        cnt += 1
        if cnt % 20000 == 0 and time.time() - T0 > WALL:
            emit(f"  WALL HIT after {cnt} planes -- PARTIAL")
            break
        nb, colfar, rho, bad = analyse(s0, s1, R, r, q, tbl, pw, n, H)
        if not colfar:
            continue
        ncf += 1
        dist[nb] = dist.get(nb, 0) + 1
        if nb > maxT:
            maxT = nb
            maxrec = (s0[:], s1[:], rho, [b[0] for b in bad])
        if rho < R - r:
            ndef += 1
            if nb > defmax:
                defmax = nb
                defrec = (s0[:], s1[:], rho, nb)
            if nb > rho:
                nviol += 1
    emit(f"  planes scanned={cnt}  column-far={ncf}")
    emit(f"  T distribution (bad projective points) = "
         f"{dict(sorted(dist.items()))}")
    emit(f"  MAX T over column-far planes = {maxT}   (r+1={r+1}, "
         f"C(n,r)={comb(n,r)}, q+1={q+1})")
    if maxrec:
        emit(f"    witness s0={maxrec[0]} s1={maxrec[1]} rho={maxrec[2]} "
             f"slopes={maxrec[3]}")
    emit(f"  DEFICIENT stratum (rho < R-r = {R-r}): {ndef} planes; "
         f"max T there = {defmax}; UB-DEFICIENT violations (T>rho) = {nviol}")
    if defrec:
        emit(f"    deficient witness s0={defrec[0]} s1={defrec[1]} "
             f"rho={defrec[2]} T={defrec[3]}")
    return maxT, r + 1


def lb1(n, k, r, q, trials=200):
    """round-31 LB1 construction: core E of size a-1, T = complement."""
    a = n - r
    R, D, H = build(n, k, q)
    tbl, pw, code = syn_table(n, R, H, q, r)
    Tset = list(range(a - 1, n))
    assert len(Tset) == r + 1
    best = None
    ok = 0
    for _ in range(trials):
        lams = random.sample(range(1, q), min(r + 1, q - 1))
        if len(lams) < r + 1:
            return None
        d2 = [0] * n
        d1 = [0] * n
        for j, x in enumerate(Tset):
            d2[x] = 1
            d1[x] = (-lams[j]) % q
        s0 = [sum(d1[x] * H[m][x] for x in range(n)) % q for m in range(R)]
        s1 = [sum(d2[x] * H[m][x] for x in range(n)) % q for m in range(R)]
        if rank([s0, s1], q) < 2:
            continue
        nb, colfar, rho, bad = analyse(s0, s1, R, r, q, tbl, pw, n, H)
        if colfar:
            ok += 1
            if best is None or nb > best[0]:
                best = (nb, rho, sorted(x for x in
                                        [b[0] for b in bad] if x is not None))
    emit(f"  LB1 at n={n} k={k} a={a} r={r} q={q}: column-far in {ok}/{trials}"
         f" random lam-assignments; best (T, rho, slopes) = {best}; "
         f"predicted T>=r+1={r+1}, predicted rho=R-r={R-r}")
    return best


def main():
    random.seed(20260810)
    emit("d3_wide.py -- rh_farca_upper round 32")
    emit("MAX T counts BAD PROJECTIVE POINTS on P(W) (q+1 of them);"
         " the finite-slope count of the theory is this minus at most 1.")

    # ---- a-k = 1 family (registered ZERO POWER, run as a control) ----
    for q in (7, 11, 13, 17, 31):
        census(6, 3, 2, q, "exhaustive")
    for q in (7, 11, 13):
        census(7, 3, 3, q, "exhaustive")
    for q in (7, 11):
        census(6, 2, 3, q, "exhaustive")

    # ---- a-k = 2 family (the informative one: deficient stratum exists) ----
    census(7, 2, 3, 7, "exhaustive")
    if time.time() - T0 < WALL:
        census(7, 2, 3, 11, "sample", 120000)
    if time.time() - T0 < WALL:
        census(7, 2, 3, 13, "sample", 80000)
    if time.time() - T0 < WALL:
        census(8, 3, 3, 11, "sample", 60000)
    if time.time() - T0 < WALL:
        census(9, 2, 4, 11, "sample", 40000)

    emit("")
    emit("=" * 72)
    emit("LB1 replay (round-31 construction) in the wide regime")
    for (n, k, r, q) in ((6, 3, 2, 17), (7, 3, 3, 13), (7, 2, 3, 11),
                         (8, 3, 3, 11), (9, 2, 4, 11)):
        if time.time() - T0 > WALL + 20:
            emit("  WALL -- remaining LB1 cells NOT MEASURED")
            break
        lb1(n, k, r, q)
    emit("")
    emit(f"elapsed {time.time()-T0:.1f}s")


main()
print("\n".join(LINES[-40:]))
