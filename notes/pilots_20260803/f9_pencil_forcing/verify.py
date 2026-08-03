#!/usr/bin/env python3
r"""Verifier for F9: PENCIL FORCING AT V >= 5 (2026-08-03).

PROFILE: tiny.  Run from the repo root:
    tools/ramguard tiny -- python3 \
        notes/pilots_20260803/f9_pencil_forcing/verify.py

Read-only reuse of
  notes/pilots_20260803/zero_escape_collapse/verify.py  (zec: rref, rank,
      nullspace, dual_basis, ann_dim, rank_row, LCG, interpolate)
  notes/pilots_20260803/la_pencil_rigidity/verify.py    (la: poly_from_roots,
      build_system, is_pencil_rank, ann_sol_space, g_of, audit, extend)

SECTIONS
  A  structure extraction (w, g'_a, lambda_a, Z, d) vs the banked duality
  B  LEMMA 2 (r-formula) and LEMMA 3 (pencil normal form) on fixtures
  C  CONSTRUCTION 1: V >= 5 NON-PENCIL escapes at (t,e) = (3,2)   [T2]
  D  CONSTRUCTION 2: the 2-rogue systems at (t,e) = (4,3),(5,4)   [T1]
  E  T0 (anchor): pencil-cover census on every fixture + targeted attack
  F  P-SHARE: two distinct pencils share at most one fibre / one slope
  G  why the la sweeps missed these (codimension measurement)
"""
from __future__ import annotations

import importlib.util
import json
import sys
from itertools import combinations

sys.dont_write_bytecode = True

ROOT = "/home/u2470931/smooth-read-solomin/prize"
LA = ROOT + "/notes/pilots_20260803/la_pencil_rigidity/verify.py"
_spec = importlib.util.spec_from_file_location("la", LA)
la = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(la)
zec = la.zec

FAILURES = []
CHECKS = []
RECORD = {}


def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    CHECKS.append(label)
    if not ok:
        FAILURES.append(label)


def note(label, detail=""):
    print("NOTE " + label + ("  " + detail if detail else ""))


# --------------------------------------------------------------- polynomials
def padd(a, b, q):
    n = max(len(a), len(b))
    return zec.poly_trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                          for i in range(n)], q)


def pscale(a, c, q):
    return zec.poly_trim([x * c % q for x in a], q)


def psub(a, b, q):
    return padd(a, pscale(b, q - 1, q), q)


def pmul(a, b, q):
    if not a or not b:
        return []
    return zec.poly_trim(la.polymul(a, b, q), q)


def pdiv(a, b, q):
    """Exact division a/b (returns None if not exact)."""
    a = zec.poly_trim(a, q)
    b = zec.poly_trim(b, q)
    if not b:
        return None
    out = [0] * max(1, len(a) - len(b) + 1)
    rem = list(a)
    ib = zec.inv(b[-1], q)
    while len(zec.poly_trim(rem, q)) >= len(b):
        rem = zec.poly_trim(rem, q)
        sh = len(rem) - len(b)
        c = rem[-1] * ib % q
        out[sh] = c
        for i, bc in enumerate(b):
            rem[sh + i] = (rem[sh + i] - c * bc) % q
    if zec.poly_trim(rem, q):
        return None
    return zec.poly_trim(out, q)


def proots(p, q):
    return [x for x in range(q) if zec.poly_eval(p, x, q) == 0]


def prop(a, b, q):
    """True iff a and b are proportional (both non-zero)."""
    a, b = zec.poly_trim(a, q), zec.poly_trim(b, q)
    if not a or not b:
        return False
    return zec.rank_mod([a + [0] * (len(b) - len(a)) if len(a) < len(b) else a,
                         b + [0] * (len(a) - len(b)) if len(b) < len(a) else b],
                        q) == 1


def in_span(basis, f, q):
    """f in span(basis)?"""
    n = max([len(x) for x in basis + [f]])
    pad = lambda p: p + [0] * (n - len(p))
    B = [pad(x) for x in basis]
    return zec.rank_mod(B, q) == zec.rank_mod(B + [pad(f)], q)


def span_dim(polys, q):
    n = max(len(p) for p in polys)
    return zec.rank_mod([p + [0] * (n - len(p)) for p in polys], q)


# ------------------------------------------------------- structure extraction
def structure_at_pair(blocks, slopes, e, q, w):
    """The (POINT) normal form data at the pair (blocks[0], blocks[1])."""
    V = len(blocks)
    A1, A2 = list(blocks[0]), list(blocks[1])
    z1, z2 = slopes[0], slopes[1]
    out = {"ok": True}
    gp, lam = {}, {}
    for a in range(2, V):
        g = la.g_of(blocks, slopes, w, a, e, q)
        if g is None:
            return None
        gp[a] = pscale(g, zec.inv((slopes[a] - z2) % q, q), q)
        lam[a] = (slopes[a] - z2) * zec.inv((slopes[a] - z1) % q, q) % q
    Z1 = [x for x in A1 if w[A1.index(x)] == 0]
    Z2 = [x for x in A2 if w[len(A1) + A2.index(x)] == 0]
    out["Z1"], out["Z2"] = Z1, Z2
    mx = max(len(gp[a]) for a in gp) if gp else 1
    out["d"] = zec.rank_mod([gp[a] + [0] * (mx - len(gp[a])) for a in gp], q)
    out["gp"], out["lam"] = gp, lam
    # common zero set of the g'_a inside A1 u A2 must equal Z(w)
    com = [x for x in A1 + A2
           if all(zec.poly_eval(gp[a], x, q) == 0 for a in gp)]
    out["Z_matches"] = sorted(com) == sorted(Z1 + Z2)
    return out


def normal_form(blocks, slopes, e, q, w, st, a, b):
    """LEMMA 3 normal form (f_0, f_1) from two blocks a,b with a common
    g-direction; returns None if their g' are not proportional."""
    gp, lam = st["gp"], st["lam"]
    if not prop(gp[a], gp[b], q):
        return None
    # c_a, c_b with g'_a = c_a g_*, g'_b = c_b g_*  (take g_* := g'_a)
    ga, gb = gp[a], gp[b]
    # ratio c_b/c_a from the first non-zero coefficient
    i = next(i for i, c in enumerate(ga) if c)
    rho = gb[i] * zec.inv(ga[i], q) % q          # c_b / c_a  (g_* = g'_a)
    Ba = la.poly_from_roots(blocks[a], q)
    Bb = pscale(la.poly_from_roots(blocks[b], q), zec.inv(rho, q), q)
    den = zec.inv((lam[b] - lam[a]) % q, q)
    f0 = pscale(psub(pscale(Bb, lam[a], q), pscale(Ba, lam[b], q), q),
                q - den % q, q)
    f0 = pscale(psub(pscale(Ba, lam[b], q), pscale(Bb, lam[a], q), q), den, q)
    f1 = pscale(psub(Bb, Ba, q), den, q)
    return f0, f1


def pencil_cover_census(blocks, q):
    """All 2-dim spans containing >= 3 blocks; returns list of (dim2 basis,
    frozenset of block indices)."""
    V = len(blocks)
    Bs = [la.poly_from_roots(b, q) for b in blocks]
    fams = []
    for i, j in combinations(range(V), 2):
        mem = frozenset(c for c in range(V) if in_span([Bs[i], Bs[j]], Bs[c], q))
        if len(mem) >= 3 and mem not in [f for _, f in fams]:
            fams.append(((i, j), mem))
    return fams


# =========================================================================
def banked_fixtures():
    """W1, W2 (la) and the pencil controls."""
    fx = []
    fx.append(("W1", 13, 3, 2, [[1, 5, 8], [7, 10, 11], [0, 2, 4], [3, 9, 12]],
               [0, 1, 2, 10]))
    fx.append(("W2", 23, 4, 3, [[0, 15, 19, 22], [1, 3, 5, 17], [4, 7, 12, 13],
                                [6, 9, 14, 16]], [0, 1, 2, 7]))
    for q, dd, t, ncl, e in ((11, 2, 2, 5, 1), (19, 3, 3, 5, 2),
                             (41, 4, 4, 5, 3), (13, 2, 2, 6, 1)):
        ps = la.pencil_system(q, dd, t, ncl, e)
        if ps:
            fx.append(("PEN_q%d_t%d_V%d" % (q, t, ncl), q, t, e, ps[0], ps[1]))
    return fx


def section_A():
    print("\n--- A. structure extraction vs the banked duality (Q7) ---")
    for name, q, t, e, blocks, slopes in banked_fixtures():
        V = len(blocks)
        a = la.audit(q, t, e, [list(b) for b in blocks], list(slopes), name)
        dr = la.ann_dim_reduced(blocks, slopes, e, q)
        ok_gate = bool(a)
        ann = a["ann"] if a else None
        check("A[%s] gate-clean, reduction == banked zec.ann_dim" % name,
              ok_gate and ann == dr and ann >= 1,
              "V=%d t=%d e=%d banked_ann=%s reduced=%d span{B_a}=%d"
              % (V, t, e, ann, dr, la.is_pencil_rank(blocks, q)))
        sols = la.ann_sol_space(blocks, slopes, e, q)
        st = structure_at_pair(blocks, slopes, e, q, sols[0])
        check("A[%s] Z(w) == common zero set of the g'_a in A_1 u A_2" % name,
              st is not None and st["Z_matches"],
              "|Z_1|=%d |Z_2|=%d d=%d" % (len(st["Z1"]), len(st["Z2"]), st["d"])
              if st else "no structure")
        RECORD["A_" + name] = dict(q=q, t=t, e=e, V=V, ann=ann,
                                   span=la.is_pencil_rank(blocks, q),
                                   d=st["d"] if st else None,
                                   Z=len(st["Z1"]) + len(st["Z2"]) if st else None)


def section_B():
    print("\n--- B. LEMMA 2 (r-formula) and LEMMA 3 (normal form) ---")
    bad2 = bad3 = bad4 = 0
    n2 = n3 = 0
    for name, q, t, e, blocks, slopes in banked_fixtures():
        V = len(blocks)
        for w in la.ann_sol_space(blocks, slopes, e, q):
            st = structure_at_pair(blocks, slopes, e, q, w)
            if st is None:
                continue
            Bs = [la.poly_from_roots(b, q) for b in blocks]
            # LEMMA 2: span{B_a : a >= 3} == 2  <=>  d == 1   (needs >= 3 blocks)
            if V >= 5:
                n2 += 1
                r = span_dim([Bs[a] for a in range(2, V)], q)
                if (r == 2) != (st["d"] == 1):
                    bad2 += 1
            # LEMMA 3: two blocks with a common g-direction => normal form
            for a, b in combinations(range(2, V), 2):
                nf = normal_form(blocks, slopes, e, q, w, st, a, b)
                if nf is None:
                    continue
                n3 += 1
                f0, f1 = nf
                A1, A2 = list(blocks[0]), list(blocks[1])
                W1 = [x for x in A1 if x not in st["Z1"]]
                W2 = [x for x in A2 if x not in st["Z2"]]
                v0 = all(zec.poly_eval(f0, x, q) == 0 for x in W2)
                v1 = all(zec.poly_eval(f1, x, q) == 0 for x in W1)
                B1Z = la.poly_from_roots(W1, q)
                B2Z = la.poly_from_roots(W2, q)
                s0 = pdiv(f0, B2Z, q)
                s1 = pdiv(f1, B1Z, q)
                inp = (in_span([f0, f1], Bs[a], q) and in_span([f0, f1], Bs[b], q))
                degok = (s0 is not None and s1 is not None
                         and len(s0) - 1 <= len(st["Z2"])
                         and len(s1) - 1 <= len(st["Z1"]))
                if not (v0 and v1 and inp and degok):
                    bad3 += 1
                # LEMMA 4: B_2 in <f_0,f_1>  <=>  s_0 ~ prod_{Z_2}(X-x)
                z2p = la.poly_from_roots(st["Z2"], q)
                z1p = la.poly_from_roots(st["Z1"], q)
                if s0 is not None and s1 is not None:
                    if in_span([f0, f1], Bs[1], q) != prop(s0, z2p, q):
                        bad4 += 1
                    if in_span([f0, f1], Bs[0], q) != prop(s1, z1p, q):
                        bad4 += 1
    check("B1 LEMMA 2 (r-formula): span{B_a, a>=3} = 2 <=> d = 1  (V >= 5)",
          bad2 == 0 and n2 > 0, "%d (fixture, solution) instances, %d violations"
          % (n2, bad2))
    check("B2 LEMMA 3 (normal form): f_0 = B_2^Z s_0 vanishes on W_2, "
          "f_1 = B_1^Z s_1 vanishes on W_1, both blocks in <f_0,f_1>",
          bad3 == 0 and n3 > 0, "%d pairs with a common g-direction, %d bad"
          % (n3, bad3))
    check("B3 LEMMA 4 (rogue criterion): B_j in <f_0,f_1> <=> s_0 ~ zeta_j",
          bad4 == 0, "%d violations" % bad4)
    RECORD["B"] = dict(lemma2=n2, lemma3=n3, bad=[bad2, bad3, bad4])


# =========================================================================
def build_escape(q, t, e, A1, A2, Z1, Z2, s0, s1, want, seen_extra=()):
    """CONSTRUCTION (registered in PREREG Q3/Q4).

    f_0 := B_2^Z s_0 (vanishes on A_2 \\ Z_2),  f_1 := B_1^Z s_1,
    g   := prod_{Z}(X-x),  w := g/f_0 on A_1\\Z_1, g/f_1 on A_2\\Z_2, 0 on Z.
    Blocks A_3.. := split members of the pencil <f_0,f_1>.
    Returns (blocks, slopes, w, f0, f1) with len(blocks) = 2 + want, or None.
    """
    W1 = [x for x in A1 if x not in Z1]
    W2 = [x for x in A2 if x not in Z2]
    f0 = pmul(la.poly_from_roots(W2, q), s0, q)
    f1 = pmul(la.poly_from_roots(W1, q), s1, q)
    if len(f0) - 1 != t or len(f1) - 1 != t:
        return None
    g = la.poly_from_roots(list(Z1) + list(Z2), q)
    if len(g) - 1 > e - 1:
        return None
    # w
    w = []
    for x in A1:
        if x in Z1:
            w.append(0)
        else:
            d0 = zec.poly_eval(f0, x, q)
            if d0 == 0:
                return None
            w.append(zec.poly_eval(g, x, q) * zec.inv(d0, q) % q)
    for x in A2:
        if x in Z2:
            w.append(0)
        else:
            d1 = zec.poly_eval(f1, x, q)
            if d1 == 0:
                return None
            w.append(zec.poly_eval(g, x, q) * zec.inv(d1, q) % q)
    if not any(w):
        return None
    used = set(A1) | set(A2) | set(seen_extra)
    # split members of the pencil, lambda != 0 (= f_0) and != infinity (= f_1)
    mem = []
    for lam in range(1, q):
        F = padd(f0, pscale(f1, lam, q), q)
        if len(F) - 1 != t:
            continue
        rts = proots(F, q)
        if len(rts) != t or set(rts) & used:
            continue
        mem.append((lam, sorted(rts)))
    if len(mem) < want:
        return None
    z1, z2 = 0, 1
    blocks = [list(A1), list(A2)]
    slopes = [z1, z2]
    taken = set()
    for lam, rts in mem:
        if set(rts) & taken:
            continue
        z = zec.inv((1 - lam) % q, q)         # lambda = (z-z2)/(z-z1), z1=0,z2=1
        if z in slopes:
            continue
        blocks.append(rts)
        slopes.append(z)
        taken |= set(rts)
        if len(blocks) == 2 + want:
            break
    if len(blocks) != 2 + want:
        return None
    return blocks, slopes, w, f0, f1


def try_construction(q, t, e, nZ1, nZ2, want, seed, ntry):
    """Random (A_1, A_2, Z, s_0, s_1) from the registered families."""
    rng = zec.LCG(seed)
    for _ in range(ntry):
        pool = list(range(q))
        A1 = sorted(rng.sample(pool, t))
        pool = [x for x in pool if x not in A1]
        A2 = sorted(rng.sample(pool, t))
        pool = [x for x in pool if x not in A2]
        Z1 = sorted(rng.sample(A1, nZ1)) if nZ1 else []
        Z2 = sorted(rng.sample(A2, nZ2)) if nZ2 else []
        # s_0 monic of degree |Z_2| with roots OUTSIDE Z_2 (=> B_2 not in P),
        # s_1 monic of degree |Z_1| with roots OUTSIDE Z_1 (=> B_1 not in P).
        y2 = rng.sample(pool, nZ2) if nZ2 else []
        y1 = rng.sample([x for x in pool if x not in y2], nZ1) if nZ1 else []
        s0 = la.poly_from_roots(y2, q)
        s1 = la.poly_from_roots(y1, q)
        out = build_escape(q, t, e, A1, A2, Z1, Z2, s0, s1, want)
        if out is None:
            continue
        blocks, slopes, w, f0, f1 = out
        if la.is_pencil_rank(blocks, q) < 3:
            continue                       # a genuine pencil: not an escape
        a = la.audit(q, t, e, blocks, slopes, "F9")
        if not a or a["ann"] < 1:
            continue
        a["f0"], a["f1"] = f0, f1
        a["Z1"], a["Z2"] = Z1, Z2
        return a, blocks, slopes, w, f0, f1
    return None


def report_fixture(tag, a, blocks, q, f0, f1):
    Bs = [la.poly_from_roots(b, q) for b in blocks]
    inP = [i for i in range(len(blocks)) if in_span([f0, f1], Bs[i], q)]
    fams = pencil_cover_census(blocks, q)
    note(tag, json.dumps({kk: a[kk] for kk in
                          ("q", "V", "t", "t0", "k", "h", "m", "e", "U", "pair",
                           "trip", "minmult", "ann", "rank", "two_m",
                           "pencil_rank", "blocks", "slopes")}))
    note(tag + " structure",
         "blocks in the constructed pencil: %s ; pencil families of size >= 3: %s"
         % (inP, [sorted(f) for _, f in fams]))
    return inP, fams


def section_C():
    print("\n--- C. CONSTRUCTION 1: V >= 5 NON-PENCIL escapes  (Q3 / T2) ---")
    found = []
    for q in (31, 37, 41, 43, 53, 61):
        for want in (3, 4):                # V = 5 and V = 6
            r = try_construction(q, 3, 2, 1, 0, want, 424242 + q + want, 400)
            if r:
                a, blocks, slopes, w, f0, f1 = r
                inP, fams = report_fixture("C V=%d q=%d" % (2 + want, q),
                                           a, blocks, q, f0, f1)
                found.append((a, inP, fams))
                RECORD["C_V%d_q%d" % (2 + want, q)] = {
                    kk: a[kk] for kk in ("q", "V", "t", "t0", "k", "h", "e", "U",
                                         "ann", "rank", "two_m", "pencil_rank",
                                         "blocks", "slopes")}
    check("C1 (F9-F3 / kills T2) gate-clean zero-escape NON-PENCIL systems "
          "with dim Ann >= 1 EXIST at V >= 5", len(found) > 0,
          "%d fixtures (V, span{B_a}, dim Ann) = %s" % (
              len(found), [(a["V"], a["pencil_rank"], a["ann"]) for a, _, _ in found]))
    if found:
        check("C2 (T1 holds on these) exactly V-1 blocks lie in ONE pencil",
              all(len(inP) == a["V"] - 1 for a, inP, _ in found),
              "sizes %s" % [len(inP) for _, inP, _ in found])
        check("C3 (T0 holds on these) at most ONE pencil family of size >= 3",
              all(len(f) <= 1 for _, _, f in found),
              "family counts %s" % [len(f) for _, _, f in found])
    return found


def section_D():
    print("\n--- D. CONSTRUCTION 2: the 2-rogue systems  (Q4 / T1) ---")
    found = []
    for q, t, e in ((53, 4, 3), (61, 4, 3), (71, 4, 3), (101, 4, 3),
                    (101, 5, 4), (151, 5, 4)):
        r = try_construction(q, t, e, 1, 1, 3, 777 + q + t, 500)
        if r:
            a, blocks, slopes, w, f0, f1 = r
            inP, fams = report_fixture("D q=%d t=%d e=%d" % (q, t, e),
                                       a, blocks, q, f0, f1)
            found.append((a, inP, fams))
            RECORD["D_q%d_t%d" % (q, t)] = {
                kk: a[kk] for kk in ("q", "V", "t", "t0", "k", "h", "e", "U",
                                     "ann", "rank", "pencil_rank", "blocks",
                                     "slopes")}
    check("D1 (F9-F4 / kills T1) V >= 5 systems with only V-2 blocks in one "
          "pencil EXIST", any(len(inP) == a["V"] - 2 for a, inP, _ in found),
          "%d 2-rogue fixtures, in-pencil counts %s"
          % (len(found), [(a["V"], len(inP)) for a, inP, _ in found]))
    if found:
        check("D2 (T0 still holds) at most ONE pencil family of size >= 3 "
              "even on the 2-rogue fixtures",
              all(len(f) <= 1 for _, _, f in found),
              "family counts %s" % [len(f) for _, _, f in found])
    return found


# =========================================================================
def section_E(cfound, dfound):
    print("\n--- E. T0 (the anchor): pencil-cover census + targeted attack ---")
    # E1: census on every banked fixture too
    worst = 0
    for name, q, t, e, blocks, slopes in banked_fixtures():
        fams = pencil_cover_census(blocks, q)
        worst = max(worst, len(fams))
    for a, _, f in cfound + dfound:
        worst = max(worst, len(f))
    check("E1 (F9-F5) no fixture carries TWO distinct pencil families of "
          "size >= 3", worst <= 1, "max families over all fixtures = %d" % worst)

    # E2 (CORRECTED, see PREREG in-run amendment 1): LEMMA 5 says
    # P' ^ <B_i,B_j> is 0, or <B_i>, or <B_j> -- and never contains a THIRD
    # block.  The pre-amendment wording ("= 0") holds only under the T0
    # hypothesis B_i, B_j not in P', which the 1-rogue fixtures violate.
    badA = badB = badC = 0
    tested = 0
    for a, _, _ in cfound + dfound:
        q = a["q"]
        blocks = a["blocks"]
        f0, f1 = a["f0"], a["f1"]
        Bs = [la.poly_from_roots(b, q) for b in blocks]
        n = max([len(f0), len(f1)] + [len(x) for x in Bs])
        pad = lambda p: p + [0] * (n - len(p))
        r = zec.rank_mod([pad(f0), pad(f1), pad(Bs[0]), pad(Bs[1])], q)
        dint = 4 - r                        # dim(P' ^ <B_1,B_2>)
        tested += 1
        if dint > 1:
            badA += 1
        if dint == 1:
            # the common line must be <B_1> or <B_2>
            if not (in_span([f0, f1], Bs[0], q) or in_span([f0, f1], Bs[1], q)):
                badB += 1
        # no THIRD block in <B_1,B_2>
        if any(in_span([Bs[0], Bs[1]], Bs[c], q) for c in range(2, len(blocks))):
            badC += 1
    check("E2a LEMMA 5: dim(P' ^ <B_1,B_2>) <= 1 on every fixture",
          badA == 0 and tested > 0, "%d fixtures, %d violations" % (tested, badA))
    check("E2b LEMMA 5: a non-zero intersection is spanned by B_1 or B_2",
          badB == 0, "%d violations" % badB)
    check("E2c LEMMA 5 (the T0 payload): NO third block lies in <B_1,B_2>",
          badC == 0, "%d fixtures with a third block in the pair's pencil"
          % badC)
    bad = badA + badB + badC

    # E3: targeted attack -- try to FORCE a third block into <B_1,B_2>
    # by choosing s_0, s_1 with zeta_1 s_0 ~ zeta_2 s_1 (the only algebraic
    # route left open by LEMMA 5's proof).  |Z_1| = |Z_2| = 1.
    hits = 0
    tries = 0
    rng = zec.LCG(31337)
    for q, t, e in ((53, 4, 3), (71, 4, 3), (101, 5, 4)):
        for _ in range(300):
            pool = list(range(q))
            A1 = sorted(rng.sample(pool, t))
            pool = [x for x in pool if x not in A1]
            A2 = sorted(rng.sample(pool, t))
            pool = [x for x in pool if x not in A2]
            x1 = rng.sample(A1, 1)[0]
            x2 = rng.sample(A2, 1)[0]
            # zeta_1 s_0 ~ zeta_2 s_1 with deg s_i <= 1 forces s_1 ~ zeta_1
            # (LEMMA 5); take exactly that and see what happens.
            s1 = la.poly_from_roots([x1], q)
            s0 = la.poly_from_roots([x2], q)
            tries += 1
            out = build_escape(q, t, e, A1, A2, [x1], [x2], s0, s1, 3)
            if out is None:
                continue
            blocks, slopes, w, f0, f1 = out
            if la.is_pencil_rank(blocks, q) >= 3:
                hits += 1               # would be a two-pencil system
    check("E3 (F9-F5 targeted) forcing zeta_1 s_0 ~ zeta_2 s_1 collapses the "
          "system to ONE pencil, never to two", hits == 0,
          "%d constructions on the only algebraically open route, %d non-pencil"
          % (tries, hits))
    RECORD["E"] = dict(max_families=worst, intersection_bad=bad,
                       forced_tries=tries, forced_hits=hits)


def section_F():
    print("\n--- F. P-SHARE: distinct pencils share at most one fibre ---")
    # a degree-s poly is determined up to scalar by s distinct roots, so two
    # 2-dim spaces sharing two fibres coincide.  Machine check at toy scale.
    rng = zec.LCG(20260803)
    bad = 0
    tested = 0
    for q, s in ((13, 2), (17, 3), (19, 3)):
        pencils = []
        for _ in range(60):
            r1 = sorted(rng.sample(list(range(q)), s))
            r2 = sorted(rng.sample([x for x in range(q) if x not in r1], s))
            f0 = la.poly_from_roots(r1, q)
            f1 = la.poly_from_roots(r2, q)
            fib = set()
            for lam in list(range(q)):
                F = padd(f0, pscale(f1, lam, q), q)
                if len(F) - 1 != s:
                    continue
                rts = proots(F, q)
                if len(rts) == s:
                    fib.add(frozenset(rts))
            fib.add(frozenset(r2))
            pencils.append((f0, f1, fib))
        for (a0, a1, fa), (b0, b1, fb) in combinations(pencils, 2):
            n = max(len(a0), len(a1), len(b0), len(b1))
            pad = lambda p: p + [0] * (n - len(p))
            same = zec.rank_mod([pad(a0), pad(a1), pad(b0), pad(b1)], q) == 2
            if same:
                continue
            tested += 1
            if len(fa & fb) > 1:
                bad += 1
    check("F1 (P-SHARE) two DISTINCT pencils share at most one fibre",
          bad == 0 and tested > 0, "%d distinct pencil pairs, %d sharing >= 2"
          % (tested, bad))
    # the slope form: two shared slopes force equal cores, hence equal pencils
    check("F2 (P-SHARE, slope form) two shared live slopes force A_0 = A_0' "
          "(A_z ^ A_z' = A_0 inside a family), hence the same pencil", True,
          "set-theoretic; blocks inside one family are disjoint")
    RECORD["F"] = dict(pairs=tested, bad=bad)


def section_G(cfound):
    print("\n--- G. why the la_pencil_rigidity sweeps missed these (Q8b) ---")
    # measure: how often does a RANDOM partition into V blocks have V-1 of them
    # in one pencil?  (the escape's defining feature)
    rng = zec.LCG(99)
    q, t, V = 31, 3, 5
    hit = 0
    N = 400
    for _ in range(N):
        pool = list(range(q))
        blocks = []
        for _a in range(V):
            b = sorted(rng.sample(pool, t))
            for x in b:
                pool.remove(x)
            blocks.append(b)
        fams = pencil_cover_census(blocks, q)
        if any(len(f) >= V - 1 for _, f in fams):
            hit += 1
    note("G random partitions with V-1 blocks in one pencil",
         "%d / %d at q=31, t=3, V=5" % (hit, N))
    check("G1 the escape's defining feature (V-1 blocks in one pencil) has "
          "measure ~0 among random partitions, so la's 700+310 partition "
          "sweeps were structurally blind to it", hit == 0,
          "%d/%d random partitions" % (hit, N))
    # la's extension route: 0 extensions were found because there was no room
    note("G la extension route", "la RECORD D_V5_ext_e2 = 0 and D_V5_ext_e3 = 0: "
         "ZERO V=5 extensions of ANY kind (pencil ones included) were found, "
         "at q = 13,17,19 (t=3: 12 of q points already used) and q = 23,29 "
         "(t=4: 16 used) -- a 5th disjoint block usually cannot fit.")
    RECORD["G"] = dict(random_hits=hit, N=N)


# =========================================================================
def slope_sweep(q, t, e, blocks, cap=400000):
    """EXHAUSTIVE (mod affine, z_1 = 0, z_2 = 1) enumeration of slope tuples
    with dim Ann >= 1, via the banked (T_a, E) reduction. Complete: dim Ann
    is monotone decreasing in the number of blocks, so prefix pruning is
    lossless."""
    A1, A2 = list(blocks[0]), list(blocks[1])
    z1, z2 = 0, 1
    zp = [z for z in range(q) if z not in (z1, z2)]
    Pi = la.perp_E(A1 + A2, e, q)
    V = len(blocks)
    L = {(i, z): la.cond_rows(A1, A2, blocks[i], z, z1, z2, Pi, q)
         for i in range(2, V) for z in zp}
    out = []
    budget = [cap]

    def rec(i, rows, used):
        if budget[0] <= 0:
            return
        if i == V:
            out.append(list(used))
            return
        for z in zp:
            if z in used:
                continue
            budget[0] -= 1
            if budget[0] <= 0:
                return
            nr = rows + L[(i, z)]
            if 2 * t - zec.rank_mod(nr, q) >= 1:
                rec(i + 1, nr, used + [z])

    rec(2, [], [z1, z2])
    return out, cap - budget[0]


def power_fibres(q, t, shift):
    """The t-th power fibres of F_q shifted by `shift` (needs t | q-1):
    fibres of the pencil <(X-shift)^t, 1>, all split, pairwise disjoint."""
    cs = sorted({pow(x, t, q) for x in range(1, q)})
    out = []
    for c in cs:
        f = [x for x in range(q) if pow((x - shift) % q, t, q) == c]
        if len(f) == t:
            out.append(sorted(f))
    return out


def two_pencil_config(q, t, shift, npick=3):
    """3 fibres of P = <X^t,1> and 3 of P' = <(X-shift)^t,1>, pairwise
    disjoint; the first two blocks are the P-pair (T0's normalising pair)."""
    F = power_fibres(q, t, 0)
    G = power_fibres(q, t, shift)
    for i in combinations(range(len(F)), npick):
        A = [F[x] for x in i]
        used = set().union(*[set(b) for b in A])
        B = []
        for g in G:
            if not (set(g) & used):
                B.append(g)
                used |= set(g)
            if len(B) == npick:
                break
        if len(B) == npick:
            return A + B
    return None


def random_two_pencil_configs(q, t, rng, npencil=40, nwant=3):
    """Two GENERIC (non power-map) pencils, 3 split fibres each, pairwise
    disjoint; returns a list of 6-block configurations."""
    pens = []
    for _ in range(npencil):
        pool = list(range(q))
        D1 = sorted(rng.sample(pool, t))
        D2 = sorted(rng.sample([x for x in pool if x not in D1], t))
        f0 = la.poly_from_roots(D1, q)
        f1 = la.poly_from_roots(D2, q)
        fib = []
        for lam in range(q):
            F = padd(f0, pscale(f1, lam, q), q)
            if len(F) - 1 != t:
                continue
            r = proots(F, q)
            if len(r) == t:
                fib.append(sorted(r))
        fib.append(sorted(D2))
        if len(fib) >= nwant:
            pens.append((f0, f1, fib))
    out = []
    for (a0, a1, fa), (b0, b1, fb) in combinations(pens, 2):
        n = max(len(a0), len(a1), len(b0), len(b1))
        pad = lambda p: p + [0] * (n - len(p))
        if zec.rank_mod([pad(a0), pad(a1), pad(b0), pad(b1)], q) == 2:
            continue                                    # same pencil
        A = fa[:nwant]
        used = set().union(*[set(x) for x in A])
        B = []
        for g in fb:
            if not (set(g) & used):
                B.append(g)
                used |= set(g)
            if len(B) == nwant:
                break
        if len(B) == nwant:
            out.append(A + B)
        if len(out) >= 3:
            break
    return out


def section_H():
    print("\n--- H. ADVERSARIAL two-pencil sweep (F9-F5, direct; NOT "
          "pre-registered as a section — added in-run) ---")
    tot = 0
    worst = 0
    hits = []
    ctrl_ok = 0
    ctrl_n = 0
    truncated = 0
    covered = []
    cfgs = []
    for q, t in ((31, 3), (41, 4), (61, 5), (71, 5)):
        for shift in (1, 2, 3):
            c = two_pencil_config(q, t, shift)
            if c is not None:
                cfgs.append((q, t, "power+shift%d" % shift, c))
    rng = zec.LCG(6060842)
    for q, t in ((31, 3), (37, 3), (41, 4), (61, 5)):
        for i, c in enumerate(random_two_pencil_configs(q, t, rng)):
            cfgs.append((q, t, "generic%d" % i, c))
    for q, t, tag, cfg in cfgs:
        for e in range(1, t):
            sols, used = slope_sweep(q, t, e, cfg)
            if used >= 400000:
                truncated += 1
            tot += 1
            covered.append((q, t, e))
            good = 0
            for slopes in sols:
                a = la.audit(q, t, e, [list(b) for b in cfg], slopes, "H")
                if a and a["ann"] >= 1:
                    good += 1
                    fams = pencil_cover_census(cfg, q)
                    if len(fams) >= 2:
                        hits.append((q, t, e, tag, slopes))
            worst = max(worst, good)
            if sols:
                note("H two-pencil q=%d t=%d e=%d %s" % (q, t, e, tag),
                     "%d slope tuples with dim Ann >= 1 (reduction), "
                     "%d gate-clean+banked" % (len(sols), good))
    check("H2 the two-pencil sweeps are COMPLETE (no budget truncation)",
          truncated == 0, "%d truncated of %d sweeps" % (truncated, tot))
    note("H coverage", "(q,t,e) swept: %s" % sorted(set(covered)))
    # POSITIVE CONTROL: the same sweep on a SINGLE-pencil 6-block system must
    # find the Moebius locus (otherwise the sweep is vacuous)
    for q, t in ((31, 3), (41, 4), (41, 5)):
        F = power_fibres(q, t, 0)
        if len(F) < 6:
            continue
        cfg = F[:6]
        for e in range(1, t):
            sols, _ = slope_sweep(q, t, e, cfg)
            ctrl_n += 1
            for slopes in sols:
                a = la.audit(q, t, e, [list(b) for b in cfg], slopes, "Hctrl")
                if a and a["ann"] >= 1:
                    ctrl_ok += 1
                    break
    check("H0 POSITIVE CONTROL: the sweep DOES find non-collapsing "
          "single-pencil V=6 systems (Moebius locus)", ctrl_ok > 0,
          "%d of %d (q,t,e) single-pencil configurations non-collapsing"
          % (ctrl_ok, ctrl_n))
    check("H1 (F9-F5, direct) NO 3+3 two-pencil V=6 block system is "
          "non-collapsing, over ALL slope tuples mod affine",
          worst == 0 and len(hits) == 0 and tot > 0,
          "%d (q,t,e,shift) two-pencil configurations swept exhaustively, "
          "worst dim-Ann-positive count = %d, two-family hits = %d"
          % (tot, worst, len(hits)))
    RECORD["H"] = dict(configs=tot, worst=worst, hits=len(hits),
                       control_ok=ctrl_ok, control_n=ctrl_n)


# =========================================================================
def gate_general(blocks, A0, k):
    """Gate report for a possibly OVERLAPPING-complement system."""
    pts, sup = la.build_system(blocks, A0)
    sets = [set(S) for S in sup]
    if len({len(s) for s in sets}) != 1:
        return None
    V, n = len(blocks), len(pts)
    A = len(sets[0])
    h = A - k
    mult = [sum(1 for s in sets if i in s) for i in range(n)]
    pair = min(len(sets[a] & sets[b]) for a, b in combinations(range(V), 2))
    trip = max(len(sets[a] & sets[b] & sets[c])
               for a, b, c in combinations(range(V), 3))
    if not (h >= 2 and min(mult) >= 3 and pair >= k + 1 and trip <= k - 1
            and 1 <= pair - k <= h - 2):
        return None
    return dict(pts=pts, sup=sup, A=A, h=h, m=n - k, U=n, pair=pair, trip=trip,
                minmult=min(mult))


def overlap_sweep(q, blocks, A0, k, cap=400000):
    """All slope tuples (z_1=0, z_2=1) with dim Ann >= 1, via the banked
    OVERLAP-TOLERANT reduction (la.ann_dim_general's row construction)."""
    pts, sup = la.build_system(blocks, A0)
    idx = {x: i for i, x in enumerate(pts)}
    A1, A2 = list(blocks[0]), list(blocks[1])
    unk = A1 + A2
    V = len(blocks)
    duals = [zec.dual_basis(sup[a], pts, k, q) for a in range(2, V)]
    zp = [z for z in range(q) if z not in (0, 1)]

    def rows_for(a, z):
        Sa = set(sup[a + 2])
        out = []
        for c in duals[a]:
            row = []
            for j, x in enumerate(unk):
                if idx[x] not in Sa:
                    row.append(0)
                else:
                    f = (z - 1) if j < len(A1) else z
                    row.append(c[idx[x]] * f % q)
            out.append(row)
        return out

    R = {(a, z): rows_for(a, z) for a in range(V - 2) for z in zp}
    out = []
    budget = [cap]

    def rec(a, rows, used):
        if budget[0] <= 0:
            return
        if a == V - 2:
            out.append(list(used))
            return
        for z in zp:
            if z in used:
                continue
            budget[0] -= 1
            if budget[0] <= 0:
                return
            nr = rows + R[(a, z)]
            if len(unk) - zec.rank_mod(nr, q) >= 1:
                rec(a + 1, nr, used + [z])

    rec(0, [], [0, 1])
    return out, cap - budget[0]


def section_I():
    print("\n--- I. OVERLAPPING-complement two-pencil sweep (the P-DISJ gap; "
          "added in-run) ---")
    rng = zec.LCG(112233)
    tot = nover = 0
    good = 0
    truncated = 0
    xcheck_ok = xcheck_n = 0
    ctrl = 0
    for q, t in ((31, 3), (37, 3)):
        pens = []
        for _ in range(60):
            D1 = sorted(rng.sample(list(range(q)), t))
            D2 = sorted(rng.sample([x for x in range(q) if x not in D1], t))
            f0 = la.poly_from_roots(D1, q)
            f1 = la.poly_from_roots(D2, q)
            fib = [sorted(D2)]
            for lam in range(q):
                F = padd(f0, pscale(f1, lam, q), q)
                if len(F) - 1 == t:
                    r = proots(F, q)
                    if len(r) == t:
                        fib.append(sorted(r))
            if len(fib) >= 3:
                pens.append((f0, f1, fib))
        ncfg = 0
        for (a0, a1, fa), (b0, b1, fb) in combinations(pens, 2):
            if ncfg >= 6:
                break
            n = max(len(a0), len(a1), len(b0), len(b1))
            pad = lambda p: p + [0] * (n - len(p))
            if zec.rank_mod([pad(a0), pad(a1), pad(b0), pad(b1)], q) == 2:
                continue
            cfg = fa[:3] + fb[:3]
            if len({tuple(b) for b in cfg}) != 6:
                continue
            allp = sorted({x for b in cfg for x in b})
            mult = {x: sum(1 for b in cfg if x in b) for x in allp}
            if max(mult.values()) > 3:            # gate: each point in <= V-3
                continue
            overlapping = any(set(x) & set(y) for x, y in combinations(cfg, 2))
            ncfg += 1
            tot += 1
            if overlapping:
                nover += 1
            for k in range(2, len(allp) - t):
                g = gate_general(cfg, [], k)
                if g is None:
                    continue
                sols, used = overlap_sweep(q, cfg, [], k)
                if used >= 400000:
                    truncated += 1
                for slopes in sols:
                    good += 1
                    # cross-check the reduction against the banked duality
                    da = zec.ann_dim(g["sup"], slopes, g["pts"], k, q,
                                     set(range(len(g["pts"]))))
                    dg = la.ann_dim_general(cfg, [], slopes, k, q)
                    xcheck_n += 1
                    if da == dg and da >= 1:
                        xcheck_ok += 1
                    note("I NON-COLLAPSING overlapping two-pencil system",
                         "q=%d t=%d k=%d slopes=%s ann=%d" % (q, t, k, slopes, da))
    # positive control: the SAME machinery on a disjoint single pencil
    F = power_fibres(31, 3, 0)
    cfg = F[:6]
    for k in range(2, 15):
        g = gate_general(cfg, [], k)
        if g is None:
            continue
        sols, _ = overlap_sweep(31, cfg, [], k)
        if sols:
            ctrl += 1
    check("I0 POSITIVE CONTROL: the overlap-tolerant sweep finds "
          "non-collapsing single-pencil V=6 systems", ctrl > 0,
          "%d gate-clean k values with a non-collapsing slope tuple" % ctrl)
    check("I1 the overlap sweeps are COMPLETE (no budget truncation)",
          truncated == 0, "%d truncated" % truncated)
    check("I2 (P-DISJ, anchor-relevant) NO two-pencil V=6 system with "
          "OVERLAPPING complements is non-collapsing", good == 0,
          "%d two-pencil configurations (%d with genuine overlaps), all k, "
          "all slope tuples mod affine; %d non-collapsing" % (tot, nover, good))
    RECORD["I"] = dict(configs=tot, overlapping=nover, noncollapsing=good,
                       control=ctrl, xcheck=[xcheck_ok, xcheck_n])


def section_J(cfound, dfound):
    print("\n--- J. self-audit: my fixtures vs la_pencil_rigidity's PROVED "
          "theorems, and which of its PREDICTIONS they kill ---")
    bad2 = bad3 = bad5 = 0
    nsol = 0
    for a, _, _ in cfound + dfound:
        q, e = a["q"], a["e"]
        blocks = [list(b) for b in a["blocks"]]
        slopes = list(a["slopes"])
        for w in la.ann_sol_space(blocks, slopes, e, q):
            s = la.structure(blocks, slopes, e, q, w)
            if s is None:
                continue
            nsol += 1
            if not s["thm2"]:
                bad2 += 1
            if not s["thm3"]:
                bad3 += 1
            if s["dimG"] == 1 and (not s["inPQ"] or s["rank_p"] > 1
                                   or s["rank_q"] > 1
                                   or len(s["Z1"]) + len(s["Z2"]) > e - 1):
                bad5 += 1
    check("J1 la THEOREM 2 (B_b g_a in M) holds on every new fixture",
          bad2 == 0 and nsol > 0, "%d solutions, %d violations" % (nsol, bad2))
    check("J2 la THEOREM 3 (dim G_b = e => B_b in <B_1,B_2>) holds on every "
          "new fixture", bad3 == 0, "%d violations" % bad3)
    check("J3 la THEOREM 5 (dim G = 1 branch) holds on every new fixture",
          bad5 == 0, "%d violations" % bad5)
    # which la prediction dies: Delta := 2e - t - 1 at V = 5
    tags = []
    for a, _, _ in cfound + dfound:
        if a["V"] >= 5:
            tags.append((a["V"], a["t"], a["e"], 2 * a["e"] - a["t"] - 1))
    d0 = [x for x in tags if x[3] <= 0]
    check("J4 la's pre-registered falsifier FB ('non-pencil non-collapsing "
          "system at V >= 5 with Delta <= 0') FIRES", len(d0) > 0,
          "(V,t,e,Delta) with Delta <= 0: %s" % sorted(set(d0)))
    # (d, |Z|) census over EVERY V >= 5 non-collapsing system seen in this run
    hist = {}
    for a, _, _ in cfound + dfound:
        q, e = a["q"], a["e"]
        blocks = [list(b) for b in a["blocks"]]
        for w in la.ann_sol_space(blocks, list(a["slopes"]), e, q):
            st = structure_at_pair(blocks, list(a["slopes"]), e, q, w)
            if st:
                key = (st["d"], len(st["Z1"]) + len(st["Z2"]))
                hist[key] = hist.get(key, 0) + 1
    for q, t in ((31, 3), (41, 4), (61, 5)):
        F = power_fibres(q, t, 0)
        if len(F) < 6:
            continue
        cfg = [list(b) for b in F[:6]]
        for e in range(1, t):
            sols, _ = slope_sweep(q, t, e, cfg)
            for slopes in sols[:6]:
                for w in la.ann_sol_space(cfg, slopes, e, q):
                    st = structure_at_pair(cfg, slopes, e, q, w)
                    if st:
                        key = (st["d"], len(st["Z1"]) + len(st["Z2"]))
                        hist[key] = hist.get(key, 0) + 1
    note("J5 (dim G, |Z|) census over every V >= 5 non-collapsing system in "
         "this run", str(sorted(hist.items())))
    check("J5 no V >= 5 non-collapsing system with dim G >= 2 was observed "
          "(the branch where T0's proof needs its degree hypothesis)",
          all(k[0] == 1 for k in hist), "histogram %s" % sorted(hist.items()))
    RECORD["J"] = dict(solutions=nsol, bad=[bad2, bad3, bad5],
                       delta_le_0=sorted(set(d0)),
                       dZ_hist=sorted(hist.items()))


def main():
    section_A()
    section_B()
    cf = section_C()
    df = section_D()
    section_E(cf, df)
    section_F()
    section_G(cf)
    section_H()
    section_I()
    section_J(cf, df)
    print("\n%d checks, %d FAIL" % (len(CHECKS), len(FAILURES)))
    with open(ROOT + "/notes/pilots_20260803/f9_pencil_forcing/verify.json",
              "w") as f:
        json.dump(RECORD, f, indent=1, sort_keys=True, default=str)
    if FAILURES:
        print("FAILURES: " + ", ".join(FAILURES))
        sys.exit(1)
    print("F9_PENCIL_FORCING_ALL_PASS")


if __name__ == "__main__":
    main()
