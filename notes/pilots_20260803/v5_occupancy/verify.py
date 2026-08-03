#!/usr/bin/env python3
r"""Verifier for the V >= 5 zero-escape occupancy pilot (2026-08-03).

PROFILE: tiny.  Run from the repo root:
    tools/ramguard tiny -- python3 \
        notes/pilots_20260803/v5_occupancy/verify.py

Pure python integers, deterministic, no third-party imports.  Files read
outside this directory (READ-ONLY, never written):
  * notes/pilots_20260803/zero_escape_collapse/verify.py   (machinery:
    rref/rank/nullspace, dual_basis, row_cols, rank_row, ann_space,
    ann_dim, interpolate, cross_ratio)  -- reuse, do not copy;
  * notes/pilots_20260802/support4_relation/stage5_escape.json  (the
    record's escape-clique rows, for section H).

CLASS OF RECORD (the pilot's question).  A zero-escape BLOCK system
B(V,t,t_0,k):  U = A_0 |_| A_1 |_| ... |_| A_V disjoint, |A_0| = t_0,
|A_a| = t, S_a = U \ A_a, slopes z_a distinct.  Then
  |U| = t_0 + Vt,  A = |S_a| = t_0 + (V-1)t,  h = A - k,  m = |U| - k,
  sigma = |S_a^S_b^S_c| = t_0 + (V-3)t,  e = k - sigma,
and the identities m = t + h, e = 2t - h, 2m - 3h = e.  Gates:
zero escape automatic (V >= 4); pairwise >= k+1  <=>  h >= t+1;
gate (T) sigma <= k-1  <=>  h <= 2t-1  <=>  e >= 1.

SECTIONS
  A  class arithmetic (Q9)
  B  reformulation lemma rank = dim span{(B_a X^i, z_a B_a X^i)} (Q7)
     cross-checked against the banked brute-force rank_row, and
     rank + dim Ann = 2m (banked THEOREM 1)
  C  fixtures Y1, Y2, Y2b, Y3, Y3', Y4 -- gates + ranks (Q1, Q2, Q4, Q5)
  D  explicit annihilator CERTIFICATE at Y1/Y4 (the V >= 5 construction)
  E  exact slope locus = the Mobius orbit, exhaustive sweep (Q3)
  F  Y5/Y6: the RowC 1/4 clique's OWN recorded shape (Q6)
  G  retro-explanation of the banked X1/X2/X3 deficits (Q8)
  H  the record's clique model = this class; the k <= 2h^2 criterion
     refuted; the corrected criterion 2V <= 3h at all six rows (Q11,Q12)
  I  V = 5 general (non-block) zero escape: m <= 3h - 4 (Q10)
"""
from __future__ import annotations

import importlib.util
import json
import sys
from itertools import combinations

sys.dont_write_bytecode = True

ROOT = "/home/u2470931/smooth-read-solomin/prize"
ZEC = ROOT + "/notes/pilots_20260803/zero_escape_collapse/verify.py"
STAGE5 = ROOT + "/notes/pilots_20260802/support4_relation/stage5_escape.json"

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


# ------------------------------------------------------------ ray systems
def build_system(blocks, A0):
    """pts (sorted field elements), supports (index tuples into pts)."""
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


def gates(pts, supports, k, full=True, sample=None):
    """Combinatorial gate report.  full=False -> triples/quads by sample."""
    V = len(supports)
    n = len(pts)
    sets = [set(S) for S in supports]
    A = len(sets[0])
    same_size = all(len(s) == A for s in sets)
    mult = [sum(1 for s in sets if i in s) for i in range(n)]
    pair = min(len(sets[a] & sets[b]) for a, b in combinations(range(V), 2))
    if full:
        trip = max(len(sets[a] & sets[b] & sets[c])
                   for a, b, c in combinations(range(V), 3))
        quad = (max(len(sets[a] & sets[b] & sets[c] & sets[d])
                    for a, b, c, d in combinations(range(V), 4))
                if V >= 4 else 0)
    else:
        trip = max(len(sets[a] & sets[b] & sets[c]) for a, b, c in sample)
        quad = 0
    return dict(V=V, n=n, A=A, same_size=same_size, minmult=min(mult),
                pair=pair, trip=trip, quad=quad, h=A - k, m=n - k)


# ------------------------------------------------- the reformulation lemma
def rank_poly(blocks, slopes, q, m, h):
    """dim span{(B_a X^i, z_a B_a X^i)} in F[X]_{<m}^2, B_a = prod (X-x)."""
    gens = []
    for blk, z in zip(blocks, slopes):
        B = poly_from_roots(blk, q)
        assert len(B) + h - 1 <= m, "degree overflow in reformulation"
        for i in range(h):
            v = [0] * m
            for j, cf in enumerate(B):
                v[i + j] = cf
            gens.append(v + [z * x % q for x in v])
    return zec.rank_mod(gens, q)


def is_pencil(blocks, q):
    """True iff all B_a lie in one 2-dim space (blocks = fibres of a pencil)."""
    rows = [poly_from_roots(b, q) for b in blocks]
    return zec.rank_mod(rows, q) == 2


def pencil_params(blocks, q):
    """Affine pencil parameters c_a with c_0 = 0, c_1 = 1 (None if no pencil)."""
    Bs = [poly_from_roots(b, q) for b in blocks]
    v = [(Bs[1][i] - Bs[0][i]) % q for i in range(len(Bs[0]))]
    piv = next((i for i, x in enumerate(v) if x), None)
    if piv is None:
        return None
    out = []
    for B in Bs:
        u = [(B[i] - Bs[0][i]) % q for i in range(len(B))]
        c = u[piv] * zec.inv(v[piv], q) % q
        if any((u[i] - c * v[i]) % q for i in range(len(u))):
            return None
        out.append(c)
    return out


def mobius_equiv(cs, zs, q):
    """True iff some psi in PGL_2 has c_a = psi(z_a) for all a."""
    if len(cs) < 4:
        return True
    for a in range(3, len(cs)):
        r1 = zec.cross_ratio(cs[0], cs[1], cs[2], cs[a], q)
        r2 = zec.cross_ratio(zs[0], zs[1], zs[2], zs[a], q)
        if r1 is None or r2 is None or r1 != r2:
            return False
    return True


# ------------------------------------------- the V >= 5 annihilator recipe
def ann_certificate(pts, blocks, A0, slopes, k, q, qpoly):
    """Build (lam, mu) from the construction; return None if the shape fails.

    Normalisation p_0 = p_1 = 0.  For a >= 2:
      p_a = kappa_a * D * prod_{j>=2, j!=a} B_j * qpoly,
      kappa_a fixed by nu(x1) = 1 at one point x1 of block 0.
    Consistency of nu on the REST of blocks 0 and 1 is the real content.
    """
    V = len(blocks)
    z = slopes
    D = poly_from_roots(sorted(A0), q)
    Bs = [poly_from_roots(b, q) for b in blocks]
    x1 = blocks[0][0]

    def base(a, x):
        acc = peval(D, x, q) * peval(qpoly, x, q) % q
        for j in range(2, V):
            if j != a:
                acc = acc * peval(Bs[j], x, q) % q
        return acc

    kappa = {}
    for a in range(2, V):
        b0 = base(a, x1)
        if b0 % q == 0:
            return None
        kappa[a] = (z[a] - z[1]) % q * zec.inv(b0, q) % q

    nu = {}
    for x in blocks[0]:
        vals = {(kappa[a] * base(a, x) % q) * zec.inv((z[a] - z[1]) % q, q) % q
                for a in range(2, V)}
        if len(vals) != 1:
            return None
        nu[x] = vals.pop()
    for x in blocks[1]:
        vals = {(kappa[a] * base(a, x) % q) * zec.inv((z[a] - z[0]) % q, q) % q
                for a in range(2, V)}
        if len(vals) != 1:
            return None
        nu[x] = vals.pop()

    n = len(pts)
    idx = {x: i for i, x in enumerate(pts)}
    lam = [0] * n
    mu = [0] * n
    for x in blocks[0]:
        mu[idx[x]] = nu[x]
        lam[idx[x]] = (-z[1] * nu[x]) % q
    for x in blocks[1]:
        mu[idx[x]] = nu[x]
        lam[idx[x]] = (-z[0] * nu[x]) % q
    if not any(mu):
        return None
    return lam, mu


def annihilates(lam, mu, supports, slopes, pts, k, q):
    """(lam + z_a mu)|_{S_a} in RS_k|_{S_a} for every ray."""
    for S, z in zip(supports, slopes):
        for c in zec.dual_basis(S, pts, k, q):
            s = sum((lam[i] + z * mu[i]) * c[i] for i in range(len(pts))) % q
            if s:
                return False
    return True


def nontrivial(mu, pts, k, q):
    """mu is not the restriction of a poly of degree < k (so the class != 0)."""
    supp = [i for i in range(len(pts)) if mu[i] % q]
    if not supp:
        return False
    zeros = [i for i in range(len(pts)) if not mu[i] % q]
    return len(zeros) >= k


# =========================================================================
def main():
    q_all_ok = True

    # ------------------------------------------------------------ SECTION A
    print("\n--- A. class arithmetic (Q9) ---")
    bad = []
    admissible_with_V_gt_m = 0
    total = 0
    for t in range(2, 13):
        for h in range(t + 1, 2 * t):          # t+1 <= h <= 2t-1
            for t0 in range(0, 13):
                for V in range(4, 41):
                    k = t0 + (V - 1) * t - h
                    if k < 1:
                        continue
                    total += 1
                    U = t0 + V * t
                    m = U - k
                    sigma = t0 + (V - 3) * t
                    e = k - sigma
                    pair = t0 + (V - 2) * t
                    ok = (m == t + h and e == 2 * t - h and e >= 1
                          and 2 * m - 3 * h == e and pair >= k + 1
                          and sigma <= k - 1 and m <= 3 * t - 1
                          and 3 * h <= 2 * m)
                    if not ok:
                        bad.append((t, h, t0, V))
                    if V > m:
                        admissible_with_V_gt_m += 1
    check("A1 identities m=t+h, e=2t-h=2m-3h>=1, gates, m<=3t-1",
          not bad, "%d admissible tuples, %d bad" % (total, len(bad)))
    check("A2 V > m (ceiling regime) is admissible and common",
          admissible_with_V_gt_m > 0,
          "%d of %d admissible tuples have V > m" % (admissible_with_V_gt_m,
                                                     total))
    # the ceiling regime is reachable for EVERY (t,h)
    miss = []
    for t in range(2, 13):
        for h in range(t + 1, 2 * t):
            if not any(V > t + h for V in range(4, 41)):
                miss.append((t, h))
    check("A3 for every (t,h) some admissible V exceeds m = t+h", not miss)
    RECORD["A_admissible_tuples"] = total

    # ------------------------------------------------------- FIXTURE BUILDS
    def fibres(q, d, cs):
        return [sorted(x for x in range(q) if pow(x, d, q) == c % q) for c in cs]

    # Y1 / Y2 / Y2b : q=11, t=2, h=3, V=5, k=5
    q1, k1 = 11, 5
    cs1 = [1, 3, 4, 5, 9]                       # the nonzero squares of F_11
    Y1_blocks = fibres(q1, 2, cs1)
    Y1_slopes = list(cs1)                        # z_a = c_a  (psi = id)
    Y2_slopes = [1, 3, 4, 5, 2]
    Y2b_blocks = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

    # Y3 / Y3' : q=13, t=2, h=3, V=6, k=7
    q3, k3 = 13, 7
    Y3_blocks = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
    Y3_slopes = [1, 2, 3, 4, 5, 6]
    cs3 = sorted({pow(x, 2, q3) for x in range(1, q3)})
    Y3p_blocks = fibres(q3, 2, cs3)
    Y3p_slopes = list(cs3)

    # Y4 : q=41, t=4, h=5, V=10, t_0=1, k=32
    q4, k4 = 41, 32
    cs4 = sorted({pow(x, 4, q4) for x in range(1, q4)})
    Y4_blocks = fibres(q4, 4, cs4)
    Y4_slopes = list(cs4)

    fixtures = [
        ("Y1", q1, k1, Y1_blocks, [], Y1_slopes, 5, 1, 9),
        ("Y2", q1, k1, Y1_blocks, [], Y2_slopes, 5, 0, 10),
        ("Y2b", q1, k1, Y2b_blocks, [], Y1_slopes, 5, 0, 10),
        ("Y3", q3, k3, Y3_blocks, [], Y3_slopes, 5, 0, 10),
        ("Y3'", q3, k3, Y3p_blocks, [], Y3p_slopes, 5, 1, 9),
        ("Y4", q4, k4, Y4_blocks, [0], Y4_slopes, 9, 3, 15),
    ]

    # ------------------------------------------------------------ SECTION B
    print("\n--- B. reformulation lemma + duality (Q7) ---")
    for name, q, k, blocks, A0, slopes, m_p, ann_p, rk_p in fixtures:
        pts, supports = build_system(blocks, A0)
        m = len(pts) - k
        h = len(supports[0]) - k
        r_brute = zec.rank_row(supports, slopes, pts, k, q)
        r_poly = rank_poly(blocks, slopes, q, m, h)
        da = zec.ann_dim(supports, slopes, pts, k, q, set(range(len(pts))))
        check("B[%s] rank_poly == rank_row" % name, r_poly == r_brute,
              "poly %d brute %d" % (r_poly, r_brute))
        check("B[%s] rank + dim Ann == 2m" % name, r_brute + da == 2 * m,
              "rank %d + ann %d = %d, 2m = %d" % (r_brute, da,
                                                  r_brute + da, 2 * m))

    # ------------------------------------------------------------ SECTION C
    print("\n--- C. the fixtures: gates and ranks (Q1, Q2, Q4, Q5) ---")
    for name, q, k, blocks, A0, slopes, m_p, ann_p, rk_p in fixtures:
        pts, supports = build_system(blocks, A0)
        g = gates(pts, supports, k)
        t = len(blocks[0])
        t0 = len(A0)
        V = len(blocks)
        m, h = g["m"], g["h"]
        e = 2 * t - h
        gate_ok = (g["same_size"] and g["minmult"] >= 3
                   and g["pair"] >= k + 1 and g["trip"] <= k - 1
                   and 1 <= g["pair"] - k <= h - 2)
        r = zec.rank_row(supports, slopes, pts, k, q)
        da = zec.ann_dim(supports, slopes, pts, k, q, set(range(len(pts))))
        check("C[%s] gate-clean (zero escape, pairwise>=k+1, (T), band-proper)"
              % name, gate_ok,
              "V=%d t=%d t0=%d |U|=%d A=%d h=%d m=%d e=%d minmult=%d "
              "pair=%d trip=%d quad=%d"
              % (V, t, t0, g["n"], g["A"], h, m, e, g["minmult"],
                 g["pair"], g["trip"], g["quad"]))
        check("C[%s] m, dim Ann, rank as pre-registered" % name,
              (m, da, r) == (m_p, ann_p, rk_p),
              "m=%d dimAnn=%d rank=%d (predicted %d/%d/%d)"
              % (m, da, r, m_p, ann_p, rk_p))
        check("C[%s] floor 3h <= rank <= 2m = ceiling" % name,
              3 * h <= r <= 2 * m, "3h=%d rank=%d 2m=%d" % (3 * h, r, 2 * m))
        note("C[%s] charge = rank/V = %.4f   (2V = %d)" % (name, r / V, 2 * V))
        RECORD[name] = dict(q=q, k=k, V=V, t=t, t0=t0, U=g["n"], A=g["A"],
                            h=h, m=m, e=e, rank=r, dim_ann=da,
                            charge=r / V, two_V=2 * V, three_h=3 * h,
                            two_m=2 * m, pair=g["pair"], trip=g["trip"])

    check("C-Q1 Y1 (V=5) refutes rank >= 2V",
          RECORD["Y1"]["rank"] < RECORD["Y1"]["two_V"],
          "rank 9 < 2V 10, charge 1.8")
    check("C-Q4 Y3 (V=6) refutes rank >= 2V WITH the collapse holding",
          RECORD["Y3"]["rank"] == RECORD["Y3"]["two_m"]
          and RECORD["Y3"]["rank"] < RECORD["Y3"]["two_V"],
          "rank = 2m = 10 < 2V = 12")
    check("C-Q5 Y4 (V=10, RowC invariants t=4,h=5,m=9,e=3) refutes rank >= 2V",
          RECORD["Y4"]["rank"] < RECORD["Y4"]["two_V"]
          and RECORD["Y4"]["two_m"] < RECORD["Y4"]["two_V"],
          "rank 15 < 2m 18 < 2V 20")

    # ------------------------------------------------------------ SECTION D
    print("\n--- D. explicit annihilator certificate (the V>=5 construction) ---")
    for name, q, k, blocks, A0, slopes, m_p, ann_p, rk_p in fixtures:
        if ann_p == 0:
            continue
        pts, supports = build_system(blocks, A0)
        t = len(blocks[0])
        h = len(supports[0]) - k
        e = 2 * t - h
        certs = []
        for i in range(e):
            qp = [0] * i + [1]
            cert = ann_certificate(pts, blocks, A0, slopes, k, q, qp)
            if cert is None:
                break
            lam, mu = cert
            if not annihilates(lam, mu, supports, slopes, pts, k, q):
                break
            if not nontrivial(mu, pts, k, q):
                break
            certs.append(lam + mu)
        indep = zec.rank_mod(certs, q) if certs else 0
        check("D[%s] %d independent explicit annihilators (= e)" % (name, e),
              len(certs) == e and indep == e,
              "built %d, rank %d, e = 2t-h = %d" % (len(certs), indep, e))
    # the certificate must FAIL off the Mobius locus
    pts, supports = build_system(Y1_blocks, [])
    cert = ann_certificate(pts, Y1_blocks, [], Y2_slopes, k1, q1, [1])
    check("D[Y2] the same recipe fails off the Mobius locus", cert is None)

    # ------------------------------------------------------------ SECTION E
    print("\n--- E. exact slope locus = the Mobius orbit (Q3) ---")

    def pairings(items):
        if not items:
            yield []
            return
        a = items[0]
        for j in range(1, len(items)):
            b = items[j]
            rest = items[1:j] + items[j + 1:]
            for p in pairings(rest):
                yield [[a, b]] + p

    pool = list(range(1, q1))
    allp = list(pairings(pool))
    pen = [p for p in allp if is_pencil(p, q1)]
    non = [p for p in allp if not is_pencil(p, q1)]
    note("E pairings of F_11^* into 5 pairs", "%d total, %d pencil, %d not"
         % (len(allp), len(pen), len(non)))
    check("E0 Y1's blocks are a pencil; Y2b's are not",
          is_pencil(Y1_blocks, q1) and not is_pencil(Y2b_blocks, q1))
    swept = []
    chosen = ([Y1_blocks] + [p for p in pen if p != Y1_blocks][:2]
              + [Y2b_blocks] + [p for p in non if p != Y2b_blocks][:2])
    mism = 0
    tot = 0
    hits = 0
    for blocks in chosen:
        pts_s, sup_s = build_system(blocks, [])
        m_s = len(pts_s) - k1
        h_s = len(sup_s[0]) - k1
        cs = pencil_params(blocks, q1)
        loc_pred, loc_obs = set(), set()
        for z2 in range(q1):
            if z2 in (0, 1):
                continue
            for z3 in range(q1):
                if z3 in (0, 1, z2):
                    continue
                for z4 in range(q1):
                    if z4 in (0, 1, z2, z3):
                        continue
                    zs = [0, 1, z2, z3, z4]
                    tot += 1
                    r = rank_poly(blocks, zs, q1, m_s, h_s)
                    obs = (2 * m_s - r) > 0
                    pred = (cs is not None) and mobius_equiv(cs, zs, q1)
                    if obs:
                        loc_obs.add((z2, z3, z4))
                        hits += 1
                    if pred:
                        loc_pred.add((z2, z3, z4))
                    if obs != pred:
                        mism += 1
        swept.append((cs is not None, len(loc_obs), len(loc_pred)))
    check("E1 dim Ann > 0 EXACTLY on the Mobius locus, exhaustive sweep",
          mism == 0,
          "%d slope tuples over 6 pairings, %d with dim Ann > 0, %d mismatches"
          % (tot, hits, mism))
    for i, (isp, nobs, npred) in enumerate(swept):
        note("E1 pairing %d" % i, "pencil=%s  observed locus %d = predicted %d"
             % (isp, nobs, npred))
    check("E2 non-pencil pairings have EMPTY locus over the whole sweep",
          all(nobs == 0 for isp, nobs, npred in swept if not isp))
    check("E3 pencil pairings have NON-EMPTY locus",
          all(nobs > 0 for isp, nobs, npred in swept if isp))

    # ------------------------------------------------------------ SECTION F
    print("\n--- F. the RowC 1/4 clique's own recorded shape (Q6) ---")
    q5, k5, V5 = 269, 256, 66
    cs5 = sorted({pow(x, 4, q5) for x in range(1, q5)})[:V5]
    Y5_blocks = fibres(q5, 4, cs5)
    Y5_A0 = [0]
    Y5_slopes = list(cs5)
    pts5, sup5 = build_system(Y5_blocks, Y5_A0)
    m5 = len(pts5) - k5
    h5 = len(sup5[0]) - k5
    t5 = len(Y5_blocks[0])
    disjoint = all(not (set(a) & set(b))
                   for a, b in combinations(Y5_blocks, 2)) and \
        all(0 not in b for b in Y5_blocks)
    smp = [(0, 1, 2), (0, 1, 65), (3, 30, 64), (10, 20, 30), (1, 2, 3),
           (0, 33, 65), (5, 6, 7), (60, 62, 64)]
    g5 = gates(pts5, sup5, k5, full=False, sample=smp)
    check("F0 Y5 is the recorded RowC 1/4 shape",
          (len(pts5), k5, t5, V5) == (265, 256, 4, 66)
          and (h5, m5) == (5, 9) and g5["A"] == 261 and disjoint,
          "|U|=%d k=%d |A_a|=%d V=%d A=%d h=%d m=%d"
          % (len(pts5), k5, t5, V5, g5["A"], h5, m5))
    check("F1 Y5 gates: zero escape, pairwise = k+1, triples = |U|-3t = 253",
          g5["minmult"] >= 3 and g5["pair"] == k5 + 1 and g5["trip"] == 253
          and g5["trip"] <= k5 - 1,
          "minmult=%d pair=%d trip=%d (k-1=%d)"
          % (g5["minmult"], g5["pair"], g5["trip"], k5 - 1))
    r5 = rank_poly(Y5_blocks, Y5_slopes, q5, m5, h5)
    e5 = 2 * t5 - h5
    check("F2 Y5 rank = 3h = 15 < 2m = 18: the collapse FAILS at RowC's shape",
          r5 == 3 * h5 and 2 * m5 - r5 == e5,
          "rank=%d 3h=%d 2m=%d dimAnn=%d e=%d"
          % (r5, 3 * h5, 2 * m5, 2 * m5 - r5, e5))
    Y6_slopes = list(cs5)
    Y6_slopes[3] = cs5[4]
    Y6_slopes[4] = cs5[3]                      # transpose two slopes
    r6 = rank_poly(Y5_blocks, Y6_slopes, q5, m5, h5)
    check("F3 Y6 (same supports, slopes off the Mobius locus) collapses",
          r6 == 2 * m5, "rank=%d 2m=%d" % (r6, 2 * m5))
    check("F4 both are astronomically below 2V = 132",
          r5 < 2 * V5 and r6 < 2 * V5,
          "rank %d and %d vs 2V = %d; charges %.4f and %.4f"
          % (r5, r6, 2 * V5, r5 / V5, r6 / V5))
    r5b = zec.rank_row(sup5, Y5_slopes, pts5, k5, q5)
    check("F5 brute-force rank_row agrees at RowC scale", r5b == r5,
          "brute %d poly %d" % (r5b, r5))
    RECORD["Y5"] = dict(q=q5, k=k5, V=V5, t=t5, U=len(pts5), A=g5["A"],
                        h=h5, m=m5, e=e5, rank=r5, rank_control=r6,
                        charge=r5 / V5, two_V=2 * V5)

    # ------------------------------------------------------------ SECTION G
    print("\n--- G. retro-explanation of the banked X1/X2/X3 (Q8) ---")
    banked = [
        ("X1", 17, 3, 2, [1, 2, 4, 8], 3, 5, 9, 1, [12, 8, 2, 3]),
        ("X2", 17, 5, 4, sorted({pow(x, 4, 17) for x in range(1, 17)}),
         7, 11, 21, 1, None),
        ("X3", 13, 5, 3, sorted({pow(x, 3, 13) for x in range(1, 13)}),
         4, 7, 12, 2, None),
    ]
    for name, q, k, d, cs, h_p, m_p, rk_p, e_p, zrec in banked:
        blocks = fibres(q, d, cs)
        pts, supports = build_system(blocks, [])
        m = len(pts) - k
        h = len(supports[0]) - k
        t = len(blocks[0])
        sigma = (len(blocks) - 3) * t
        e = k - sigma
        slopes = list(cs)
        r = zec.rank_row(supports, slopes, pts, k, q)
        da = zec.ann_dim(supports, slopes, pts, k, q, set(range(len(pts))))
        check("G[%s] e = k - sigma = 2t - h equals the banked deficit" % name,
              e == e_p and e == 2 * t - h and da == e,
              "e=%d banked deficit=%d dimAnn=%d" % (e, e_p, da))
        check("G[%s] rank = 3h reproduces the banked rank" % name,
              r == 3 * h and r == rk_p and (h, m) == (h_p, m_p),
              "rank=%d banked=%d 3h=%d h=%d m=%d" % (r, rk_p, 3 * h, h, m))
        if zrec is not None:
            check("G[%s] the banked slopes ARE Mobius-equivalent to (c_a)"
                  % name, mobius_equiv(cs, zrec, q),
                  "c=%s z=%s CR=%s" % (cs, zrec,
                                       zec.cross_ratio(cs[0], cs[1], cs[2],
                                                       cs[3], q)))

    # ------------------------------------------------------------ SECTION H
    print("\n--- H. the record's clique model and the k <= 2h^2 criterion ---")
    rows = json.load(open(STAGE5))["criterion"]
    bad_model = []
    for row in rows:
        h = row["h"]
        d = 1
        t = h - d
        m = 2 * h - d
        u = row["k"] + 2 * h - d
        vmax = u // t
        if not (m == row["clique_m"] and u == row["clique_u"]
                and vmax == row["clique_Vmax"] and m == t + h):
            bad_model.append(row["name"])
    check("H1 (Q11) the record's clique model IS B(V,t,t_0,k) with t = h-d",
          not bad_model, "checked %d rows: m = 2h-d = t+h, u = k+m, "
          "Vmax = u//t (block-disjointness bound)" % len(rows))
    y1 = RECORD["Y1"]
    h1, d1 = y1["h"], y1["pair"] - y1["k"]
    check("H2 (Q11) Y1 IS the record's own clique at (k,h,d) = (5,3,1), V=Vmax",
          (y1["k"], h1, d1) == (5, 3, 1) and y1["t"] == h1 - d1
          and y1["m"] == 2 * h1 - d1
          and y1["V"] == (y1["k"] + 2 * h1 - d1) // (h1 - d1),
          "t=h-d=%d m=2h-d=%d Vmax=%d" % (y1["t"], y1["m"], y1["V"]))
    check("H3 (Q12) the secondary criterion k <= 2h^2 is REFUTED by Y1",
          y1["k"] <= 2 * h1 * h1 and y1["charge"] < 2,
          "k=%d <= 2h^2=%d yet per-ray charge = %.2f < 2"
          % (y1["k"], 2 * h1 * h1, y1["charge"]))
    print("    row              h        Vmax   2*Vmax<=3h  k<=2h^2  "
          "ceiling charge")
    corrected = {}
    for row in rows:
        h = row["h"]
        vmax = row["clique_Vmax"]
        corrected[row["name"]] = (2 * vmax <= 3 * h)
        print("    %-14s %-11d %-6d %-11s %-8s %.4f"
              % (row["name"], h, vmax, 2 * vmax <= 3 * h, row["k_le_2h2"],
                 row["clique_charge_per_ray"]))
    prize = [r for r in rows if r["name"].startswith("prize")]
    rowc = [r for r in rows if r["name"].startswith("RowC")]
    check("H4 (Q12) corrected criterion 2V <= 3h HOLDS at all three prize rows",
          all(corrected[r["name"]] for r in prize),
          "so the prize-row conclusion survives, now on the PROVED floor "
          "rank >= 3h")
    check("H5 (Q12) corrected criterion FAILS at all three RowC rows",
          all(not corrected[r["name"]] for r in rowc),
          "as the record already concedes (ceiling charge 0.27/0.53/0.29)")
    check("H6 the two criteria are NOT equivalent (Y1 separates them)",
          (y1["k"] <= 2 * h1 * h1) != (2 * y1["V"] <= 3 * h1))

    # ------------------------------------------------------------ SECTION I
    print("\n--- I. V = 5 general (non-block) zero escape: m <= 3h-4 (Q10) ---")
    rng = zec.LCG(20260803)
    seen = 0
    viol = 0
    overlap = 0
    for _ in range(4000):
        n0 = rng.randint(9, 16)
        b = rng.randint(2, 4)
        blocks = []
        cnt = [0] * n0
        ok = True
        for _a in range(5):
            avail = [x for x in range(n0) if cnt[x] < 2]
            if len(avail) < b:
                ok = False
                break
            blk = rng.sample(avail, b)
            for x in blk:
                cnt[x] += 1
            blocks.append(sorted(blk))
        if not ok:
            continue
        A0 = [x for x in range(n0) if cnt[x] == 0]
        pts, supports = build_system(blocks, A0)
        if len(pts) != n0:
            continue
        sets = [set(S) for S in supports]
        if len({len(s) for s in sets}) != 1:
            continue
        A = len(sets[0])
        for k in range(2, A):
            h = A - k
            pair = min(len(sets[a] & sets[bb])
                       for a, bb in combinations(range(5), 2))
            trip = max(len(sets[a] & sets[bb] & sets[c])
                       for a, bb, c in combinations(range(5), 3))
            mult = [sum(1 for s in sets if i in s) for i in range(n0)]
            if min(mult) < 3 or pair < k + 1 or trip > k - 1:
                continue
            seen += 1
            if any(set(x) & set(y) for x, y in combinations(blocks, 2)):
                overlap += 1
            if n0 - k > 3 * h - 4:
                viol += 1
    check("I1 (Q10) every gate-clean V=5 zero-escape system has m <= 3h-4",
          viol == 0 and seen > 0,
          "%d systems passed the gates (%d with OVERLAPPING blocks), "
          "%d violations" % (seen, overlap, viol))

    # ------------------------------------------------------------ SECTION J
    print("\n--- J. EXPLORATORY (not pre-registered): the e = 2 boundary ---")
    qj, kj, tj, hj, Vj = 19, 8, 3, 4, 5
    mj, ej = tj + hj, 2 * tj - hj
    csj = sorted({pow(x, 3, qj) for x in range(1, qj)})
    penj = fibres(qj, 3, csj)[:Vj]
    rngj = zec.LCG(777)
    pool_j = list(range(1, 16))

    def sweep_j(blocks):
        cs = pencil_params(blocks, qj)
        obs, pred, dims, mism = 0, 0, set(), 0
        for z2 in range(qj):
            if z2 in (0, 1):
                continue
            for z3 in range(qj):
                if z3 in (0, 1, z2):
                    continue
                for z4 in range(qj):
                    if z4 in (0, 1, z2, z3):
                        continue
                    zs = [0, 1, z2, z3, z4]
                    da = 2 * mj - rank_poly(blocks, zs, qj, mj, hj)
                    p = (cs is not None) and mobius_equiv(cs, zs, qj)
                    if da > 0:
                        obs += 1
                        dims.add(da)
                    if p:
                        pred += 1
                    if (da > 0) != p:
                        mism += 1
        return obs, pred, dims, mism

    ptsj, supj = build_system(penj, [])
    gj = gates(ptsj, supj, kj)
    check("J0 the e=2 pencil fixture is gate-clean",
          gj["same_size"] and gj["minmult"] >= 3 and gj["pair"] == kj + 1
          and gj["trip"] <= kj - 1 and gj["m"] == mj and gj["h"] == hj,
          "V=%d t=%d |U|=%d A=%d h=%d m=%d e=%d pair=%d trip=%d"
          % (Vj, tj, gj["n"], gj["A"], gj["h"], gj["m"], ej, gj["pair"],
             gj["trip"]))
    obs, pred, dims, mism = sweep_j(penj)
    check("J1 e=2 pencil: locus = Mobius orbit, every hit has dim Ann = e = 2",
          mism == 0 and obs > 0 and dims == {ej},
          "observed %d = predicted %d, deficits seen %s" % (obs, pred, dims))
    nonp = 0
    tot_j = 0
    for _ in range(60):
        p = list(pool_j)
        blk = []
        for _a in range(Vj):
            b = rngj.sample(p, tj)
            for x in b:
                p.remove(x)
            blk.append(sorted(b))
        if is_pencil(blk, qj):
            continue
        o, pr, dm, ms = sweep_j(blk)
        tot_j += 1
        nonp += o
        if tot_j >= 3:
            break
    check("J2 e=2 NON-pencil supports: empty locus (MEASURED, not proved)",
          nonp == 0,
          "%d non-pencil partitions x 4080 slope tuples, %d hits"
          % (tot_j, nonp))
    rj = rank_poly(penj, [csj[i] for i in range(Vj)], qj, mj, hj)
    note("J3 separability", "the e=2 pencil fixture BREAKS the collapse "
         "(rank <= 2m-e = %d < %d) yet KEEPS charge 2 (3h = %d >= 2V = %d)"
         % (2 * mj - ej, 2 * mj, 3 * hj, 2 * Vj))

    # ----------------------------------------------------------------- done
    print("\n%d checks, %d FAIL" % (len(CHECKS), len(FAILURES)))
    with open(ROOT + "/notes/pilots_20260803/v5_occupancy/verify.json",
              "w") as f:
        json.dump(RECORD, f, indent=1, sort_keys=True)
    if FAILURES:
        print("FAILURES: " + ", ".join(FAILURES))
        sys.exit(1)
    print("V5_OCCUPANCY_ALL_PASS")


if __name__ == "__main__":
    main()
