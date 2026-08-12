"""r38_cauchy_lattice D3 - from-scratch re-certification of the six
T=3-over-mu_32 witnesses, plus a* under the RULED projective convention.

Rebuilds each object from its (f,g,h,k,L) alone (the Q_j are recomputed,
not copied), re-derives every functional, and measures a* both over
SUPPORTED pairs and over ALL slope pairs, projective vs affine.
Also closes the loop with D1: each witness must be a first-minimum drop
of the rank-2 lattice {(f,g) : f = R g mod P_0 P_inf}.

Stdlib only; append-mode results; helpers duplicated per file.
"""
import time

RES = "notes/pilots_20260811/r38_cauchy_lattice/d3_results.txt"
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


def mu32(q):
    return sorted([x for x in range(1, q) if pow(x, 32, q) == 1])


def euclid_min(R, P, q):
    rp, rc = P[:], R[:]
    vp, vc = [], [1]
    best = 99
    rdegs = [pdeg(rp), pdeg(rc)]
    while rc:
        best = min(best, max(pdeg(rc), pdeg(vc)))
        qq, rr = pdivmod(rp[:], rc, q)
        vn = psub(vp, pmul(qq, vc, q), q)
        rp, rc = rc, rr
        vp, vc = vc, vn
        rdegs.append(pdeg(rc))
    return best, rdegs


W = [
    dict(tag="q97-p0-w1", q=97, S0=[8, 28, 45, 50, 70, 79, 96],
         Sinf=[27, 34, 46, 47, 55, 67, 89], S1=[1, 20, 33, 42, 45, 67, 78],
         f=[62, 36, 59, 38, 41], g=[28, 46, 63, 42, 57],
         h=[70, 50, 64, 47, 75], k=[30, 72, 86, 96], L=[52, 60]),
    dict(tag="q97-p0-w2", q=97, S0=[8, 28, 45, 50, 70, 79, 96],
         Sinf=[27, 34, 46, 47, 55, 67, 89], S1=[8, 18, 19, 42, 67, 69, 96],
         f=[82, 87, 1, 41, 95], g=[62, 56, 0, 59, 3],
         h=[18, 9, 47, 41, 37], k=[61, 93, 24, 49, 7], L=[4, 74]),
    dict(tag="q97-p0-w3", q=97, S0=[8, 28, 45, 50, 70, 79, 96],
         Sinf=[27, 34, 46, 47, 55, 67, 89], S1=[18, 27, 63, 69, 78, 79, 89],
         f=[72, 65, 38, 55, 35], g=[11, 66, 57, 67, 63],
         h=[90, 54, 67, 56, 83], k=[49, 38, 35, 2, 80], L=[47, 70]),
    dict(tag="q97-p1-w4", q=97, S0=[12, 28, 52, 70, 75, 78, 96],
         Sinf=[19, 27, 46, 50, 51, 69, 85], S1=[1, 19, 34, 64, 67, 75, 96],
         f=[32, 71, 44, 37, 14], g=[42, 82, 42, 68, 84],
         h=[56, 69, 75, 1, 3], k=[81, 22, 11, 78, 26], L=[4, 59]),
    dict(tag="q97-p1-w5", q=97, S0=[12, 28, 52, 70, 75, 78, 96],
         Sinf=[19, 27, 46, 50, 51, 69, 85], S1=[18, 34, 51, 77, 78, 85, 89],
         f=[22, 82, 48, 11, 40], g=[64, 79, 40, 57, 58],
         h=[86, 79, 52, 25, 32], k=[24, 93, 51, 5, 8], L=[61, 14]),
    dict(tag="q97-p1-w6", q=97, S0=[12, 28, 52, 70, 75, 78, 96],
         Sinf=[19, 27, 46, 50, 51, 69, 85], S1=[42, 45, 46, 47, 69, 70, 79],
         f=[50, 41, 33, 74, 64], g=[54, 72, 91, 92, 34],
         h=[76, 46, 17, 58, 55], k=[65, 25, 43, 29, 66], L=[68, 15]),
]


def analyse(w, extra=None):
    q = w["q"]
    f, g, h, k, L = w["f"], w["g"], w["h"], w["k"], w["L"]
    mu = mu32(q)
    rep = {}
    n0 = psub(pmul(f, f, q), pmul(k, g, q), q)
    n1 = padd(pmul(f, g, q), pmul(h, k, q), q)
    n2 = padd(pmul(g, g, q), pmul(h, f, q), q)
    Q = []
    for nu in (n0, n1, n2):
        qq, rr = pdivmod(nu[:], L, q)
        if rr:
            return {"FATAL": "L does not divide a (PAR) numerator"}
        Q.append(qq)
    Q0, Q1, Q2 = Q
    rep["degfghkL"] = (pdeg(f), pdeg(g), pdeg(h), pdeg(k), pdeg(L))
    rep["degQ"] = (pdeg(Q0), pdeg(Q1), pdeg(Q2))
    rep["s"] = pdeg(pgcd(pgcd(Q0, Q1, q), Q2, q))
    rep["deggcd_fg"] = pdeg(pgcd(f, g, q))
    conic = padd(psub(pmul(Q0, pmul(g, g, q), q), pmul(Q1, pmul(f, g, q), q),
                      q), pmul(Q2, pmul(f, f, q), q), q)
    rep["CONIC"] = (conic == pmul(L, pmul(Q0, Q2, q), q))
    slopes = list(range(q)) + ["inf"]
    Qz = {}
    for z in slopes:
        Qz[z] = Q2 if z == "inf" else padd(
            Q0, padd(pscal(Q1, z, q), pscal(Q2, z * z % q, q), q), q)
    sup = []
    rs = {}
    for z in slopes:
        if pdeg(Qz[z]) != 7:
            continue
        rr = [x for x in mu if peval(Qz[z], x, q) == 0]
        if len(rr) == 7:
            sup.append(z)
            rs[z] = set(rr)
    rep["T_mu32"] = len(sup)
    rep["supported"] = sup
    rep["rootsets"] = {z: sorted(rs[z]) for z in sup}
    rep["match_prescribed"] = (rs.get(0) == set(w["S0"]) and
                               rs.get("inf") == set(w["Sinf"]) and
                               rs.get(1) == set(w["S1"]))
    uni = set()
    for z in sup:
        uni |= rs[z]
    rep["union"] = len(uni)
    rep["sum_dx"] = sum(len(rs[z]) for z in sup)
    rep["2union"] = 2 * len(uni)
    ovs = {}
    ast = []
    for i in range(len(sup)):
        for j in range(i + 1, len(sup)):
            e = len(rs[sup[i]] & rs[sup[j]])
            ovs[(sup[i], sup[j])] = e
            ast.append(14 - e)
    rep["pair_overlaps"] = ovs
    rep["astar_sup_pairs"] = sorted(ast)
    rep["astar_sup"] = min(ast) if ast else None
    worst = 0
    for kz in sup:
        oth = [z for z in sup if z != kz]
        for a in range(len(oth)):
            for b in range(a + 1, len(oth)):
                worst = max(worst,
                            len(rs[kz] & rs[oth[a]]) + len(rs[kz] & rs[oth[b]]))
    rep["OV4_worst_e(k,i)+e(k,j)"] = worst
    m = 0
    for z in range(q):
        fz = padd(f, pscal(g, z, q), q)
        m = max(m, len([x for x in set(w["S0"]) | set(w["Sinf"])
                        if peval(fz, x, q) == 0]))
    rep["OV4_max_roots(f+zg)_in_S0uSinf"] = m
    lead = [Q0[7] if len(Q0) == 8 else 0, Q1[7] if len(Q1) == 8 else 0,
            Q2[7] if len(Q2) == 8 else 0]
    rep["lead_quadratic"] = lead
    rep["deg_drop_slopes"] = [z for z in slopes if pdeg(Qz[z]) < 7]
    hp = {}
    ha = {}
    for i in range(len(slopes)):
        A = Qz[slopes[i]]
        for j in range(i + 1, len(slopes)):
            B = Qz[slopes[j]]
            dg = pdeg(pgcd(A, B, q))
            va = 14 - dg
            vp = 14 - (dg + min(7 - pdeg(A), 7 - pdeg(B)))
            ha[va] = ha.get(va, 0) + 1
            hp[vp] = hp.get(vp, 0) + 1
    rep["astar_all_proj_min"] = min(hp)
    rep["astar_all_affine_min"] = min(ha)
    rep["astar_all_proj_hist"] = sorted(hp.items())
    rep["astar_all_affine_hist"] = sorted(ha.items())
    # D1 loop-closure: the lattice first minimum must drop to <= 4
    P0 = from_roots(w["S0"], q)
    Pinf = from_roots(w["Sinf"], q)
    P = pmul(P0, Pinf, q)
    pts = list(w["S0"]) + list(w["Sinf"])
    vals = []
    ok = True
    for x in w["S0"]:
        d = peval(Q2, x, q)
        if d == 0 or peval(g, x, q) == 0:
            ok = False
            break
        vals.append(peval(Q1, x, q) * pow(d, q - 2, q) % q)
    if ok:
        for x in w["Sinf"]:
            d = peval(Q1, x, q)
            if d == 0 or peval(g, x, q) == 0:
                ok = False
                break
            vals.append(peval(Q0, x, q) * pow(d, q - 2, q) % q)
    if ok:
        R = [0]
        for i, x in enumerate(pts):
            num = [1]
            den = 1
            for j, y in enumerate(pts):
                if j != i:
                    num = pmul(num, [(-y) % q, 1], q)
                    den = den * ((x - y) % q) % q
            R = padd(R, pscal(num, vals[i] * pow(den, q - 2, q) % q, q), q)
        _, res = pdivmod(psub(f, pmul(R, g, q), q), P, q)
        d1, rdegs = euclid_min(R, P, q)
        rep["f==Rg mod P0Pinf"] = (res == [])
        rep["lattice_d1"] = d1
        rep["remainder_degrees"] = rdegs
        rep["window_5_9_skipped"] = all(not (5 <= dd <= 9)
                                        for dd in rdegs[1:] if dd >= 0)
    else:
        rep["lattice"] = "degenerate value (g or a member vanishes)"
    return rep


def main():
    t0 = time.time()
    out("")
    out("=== RUN d3_astar %s ===" % time.strftime("%Y-%m-%d %H:%M:%S"))
    out("Re-certifies each witness from (f,g,h,k,L) ALONE; Q_j recomputed.")
    astar_sup_all = []
    astar_all_proj = []
    astar_all_aff = []
    for w in W:
        rep = analyse(w)
        out("--- %s ---" % w["tag"])
        for kk in ("degfghkL", "degQ", "s", "deggcd_fg", "CONIC", "T_mu32",
                   "supported", "match_prescribed", "union", "sum_dx",
                   "2union", "pair_overlaps", "astar_sup_pairs", "astar_sup",
                   "OV4_worst_e(k,i)+e(k,j)", "OV4_max_roots(f+zg)_in_S0uSinf",
                   "lead_quadratic", "deg_drop_slopes", "astar_all_proj_min",
                   "astar_all_affine_min", "astar_all_proj_hist",
                   "astar_all_affine_hist", "f==Rg mod P0Pinf", "lattice_d1",
                   "remainder_degrees", "window_5_9_skipped", "lattice",
                   "FATAL"):
            if kk in rep:
                out("   %-34s %s" % (kk, rep[kk]))
        if rep.get("astar_sup") is not None:
            astar_sup_all.extend(rep["astar_sup_pairs"])
            astar_all_proj.append(rep["astar_all_proj_min"])
            astar_all_aff.append(rep["astar_all_affine_min"])
    hist = {}
    for a in astar_sup_all:
        hist[a] = hist.get(a, 0) + 1
    out("")
    out("D3 SUMMARY over %d witnesses (%d supported pairs):" %
        (len(W), len(astar_sup_all)))
    out("  a* per SUPPORTED pair, projective ruling, histogram: %s"
        % sorted(hist.items()))
    out("  7m-1 = 13 ; #pairs with a* > 13: %d ; = 13: %d ; < 13: %d"
        % (sum(v for a, v in hist.items() if a > 13),
           hist.get(13, 0), sum(v for a, v in hist.items() if a < 13)))
    out("  per-object a* (min over supported pairs): %s"
        % [min(analyse(w)["astar_sup_pairs"]) for w in W])
    out("  a* over ALL slope pairs, projective min per object: %s"
        % astar_all_proj)
    out("  a* over ALL slope pairs, affine min per object:     %s"
        % astar_all_aff)
    out("=== END d3_astar wall=%.1fs ===" % (time.time() - t0))


main()
FH.close()
