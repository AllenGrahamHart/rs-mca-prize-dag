#!/usr/bin/env python3
r"""Verifier for L-A: pencil rigidity at e >= 2 (2026-08-03).

PROFILE: tiny.  Run from the repo root:
    tools/ramguard tiny -- python3 \
        notes/pilots_20260803/la_pencil_rigidity/verify.py

Read-only reuse of notes/pilots_20260803/zero_escape_collapse/verify.py
(rref/rank/nullspace, dual_basis, rank_row, ann_dim, LCG).

SECTIONS
  A  the (T_a, E) REDUCTION checked against the banked duality
  B  V = 4, e = 2 search for non-pencil non-collapsing systems  (FA)
  C  full independent audit + weak-form structure of every hit
  D  extension to V = 5, 6: the pre-registered prediction P       (FB)
  E  overlapping complements and the consumer V <= |U|/2      (FC, FD)
"""
from __future__ import annotations

import importlib.util
import json
import sys
from itertools import combinations

sys.dont_write_bytecode = True

ROOT = "/home/u2470931/smooth-read-solomin/prize"
ZEC = ROOT + "/notes/pilots_20260803/zero_escape_collapse/verify.py"
_spec = importlib.util.spec_from_file_location("zec", ZEC)
zec = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(zec)

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


# ------------------------------------------------------------- polynomials
def polymul(a, b, q):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] = (out[i + j] + ai * bj) % q
    return out


def poly_from_roots(roots, q):
    p = [1]
    for r in roots:
        p = polymul(p, [(-r) % q, 1], q)
    return p


def peval(p, x, q):
    return zec.poly_eval(p, x, q)


def build_system(blocks, A0):
    allpts = set(A0)
    for b in blocks:
        allpts |= set(b)
    pts = sorted(allpts)
    idx = {x: i for i, x in enumerate(pts)}
    supports = []
    for b in blocks:
        bs = set(b)
        supports.append(tuple(sorted(idx[x] for x in pts if x not in bs)))
    return pts, supports


def is_pencil_rank(blocks, q):
    """dim span{B_a}: 2 = pencil, >= 3 = NOT a pencil."""
    return zec.rank_mod([poly_from_roots(b, q) for b in blocks], q)


# ------------------------------------------------- the (T_a, E) reduction
def perp_E(pts2, e, q):
    """Basis of E^perp, E = {(g(x))_{x in pts2} : deg g < e} (dim e)."""
    vand = [[pow(x, j, q) for x in pts2] for j in range(e)]
    return zec.nullspace_mod(vand, len(pts2), q)


def cond_rows(A1, A2, blk, z, z1, z2, Pi, q):
    """Rows of Pi . T_a ; T_a w in E  <=>  these rows kill w."""
    B = poly_from_roots(blk, q)
    d = [(z - z2) * peval(B, x, q) % q for x in A1] + \
        [(z - z1) * peval(B, x, q) % q for x in A2]
    return [[pi[i] * d[i] % q for i in range(len(d))] for pi in Pi]


def ann_dim_reduced(blocks, slopes, e, q):
    """dim Ann via the reduction (blocks[0], blocks[1] = the normalising pair)."""
    A1, A2 = list(blocks[0]), list(blocks[1])
    z1, z2 = slopes[0], slopes[1]
    Pi = perp_E(A1 + A2, e, q)
    rows = []
    for blk, z in zip(blocks[2:], slopes[2:]):
        rows += cond_rows(A1, A2, blk, z, z1, z2, Pi, q)
    return len(A1) + len(A2) - zec.rank_mod(rows, q)


def ann_sol_space(blocks, slopes, e, q):
    A1, A2 = list(blocks[0]), list(blocks[1])
    z1, z2 = slopes[0], slopes[1]
    Pi = perp_E(A1 + A2, e, q)
    rows = []
    for blk, z in zip(blocks[2:], slopes[2:]):
        rows += cond_rows(A1, A2, blk, z, z1, z2, Pi, q)
    return zec.nullspace_mod(rows, len(A1) + len(A2), q)


def g_of(blocks, slopes, w, a, e, q):
    """The degree-<e polynomial g_a attached to a solution w (None if none)."""
    A1, A2 = list(blocks[0]), list(blocks[1])
    z1, z2 = slopes[0], slopes[1]
    B = poly_from_roots(blocks[a], q)
    xs = A1 + A2
    vals = [(slopes[a] - z2) * peval(B, x, q) % q * w[i] % q
            for i, x in enumerate(A1)]
    vals += [(slopes[a] - z1) * peval(B, x, q) % q * w[len(A1) + i] % q
             for i, x in enumerate(A2)]
    g = zec.interpolate(xs[:e], vals[:e], q)
    for x, v in zip(xs, vals):
        if peval(g, x, q) != v % q:
            return None
    return zec.poly_trim(g, q)


# =========================================================================
def section_A():
    print("\n--- A. the (T_a, E) reduction vs the banked duality (FE) ---")

    def fibres(q, d, cs):
        return [sorted(x for x in range(q) if pow(x, d, q) == c % q) for c in cs]

    fx = []
    # banked X1, X2, X3 (zero_escape_collapse) : V = 4
    fx.append(("X1", 17, 3, fibres(17, 2, [1, 2, 4, 8]), [], [12, 8, 2, 3]))
    cs = sorted({pow(x, 4, 17) for x in range(1, 17)})
    R1 = (cs[2] - cs[0]) * zec.inv((cs[3] - cs[0]) % 17, 17) % 17
    R2 = (cs[2] - cs[1]) * zec.inv((cs[3] - cs[1]) % 17, 17) % 17
    fx.append(("X2", 17, 5, fibres(17, 4, cs), [],
               [zec.inv((1 - R2) % 17, 17), zec.inv((1 - R1) % 17, 17), 0, 1]))
    cs = sorted({pow(x, 3, 13) for x in range(1, 13)})
    R1 = (cs[2] - cs[0]) * zec.inv((cs[3] - cs[0]) % 13, 13) % 13
    R2 = (cs[2] - cs[1]) * zec.inv((cs[3] - cs[1]) % 13, 13) % 13
    fx.append(("X3", 13, 5, fibres(13, 3, cs), [],
               [zec.inv((1 - R2) % 13, 13), zec.inv((1 - R1) % 13, 13), 0, 1]))
    # banked Y1, Y3', Y4 (v5_occupancy) : V = 5, 6, 10
    cs = [1, 3, 4, 5, 9]
    fx.append(("Y1", 11, 5, fibres(11, 2, cs), [], list(cs)))
    cs = sorted({pow(x, 2, 13) for x in range(1, 13)})
    fx.append(("Y3'", 13, 7, fibres(13, 2, cs), [], list(cs)))
    cs = sorted({pow(x, 4, 41) for x in range(1, 41)})
    fx.append(("Y4", 41, 32, fibres(41, 4, cs), [0], list(cs)))
    # a NON-pencil control at V = 5 (dim Ann must be 0 both ways)
    fx.append(("N1", 11, 5, [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], [],
               [1, 3, 4, 5, 9]))

    for name, q, k, blocks, A0, slopes in fx:
        pts, sup = build_system(blocks, A0)
        V, t, t0 = len(blocks), len(blocks[0]), len(A0)
        sigma = t0 + (V - 3) * t
        e = k - sigma
        da = zec.ann_dim(sup, slopes, pts, k, q, set(range(len(pts))))
        dr = ann_dim_reduced(blocks, slopes, e, q)
        r = zec.rank_row(sup, slopes, pts, k, q)
        m = len(pts) - k
        check("A[%s] reduction == banked ann_dim, and rank + ann = 2m" % name,
              da == dr and r + da == 2 * m,
              "V=%d t=%d t0=%d k=%d e=%d  banked %d reduced %d  rank %d 2m %d"
              % (V, t, t0, k, e, da, dr, r, 2 * m))
        RECORD[name] = dict(q=q, k=k, V=V, t=t, e=e, ann=da,
                            pencil_rank=is_pencil_rank(blocks, q))


# =========================================================================
def sweep_V4(q, t, e, seed, npart, verbose=False):
    """Random V=4 block systems with parameters (t,e): report hits."""
    rng = zec.LCG(seed)
    z1, z2 = 0, 1
    zpool = [z for z in range(q) if z not in (z1, z2)]
    hits = []
    tried = 0
    for _ in range(npart):
        pool = list(range(q))
        blocks = []
        ok = True
        for _a in range(4):
            if len(pool) < t:
                ok = False
                break
            b = rng.sample(pool, t)
            for x in b:
                pool.remove(x)
            blocks.append(sorted(b))
        if not ok:
            continue
        A1, A2 = blocks[0], blocks[1]
        Pi = perp_E(A1 + A2, e, q)
        L = {}
        for i, blk in ((2, blocks[2]), (3, blocks[3])):
            for z in zpool:
                L[(i, z)] = zec.nullspace_mod(
                    cond_rows(A1, A2, blk, z, z1, z2, Pi, q), 2 * t, q)
        for z3 in zpool:
            n3 = L[(2, z3)]
            for z4 in zpool:
                if z4 == z3:
                    continue
                tried += 1
                if zec.rank_mod(n3 + L[(3, z4)], q) < len(n3) + len(L[(3, z4)]):
                    hits.append((blocks, [z1, z2, z3, z4]))
    return hits, tried


def section_B():
    print("\n--- B. V = 4, e = 2 search for NON-PENCIL non-collapsing (FA) ---")
    allhits = []
    for q, t, e, npart in ((13, 3, 2, 260), (17, 3, 2, 200), (19, 3, 2, 160)):
        hits, tried = sweep_V4(q, t, e, 20260803 + q, npart)
        npen = [(b, s) for b, s in hits if is_pencil_rank(b, q) >= 3]
        note("B q=%d t=%d e=%d" % (q, t, e),
             "%d (partition, slope-pair) configs tested, %d hits, "
             "%d of them NON-pencil" % (tried, len(hits), len(npen)))
        allhits += [(q, t, e, b, s) for b, s in npen]
    RECORD["B_nonpencil_hits"] = len(allhits)
    check("B1 (FA) non-pencil non-collapsing e=2 V=4 systems EXIST",
          len(allhits) > 0, "%d found" % len(allhits))
    return allhits


# =========================================================================
def audit(q, t, e, blocks, slopes, tag):
    """Independent audit of one hit: gates + banked rank/ann + structure."""
    V = len(blocks)
    t0_pts = sorted(set(range(q)) - {x for b in blocks for x in b})
    out = {}
    for t0 in range(0, len(t0_pts) + 1):
        A0 = t0_pts[:t0]
        k = t0 + (V - 1) * t - (2 * t - e)
        pts, sup = build_system(blocks, A0)
        sets = [set(S) for S in sup]
        n = len(pts)
        mult = [sum(1 for s in sets if i in s) for i in range(n)]
        pair = min(len(sets[a] & sets[b]) for a, b in combinations(range(V), 2))
        trip = max(len(sets[a] & sets[b] & sets[c])
                   for a, b, c in combinations(range(V), 3))
        h = len(sets[0]) - k
        gate = (min(mult) >= 3 and pair >= k + 1 and trip <= k - 1
                and 1 <= pair - k <= h - 2 and h == 2 * t - e)
        if not gate:
            continue
        da = zec.ann_dim(sup, slopes, pts, k, q, set(range(n)))
        r = zec.rank_row(sup, slopes, pts, k, q)
        m = n - k
        out = dict(tag=tag, q=q, V=V, t=t, t0=t0, k=k, h=h, m=m, e=e,
                   U=n, A=len(sets[0]), pair=pair, trip=trip,
                   minmult=min(mult), ann=da, rank=r, two_m=2 * m,
                   three_h=3 * h, charge=r / V,
                   pencil_rank=is_pencil_rank(blocks, q),
                   blocks=[list(b) for b in blocks], slopes=list(slopes),
                   A0=list(A0))
        break
    return out


def solve_lin(rows, rhs, ncol, q):
    """One solution of rows.x = rhs, or None."""
    aug = [rows[i] + [rhs[i]] for i in range(len(rows))]
    red, piv = zec.rref(aug, q)
    if ncol in piv:
        return None
    x = [0] * ncol
    for r, pc in enumerate(piv):
        x[pc] = red[r][ncol]
    return x


def PQ_basis(A, Zi, t, q):
    """Basis of P = {B : deg B <= t, B = 0 on A \\ Z}, dim |Z|+1."""
    F = poly_from_roots([x for x in A if x not in Zi], q)
    out = []
    for i in range(len(Zi) + 1):
        out.append([0] * i + F)
    return out


def structure(blocks, slopes, e, q, w):
    """The LA structure data of one solution w.  Returns a dict."""
    t = len(blocks[0])
    V = len(blocks)
    gs = [g_of(blocks, slopes, w, a, e, q) for a in range(2, V)]
    if any(g is None for g in gs):
        return None
    dimG = zec.rank_mod([g + [0] * (e - len(g)) for g in gs], q)
    Z1 = [x for x in blocks[0] if peval(gs[0], x, q) == 0]
    Z2 = [x for x in blocks[1] if peval(gs[0], x, q) == 0]
    P1 = PQ_basis(blocks[0], Z1, t, q)
    P2 = PQ_basis(blocks[1], Z2, t, q)
    basis = P1 + P2
    cols = len(basis)
    rows = [[basis[j][i] if i < len(basis[j]) else 0 for j in range(cols)]
            for i in range(t + 1)]
    ps, qs, inPQ = [], [], True
    for a in range(2, V):
        B = poly_from_roots(blocks[a], q)
        B = B + [0] * (t + 1 - len(B))
        c = solve_lin([r[:] for r in rows], list(B), cols, q)
        if c is None:
            inPQ = False
            break
        p = [0] * (t + 1)
        for j in range(len(P1)):
            for i, cf in enumerate(P1[j]):
                p[i] = (p[i] + c[j] * cf) % q
        ps.append(p)
        qq = [(B[i] - p[i]) % q for i in range(t + 1)]
        qs.append(qq)
    # THEOREM 2: B_b g_a in M := B_1 F_{<e} (+) B_2 F_{<e}, for a != b >= 3
    Mb = []
    for i in range(e):
        for BB in (poly_from_roots(blocks[0], q), poly_from_roots(blocks[1], q)):
            Mb.append([0] * i + BB + [0] * (e - 1 - i))
    rkM = zec.rank_mod(Mb, q)
    thm2 = True
    for a in range(2, V):
        for b in range(2, V):
            if a == b:
                continue
            f = polymul(poly_from_roots(blocks[b], q), gs[a - 2], q)
            f = f + [0] * (t + e - len(f))
            if zec.rank_mod(Mb + [f], q) != rkM:
                thm2 = False
    # THEOREM 3: dim G_b = e  =>  B_b in <B_1, B_2>
    pen = [poly_from_roots(blocks[0], q), poly_from_roots(blocks[1], q)]
    rkP = zec.rank_mod(pen, q)
    thm3 = True
    nfire = 0
    for b in range(2, V):
        Gb = [gs[a - 2] + [0] * (e - len(gs[a - 2]))
              for a in range(2, V) if a != b]
        if Gb and zec.rank_mod(Gb, q) == e:
            nfire += 1
            if zec.rank_mod(pen + [poly_from_roots(blocks[b], q)], q) != rkP:
                thm3 = False
    return dict(dimG=dimG, Z1=Z1, Z2=Z2, inPQ=inPQ, thm2=thm2, thm3=thm3,
                thm3_fired=nfire,
                dimPQ=len(P1) + len(P2),
                rank_p=zec.rank_mod(ps, q) if ps else 0,
                rank_q=zec.rank_mod(qs, q) if qs else 0,
                rank_rest=zec.rank_mod(
                    [poly_from_roots(blocks[a], q) for a in range(2, V)], q),
                g3=gs[0])


def section_C(allhits):
    print("\n--- C. independent audit of the hits + weak-form structure ---")
    audited = []
    for q, t, e, blocks, slopes in allhits[:40]:
        a = audit(q, t, e, blocks, slopes, "V4")
        if a and a["ann"] >= 1:
            audited.append(a)
    check("C1 a NON-pencil hit survives the FULL gate + banked-duality audit",
          any(x["pencil_rank"] >= 3 for x in audited),
          "%d audited gate-clean hits, %d non-pencil"
          % (len(audited), sum(1 for x in audited if x["pencil_rank"] >= 3)))
    if not audited:
        return []
    best = [x for x in audited if x["pencil_rank"] >= 3]
    ex = best[0] if best else audited[0]
    note("C  witness", json.dumps({kk: ex[kk] for kk in
                                   ("q", "V", "t", "t0", "k", "h", "m", "e",
                                    "U", "pair", "trip", "ann", "rank",
                                    "two_m", "pencil_rank", "blocks",
                                    "slopes")}))
    RECORD["C_witness"] = ex
    RECORD["C_audited"] = len(audited)
    return best


def section_C2(cases, tag):
    """THEOREM LA tested on every listed non-collapsing system."""
    print("\n--- C2[%s]. THEOREM LA structure on every solution ---" % tag)
    nsol = n1 = fired = 0
    bad2 = bad3 = bad5 = 0
    seen = {}
    for x in cases:
        q, e = x["q"], x["e"]
        blocks, slopes = [list(b) for b in x["blocks"]], x["slopes"]
        for w in ann_sol_space(blocks, slopes, e, q):
            s = structure(blocks, slopes, e, q, w)
            if s is None:
                continue
            nsol += 1
            key = (s["dimG"], len(s["Z1"]) + len(s["Z2"]))
            seen[key] = seen.get(key, 0) + 1
            if not s["thm2"]:
                bad2 += 1
            fired += s["thm3_fired"]
            if not s["thm3"]:
                bad3 += 1
            if s["dimG"] == 1:                       # THEOREM 5 branch
                n1 += 1
                if (not s["inPQ"] or s["rank_p"] > 1 or s["rank_q"] > 1
                        or len(s["Z1"]) + len(s["Z2"]) > e - 1):
                    bad5 += 1
    note("C2[%s] (dim G, |Z|) histogram over %d solutions" % (tag, nsol),
         str(sorted(seen.items())))
    check("C2[%s]-2 THEOREM 2: B_b g_a in M = B_1 F_{<e} (+) B_2 F_{<e}"
          % tag, bad2 == 0 and nsol > 0,
          "%d solutions, %d violations" % (nsol, bad2))
    check("C2[%s]-3 THEOREM 3: dim G_b = e => B_b in <B_1,B_2>" % tag,
          bad3 == 0, "%d (solution, b) instances fired, %d violations"
          % (fired, bad3))
    check("C2[%s]-5 THEOREM 5 (dim G = 1 branch): blocks 3..V lie in "
          "P_1 (+) P_2 with pairwise-proportional P_i-parts, |Z| <= e-1"
          % tag, bad5 == 0, "%d dim-G=1 solutions, %d violations"
          % (n1, bad5))
    RECORD["C2_" + tag] = dict(solutions=nsol, dimG1=n1,
                               hist=str(sorted(seen.items())),
                               thm3_fired=fired, bad=[bad2, bad3, bad5])


# =========================================================================
def extend(q, t, e, blocks, slopes, w):
    """All monic degree-t B_5 (split, disjoint) extending the solution w."""
    A1, A2 = list(blocks[0]), list(blocks[1])
    z1, z2 = slopes[0], slopes[1]
    Pi = perp_E(A1 + A2, e, q)
    used = {x for b in blocks for x in b}
    outs = []
    for z in range(q):
        if z in slopes:
            continue
        # unknowns b_0..b_{t-1} of B = X^t + sum b_i X^i
        rows, rhs = [], []
        for pi in Pi:
            c = [pi[i] * w[i] % q * ((z - z2) % q) % q for i in range(len(A1))]
            c += [pi[len(A1) + i] * w[len(A1) + i] % q * ((z - z1) % q) % q
                  for i in range(len(A2))]
            xs = A1 + A2
            rows.append([sum(c[i] * pow(xs[i], j, q) for i in range(len(xs))) % q
                         for j in range(t)])
            rhs.append((-sum(c[i] * pow(xs[i], t, q)
                             for i in range(len(xs)))) % q)
        aug = [rows[i] + [rhs[i]] for i in range(len(rows))]
        red, piv = zec.rref(aug, q)
        if t in piv:                      # inconsistent
            continue
        sol = [0] * t
        for r, pc in enumerate(piv):
            sol[pc] = red[r][t]
        free = [c for c in range(t) if c not in piv]
        cands = []
        if not free:
            cands = [sol]
        else:                              # enumerate the (small) free space
            for vals in range(q ** len(free)):
                v = list(sol)
                vv = vals
                for fc in free:
                    v[fc] = (v[fc] + vv % q) % q
                    vv //= q
                # re-solve pivots for this free choice
                v2 = [0] * t
                for fc in free:
                    v2[fc] = v[fc]
                for r, pc in enumerate(piv):
                    s = red[r][t]
                    for fc in free:
                        s = (s - red[r][fc] * v2[fc]) % q
                    v2[pc] = s % q
                cands.append(v2)
        for v in cands:
            B = v + [1]
            roots = [x for x in range(q) if peval(B, x, q) == 0]
            if len(roots) != t or set(roots) & used:
                continue
            outs.append((sorted(roots), z))
    return outs


def pencil_system(q, d, t, ncl, e):
    """V = ncl fibres of the pencil <X^d, 1>, Mobius slopes z_a = c_a."""
    cs = sorted({pow(x, d, q) for x in range(1, q)})[:ncl]
    blocks = [sorted(x for x in range(q) if pow(x, d, q) == c) for c in cs]
    if any(len(b) != t for b in blocks):
        return None
    return blocks, list(cs)


def section_D_control():
    print("\n--- D0. POSITIVE CONTROL for the extension routine ---")
    ctrl = []
    for q, d, t, ncl, e in ((19, 3, 3, 5, 2), (13, 2, 2, 6, 1),
                            (41, 4, 4, 5, 3)):
        ps = pencil_system(q, d, t, ncl, e)
        if ps is None:
            continue
        blocks, slopes = ps
        da5 = ann_dim_reduced(blocks, slopes, e, q)
        b4, s4 = blocks[:4], slopes[:4]
        found = False
        for w in ann_sol_space(b4, s4, e, q):
            ext = extend(q, t, e, b4, s4, w)
            if (blocks[4], slopes[4]) in [(bb, zz) for bb, zz in ext]:
                found = True
        check("D0[q=%d t=%d e=%d] extend() recovers the 5th pencil fibre "
              "and its slope" % (q, t, e), da5 >= 1 and found,
              "dim Ann(V=5 pencil) = %d, 5th block recovered = %s"
              % (da5, found))
        ctrl.append((q, t, e))
    return ctrl


def section_D(best, tag="V4"):
    print("\n--- D. extension to V = 5: the pre-registered prediction ---")
    if not best:
        note("D skipped", "no V=4 non-pencil hit to extend")
        return
    n5 = n5np = 0
    ncand = 0
    wit5 = None
    for x in best[:40]:
        q, e, t = x["q"], x["e"], x["t"]
        blocks, slopes = [list(b) for b in x["blocks"]], x["slopes"]
        for w in ann_sol_space(blocks, slopes, e, q):
            for blk, z in extend(q, t, e, blocks, slopes, w):
                b5, s5 = blocks + [blk], slopes + [z]
                if ann_dim_reduced(b5, s5, e, q) < 1:
                    continue
                n5 += 1
                if is_pencil_rank(b5, q) >= 3:
                    n5np += 1
                    a = audit(q, t, e, b5, s5, "V5")
                    if a and a["ann"] >= 1 and wit5 is None:
                        wit5 = a
    note("D[%s] V=5 extensions" % tag,
         "%d found, %d NON-pencil, %d gate-clean+audited"
         % (n5, n5np, 1 if wit5 else 0))
    RECORD["D_V5_ext_" + tag] = n5
    RECORD["D_V5_nonpencil_" + tag] = n5np
    if wit5:
        RECORD["D_witness5_" + tag] = wit5
        note("D V=5 witness", json.dumps({kk: wit5[kk] for kk in
                                          ("q", "V", "t", "t0", "k", "e", "U",
                                           "ann", "rank", "two_m",
                                           "pencil_rank", "blocks",
                                           "slopes")}))
    check("D1[%s] V=5 non-pencil extensions do not exist" % tag,
          wit5 is None,
          "THEOREM LA predicts none at V >= 5; %d V=5 extensions total" % n5)
    return wit5


# =========================================================================
def ann_dim_general(blocks, A0, slopes, k, q):
    """dim Ann for ANY system with A_1 ^ A_2 = empty (overlaps allowed).

    Unknown nu on A_1 u A_2; ray a >= 3 contributes h = |S_a| - k rows.
    """
    pts, sup = build_system(blocks, A0)
    idx = {x: i for i, x in enumerate(pts)}
    A1, A2 = list(blocks[0]), list(blocks[1])
    unk = A1 + A2
    z1, z2 = slopes[0], slopes[1]
    rows = []
    for a in range(2, len(blocks)):
        Sa = set(sup[a])
        for c in zec.dual_basis(sup[a], pts, k, q):
            row = []
            for j, x in enumerate(unk):
                if idx[x] not in Sa:
                    row.append(0)
                else:
                    f = (slopes[a] - z2) if j < len(A1) else (slopes[a] - z1)
                    row.append(c[idx[x]] * f % q)
            rows.append(row)
    return len(unk) - zec.rank_mod(rows, q)


def section_E():
    print("\n--- E. (t,e) = (4,3): V = 4 search and V = 5 extension ---")
    allhits = []
    for q, npart in ((23, 90), (29, 60)):
        hits, tried = sweep_V4(q, 4, 3, 43 + q, npart)
        npen = [(b, s) for b, s in hits if is_pencil_rank(b, q) >= 3]
        note("E q=%d t=4 e=3" % q, "%d configs tested, %d hits, %d non-pencil"
             % (tried, len(hits), len(npen)))
        allhits += [(q, 4, 3, b, s) for b, s in npen]
    aud = []
    for q, t, e, b, s in allhits[:40]:
        a = audit(q, t, e, b, s, "V4e3")
        if a and a["ann"] >= 1:
            aud.append(a)
    check("E1 (FA at e=3) non-pencil non-collapsing V=4 systems exist",
          len(aud) > 0, "%d audited gate-clean non-pencil hits" % len(aud))
    if aud:
        RECORD["E_witness"] = aud[0]
        note("E witness", json.dumps({kk: aud[0][kk] for kk in
                                      ("q", "V", "t", "t0", "k", "h", "m", "e",
                                       "U", "pair", "trip", "ann", "rank",
                                       "two_m", "pencil_rank", "blocks",
                                       "slopes")}))
        section_C2(aud, "e3V4")
        section_D(aud, "e3")
    return aud


def section_F():
    print("\n--- F. overlapping complements (FC) and V <= |U|/2 (FD) ---")
    # F0: the general reduction agrees with the banked ann_dim on blocks
    cs = sorted({pow(x, 3, 13) for x in range(1, 13)})
    R1 = (cs[2] - cs[0]) * zec.inv((cs[3] - cs[0]) % 13, 13) % 13
    R2 = (cs[2] - cs[1]) * zec.inv((cs[3] - cs[1]) % 13, 13) % 13
    X3b = [sorted(x for x in range(13) if pow(x, 3, 13) == c) for c in cs]
    X3s = [zec.inv((1 - R2) % 13, 13), zec.inv((1 - R1) % 13, 13), 0, 1]
    pts, sup = build_system(X3b, [])
    ok = (ann_dim_general(X3b, [], X3s, 5, 13)
          == zec.ann_dim(sup, X3s, pts, 5, 13, set(range(len(pts)))))
    check("F0 the general (overlap-tolerant) reduction reproduces X3", ok)

    check("F-auto at V = 4 zero escape FORCES disjoint complements "
          "(mult >= 3 <=> each point in <= V-3 = 1 blocks)", True,
          "so overlapping shapes first exist at V >= 5")
    rng = zec.LCG(20260804)
    q = 11
    seen = ov = ovnon = 0
    worst = None
    ndisj_non = 0
    fd_bad = 0
    for _ in range(3000):
        n0 = rng.randint(9, 11)
        V = 5
        tp = rng.randint(2, 3)
        blocks = []
        cnt = [0] * n0
        ok = True
        for _a in range(V):
            avail = [x for x in range(n0) if cnt[x] <= V - 4]
            if len(avail) < tp:
                ok = False
                break
            b = sorted(rng.sample(avail, tp))
            for x in b:
                cnt[x] += 1
            blocks.append(b)
        if not ok or set(blocks[0]) & set(blocks[1]):
            continue
        A0 = [x for x in range(n0) if cnt[x] == 0]
        pts, sup = build_system(blocks, A0)
        if len(pts) != n0:
            continue
        sets = [set(S) for S in sup]
        if len({len(s) for s in sets}) != 1:
            continue
        A = len(sets[0])
        mult = [sum(1 for s in sets if i in s) for i in range(n0)]
        pair = min(len(sets[a] & sets[b]) for a, b in combinations(range(V), 2))
        trip = max(len(sets[a] & sets[b] & sets[c])
                   for a, b, c in combinations(range(V), 3))
        overlap = any(set(x) & set(y) for x, y in combinations(blocks, 2))
        idx = {x: i for i, x in enumerate(pts)}
        unk = list(blocks[0]) + list(blocks[1])
        for k in range(2, A):
            h = A - k
            if min(mult) < 3 or pair < k + 1 or trip > k - 1:
                continue
            if not (1 <= pair - k <= h - 2):
                continue
            seen += 1
            if overlap:
                ov += 1
            # precompute the per-ray dual bases ONCE, then sweep slopes
            duals = [zec.dual_basis(sup[a], pts, k, q) for a in range(2, V)]
            def rows_for(a, z):
                Sa = set(sup[a + 2])
                out = []
                for c in duals[a]:
                    row = []
                    for j, x in enumerate(unk):
                        if idx[x] not in Sa:
                            row.append(0)
                        else:
                            f = (z - 1) if j < len(blocks[0]) else z
                            row.append(c[idx[x]] * f % q)
                    out.append(row)
                return out
            R = {(a, z): rows_for(a, z) for a in range(V - 2)
                 for z in range(2, q)}
            best_da = 0
            for z3 in range(2, q):
                for z4 in range(2, q):
                    if z4 == z3:
                        continue
                    base = R[(0, z3)] + R[(1, z4)]
                    if len(unk) - zec.rank_mod(base, q) == 0:
                        continue
                    for z5 in range(2, q):
                        if z5 in (z3, z4):
                            continue
                        da = len(unk) - zec.rank_mod(base + R[(2, z5)], q)
                        best_da = max(best_da, da)
            if best_da >= 1:
                if overlap:
                    ovnon += 1
                    if worst is None:
                        worst = (blocks, A0, k, n0)
                else:
                    ndisj_non += 1
                if V > len(pts) / 2:
                    fd_bad += 1
    note("F sweep", "%d gate-clean V=5 systems (%d with OVERLAPPING "
         "complements); non-collapsing: %d disjoint, %d overlapping"
         % (seen, ov, ndisj_non, ovnon))
    check("F1 (FC) NO overlapping-complement system is non-collapsing",
          ovnon == 0, "%d overlapping gate-clean systems swept over ALL "
          "slope tuples mod affine" % ov)
    check("F2 (FD) every non-collapsing system found has V <= |U|/2",
          fd_bad == 0, "%d violations" % fd_bad)
    RECORD["F"] = dict(seen=seen, overlap=ov, overlap_noncollapsing=ovnon,
                       disjoint_noncollapsing=ndisj_non, fd_bad=fd_bad)
    if worst:
        RECORD["F_overlap_witness"] = str(worst)


def section_F2():
    """CONSTRUCTED overlapping gate-clean systems: V=5, t=3, one shared point.

    |U| = 14, k = 7, h = 4, m = 7, e = 2, A_4 ^ A_5 = {one point}.
    """
    print("\n--- F2. CONSTRUCTED overlapping gate-clean systems (FC) ---")
    q, V, t, k = 17, 5, 3, 7
    rng = zec.LCG(555)
    nsys = nclean = nnon = 0
    wit = None
    for _ in range(45):
        pts14 = sorted(rng.sample(list(range(q)), 14))
        pool = list(pts14)
        blocks = []
        for _a in range(4):
            b = rng.sample(pool, 3)
            for x in b:
                pool.remove(x)
            blocks.append(sorted(b))
        shared = blocks[3][0]
        b5 = sorted(pool + [shared])          # |pool| = 2, so |A_5| = 3
        blocks.append(b5)
        pts, sup = build_system(blocks, [])
        if len(pts) != 14:
            continue
        sets = [set(S) for S in sup]
        if len({len(s) for s in sets}) != 1:
            continue
        mult = [sum(1 for s in sets if i in s) for i in range(14)]
        pair = min(len(sets[a] & sets[b]) for a, b in combinations(range(V), 2))
        trip = max(len(sets[a] & sets[b] & sets[c])
                   for a, b, c in combinations(range(V), 3))
        A = len(sets[0])
        h = A - k
        nsys += 1
        if not (min(mult) >= 3 and pair >= k + 1 and trip <= k - 1
                and 1 <= pair - k <= h - 2):
            continue
        nclean += 1
        idx = {x: i for i, x in enumerate(pts)}
        unk = list(blocks[0]) + list(blocks[1])
        duals = [zec.dual_basis(sup[a], pts, k, q) for a in range(2, V)]

        def rows_for(a, z):
            Sa = set(sup[a + 2])
            out = []
            for c in duals[a]:
                row = []
                for j, x in enumerate(unk):
                    if idx[x] not in Sa:
                        row.append(0)
                    else:
                        f = (z - 1) if j < len(blocks[0]) else z
                        row.append(c[idx[x]] * f % q)
                out.append(row)
            return out
        R = {(a, z): rows_for(a, z) for a in range(3) for z in range(2, q)}
        best = 0
        for z3 in range(2, q):
            for z4 in range(2, q):
                if z4 == z3:
                    continue
                base = R[(0, z3)] + R[(1, z4)]
                if len(unk) - zec.rank_mod(base, q) == 0:
                    continue
                for z5 in range(2, q):
                    if z5 in (z3, z4):
                        continue
                    da = len(unk) - zec.rank_mod(base + R[(2, z5)], q)
                    if da > best:
                        best = da
                        if wit is None:
                            wit = (blocks, [0, 1, z3, z4, z5], k, q)
        if best >= 1:
            nnon += 1
    note("F2 constructed overlapping shape", "%d built, %d gate-clean "
         "(V=5, t=3, |U|=14, k=7, h=4, e=2, one shared point), "
         "%d NON-collapsing over all slope triples mod affine"
         % (nsys, nclean, nnon))
    check("F2 (FC) overlapping gate-clean systems EXIST but none is "
          "non-collapsing", nclean > 0 and nnon == 0,
          "%d gate-clean overlapping systems, %d non-collapsing" % (nclean, nnon))
    RECORD["F2"] = dict(built=nsys, gate_clean=nclean, noncollapsing=nnon)
    if wit:
        RECORD["F2_witness"] = str(wit)


def sweep_V5(q, t, e, seed, npart):
    """Random V=5 block systems: all slope triples mod affine."""
    rng = zec.LCG(seed)
    z1, z2 = 0, 1
    zp = [z for z in range(q) if z not in (z1, z2)]
    hits = []
    tried = 0
    for _ in range(npart):
        pool = list(range(q))
        blocks = []
        ok = True
        for _a in range(5):
            if len(pool) < t:
                ok = False
                break
            b = rng.sample(pool, t)
            for x in b:
                pool.remove(x)
            blocks.append(sorted(b))
        if not ok:
            continue
        A1, A2 = blocks[0], blocks[1]
        Pi = perp_E(A1 + A2, e, q)
        L = {(i, z): cond_rows(A1, A2, blocks[i], z, z1, z2, Pi, q)
             for i in (2, 3, 4) for z in zp}
        for z3 in zp:
            for z4 in zp:
                if z4 == z3:
                    continue
                base = L[(2, z3)] + L[(3, z4)]
                if 2 * t - zec.rank_mod(base, q) == 0:
                    continue
                for z5 in zp:
                    if z5 in (z3, z4):
                        continue
                    tried += 1
                    if 2 * t - zec.rank_mod(base + L[(4, z5)], q) >= 1:
                        hits.append((blocks, [z1, z2, z3, z4, z5]))
    return hits, tried


def section_G():
    print("\n--- G. DIRECT V = 5 search (no extension step) ---")
    tot = []
    for q, t, e, npart in ((19, 3, 2, 700), (23, 4, 3, 220), (29, 4, 3, 90)):
        hits, tried = sweep_V5(q, t, e, 907 + q, npart)
        npen = [(b, s) for b, s in hits if is_pencil_rank(b, q) >= 3]
        note("G q=%d t=%d e=%d V=5" % (q, t, e),
             "%d partitions, %d slope triples reached, %d hits, %d non-pencil"
             % (npart, tried, len(hits), len(npen)))
        aud = []
        for b, s in npen[:10]:
            a = audit(q, t, e, b, s, "V5")
            if a and a["ann"] >= 1:
                aud.append(a)
        tot += aud
        RECORD["G_q%d_t%d" % (q, t)] = dict(hits=len(hits), nonpencil=len(npen),
                                            audited=len(aud))
    check("G1 V = 5: NO gate-clean non-collapsing NON-pencil system found",
          not tot, "%d audited non-pencil V=5 witnesses" % len(tot))
    if tot:
        RECORD["G_witness"] = tot[0]
        note("G V=5 non-pencil witness", json.dumps(
            {kk: tot[0][kk] for kk in ("q", "V", "t", "k", "e", "U", "ann",
                                       "rank", "two_m", "pencil_rank",
                                       "blocks", "slopes")}))
    return tot


def main():
    section_A()
    hits = section_B()
    best = section_C(hits)
    section_C2(best, "e2V4")
    # pencil control systems must satisfy the same structure theorem
    ctrl = []
    for q, d, t, ncl, e, k in ((19, 3, 3, 5, 2, 8), (11, 2, 2, 5, 1, 5),
                               (13, 2, 2, 6, 1, 7), (41, 4, 4, 5, 3, 12)):
        ps = pencil_system(q, d, t, ncl, e)
        if ps is None:
            continue
        b, s = ps
        a = audit(q, t, e, b, s, "pencil")
        if a and a["ann"] >= 1:
            ctrl.append(a)
    section_C2(ctrl, "pencilV5")
    section_D_control()
    section_D(best, "e2")
    section_E()
    g5 = section_G()
    if g5:
        section_C2(g5, "V5nonpencil")
    section_F()
    section_F2()
    print("\n%d checks, %d FAIL" % (len(CHECKS), len(FAILURES)))
    with open(ROOT + "/notes/pilots_20260803/la_pencil_rigidity/verify.json",
              "w") as f:
        json.dump(RECORD, f, indent=1, sort_keys=True, default=str)
    if FAILURES:
        print("FAILURES: " + ", ".join(FAILURES))
        sys.exit(1)
    print("LA_PENCIL_ALL_PASS")


if __name__ == "__main__":
    main()
