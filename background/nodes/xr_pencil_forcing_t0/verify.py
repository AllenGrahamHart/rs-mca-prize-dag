#!/usr/bin/env python3
"""Verifier for xr_pencil_forcing_t0.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Pure python integers, deterministic, no third-party imports, NO FILE
READS.  The SOURCE verifier imports two other pilot directories by
absolute path (la_pencil_rigidity, zero_escape_collapse); everything
needed is re-implemented from scratch here, so this node survives the
move to background/nodes/.

  A  Q0: two disjoint equal-size blocks are ALWAYS fibres of a common
     pencil -- so "pencil-structured" is vacuous at family size 2, which
     is why T0 quantifies over pencils carrying >= 3 blocks
  B  P-SHARE, FIBRE form: over EVERY pair of distinct pencils, the
     number of shared fibres is <= 1
  C  P-SHARE, SLOPE form -- COMPUTED.  The source hard-codes this check
     to True (f9/verify.py:574-577, detail "set-theoretic").  Here the
     mechanism is computed: any TWO distinct fibres span the whole
     pencil, hence two shared fibres force the pencils equal
  D  LEMMA 5's algebraic engine: A P = B Q with gcd(A,B) = 1 and
     deg P < deg B forces P = Q = 0  (the coprime-degree kill)
  E  LEMMA 2 (r-formula): dim span{(g'_a, lambda_a g'_a)} = 2 <=>
     dim span{g'_a} = 1, for >= 3 blocks with distinct lambda
  F  the RESIDUAL band arithmetic: t <= 2e-3 <=> h >= 3d+3; the band is
     EMPTY for t <= 4; its smallest shape is exactly (t,e) = (5,4)
  G  the HONEST NEGATIVE: combinatorial M <= 1 is FALSE -- two distinct
     pencils CAN each carry >= 3 pairwise-disjoint blocks.  What kills
     them is realisability, which is NOT reproduced here (recorded)
  H  the Delta bookkeeping catch at V = 6, recorded
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


# --------------------------------------------------------------- polynomials

def trim(a, q):
    a = [x % q for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b, q):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] = (out[i + j] + ai * bj) % q
    return trim(out, q)


def padd(a, b, q):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(n)], q)


def pscale(a, c, q):
    return trim([x * c for x in a], q)


def pdivmod(a, b, q):
    a = trim(a, q)[:]
    b = trim(b, q)
    if not b:
        raise ZeroDivisionError
    out = [0] * max(1, len(a) - len(b) + 1)
    inv = pow(b[-1], q - 2, q)
    while len(a) >= len(b) and a:
        sh = len(a) - len(b)
        c = a[-1] * inv % q
        out[sh] = c
        for i, bc in enumerate(b):
            a[sh + i] = (a[sh + i] - c * bc) % q
        a = trim(a, q)
    return trim(out, q), a


def pgcd(a, b, q):
    a, b = trim(a, q), trim(b, q)
    while b:
        a, b = b, pdivmod(a, b, q)[1]
    if a:
        a = pscale(a, pow(a[-1], q - 2, q), q)
    return a


def locator(pts, q):
    e = [1]
    for t in pts:
        e = pmul(e, [(-t) % q, 1], q)
    return e


def roots_in(a, U, q):
    out = []
    for x in U:
        v = 0
        for c in reversed(a):
            v = (v * x + c) % q
        if v == 0:
            out.append(x)
    return out


def rank_mod(rows, q):
    M = [[x % q for x in r] for r in rows]
    nr = len(M)
    nc = len(M[0]) if M else 0
    r = 0
    for c in range(nc):
        piv = next((i for i in range(r, nr) if M[i][c]), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], q - 2, q)
        M[r] = [x * inv % q for x in M[r]]
        for i in range(nr):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % q for j in range(nc)]
        r += 1
        if r == nr:
            break
    return r


def rref_key(polys, s, q):
    """canonical key of the 2-dim span of `polys` inside F_q[X]_{<=s}."""
    M = [[(p[i] if i < len(p) else 0) % q for i in range(s + 1)] for p in polys]
    nr, nc = len(M), s + 1
    r = 0
    for c in range(nc):
        piv = next((i for i in range(r, nr) if M[i][c]), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], q - 2, q)
        M[r] = [x * inv % q for x in M[r]]
        for i in range(nr):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % q for j in range(nc)]
        r += 1
        if r == nr:
            break
    return tuple(tuple(row) for row in M[:r]), r


# ------------------------------------------------------------- pencil engine

def build_pencils(q, s):
    """All 2-dim spans of two SPLIT monic degree-s polys over U = F_q,
    together with each pencil's set of fibres (root sets of its members
    that split with s distinct roots in U)."""
    U = list(range(q))
    blocks = [frozenset(c) for c in combinations(U, s)]
    ploc = {B: locator(sorted(B), q) for B in blocks}
    pencils = {}
    for B1, B2 in combinations(blocks, 2):
        if B1 & B2:
            continue
        key, r = rref_key([ploc[B1], ploc[B2]], s, q)
        if r != 2 or key in pencils:
            continue
        fib = set()
        p1, p2 = ploc[B1], ploc[B2]
        for a in range(q):
            for b in (0, 1):
                if a == 0 and b == 0:
                    continue
                if b == 0 and a != 1:
                    continue
                m = padd(pscale(p1, a, q), pscale(p2, b, q), q) if b else pscale(p1, a, q)
                m = trim(m, q)
                if len(m) != s + 1:
                    continue
                rts = roots_in(m, U, q)
                if len(rts) == s:
                    fib.add(frozenset(rts))
        # also the b-scaled family a*p1 + p2 covers all [a:1]; add [1:0]
        pencils[key] = fib
    return pencils


# ------------------------------------------------------------------- stage A

def stage_A():
    q, s = 11, 2
    U = list(range(q))
    bad = 0
    tried = 0
    for B1, B2 in combinations([frozenset(c) for c in combinations(U, s)], 2):
        if B1 & B2:
            continue
        tried += 1
        key, r = rref_key([locator(sorted(B1), q), locator(sorted(B2), q)], s, q)
        if r != 2:
            bad += 1
    check("A (Q0): any two DISJOINT equal-size blocks span a 2-dimensional "
          "pencil having both as fibres -- so 'pencil-structured' is VACUOUS "
          "at family size 2, and T0's '>= 3 blocks each' is the right "
          "quantifier, not a convenience",
          bad == 0 and tried > 0, f"{tried} disjoint block pairs, {bad} failures")


# ---------------------------------------------------------------- stages B/C

def stage_B_C():
    for (q, s) in ((11, 2), (13, 2)):
        pen = build_pencils(q, s)
        keys = list(pen)
        worst = 0
        pairs = 0
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                sh = len(pen[keys[i]] & pen[keys[j]])
                pairs += 1
                if sh > worst:
                    worst = sh
        check(f"B (P-SHARE, FIBRE form) q={q} s={s}: every pair of DISTINCT "
              "pencils shares AT MOST ONE fibre",
              worst <= 1, f"{len(keys)} pencils, {pairs} distinct pairs, "
                          f"worst shared = {worst}")

        # C: the SLOPE form's mechanism, COMPUTED (source hard-codes True)
        bad = 0
        tested = 0
        for k in keys:
            fl = sorted(pen[k], key=sorted)
            for F1, F2 in combinations(fl, 2):
                key2, r = rref_key([locator(sorted(F1), q),
                                    locator(sorted(F2), q)], s, q)
                tested += 1
                if r != 2 or key2 != k:
                    bad += 1
        check(f"C (P-SHARE, SLOPE form -- COMPUTED, not asserted) q={q} s={s}: "
              "ANY TWO distinct fibres of a pencil SPAN it, so two shared "
              "fibres force the two pencils equal. The source records this "
              "check as hard-coded True (f9/verify.py:574-577)",
              bad == 0 and tested > 0,
              f"{tested} (pencil, fibre-pair) instances, {bad} failures")


# ------------------------------------------------------------------- stage D

def stage_D():
    """LEMMA 5's engine: A P = B Q, gcd(A,B) = 1, deg P < deg B  =>  P = Q = 0."""
    q = 13
    bad = 0
    tested = 0
    for degA in (2, 3):
        for degB in (2, 3):
            for a0 in range(1, 5):
                for b0 in range(1, 5):
                    A = locator([a0, a0 + 1][:degA] if degA == 2
                                else [a0, a0 + 1, a0 + 2], q)
                    B = locator([b0 + 5, b0 + 6][:degB] if degB == 2
                                else [b0 + 5, b0 + 6, b0 + 7], q)
                    if len(pgcd(A, B, q)) != 1:
                        continue          # need coprime
                    # search P with deg P < deg B and Q with A P = B Q
                    for pc in range(q ** degB):
                        P = trim([(pc // q ** i) % q for i in range(degB)], q)
                        if not P:
                            continue
                        LHS = pmul(A, P, q)
                        Q, rem = pdivmod(LHS, B, q)
                        tested += 1
                        if not rem:
                            # A P divisible by B with gcd(A,B)=1 => B | P,
                            # impossible for 0 < deg P < deg B
                            bad += 1
                    break                 # one (a0,b0) shape is enough per pair
    check("D (LEMMA 5's engine): with gcd(A,B) = 1 and 0 <= deg P < deg B, "
          "A*P is NEVER divisible by B unless P = 0 -- the coprime-degree "
          "forcing behind 'no third block in the pencil intersection'",
          bad == 0 and tested > 0,
          f"{tested} (A,B,P) instances, {bad} spurious divisibilities")


# ------------------------------------------------------------------- stage E

def stage_E():
    """LEMMA 2 (r-formula), over F_q with e-dimensional g'-space."""
    q, e = 13, 3
    bad = []
    tested = 0
    lams = [2, 5, 7, 11]          # distinct
    basis = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    def span_dim(vs):
        return rank_mod(vs, q) if vs else 0

    # d_ij = 1 case: all g' proportional
    for nblk in (3, 4):
        gs = [[(i + 1) % q, 0, 0] for i in range(nblk)]
        vecs = [g + [l * x % q for x in g] for g, l in zip(gs, lams[:nblk])]
        tested += 1
        if not (span_dim(gs) == 1 and span_dim(vecs) == 2):
            bad.append(("d=1", nblk, span_dim(gs), span_dim(vecs)))
    # d_ij >= 2 case: independent g'
    for nblk in (3, 4):
        gs = [basis[i % e][:] for i in range(nblk)]
        vecs = [g + [l * x % q for x in g] for g, l in zip(gs, lams[:nblk])]
        tested += 1
        if not (span_dim(gs) >= 2 and span_dim(vecs) >= 3):
            bad.append(("d>=2", nblk, span_dim(gs), span_dim(vecs)))
    check("E (LEMMA 2, the r-formula): with distinct lambda_a and g'_a != 0, "
          "dim span{(g'_a, lambda_a g'_a)} = 2  <=>  dim span{g'_a} = 1, "
          "given >= 3 blocks off the pair (i.e. V >= 5)",
          not bad and tested > 0, f"{tested} configurations, {bad}")


# ------------------------------------------------------------------- stage F

def stage_F():
    """The residual band, in exact integer arithmetic.
    Admissible window: t >= 2, t+1 <= h <= 2t-1; e = 2t-h; d = h-t."""
    equiv_bad, in_band, smallest = [], [], None
    for t in range(2, 40):
        for h in range(t + 1, 2 * t):
            e = 2 * t - h
            d = h - t
            lhs = (t <= 2 * e - 3)
            rhs = (h >= 3 * d + 3)
            if lhs != rhs:
                equiv_bad.append((t, h, e, d, lhs, rhs))
            if lhs:
                in_band.append((t, e))
                if smallest is None or (t, e) < smallest:
                    smallest = (t, e)
    empty_small = all(t >= 5 for (t, e) in in_band)
    check("F1 (residual, DERIVED equivalence): on the whole admissible "
          "window, t <= 2e-3  <=>  h >= 3d+3 -- the audit's parenthesis, "
          "and confirmation that '2e-3' means 2e MINUS 3, NOT 0.002",
          not equiv_bad, f"{len(equiv_bad)} mismatches over the window")
    check("F2 (residual is EMPTY at small t): the band t <= 2e-3 forces "
          "t >= 5, so it is empty for t <= 4 -- which is exactly why the "
          "audit can say case (b) is 'unconditional for e <= 3'; and its "
          "SMALLEST shape is exactly (t,e) = (5,4)",
          empty_small and smallest == (5, 4),
          f"smallest band shape = {smallest}, {len(in_band)} band shapes "
          f"with t < 40")
    # the complementary proved region
    proved_bad = [(t, e) for t in range(2, 40) for h in range(t + 1, 2 * t)
                  for e in [2 * t - h]
                  if (t >= 2 * e - 2) and (t <= 2 * e - 3)]
    check("F3 (the two regions are complementary): t >= 2e-2 (proved) and "
          "t <= 2e-3 (residual) never overlap", not proved_bad,
          f"{len(proved_bad)} overlaps")


# ------------------------------------------------------------------- stage G

def stage_G():
    """The HONEST NEGATIVE: combinatorial M <= 1 is FALSE."""
    # six disjoint size-s blocks need 6s points, so q MUST exceed 6s:
    # at q = 11, s = 2 no witness can exist (12 > 11).  Use q = 17.
    q, s = 17, 2
    assert q > 6 * s, "field too small for six disjoint blocks"
    pen = build_pencils(q, s)
    keys = [k for k in pen if len(pen[k]) >= 3]
    found = None
    for i in range(len(keys)):
        if found:
            break
        for j in range(i + 1, len(keys)):
            f1 = [x for x in sorted(pen[keys[i]], key=sorted)]
            f2 = [x for x in sorted(pen[keys[j]], key=sorted)]
            for c1 in combinations(f1, 3):
                u1 = set().union(*c1)
                if len(u1) != 3 * s:
                    continue
                for c2 in combinations(f2, 3):
                    u2 = set().union(*c2)
                    if len(u2) != 3 * s or (u1 & u2):
                        continue
                    found = (len(pen[keys[i]]), len(pen[keys[j]]),
                             sorted(sorted(b) for b in c1),
                             sorted(sorted(b) for b in c2))
                    break
                if found:
                    break
            if found:
                break
    check("G (the HONEST NEGATIVE, reproduced): COMBINATORIAL M <= 1 is "
          "FALSE -- two DISTINCT pencils can each carry >= 3 pairwise "
          "disjoint blocks with all six blocks disjoint. So T0 is NOT a "
          "counting fact; what kills these is REALISABILITY (dim Ann), "
          "which this verifier does NOT reproduce",
          found is not None,
          (f"q={q} s={s}: witness FOUND -- pencils with {found[0]} and "
           f"{found[1]} fibres; disjoint triples {found[2]} and {found[3]}")
          if found else f"no witness at q={q} s={s}")
    print("NOTE (replayed from record, NOT recomputed here): the source's "
          "realisability negative is 0/720 multi-pencil configs realised "
          "against a positive control at 200/200 (unified_pencil_bound "
          "PART E), and its own source reports it 'as a NEGATIVE, not as "
          "support for the anchor' because realise_family never returned a "
          "pair, so the gate was never evaluated on a multi-pencil config. "
          "T0's 39/39 census and the 54+12 COMPLETE two-pencil sweeps are "
          "likewise the pilot's, not re-run here.")


# ------------------------------------------------------------------- stage H

def stage_H():
    """Delta bookkeeping: f9's 2e-t-1 equals la's formula only at V = 5."""
    def la_delta(V, e, t):
        return (V - 2) * (e + 1 - t) + 2 * t - V - e + 1

    def f9_delta(e, t):
        return 2 * e - t - 1

    agree_V5 = all(la_delta(5, e, t) == f9_delta(e, t)
                   for t in range(2, 12) for e in range(1, t))
    v6 = (la_delta(6, 2, 3), f9_delta(2, 3))
    check("H (Delta bookkeeping catch): f9's Delta = 2e-t-1 agrees with la's "
          "registered (V-2)(e+1-t)+2t-V-e+1 EXACTLY at V = 5, and DIFFERS at "
          "V = 6 ((t,e)=(3,2): la gives -1, f9 reports 0). Both are <= 0 so "
          "FB fires either way and no verdict changes -- quote (5,3,2,0) as "
          "the exact entry",
          agree_V5 and v6 == (-1, 0), f"V=6 (t,e)=(3,2): la={v6[0]} f9={v6[1]}")


def main():
    stage_A()
    stage_B_C()
    stage_D()
    stage_E()
    stage_F()
    stage_G()
    stage_H()
    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("XR_PENCIL_FORCING_T0_ALL_PASS")


if __name__ == "__main__":
    main()
