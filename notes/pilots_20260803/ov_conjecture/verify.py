#!/usr/bin/env python3
"""CONJECTURE OV -- machine verification.

Run:  tools/ramguard tiny -- python3 notes/pilots_20260803/ov_conjecture/verify.py

Reuses, read-only:
  notes/pilots_20260803/zero_escape_collapse/verify.py   (zec: ann_dim, rank_row, ...)
  notes/pilots_20260803/overlap_sliver/verify.py         (osl: analyse, gates, pg2, MINWIT)
"""
from __future__ import annotations

import importlib.util
import json
import sys
from itertools import combinations

ROOT = "/home/u2470931/smooth-read-solomin/prize"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


import io
import contextlib

_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    zec = _load("zec", ROOT + "/notes/pilots_20260803/zero_escape_collapse/verify.py")
    osl = _load("osl", ROOT + "/notes/pilots_20260803/overlap_sliver/verify.py")

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


# ------------------------------------------------------------------ polys
def polymul(a, b, q):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % q
    return out


def poly_from_roots(roots, q):
    p = [1]
    for r in roots:
        p = polymul(p, [(-r) % q, 1], q)
    return p


# --------------------------------------------------------- the W-model
def syn(xs, q, m):
    """e_x -> omega_x * (1, x, ..., x^{m-1}); kernel of v -> sum v_x e_x is RS_k|_U."""
    n = len(xs)
    out = []
    for i, x in enumerate(xs):
        den = 1
        for j, y in enumerate(xs):
            if j != i:
                den = den * (x - y) % q
        w = zec.inv(den, q)
        out.append([w * pow(x, j, q) % q for j in range(m)])
    return out


def span_dim(idx, xs, q, m):
    S = syn(xs, q, m)
    return zec.rank_mod([S[i] for i in idx], q)


def blocks_to_supports(blocks, n_U):
    full = set(range(n_U))
    return [sorted(full - set(b)) for b in blocks]


def j_rows(blocks, xs, k, q):
    """Rows spanning J = sum_{a<b} L_ab * F[X]_{<d_ab} inside F[X]_{<m}."""
    n_U = len(xs)
    m = n_U - k
    rows = []
    for a, b in combinations(range(len(blocks)), 2):
        B = sorted(set(blocks[a]) | set(blocks[b]))
        dd = m - len(B)
        if dd <= 0:                     # pair union not MDS-independent
            return None
        L = poly_from_roots([xs[i] for i in B], q)
        for j in range(dd):
            r = [0] * m
            for e, c in enumerate(L):
                r[e + j] = c % q
            rows.append(r)
    return rows


def jperp_dim(blocks, xs, k, q):
    """dim of Jperp = intersection over pairs of (W_a + W_b)."""
    m = len(xs) - k
    rows = j_rows(blocks, xs, k, q)
    if rows is None:
        return None
    return m - zec.rank_mod(rows, q)


def jperp_dim_direct(blocks, xs, k, q):
    """Same quantity computed from the syndrome model (independent route)."""
    n_U = len(xs)
    m = n_U - k
    S = syn(xs, q, m)
    rows = []
    for a, b in combinations(range(len(blocks)), 2):
        B = sorted(set(blocks[a]) | set(blocks[b]))
        perp = zec.nullspace_mod([S[i] for i in B], m, q)
        rows.extend(perp)
    if not rows:
        return m
    return m - zec.rank_mod(rows, q)


def flat_space_dim(blocks, xs, k, q):
    """dim {v in F^U : v|_{I_ab} in RS_k|_{I_ab} for every pair} - k   (THEOREM 3)."""
    n_U = len(xs)
    full = set(range(n_U))
    rows = []
    for a, b in combinations(range(len(blocks)), 2):
        I = sorted(full - (set(blocks[a]) | set(blocks[b])))
        rows.extend(zec.dual_basis(tuple(I), xs, k, q))
    return len(zec.nullspace_mod(rows, n_U, q)) - k


def ann_of(blocks, slopes, xs, k, q):
    n_U = len(xs)
    sup = blocks_to_supports(blocks, n_U)
    return zec.ann_dim(sup, slopes, xs, k, q, set(range(n_U)))


def facts(blocks, n_U, h):
    return osl.analyse([frozenset(b) for b in blocks], n_U, h)


def gate_clean(blocks, n_U, h, strict=True):
    F = facts(blocks, n_U, h)
    return (F is not None) and osl.gates(F, strict_depth=strict), F


# ============================================================ section A
def section_A():
    """(D1)-(D5): the gate <-> MDS dictionary."""
    print("\n--- A. the gate <-> MDS dictionary (OV3) ---")
    bank = []

    # PG(2,3) as a block system on 13 points, h = 4
    pts, lines = osl.pg2(3)
    bank.append(("PG(2,3)", [sorted(L) for L in lines], 13, 4))
    # the sliver's frozen minimal witness
    MW = osl.MINWIT
    bank.append(("MINWIT", [sorted(b) for b in MW["blocks"]], MW["n_U"], MW["h"]))

    q = 17
    ok_d1 = ok_d2 = ok_d3 = ok_d4 = ok_d5 = True
    det = []
    for name, blocks, n_U, h in bank:
        F = facts(blocks, n_U, h)
        k, t, V = F["k"], F["t"], F["V"]
        m = h + t
        assert n_U - k == m, (name, n_U, k, m)
        xs = list(range(1, n_U + 1))
        S = syn(xs, q, m)
        # D1
        for a, b in combinations(range(V), 2):
            un = set(blocks[a]) | set(blocks[b])
            d_ab = F["d"][(a, b)]
            if len(un) != m - d_ab:
                ok_d1 = False
            if len(un) > m - 1:
                ok_d1 = False
            if zec.rank_mod([S[i] for i in un], q) != len(un):
                ok_d1 = False
            if zec.rank_mod([S[i] for i in un], q) != m - d_ab:
                ok_d5 = False
            # D4
            inter = set(blocks[a]) & set(blocks[b])
            Wa = [S[i] for i in blocks[a]]
            Wb = [S[i] for i in blocks[b]]
            di = len(Wa) + len(Wb) - zec.rank_mod(Wa + Wb, q)
            if di != len(inter):
                ok_d4 = False
        # D2
        for a, b, c in combinations(range(V), 3):
            un = set(blocks[a]) | set(blocks[b]) | set(blocks[c])
            if len(un) < m + 1:
                ok_d2 = False
        # D3
        common = None
        for a, b in combinations(range(V), 2):
            u = set(blocks[a]) | set(blocks[b])
            common = u if common is None else (common & u)
        if common:
            ok_d3 = False
        det.append("%s V=%d t=%d h=%d k=%d m=%d" % (name, V, t, h, k, m))

    check("A1 (D1) pair union = m-d <= m-1 and MDS-independent", ok_d1, "; ".join(det))
    check("A2 (D2) gate (T) <=> every triple union >= m+1", ok_d2)
    check("A3 (D3) zero escape => cap over pairs of (A_a u A_b) empty", ok_d3)
    check("A4 (D4) dim(W_a ^ W_b) = w_ab", ok_d4)
    check("A5 (D5) dim(W_a + W_b) = m - d", ok_d5)

    # J built from L_ab agrees with the syndrome-perp construction
    agree = True
    for name, blocks, n_U, h in bank:
        F = facts(blocks, n_U, h)
        k = F["k"]
        xs = list(range(1, n_U + 1))
        if jperp_dim(blocks, xs, k, q) != jperp_dim_direct(blocks, xs, k, q):
            agree = False
    check("A6 (D5) L_ab*F[X]_{<d} construction = syndrome-perp construction", agree)

    # A7: THEOREM 3 -- Jperp = {v k-flat on every I_ab} / RS_k, computed directly
    ok7, det7 = True, []
    for name, blocks, n_U, h in bank:
        F = facts(blocks, n_U, h)
        k = F["k"]
        for qq in (17, 23):
            xs = list(range(1, n_U + 1))
            got = flat_space_dim(blocks, xs, k, qq)
            want = jperp_dim(blocks, xs, k, qq)
            det7.append("%s q=%d flat=%d Jperp=%d" % (name, qq, got, want))
            if got != want:
                ok7 = False
    check("A7 (THM 3) Jperp = {v k-flat on every I_ab}/RS_k", ok7, "; ".join(det7))
    RECORD["A"] = det + det7


# ============================================================ section B
def X_fixtures():
    """The banked DISJOINT non-collapsing fixtures X1/X2/X3 (zero_escape_collapse 5.1)."""
    out = []
    for tag, q, k, tdeg in (("X1", 17, 3, 2), ("X2", 17, 5, 4), ("X3", 13, 5, 3)):
        # the fibre constants must be tdeg-th powers with full fibres
        cs = [c for c in range(1, q)
              if sum(1 for x in range(1, q) if pow(x, tdeg, q) == c) == tdeg]
        fix = None
        for quad in combinations(cs, 4):
            fix = zec.pencil_fixture(q, k, tdeg, quad)
            if fix is not None:
                break
        if fix is None:
            note("B fixture %s unavailable" % tag, "no admissible fibre quadruple")
            continue
        out.append((tag, q, k, fix))
    return out


def section_B():
    """OV4: containment sanity -- Ann != 0 (non-degenerate) forces dim Jperp >= 2."""
    print("\n--- B. containment sanity: Ann != 0 => dim Jperp >= 2 (OV4) ---")
    got = []
    ok = True
    for tag, q, k, fix in X_fixtures():
        xs, sup, slopes = fix["xs"], fix["supports"], fix["slopes"]
        n_U = len(xs)
        blocks = [sorted(set(range(n_U)) - set(S)) for S in sup]
        da = zec.ann_dim(sup, slopes, xs, k, q, set(range(n_U)))
        jp = jperp_dim(blocks, xs, k, q)
        got.append("%s dimAnn=%d dimJperp=%s m=%d" % (tag, da, jp, n_U - k))
        if da >= 1 and (jp is None or jp < 2):
            ok = False
    check("B1 X1/X2/X3: dim Ann >= 1 and dim Jperp >= 2", ok, "; ".join(got))
    RECORD["B"] = got


# ============================================================ section C
def section_C():
    """OV5: PG(2,3) (and PG(2,5)) -- the extremal overlapping case."""
    print("\n--- C. PG(2,r): the extremal overlapping case (OV5) ---")
    res = []
    ok = True
    for r, qs in ((3, (13, 17, 19, 23, 25 if False else 29)),):
        pts, lines = osl.pg2(r)
        blocks = [sorted(L) for L in lines]
        n_U = len(pts)
        h = r + 1
        F = facts(blocks, n_U, h)
        k = F["k"]
        gc = osl.gates(F, strict_depth=True)
        check("C0 PG(2,%d) gate-clean, overlapping, zero escape" % r,
              gc and F["lam"] == 1 and max(F["mult"]) <= F["V"] - 3,
              "V=%d t=%d h=%d k=%d lam=%s maxmult=%d" %
              (F["V"], F["t"], h, k, F["lam"], max(F["mult"])))
        for q in qs:
            if q <= n_U:
                continue
            for tag, xs in point_sets(q, n_U):
                if xs is None:
                    continue
                jp = jperp_dim(blocks, xs, k, q)
                res.append("PG(2,%d) q=%d %s dimJperp=%s" % (r, q, tag, jp))
                if jp is None or jp >= 2:
                    ok = False
    check("C1 PG(2,3): dim Jperp <= 1 on every point set tried", ok)
    for line in res:
        note("C", line)
    RECORD["C"] = res


def point_sets(q, n_U, cap=6):
    """A few structurally different evaluation-point sets of size n_U in F_q."""
    out = []
    if n_U > q:
        return out
    out.append(("consecutive", list(range(n_U))))
    if n_U <= q - 1:
        out.append(("shifted", list(range(1, n_U + 1))))
    # geometric progression (multiplicative)
    for g in range(2, min(q, 8)):
        pw, seen, x = [], set(), 1
        for _ in range(n_U):
            if x in seen:
                break
            seen.add(x)
            pw.append(x)
            x = x * g % q
        if len(pw) == n_U:
            out.append(("geom g=%d" % g, pw))
            break
    # squares / fibre-flavoured set
    sq = sorted({pow(i, 2, q) for i in range(1, q)})
    if len(sq) >= n_U:
        out.append(("squares", sq[:n_U]))
    # a pseudo-random set
    rng = zec.LCG(9090 + q)
    pool = list(range(q))
    pick = []
    for _ in range(n_U):
        pick.append(pool.pop(rng.randint(0, len(pool) - 1)))
    out.append(("random", pick))
    return out[:cap]


# ============================================================ section D
def section_D():
    """OV8: the frozen minimal witness MINWIT must replay through every claim."""
    print("\n--- D. MINWIT replay (OV8) ---")
    MW = osl.MINWIT
    blocks = [sorted(b) for b in MW["blocks"]]
    n_U, h = MW["n_U"], MW["h"]
    F = facts(blocks, n_U, h)
    k = F["k"]
    gc = osl.gates(F, strict_depth=True)
    check("D0 MINWIT gate-clean overlapping zero-escape",
          gc and F["lam"] is not None and F["lam"] >= 1,
          "V=%d t=%d h=%d k=%d n_U=%d lam=%s maxmult=%d m=%d" %
          (F["V"], F["t"], h, k, n_U, F["lam"], max(F["mult"]), h + F["t"]))
    res, ok = [], True
    for q in (13, 17, 19, 23):
        for tag, xs in point_sets(q, n_U):
            jp = jperp_dim(blocks, xs, k, q)
            res.append("q=%d %s dimJperp=%s" % (q, tag, jp))
            if jp is None or jp >= 2:
                ok = False
    check("D1 MINWIT: dim Jperp <= 1 on every point set tried", ok)
    for line in res:
        note("D", line)
    RECORD["D"] = res


# ============================================================ section E
def rand_design(rng, n_U, t, h, V=None, tries=1):
    """Gate-clean zero-escape block system, grown with the sliver's own generator."""
    cands = [frozenset(c) for c in combinations(range(n_U), t)]
    for _ in range(tries):
        fam = osl.grow(cands, t, h, n_U, rng, cap=40)
        fam = osl.zero_escape_trim(fam, n_U)
        if not fam or len(fam) < 5:
            continue
        blocks = [sorted(b) for b in fam]
        F = facts(blocks, n_U, h)
        if F is None or not osl.gates(F, strict_depth=True):
            continue
        return blocks, F
    return None, None


def scan_design(blocks, k, qs=(29, 31, 37, 41)):
    """Max dim Jperp over a spread of point sets / fields."""
    n_U = len(set().union(*[set(b) for b in blocks]))
    n_U = max(max(b) for b in blocks) + 1
    best, where = 0, ""
    for q in qs:
        for tag, xs in point_sets(q, n_U):
            jp = jperp_dim(blocks, xs, k, q)
            if jp is not None and jp > best:
                best, where = jp, "q=%d %s" % (q, tag)
    return best, where


def section_E(rounds=90):
    """OV2 / OV1: random overlapping gate-clean zero-escape systems."""
    print("\n--- E. random overlapping gate-clean zero-escape systems (OV2) ---")
    rng = zec.LCG(20260803)
    shapes = []
    for n_U in (9, 10, 11, 12, 13, 14):
        for t in (3, 4, 5):
            for h in (3, 4, 5, 6):
                if n_U - h - t >= 2 and t - h + 1 <= t - 2:
                    shapes.append((n_U, t, h))
    shapes = sorted(set(shapes))
    found = []
    worst = 0
    nover = ndisj = 0
    sigma_alive = []
    for rd in range(rounds):
        n_U, t, h = shapes[rd % len(shapes)]
        blocks, F = rand_design(rng, n_U, t, h)
        if blocks is None:
            continue
        maxw = max(F["w"].values())
        if maxw >= 1:
            nover += 1
        else:
            ndisj += 1
            continue
        jp, where = scan_design(blocks, F["k"])
        worst = max(worst, jp)
        if jp >= 1:
            found.append((blocks, n_U, h, F["k"], jp, where, F["lam"], maxw))
        # route-1 sigma test on the same system
        basis = sigma_system(blocks, n_U, 101)
        if not forced_collisions(basis, n_U):
            sigma_alive.append((blocks, n_U, h, F["k"]))
    note("E sigma", "overlapping systems whose e_1 mechanism stays alive: %d / %d"
         % (len(sigma_alive), nover))
    RECORD["E_sigma_alive"] = [(b, n, h, k) for b, n, h, k in sigma_alive[:5]]
    check("E1 overlapping gate-clean zero-escape: dim Jperp <= 1 always",
          worst <= 1, "systems=%d  max dim Jperp=%d" % (nover, worst))
    check("E2 overlapping gate-clean zero-escape: dim Jperp = 0 always",
          worst == 0, "%d hits with dim Jperp >= 1" % len(found))
    note("E", "overlapping systems scanned=%d (disjoint skipped=%d)" % (nover, ndisj))
    RECORD["E"] = dict(n=nover, worst=worst,
                       hits=[(b, n, h, k, j, w) for b, n, h, k, j, w, _, _ in found[:5]])
    return found


# ============================================================ section F
def sigma_system(blocks, n_U, q):
    """Linear system  sum_{x in A_a u A_b} x = C  over F_q; unknowns x_0..x_{n-1}, C.

    Solutions of this system are exactly the point sets admitting the
    r = d 'M_I' mechanism's NECESSARY condition e_1(I_ab) = const.
    Returns a basis of the solution space in the x-coordinates.
    """
    V = len(blocks)
    rows = []
    for a, b in combinations(range(V), 2):
        r = [0] * (n_U + 1)
        for x in set(blocks[a]) | set(blocks[b]):
            r[x] = 1
        r[n_U] = q - 1                      # -C
        rows.append(r)
    return zec.nullspace_mod(rows, n_U + 1, q)


def forced_collisions(basis, n_U):
    """Pairs (i,j) whose coordinates agree on the WHOLE solution space."""
    out = []
    for i, j in combinations(range(n_U), 2):
        if all(v[i] == v[j] for v in basis):
            out.append((i, j))
    return out


def section_F():
    """Route 1: the shared-point forcing, tested exactly on the e_1 mechanism."""
    print("\n--- F. the sigma / shared-point forcing (route 1, r = d branch) ---")
    q = 101
    cases = []
    pts, lines = osl.pg2(3)
    cases.append(("PG(2,3)", [sorted(L) for L in lines], 13, 4))
    MW = osl.MINWIT
    cases.append(("MINWIT", [sorted(b) for b in MW["blocks"]], MW["n_U"], MW["h"]))
    # a disjoint control: X1's four blocks of size 2 on 8 points
    cases.append(("X1-shape (DISJOINT control)",
                  [[0, 1], [2, 3], [4, 5], [6, 7]], 8, 3))

    ok = True
    det = []
    for name, blocks, n_U, h in cases:
        basis = sigma_system(blocks, n_U, q)
        col = forced_collisions(basis, n_U)
        # is there a solution with all coordinates distinct?
        alive = (len(col) == 0)
        det.append("%s: soln dim=%d forced-collisions=%d distinct-solution=%s"
                   % (name, len(basis), len(col), alive))
        if name.startswith("PG") or name.startswith("MINWIT"):
            if alive:
                ok = False
    check("F1 overlapping designs: the e_1 (r=d) mechanism is DEAD "
          "(every solution has repeated points)", ok, "; ".join(det))

    # F2: not a characteristic artifact -- replay over a spread of primes
    ok2, det2 = True, []
    for qq in (7, 11, 13, 19, 101, 1009, 10007):
        for name, blocks, n_U, h in cases:
            basis = sigma_system(blocks, n_U, qq)
            alive = not forced_collisions(basis, n_U)
            if name.startswith("X1-shape"):
                if not alive:
                    det2.append("q=%d DISJOINT control unexpectedly dead" % qq)
                continue
            if alive:
                ok2 = False
                det2.append("q=%d %s ALIVE" % (qq, name))
    check("F2 the e_1 mechanism is dead in every characteristic tried "
          "(and the disjoint control stays alive)", ok2,
          "primes 7..10007; anomalies: %s" % ("; ".join(det2) or "none"))

    # F3: the uniform-multiplicity lemma's hypotheses at PG(2,3)
    pts, lines = osl.pg2(3)
    blocks = [sorted(L) for L in lines]
    F = facts(blocks, 13, 4)
    mult = set(F["mult"])
    check("F3 PG(2,3) has uniform block multiplicity mu with V-1-mu != 0",
          len(mult) == 1 and (F["V"] - 1 - mult.copy().pop()) != 0,
          "mult set=%s V=%d V-1-mu=%d" % (sorted(mult), F["V"],
                                          F["V"] - 1 - sorted(mult)[0]))
    RECORD["F"] = det


# ============================================================ section G
def section_G():
    """OV7: the degenerate branch dim P <= 1 is killed by zero escape."""
    print("\n--- G. degenerate branch: cap over any V-1 blocks of W_a is 0 (OV7) ---")
    q = 37
    cases = []
    pts, lines = osl.pg2(3)
    cases.append(("PG(2,3)", [sorted(L) for L in lines], 13, 4))
    MW = osl.MINWIT
    cases.append(("MINWIT", [sorted(b) for b in MW["blocks"]], MW["n_U"], MW["h"]))
    ok = True
    det = []
    for name, blocks, n_U, h in cases:
        F = facts(blocks, n_U, h)
        k, V = F["k"], F["V"]
        m = n_U - k
        xs = list(range(1, n_U + 1))
        S = syn(xs, q, m)
        worst = 0
        for drop in range(V):
            idx = [a for a in range(V) if a != drop]
            rows = []
            for a in idx:
                rows.extend(zec.nullspace_mod([S[i] for i in blocks[a]], m, q))
            worst = max(worst, m - zec.rank_mod(rows, q))
        det.append("%s: max dim cap_{a != drop} W_a = %d" % (name, worst))
        if worst != 0:
            ok = False
    check("G1 cap over any V-1 of the W_a is 0 (zero escape)", ok, "; ".join(det))
    RECORD["G"] = det


# ============================================================ section H
def rand_points(rng, q, n_U):
    pool = list(range(q))
    return [pool.pop(rng.randint(0, len(pool) - 1)) for _ in range(n_U)]


def sweep_points(blocks, k, rng, qs, tries):
    """Max dim Jperp over random point sets AND random point<->index assignments."""
    n_U = max(max(b) for b in blocks) + 1
    best, where = 0, ""
    for q in qs:
        if q <= n_U:
            continue
        for _ in range(tries):
            xs = rand_points(rng, q, n_U)
            jp = jperp_dim(blocks, xs, k, q)
            if jp is not None and jp > best:
                best, where = jp, "q=%d xs=%s" % (q, xs)
    return best, where


def section_H(tries=120):
    """OV2 adversarial: many point sets / assignments; lam >= 2; OV1 slope replay."""
    print("\n--- H. adversarial point-set sweep + lam >= 2 + Ann replay (OV1/OV2/OV6) ---")
    rng = zec.LCG(778899)
    qs = (17, 19, 23, 29, 31, 37, 41)

    cases = []
    pts, lines = osl.pg2(3)
    cases.append(("PG(2,3) lam=1", [sorted(L) for L in lines], 13, 4))
    MW = osl.MINWIT
    cases.append(("MINWIT lam=1", [sorted(b) for b in MW["blocks"]], MW["n_U"], MW["h"]))

    # grow overlapping designs, keeping the lam >= 2 ones apart
    lam1, lam2 = [], []
    for n_U in (10, 11, 12, 13, 14, 15):
        for t in (4, 5, 6):
            for h in (3, 4, 5):
                if n_U - h - t < 2 or t - h + 1 > t - 2:
                    continue
                for _ in range(6):
                    blocks, F = rand_design(rng, n_U, t, h)
                    if blocks is None:
                        continue
                    minw = min(F["w"].values())
                    if minw >= 2:
                        lam2.append((blocks, n_U, h, F))
                    elif minw >= 1:
                        lam1.append((blocks, n_U, h, F))
    for i, (b, n, h, F) in enumerate(lam1[:6]):
        cases.append(("grown lam>=1 #%d" % i, b, n, h))
    for i, (b, n, h, F) in enumerate(lam2[:6]):
        cases.append(("grown lam>=2 #%d" % i, b, n, h))

    worst, det, hits = 0, [], []
    for name, blocks, n_U, h in cases:
        F = facts(blocks, n_U, h)
        k = F["k"]
        best, where = sweep_points(blocks, k, rng, qs, tries)
        worst = max(worst, best)
        det.append("%s V=%d t=%d h=%d k=%d minw=%d maxJperp=%d"
                   % (name, F["V"], F["t"], h, k, min(F["w"].values()), best))
        if best >= 1:
            hits.append((name, blocks, k, where))
    check("H1 OV2: dim Jperp = 0 on every overlapping system x point set",
          worst == 0, "%d systems, %d point sets each" % (len(cases), tries * len(qs)))
    check("H2 OV6: lam >= 2 overlapping systems behave like lam = 1",
          len(lam2) > 0 and worst == 0,
          "lam>=2 systems grown: %d" % len(lam2))
    for line in det:
        note("H", line)

    # OV1 direct replay: dim Ann over random slope tuples
    ann_bad = []
    ntup = 0
    for name, blocks, n_U, h in cases[:4]:
        F = facts(blocks, n_U, h)
        k = F["k"]
        for q in (17, 19, 23):
            if q <= n_U:
                continue
            for _ in range(12):
                xs = rand_points(rng, q, n_U)
                z = rand_points(rng, q, F["V"])
                da = ann_of(blocks, z, xs, k, q)
                ntup += 1
                if da != 0:
                    ann_bad.append((name, q, xs, z, da))
    check("H3 OV1: dim Ann = 0 on every overlapping tuple replayed",
          not ann_bad, "%d (point set, slope tuple) pairs" % ntup)
    RECORD["H"] = det
    RECORD["H_hits"] = [(n, w) for n, _, _, w in hits]

    # H4: EXHAUSTIVE-modulo-affine slope sweep on an OVERLAPPING system.
    # (The sibling pilot's exhaustive sweeps were all on DISJOINT fixtures.)
    MWb = [sorted(b) for b in osl.MINWIT["blocks"]]
    n_U, h = osl.MINWIT["n_U"], osl.MINWIT["h"]
    k = facts(MWb, n_U, h)["k"]
    q = 13
    xs = list(range(q))            # U = all of F_13 is too big; take n_U points
    xs = list(range(1, n_U + 1))
    bad, ntot = 0, 0
    rest = [z for z in range(q) if z not in (0, 1)]
    for i3 in rest:
        for i4 in rest:
            if i4 == i3:
                continue
            for i5 in rest:
                if i5 in (i3, i4):
                    continue
                for i6 in rest:
                    if i6 in (i3, i4, i5):
                        continue
                    ntot += 1
                    if ann_of(MWb, [0, 1, i3, i4, i5, i6], xs, k, q) != 0:
                        bad += 1
    check("H4 OV1: MINWIT exhaustive-mod-affine slope sweep, dim Ann = 0 always",
          bad == 0, "q=%d, %d slope tuples (z1=0,z2=1 fixed), %d non-collapsing"
          % (q, ntot, bad))


def main():
    section_A()
    section_B()
    section_C()
    section_D()
    section_E(rounds=260)
    section_F()
    section_G()
    section_H()
    print("\n%d checks, %d FAIL" % (len(CHECKS), len(FAILURES)))
    if FAILURES:
        print("FAILURES: " + ", ".join(FAILURES))
    with open(ROOT + "/notes/pilots_20260803/ov_conjecture/verify.json", "w") as fh:
        json.dump({"checks": CHECKS, "failures": FAILURES, "record": RECORD}, fh, indent=1)
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
