"""Shared F_p linear algebra / polynomial helpers for r35_l2_gate.
Loaded with exec() by d3_scale.py.  Stdlib only.
"""


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


def hankel(y, p):
    return [[y[a + b] % p for b in range(8)] for a in range(9)]


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


def phi_14x10(Q, p):
    Q0, Q1, Q2 = [ptrim(list(q), p) for q in Q]
    cols = []
    for i in range(5):
        e = [0] * i + [1]
        cols.append(pad(pmod(pmul(Q2, e, p), Q0, p), 7)
                    + pad(pmod(pmul(Q1, e, p), Q2, p), 7))
    for i in range(5):
        e = [0] * i + [1]
        n1 = [(-x) % p for x in Q1]
        n0 = [(-x) % p for x in Q0]
        cols.append(pad(pmod(pmul(n1, e, p), Q0, p), 7)
                    + pad(pmod(pmul(n0, e, p), Q2, p), 7))
    return [[cols[j][i] for j in range(10)] for i in range(14)]


def build_MB(B, p):
    f, g, h, k = [pad(b, 5) for b in B]
    ng = [(-x) % p for x in g]
    nh = [(-x) % p for x in h]
    nk = [(-x) % p for x in k]
    e1 = [nh, ng, f]
    e2 = [ng, f, nk]
    M = [[0] * 24 for _ in range(24)]
    for j in range(3):
        for i in range(8):
            col = 8 * j + i
            for t in range(5):
                M[i + t][col] = e1[j][t] % p
                M[12 + i + t][col] = e2[j][t] % p
    return M


def quick_certify(Q, p):
    Q0, Q1, Q2 = [ptrim(list(q), p) for q in Q]
    if len(Q0) != 8 or len(Q2) != 8:
        return None
    if len(pgcd(pgcd(Q0, Q1, p), Q2, p)) > 1:
        return None
    sr = rank([pad(Q0, 8), pad(Q1, 8), pad(Q2, 8)], p)
    if sr != 3:
        return None
    ns = nullspace(sys_36x32([Q0, Q1, Q2], p), p, 32)
    if not ns:
        return None
    v = ns[0]
    y0, y1 = v[:16], v[16:]
    gr = max([rank(hankel([(y0[i] + z * y1[i]) % p for i in range(16)], p), p)
              for z in range(min(p, 30))] + [rank(hankel(y1, p), p)])
    if gr != 7:
        return None
    H0, H1 = hankel(y0, p), hankel(y1, p)
    QL = [pad(Q0, 8), pad(Q1, 8), pad(Q2, 8)]
    for kk in range(4):
        for a in range(9):
            tot = 0
            if kk <= 2:
                tot += sum(H0[a][b] * QL[kk][b] for b in range(8))
            if kk >= 1:
                tot += sum(H1[a][b] * QL[kk - 1][b] for b in range(8))
            if tot % p:
                return None
    M2 = []
    for kk in range(3):
        for a in range(9):
            row = [0] * 16
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
    if 16 - rank(M2, p) != 0:
        return None
    return dict(e=2, generic_rank=gr, s=0, seprank=sr, nullity36=len(ns),
                direct=True)
