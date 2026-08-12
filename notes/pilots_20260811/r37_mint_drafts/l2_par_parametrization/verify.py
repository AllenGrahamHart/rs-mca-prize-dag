#!/usr/bin/env python3
"""(PAR) / (RES) / the determinantal form for the e=m=2 (L2) stratum.

Source: critical/nodes/rate_half_band_crossing_location/statement.md
        L4347-4366 (Round-36 (SAT3)-on-(L2) addendum, round 36 bank 2).
Witness bank: notes/pilots_20260811/r36_sat3_on_l2/d2_results.txt:18-33
        (the certified T = 2 doubly-prescribed object at q = 97).

Checks
  A. the determinantal identity, symbolically, on random draws over two fields;
  B. the two syzygies f*C = g*B + h*A and f*B = g*A + k*C, symbolically;
  C. the two-conditions-imply-the-third statement AND its exception,
     EXHAUSTIVELY over all local value 4-tuples of a small field;
  D. (PAR) on the banked certified T = 2 witness, re-derived from scratch,
     including the full (L2) certification (degrees, s = 0, M(Z)Q_Z = 0,
     nullity, generic rank, minimal index e = 2 exactly, rank drop, T = 2);
  E. the dimension arithmetic 20 + 1 - 2 - 1 = 18.

Helpers are DUPLICATED into this file on purpose: nothing is imported, so no
banked script can write at import time.  Stdlib only.
Run: tools/ramguard tiny -- python3 <this file>   (RAMGUARD_TIMEOUT default 60s)
"""

import random

FAIL = []


def bad(msg):
    FAIL.append(msg)


# ------------------------------------------------- polynomials over F_p (lo->hi)
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


def psub(a, b, p):
    return padd(a, pneg(b, p), p)


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


def pdivexact(a, m, p):
    """a / m assuming exact division."""
    a = ptrim(list(a), p)
    m = ptrim(list(m), p)
    q = [0] * max(1, len(a) - len(m) + 1)
    iv = pow(m[-1], p - 2, p)
    work = list(a)
    while work and len(work) - 1 >= len(m) - 1:
        sh = len(work) - len(m)
        c = (work[-1] * iv) % p
        q[sh] = c
        for i in range(len(m)):
            work[sh + i] = (work[sh + i] - c * m[i]) % p
        work = ptrim(work, p)
    if work:
        return None
    return ptrim(q, p)


def pgcd(a, b, p):
    a = ptrim(list(a), p)
    b = ptrim(list(b), p)
    while b:
        a, b = b, pmod(a, b, p)
    if a:
        iv = pow(a[-1], p - 2, p)
        a = [(x * iv) % p for x in a]
    return a


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


# ---------------------------------------------------------- linear algebra F_p
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


# --------------------------------------------------------- the (PAR) triple
def par_triple(f, g, h, k, p):
    """A = f^2-kg, B = fg+hk, C = g^2+hf."""
    A = psub(pmul(f, f, p), pmul(k, g, p), p)
    B = padd(pmul(f, g, p), pmul(h, k, p), p)
    C = padd(pmul(g, g, p), pmul(h, f, p), p)
    return A, B, C


# ==================================================================== A, B
def check_identities():
    for p in (97, 193):
        rng = random.Random(37_000 + p)
        for _ in range(60):
            f, g, h, k = ([rng.randrange(p) for _ in range(5)] for _ in range(4))
            A, B, C = par_triple(f, g, h, k, p)

            # A. det([[f+zg, k+zf],[g-zh, f+zg]]) = A + zB + z^2 C.
            # expand the 2x2 determinant in z with polynomial entries.
            t00 = [f, g]          # f + z g
            t01 = [k, f]          # k + z f
            t10 = [g, pneg(h, p)]  # g - z h
            t11 = [f, g]          # f + z g
            det = [[] for _ in range(3)]
            for i in range(2):
                for j in range(2):
                    det[i + j] = padd(det[i + j], pmul(t00[i], t11[j], p), p)
                    det[i + j] = psub(det[i + j], pmul(t01[i], t10[j], p), p)
            for got, want, nm in ((det[0], A, "z^0"), (det[1], B, "z^1"),
                                  (det[2], C, "z^2")):
                if ptrim(got, p) != ptrim(want, p):
                    bad("determinantal identity fails at %s, q=%d" % (nm, p))

            # B. the two syzygies.
            if ptrim(pmul(f, C, p), p) != ptrim(
                    padd(pmul(g, B, p), pmul(h, A, p), p), p):
                bad("syzygy f*C = g*B + h*A fails at q=%d" % p)
            if ptrim(pmul(f, B, p), p) != ptrim(
                    padd(pmul(g, A, p), pmul(k, C, p), p), p):
                bad("syzygy f*B = g*A + k*C fails at q=%d" % p)


# ======================================================================== C
def check_local_implication():
    """Exhaustive over (f,g,h,k) VALUES at ell in a small field.

    Claim: A = C = 0 at ell implies B = 0 at ell, EXCEPT when f = g = 0
    there (in which case A = C = 0 automatically and B = hk is free).
    """
    p = 13
    exceptions = 0
    witness = None
    for fv in range(p):
        for gv in range(p):
            for hv in range(p):
                for kv in range(p):
                    Av = (fv * fv - kv * gv) % p
                    Cv = (gv * gv + hv * fv) % p
                    Bv = (fv * gv + hv * kv) % p
                    if Av or Cv:
                        continue
                    if Bv == 0:
                        continue
                    exceptions += 1
                    if not (fv == 0 and gv == 0):
                        bad("third condition failed OUTSIDE the f=g=0 "
                            "exception at (%d,%d,%d,%d)" % (fv, gv, hv, kv))
                    if witness is None:
                        witness = (fv, gv, hv, kv, Bv)
    if witness is None:
        bad("the f=g=0 exception is empty -- the third condition would be "
            "unconditional, contradicting the source")
    return exceptions, witness


# ======================================================== the (L2) certification
MU32_97 = [1, 8, 12, 18, 19, 20, 22, 27, 28, 30, 33, 34, 42, 45, 46, 47, 50,
           51, 52, 55, 63, 64, 67, 69, 70, 75, 77, 78, 79, 85, 89, 96]

W = {                                    # d2_results.txt:19-31, q = 97
    "p": 97,
    "S0": [30, 33, 51, 63, 69, 77, 85],
    "S2": [8, 12, 18, 27, 45, 52, 78],
    "f": [42, 3, 81, 6, 89],
    "g": [71, 19, 15, 60, 1],
    "h": [5, 40, 44, 0, 6],
    "k": [24, 46, 52, 68, 63],
    "L": [53, 1],
    "Q0": [78, 63, 82, 85, 33, 58, 77, 1],
    "Q1": [75, 9, 93, 12, 8, 88, 15, 79],
    "Q2": [46, 93, 4, 16, 76, 49, 28, 50],
    "y0": [27, 56, 11, 6, 39, 43, 74, 62, 47, 5, 47, 52, 66, 62, 81, 81],
    "y1": [9, 76, 44, 51, 3, 76, 93, 68, 66, 20, 37, 43, 86, 74, 68, 1],
    "dropz": 89,
}


def hankel_pair(y0, y1, p):
    """M(Z) = M_r(y_0) + Z M_r(y_1), M_r(y)[a][b] = y[a+b], 9 x 8."""
    M0 = [[y0[a + b] % p for b in range(8)] for a in range(9)]
    M1 = [[y1[a + b] % p for b in range(8)] for a in range(9)]
    return M0, M1


def kernel_system(M0, M1, e, p):
    """rows of (M_0 + z M_1)(P_0 + ... + z^e P_e) = 0, unknowns P_0..P_e."""
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


def sys_36x32(Q0, Q1, Q2, p):
    """M(Z)Q_Z = 0 as 36 rows on (y_0[0..15], y_1[0..15])."""
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


def check_witness():
    p = W["p"]
    f, g, h, k, L = W["f"], W["g"], W["h"], W["k"], W["L"]
    Q0, Q1, Q2 = W["Q0"], W["Q1"], W["Q2"]
    A, B, C = par_triple(f, g, h, k, p)

    # (PAR) itself, re-derived from scratch
    if ptrim(pmul(L, Q0, p), p) != ptrim(A, p):
        bad("witness: L*Q_0 != f^2-kg")
    if ptrim(pmul(L, Q1, p), p) != ptrim(B, p):
        bad("witness: L*Q_1 != fg+hk")
    if ptrim(pmul(L, Q2, p), p) != ptrim(C, p):
        bad("witness: L*Q_2 != g^2+hf")
    for nm, poly in (("f", f), ("g", g), ("h", h), ("k", k)):
        if pdeg(poly, p) > 4:
            bad("witness: deg %s > 4" % nm)
    if pdeg(L, p) != 1:
        bad("witness: L is not linear")
    ell = (-W["L"][0] * pow(W["L"][1], p - 2, p)) % p
    for nm, poly in (("A", A), ("C", C)):
        if peval(poly, ell, p) != 0:
            bad("witness: %s(ell) != 0" % nm)
    if peval(B, ell, p) != 0:
        bad("witness: B(ell) != 0 (the derived third condition)")

    # the elimination Q_2 * (f^2-kg) = Q_0 * (g^2+hf)
    if ptrim(pmul(Q2, A, p), p) != ptrim(pmul(Q0, C, p), p):
        bad("witness: elimination Q_2*A != Q_0*C")

    # (RES), forward direction: L divides all three, so the gcd is nonconstant
    gg = pgcd(pgcd(A, B, p), C, p)
    if pdeg(gg, p) < 1:
        bad("witness: gcd(A,B,C) is constant -- (RES) forward direction fails")
    if pdivexact(gg, ptrim([x * pow(L[-1], p - 2, p) % p for x in L], p),
                 p) is None:
        bad("witness: L does not divide gcd(A,B,C)")

    # degrees and s = 0
    if (pdeg(Q0, p), pdeg(Q1, p), pdeg(Q2, p)) != (7, 7, 7):
        bad("witness: degrees are not (7,7,7)")
    if pdeg(pgcd(pgcd(Q0, Q1, p), Q2, p), p) != 0:
        bad("witness: s != 0")

    # M(Z) Q_Z = 0, entrywise from scratch
    M0, M1 = hankel_pair(W["y0"], W["y1"], p)
    for a in range(9):
        for blk in range(4):
            acc = 0
            QL = [pad(Q0, 8), pad(Q1, 8), pad(Q2, 8)]
            if blk <= 2:
                acc += sum(M0[a][b] * QL[blk][b] for b in range(8))
            if blk >= 1:
                acc += sum(M1[a][b] * QL[blk - 1][b] for b in range(8))
            if acc % p:
                bad("witness: M(Z)Q_Z != 0 at row %d block %d" % (a, blk))

    # nullity of the 36x32 system and that (y0,y1) spans it
    S = sys_36x32(Q0, Q1, Q2, p)
    ns = nullspace(S, p, 32)
    if len(ns) != 1:
        bad("witness: nullity(36x32) = %d, want 1" % len(ns))
    else:
        vec = [x % p for x in W["y0"] + W["y1"]]
        basis = ns[0]
        j = next(i for i in range(32) if basis[i] % p)
        lam = (vec[j] * pow(basis[j], p - 2, p)) % p
        if [lam * b % p for b in basis] != vec:
            bad("witness: (y0,y1) is not the 36x32 kernel vector")

    # generic rank 7, single finite rank drop to 6, full rank at infinity
    ranks = {}
    for z in range(p):
        Mz = [[(M0[a][b] + z * M1[a][b]) % p for b in range(8)]
              for a in range(9)]
        ranks[z] = rank(Mz, p)
    if max(ranks.values()) != 7:
        bad("witness: generic rank %d, want 7" % max(ranks.values()))
    drops = sorted(z for z, rk in ranks.items() if rk < 7)
    if drops != [W["dropz"]] or ranks[W["dropz"]] != 6:
        bad("witness: rank drops %s (ranks %s), want [%d] -> 6"
            % (drops, [ranks[z] for z in drops], W["dropz"]))
    if rank(M1, p) != 7:
        bad("witness: rank at infinity %d, want 7" % rank(M1, p))

    # minimal index EXACTLY 2
    for e in (0, 1):
        if len(nullspace(kernel_system(M0, M1, e, p), p, 8 * (e + 1))) != 0:
            bad("witness: a kernel vector of parameter degree <= %d exists" % e)
    k2 = nullspace(kernel_system(M0, M1, 2, p), p, 24)
    if len(k2) != 1:
        bad("witness: degree-2 kernel dim %d, want 1" % len(k2))

    # T = 2 over mu_32: Q_0 and Q_2 split with 7 roots each, nothing else
    mu = set(MU32_97)
    r0 = sorted(x for x in mu if peval(Q0, x, p) == 0)
    r2 = sorted(x for x in mu if peval(Q2, x, p) == 0)
    if r0 != sorted(W["S0"]) or r2 != sorted(W["S2"]):
        bad("witness: prescribed root sets do not reproduce")
    if set(r0) & set(r2):
        bad("witness: |S_0 cap S_2| != 0")
    supported = 0
    for z in range(p):                     # finite slopes
        Qz = padd(padd(Q0, [c * z % p for c in Q1], p),
                  [c * z * z % p for c in Q2], p)
        if sum(1 for x in mu if peval(Qz, x, p) == 0) == 7:
            supported += 1
    if sum(1 for x in mu if peval(Q2, x, p) == 0) == 7:
        supported += 1                     # z = infinity
    if supported != 2:
        bad("witness: T over mu_32 = %d, want 2" % supported)
    return supported


# ======================================================================== E
def check_dimension():
    coords = 5 * 4          # f,g,h,k with deg <= 4
    if coords != 20:
        bad("coordinate count != 20")
    affine = coords + 1 - 2     # + ell, - the two conditions at ell
    projective = affine - 1     # - the overall scaling
    if (affine, projective) != (19, 18):
        bad("dimension arithmetic: got (%d,%d), want (19,18)"
            % (affine, projective))
    return projective


# ===================================================================== main
check_identities()
nexc, wexc = check_local_implication()
T = check_witness()
dim = check_dimension()

if FAIL:
    for m in FAIL:
        print("FAIL " + m)
    raise SystemExit(1)
print("L2_PAR_PARAMETRIZATION_PASS det-identity+2 syzygies OK on 120 draws "
      "(q=97,193); local implication exhaustive over F_13^4 with %d exception "
      "tuples all of the form f=g=0 (e.g. %s); banked q=97 T=%d witness "
      "re-derived from scratch; dim=%d" % (nexc, wexc, T, dim))
