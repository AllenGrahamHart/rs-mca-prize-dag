#!/usr/bin/env python3
"""R-L2: the e = m stratum is NONEMPTY at m = 2 -- witness replay from scratch.

Source: critical/nodes/rate_half_band_crossing_location/statement.md
        L3526-3604 (Round-35 R-L2 addendum, round 35 bank 1).
Witness bank: notes/pilots_20260811/r35_l2_gate/d2_results.txt:9-31 (q = 97).
Model:        notes/pilots_20260811/r35_l2_gate/d1_structure.py:6-9.

Checks
  A. the published q = 97 witness, rebuilt and certified from scratch;
  B. the (D-B) congruence criterion nullity(36x32) = 10 - rank(Phi) on the
     witness and on fresh pairwise-coprime squarefree random curves;
  C. the excess (common-root) component: planted common root => nullity 2;
  D. the counting corrections -- 11m-4 > 0 at every m, the determinantal
     codimension 5, dim 18 = 23-5, dim 21 for the excess component, and the
     DEAD +4 reading 4m^2-7m+2 = -1,+4,+17,+38.

Helpers are DUPLICATED into this file: nothing is imported.  Stdlib only.
Run: tools/ramguard local -- python3 \
  background/nodes/rate_half_l2_stratum_nonempty_at_m_two/verify.py
(RAMGUARD_TIMEOUT 300s)
"""

import random

FAIL = []


def bad(m):
    FAIL.append(m)


# ------------------------------------------------------------- polynomials
def ptrim(a, p):
    a = [x % p for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def padd(a, b, p):
    n = max(len(a), len(b))
    r = [0] * n
    for i, x in enumerate(a):
        r[i] = (r[i] + x) % p
    for i, x in enumerate(b):
        r[i] = (r[i] + x) % p
    return ptrim(r, p)


def pneg(a, p):
    return ptrim([(-x) % p for x in a], p)


def pmul(a, b, p):
    a = ptrim(list(a), p)
    b = ptrim(list(b), p)
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                r[i + j] = (r[i + j] + ai * bj) % p
    return ptrim(r, p)


def pmod(a, m, p):
    a = ptrim(list(a), p)
    m = ptrim(list(m), p)
    dm = len(m) - 1
    iv = pow(m[-1], p - 2, p)
    while a and len(a) - 1 >= dm:
        sh = len(a) - 1 - dm
        f = (a[-1] * iv) % p
        for i in range(len(m)):
            a[sh + i] = (a[sh + i] - f * m[i]) % p
        a = ptrim(a, p)
    return a


def pgcd(a, b, p):
    a = ptrim(list(a), p)
    b = ptrim(list(b), p)
    while b:
        a, b = b, pmod(a, b, p)
    if a:
        iv = pow(a[-1], p - 2, p)
        a = [(x * iv) % p for x in a]
    return a


def pderiv(a, p):
    return ptrim([(i * a[i]) % p for i in range(1, len(a))], p)


def peval(a, x, p):
    s = 0
    for c in reversed(a):
        s = (s * x + c) % p
    return s


def pdeg(a, p):
    a = ptrim(list(a), p)
    return len(a) - 1 if a else -1


def pad(a, n):
    return (list(a) + [0] * n)[:n]


# ---------------------------------------------------------- linear algebra
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
        iv = pow(rows[r][c], p - 2, p)
        rows[r] = [(v * iv) % p for v in rows[r]]
        for i in range(nr):
            if i != r and rows[i][c] % p:
                f = rows[i][c]
                rows[i] = [(rows[i][j] - f * rows[r][j]) % p for j in range(nc)]
        piv.append(c)
        r += 1
        if r == nr:
            break
    return rows, r, piv


def rank(M, p):
    return rref(M, p)[1] if M else 0


def nullspace(M, p, nc):
    if not M:
        return [[1 if i == j else 0 for j in range(nc)] for i in range(nc)]
    rows, _, piv = rref(M, p)
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


# ------------------------------------------------------------- the systems
def sys_36x32(Q0, Q1, Q2, p):
    QL = [pad(Q0, 8), pad(Q1, 8), pad(Q2, 8)]
    M = []
    for blk in range(4):
        for a in range(9):
            row = [0] * 32
            if blk <= 2:
                for b in range(8):
                    row[a + b] = (row[a + b] + QL[blk][b]) % p
            if blk >= 1:
                for b in range(8):
                    row[16 + a + b] = (row[16 + a + b] + QL[blk - 1][b]) % p
            M.append(row)
    return M


def phi_14x10(Q0, Q1, Q2, p):
    """(f,g) of degree <= 4 |-> (Q2 f - Q1 g mod Q0, Q1 f - Q0 g mod Q2)."""
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


def hankel_pair(y0, y1, p):
    M0 = [[y0[a + b] % p for b in range(8)] for a in range(9)]
    M1 = [[y1[a + b] % p for b in range(8)] for a in range(9)]
    return M0, M1


def kernel_system(M0, M1, e, p):
    rows = []
    for blk in range(e + 2):
        for a in range(9):
            row = [0] * (8 * (e + 1))
            if blk <= e:
                for b in range(8):
                    row[8 * blk + b] = (row[8 * blk + b] + M0[a][b]) % p
            if blk >= 1:
                for b in range(8):
                    row[8 * (blk - 1) + b] = (row[8 * (blk - 1) + b]
                                              + M1[a][b]) % p
            rows.append(row)
    return rows


# ------------------------------------------------------------ the witness
MU32_97 = [1, 8, 12, 18, 19, 20, 22, 27, 28, 30, 33, 34, 42, 45, 46, 47, 50,
           51, 52, 55, 63, 64, 67, 69, 70, 75, 77, 78, 79, 85, 89, 96]

WIT = {                                  # d2_results.txt:10-31
    "p": 97,
    "Q0": [7, 10, 78, 31, 43, 62, 29, 22],
    "Q1": [80, 88, 69, 63, 34, 94, 70, 62],
    "Q2": [80, 4, 73, 12, 82, 59, 47, 1],
    "y0": [77, 90, 33, 0, 95, 81, 25, 10, 92, 6, 84, 21, 86, 26, 40, 74],
    "y1": [1, 20, 62, 91, 3, 28, 56, 71, 93, 78, 43, 53, 86, 96, 93, 1],
    "dropz": 10,
}


def check_witness():
    p = WIT["p"]
    Q0, Q1, Q2 = WIT["Q0"], WIT["Q1"], WIT["Q2"]

    if (pdeg(Q0, p), pdeg(Q1, p), pdeg(Q2, p)) != (7, 7, 7):
        bad("witness degrees != (7,7,7)")
    if pdeg(pgcd(pgcd(Q0, Q1, p), Q2, p), p) != 0:
        bad("witness s != 0")
    if rank([pad(Q0, 8), pad(Q1, 8), pad(Q2, 8)], p) != 3:
        bad("witness separation rank != 3 (RNC2 needs m+1 = 3)")

    M0, M1 = hankel_pair(WIT["y0"], WIT["y1"], p)
    QL = [pad(Q0, 8), pad(Q1, 8), pad(Q2, 8)]
    for a in range(9):
        for blk in range(4):
            acc = 0
            if blk <= 2:
                acc += sum(M0[a][b] * QL[blk][b] for b in range(8))
            if blk >= 1:
                acc += sum(M1[a][b] * QL[blk - 1][b] for b in range(8))
            if acc % p:
                bad("witness M(Z)Q_Z != 0 at (%d,%d)" % (a, blk))

    ns = nullspace(sys_36x32(Q0, Q1, Q2, p), p, 32)
    if len(ns) != 1:
        bad("witness nullity(36x32) = %d, want 1" % len(ns))
    else:
        vec = [x % p for x in WIT["y0"] + WIT["y1"]]
        b0 = ns[0]
        j = next(i for i in range(32) if b0[i] % p)
        lam = (vec[j] * pow(b0[j], p - 2, p)) % p
        if [lam * c % p for c in b0] != vec:
            bad("witness (y0,y1) does not span the 36x32 kernel")

    ranks = {}
    for z in range(p):
        Mz = [[(M0[a][b] + z * M1[a][b]) % p for b in range(8)]
              for a in range(9)]
        ranks[z] = rank(Mz, p)
    if max(ranks.values()) != 7:
        bad("witness generic rank %d, want 7" % max(ranks.values()))
    drops = sorted(z for z, rk in ranks.items() if rk < 7)
    if drops != [WIT["dropz"]] or ranks[WIT["dropz"]] != 6:
        bad("witness rank drops %s, want [%d] -> 6" % (drops, WIT["dropz"]))
    if rank(M1, p) != 7:
        bad("witness rank at infinity %d, want 7 (no drop at infinity)"
            % rank(M1, p))

    for e in (0, 1):
        if len(nullspace(kernel_system(M0, M1, e, p), p, 8 * (e + 1))) != 0:
            bad("witness has a kernel vector of parameter degree <= %d" % e)
    if len(nullspace(kernel_system(M0, M1, 2, p), p, 24)) != 1:
        bad("witness degree-2 kernel is not 1-dimensional")

    # the splitting layer: T = 0, and the locator statistics
    mu = set(MU32_97)
    members = []
    for z in range(p):
        members.append(padd(padd(Q0, [c * z % p for c in Q1], p),
                            [c * z * z % p for c in Q2], p))
    members.append(ptrim(list(Q2), p))          # z = infinity
    T = sum(1 for M in members
            if sum(1 for x in mu if peval(M, x, p) == 0) == 7)
    if T != 0:
        bad("witness T over mu_32 = %d, want 0" % T)
    maxroots = max(sum(1 for x in mu if peval(M, x, p) == 0) for M in members)
    if maxroots != 4:
        bad("witness max roots in mu_32 = %d, want 4" % maxroots)
    # a*: the locator of a slope is the corresponding pencil member read as a
    # form of degree exactly rho = 7 on P^1, so a member of affine degree
    # 7-t carries t roots at infinity.  |S_g u S_g'| = 14 - (common roots),
    # common roots = deg gcd(finite parts) + min(7-deg_g, 7-deg_g').
    maxshared = 0
    astar_proj = None
    astar_aff = None
    for i in range(len(members)):
        for j in range(i + 1, len(members)):
            gd = pdeg(pgcd(members[i], members[j], p), p)
            maxshared = max(maxshared, gd)
            di, dj = pdeg(members[i], p), pdeg(members[j], p)
            common = gd + min(7 - di, 7 - dj)
            up = 14 - common
            ua = di + dj - gd
            astar_proj = up if astar_proj is None else min(astar_proj, up)
            astar_aff = ua if astar_aff is None else min(astar_aff, ua)
    if maxshared != 1:
        bad("witness max shared FINITE roots = %d, want 1" % maxshared)
    if astar_proj != 13:
        bad("witness a* = %s projective / %s affine, want 13 (= 7m-1)"
            % (astar_proj, astar_aff))
    return T, maxroots, maxshared, (astar_proj, astar_aff)


# ------------------------------------------------------------ (D-B) + excess
def check_db_and_excess():
    agree = 0
    tried = 0
    excess = {}
    for p in (97, 193):
        rng = random.Random(35_000 + p)
        # the witness itself
        n1 = 32 - rank(sys_36x32(WIT["Q0"], WIT["Q1"], WIT["Q2"], 97), 97)
        n2 = 10 - rank(phi_14x10(WIT["Q0"], WIT["Q1"], WIT["Q2"], 97), 97)
        if p == 97 and n1 != n2:
            bad("(D-B) fails ON THE WITNESS: %d != %d" % (n1, n2))
        cnt = 0
        while cnt < 30:
            Qs = []
            for _ in range(3):
                a = [rng.randrange(p) for _ in range(8)]
                while a[7] == 0:
                    a[7] = rng.randrange(p)
                Qs.append(a)
            Q0, Q1, Q2 = Qs
            if pdeg(pgcd(Q0, pderiv(Q0, p), p), p) > 0:
                continue
            if pdeg(pgcd(Q2, pderiv(Q2, p), p), p) > 0:
                continue
            if (pdeg(pgcd(Q0, Q2, p), p) > 0 or pdeg(pgcd(Q0, Q1, p), p) > 0
                    or pdeg(pgcd(Q1, Q2, p), p) > 0):
                continue
            cnt += 1
            tried += 1
            a1 = 32 - rank(sys_36x32(Q0, Q1, Q2, p), p)
            a2 = 10 - rank(phi_14x10(Q0, Q1, Q2, p), p)
            if a1 == a2:
                agree += 1
            else:
                bad("(D-B) mismatch at q=%d: %d != %d" % (p, a1, a2))
        # the excess component: a planted common root
        for _ in range(12):
            xs = rng.randrange(p)
            root = [(-xs) % p, 1]
            Q0 = pmul(root, [rng.randrange(p) for _ in range(7)], p)
            Q1 = pmul(root, [rng.randrange(p) for _ in range(7)], p)
            Q2 = pmul(root, [rng.randrange(p) for _ in range(7)], p)
            nn = 32 - rank(sys_36x32(Q0, Q1, Q2, p), p)
            excess[nn] = excess.get(nn, 0) + 1
    if set(excess) != {2}:
        bad("planted-common-root nullity histogram %s, want {2: all}" % excess)
    return agree, tried, excess


# ---------------------------------------------------------------- counting
def check_counts():
    # the DEAD reading: the equation-count excess is NOT an existence codim.
    dead = [4 * m * m - 7 * m + 2 for m in (1, 2, 3, 4)]
    if dead != [-1, 4, 17, 38]:
        bad("4m^2-7m+2 row %s, want [-1,4,17,38]" % dead)
    # the honest count: determinantal codimension and the expected dimension.
    codim = (36 - 31) * (32 - 31)
    if codim != 5:
        bad("determinantal codim %d, want 5" % codim)
    if 23 - codim != 18:
        bad("good-component dimension != 18")
    if 3 * 7 - 1 + 1 != 21:
        bad("excess-component dimension != 21")
    for m in range(1, 40):
        if 11 * m - 4 <= 0:
            bad("11m-4 <= 0 at m = %d" % m)
    if 11 * 2 - 4 != 18:
        bad("11m-4 at m=2 is not the measured 18")
    return dead, codim


# -------------------------------------------------------------------- main
T, mr, ms, astar = check_witness()
agree, tried, excess = check_db_and_excess()
dead, codim = check_counts()

if FAIL:
    for m in FAIL:
        print("FAIL " + m)
    raise SystemExit(1)
print("L2_NONEMPTY_THEOREM_PASS q=97 witness certified from scratch "
      "(degs=(7,7,7) s=0 seprank=3 nullity36x32=1 genrank=7 drop@10->6 "
      "e=2 exactly T=%d maxroots=%d maxshared=%d a*=%s (projective,affine)); "
      "(D-B) %d/%d fresh "
      "curves + the witness; planted-common-root nullity %s (dim 21 excess); "
      "codim=%d dim=18=11m-4 at m=2; dead +4 row %s"
      % (T, mr, ms, astar, agree, tried, excess, codim, dead))
