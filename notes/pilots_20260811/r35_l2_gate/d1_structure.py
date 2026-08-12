"""r35_l2_gate D1 -- the m=2 (L2) stratum as an exact object.

Tests the PRE-REGISTERED derivations D-A, D-B, D-C, D-E (PREREG.md,
"Pilot registrations").  Stdlib only.  Run under tools/ramguard.

m = 2:  rho = 7, N = 32, R = 16, r = 7, A = R+1-2rho = 3, e = m = 2.
M(Z) = M_r(y_0) + Z M_r(y_1),  M_r(y)[a][b] = y[a+b],  9 x 8,
y_i in F^16.  Q_Z = Q_0 + Z Q_1 + Z^2 Q_2, deg Q_j <= 7.
M(Z)Q_Z = 0  <=>  four 9-row blocks on 32 unknowns.
"""
import random

LINES = []


def P(s=""):
    LINES.append(str(s))


# ---------- linear algebra over F_p ----------
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
    basis = []
    for fc in range(nc):
        if fc in ps:
            continue
        v = [0] * nc
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-rows[i][fc]) % p
        basis.append(v)
    return basis


# ---------- polynomials over F_p, low-to-high ----------
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


def pneg(a, p):
    return [(-x) % p for x in a]


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


def pad(a, n):
    return (list(a) + [0] * n)[:n]


def squarefree(a, p):
    return len(pgcd(a, pderiv(a, p), p)) <= 1


# ---------- the two systems ----------
def sys_36x32(Q, p):
    """M(Z)Q_Z = 0 as 36 rows on (y_0[0..15], y_1[0..15])."""
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


def phi_14x10(Q, p):
    """(f,g) deg<=4  |->  (Q2 f - Q1 g mod Q0, Q1 f - Q0 g mod Q2)."""
    Q0, Q1, Q2 = [ptrim(list(q), p) for q in Q]
    cols = []
    for i in range(5):
        e = [0] * i + [1]
        cols.append(pad(pmod(pmul(Q2, e, p), Q0, p), 7)
                    + pad(pmod(pmul(Q1, e, p), Q2, p), 7))
    for i in range(5):
        e = [0] * i + [1]
        cols.append(pad(pmod(pmul(pneg(Q1, p), e, p), Q0, p), 7)
                    + pad(pmod(pmul(pneg(Q0, p), e, p), Q2, p), 7))
    return [[cols[j][i] for j in range(10)] for i in range(14)]


def rand_poly(deg, p, rng, monic_deg=True):
    a = [rng.randrange(p) for _ in range(deg + 1)]
    if monic_deg:
        while a[deg] == 0:
            a[deg] = rng.randrange(p)
    return a


def main():
    for p in (97, 193):
        rng = random.Random(1000 + p)
        P("=" * 68)
        P("FIELD q = %d" % p)
        P("=" * 68)

        # ---- D-A : blocks 0 and 3 have rank exactly 9 ----
        bad = 0
        ranks = {}
        for _ in range(40):
            Q0 = rand_poly(7, p, rng)
            M = []
            for a in range(9):
                row = [0] * 16
                for b in range(8):
                    row[a + b] = Q0[b]
                M.append(row)
            r = rank(M, p)
            ranks[r] = ranks.get(r, 0) + 1
            if r != 9:
                bad += 1
        P("[D-A] block-0 rank histogram over 40 random deg-7 Q_0: %s" % ranks)
        P("      => each of blocks 0,3 leaves nullity 16-9 = 7;")
        P("      cross blocks are then 18 equations on 14 unknowns (+4).")
        P("      D-A falsifier fired: %s" % (bad > 0))

        # ---- D-B : nullity(36x32) == 10 - rank(Phi) ----
        agree = 0
        mism = []
        nullhist = {}
        pairhist = {}
        tried = 0
        while tried < 120:
            Q0 = rand_poly(7, p, rng)
            Q1 = rand_poly(7, p, rng)
            Q2 = rand_poly(7, p, rng)
            if not (squarefree(Q0, p) and squarefree(Q2, p)):
                continue
            if len(pgcd(Q0, Q2, p)) > 1 or len(pgcd(Q0, Q1, p)) > 1:
                continue
            if len(pgcd(Q1, Q2, p)) > 1:
                continue
            tried += 1
            n1 = 32 - rank(sys_36x32([Q0, Q1, Q2], p), p)
            n2 = 10 - rank(phi_14x10([Q0, Q1, Q2], p), p)
            nullhist[n1] = nullhist.get(n1, 0) + 1
            pairhist[(n1, n2)] = pairhist.get((n1, n2), 0) + 1
            if n1 == n2:
                agree += 1
            else:
                if len(mism) < 3:
                    mism.append((Q0, Q1, Q2, n1, n2))
        P("[D-B] %d/%d pairwise-coprime squarefree random curves:"
          " nullity(36x32) == 10-rank(Phi)" % (agree, tried))
        P("      (nullity36, nullityPhi) histogram: %s" % pairhist)
        P("      D-B falsifier fired: %s" % (agree != tried))
        for mm in mism:
            P("      MISMATCH %s" % (mm,))
        P("[D-C] nullity histogram on random curves: %s"
          "  (0 hits => consistent with codim 5, q^-5 ~ %.1e)"
          % (nullhist, p ** -5.0))

        # ---- D-E : the common-root (excess) family ----
        hist = {}
        for _ in range(40):
            xs = rng.randrange(p)
            root = [(-xs) % p, 1]
            Q0 = pmul(root, rand_poly(6, p, rng), p)
            Q1 = pmul(root, rand_poly(6, p, rng), p)
            Q2 = pmul(root, rand_poly(6, p, rng), p)
            n1 = 32 - rank(sys_36x32([Q0, Q1, Q2], p), p)
            hist[n1] = hist.get(n1, 0) + 1
        P("[D-E] planted common root x*: nullity(36x32) histogram over 40: %s"
          % hist)
        P("      D-E falsifier (a common-root curve with nullity 0) fired: %s"
          % (0 in hist))
        P("      dim of that family in P^23 = 3*7-1 (curves) + 1 (x*) = 21;")
        P("      expected dim of the solvability locus = 23-5 = 18  => EXCESS.")

    # ---- the reduced shape at general m (arithmetic only) ----
    P("=" * 68)
    P("REDUCED SHAPE OF (L2) AT GENERAL m  (D-A applied at every m)")
    P("=" * 68)
    P(" m | raw eqs (m+2)(4m+1) | raw unk 16m | reduced eqs m(4m+1) |"
      " reduced unk 8m-2 | deficit")
    for m in range(1, 8):
        P(" %d | %18d | %11d | %19d | %16d | %+d"
          % (m, (m + 2) * (4 * m + 1), 16 * m, m * (4 * m + 1), 8 * m - 2,
             4 * m * m - 7 * m + 2))
    P("Both reductions preserve the deficit 4m^2-7m+2 exactly; the")
    P("determinantal codimension of the solvability locus is deficit+1 = 5")
    P("at m=2 (rank <= 31 of a 36x32, equivalently rank <= 9 of the 14x10).")

    with open("notes/pilots_20260811/r35_l2_gate/d1_results.txt", "w") as fh:
        fh.write("\n".join(LINES) + "\n")
    print("\n".join(LINES))


main()
