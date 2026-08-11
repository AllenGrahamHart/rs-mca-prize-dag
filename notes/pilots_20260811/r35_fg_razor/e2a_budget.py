#!/usr/bin/env python3
"""r35_fg_razor D2 (a): the key-equation budget on a RATE-HALF replica shape,
swept across the first-moment threshold mu_1 = C(n,r)/q^rho = 1.

e1 used k=1 cells; those are separating (4rho < R) but NOT faithful to the
razor in the two signs that matter: the razor has a > R+1 and a-1 > r,
while k=1 gives a = 3..4 < r.  Every cell here is rate-half
(k = n/2 = R, rho, r = R-rho, a = R+rho), so a > R+1 and a-1 > r as at
the razor, and 4rho < R (separating: the intermediate band is nonempty).

Exact bad-slope test (no field-size ceiling, no P* needed):
  sigma in ker M_r(y_0 + gamma y_1) <=> A.sigma + gamma B.sigma = 0,
A = M_r(y_0), B = M_r(y_1) both rho x (r+1): rho linear equations in the
SINGLE unknown gamma, so one locator's bad-gamma set costs O(rho).
Ledger locator lists are capped (LOCCAP) and the cap is reported.
Stdlib only.
"""
import sys
from itertools import combinations
from math import comb, exp, log2

OUT = []
LOCCAP = 24            # locators retained per slope for the ledger


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


def nullspace(M, p, ncols):
    if not M:
        return [[1 if i == j else 0 for i in range(ncols)] for j in range(ncols)]
    Rm, piv = rref(M, p)
    out = []
    for f in [c for c in range(ncols) if c not in piv]:
        v = [0] * ncols
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


def poly_from_roots_int(rs):
    f = [1]
    for a in rs:
        g = [0] * (len(f) + 1)
        for i, ci in enumerate(f):
            g[i] -= a * ci
            g[i + 1] += ci
        f = g
    return f


def dual_mults(D, p):
    v = []
    for x in D:
        pr = 1
        for y in D:
            if y != x:
                pr = (pr * (x - y)) % p
        v.append(inv(pr, p))
    return v


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


def ledger(badmap, counts, n, R, r):
    slopes = sorted(badmap)
    if len(slopes) < 2:
        return None
    best = None
    for i in range(len(slopes)):
        for j in range(i + 1, len(slopes)):
            for Sg in badmap[slopes[i]]:
                sg = set(Sg)
                for Sh in badmap[slopes[j]]:
                    u = len(sg | set(Sh))
                    if best is None or u < best[0]:
                        best = (u, sg | set(Sh))
    wstar, W = best
    fl = R + 1 - wstar
    t1 = t2 = 0
    spends = []
    for gam in slopes:
        if any(set(S) <= W for S in badmap[gam]):
            t1 += 1
        else:
            t2 += 1
            spends.append(min(len(set(S) - W) for S in badmap[gam]))
    dx = {}
    for gam in slopes:
        for x in badmap[gam][0]:
            dx[x] = dx.get(x, 0) + 1
    e = max(dx.values()) if dx else 0
    cap = ((n - wstar) * e) // fl if fl > 0 else None
    return dict(wstar=wstar, floor=fl, T1=t1, T2=t2, spends=spends, e=e, cap=cap)


N, R, RHO = 20, 10, 2
QS = [23, 101, 349, 1009, 10007, 65537]


def main():
    n, R_, rho = N, R, RHO
    k, r = n - R_, R_ - RHO
    a = n - r
    Cnr = comb(n, r)
    D = list(range(n))
    emit("=== r35_fg_razor  e2a_budget  (rate-half shape, q sweep) ===")
    emit("SHAPE n=%d k=%d R=%d rho=%d r=%d a=%d | rate 1/2:%s | 4rho=%d<R=%d:%s"
         " | a>R+1:%s | a-1>r:%s | C(n,r)=%d"
         % (n, k, R_, rho, r, a, 2 * k == n, 4 * rho, R_, 4 * rho < R_,
            a > R_ + 1, a - 1 > r, Cnr))
    emit("  2rho=%d floor(R/2)=%d intermediate band (2rho,R/2] = %s ;"
         " (R+1)-a = %d (negative, as at the razor)"
         % (2 * rho, R_ // 2, list(range(2 * rho + 1, R_ // 2 + 1)), R_ + 1 - a))
    emit("  LOCCAP = %d locators retained per slope for the ledger"
         " (w* is therefore an UPPER bound on the true w*)" % LOCCAP)
    emit("")
    cfgs = []
    for q in QS:
        p = q
        v = dual_mults(D, p)
        P1 = find_irred(rho, p)
        P2 = [1]
        for t in range(rho):
            P2 = pmul(P2, [(-t) % p, 1], p)
        y0, y1 = impulse(P1, R_, p), impulse(P2, R_, p)
        T = list(range(r + 1))
        z1 = syn({t: 1 for t in T}, D, v, R_, p)
        z0 = syn({t: (-t) % p for t in T}, D, v, R_, p)
        for name, (u0, u1) in (("FG(witness B)", (y0, y1)), ("LB1", (z0, z1))):
            cfgs.append(dict(q=q, p=p, name=name,
                             A=hankel(u0, r, R_, p), B=hankel(u1, r, R_, p),
                             st=structure(u0, u1, R_, r, p),
                             bad={}, cnt={}, univ=0))
    emit("  ... enumerating C(%d,%d) = %d locators once, all %d configs"
         % (n, r, Cnr, len(cfgs)))
    for S in combinations(D, r):
        sig0 = poly_from_roots_int(S)
        for cf in cfgs:
            p, A, B = cf["p"], cf["A"], cf["B"]
            sig = [c % p for c in sig0]
            u = [sum(A[s][j] * sig[j] for j in range(r + 1)) % p
                 for s in range(rho)]
            w = [sum(B[s][j] * sig[j] for j in range(r + 1)) % p
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
                lst = cf["bad"].setdefault(gam, [])
                if len(lst) < LOCCAP:
                    lst.append(S)
    emit("")
    for cf in cfgs:
        q, rho_ = cf["q"], rho
        mu1 = Cnr / (q ** rho_)
        ps, hr, dK, dg, princ = cf["st"]
        isFG = princ and ps is not None and ps <= 2 * rho_ and hr == ps
        Tc = len(cf["bad"])
        sizes = sorted(cf["cnt"].values())
        lg = ledger(cf["bad"], cf["cnt"], n, R_, r) if Tc >= 2 else None
        emit("q=%-6d %-14s mu_1=%-11.5g  T=%-6d T/q=%-9.6f  1-exp(-mu_1)=%.6f"
             "  r+1=%d" % (q, cf["name"], mu1, Tc, Tc / q,
                           1 - exp(-min(mu1, 700)), r + 1))
        emit("        p*=%s h_r=%d dimK0=%d deggcd=%d principal=%s FG=%s"
             " col-close locators=%d (column-far=%s)"
             % (ps, hr, dK, dg, princ, isFG, cf["univ"], cf["univ"] == 0))
        emit("        list sizes min/med/max = %s/%s/%s  total pairs=%d"
             "  (mean list over bad slopes = %.4g ; mu_1 = %.4g)"
             % (sizes[0] if sizes else 0,
                sizes[len(sizes) // 2] if sizes else 0,
                sizes[-1] if sizes else 0, sum(sizes),
                (sum(sizes) / Tc) if Tc else 0, mu1))
        if lg:
            emit("        ledger: w*<=%d  (R+1)-w*=%d  T1=%d T2=%d  max spend=%s"
                 "  e=max d_x=%d  CAP=%s  T2<=CAP:%s"
                 % (lg["wstar"], lg["floor"], lg["T1"], lg["T2"],
                    max(lg["spends"]) if lg["spends"] else "-", lg["e"],
                    lg["cap"],
                    (lg["T2"] <= lg["cap"]) if lg["cap"] is not None
                    else "VACUOUS(floor<=0)"))
        emit("")
    with open("notes/pilots_20260811/r35_fg_razor/e2a_results.txt", "w") as fh:
        fh.write("\n".join(OUT) + "\n")


main()
