#!/usr/bin/env python3
"""r35_fg_razor: corrected stratum classification + the p*(LB1) law.

FIXES MY OWN TEST.  e1/e2 tested principality as
K_0 == g*F[x]_{<= r - deg g}.  That is the round-33 FG condition
(K_0 = P.F[x]_{<=r-p} with p = deg P), but it is NOT what
'h_r = p*' gives: the correct containment is
P.F[x]_{<= r - p*} subset K_0 with P in Ann(V)_{p*} of degree
d* <= p*, and the two coincide only when d* = p*.  Here I measure
d* = min{deg P : 0 != P in Ann(V)_{p*}} and run BOTH tests, so the
FG verdict is not an artefact of the shift bound.

Also: the p*(LB1) law at four shapes (structure only, no D_r(D) sweep).
Stdlib only.
"""
import sys

OUT = []


def emit(s=""):
    OUT.append(str(s))
    print(s)
    sys.stdout.flush()


def inv(a, p):
    return pow(a % p, p - 2, p)


def rref(M, p):
    M = [row[:] for row in M]
    rows, cols = len(M), (len(M[0]) if M else 0)
    piv, r = [], 0
    for c in range(cols):
        pr = None
        for i in range(r, rows):
            if M[i][c] % p:
                pr = i
                break
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        iv = inv(M[r][c], p)
        M[r] = [(x * iv) % p for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(cols)]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return M, piv


def rank(M, p):
    return len(rref(M, p)[1]) if M else 0


def nullspace(M, p, nc):
    if not M:
        return [[1 if i == j else 0 for i in range(nc)] for j in range(nc)]
    Rm, piv = rref(M, p)
    out = []
    for f in [c for c in range(nc) if c not in piv]:
        v = [0] * nc
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-Rm[i][f]) % p
        out.append(v)
    return out


def ptrim(a, p):
    a = [x % p for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b, p):
    if not a or not b:
        return []
    o = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                o[i + j] = (o[i + j] + ai * bj) % p
    return ptrim(o, p)


def pmod(a, m, p):
    a, m = ptrim(a[:], p), ptrim(m[:], p)
    dm = len(m) - 1
    iv = inv(m[-1], p)
    while a and len(a) - 1 >= dm:
        f = (a[-1] * iv) % p
        sh = len(a) - 1 - dm
        for i in range(dm + 1):
            a[sh + i] = (a[sh + i] - f * m[i]) % p
        a = ptrim(a, p)
    return a


def pgcd(a, b, p):
    a, b = ptrim(a[:], p), ptrim(b[:], p)
    while b:
        a, b = b, pmod(a, b, p)
    if a:
        iv = inv(a[-1], p)
        a = [(x * iv) % p for x in a]
    return a


def is_irred(f, p):
    d = len(f) - 1
    if d <= 0:
        return False
    if d == 1:
        return True

    def frob(kk):
        cur = [0, 1]
        for _ in range(kk):
            e, res, base = p, [1], cur[:]
            while e:
                if e & 1:
                    res = pmod(pmul(res, base, p), f, p)
                base = pmod(pmul(base, base, p), f, p)
                e >>= 1
            cur = res
        return cur

    def subx(v):
        w = v[:] + [0] * max(0, 2 - len(v))
        w[1] = (w[1] - 1) % p
        return ptrim(w, p)

    if subx(frob(d)):
        return False
    m, pr, f2 = d, set(), 2
    while f2 * f2 <= m:
        while m % f2 == 0:
            pr.add(f2)
            m //= f2
        f2 += 1
    if m > 1:
        pr.add(m)
    for l in pr:
        if len(pgcd(subx(frob(d // l)), f, p)) - 1 != 0:
            return False
    return True


def find_irred(deg, p):
    for code in range(p ** deg):
        c, t = [], code
        for _ in range(deg):
            c.append(t % p)
            t //= p
        f = c + [1]
        if is_irred(f, p):
            return f
    return None


def dual_mults(D, p):
    out = []
    for x in D:
        pr = 1
        for y in D:
            if y != x:
                pr = (pr * (x - y)) % p
        out.append(inv(pr, p))
    return out


def syn(err, D, v, R, p):
    y = []
    for m in range(R):
        s = 0
        for i, x in enumerate(D):
            e = err.get(x, 0)
            if e:
                s = (s + e * v[i] * pow(x, m, p)) % p
        y.append(s % p)
    return y


def impulse(P, R, p):
    d = len(P) - 1
    u = [0] * (d - 1) + [1]
    while len(u) < R:
        m = len(u)
        s = sum(P[j] * u[m - d + j] for j in range(d)) % p
        u.append((-s) % p)
    return u[:R]


def hankel(y, i, R, p):
    return [[y[s + j] % p for j in range(i + 1)] for s in range(R - i)]


def span_eq(A, B, p):
    """span(A) == span(B) ?"""
    ra, rb = rank(A, p), rank(B, p)
    return ra == rb and rank([r[:] for r in A] + [r[:] for r in B], p) == ra


def classify(y0, y1, R, r, rho, p, name, extra=""):
    ps, Ann = None, None
    for i in range(1, r + 1):
        M = hankel(y0, i, R, p) + hankel(y1, i, R, p)
        ns = nullspace(M, p, i + 1)
        if ns:
            ps, Ann = i, ns
            break
    M = hankel(y0, r, R, p) + hankel(y1, r, R, p)
    hr = rank(M, p)
    K0 = nullspace(M, p, r + 1)
    # d* = minimal degree of a nonzero element of Ann(V)_{p*}
    Rm, piv = rref([a[:] for a in Ann], p)
    dstar = min(len(ptrim(a[:], p)) - 1 for a in Rm[:len(piv)])
    Pgen = None
    for a in Rm[:len(piv)]:
        t = ptrim(a[:], p)
        if len(t) - 1 == dstar:
            Pgen = t
            break
    dimAnn = len(Ann)
    # test 1 (window bound):  K_0 == P.F[x]_{<= r - p*}
    sh1 = []
    for s in range(r - ps + 1):
        w = [0] * s + Pgen[:]
        sh1.append(w + [0] * (r + 1 - len(w)))
    t1 = span_eq(sh1, K0, p) if sh1 else False
    # test 2 (ROUND-33 FG condition): K_0 == P.F[x]_{<= r - deg P}
    sh2 = []
    for s in range(r - dstar + 1):
        w = [0] * s + Pgen[:]
        if len(w) <= r + 1:
            sh2.append(w + [0] * (r + 1 - len(w)))
    t2 = span_eq(sh2, K0, p) if sh2 else False
    isFG = t2 and dstar <= 2 * rho and hr == dstar
    emit("   [%s] p*=%-3d d*=deg P=%-3d dim Ann(V)_{p*}=%-2d h_r=%-3d"
         " dim K_0=%-3d (r+1-h_r=%d)" % (name, ps, dstar, dimAnn, hr,
                                         len(K0), r + 1 - hr))
    emit("        K_0 == P.F[x]_{<=r-p*} : %-5s | K_0 == P.F[x]_{<=r-degP}"
         " (ROUND-33 FG) : %-5s | FG : %-5s | d*==p* : %s"
         % (t1, t2, isFG, dstar == ps))
    if extra:
        emit("        " + extra)
    return dict(ps=ps, dstar=dstar, hr=hr, dimK0=len(K0), t1=t1, t2=t2,
                FG=isFG)


# (q, n, k, rho)  -> R = n-k, r = R-rho
CELLS = [
    ("rate-half", 101, 20, 10, 2),
    ("rate-half", 65537, 20, 10, 2),
    ("rate-half", 101, 22, 11, 2),
    ("rate-half", 65537, 22, 11, 2),
    ("rate-half", 101, 24, 12, 2),
    ("rate-half", 101, 26, 13, 3),
    ("rate-half", 101, 28, 14, 3),
    ("k=1 sep", 17, 17, 1, 3),
    ("k=1 sep", 19, 19, 1, 3),
    ("k=1 sep", 23, 23, 1, 3),
]


def main():
    emit("=== r35_fg_razor  e4_classify  (corrected stratum test) ===")
    emit("Round-33 FG (crossing_location:3059) = 'fixed squarefree generator")
    emit("P, rho < p <= 2rho' with K_0 = P.F[x]_{<= r-p}, p = deg P.")
    emit("h_r = p* gives only K_0 = P.F[x]_{<= r - p*}; the two agree iff")
    emit("d* := deg P equals p*.  BOTH tests are reported below.")
    emit("")
    for tag, q, n, k, rho in CELLS:
        p = q
        R, r = n - k, (n - k) - rho
        a = n - r
        D = list(range(n))
        v = dual_mults(D, p)
        emit("CELL[%s] q=%d n=%d k=%d R=%d rho=%d r=%d a=%d | 4rho<R:%s"
             " a>R+1:%s a-1>r:%s | 2rho=%d floor(R/2)=%d"
             % (tag, q, n, k, R, rho, r, a, 4 * rho < R, a > R + 1,
                a - 1 > r, 2 * rho, R // 2))
        P1 = find_irred(rho, p)
        P2 = [1]
        for t in range(rho):
            P2 = pmul(P2, [(-t) % p, 1], p)
        classify(impulse(P1, R, p), impulse(P2, R, p), R, r, rho, p,
                 "FG(witness B)",
                 "predicted p*=d*=2rho=%d, h_r=2rho, dim K_0=r+1-2rho=%d"
                 % (2 * rho, r + 1 - 2 * rho))
        T = list(range(r + 1))
        z1 = syn({t: 1 for t in T}, D, v, R, p)
        z0 = syn({t: (-t) % p for t in T}, D, v, R, p)
        classify(z0, z1, R, r, rho, p, "LB1",
                 "predicted h_r=rho+1=%d, dim K_0=r-rho=%d,"
                 " p*=max(rho+1, floor((R+2)/2)) = max(%d,%d) = %d,"
                 " d* = min(a-1, .) = %d"
                 % (rho + 1, r - rho, rho + 1, (R + 2) // 2,
                    max(rho + 1, (R + 2) // 2), a - 1))
        emit("")
    with open("notes/pilots_20260811/r35_fg_razor/e4_results.txt", "w") as fh:
        fh.write("\n".join(OUT) + "\n")


main()
