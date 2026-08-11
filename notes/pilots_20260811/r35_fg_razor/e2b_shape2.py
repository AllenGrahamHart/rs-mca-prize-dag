#!/usr/bin/env python3
"""r35_fg_razor D2 (b): second rate-half shape (n=22) + the rho=3 census.

Part A: rate-half shape n=22, k=11, R=11, rho=2, r=9, a=13 (4rho<R,
        a>R+1, a-1>r), two fields straddling mu_1 = 1.
Part B: the rho=3 SEPARATING cells from e1 (k=1: 4rho<R holds, but they
        are NOT rate-half and have a-1 < r -- declared, not razor-faithful).
Stdlib only.
"""
import sys
from itertools import combinations
from math import comb, exp

OUT = []
LOCCAP = 24


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


def proots_int(rs):
    f = [1]
    for a in rs:
        g = [0] * (len(f) + 1)
        for i, ci in enumerate(f):
            g[i] -= a * ci
            g[i + 1] += ci
        f = g
    return f


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


def structure(y0, y1, R, r, p):
    ps = None
    for i in range(1, r + 1):
        M = hankel(y0, i, R, p) + hankel(y1, i, R, p)
        if (i + 1) - rank(M, p) > 0:
            ps = i
            break
    M = hankel(y0, r, R, p) + hankel(y1, r, R, p)
    hr = rank(M, p)
    K0 = nullspace(M, p, r + 1)
    g = []
    for b in K0:
        g = pgcd(g, b[:], p) if g else ptrim(b[:], p)
    princ = False
    if K0 and g:
        dg = len(g) - 1
        sh = []
        for s in range(r - dg + 1):
            w = [0] * s + g[:]
            sh.append(w + [0] * (r + 1 - len(w)))
        princ = (rank(sh, p) == len(K0) and
                 rank(sh + [b[:] for b in K0], p) == len(K0))
    return ps, hr, len(K0), (len(g) - 1 if g else -1), princ


def ledger(badmap, n, R):
    sl = sorted(badmap)
    if len(sl) < 2:
        return None
    best = None
    for i in range(len(sl)):
        for j in range(i + 1, len(sl)):
            for Sg in badmap[sl[i]]:
                sg = set(Sg)
                for Sh in badmap[sl[j]]:
                    u = len(sg | set(Sh))
                    if best is None or u < best[0]:
                        best = (u, sg | set(Sh))
    ws, W = best
    fl = R + 1 - ws
    t1 = t2 = 0
    sp = []
    for gam in sl:
        if any(set(S) <= W for S in badmap[gam]):
            t1 += 1
        else:
            t2 += 1
            sp.append(min(len(set(S) - W) for S in badmap[gam]))
    dx = {}
    for gam in sl:
        for x in badmap[gam][0]:
            dx[x] = dx.get(x, 0) + 1
    e = max(dx.values()) if dx else 0
    return dict(ws=ws, fl=fl, T1=t1, T2=t2, sp=sp, e=e,
                cap=(((n - ws) * e) // fl if fl > 0 else None))


def run(n, R, rho, k, qs, label):
    r = R - rho
    a = n - r
    Cnr = comb(n, r)
    D = list(range(n))
    emit("%s n=%d k=%d R=%d rho=%d r=%d a=%d | rate=%s | 4rho<R:%s |"
         " a>R+1:%s | a-1>r:%s | C(n,r)=%d | 2rho=%d floor(R/2)=%d"
         % (label, n, k, R, rho, r, a,
            ("1/2" if 2 * k == n else "%d/%d" % (k, n)), 4 * rho < R,
            a > R + 1, a - 1 > r, Cnr, 2 * rho, R // 2))
    cfgs = []
    for q in qs:
        p = q
        v = dual_mults(D, p)
        P1 = find_irred(rho, p)
        P2 = [1]
        for t in range(rho):
            P2 = pmul(P2, [(-t) % p, 1], p)
        y0, y1 = impulse(P1, R, p), impulse(P2, R, p)
        T = list(range(r + 1))
        z1 = syn({t: 1 for t in T}, D, v, R, p)
        z0 = syn({t: (-t) % p for t in T}, D, v, R, p)
        for nm, (u0, u1) in (("FG(witness B)", (y0, y1)), ("LB1", (z0, z1))):
            cfgs.append(dict(q=q, p=p, nm=nm, A=hankel(u0, r, R, p),
                             B=hankel(u1, r, R, p),
                             st=structure(u0, u1, R, r, p),
                             bad={}, cnt={}, univ=0))
    for S in combinations(D, r):
        s0 = proots_int(S)
        for cf in cfgs:
            p, A, B = cf["p"], cf["A"], cf["B"]
            sg = [c % p for c in s0]
            u = [sum(A[s][j] * sg[j] for j in range(r + 1)) % p
                 for s in range(rho)]
            w = [sum(B[s][j] * sg[j] for j in range(r + 1)) % p
                 for s in range(rho)]
            if not any(w):
                if not any(u):
                    cf["univ"] += 1
                continue
            gam, ok = None, True
            for s in range(rho):
                if w[s]:
                    g = (-u[s]) * inv(w[s], p) % p
                    if gam is None:
                        gam = g
                    elif gam != g:
                        ok = False
                        break
                elif u[s]:
                    ok = False
                    break
            if ok and gam is not None:
                cf["cnt"][gam] = cf["cnt"].get(gam, 0) + 1
                L = cf["bad"].setdefault(gam, [])
                if len(L) < LOCCAP:
                    L.append(S)
    for cf in cfgs:
        q = cf["q"]
        mu1 = Cnr / (q ** rho)
        ps, hr, dK, dg, pr = cf["st"]
        isFG = pr and ps is not None and ps <= 2 * rho and hr == ps
        Tc = len(cf["bad"])
        lg = ledger(cf["bad"], n, R) if Tc >= 2 else None
        emit("  q=%-6d %-14s mu_1=%-11.5g T=%-6d T/q=%-9.6f"
             " 1-exp(-mu_1)=%.6f r+1=%d | p*=%s h_r=%d dimK0=%d deggcd=%d"
             " princ=%s FG=%s colclose=%d"
             % (q, cf["nm"], mu1, Tc, Tc / q, 1 - exp(-min(mu1, 700)), r + 1,
                ps, hr, dK, dg, pr, isFG, cf["univ"]))
        emit("        predictions: LB1 h_r=rho+1=%d dimK0=r-rho=%d"
             " p*=(R+2)/2=%d ; FG h_r=p*=2rho=%d dimK0=r+1-2rho=%d"
             % (rho + 1, r - rho, (R + 2) // 2, 2 * rho, r + 1 - 2 * rho))
        if lg:
            emit("        ledger: w*<=%d (R+1)-w*=%d T1=%d T2=%d maxspend=%s"
                 " e=%d CAP=%s T2<=CAP:%s"
                 % (lg["ws"], lg["fl"], lg["T1"], lg["T2"],
                    max(lg["sp"]) if lg["sp"] else "-", lg["e"], lg["cap"],
                    (lg["T2"] <= lg["cap"]) if lg["cap"] is not None
                    else "VACUOUS(floor<=0)"))
    emit("")


def main():
    emit("=== r35_fg_razor  e2b_shape2 ===")
    emit("PART A: second RATE-HALF shape (razor-faithful signs a>R+1, a-1>r)")
    run(22, 11, 2, 11, [101, 65537], "SHAPE-A")
    emit("PART B: rho=3 SEPARATING cells (k=1) -- 4rho<R holds but these are")
    emit("  NOT rate-half and have a-1 < r: declared non-faithful to the razor")
    emit("  in exactly the sign that governs p*(LB1).  rho=3 evidence only.")
    for (q, n, k, r) in [(17, 17, 1, 13), (19, 19, 1, 15), (23, 23, 1, 19)]:
        run(n, n - k, (n - k) - r, k, [q], "CELL")
    with open("notes/pilots_20260811/r35_fg_razor/e2b_results.txt", "w") as fh:
        fh.write("\n".join(OUT) + "\n")


main()
