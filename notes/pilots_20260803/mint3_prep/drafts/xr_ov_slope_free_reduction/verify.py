#!/usr/bin/env python3
"""Verifier for xr_ov_slope_free_reduction.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Pure python integers, deterministic, no third-party imports, NO FILE
READS.  PG(2,3) and MINWIT are CONSTRUCTED FROM SCRATCH here rather than
imported from the sibling pilot, so this node survives the move.

REMINDER: CONJECTURE OV IS OPEN.  Nothing below closes it.

  A  the MDS fact, and THEOREM 1's three dictionary rows, on both
     overlapping fixtures
  B  zero escape  =>  the intersection of all pair-unions is EMPTY
  C  dim Jperp computed TWO INDEPENDENT WAYS (dual-code/support route
     and the direct subspace-intersection route) -- they must agree
  D  THEOREM 2, tested directly: over many (system, slope tuple) pairs,
     never Jperp = 0 with Ann != 0; and Ann != 0 => dim Jperp >= 2,
     on a DISJOINT pencil-fibre witness of the banked X1 shape
  E  PG(2,3): gate-clean, OVERLAPPING, zero-escape, and dim Jperp = 0
     over several point sets
  F  THEOREM 5's hypotheses on PG(2,3) (uniform mu = 4, V-1-mu = 8) and
     the e_1 disjoint/overlap separator
  G  the r > d residual and OV's openness, recorded as NOT-claimed
"""
from __future__ import annotations

import sys
from itertools import combinations

sys.dont_write_bytecode = True

FAILURES = []


def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    if not ok:
        FAILURES.append(label)


# ------------------------------------------------------------ linear algebra

def rref(M, q):
    M = [[x % q for x in r] for r in M]
    nr = len(M)
    nc = len(M[0]) if M else 0
    piv, r = [], 0
    for c in range(nc):
        p = next((i for i in range(r, nr) if M[i][c]), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = pow(M[r][c], q - 2, q)
        M[r] = [x * inv % q for x in M[r]]
        for i in range(nr):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % q for j in range(nc)]
        piv.append(c)
        r += 1
        if r == nr:
            break
    return M[:r], piv


def rank(M, q):
    if not M:
        return 0
    return len(rref(M, q)[0])


def nullspace(M, q, nc):
    """basis of {y : M y^T = 0}, y of length nc."""
    if not M:
        return [[1 if i == j else 0 for i in range(nc)] for j in range(nc)]
    R, piv = rref(M, q)
    free = [c for c in range(nc) if c not in piv]
    basis = []
    for f in free:
        v = [0] * nc
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-R[i][f]) % q
        basis.append(v)
    return basis


def subspace_sum_rank(bases, q, nc):
    rows = [v for b in bases for v in b]
    return rank(rows, q) if rows else 0


def intersect(B1, B2, q, nc):
    """basis of span(B1) ^ span(B2)."""
    if not B1 or not B2:
        return []
    # y = sum a_i B1_i = sum b_j B2_j  ->  nullspace of [B1^T | -B2^T]
    rows = []
    for c in range(nc):
        rows.append([B1[i][c] for i in range(len(B1))]
                    + [(-B2[j][c]) % q for j in range(len(B2))])
    ns = nullspace(rows, q, len(B1) + len(B2))
    out = []
    for v in ns:
        y = [0] * nc
        for i in range(len(B1)):
            if v[i]:
                for c in range(nc):
                    y[c] = (y[c] + v[i] * B1[i][c]) % q
        if any(y):
            out.append(y)
    R, _ = rref(out, q) if out else ([], [])
    return R


# ---------------------------------------------------------------- the system

def rs_rows(xs, k, q):
    return [[pow(x, j, q) for x in xs] for j in range(k)]


def jperp_dual_route(xs, blocks, k, q):
    """dim Jperp via the DUAL/SUPPORT route:
    (W_a + W_b)^perp = {y in (RS_k|_U)^perp : supp(y) ^ (A_a u A_b) = empty};
    J = sum of those, dim Jperp = m - dim J."""
    n = len(xs)
    m = n - k
    R = rs_rows(xs, k, q)
    perps = []
    for a, b in combinations(range(len(blocks)), 2):
        S = set(blocks[a]) | set(blocks[b])
        rows = [r[:] for r in R]
        for x in sorted(S):
            e = [0] * n
            e[x] = 1
            rows.append(e)
        perps.append(nullspace(rows, q, n))
    dimJ = subspace_sum_rank(perps, q, n)
    return m - dimJ


def jperp_direct_route(xs, blocks, k, q):
    """dim Jperp via DIRECT subspace intersection inside W = F^U/RS.
    Preimage of W_a + W_b is span{delta_x : x in A_a u A_b} + RS."""
    n = len(xs)
    m = n - k
    R = rs_rows(xs, k, q)
    cur = None
    for a, b in combinations(range(len(blocks)), 2):
        S = set(blocks[a]) | set(blocks[b])
        rows = [r[:] for r in R]
        for x in sorted(S):
            e = [0] * n
            e[x] = 1
            rows.append(e)
        pre, _ = rref(rows, q)
        cur = pre if cur is None else intersect(cur, pre, q, n)
    return rank(cur, q) - k if cur else -k


def ann_dim(xs, blocks, slopes, k, q):
    """dim Ann = dim{(lam,mu,(p_a)) : (lam + z_a mu)|_{S_a} = p_a|_{S_a}} - 2k.
    Unknown vector: lam (n) | mu (n) | p_0..p_{V-1} (k each)."""
    n = len(xs)
    V = len(blocks)
    nc = 2 * n + V * k
    rows = []
    for a in range(V):
        S = [x for x in range(n) if x not in set(blocks[a])]
        for x in S:
            r = [0] * nc
            r[x] = 1
            r[n + x] = slopes[a] % q
            for j in range(k):
                r[2 * n + a * k + j] = (-pow(xs[x], j, q)) % q
            rows.append(r)
    return len(nullspace(rows, q, nc)) - 2 * k


# ------------------------------------------------------------ the fixtures

def pg23():
    """PG(2,3): 13 points of P^2(F_3), 13 lines of size 4."""
    pts = []
    for a in range(3):
        for b in range(3):
            pts.append((1, a, b))
    for b in range(3):
        pts.append((0, 1, b))
    pts.append((0, 0, 1))
    assert len(pts) == 13
    lines = []
    for c in pts:
        L = [i for i, p in enumerate(pts)
             if sum(c[t] * p[t] for t in range(3)) % 3 == 0]
        lines.append(sorted(L))
    assert all(len(L) == 4 for L in lines) and len(lines) == 13
    return pts, lines


MINWIT_BLOCKS = [[0, 3, 4, 8], [2, 3, 6, 10], [0, 1, 5, 10],
                 [1, 4, 6, 7], [5, 6, 8, 9], [0, 2, 7, 9]]
MINWIT_NU = 11


def gates(n_U, blocks, k):
    V = len(blocks)
    mult = [sum(1 for B in blocks if x in B) for x in range(n_U)]
    sup = [set(range(n_U)) - set(B) for B in blocks]
    pair = min(len(sup[a] & sup[b]) for a, b in combinations(range(V), 2))
    tri = max(len(sup[a] & sup[b] & sup[c])
              for a, b, c in combinations(range(V), 3))
    return dict(mult=mult, zero_escape=max(mult) <= V - 3,
                pairwise=pair >= k + 1, T=tri <= k - 1,
                pair_min=pair, tri_max=tri, V=V,
                overlapping=any(set(blocks[a]) & set(blocks[b])
                                for a, b in combinations(range(V), 2)))


# ------------------------------------------------------------------ stages

def stage_A_B():
    for name, n_U, blocks, k in (("PG(2,3)", 13, pg23()[1], 5),
                                 ("MINWIT", MINWIT_NU, MINWIT_BLOCKS, 3)):
        g = gates(n_U, blocks, k)
        m = n_U - k
        V = g["V"]
        # THEOREM 1 rows
        pair_ok = all(len(set(blocks[a]) | set(blocks[b])) <= m - 1
                      for a, b in combinations(range(V), 2))
        tri_ok = all(len(set(blocks[a]) | set(blocks[b]) | set(blocks[c])) >= m + 1
                     for a, b, c in combinations(range(V), 3))
        inter = set(range(n_U))
        for a, b in combinations(range(V), 2):
            inter &= (set(blocks[a]) | set(blocks[b]))
        check(f"A ({name}) THEOREM 1 dictionary: pair-unions have size "
              f"<= m-1 (always INDEPENDENT by MDS) and triple-unions have "
              f"size >= m+1 (always DEPENDENT) -- the WALL explanation",
              g["zero_escape"] and g["pairwise"] and g["T"] and pair_ok and tri_ok,
              f"m={m} V={V} pair_min={g['pair_min']} tri_max={g['tri_max']} "
              f"overlapping={g['overlapping']}")
        check(f"B ({name}) zero escape => the intersection of ALL pair-unions "
              f"is EMPTY", not inter and g["zero_escape"],
              f"max mult={max(g['mult'])} <= V-3={V-3}; intersection={sorted(inter)}")


def stage_C_E():
    _, lines = pg23()
    for q in (17, 23, 29):
        xs = list(range(1, 14))
        d1 = jperp_dual_route(xs, lines, 5, q)
        d2 = jperp_direct_route(xs, lines, 5, q)
        check(f"C/E PG(2,3) q={q}: dim Jperp computed TWO INDEPENDENT WAYS "
              f"agrees, and equals 0 -- the parameter-free obstruction "
              f"VANISHES on this overlapping system",
              d1 == d2 == 0, f"dual-route={d1} direct-route={d2}")
    for q in (17, 23):
        xs = list(range(1, MINWIT_NU + 1))
        d1 = jperp_dual_route(xs, MINWIT_BLOCKS, 3, q)
        d2 = jperp_direct_route(xs, MINWIT_BLOCKS, 3, q)
        check(f"C/E MINWIT q={q}: the two routes agree and dim Jperp = 0",
              d1 == d2 == 0, f"dual-route={d1} direct-route={d2}")


def build_pencil_fixture(q, t, V):
    """V disjoint blocks of size t as fibres of a degree-t pencil (the X1
    mechanism).  Returns (xs, blocks, params) or None."""
    U = list(range(q))
    from itertools import combinations as C

    def loc(pts):
        e = [1]
        for x in pts:
            ne = [0] * (len(e) + 1)
            for i, c in enumerate(e):
                ne[i] = (ne[i] - c * x) % q
                ne[i + 1] = (ne[i + 1] + c) % q
            e = ne
        return e

    def rts(p):
        out = []
        for x in U:
            v = 0
            for c in reversed(p):
                v = (v * x + c) % q
            if v == 0:
                out.append(x)
        return out

    for B1 in C(U, t):
        for B2 in C([x for x in U if x not in B1], t):
            p1, p2 = loc(B1), loc(B2)
            fib, par = [list(B1)], [0]
            for c in range(1, q):
                mem = [(p1[i] - c * p2[i]) % q for i in range(t + 1)]
                if mem[t] == 0:
                    continue
                r = rts(mem)
                if len(r) == t:
                    fib.append(r)
                    par.append(c)
            if len(fib) >= V:
                pts = sorted({x for B in fib[:V] for x in B})
                idx = {x: i for i, x in enumerate(pts)}
                return pts, [sorted(idx[x] for x in B) for B in fib[:V]], par[:V]
    return None


def stage_D():
    """THEOREM 2, tested directly on the banked X1 SHAPE (t=2,V=4,k=3,m=5)."""
    q, t, V, k = 17, 2, 4, 3
    fx = build_pencil_fixture(q, t, V)
    if fx is None:
        check("D (THEOREM 2): pencil-fibre fixture construction", False,
              "no fixture found")
        return
    xs, blocks, par = fx
    n_U = len(xs)
    g = gates(n_U, blocks, k)
    hits, tested, bad_imp, bad_ge2 = 0, 0, 0, 0
    worst_jp = jperp_dual_route(xs, blocks, k, q)
    for z2 in range(2, q):
        for z3 in range(2, q):
            if z3 == z2:
                continue
            slopes = [0, 1, z2, z3]
            a = ann_dim(xs, blocks, slopes, k, q)
            tested += 1
            if a >= 1:
                hits += 1
                if worst_jp < 2:
                    bad_ge2 += 1
            if worst_jp == 0 and a != 0:
                bad_imp += 1
    check("D (THEOREM 2, tested directly on the banked X1 shape "
          "t=2,V=4,k=3,m=5, DISJOINT blocks = pencil fibres): over every "
          "slope tuple, NEVER Jperp = 0 together with Ann != 0; and "
          "wherever Ann != 0 we have dim Jperp >= 2",
          bad_imp == 0 and bad_ge2 == 0 and tested > 0,
          f"n_U={n_U} dim Jperp={worst_jp}; {tested} slope tuples, "
          f"{hits} with dim Ann >= 1, {bad_imp} implication violations, "
          f"{bad_ge2} Jperp<2 violations; disjoint={not g['overlapping']}")


def stage_F():
    pts, lines = pg23()
    V = len(lines)
    mult = [sum(1 for L in lines if x in L) for x in range(13)]
    mu = mult[0]
    uniform = all(x == mu for x in mult)
    check("F1 (THEOREM 5's hypotheses on PG(2,3)): uniform block "
          "multiplicity mu = 4 with V-1-mu = 8 != 0, and L = 1 (any two "
          "lines meet in exactly one point) -- the theorem applies verbatim",
          uniform and mu == 4 and (V - 1 - mu) == 8
          and all(len(set(lines[a]) & set(lines[b])) == 1
                  for a, b in combinations(range(V), 2)),
          f"mult set={sorted(set(mult))} V={V} V-1-mu={V-1-mu}")

    # F2: the e_1 separator, solved for the POINT SET (exact linear algebra)
    for q in (101, 1009):
        rows = []
        for a, b in combinations(range(V), 2):
            r = [0] * (13 + 1)
            for x in lines[a]:
                r[x] = (r[x] + 1) % q
            for x in lines[b]:
                r[x] = (r[x] + 1) % q
            for x in set(lines[a]) & set(lines[b]):
                r[x] = (r[x] - 1) % q
            r[13] = q - 1                      # the constant C
            rows.append(r)
        ns = nullspace(rows, q, 14)
        # a solution is USABLE only if it gives 13 DISTINCT coordinates
        usable = 0
        for v in ns:
            if len(set(v[:13])) == 13:
                usable += 1
        check(f"F2 (the e_1 disjoint/overlap SEPARATOR) PG(2,3) q={q}: the "
              f"r = d mechanism is DEAD -- the solution space collapses to "
              f"constants, so no usable point set exists",
              len(ns) == 1 and usable == 0,
              f"solution dim={len(ns)}, usable (all-distinct) solutions={usable}")


def stage_G():
    print("NOTE (NOT CLAIMED -- the residual): Jperp = 0 is OPEN exactly in "
          "the branch r > d. For d = 1, dim Jperp >= 1 iff the m vectors "
          "(e_j(A_a u A_b))_pairs, j = 0..m-1, are linearly DEPENDENT; "
          "THEOREM 5 kills only the dependency u_1 in <u_0>, i.e. r = d. "
          "Dependencies involving e_2,...,e_{m-1} are OPEN. The pilot states "
          "plainly: 'I did NOT find a reduction of r > d to r = d, and I do "
          "not claim one.' Named next attack: the s = 1 telescoping cocycle.")
    print("NOTE (NOT CLAIMED -- the conjecture): CONJECTURE OV remains OPEN, "
          "neither proved nor refuted. The two consumers -- overlap_sliver's "
          "V <= |U|/2 upgrade and crosslane_cashout's VERDICT A -- STAY "
          "BLOCKED and may NOT cite this node as a close; they may cite "
          "THEOREM 2 only to re-scope the obligation.")
    print("NOTE (scope): THEOREM 5 is NOT sharp -- MINWIT lies OUTSIDE its "
          "hypotheses (multiplicity vector [3,2,2,2,2,2,3,2,2,2,2], not "
          "uniform) and is dead anyway. All work here is toy scale.")
    check("G: the residual, the openness of OV and the blocked consumers are "
          "recorded as NOT-claimed (this check is a marker, and asserts only "
          "that the node makes no closure claim)", True)


def main():
    stage_A_B()
    stage_C_E()
    stage_D()
    stage_F()
    stage_G()
    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("XR_OV_SLOPE_FREE_REDUCTION_ALL_PASS")


if __name__ == "__main__":
    main()
