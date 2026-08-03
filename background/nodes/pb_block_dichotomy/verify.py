#!/usr/bin/env python3
"""Verifier for pb_block_dichotomy.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Pure python integers, deterministic, no third-party imports, no file reads.
All pins inlined; provenance paths appear in comments only.

  A  |S_J ^ S_J'| = |G| + m|J ^ J'| and CLAIM 1's threshold (spread iff
     m >= h+1), on coset-block families
  B  CLAIM 2 (SF-SELFCOLLISION derived): at m <= h every member has a
     partner at core >= K
  C  the coset identity prod_{x in g mu_m}(X - x) = X^m - g^m, the
     e-vector support, and p_t = m g^t [m | t]
  D  CLAIM 3 both branches: m > h => all E(S_J) EQUAL (no live slope
     direction, but spread);  m <= h < 2m => E(S_J) moves along e_m
     (live direction) but the family is NOT spread
  E  the ring identity R_{S u T} = R_S R_T in F_q[Y]/(Y^{h+1}) and the
     linearity/bijectivity of multiplication by a unit  (Claim 4's engine)
  F  CLAIM 4 at a = 1 and at a = 2 with b >= a+2
  G  COORDINATE FLAG: an explicit p-collinear triple whose Newton images
     are NOT e-collinear; and the coset case where the two agree
  H  the OPEN residue replayed at the pilot's n=20,q=101,h=2,m=3 shape
     -- LABELLED MEASURED-OPEN, not a claim
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


# ------------------------------------------------------------- utilities --

def factors(m):
    out, d = set(), 2
    while d * d <= m:
        if m % d == 0:
            out.add(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        out.add(m)
    return sorted(out)


def root_of_unity(q, n):
    fs = factors(q - 1)
    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // f, q) != 1 for f in fs))
    w = pow(g, (q - 1) // n, q)
    assert pow(w, n, q) == 1
    assert all(pow(w, d, q) != 1 for d in range(1, n) if n % d == 0)
    return w


def evec(vals, h, q):
    """E(S) = (e_1,...,e_h) of the value multiset, exact mod q."""
    e = [1] + [0] * h
    for x in vals:
        for j in range(h, 0, -1):
            e[j] = (e[j] + x * e[j - 1]) % q
    return tuple(e[1:h + 1])


def pvec(vals, h, q):
    return tuple(sum(pow(x, t, q) for x in vals) % q for t in range(1, h + 1))


def rvec(vals, h, q):
    """R_S(Y) = prod (1 - xY) truncated to degree h; length h+1, R[0] = 1."""
    r = [1] + [0] * h
    for x in vals:
        for j in range(h, 0, -1):
            r[j] = (r[j] - x * r[j - 1]) % q
    return r


def rmul(a, b, h, q):
    out = [0] * (h + 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj and i + j <= h:
                    out[i + j] = (out[i + j] + ai * bj) % q
    return out


def rinv(a, h, q):
    """inverse of a unit (a[0] = 1) in F_q[Y]/(Y^{h+1})."""
    assert a[0] % q == 1
    inv = [1] + [0] * h
    for k in range(1, h + 1):
        s = 0
        for i in range(1, k + 1):
            s += a[i] * inv[k - i]
        inv[k] = (-s) % q
    return inv


def newton_p_to_e(p, q):
    """(p_1..p_h) -> (e_1..e_h) by Newton's identities (char q > h)."""
    h = len(p)
    e = [1] + [0] * h
    for j in range(1, h + 1):
        s = 0
        for i in range(1, j + 1):
            s += ((-1) ** (i - 1)) * e[j - i] * p[i - 1]
        e[j] = s % q * pow(j % q, q - 2, q) % q
    return tuple(e[1:])


def affine_rank(vecs, q):
    if not vecs:
        return -1
    base = vecs[0]
    rows = [[(v[i] - base[i]) % q for i in range(len(base))] for v in vecs[1:]]
    if not rows:
        return 0
    ncol = len(rows[0])
    piv = 0
    for col in range(ncol):
        sel = None
        for i in range(piv, len(rows)):
            if rows[i][col] % q:
                sel = i
                break
        if sel is None:
            continue
        rows[piv], rows[sel] = rows[sel], rows[piv]
        iv = pow(rows[piv][col], q - 2, q)
        rows[piv] = [x * iv % q for x in rows[piv]]
        for i in range(len(rows)):
            if i != piv and rows[i][col] % q:
                f = rows[i][col]
                rows[i] = [(rows[i][c] - f * rows[piv][c]) % q
                           for c in range(ncol)]
        piv += 1
        if piv == len(rows):
            break
    return piv


def cosets(q, n, m):
    """the n/m cosets of mu_m inside mu_n, as lists of field values."""
    w = root_of_unity(q, n)
    D = [pow(w, i, q) for i in range(n)]
    z = pow(w, n // m, q)
    out, seen = [], set()
    for x in D:
        if x in seen:
            continue
        c = [x * pow(z, i, q) % q for i in range(m)]
        for y in c:
            seen.add(y)
        out.append(c)
    return out


# --------------------------------------------------------------- shapes ---
# (name, n, q, h, m, K, a):  A = K + h,  |G| = A - a*m  (must be >= 0)
SHAPES = [
    ("m>h  (4>3)", 24, 73, 3, 4, 8, 2),      # spread, slope-dead
    ("m<=h (3<=3<6)", 24, 73, 3, 3, 8, 2),   # live slope, not spread
    ("m>h  (4>2)", 20, 101, 2, 4, 6, 2),     # spread, slope-dead
    ("m<=h (2<=3<4)", 24, 73, 3, 2, 8, 3),   # live slope, not spread
]


def build(shape):
    name, n, q, h, m, K, a = shape
    A = K + h
    gsz = A - a * m
    assert gsz >= 0
    cs = cosets(q, n, m)
    assert len(cs) == n // m
    # core G: gsz points taken from the LAST coset(s); blocks: the first ones
    pool_ct = len(cs) - ((gsz + m - 1) // m if gsz else 0)
    blocks = cs[:pool_ct]
    spare = [x for c in cs[pool_ct:] for x in c]
    G = spare[:gsz]
    assert len(G) == gsz
    return name, n, q, h, m, K, a, A, G, blocks


def stage_A_B():
    bad_a, bad_b, rows = [], [], []
    for shape in SHAPES:
        name, n, q, h, m, K, a, A, G, blocks = build(shape)
        b = len(blocks)
        if b < a + 1:
            bad_a.append((name, "pool too small", b))
            continue
        Js = list(combinations(range(b), a))
        sets = {J: set(G) | {x for j in J for x in blocks[j]} for J in Js}
        for J in Js:
            if len(sets[J]) != A:
                bad_a.append((name, J, "size"))
        mx = 0
        for i in range(len(Js)):
            for j in range(i + 1, len(Js)):
                J1, J2 = Js[i], Js[j]
                core = len(sets[J1] & sets[J2])
                want = len(G) + m * len(set(J1) & set(J2))
                if core != want:
                    bad_a.append((name, J1, J2, core, want))
                mx = max(mx, core)
        spread = mx <= K - 1
        if spread != (m >= h + 1):
            bad_a.append((name, "threshold", m, h, spread))
        if mx != A - m:
            bad_a.append((name, "max core", mx, A - m))
        # B: at m <= h every member has a partner at core >= K
        if m <= h:
            for J1 in Js:
                if not any(len(sets[J1] & sets[J2]) >= K
                           for J2 in Js if J2 != J1):
                    bad_b.append((name, J1))
        rows.append((name, f"A={A} |G|={len(G)} b={b} maxcore={mx} "
                           f"(A-m={A-m}) K={K} spread={spread}"))
    check("A: |S_J ^ S_J'| = |G| + m|J ^ J'| exactly, max pairwise core "
          "= A - m, and CLAIM 1's threshold: spread <=> m >= h+1",
          not bad_a, "; ".join(r[1] for r in rows) + f" bad={bad_a[:2]}")
    check("B: CLAIM 2 (SF-SELFCOLLISION derived) -- at m <= h EVERY member "
          "has a partner at core >= K, so the whole planted family sits in "
          "Gamma_hi", not bad_b, f"bad={bad_b[:2]}")


def stage_C():
    bad, rows = [], []
    for (n, q, m, h) in [(24, 73, 4, 3), (24, 73, 3, 3), (20, 101, 4, 2),
                         (24, 73, 2, 3), (16, 97, 8, 3)]:
        for B in cosets(q, n, m):
            g = B[0]
            # prod (X - x) == X^m - g^m: compare coefficient vectors
            poly = [1]
            for x in B:
                new = [0] * (len(poly) + 1)
                for i, c in enumerate(poly):
                    new[i] = (new[i] - c * x) % q
                    new[i + 1] = (new[i + 1] + c) % q
                poly = new
            want = [0] * (m + 1)
            want[0] = (-pow(g, m, q)) % q
            want[m] = 1
            if poly != want:
                bad.append((n, q, m, g, "poly"))
            # e-vector support and p_t = m g^t [m|t]
            E = evec(B, h, q)
            P = pvec(B, h, q)
            for j in range(1, h + 1):
                if j != m and E[j - 1] != 0:
                    bad.append((n, q, m, h, g, "e support", j))
                if P[j - 1] != (m * pow(g, j, q) % q if j % m == 0 else 0):
                    bad.append((n, q, m, h, g, "p form", j))
            if m <= h and E[m - 1] == 0:
                bad.append((n, q, m, h, g, "e_m vanishes"))
        rows.append((n, q, m, h))
    check("C: coset identity prod_{x in g mu_m}(X-x) = X^m - g^m; e_j = 0 "
          "for j != m in 1..h; p_t = m g^t if m|t else 0 (so for "
          "m <= h < 2m only t = m survives)", not bad,
          f"shapes (n,q,m,h) = {rows}; bad={bad[:2]}")


def stage_D():
    bad, rows = [], []
    for shape in SHAPES:
        name, n, q, h, m, K, a, A, G, blocks = build(shape)
        b = len(blocks)
        Js = list(combinations(range(b), a))
        Es = [evec(list(G) + [x for j in J for x in blocks[j]], h, q)
              for J in Js]
        rk = affine_rank(Es, q)
        distinct = len(set(Es))
        mx = max(len(set(G) | {x for j in J1 for x in blocks[j]}
                     & (set(G) | {x for j in J2 for x in blocks[j]}))
                 for J1 in Js for J2 in Js if J1 != J2)
        spread = mx <= K - 1
        if m > h:
            # all moment vectors EQUAL: single point, no live direction
            if not (rk == 0 and distinct == 1):
                bad.append((name, "expected a single point", rk, distinct))
            if not spread:
                bad.append((name, "expected spread at m > h"))
        else:
            # moves along a line; direction must be e_m up to the R_G twist
            if rk != 1:
                bad.append((name, "expected affine rank 1", rk))
            if spread:
                bad.append((name, "expected NOT spread at m <= h"))
            if h < 2 * m:
                # the moving coordinate block starts at index m
                base = Es[0]
                dirs = {tuple((e[i] - base[i]) % q for i in range(h))
                        for e in Es}
                if any(d[i] != 0 for d in dirs for i in range(m - 1)):
                    bad.append((name, "direction not supported from e_m"))
        rows.append((name, f"rank={rk} distinct={distinct} spread={spread}"))
    check("D: CLAIM 3 -- at m > h ALL E(S_J) coincide (one point: no live "
          "slope direction) while the family IS spread; at m <= h < 2m the "
          "E(S_J) move on a line whose direction starts at coordinate e_m "
          "(live slope direction) while the family is NOT spread. The two "
          "are INCOMPATIBLE for every coset-block geometry",
          not bad, "; ".join(f"{r[0]}: {r[1]}" for r in rows)
                   + f" bad={bad[:2]}")


def stage_E_F():
    bad_e, bad_f, rows = [], [], []
    q, h = 241, 4
    # E: multiplicativity + unit linearity
    rnd = 424242
    for _ in range(200):
        rnd = (6364136223846793005 * rnd + 1442695040888963407) % (1 << 64)
        S = [(rnd >> (8 * i)) % (q - 1) + 1 for i in range(4)]
        rnd = (6364136223846793005 * rnd + 1442695040888963407) % (1 << 64)
        T = [(rnd >> (8 * i)) % (q - 1) + 1 for i in range(3)]
        if set(S) & set(T):
            continue
        if rmul(rvec(S, h, q), rvec(T, h, q), h, q) != rvec(S + T, h, q):
            bad_e.append((tuple(S), tuple(T)))
        C = rvec(S, h, q)
        Ci = rinv(C, h, q)
        if rmul(C, Ci, h, q) != [1] + [0] * h:
            bad_e.append(("inverse", tuple(S)))
        # linearity of multiplication by C on three points
        A1, A2 = rvec(T, h, q), rvec([2, 5, 7], h, q)
        lam = 3
        lhs = rmul(C, [(A1[i] + lam * (A2[i] - A1[i])) % q
                       for i in range(h + 1)], h, q)
        cA1, cA2 = rmul(C, A1, h, q), rmul(C, A2, h, q)
        rhs = [(cA1[i] + lam * (cA2[i] - cA1[i])) % q for i in range(h + 1)]
        if lhs != rhs:
            bad_e.append(("linearity", tuple(S)))
    check("E: R_{S u T} = R_S R_T in F_q[Y]/(Y^{h+1}) for disjoint S,T; "
          "every R_S is a UNIT; multiplication by a unit is linear and "
          "bijective (Claim 4's engine)", not bad_e, f"bad={bad_e[:2]}")

    # F: Claim 4 -- plant a family on a line, recover block collinearity
    for (n, q, h, m, a) in [(24, 73, 3, 3, 1), (24, 73, 3, 3, 2),
                            (20, 101, 2, 4, 1), (24, 73, 3, 2, 2)]:
        cs = cosets(q, n, m)
        blocks = cs[:len(cs) - 1]
        G = cs[-1][:1]
        b = len(blocks)
        if a >= 2 and b < a + 2:
            continue
        Js = list(combinations(range(b), a))
        Es = [evec(list(G) + [x for j in J for x in blocks[j]], h, q)
              for J in Js]
        on_line = affine_rank(Es, q) <= 1
        blk = [evec(B, h, q) for B in blocks]
        blk_line = affine_rank(blk, q) <= 1
        rows.append((n, q, h, m, a, b, on_line, blk_line))
        if on_line and not blk_line:
            bad_f.append((n, q, h, m, a, "family on a line but blocks not"))
    check("F: CLAIM 4 -- whenever the planted family {S_J} lies on ONE line "
          "(a = 1, or a >= 2 with b >= a+2), the BLOCK moment vectors "
          "E(B_j) are collinear in ELEMENTARY-SYMMETRIC coordinates",
          not bad_f,
          f"(n,q,h,m,a,b, family-on-line, blocks-collinear) = {rows}")


def stage_G():
    """COORDINATE FLAG: p-collinear does not imply e-collinear."""
    q, h = 1009, 3
    # three p-vectors on a line: (t, 0, 0), t = 0, 1, 2
    ps = [(0, 0, 0), (1, 0, 0), (2, 0, 0)]
    es = [newton_p_to_e(p, q) for p in ps]
    rp, re = affine_rank([tuple(p) for p in ps], q), affine_rank(es, q)
    flag = (rp <= 1 and re > 1)
    # and the coset case where the two agree
    agree = []
    for (n, qq, m, hh) in [(24, 73, 3, 3), (20, 101, 4, 2), (24, 73, 2, 3)]:
        cs = cosets(qq, n, m)
        E = [evec(B, hh, qq) for B in cs]
        P = [pvec(B, hh, qq) for B in cs]
        agree.append((n, qq, m, hh, affine_rank(E, qq), affine_rank(P, qq)))
    both_line = all(a[4] <= 1 and a[5] <= 1 for a in agree)
    check("G: COORDINATE FLAG -- the Newton map p -> e is NOT affine: the "
          "p-collinear triple (0,0,0),(1,0,0),(2,0,0) has e-images of "
          "affine rank 2. So 'collinear in p' (the source's phrasing, "
          "expE.py:7-8) is NOT the condition the source's code tests "
          "(core.moment_vector = e). For COSET blocks the two agree "
          "(both give direction e_m), so the dichotomy is unaffected",
          flag and both_line,
          f"p-rank={rp} e-rank={re}; coset (n,q,m,h,rk_E,rk_P) = {agree}")


def stage_H():
    """The OPEN residue, replayed at the pilot's n=20,q=101,h=2,m=3 shape."""
    n, q, h, m, K, a = 20, 101, 2, 3, 6, 2
    blocks = list(combinations(range(n), m))
    w = root_of_unity(q, n)
    D = [pow(w, i, q) for i in range(n)]
    P = [evec([D[i] for i in B], h, q) for B in blocks]
    NB = len(blocks)
    best = (0, None, None)
    for i in range(NB):
        cnt = {}
        for j in range(NB):
            if j == i:
                continue
            d = tuple((P[j][t] - P[i][t]) % q for t in range(h))
            if not any(d):
                continue
            f = next(t for t in range(h) if d[t])
            iv = pow(d[f], q - 2, q)
            key = tuple(x * iv % q for x in d)
            cnt[key] = cnt.get(key, 0) + 1
        if cnt:
            k, c = max(cnt.items(), key=lambda kv: kv[1])
            if c + 1 > best[0]:
                best = (c + 1, i, k)
    tot, bi, key = best
    on = [blocks[bi]]
    for j in range(NB):
        if j == bi:
            continue
        d = tuple((P[j][t] - P[bi][t]) % q for t in range(h))
        if not any(d):
            on.append(blocks[j])
            continue
        f = next(t for t in range(h) if d[t])
        iv = pow(d[f], q - 2, q)
        if tuple(x * iv % q for x in d) == key:
            on.append(blocks[j])
    masks = []
    chosen = []
    for B in on:
        mk = 0
        for i in B:
            mk |= 1 << i
        if all(mk & o == 0 for o in chosen):
            chosen.append(mk)
        masks.append(mk)
    b_disj = len(chosen)
    fam = b_disj * (b_disj - 1) // 2 if b_disj >= a else 0
    print("NOTE (MEASURED-OPEN, not a claim of the node): the NON-coset "
          f"residue at n={n}, q={q}, h={h}, m={m} (>= h+1, so spread): "
          f"{NB} blocks, richest line carries {len(on)}, {b_disj} of them "
          f"DISJOINT -> a spread block family of size C({b_disj},{a}) = "
          f"{fam}; feasible = {b_disj >= a + 1}. The residue is ALIVE at "
          "toy scale (pilot EXPE.json: 28 on the line, 4 disjoint, family "
          "6) and is closed at official scale only by a FIRST-MOMENT "
          "count, which the pilot states is NOT a theorem "
          "(pb_h4_hunt/REPORT.md:61).")
    check("H: the residue replay ran and is non-trivial (the richest line "
          "carries at least 3 blocks) -- recorded as MEASURED-OPEN",
          len(on) >= 3 and NB == 1140, f"line={len(on)} blocks={NB}")


def main():
    stage_A_B()
    stage_C()
    stage_D()
    stage_E_F()
    stage_G()
    stage_H()
    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("PB_BLOCK_DICHOTOMY_ALL_PASS")


if __name__ == "__main__":
    main()
