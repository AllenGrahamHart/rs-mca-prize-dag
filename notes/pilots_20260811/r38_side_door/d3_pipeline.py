"""d3_pipeline.py -- r38_side_door D3: W assembly, per-side split, mu(x) at the
middles, the full incidence table, and the DEFICIENCY-AWARE bivariate system S2.

tools/ramguard local -- python3 notes/pilots_20260811/r38_side_door/d3_pipeline.py <tag>

bank 2's biv_core.py is IMPORTED READ-ONLY after a pre-import audit: it contains no
open(), no .write, no flush and no module-level statement other than `import random`
(so the brief's "it writes at import time" warning is FALSE for this file -- the
module-level "w"-mode write is in share3_pencil.py, a different banked script).
sys.dont_write_bytecode is set BEFORE the import so no __pycache__ is created
outside my write scope.
"""

import random
import sys
import time

sys.dont_write_bytecode = True
sys.path.insert(0, "notes/pilots_20260811/rh_bivariate_system")
import biv_core                                                    # noqa: E402

TAG = sys.argv[1] if len(sys.argv) > 1 else "a"
OUT = "notes/pilots_20260811/r38_side_door/d3_pipeline_results_%s.txt" % TAG
FH = open(OUT, "a")


def say(s=""):
    FH.write(s + "\n")
    FH.flush()
    print(s)


M = 4
RHO = 4 * M - 1

# ---- the two best legal objects from d2_build_results_d.txt:34,70,105 ------------
OBJ = {
    "A": dict(q=193, tag="DOOR A (one double-root fibre, 23 slots, 9 merges)",
              t=[0, 11, 36, 43, 44, 80, 156, 178],
              Psi=[143, 27, 114, 48, 125, 71, 24, 160, 72, 119, 119, 145, 182, 125, 84, 96]),
    "B": dict(q=257, tag="BASELINE (24 slots, 10 merges) -- beats r36/r37's q=257 ceiling",
              t=[0, 21, 42, 66, 68, 147, 180, 230],
              Psi=[169, 51, 210, 191, 159, 249, 166, 36, 56, 40, 49, 135, 14, 169, 15, 60]),
}


def wv(t, q):
    return [1, t % q, t * t % q, t * t % q * t % q]


def cubic_at(Psi, t, q):
    w = wv(t, q)
    return [sum(w[i] * Psi[4 * i + j] for i in range(4)) % q for j in range(4)]


def roots_of(c, q):
    if c[0] == 0:
        return None
    r = []
    for g in range(q):
        if (c[0] * g % q * g % q * g - c[1] * g % q * g + c[2] * g - c[3]) % q == 0:
            r.append(g)
    if len(r) == 3:
        return r
    inv = pow(c[0], q - 2, q)
    s = c[1] * inv % q
    if len(r) == 2:
        for x in r:
            y = [z for z in r if z != x][0]
            if (2 * x + y) % q == s:
                return [x, x, y]
    if len(r) == 1 and (3 * r[0]) % q == s:
        return [r[0]] * 3
    return None


def pencil_fibres(q):
    D = biv_core.mu_N(q, 64)
    idx = {x: i for i, x in enumerate(D)}
    pts = {}
    for i in range(64):
        for j in range(i + 1, 64):
            x, y = D[i], D[j]
            z = pow(x * y % q, q - 2, q)
            k = idx[z]
            if k <= j or z == x or z == y:
                continue
            pts[((x + y + z) % q, (x * y + y * z + z * x) % q)] = (x, y, z)
    P = list(pts.keys())
    lines = {}
    for i in range(len(P)):
        x1, y1 = P[i]
        for j in range(i + 1, len(P)):
            x2, y2 = P[j]
            u, v = (x2 - x1) % q, (y2 - y1) % q
            n1, n2 = (-v) % q, u
            c = (n1 * x1 + n2 * y1) % q
            piv = n1 if n1 else n2
            inv = pow(piv, q - 2, q)
            lines.setdefault((n1 * inv % q, n2 * inv % q, c * inv % q), set()).update((i, j))
    best = None
    for key, mem in lines.items():
        if len(mem) < 9:
            continue
        n1, n2, c = key
        u, v = (-n2) % q, n1
        base = P[sorted(mem)[0]]
        sel, used = {}, set()
        for mi in sorted(mem):
            tri = pts[P[mi]]
            if used & set(tri):
                continue
            used |= set(tri)
            dx, dy = (P[mi][0] - base[0]) % q, (P[mi][1] - base[1]) % q
            s = dx * pow(u, q - 2, q) % q if u else dy * pow(v, q - 2, q) % q
            sel[s] = tri
        if best is None or len(sel) > len(best):
            best = sel
    return best


def nullspace(rows, ncols, q):
    """independent Gaussian elimination -> (rank, kernel basis)."""
    R = [r[:] for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        p = None
        for i in range(r, len(R)):
            if R[i][c]:
                p = i
                break
        if p is None:
            continue
        R[r], R[p] = R[p], R[r]
        inv = pow(R[r][c], q - 2, q)
        R[r] = [x * inv % q for x in R[r]]
        for i in range(len(R)):
            if i != r and R[i][c]:
                f = R[i][c]
                R[i] = [(R[i][k] - f * R[r][k]) % q for k in range(ncols)]
        piv.append(c)
        r += 1
        if r == len(R):
            break
    free = [c for c in range(ncols) if c not in piv]
    ker = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-R[i][fc]) % q
        ker.append(v)
    return r, ker


def s2_rows(m, q, Wvals, Amap, extra):
    """the S2 rows, built exactly as biv_core.build_S2 does, for the independent solve."""
    cols, polys = [], {}
    for x in Wvals:
        pi = biv_core.poly_from_roots(Amap[x], q)
        k = extra.get(x, 0)
        for t in range(k + 2):
            polys[(x, t)] = [0] * t + pi
            cols.append((x, t))
    pw = {x: [pow(x, i, q) for i in range(4 * m + 1)] for x in Wvals}
    rows = []
    for i in range(4 * m + 1):
        for j in range(m + 2):
            vec = [0] * len(cols)
            nz = False
            for ci, (x, t) in enumerate(cols):
                p = polys[(x, t)]
                if j < len(p) and p[j]:
                    vec[ci] = pw[x][i] * p[j] % q
                    nz = True
            if nz:
                rows.append(vec)
    return rows, cols


def blockwise_nonzero(ker, cols, Wvals, q):
    """is there a kernel vector whose block at EVERY x in W is nonzero?
    tries the basis and 400 random combinations (the honest sampled answer)."""
    blocks = {}
    for ci, (x, t) in enumerate(cols):
        blocks.setdefault(x, []).append(ci)
    rng = random.Random(20260811)
    trials = [k[:] for k in ker]
    for _ in range(400):
        v = [0] * len(cols)
        for k in ker:
            c = rng.randrange(q)
            v = [(v[i] + c * k[i]) % q for i in range(len(cols))]
        trials.append(v)
    for v in trials:
        if any(v) and all(any(v[i] for i in blocks[x]) for x in Wvals):
            return True
    return False


def pipeline(name, o):
    q, T8, Psi = o["q"], o["t"], o["Psi"]
    say("")
    say("=" * 74)
    say("D3 PIPELINE on OBJECT %s : q=%d  %s" % (name, q, o["tag"]))
    fib = pencil_fibres(q)
    cub = {}
    for t in T8:
        cub[t] = roots_of(cubic_at(Psi, t, q), q)
    say("  replay of the d2 object: " + str({t: cub[t] for t in T8}))
    slopes2 = sorted({g for t in T8 for g in cub[t]})
    deg = {g: sum(1 for t in T8 if g in cub[t]) for g in slopes2}
    slots = sum(len(set(cub[t])) for t in T8)
    say("  |slopes|=%d slots=%d merges=%d maxdeg=%d  deficient fibres=%s"
        % (len(slopes2), slots, slots - len(slopes2), max(deg.values()),
           [t for t in T8 if len(set(cub[t])) < 3]))
    # ---- 2-colour the merge graph -> the per-side (2,1)/(1,2) classes
    adj = {t: set() for t in T8}
    for g in slopes2:
        ts = [t for t in T8 if g in cub[t]]
        if len(ts) == 2:
            adj[ts[0]].add(ts[1])
            adj[ts[1]].add(ts[0])
    col, stack = {T8[0]: 0}, [T8[0]]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in col:
                col[v] = 1 - col[u]
                stack.append(v)
            elif col[v] == col[u]:
                say("  MERGE GRAPH NOT BIPARTITE -- object rejected")
                return
    for t in T8:
        col.setdefault(t, 0)
    X = [t for t in T8 if col[t] == 0]
    Y = [t for t in T8 if col[t] == 1]
    say("  per-side 2-colouring: (2,1)-fibres %s | (1,2)-fibres %s  -> %d/%d %s"
        % (X, Y, len(X), len(Y), "BALANCED" if len(X) == len(Y) == 4 else "UNBALANCED"))
    if len(X) != 4 or len(Y) != 4:
        say("  4/4 per-side balance FAILS -- object rejected (r36's verifier clause)")
        return
    # ---- the middle fibre: pick an unused pencil fibre whose cubic splits enough
    mid = None
    for t in sorted(fib):
        if t in T8:
            continue
        c = cubic_at(Psi, t, q)
        rr = [g for g in range(q) if (c[0] * g % q * g % q * g - c[1] * g % q * g
                                      + c[2] * g - c[3]) % q == 0]
        if len(rr) >= 2:
            mid = (t, rr)
            break
    if mid is None:
        say("  NO USABLE MIDDLE FIBRE (no unused pencil fibre whose slope cubic has")
        say("  >= 2 roots in F_q) -- the 9th fibre cannot be assembled.  MISS recorded.")
        return
    tmid, mroots = mid
    say("  middle fibre t=%d, slope-cubic roots in F_q: %s" % (tmid, mroots))
    # ---- mu(x) at the middles: exactly ONE root must NOT be a type-2 slope
    inZ = [g for g in mroots if g in slopes2]
    say("  mu(x)-AT-MIDDLES CHECK (never verified in this lane before):")
    say("     roots of the middle cubic that ARE type-2 slopes of the outer layer: %s" % inZ)
    say("     -> a middle needs EXACTLY m-2 = 2 type-2 slopes and one non-slope root;")
    say("        here %d of %d roots collide with the outer slope set: %s"
        % (len(inZ), len(mroots), "PASS" if len(inZ) == 0 else "COLLISION"))
    mid2 = [g for g in mroots if g not in slopes2][:2]
    if len(mid2) < 2:
        say("     FEWER THAN 2 usable middle slopes -- W cannot be completed. STOP.")
        return
    munot = [g for g in mroots if g not in mid2]
    say("     reserved middle type-2 slopes (X''=3, X'=0): %s ; mu-root(s): %s"
        % (mid2, munot))
    # ---- type-1 slopes: any two values outside Z
    Z2 = set(slopes2) | set(mid2)
    g1 = next(g for g in range(q) if g not in Z2 and g not in munot)
    g2 = next(g for g in range(q) if g not in Z2 and g not in munot and g != g1)
    say("  type-1 slopes chosen outside Z: gamma_g=%d gamma_h=%d ; |Z| = 2+%d = %d (need T=%d)"
        % (g1, g2, len(Z2), 2 + len(Z2), RHO + 2))
    # ---- W assembly and A_x
    Wv, Amap, side, extra = [], {}, {}, {}
    for t in T8:
        tri = fib[t]
        rs = sorted(set(cub[t]))
        gs = 2 if t in X else 1
        for k, x in enumerate(tri):
            Wv.append(x)
            side[x] = "g" if k < gs else "h"
            Amap[x] = sorted(set(rs) | {g1 if side[x] == "g" else g2})
            if len(rs) < 3:
                extra[x] = 3 - len(rs)
    for x in fib[tmid]:
        Wv.append(x)
        side[x] = "gh"
        Amap[x] = sorted(set(mid2) | {g1, g2})
    say("  |W| = %d (need a = 7m-1 = 27) %s ; distinct %d"
        % (len(Wv), "OK" if len(Wv) == 27 else "FAIL", len(set(Wv))))
    dxs = {}
    for x in Wv:
        dxs[len(Amap[x])] = dxs.get(len(Amap[x]), 0) + 1
    defsum = sum((M - len(Amap[x])) for x in Wv)
    say("  d_x histogram %s ; sum_x (m-d_x) over W = %d = 1+O -> O = %d  [(SAT4) cap m=%d]"
        % (dxs, defsum, defsum - 1, M))
    # ---- the full incidence table
    say("  INCIDENCE TABLE (gamma : X'_g, X''_g, per-side g|h, degree):")
    okinc = True
    for g in sorted(Z2 | {g1, g2}):
        Sg = [x for x in Wv if g in Amap[x]]
        Xp = sum(1 for x in Sg if side[x] != "gh")
        Xpp = sum(1 for x in Sg if side[x] == "gh")
        pg = sum(1 for x in Sg if side[x] in ("g", "gh"))
        ph = sum(1 for x in Sg if side[x] in ("h", "gh"))
        d = deg.get(g, 0)
        bad = []
        if g not in (g1, g2):
            if pg > M - 1 or ph > M - 1:
                bad.append("PER-SIDE>%d" % (M - 1))
            if Xp + 2 * Xpp > 2 * M - 2:
                bad.append("X'+2X''>%d" % (2 * M - 2))
            if Xp + 2 * Xpp < M - 1 - (3 if g in cub.get(sorted(cub)[0], []) else 0) and Xp + 2 * Xpp < M - 1:
                eps = sum(1 for x in Sg if len(Amap[x]) < M)
                if Xp + 2 * Xpp < M - 1 - eps:
                    bad.append("(OUT-m)")
        if bad:
            okinc = False
        say("     %4d : X'=%2d X''=%d  per-side %d|%d  deg=%d  %s"
            % (g, Xp, Xpp, pg, ph, d, ",".join(bad) if bad else "ok"))
    say("  incidence table: %s" % ("ALL CAPS RESPECTED" if okinc else "CAP VIOLATION"))
    # ---- the deficiency-aware bivariate system S2, via bank 2's builder
    t0 = time.time()
    pr, cols, ncols, nrows, TT, aa = biv_core.build_S2(M, q, Wv, Amap, extra=extra)
    rows, cols2 = s2_rows(M, q, Wv, Amap, extra)
    rk, ker = nullspace(rows, len(cols2), q)
    say("  S2 (deficiency-aware): %d rows x %d cols  [2a + Delta_W = %d + %d]"
        % (nrows, ncols, 2 * len(Wv), sum(extra.values())))
    say("     bank-2 biv_core rank = %d ; independent rank = %d  -> %s"
        % (pr.rank, rk, "AGREE" if pr.rank == rk else "DISAGREE"))
    say("     nullity = %d" % (ncols - rk))
    if ncols - rk == 0:
        say("     NO KERNEL AT ALL -> this configuration is EXCLUDED by the")
        say("     bivariate layer, independently of the slope-count shortfall.")
    else:
        bw = blockwise_nonzero(ker, cols2, Wv, q)
        say("     blockwise-nonzero kernel vector found: %s" % bw)
        if not bw:
            say("     -> kernel exists but every vector vanishes on some x in W:")
            say("        EXCLUDED (the (alpha_x,beta_x) != (0,0) requirement fails).")
    say("     (%.1f s)" % (time.time() - t0))


def synthetic(q, nrep, rng):
    """THE DECISIVE TEST: would the bivariate layer accept a DOOR-A witness if the
    slope layer were solved?  Build legal 13-slope Door-A incidence tables on a real
    27-point W with fresh random slope values and run S2 on each."""
    say("")
    say("=" * 74)
    say("D3(b) SYNTHETIC 13-SLOPE DOOR-A TABLES at q=%d (slope layer ASSUMED solved)" % q)
    fib = pencil_fibres(q)
    ts = sorted(fib)[:9]
    T8, tmid = ts[:8], ts[8]
    # A slots (3,3,3,2) with A4 degenerate; B slots (3,3,3,3); 10 edges
    edges = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 3),
             (2, 0), (2, 2), (3, 1), (3, 3)]
    res = {}
    for rep in range(nrep):
        vals = rng.sample(range(q), 17)
        merged, un = vals[:10], vals[10:13]
        mid2, g1, g2 = vals[13:15], vals[15], vals[16]
        F = {i: [] for i in range(8)}
        for e, (i, j) in enumerate(edges):
            F[i].append(merged[e])
            F[4 + j].append(merged[e])
        F[2].append(un[0])            # A3 has 3 slots, 2 merged
        F[6].append(un[1])
        F[7].append(un[2])
        Wv, Amap, extra, side = [], {}, {}, {}
        ok = True
        for i in range(8):
            if len(set(F[i])) != (2 if i == 3 else 3):
                ok = False
            tri = fib[T8[i]]
            gs = 2 if i < 4 else 1
            for k, x in enumerate(tri):
                Wv.append(x)
                side[x] = "g" if k < gs else "h"
                Amap[x] = sorted(set(F[i]) | {g1 if side[x] == "g" else g2})
                if i == 3:
                    extra[x] = 1
        for x in fib[tmid]:
            Wv.append(x)
            side[x] = "gh"
            Amap[x] = sorted(set(mid2) | {g1, g2})
        if not ok:
            continue
        rows, cols2 = s2_rows(M, q, Wv, Amap, extra)
        rk, ker = nullspace(rows, len(cols2), q)
        nul = len(cols2) - rk
        bw = blockwise_nonzero(ker, cols2, Wv, q) if nul else False
        res[(nul, bw)] = res.get((nul, bw), 0) + 1
    say("  %d synthetic legal 13-slope Door-A tables, |W| = 27, deficiency 3 at the" % nrep)
    say("  three points of the degenerate fibre (extra column each):")
    say("  (nullity, blockwise-nonzero kernel) -> count : %s" % res)
    return res


def main():
    say("")
    say("#" * 74)
    say("D3 PIPELINE  r38_side_door  tag=%s  %s" % (TAG, time.strftime("%H:%M:%S")))
    for name in ("A", "B"):
        pipeline(name, OBJ[name])
    rng = random.Random(38)
    for q in (193, 257):
        synthetic(q, 12, rng)
    say("#" * 74)
    FH.close()


main()
