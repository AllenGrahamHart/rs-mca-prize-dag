"""d2_build.py -- r38_side_door D2: build the degenerate-fibre configuration.

Stdlib only.  tools/ramguard local -- python3 notes/pilots_20260811/r38_side_door/d2_build.py <tag> <draws>
Results file APPEND mode, versioned by tag.  Checkpoint append-only.

Slope layer:  R(t,gamma) = w(t)^T Psi v(gamma),  w(t)=(1,t,t^2,t^3),
              v(gamma)=(gamma^3,-gamma^2,gamma,-1);  Psi in P^15.
Merge edge (i,j) at gamma : two rank-one functionals w(t_i)(x)v(gamma), w(t_j)(x)v(gamma).
Tangency (double root alpha over t_*) : w(t_*)(x)v(alpha) AND w(t_*)(x)v'(alpha),
              v'(gamma) = (3gamma^2,-2gamma,1,0).
"""

import random
import sys
import time

TAG = sys.argv[1] if len(sys.argv) > 1 else "a"
DRAWS = int(sys.argv[2]) if len(sys.argv) > 2 else 150
OUT = "notes/pilots_20260811/r38_side_door/d2_build_results_%s.txt" % TAG
CKPT = "notes/pilots_20260811/r38_side_door/d2_build_ckpt.txt"
FH = open(OUT, "a")
CK = open(CKPT, "a")


def say(s=""):
    FH.write(s + "\n")
    FH.flush()
    print(s)


def ck(s):
    CK.write(s + "\n")
    CK.flush()


# --------------------------------------------------------------------- field utils
def primitive_root(q):
    n = q - 1
    fac, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            fac.add(d)
            n //= d
        d += 1
    if n > 1:
        fac.add(n)
    for g in range(2, q):
        if all(pow(g, (q - 1) // f, q) != 1 for f in fac):
            return g
    raise RuntimeError


def mu_N(q, N):
    assert (q - 1) % N == 0
    g = primitive_root(q)
    w = pow(g, (q - 1) // N, q)
    out, cur = [], 1
    for _ in range(N):
        out.append(cur)
        cur = cur * w % q
    return out


# ------------------------------------------------------------- constant-norm pencils
def pencils(q, want=9):
    """all lines in the (e1,e2) plane of the e3=1 slice of mu_64-split cubics
    carrying >= want members with pairwise DISJOINT root triples."""
    D = mu_N(q, 64)
    idx = {x: i for i, x in enumerate(D)}
    pts = {}                       # (e1,e2) -> triple
    for i in range(64):
        for j in range(i + 1, 64):
            x, y = D[i], D[j]
            z = pow(x * y % q, q - 2, q)
            k = idx[z]
            if k <= j or z == x or z == y:
                continue
            e1 = (x + y + z) % q
            e2 = (x * y + y * z + z * x) % q
            pts[(e1, e2)] = (x, y, z)
    P = list(pts.keys())
    lines = {}
    for i in range(len(P)):
        x1, y1 = P[i]
        for j in range(i + 1, len(P)):
            x2, y2 = P[j]
            u, v = (x2 - x1) % q, (y2 - y1) % q
            n1, n2 = (-v) % q, u                     # normal
            c = (n1 * x1 + n2 * y1) % q
            piv = n1 if n1 else n2
            inv = pow(piv, q - 2, q)
            key = (n1 * inv % q, n2 * inv % q, c * inv % q)
            lines.setdefault(key, set()).update((i, j))
    good = []
    for key, mem in lines.items():
        if len(mem) < want:
            continue
        mem = sorted(mem)
        # direction along the line
        n1, n2, c = key
        u, v = (-n2) % q, n1                          # direction (u,v)
        base = P[mem[0]]
        sel, used = [], set()
        for mi in mem:
            tri = pts[P[mi]]
            if used & set(tri):
                continue
            used |= set(tri)
            dx = (P[mi][0] - base[0]) % q
            dy = (P[mi][1] - base[1]) % q
            s = dx * pow(u, q - 2, q) % q if u else dy * pow(v, q - 2, q) % q
            sel.append((s, tri))
        if len(sel) >= want:
            good.append(sorted(sel))
    return good, len(P)


# ------------------------------------------------------------------ 16-dim span
def wv(t, q):
    return [1, t % q, t * t % q, t * t % q * t % q]


def vv(g, q):
    g2 = g * g % q
    return [g2 * g % q, (-g2) % q, g % q, q - 1]


def dvv(g, q):
    return [3 * g % q * g % q, (-2 * g) % q, 1, 0]


def tens(a, b, q):
    return [a[i] * b[j] % q for i in range(4) for j in range(4)]


class Span:
    def __init__(self, q):
        self.q = q
        self.piv = {}

    def reduce(self, v):
        q = self.q
        v = v[:]
        for c in sorted(self.piv):
            if v[c]:
                f = v[c]
                p = self.piv[c]
                for k in range(16):
                    v[k] = (v[k] - f * p[k]) % q
        return v

    def add(self, v):
        q = self.q
        v = self.reduce(v)
        for c in range(16):
            if v[c]:
                inv = pow(v[c], q - 2, q)
                v = [x * inv % q for x in v]
                self.piv[c] = v
                return 1
        return 0

    def cost(self, vs):
        """cost of adding the list vs, without mutating."""
        save = dict(self.piv)
        c = sum(self.add(v) for v in vs)
        self.piv = save
        return c

    @property
    def rank(self):
        return len(self.piv)

    def nullvec(self, rng):
        """a random nonzero vector killed by all rows (Psi lives here)."""
        q = self.q
        free = [c for c in range(16) if c not in self.piv]
        if not free:
            return None
        vals = {c: rng.randrange(q) for c in free}
        if all(vals[c] == 0 for c in free):
            vals[free[0]] = 1
        x = [0] * 16
        for c in free:
            x[c] = vals[c]
        for c in sorted(self.piv, reverse=True):
            p = self.piv[c]
            x[c] = (-sum(p[k] * x[k] for k in range(16) if k != c)) % q
        return x if any(x) else None


def cubic_at(Psi, t, q):
    """coefficients (c0..c3) of R(t,.) = c0 g^3 - c1 g^2 + c2 g - c3."""
    w = wv(t, q)
    return [sum(w[i] * Psi[4 * i + j] for i in range(4)) % q for j in range(4)]


def roots_of(c, q, gl):
    """roots with multiplicity of c0 g^3 - c1 g^2 + c2 g - c3 (needs c0 != 0)."""
    if c[0] == 0:
        return None
    r = []
    for g in gl:
        if (c[0] * g % q * g % q * g - c[1] * g % q * g + c[2] * g - c[3]) % q == 0:
            r.append(g)
    if len(r) == 3:
        return r
    if len(r) == 2:                     # one is a double root
        inv = pow(c[0], q - 2, q)
        s = c[1] * inv % q              # sum with multiplicity
        for x in r:
            if (2 * x + (r[0] + r[1] - x)) % q == s:
                pass
        for x in r:
            y = [z for z in r if z != x][0]
            if (2 * x + y) % q == s:
                return [x, x, y]
        return None
    if len(r) == 1:
        inv = pow(c[0], q - 2, q)
        if (3 * r[0]) % q == c[1] * inv % q:
            return [r[0]] * 3
        return None
    return None


# --------------------------------------------------------------------- the search
def run(q, draws, rng, mode, m4=4):
    """mode 'base' = 11-merge design, 'doorA' = tangency + 10-merge design."""
    gl = list(range(q))
    pens, npts = pencils(q, 9)
    if not pens:
        return None
    pen = max(pens, key=len)
    tvals = [s for s, _ in pen]
    tris = {s: tri for s, tri in pen}
    stat = {"cost": {}, "items": {}, "slopes": {}, "free": {}, "illegal": 0,
            "npts": npts, "npen": len(pens), "nfib": len(pen)}
    best = None
    for _ in range(draws):
        T8 = rng.sample(tvals, 8)
        A, B = T8[:4], T8[4:]
        nedge = 11 if mode == "base" else 10
        # bipartite design with degrees <= 3 (and <= 2 at the degenerate A-vertex)
        capA = [3, 3, 3, 3] if mode == "base" else [3, 3, 3, 2]
        edges = []
        for _try in range(400):
            edges = []
            da, db = [0] * 4, [0] * 4
            cells = [(i, j) for i in range(4) for j in range(4)]
            rng.shuffle(cells)
            for (i, j) in cells:
                if len(edges) == nedge:
                    break
                if da[i] < capA[i] and db[j] < 3:
                    edges.append((i, j))
                    da[i] += 1
                    db[j] += 1
            if len(edges) == nedge:
                break
        if len(edges) != nedge:
            continue
        S = Span(q)
        items = 0
        used = set()

        def implied_third(g, keep):
            """True if some fibre OUTSIDE keep is already forced to have g as a slope
            (r36's common-root collapse: a slope of hypergraph degree > 2)."""
            for tk in T8:
                if tk in keep:
                    continue
                if S.cost([tens(wv(tk, q), vv(g, q), q)]) == 0:
                    return True
            return False

        if mode == "doorA":                       # tangency on A[3] (the 2-slot fibre)
            d0 = S.rank
            alpha = None
            for g in rng.sample(gl, 40):
                if not implied_third(g, (A[3],)):
                    alpha = g
                    break
            if alpha is None:
                continue
            c = S.add(tens(wv(A[3], q), vv(alpha, q), q))
            c += S.add(tens(wv(A[3], q), dvv(alpha, q), q))
            stat["cost"].setdefault(("tang", d0), []).append(c)
            used.add(alpha)
            items += 1
        for (i, j) in edges:
            d0 = S.rank
            if d0 >= 15:
                break
            ncand = 30 if d0 >= 12 else 3
            pick = None
            for g in rng.sample(gl, ncand):
                if g in used:
                    continue
                va = tens(wv(A[i], q), vv(g, q), q)
                vb = tens(wv(B[j], q), vv(g, q), q)
                c = S.cost([va, vb])
                if d0 + c > 15 or c == 0:
                    continue
                save = dict(S.piv)
                S.add(va)
                S.add(vb)
                bad = implied_third(g, (A[i], B[j]))
                S.piv = save
                if bad:
                    continue
                if pick is None or c < pick[0]:
                    pick = (c, g, va, vb)
                if c == 1:
                    break
            if pick is None:
                continue
            c, g, va, vb = pick
            stat["cost"].setdefault(("edge", d0), []).append(c)
            S.add(va)
            S.add(vb)
            used.add(g)
            items += 1
        stat["items"][items] = stat["items"].get(items, 0) + 1
        stat["rank"] = stat.get("rank", {})
        stat["rank"][S.rank] = stat["rank"].get(S.rank, 0) + 1
        Psi = S.nullvec(rng)
        if Psi is None:
            continue
        # ---------------- evaluate the ACTUAL configuration on the 8 outer fibres
        cub, ok = {}, True
        for t in T8:
            c = cubic_at(Psi, t, q)
            r = roots_of(c, q, gl)
            if r is None:
                ok = False
                break
            cub[t] = r
        if not ok:
            stat["illegal"] += 1
            continue
        allsl = []
        for t in T8:
            allsl.extend(sorted(set(cub[t])))
        sl = sorted(set(allsl))
        deg = {g: sum(1 for t in T8 if g in cub[t]) for g in sl}
        ndeg = len(sl)
        # structural verification (MISS-2 guard G1)
        legal = max(deg.values()) <= 2
        pm = {}
        for t in T8:
            ss = sorted(set(cub[t]))
            for x in range(len(ss)):
                for y in range(x + 1, len(ss)):
                    pm[(ss[x], ss[y])] = pm.get((ss[x], ss[y]), 0) + 1
        if any(v > 1 for v in pm.values()):
            legal = False
        # merge graph bipartite between A and B?
        for g in sl:
            if deg[g] == 2:
                ts = [t for t in T8 if g in cub[t]]
                if (ts[0] in A) == (ts[1] in A):
                    legal = False
        ndbl = sum(1 for t in T8 if len(set(cub[t])) == 2)
        ntpl = sum(1 for t in T8 if len(set(cub[t])) == 1)
        slots = sum(len(set(cub[t])) for t in T8)
        merges = slots - ndeg
        # (SAT4): total domain deficiency = 1+O <= m = 4.  A double-root fibre spends
        # 3 units, a triple-root fibre 6.  So at most ONE double and NO triple.
        sat4 = 3 * ndbl + 6 * ntpl
        if sat4 > m4:
            legal = False
        key = (ndeg, ndbl, ntpl, legal)
        stat["slopes"][key] = stat["slopes"].get(key, 0) + 1
        stat["free"][merges - items if mode == "base" else merges - (items - 1)] = \
            stat["free"].get(merges - items if mode == "base" else merges - (items - 1), 0) + 1
        # ---------------- DOOR B probe + THE 9th (MIDDLE) FIBRE REQUIREMENT
        # A middle needs m-2 = 2 type-2 slopes with X''=3, which saturates the per-side
        # cap m-1 = 3 and therefore forces X' = 0: those two roots must AVOID the outer
        # slope set.  So the middle fibre's cubic must (i) split over F_q and (ii) have
        # >= 2 roots outside the outer slope set.  Never imposed before this round.
        dbmid = []
        nsplit = navoid = 0
        for t in tvals:
            if t in T8:
                continue
            c = cubic_at(Psi, t, q)
            r = roots_of(c, q, gl)
            if r is None:
                continue
            nsplit += 1
            if len(set(r)) < 3:
                dbmid.append((t, r))
            if len([g for g in set(r) if g not in sl]) >= 2:
                navoid += 1
        if dbmid:
            stat["doorB"] = stat.get("doorB", 0) + 1
        if legal:
            stat["mid_split"] = stat.get("mid_split", {})
            stat["mid_split"][nsplit] = stat["mid_split"].get(nsplit, 0) + 1
            stat["mid_avoid"] = stat.get("mid_avoid", {})
            stat["mid_avoid"][navoid] = stat["mid_avoid"].get(navoid, 0) + 1
        if legal:
            # WITNESS TESTS (MISS-2 guard G1/G2: a count is not a configuration)
            if ndeg == 13 and ndbl == 1 and ntpl == 0:
                stat["HIT_A"] = stat.get("HIT_A", 0) + 1
            if ndeg == 13 and ndbl == 0:
                stat["HIT_BASE"] = stat.get("HIT_BASE", 0) + 1
            if ndeg == 14 and ndbl == 0 and dbmid:
                stat["HIT_B"] = stat.get("HIT_B", 0) + 1
            score = (ndeg, -ndbl)
            if best is None or score < best[0]:
                best = (score, ndeg, ndbl, slots, merges, sorted(T8),
                        {t: cub[t] for t in T8}, Psi[:], dbmid)
    return stat, best, pen, tris


def main():
    t0 = time.time()
    say("=" * 74)
    say("D2 BUILD  r38_side_door  tag=%s draws=%d  %s" % (TAG, DRAWS, time.strftime("%H:%M:%S")))
    for q in (193, 257):
        for mode in ("base", "doorA"):
            rng = random.Random(hash((q, mode, TAG)) & 0xFFFF)
            r = run(q, DRAWS, rng, mode)
            if r is None:
                say("q=%d: NO PENCIL WITH 9 DISJOINT COMPLETE FIBRES" % q)
                continue
            stat, best, pen, tris = r
            say("")
            say("--- q=%d mode=%s : e3=1 slice %d cubics, %d pencils with >=9 disjoint"
                % (q, mode, stat["npts"], stat["npen"]))
            say("    chosen pencil: %d disjoint complete fibres, t = %s"
                % (stat["nfib"], [s for s, _ in pen]))
            say("    prescribed items per draw : %s" % dict(sorted(stat["items"].items())))
            ct = {}
            for (kind, d), cs in sorted(stat["cost"].items()):
                ct[(kind, d)] = (len(cs), sum(cs) / len(cs), min(cs))
            say("    COST TABLE (kind, span dim) -> (draws, mean cost, min cost):")
            for k in sorted(ct):
                say("       %-12s dim %2d : n=%4d mean %.3f min %d" % (k[0], k[1], ct[k][0], ct[k][1], ct[k][2]))
            say("    illegal (a fibre cubic not split / degenerate leading coeff): %d" % stat["illegal"])
            say("    (|slopes|, #double-root fibres, #triple-root fibres, legal) histogram:")
            for k in sorted(stat["slopes"]):
                say("       %s : %d" % (k, stat["slopes"][k]))
            say("    free (unprescribed) merges: %s" % dict(sorted(stat["free"].items())))
            say("    final rank of the prescribed span: %s" % dict(sorted(stat.get("rank", {}).items())))
            say("    DOOR-B probe (unused pencil fibre with a degenerate slope cubic): %d"
                % stat.get("doorB", 0))
            say("    WITNESS TESTS: HIT_A(13 slopes,1 double)=%d  HIT_BASE(13,0)=%d  HIT_B(14,0+deg mid)=%d"
                % (stat.get("HIT_A", 0), stat.get("HIT_BASE", 0), stat.get("HIT_B", 0)))
            say("    9th (MIDDLE) FIBRE, over LEGAL objects only:")
            say("       # unused pencil fibres whose slope cubic SPLITS  : %s"
                % dict(sorted(stat.get("mid_split", {}).items())))
            say("       # of those with >=2 roots OFF the outer slope set: %s"
                % dict(sorted(stat.get("mid_avoid", {}).items())))
            ms = stat.get("mid_avoid", {})
            tot = sum(ms.values())
            if tot:
                say("       -> W CANNOT be completed to 27 points in %d of %d legal objects (%.1f%%)"
                    % (ms.get(0, 0), tot, 100.0 * ms.get(0, 0) / tot))
            if best:
                say("    BEST LEGAL: |slopes|=%d double-root-fibres=%d slots=%d merges=%d"
                    % (best[1], best[2], best[3], best[4]))
                say("       t = %s" % best[5])
                say("       fibres: %s" % {k: v for k, v in sorted(best[6].items())})
                say("       Psi = %s" % best[7])
                say("       degenerate unused fibres: %s" % best[8])
                ck("q=%d mode=%s best |slopes|=%d dbl=%d merges=%d" % (q, mode, best[1], best[2], best[4]))
            else:
                say("    BEST LEGAL: none")
    say("")
    say("elapsed %.1f s" % (time.time() - t0))
    say("=" * 74)
    FH.close()
    CK.close()


main()
