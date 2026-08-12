"""r38_cauchy_lattice D2 - THE PUSH: exhaustive sweep for T=3 over mu_32.

For a fixed (S_0, S_inf) pair of disjoint 7-subsets of mu_32, tests ALL
C(32,7) = 3,365,856 subsets S_1 for a third split member, using the
scale-eliminated moment/rank criterion (TEST) derived in D1.  Any hit is
reconstructed into a full (PAR) object and certified.

usage:  tools/ramguard local -- python3 d2_sweep.py Q PAIRSEED BUDGET [SKIP]

Stdlib only; results appended (never a blind "w"); helpers duplicated
per file (no import of any banked script).
"""
import random
import sys
import time
import itertools

RES = ("notes/pilots_20260811/r38_cauchy_lattice/d2_results_q%s_s%s.txt"
       % (sys.argv[1], sys.argv[2]))
FH = open(RES, "a")


def out(s):
    print(s)
    FH.write(s + "\n")
    FH.flush()


def ptrim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def padd(a, b, q):
    n = max(len(a), len(b))
    r = [0] * n
    for i, c in enumerate(a):
        r[i] = c
    for i, c in enumerate(b):
        r[i] = (r[i] + c) % q
    return ptrim(r)


def psub(a, b, q):
    n = max(len(a), len(b))
    r = [0] * n
    for i, c in enumerate(a):
        r[i] = c
    for i, c in enumerate(b):
        r[i] = (r[i] - c) % q
    return ptrim(r)


def pmul(a, b, q):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        if ca:
            for j, cb in enumerate(b):
                r[i + j] = (r[i + j] + ca * cb) % q
    return ptrim(r)


def pscal(a, c, q):
    return ptrim([x * c % q for x in a])


def pdivmod(a, b, q):
    a = [c % q for c in a]
    ptrim(a)
    b = [c % q for c in b]
    ptrim(b)
    db = len(b) - 1
    if not a or len(a) - 1 < db:
        return [], a
    ivl = pow(b[-1], q - 2, q)
    quo = [0] * (len(a) - db)
    while a and len(a) - 1 >= db:
        d = len(a) - 1 - db
        c = a[-1] * ivl % q
        quo[d] = c
        for j in range(db + 1):
            a[d + j] = (a[d + j] - c * b[j]) % q
        ptrim(a)
    ptrim(quo)
    return quo, a


def pgcd(a, b, q):
    a = a[:]
    b = b[:]
    while b:
        _, r = pdivmod(a, b, q)
        a, b = b, r
    if a:
        iv = pow(a[-1], q - 2, q)
        a = [c * iv % q for c in a]
    return a


def peval(a, x, q):
    r = 0
    for c in reversed(a):
        r = (r * x + c) % q
    return r


def pdeg(a):
    return len(a) - 1


def from_roots(S, q):
    p = [1]
    for r in S:
        p = pmul(p, [(-r) % q, 1], q)
    return p


def nullspace(rows, ncols, q):
    M = [[c % q for c in r] for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        pr = None
        for i in range(r, len(M)):
            if M[i][c]:
                pr = i
                break
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        iv = pow(M[r][c], q - 2, q)
        M[r] = [x * iv % q for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % q for j in range(ncols)]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-M[i][fc]) % q
        basis.append(v)
    return basis, len(piv)


def lagrange_basis(pts, q):
    ba = []
    for i, xi in enumerate(pts):
        num = [1]
        den = 1
        for j, xj in enumerate(pts):
            if j != i:
                num = pmul(num, [(-xj) % q, 1], q)
                den = den * ((xi - xj) % q) % q
        iv = pow(den, q - 2, q)
        c = [v * iv % q for v in num]
        while len(c) < 5:
            c.append(0)
        ba.append(c)
    return ba


def mu32(q):
    return sorted([x for x in range(1, q) if pow(x, 32, q) == 1])


# --------------------------- the sweep ---------------------------------
def build_pair(q, mu, i0, iinf):
    pts0 = [mu[i] for i in i0]
    ptsi = [mu[i] for i in iinf]
    P0 = from_roots(pts0, q)
    Pinf = from_roots(ptsi, q)
    ctx = {}
    ctx["q"] = q
    ctx["pts0"] = pts0
    ctx["ptsi"] = ptsi
    ctx["P0"] = P0
    ctx["Pinf"] = Pinf
    ctx["a0"] = [peval(Pinf, x, q) for x in pts0]
    ctx["ai"] = [peval(P0, x, q) for x in ptsi]
    d0i = []
    for x in pts0:
        d = 1
        for y in pts0:
            if y != x:
                d = d * ((x - y) % q) % q
        d0i.append(pow(d, q - 2, q))
    dii = []
    for x in ptsi:
        d = 1
        for y in ptsi:
            if y != x:
                d = d * ((x - y) % q) % q
        dii.append(pow(d, q - 2, q))
    ctx["d0i"] = d0i
    ctx["dii"] = dii
    ctx["pw0"] = [[pow(x, j, q) for j in range(6)] for x in pts0]
    ctx["pwi"] = [[pow(x, j, q) for j in range(6)] for x in ptsi]

    def table(S):
        tab = {}
        for sz in (0, 1, 2):
            for D in itertools.combinations(range(7), sz):
                rest = [i for i in range(7) if i not in D]
                adj = []
                for i in rest:
                    v = 1
                    for j in D:
                        v = v * ((S[i] - S[j]) % q) % q
                    adj.append(v)
                nmom = len(rest) - 5
                lb = lagrange_basis([S[i] for i in rest[:5]], q)
                tab[D] = (rest, adj, nmom, lb)
        return tab

    ctx["tab0"] = table(pts0)
    ctx["tabi"] = table(ptsi)
    return ctx


def probe(ctx, p1, mask0, maski):
    """p1: 14 values; mask0/maski: tuples of positions where p1 vanishes."""
    q = ctx["q"]
    if len(mask0) > 2 or len(maski) > 2:
        # dim A <= 2 or dim B <= 2 : generically u = 0.  Cheap exact check.
        rows = [ctx["pw0"][i][:5] for i in mask0] + \
               [ctx["pwi"][i][:5] for i in maski]
        if len(mask0) <= 2:
            rows += mom_rows(ctx, 0, p1, mask0)
        if len(maski) <= 2:
            rows += mom_rows(ctx, 1, p1, maski)
        bas, rk = nullspace(rows, 5, q)
        return ("BIGOVL", len(bas)) if bas else None
    rows = [ctx["pw0"][i][:5] for i in mask0] + \
           [ctx["pwi"][i][:5] for i in maski]
    r0, c0, e0 = mom_rows(ctx, 0, p1, mask0, True)
    ri, ci, ei = mom_rows(ctx, 1, p1, maski, True)
    rows = rows + r0 + ri
    bas, rk = nullspace(rows, 5, q)
    if len(bas) != 1:
        return ("DIM", len(bas)) if len(bas) > 1 else None
    u = bas[0]
    G = interp(ctx, 0, u, e0, c0)
    if G is None:
        return None
    H = interp(ctx, 1, u, ei, ci)
    if H is None:
        return None
    if nullspace([u, G, H], 5, q)[1] > 2:
        return None
    # corrected (TEST): u must genuinely lie in span(G,H) with BOTH
    # coefficients nonzero and both reconstructed forms of degree 4.
    bas, rk = nullspace([[G[j], H[j], (-u[j]) % q] for j in range(5)], 3, q)
    for b in bas:
        if b[2]:
            iv = pow(b[2], q - 2, q)
            c1, c2 = b[0] * iv % q, b[1] * iv % q
            if c1 and c2:
                gg = ptrim([c1 * x % q for x in G])
                ff = ptrim([c2 * x % q for x in H])
                if pdeg(ff) == 4 and pdeg(gg) == 4:
                    return ("HIT", u, G, H)
            return ("DEGEN", 0)
    return ("DEGEN", 1)


def mom_rows(ctx, which, p1, mask, ret=False):
    q = ctx["q"]
    if which == 0:
        ent = ctx["tab0"][tuple(mask)]
        a, di, pw, off = ctx["a0"], ctx["d0i"], ctx["pw0"], 0
    else:
        ent = ctx["tabi"][tuple(mask)]
        a, di, pw, off = ctx["ai"], ctx["dii"], ctx["pwi"], 7
    rest, adj, nmom, lb = ent
    vals = [p1[off + i] for i in rest]
    n = len(vals)
    pre = [1] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] * vals[i] % q
    suf = [1] * (n + 1)
    for i in range(n - 1, -1, -1):
        suf[i] = suf[i + 1] * vals[i] % q
    c = [pre[i] * suf[i + 1] % q for i in range(n)]
    rows = []
    if nmom > 0:
        nm = nmom + 4
        m = [0] * nm
        for t in range(n):
            i = rest[t]
            w = a[i] * di[i] % q * adj[t] % q * c[t] % q
            pwr = pw[i]
            for j in range(nm):
                m[j] = (m[j] + w * pwr[j]) % q
        for r in range(nmom):
            rows.append(m[r:r + 5])
    if ret:
        return rows, c, ent
    return rows


def interp(ctx, which, u, ent, c):
    q = ctx["q"]
    rest, adj, nmom, lb = ent
    if which == 0:
        a, pw = ctx["a0"], ctx["pw0"]
    else:
        a, pw = ctx["ai"], ctx["pwi"]
    v = []
    for t in range(len(rest)):
        i = rest[t]
        pwr = pw[i]
        ux = (u[0] + u[1] * pwr[1] + u[2] * pwr[2] + u[3] * pwr[3]
              + u[4] * pwr[4]) % q
        v.append(a[i] * ux % q * c[t] % q)
    G = [0] * 5
    for t in range(5):
        tv = v[t]
        if tv:
            lbt = lb[t]
            G[0] = (G[0] + tv * lbt[0]) % q
            G[1] = (G[1] + tv * lbt[1]) % q
            G[2] = (G[2] + tv * lbt[2]) % q
            G[3] = (G[3] + tv * lbt[3]) % q
            G[4] = (G[4] + tv * lbt[4]) % q
    for t in range(5, len(rest)):
        i = rest[t]
        pwr = pw[i]
        ev = (G[0] + G[1] * pwr[1] + G[2] * pwr[2] + G[3] * pwr[3]
              + G[4] * pwr[4]) % q
        if ev != v[t]:
            return None
    return G


def reconstruct(ctx, S1pts, u, G, H):
    q = ctx["q"]
    bas, rk = nullspace([[G[j], H[j], (-u[j]) % q] for j in range(5)], 3, q)
    sol = None
    for b in bas:
        if b[2]:
            iv = pow(b[2], q - 2, q)
            sol = (b[0] * iv % q, b[1] * iv % q)
            break
    if sol is None:
        return None, "no(c1,c2)"
    c1, c2 = sol
    if c1 == 0 or c2 == 0:
        return None, "c1c2zero"
    g = ptrim([c1 * x % q for x in G])
    f = ptrim([c2 * x % q for x in H])
    if pdeg(f) != 4 or pdeg(g) != 4:
        return None, "degf=%d degg=%d" % (pdeg(f), pdeg(g))
    F = padd(f, g, q)
    P1 = from_roots(S1pts, q)
    gam = alp = None
    for i, x in enumerate(ctx["pts0"]):
        de = ctx["a0"][i] * peval(F, x, q) % q
        if de:
            gam = peval(P1, x, q) * peval(g, x, q) % q * pow(de, q - 2, q) % q
            break
    for i, x in enumerate(ctx["ptsi"]):
        de = ctx["ai"][i] * peval(F, x, q) % q
        if de:
            alp = peval(P1, x, q) * peval(f, x, q) % q * pow(de, q - 2, q) % q
            break
    if not gam or not alp:
        return None, "scales"
    Q0 = pscal(ctx["P0"], alp, q)
    Q2 = pscal(ctx["Pinf"], gam, q)
    Q1 = psub(P1, padd(Q0, Q2, q), q)
    num = padd(psub(pmul(Q0, pmul(g, g, q), q), pmul(Q1, pmul(f, g, q), q), q),
               pmul(Q2, pmul(f, f, q), q), q)
    L, rr = pdivmod(num[:], pmul(Q0, Q2, q), q)
    if rr:
        return None, "CONICnondiv"
    if pdeg(L) != 1:
        return None, "degL=%d" % pdeg(L)
    k, r1 = pdivmod(psub(pmul(f, f, q), pmul(L, Q0, q), q), g, q)
    if r1:
        return None, "k_nonpoly"
    h, r2 = pdivmod(psub(pmul(L, Q2, q), pmul(g, g, q), q), f, q)
    if r2:
        return None, "h_nonpoly"
    ch = [pmul(L, Q0, q) == psub(pmul(f, f, q), pmul(k, g, q), q),
          pmul(L, Q1, q) == padd(pmul(f, g, q), pmul(h, k, q), q),
          pmul(L, Q2, q) == padd(pmul(g, g, q), pmul(h, f, q), q),
          padd(padd(Q0, Q1, q), Q2, q) == P1]
    return {"f": f, "g": g, "h": h, "k": k, "L": L, "Q0": Q0, "Q1": Q1,
            "Q2": Q2, "alpha": alp, "gamma": gam, "checks": ch}, "ok"


def certify(obj, q, mu):
    """T over mu_32 with the full slope scan, plus structural functionals."""
    Q0, Q1, Q2, L = obj["Q0"], obj["Q1"], obj["Q2"], obj["L"]
    muset = set(mu)
    rep = {}
    rep["degQ"] = (pdeg(Q0), pdeg(Q1), pdeg(Q2))
    rep["degL"] = pdeg(L)
    rep["degfghk"] = (pdeg(obj["f"]), pdeg(obj["g"]), pdeg(obj["h"]),
                      pdeg(obj["k"]))
    rep["s"] = pdeg(pgcd(pgcd(Q0, Q1, q), Q2, q))
    supported = []
    rootsets = {}
    degz = {}
    Qzs = {}
    for z in list(range(q)) + ["inf"]:
        if z == "inf":
            Qz = Q2
        else:
            Qz = padd(Q0, padd(pscal(Q1, z, q), pscal(Q2, z * z % q, q), q), q)
        Qzs[z] = Qz
        degz[z] = pdeg(Qz)
        rr = [x for x in mu if peval(Qz, x, q) == 0]
        if len(rr) == 7 and pdeg(Qz) == 7:
            supported.append(z)
            rootsets[z] = set(rr)
    rep["T_mu32"] = len(supported)
    rep["supported"] = supported
    rep["rootsets"] = {z: sorted(rootsets[z]) for z in supported}
    uni = set()
    for z in supported:
        uni |= rootsets[z]
    rep["union"] = len(uni)
    rep["sum_dx"] = sum(len(rootsets[z]) for z in supported)
    ov = {}
    worst = 0
    for i in range(len(supported)):
        for j in range(i + 1, len(supported)):
            zi, zj = supported[i], supported[j]
            ov[(zi, zj)] = len(rootsets[zi] & rootsets[zj])
    if len(supported) >= 3:
        for kz in supported:
            others = [z for z in supported if z != kz]
            for a in range(len(others)):
                for b in range(a + 1, len(others)):
                    e1 = len(rootsets[kz] & rootsets[others[a]])
                    e2 = len(rootsets[kz] & rootsets[others[b]])
                    worst = max(worst, e1 + e2)
    rep["ov"] = ov
    rep["OV4worst"] = worst
    # a* under the PROJECTIVE ruling: |S_i u S_j| with roots at infinity
    # counted (deg Q_z < 7 contributes 7-deg roots at infinity).
    astars = []
    for i in range(len(supported)):
        for j in range(i + 1, len(supported)):
            zi, zj = supported[i], supported[j]
            astars.append(14 - len(rootsets[zi] & rootsets[zj]))
    rep["astar_pairs"] = sorted(astars)
    rep["astar"] = min(astars) if astars else None
    rep["deg_drop_slopes"] = [z for z in degz if degz[z] < 7]
    # a* over ALL slope pairs, projective ruling vs affine reading
    sl = list(range(q)) + ["inf"]
    hp = {}
    ha = {}
    for i in range(len(sl)):
        A = Qzs[sl[i]]
        for j in range(i + 1, len(sl)):
            B = Qzs[sl[j]]
            dg = pdeg(pgcd(A, B, q))
            vaff = 14 - dg
            vproj = 14 - (dg + min(7 - pdeg(A), 7 - pdeg(B)))
            ha[vaff] = ha.get(vaff, 0) + 1
            hp[vproj] = hp.get(vproj, 0) + 1
    rep["astar_all_proj_min"] = min(hp)
    rep["astar_all_affine_min"] = min(ha)
    rep["astar_all_proj_hist"] = sorted(hp.items())
    return rep


def main():
    q = int(sys.argv[1])
    seed = int(sys.argv[2])
    budget = float(sys.argv[3])
    skip = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    t00 = time.time()
    mu = mu32(q)
    assert len(mu) == 32, len(mu)
    rnd = random.Random(seed)
    i0 = sorted(rnd.sample(range(32), 7))
    iinf = sorted(rnd.sample([i for i in range(32) if i not in i0], 7))
    ctx = build_pair(q, mu, i0, iinf)
    out("")
    out("=== RUN d2_sweep q=%d seed=%d budget=%.0fs skip=%d %s ==="
        % (q, seed, budget, skip, time.strftime("%Y-%m-%d %H:%M:%S")))
    out("mu_32[0:5]=%s ... ; S_0=%s ; S_inf=%s"
        % (mu[:5], ctx["pts0"], ctx["ptsi"]))
    pos0 = {}
    posi = {}
    for t, i in enumerate(i0):
        pos0[i] = t
    for t, i in enumerate(iinf):
        posi[i] = t
    allpts = ctx["pts0"] + ctx["ptsi"]
    col = [[(allpts[i] - mu[e]) % q for i in range(14)] for e in range(32)]
    lvl = [None] * 8
    lvl[0] = [1] * 14
    m0lvl = [()] * 8
    milvl = [()] * 8
    prev = None
    n = 0
    hits = []
    tags = {}
    t0 = time.time()
    stop = False
    for cb in itertools.combinations(range(32), 7):
        n += 1
        if n <= skip:
            prev = cb
            continue
        d = 0
        if prev is not None:
            while d < 7 and cb[d] == prev[d]:
                d += 1
        for t in range(d, 7):
            e = cb[t]
            pv = lvl[t]
            cl = col[e]
            lvl[t + 1] = [pv[i] * cl[i] % q for i in range(14)]
            m0lvl[t + 1] = m0lvl[t] + ((pos0[e],) if e in pos0 else ())
            milvl[t + 1] = milvl[t] + ((posi[e],) if e in posi else ())
        prev = cb
        r = probe(ctx, lvl[7], tuple(sorted(m0lvl[7])),
                  tuple(sorted(milvl[7])))
        if r is not None:
            if r[0] == "HIT":
                hits.append((cb, r[1], r[2], r[3]))
                out("  HIT at combination #%d  S_1=%s"
                    % (n, [mu[e] for e in cb]))
            else:
                tags[r[0] + str(r[1])] = tags.get(r[0] + str(r[1]), 0) + 1
        if (n & 0xFFFF) == 0 and time.time() - t0 > budget:
            stop = True
            break
    el = time.time() - t0
    out("swept %d of 3365856 combinations in %.1fs (%.1f us/triple)%s"
        % (n - skip, el, 1e6 * el / max(1, n - skip),
           "  [BUDGET STOP at n=%d]" % n if stop else "  [COMPLETE]"))
    out("degenerate branch tags: %s" % sorted(tags.items()))
    out("hits: %d" % len(hits))
    for cb, u, G, H in hits:
        S1pts = [mu[e] for e in cb]
        obj, why = reconstruct(ctx, S1pts, u, G, H)
        if obj is None:
            out("  RECON FAIL %s : %s" % (S1pts, why))
            continue
        rep = certify(obj, q, mu)
        out("  --- CERTIFIED WITNESS ---")
        out("  S_0=%s" % ctx["pts0"])
        out("  S_inf=%s" % ctx["ptsi"])
        out("  S_1=%s" % S1pts)
        out("  f=%s g=%s h=%s k=%s L=%s alpha=%d gamma=%d"
            % (obj["f"], obj["g"], obj["h"], obj["k"], obj["L"],
               obj["alpha"], obj["gamma"]))
        out("  Q0=%s" % obj["Q0"])
        out("  Q1=%s" % obj["Q1"])
        out("  Q2=%s" % obj["Q2"])
        out("  PAR identity checks (LQ0,LQ1,LQ2,member1=P_1): %s"
            % obj["checks"])
        out("  cert: %s" % {kk: rep[kk] for kk in
                            ("degQ", "degL", "degfghk", "s", "T_mu32",
                             "supported", "union", "sum_dx", "OV4worst",
                             "astar_pairs", "astar", "deg_drop_slopes")})
        out("  rootsets: %s" % rep["rootsets"])
        out("  pairwise overlaps: %s" % rep["ov"])
    out("=== END d2_sweep wall=%.1fs ===" % (time.time() - t00))


main()
FH.close()
