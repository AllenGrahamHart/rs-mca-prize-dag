"""r38_sporadic_det -- D2: the determinantal 11-merge solve.

Stdlib only.  Run:  tools/ramguard local -- python3 <this> TAG Q NDRAW
Results append to d2_solve_results_TAG.txt (append mode, versioned by TAG).
Every open() is hard-coded to this pilot directory.  No banked script is
imported (imported-script rule: not triggered; helpers are duplicated).

Instrument (registered R4.2/R4.3/R4.4):
  Psi in P^15,  R(t,gamma) = w(t)^T Psi v(gamma),
  w(t) = (1,t,t^2,t^3),  v(gamma) = (gamma^3, -gamma^2, gamma, -1).
  Merge graph = K_{4,4} minus a perfect matching minus one edge, 11 edges,
  degrees (3,3,3,2 | 3,3,3,2).
  Prescribe 7 edges with explicit slopes -> 14 linear rows, rank 14,
  kernel dim 2 -> pencil Psi = alpha A + B.
  Each of the 4 RESIDUAL edges (i,j) merges at gamma iff
    D_ij(gamma) = A_i(gamma) B_j(gamma) - A_j(gamma) B_i(gamma) = 0,
  a binary form of degree <= 6; each root gives one alpha.  A solution is a
  COMMON alpha across all four residual edges.  Then the MISS-2 guard runs.
"""
import sys, random, time
from collections import defaultdict

DIR = "/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260811/r38_sporadic_det/"
TAG = sys.argv[1] if len(sys.argv) > 1 else "a"
Q = int(sys.argv[2]) if len(sys.argv) > 2 else 193
NDRAW = int(sys.argv[3]) if len(sys.argv) > 3 else 20000
FH = open(DIR + "d2_solve_results_%s.txt" % TAG, "a")
CK = open(DIR + "d2_solve_ckpt.txt", "a")


def w_(s=""):
    FH.write(s + "\n")
    FH.flush()
    print(s)


def ck(s):
    CK.write(s + "\n")
    CK.flush()


# ------------------------------------------------------------------ field
def mu_group(q, n):
    g = 2
    while True:
        x, k = 1, 0
        while True:
            x = x * g % q
            k += 1
            if x == 1:
                break
        if k == q - 1:
            break
        g += 1
    h = pow(g, (q - 1) // n, q)
    out, x = [], 1
    for _ in range(n):
        out.append(x)
        x = x * h % q
    return sorted(out)


INV = None


def build_inv(q):
    global INV
    INV = [0] * q
    for a in range(1, q):
        INV[a] = pow(a, q - 2, q)


# --------------------------------------------- constant-norm pencil census
def pencils(q, want=8):
    """lines in the (e1,e2)-plane holding >= want pairwise-disjoint
    mu_64-split monic cubics with e3 = 1.  Returns list of (t-values,)."""
    M = mu_group(q, 64)
    S = set(M)
    n = len(M)
    pts = []          # (e1, e2, frozenset(roots))
    for i in range(n):
        x = M[i]
        for j in range(i + 1, n):
            y = M[j]
            z = INV[x * y % q]
            if z not in S or z == x or z == y:
                continue
            if z < y:          # keep each triple once: need z the largest
                continue
            e1 = (x + y + z) % q
            e2 = (x * y + x * z + y * z) % q
            pts.append((e1, e2, (x, y, z)))
    lines = defaultdict(set)
    m = len(pts)
    for i in range(m):
        x1, y1, _ = pts[i]
        for j in range(i + 1, m):
            x2, y2, _ = pts[j]
            a = (y2 - y1) % q
            b = (x1 - x2) % q
            c = (a * x1 + b * y1) % q
            if a:
                iv = INV[a]
                key = (1, b * iv % q, c * iv % q)
            else:
                iv = INV[b]
                key = (0, 1, c * iv % q)
            L = lines[key]
            L.add(i)
            L.add(j)
    out = []
    big = 0
    for key, idxs in lines.items():
        if len(idxs) < want:
            continue
        idxs = sorted(idxs)
        # greedy maximum pairwise-disjoint subset (several random orders)
        best = []
        rnd = random.Random(1)
        for _ in range(12):
            order = idxs[:]
            rnd.shuffle(order)
            chosen, used = [], set()
            for k in order:
                r = pts[k][2]
                if used.isdisjoint(r):
                    chosen.append(k)
                    used.update(r)
            if len(chosen) > len(best):
                best = chosen
        big = max(big, len(best))
        if len(best) < want:
            continue
        # affine parameter s along the line: e1 = e1_0 + s*d1, e2 = e2_0 + s*d2
        a, b, c = key
        d1, d2 = (-b) % q, a % q          # direction vector of a*e1+b*e2=c
        if d1:
            base = pts[best[0]]
            ts = [((pts[k][0] - base[0]) * INV[d1]) % q for k in best]
        else:
            base = pts[best[0]]
            ts = [((pts[k][1] - base[1]) * INV[d2]) % q for k in best]
        if len(set(ts)) != len(ts):
            continue
        out.append((ts, [pts[k][2] for k in best]))
    return out, big, len(pts)


# --------------------------------------------------------- merge graph
# A = 0..3, B = 4..7 ; K_{4,4} minus PM {(0,4),(1,5),(2,6),(3,7)} minus (3,6)
EDGES = [(0, 5), (0, 6), (0, 7), (1, 4), (1, 6), (1, 7),
         (2, 4), (2, 5), (2, 7), (3, 4), (3, 5)]
PRESCRIBE_SETS = []


def build_prescribe_sets():
    """All 7-subsets of EDGES, SCORED by the genuine residual degree.

    DISCOVERED IN-ROUND (smoke run, tag 'smoke'): if slope g is prescribed on
    an edge at vertex i then EVERY Psi in the kernel has R(t_i,g) = 0, so both
    kernel basis cubics A_i and B_i vanish at g.  Hence
        D_ij(gamma) = A_i B_j - A_j B_i
    vanishes IDENTICALLY at every prescribed slope of i and of j.  Those roots
    are FORCED and guard-ILLEGAL (they would give the slope hypergraph degree
    3 > 2).  The GENUINE residual condition therefore has degree
        6 - p_i - p_j ,   p_v = number of prescribed edges at v.
    The registered R4.3 degree 6 is the RAW degree; the legal degree is lower.
    Score = product over residual edges of (6 - p_i - p_j): the naive
    common-root rate is score / q^3.
    """
    from itertools import combinations
    scored = []
    for sub in combinations(range(11), 7):
        p = [0] * 8
        for e in sub:
            i, j = EDGES[e]
            p[i] += 1
            p[j] += 1
        resid = [e for e in range(11) if e not in sub]
        sc = 1
        degs = []
        for e in resid:
            i, j = EDGES[e]
            d = 6 - p[i] - p[j]
            degs.append(d)
            sc *= max(d, 0)
        scored.append((sc, sub, tuple(degs), max(p)))
    scored.sort(key=lambda z: -z[0])
    return scored


def vvec(g, q):
    g2 = g * g % q
    return (g2 * g % q, (-g2) % q, g % q, q - 1)


def wvec(t, q):
    t2 = t * t % q
    return (1, t % q, t2, t2 * t % q)


def nullspace(rows, ncols, q):
    m = [r[:] for r in rows]
    piv = {}
    r = 0
    for c in range(ncols):
        p = None
        for i in range(r, len(m)):
            if m[i][c]:
                p = i
                break
        if p is None:
            continue
        m[r], m[p] = m[p], m[r]
        iv = INV[m[r][c]]
        m[r] = [v * iv % q for v in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c]:
                f = m[i][c]
                m[i] = [(m[i][j] - f * m[r][j]) % q for j in range(ncols)]
        piv[c] = r
        r += 1
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for c, rr in piv.items():
            v[c] = (-m[rr][fc]) % q
        basis.append(v)
    return basis


def polymul(a, b, q):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if not ai:
            continue
        for j, bj in enumerate(b):
            if bj:
                out[i + j] = (out[i + j] + ai * bj) % q
    return out


def cubic_from_u(u, q):
    """R(gamma) = u0 g^3 - u1 g^2 + u2 g - u3, ascending coefficient list."""
    return [(-u[3]) % q, u[2] % q, (-u[1]) % q, u[0] % q]


def poly_roots(p, q):
    """all roots in F_q of an ascending-coefficient poly, brute force."""
    out = []
    d = len(p) - 1
    while d >= 0 and p[d] == 0:
        d -= 1
    if d < 0:
        return None      # identically zero
    for g in range(q):
        v = 0
        for k in range(d, -1, -1):
            v = (v * g + p[k]) % q
        if v == 0:
            out.append(g)
    return out


def pgcd_deg(a, b, q):
    """degree of gcd of two ascending-coefficient polynomials over F_q."""
    a = a[:]
    b = b[:]
    while True:
        while a and a[-1] == 0:
            a.pop()
        while b and b[-1] == 0:
            b.pop()
        if not b:
            return len(a) - 1 if a else -1
        if len(a) < len(b):
            a, b = b, a
        if not b:
            return len(a) - 1
        iv = INV[b[-1]]
        while len(a) >= len(b) and a:
            while a and a[-1] == 0:
                a.pop()
            if len(a) < len(b):
                break
            f = a[-1] * iv % q
            sh = len(a) - len(b)
            for k in range(len(b)):
                a[sh + k] = (a[sh + k] - f * b[k]) % q
        a, b = b, a


def slope_set(u, q):
    """The 3 slopes of a fibre as points of the PROJECTIVE slope line P^1(F_q).

    IN-ROUND CORRECTION: PGL_2 acts freely on the slope line (r37 D2.2's
    intrinsic count 12 - 11 + 3 = 4 uses exactly this freedom), so a vanishing
    leading coefficient U~(t) is NOT a degeneracy -- it is the slope gamma =
    infinity, and a PGL_2 change of chart makes it finite.  Rejecting it (the
    affine-chart guard) discards legal configurations.
    Returns None if the binary cubic is degenerate or has a repeated /
    non-rational root; otherwise the 3-element set of P^1 points.
    """
    c = [(-u[3]) % q, u[2] % q, (-u[1]) % q, u[0] % q]   # ascending in gamma
    d = 3
    while d >= 0 and c[d] == 0:
        d -= 1
    if d < 2:
        return None          # identically zero, linear, or a double root at inf
    rts = set()
    for g in range(q):
        v = 0
        for k in range(d, -1, -1):
            v = (v * g + c[k]) % q
        if v == 0:
            rts.add(g)
    if len(rts) != d:
        return None          # a repeated or non-rational finite root
    if d == 2:
        rts.add('inf')       # one simple root at infinity
    return rts


def verify(Psi, ts, q):
    """MISS-2 guard, clauses G1-G3.  Returns (ok, nslopes, reason, sets)."""
    sets = []
    for t in ts:
        wv = wvec(t, q)
        u = [0] * 4
        for k in range(4):
            wk = wv[k]
            if wk:
                for j in range(4):
                    u[j] = (u[j] + wk * Psi[4 * k + j]) % q
        if not any(u):
            return (False, None, "G1 zero cubic", None)
        s = slope_set(u, q)
        if s is None:
            return (False, None, "G2 not 3 distinct P^1 slopes", None)
        sets.append(s)
    allsl = set()
    for s in sets:
        allsl |= s
    deg = defaultdict(int)
    for s in sets:
        for g in s:
            deg[g] += 1
    if max(deg.values()) > 2:
        return (False, len(allsl), "G3 slope degree %d > 2" % max(deg.values()), sets)
    edges = []
    for i in range(8):
        for j in range(i + 1, 8):
            c = len(sets[i] & sets[j])
            if c > 1:
                return (False, len(allsl), "G3 pair multiplicity %d > 1" % c, sets)
            if c == 1:
                edges.append((i, j))
    if len(allsl) != 13:
        return (False, len(allsl), "G3 |slopes| = %d != 13" % len(allsl), sets)
    if len(edges) != 11:
        return (False, len(allsl), "G3 %d merges != 11" % len(edges), sets)
    dg = [0] * 8
    for i, j in edges:
        dg[i] += 1
        dg[j] += 1
    if any((i < 4) == (j < 4) for i, j in edges):
        return (False, len(allsl), "G3 not bipartite on the 4/4 split", sets)
    if sorted(dg[:4]) != [2, 3, 3, 3] or sorted(dg[4:]) != [2, 3, 3, 3]:
        return (False, len(allsl), "G3 degree sequence %s" % dg, sets)
    return (True, len(allsl), "PASS", sets)


def slope_count(Psi, ts, q):
    """lightweight |slopes| measurement (free-merge arm)."""
    sets = []
    for t in ts:
        wv = wvec(t, q)
        u = [0] * 4
        for k in range(4):
            wk = wv[k]
            if wk:
                for j in range(4):
                    u[j] = (u[j] + wk * Psi[4 * k + j]) % q
        s = slope_set(u, q)
        if s is None:
            return None
        sets.append(s)
    allsl = set()
    for s in sets:
        allsl |= s
    deg = defaultdict(int)
    for s in sets:
        for g in s:
            deg[g] += 1
    ok = max(deg.values()) <= 2 and all(
        len(sets[i] & sets[j]) <= 1 for i in range(8) for j in range(i + 1, 8))
    return (len(allsl), ok)


# ----------------------------------------------------------------- the sweep
def sweep(q, ndraw, tpool, armname, seed):
    rnd = random.Random(seed)
    stat = defaultdict(int)
    kerhist = defaultdict(int)
    candhist = defaultdict(int)
    reasons = defaultdict(int)
    slopehist = defaultdict(int)
    best = (99, None)
    hits = []
    t0 = time.time()
    rootdeg = defaultdict(int)
    freehist = defaultdict(int)
    for it in range(ndraw):
        if tpool is None:
            ts = rnd.sample(range(q), 8)
        else:
            full = rnd.choice(tpool)
            ts = rnd.sample(list(full), 8)
        pset = rnd.choice(PRESCRIBE_SETS)
        resid = [e for e in range(11) if e not in pset]
        gs = rnd.sample(range(q), 7)
        gset = set(gs)
        rows = []
        wv = {}
        for t in ts:
            wv[t] = wvec(t, q)
        okrow = True
        for e, g in zip(pset, gs):
            i, j = EDGES[e]
            vv = vvec(g, q)
            for vtx in (i, j):
                W = wv[ts[vtx]]
                rows.append([W[a] * vv[b] % q for a in range(4) for b in range(4)])
        ker = nullspace(rows, 16, q)
        kerhist[len(ker)] += 1
        if len(ker) != 2:
            stat["kernel_dim_not_2"] += 1
            continue
        A, B = ker
        Ai, Bi = [], []
        for t in ts:
            W = wv[t]
            ua = [0] * 4
            ub = [0] * 4
            for k in range(4):
                wk = W[k]
                if wk:
                    for jj in range(4):
                        ua[jj] = (ua[jj] + wk * A[4 * k + jj]) % q
                        ub[jj] = (ub[jj] + wk * B[4 * k + jj]) % q
            Ai.append(cubic_from_u(ua, q))
            Bi.append(cubic_from_u(ub, q))
        # ONE root scan on the first residual edge; the other three are
        # checked by a cheap gcd at each candidate alpha (mathematically
        # identical: every common alpha is in particular an alpha of e0).
        e0 = resid[0]
        i0, j0 = EDGES[e0]
        D = polymul(Ai[i0], Bi[j0], q)
        D2 = polymul(Ai[j0], Bi[i0], q)
        Dp = [(D[k] - D2[k]) % q for k in range(len(D))]
        rts = poly_roots(Dp, q)
        if rts is None:
            stat["e0_identically_zero"] += 1
            continue
        rts = [g for g in rts if g not in gset]
        rootdeg[len(rts)] += 1
        alphas = set()
        for g in rts:
            av = 0
            bv = 0
            for k in range(3, -1, -1):
                av = (av * g + Ai[i0][k]) % q
                bv = (bv * g + Bi[i0][k]) % q
            if av:
                alphas.add((-bv) * INV[av] % q)
        # gamma = infinity branch on e0 (both leading coefficients vanish)
        if Ai[i0][3]:
            al = (-Bi[i0][3]) * INV[Ai[i0][3]] % q
            if (al * Ai[j0][3] + Bi[j0][3]) % q == 0:
                alphas.add(al)
                stat["e0_merge_at_infinity"] += 1
        good = []
        for al in alphas:
            nsat = 0
            for e in resid[1:]:
                i, j = EDGES[e]
                fi = [(al * Ai[i][k] + Bi[i][k]) % q for k in range(4)]
                fj = [(al * Ai[j][k] + Bi[j][k]) % q for k in range(4)]
                if fi[3] == 0 and fj[3] == 0:
                    nsat += 1            # shared slope at gamma = infinity
                elif pgcd_deg(fi, fj, q) >= 1:
                    nsat += 1
            # 7 prescribed + e0 = 8 merges realised; nsat = FREE merges beyond 8
            # (this is r37's free-merge functional, matched and at scale)
            stat["at8"] += 1
            freehist[nsat] += 1
            if nsat == 3:
                good.append(al)
            elif nsat >= 1 or (stat["at8"] % 500 == 0):
                Psi = [(al * A[k] + B[k]) % q for k in range(16)]
                r = slope_count(Psi, ts, q)
                if r is not None:
                    ns, legal = r
                    slopehist[(ns, legal)] += 1
                    if legal and ns < best[0]:
                        best = (ns, (list(ts), al))
        candhist[min(len(good), 5)] += 1
        for al in good:
            Psi = [(al * A[k] + B[k]) % q for k in range(16)]
            ok, ns, why, _ = verify(Psi, ts, q)
            reasons[why] += 1
            if ok:
                stat["VERIFIED_13_SLOPE"] += 1
                hits.append((ts, pset, gs, al))
                ck("HIT q=%d arm=%s ts=%s pset=%s gs=%s alpha=%s"
                   % (q, armname, ts, pset, gs, al))
        if it % 50000 == 0 and it:
            ck("progress q=%d arm=%s it=%d elapsed=%.0fs" % (q, armname, it, time.time() - t0))
    return (dict(stat), dict(kerhist), dict(candhist), dict(reasons),
            dict(slopehist), best, hits, time.time() - t0, dict(rootdeg),
            dict(freehist))


def main():
    global PRESCRIBE_SETS
    q = Q
    build_inv(q)
    SCORED = build_prescribe_sets()
    # IN-ROUND CATCH (run tag q193): a prescribed vertex with p_v = 3 pins
    # u(t_v) into a 1-dimensional space, so the pencil contains EXACTLY ONE
    # alpha with u(t_v) = 0 -- a fibre whose cubic vanishes identically, which
    # makes every edge at v merge trivially.  The score-400 designs saturate
    # THREE vertices, and 11 of the 12 raw solutions they produced were on
    # that degenerate component.  Restrict to max p_v <= 2, which removes the
    # component (2 conditions cannot make a 4-vector vanish on a pencil).
    CLEAN = [z for z in SCORED if z[3] <= 2]
    TOPSCORE = CLEAN[0][0]
    PRESCRIBE_SETS = [z[1] for z in CLEAN if z[0] == TOPSCORE]
    w_("")
    w_("#" * 72)
    w_("# r38_sporadic_det  D2  tag=%s  q=%d  ndraw=%d  %s"
       % (TAG, q, NDRAW, time.strftime("%Y-%m-%d %H:%M:%S")))
    w_("#" * 72)
    w_("merge graph: 11 edges %s" % (EDGES,))
    dg = [0] * 8
    for i, j in EDGES:
        dg[i] += 1
        dg[j] += 1
    w_("  degree sequence %s  (A-side %s | B-side %s)" % (dg, dg[:4], dg[4:]))
    w_("")
    w_("PRESCRIPTION-SET SCORING (in-round discovery, see build_prescribe_sets):")
    w_("  every prescribed slope at a residual endpoint is a FORCED, guard-")
    w_("  ILLEGAL root of D_ij, so the genuine residual degree is 6 - p_i - p_j.")
    w_("  score = prod over the 4 residual edges;  naive rate = score / q^3.")
    sc = defaultdict(int)
    for s, sub, degs, mp in SCORED:
        sc[s] += 1
    w_("  score histogram over all C(11,7) = %d subsets : %s"
       % (len(SCORED), dict(sorted(sc.items(), reverse=True))))
    w_("  UNRESTRICTED best score %d (degrees %s) SATURATES max p_v = %d --"
       % (SCORED[0][0], str(SCORED[0][2]), SCORED[0][3]))
    w_("    REJECTED: p_v = 3 pins u(t_v) to a line, so the pencil carries one")
    w_("    alpha with u(t_v) = 0 (a fibre with an identically-zero cubic).")
    w_("    Run tag q193 produced 12 raw solutions on that design; 11 were on")
    w_("    exactly that degenerate component.  This is the round's MISS-2 catch.")
    w_("  CLEAN designs (max p_v <= 2) : %d ; best score %d (degrees %s),"
       % (len(CLEAN), TOPSCORE, str(CLEAN[0][2])))
    w_("    attained by %d subsets -- USED" % len(PRESCRIBE_SETS))
    w_("  naive common-alpha rate at this design : %.3e   (registered R4.4"
       % (TOPSCORE / q ** 3))
    w_("  used the RAW degree 6, giving %.3e -- registration too optimistic"
       % (1296 / q ** 3))
    t0 = time.time()
    pk, big, npts = pencils(q, 8)
    w_("")
    w_("CONSTANT-NORM PENCIL CENSUS (e3 = 1 slice), q = %d" % q)
    w_("  split cubics in the slice          : %d   (predicted 41664/64 = 651)" % npts)
    w_("  max pairwise-disjoint complete fibres on any line : %d" % big)
    w_("  lines with >= 8 pairwise-disjoint complete fibres  : %d" % len(pk))
    w_("  census elapsed %.1f s" % (time.time() - t0))
    tpool = [tuple(ts) for ts, tris in pk]
    fibhist = defaultdict(int)
    for t in tpool:
        fibhist[len(t)] += 1
    w_("  complete-fibre-count histogram of those lines : %s"
       % dict(sorted(fibhist.items())))
    if not tpool:
        w_("  NO PENCIL AT THIS FIELD -- arm A skipped")
    w_("  arm-A t-pools available            : %d" % len(tpool))

    for armname, pool, seed in (("A_real_t", tpool if tpool else None, 11),
                                ("B_generic_t", None, 23)):
        if armname == "A_real_t" and not tpool:
            continue
        w_("")
        w_("-" * 72)
        w_("ARM %s   q=%d   draws=%d" % (armname, q, NDRAW))
        w_("-" * 72)
        st, kh, ch, rs, sh, best, hits, el, rd, fh = sweep(q, NDRAW, pool, armname, seed)
        w_("kernel-dim histogram after 7 prescribed edges : %s" % dict(sorted(kh.items())))
        w_("  (registered R4.2: rank 2r = 14, kernel dim 2)")
        w_("NON-FORCED root count per residual edge : %s" % dict(sorted(rd.items())))
        tr = sum(rd.values())
        mean = sum(k * v for k, v in rd.items()) / max(tr, 1)
        w_("  mean %.3f legal roots per residual edge (design degrees %s)"
           % (mean, str(CLEAN[0][2])))
        w_("common-alpha count per draw (capped at 5)     : %s" % dict(sorted(ch.items())))
        tot = sum(ch.values())
        nz = sum(v for k, v in ch.items() if k >= 1)
        w_("draws with >= 1 common alpha : %d of %d  = %.3e" % (nz, tot, nz / max(tot, 1)))
        w_("  design-predicted rate %.3e ; registered (raw-degree) rate %.3e"
           % (TOPSCORE / q ** 3, 1296 / q ** 3))
        nat8 = sum(fh.values())
        mf = sum(k * v for k, v in fh.items()) / max(nat8, 1)
        w_("AT THE 8-MERGE STATE (7 prescribed + e0 solved), %d states reached:" % nat8)
        w_("  FREE-MERGE distribution beyond 8 : %s   mean %.4f"
           % (dict(sorted(fh.items())), mf))
        w_("  r37 measured {0:104, 1:11} / {0:128, 1:11}, means .096/.079, max 2")
        w_("  3 free merges are needed for |slopes| = 13.")
        w_("guard outcomes on candidate alphas : %s" % dict(sorted(rs.items(), key=lambda kv: -kv[1])))
        w_("VERIFIED 13-SLOPE SOLUTIONS : %d" % st.get("VERIFIED_13_SLOPE", 0))
        agg = defaultdict(int)
        for (ns, legal), v in sh.items():
            agg[(ns, legal)] += v
        w_("|slopes| histogram on the free-merge subsample (ns, legal) : %s"
           % dict(sorted(agg.items())))
        w_("BEST LEGAL |slopes| this arm : %s" % (best[0] if best[0] < 99 else "none"))
        w_("elapsed %.1f s" % el)
        if hits:
            for h in hits[:5]:
                w_("  HIT ts=%s pset=%s gs=%s alpha=%s" % h)
    w_("")
    w_("TOTAL ELAPSED %.1f s" % (time.time() - t0))
    FH.close()
    CK.close()


main()
