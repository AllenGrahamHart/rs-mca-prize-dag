"""r35_l2_gate D2 -- THE CONSTRUCTIVE ATTACK (pre-registered route D-F).

Invert the m=2 (L2) system: choose the SYZYGY DATA first, read the
curve off it, pay only ONE determinant condition.

D-B (verified in d1_results.txt) says the system M(Z)Q_Z = 0 has a
nonzero solution iff there are f,g of degree <= 4, not both zero, with
    Q_2 f == Q_1 g  (mod Q_0)      and     Q_1 f == Q_0 g  (mod Q_2).
Clearing the congruences with quotients h,k (degree <= 4 automatically):
    E1:  Q_2 f - Q_1 g - Q_0 h = 0        (12 coefficient equations)
    E2:  Q_1 f - Q_0 g - Q_2 k = 0        (12 coefficient equations)
Bilinear in A = (Q_0,Q_1,Q_2) [24 unknowns] and B = (f,g,h,k) [20].
For FIXED B this is a SQUARE 24x24 homogeneous system in A, so a curve
exists iff det M(B) = 0 -- ONE condition on a 19-dim projective
B-space, i.e. hit rate ~1/q, versus q^-5 for a blind curve search.

Every hit is then certified from scratch against the ORIGINAL 36x32
system, never through the reduction.
"""
import random

LINES = []


def P(s=""):
    LINES.append(str(s))


def rref(M, p):
    rows = [r[:] for r in M]
    nr = len(rows)
    nc = len(rows[0]) if nr else 0
    r = 0
    piv = []
    for c in range(nc):
        pr = -1
        for i in range(r, nr):
            if rows[i][c] % p:
                pr = i
                break
        if pr < 0:
            continue
        rows[r], rows[pr] = rows[pr], rows[r]
        inv = pow(rows[r][c], p - 2, p)
        rows[r] = [(v * inv) % p for v in rows[r]]
        for i in range(nr):
            if i != r and rows[i][c]:
                f = rows[i][c]
                rr, ri = rows[r], rows[i]
                rows[i] = [(ri[j] - f * rr[j]) % p for j in range(nc)]
        piv.append(c)
        r += 1
        if r == nr:
            break
    return r, rows, piv


def rank(M, p):
    return rref(M, p)[0] if M else 0


def nullspace(M, p, nc):
    if not M:
        return [[1 if i == j else 0 for j in range(nc)] for i in range(nc)]
    r, rows, piv = rref(M, p)
    ps = set(piv)
    out = []
    for fc in range(nc):
        if fc in ps:
            continue
        v = [0] * nc
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-rows[i][fc]) % p
        out.append(v)
    return out


def det(M, p):
    n = len(M)
    rows = [r[:] for r in M]
    d = 1
    for c in range(n):
        pr = -1
        for i in range(c, n):
            if rows[i][c] % p:
                pr = i
                break
        if pr < 0:
            return 0
        if pr != c:
            rows[c], rows[pr] = rows[pr], rows[c]
            d = (-d) % p
        d = (d * rows[c][c]) % p
        inv = pow(rows[c][c], p - 2, p)
        rows[c] = [(v * inv) % p for v in rows[c]]
        for i in range(c + 1, n):
            f = rows[i][c]
            if f:
                rc, ri = rows[c], rows[i]
                rows[i] = [(ri[j] - f * rc[j]) % p for j in range(n)]
    return d % p


def ptrim(a, p):
    a = [x % p for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b, p):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                r[i + j] = (r[i + j] + ai * bj) % p
    return ptrim(r, p)


def padd(a, b, p):
    n = max(len(a), len(b))
    r = [0] * n
    for i, x in enumerate(a):
        r[i] = (r[i] + x) % p
    for i, x in enumerate(b):
        r[i] = (r[i] + x) % p
    return ptrim(r, p)


def pmod(a, m, p):
    a = ptrim(a[:], p)
    m = ptrim(m[:], p)
    dm = len(m) - 1
    inv = pow(m[-1], p - 2, p)
    while a and len(a) - 1 >= dm:
        sh = len(a) - 1 - dm
        f = (a[-1] * inv) % p
        for i in range(len(m)):
            a[sh + i] = (a[sh + i] - f * m[i]) % p
        a = ptrim(a, p)
    return a


def pgcd(a, b, p):
    a = ptrim(a[:], p)
    b = ptrim(b[:], p)
    while b:
        a, b = b, pmod(a, b, p)
    if a:
        inv = pow(a[-1], p - 2, p)
        a = [(x * inv) % p for x in a]
    return a


def pderiv(a, p):
    return ptrim([(i * a[i]) % p for i in range(1, len(a))], p)


def peval(a, x, p):
    v = 0
    for c in reversed(a):
        v = (v * x + c) % p
    return v


def pad(a, n):
    return (list(a) + [0] * n)[:n]


def sys_36x32(Q, p):
    Q0, Q1, Q2 = [pad(q, 8) for q in Q]
    QL = [Q0, Q1, Q2]
    M = []
    for k in range(4):
        for a in range(9):
            row = [0] * 32
            if k <= 2:
                for b in range(8):
                    row[a + b] = (row[a + b] + QL[k][b]) % p
            if k >= 1:
                for b in range(8):
                    row[16 + a + b] = (row[16 + a + b] + QL[k - 1][b]) % p
            M.append(row)
    return M


def hankel(y, p):
    return [[y[a + b] % p for b in range(8)] for a in range(9)]


def build_MB(B, p):
    """24x24 matrix of A=(Q_0,Q_1,Q_2) |-> (E1 coeffs, E2 coeffs)."""
    f, g, h, k = [pad(b, 5) for b in B]
    nf = [(-x) % p for x in f]
    ng = [(-x) % p for x in g]
    nh = [(-x) % p for x in h]
    nk = [(-x) % p for x in k]
    # E1 : Q_0*(-h) + Q_1*(-g) + Q_2*(f)
    e1 = [nh, ng, f]
    # E2 : Q_0*(-g) + Q_1*(f) + Q_2*(-k)
    e2 = [ng, f, nk]
    M = [[0] * 24 for _ in range(24)]
    for j in range(3):
        for i in range(8):
            col = 8 * j + i
            for t in range(5):
                M[i + t][col] = e1[j][t] % p
                M[12 + i + t][col] = e2[j][t] % p
    return M


def certify(Q, p, D, verbose_lines):
    """Full certification of a candidate curve Q against the ORIGINAL system."""
    Q0, Q1, Q2 = [ptrim(list(q), p) for q in Q]
    rep = {}
    rep["degs"] = (len(Q0) - 1, len(Q1) - 1, len(Q2) - 1)
    if len(Q0) != 8 or len(Q2) != 8:
        rep["fail"] = "deg Q_0 or deg Q_2 != 7 (leading parameter coefficient"\
                      " is not a degree-rho locator)"
        return rep
    s = pgcd(pgcd(Q0, Q1, p), Q2, p)
    rep["s"] = len(s) - 1
    if len(s) > 1:
        rep["fail"] = "s != 0 (common domain factor) -- (SAT1) forbids"
        return rep
    # linear independence of Q_0,Q_1,Q_2  (RNC2 / separation rank m+1 = 3)
    rep["seprank"] = rank([pad(Q0, 8), pad(Q1, 8), pad(Q2, 8)], p)
    if rep["seprank"] != 3:
        rep["fail"] = "Q_0,Q_1,Q_2 dependent: nu_Q is not a degree-2 RNC"
        return rep
    M = sys_36x32([Q0, Q1, Q2], p)
    ns = nullspace(M, p, 32)
    rep["nullity36"] = len(ns)
    if not ns:
        rep["fail"] = "no syndrome pencil (nullity 0)"
        return rep
    # pick a solution; if nullity > 1 try each basis vector + a few combos
    cands = list(ns)
    if len(ns) > 1:
        rng2 = random.Random(7)
        for _ in range(8):
            v = [0] * 32
            for b in ns:
                c = rng2.randrange(p)
                v = [(v[i] + c * b[i]) % p for i in range(32)]
            cands.append(v)
    best = None
    for v in cands:
        y0, y1 = v[:16], v[16:]
        if not any(y0) and not any(y1):
            continue
        gr = 0
        for z in range(min(p, 40)):
            yz = [(y0[i] + z * y1[i]) % p for i in range(16)]
            gr = max(gr, rank(hankel(yz, p), p))
        gr = max(gr, rank(hankel(y1, p), p))
        if best is None or gr > best[0]:
            best = (gr, y0, y1)
    rep["generic_rank"] = best[0]
    y0, y1 = best[1], best[2]
    rep["y0"] = y0
    rep["y1"] = y1
    if best[0] != 7:
        rep["fail"] = "generic rank %d != rho = 7" % best[0]
        return rep
    # INDEPENDENT re-verification of M(Z)Q_Z = 0, entrywise, from scratch
    H0, H1 = hankel(y0, p), hankel(y1, p)
    QL = [pad(Q0, 8), pad(Q1, 8), pad(Q2, 8)]
    ok = True
    for kk in range(4):
        for a in range(9):
            tot = 0
            if kk <= 2:
                tot += sum(H0[a][b] * QL[kk][b] for b in range(8))
            if kk >= 1:
                tot += sum(H1[a][b] * QL[kk - 1][b] for b in range(8))
            if tot % p:
                ok = False
    rep["direct_check"] = ok
    # minimal index: is there a kernel vector of parameter degree <= 1 ?
    #   M(Z)(P_0 + Z P_1) = 0  ->  3 blocks of 9 rows on 16 unknowns
    M2 = []
    for kk in range(3):
        for a in range(9):
            row = [0] * 16
            if kk <= 1:
                for b in range(8):
                    row[b] = (row[b] + (H0[a][b] if kk == 0 else 0)) % p
            M2.append(row)
    M2 = []
    for kk in range(3):
        for a in range(9):
            row = [0] * 16
            # coefficient of Z^kk in (H0 + Z H1)(P_0 + Z P_1)
            if kk == 0:
                for b in range(8):
                    row[b] = H0[a][b]
            elif kk == 1:
                for b in range(8):
                    row[b] = H1[a][b]
                    row[8 + b] = H0[a][b]
            else:
                for b in range(8):
                    row[8 + b] = H1[a][b]
            M2.append(row)
    rep["deg_le_1_kernel"] = 16 - rank(M2, p)
    rep["e"] = 2 if rep["deg_le_1_kernel"] == 0 else "<=1"
    # rank-drop divisor (banked (MI1)/my D-D: e=2 forces delta = 1)
    drops = []
    for z in range(p):
        yz = [(y0[i] + z * y1[i]) % p for i in range(16)]
        if rank(hankel(yz, p), p) < 7:
            drops.append(z)
    inf_drop = rank(hankel(y1, p), p) < 7
    rep["rank_drop_finite"] = drops
    rep["rank_drop_infinity"] = inf_drop
    # T and a* over the domain D
    Dset = set(D)
    Tsplit = 0
    nroots_max = 0
    locs = {}
    for z in range(p):
        Qz = ptrim([(Q0[i] + z * Q1[i] + z * z * Q2[i]) % p
                    for i in range(8)], p)
        locs[z] = Qz
        if len(Qz) != 8:
            continue
        if len(pgcd(Qz, pderiv(Qz, p), p)) > 1:
            continue
        rts = [x for x in Dset if peval(Qz, x, p) == 0]
        nroots_max = max(nroots_max, len(rts))
        if len(rts) == 7:
            Tsplit += 1
    rep["T_split_over_mu32"] = Tsplit
    rep["max_roots_in_D"] = nroots_max
    mx = 0
    for z in range(p):
        for w in range(z + 1, p):
            d = len(pgcd(locs[z], locs[w], p)) - 1
            if d > mx:
                mx = d
    rep["max_shared_roots"] = mx
    rep["a_star"] = 14 - mx
    rep["fail"] = None
    return rep


def main():
    for p in (97, 193):
        rng = random.Random(20260811 + p)
        # multiplicative domain D = mu_32
        gg = 2
        while pow(gg, (p - 1) // 2, p) == 1 or pow(gg, (p - 1) // 3, p) == 1:
            gg += 1
        w = pow(gg, (p - 1) // 32, p)
        D = sorted({pow(w, i, p) for i in range(32)})
        P("=" * 70)
        P("FIELD q = %d      domain D = mu_32, |D| = %d" % (p, len(D)))
        P("=" * 70)
        # is det M(B) generically nonzero?  (D-F falsifier)
        nz = 0
        for _ in range(30):
            B = [[rng.randrange(p) for _ in range(5)] for _ in range(4)]
            if det(build_MB(B, p), p):
                nz += 1
        P("[D-F] det M(B) nonzero on %d/30 random B  =>  the determinant is"
          " NOT identically zero" % nz)
        if nz == 0:
            P("      D-F FALSIFIER FIRED: route vacuous.")
            continue
        hits = 0
        draws = 0
        certified = []
        rejected = {}
        while draws < 1600 and len(certified) < 3:
            draws += 1
            B = [[rng.randrange(p) for _ in range(5)] for _ in range(4)]
            MB = build_MB(B, p)
            if det(MB, p) != 0:
                continue
            hits += 1
            ker = nullspace(MB, p, 24)
            trial = list(ker)
            if len(ker) > 1:
                for _ in range(6):
                    v = [0] * 24
                    for b in ker:
                        c = rng.randrange(p)
                        v = [(v[i] + c * b[i]) % p for i in range(24)]
                    trial.append(v)
            for v in trial:
                Q = [v[0:8], v[8:16], v[16:24]]
                if not any(v):
                    continue
                rep = certify(Q, p, D, LINES)
                if rep.get("fail") is None:
                    certified.append((B, Q, rep))
                    break
                key = rep["fail"]
                rejected[key] = rejected.get(key, 0) + 1
        P("[D-F] %d random B draws -> %d with det M(B) = 0  (rate %.4f,"
          " predicted ~1/q = %.4f)" % (draws, hits, hits / max(draws, 1),
                                       1.0 / p))
        P("      rejection reasons among kernel curves: %s" % rejected)
        P("      FULLY CERTIFIED (SAT1)-profile objects: %d" % len(certified))
        for (B, Q, rep) in certified:
            P("")
            P("  ---- WITNESS (q = %d) ----" % p)
            P("  f = %s" % pad(B[0], 5))
            P("  g = %s" % pad(B[1], 5))
            P("  h = %s" % pad(B[2], 5))
            P("  k = %s" % pad(B[3], 5))
            P("  Q_0 = %s" % pad(Q[0], 8))
            P("  Q_1 = %s" % pad(Q[1], 8))
            P("  Q_2 = %s" % pad(Q[2], 8))
            P("  y_0 = %s" % rep["y0"])
            P("  y_1 = %s" % rep["y1"])
            P("  deg(Q_0,Q_1,Q_2)      = %s" % (rep["degs"],))
            P("  separation rank       = %d   (m+1 = 3 required, RNC2)"
              % rep["seprank"])
            P("  s (common factor deg) = %d   ((SAT1) requires 0)" % rep["s"])
            P("  nullity(36x32)        = %d" % rep["nullity36"])
            P("  generic rank of M(Z)  = %d   (rho = 4m-1 = 7 required)"
              % rep["generic_rank"])
            P("  M(Z)Q_Z = 0 rechecked entrywise from scratch: %s"
              % rep["direct_check"])
            P("  kernel vectors of parameter degree <= 1 : %d"
              % rep["deg_le_1_kernel"])
            P("  ==> minimal index e   = %s   (e = m = 2 is the target)"
              % rep["e"])
            P("  finite rank-drop parameters: %s ; drop at infinity: %s"
              % (rep["rank_drop_finite"], rep["rank_drop_infinity"]))
            P("  T (parameters whose locator splits with 7 roots in mu_32)"
              " = %d" % rep["T_split_over_mu32"])
            P("  max roots of a locator inside mu_32 = %d"
              % rep["max_roots_in_D"])
            P("  max shared roots between two locators = %d"
              % rep["max_shared_roots"])
            P("  a* = w* = min_{g!=g'} |S_g u S_g'| = %d   (7m-1 = 13)"
              % rep["a_star"])

    with open("notes/pilots_20260811/r35_l2_gate/d2_results.txt", "w") as fh:
        fh.write("\n".join(LINES) + "\n")
    print("\n".join(LINES))


main()
