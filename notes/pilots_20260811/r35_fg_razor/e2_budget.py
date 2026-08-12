#!/usr/bin/env python3
"""r35_fg_razor D2: the key-equation budget on RATE-HALF replicas.

e1 used k=1 cells; those are separating (4rho < R) but NOT faithful to the
razor in the two signs that matter: the razor has a > R+1 and a-1 > r,
while k=1 gives a = 3..4 < r.  Here every cell is rate-half (k = n/2 = R,
a = R + rho, r = R - rho), so a > R+1 and a-1 > r as at the razor.

Exact bad-slope test (no field-size ceiling, no P* needed):
  sigma in ker M_r(y_0 + gamma y_1)  <=>  A.sigma + gamma B.sigma = 0
with A = M_r(y_0), B = M_r(y_1) both rho x (r+1).  For each sigma this is
rho linear equations in the SINGLE unknown gamma, so the bad-gamma set of
one locator is computed in O(rho).  That lets q sweep across the
first-moment threshold mu_1 = C(n,r)/q^rho = 1.
Stdlib only.
"""
import sys
from itertools import combinations
from math import comb, exp, log2

OUT = []


def emit(s=""):
    OUT.append(str(s))
    print(s)
    sys.stdout.flush()


def inv(a, p):
    return pow(a % p, p - 2, p)


def rref(M, p):
    M = [row[:] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    piv = []
    r = 0
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
    free = [c for c in range(ncols) if c not in piv]
    out = []
    for f in free:
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
    a = ptrim(a[:], p)
    m = ptrim(m[:], p)
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
    def frob(k):
        cur = [0, 1]
        for _ in range(k):
            e, res, base = p, [1], cur[:]
            while e:
                if e & 1:
                    res = pmod(pmul(res, base, p), f, p)
                base = pmod(pmul(base, base, p), f, p)
                e >>= 1
            cur = res
        return cur
    def sub_x(v):
        w = v[:] + [0] * max(0, 2 - len(v))
        w[1] = (w[1] - 1) % p
        return ptrim(w, p)
    if sub_x(frob(d)):
        return False
    m, pr = d, set()
    f2 = 2
    while f2 * f2 <= m:
        while m % f2 == 0:
            pr.add(f2)
            m //= f2
        f2 += 1
    if m > 1:
        pr.add(m)
    for l in pr:
        if len(pgcd(sub_x(frob(d // l)), f, p)) - 1 != 0:
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


def poly_from_roots(rs, p):
    f = [1]
    for a in rs:
        f = pmul(f, [(-a) % p, 1], p)
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
        s = 0
        for j in range(d):
            s = (s + P[j] * u[m - d + j]) % p
        u.append((-s) % p)
    return u[:R]


def hankel(y, i, R, p):
    return [[y[s + j] % p for j in range(i + 1)] for s in range(R - i)]


def pstar_and_K0(y0, y1, R, r, p):
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
    principal = False
    if K0 and g:
        dg = len(g) - 1
        sh = []
        for s in range(r - dg + 1):
            w = [0] * s + g[:]
            sh.append(w + [0] * (r + 1 - len(w)))
        principal = (rank(sh, p) == len(K0) and
                     rank(sh + [b[:] for b in K0], p) == len(K0))
    return ps, hr, K0, (len(g) - 1 if g else -1), principal


def bad_slopes(A, B, D, r, p, sample=None, rng_seed=12345):
    """Exact: returns dict gamma -> list of locator supports; plus
    the count of universal (column-close) locators."""
    out = {}
    universal = 0
    rho = len(A)
    if sample is None:
        it = combinations(D, r)
    else:
        import random
        rnd = random.Random(rng_seed)
        seen = set()
        it = []
        while len(it) < sample:
            S = tuple(sorted(rnd.sample(D, r)))
            if S not in seen:
                seen.add(S)
                it.append(S)
    for S in it:
        sig = poly_from_roots(S, p)
        sig = sig + [0] * (r + 1 - len(sig))
        u = [sum(A[s][j] * sig[j] for j in range(r + 1)) % p for s in range(rho)]
        w = [sum(B[s][j] * sig[j] for j in range(r + 1)) % p for s in range(rho)]
        if not any(w):
            if not any(u):
                universal += 1
            continue
        gam = None
        ok = True
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
            out.setdefault(gam, []).append(S)
    return out, universal


def ledger(badmap, n, R, r, D):
    """type-2 ledger functionals in far-CA symbols."""
    slopes = sorted(badmap)
    if len(slopes) < 2:
        return None
    # w* = min over distinct bad slopes and locator choices of |S_g u S_h|
    best = None
    for i in range(len(slopes)):
        for j in range(i + 1, len(slopes)):
            for Sg in badmap[slopes[i]]:
                for Sh in badmap[slopes[j]]:
                    u = len(set(Sg) | set(Sh))
                    if best is None or u < best[0]:
                        best = (u, slopes[i], slopes[j], set(Sg) | set(Sh))
    wstar, g1, g2, W = best
    floor_c2 = R + 1 - wstar
    t1 = t2 = 0
    spends = []
    for gam in slopes:
        # a slope is type-1 if SOME locator sits inside W
        if any(set(S) <= W for S in badmap[gam]):
            t1 += 1
        else:
            t2 += 1
            spends.append(min(len(set(S) - W) for S in badmap[gam]))
    dx = {}
    for gam in slopes:
        S = badmap[gam][0]
        for x in S:
            dx[x] = dx.get(x, 0) + 1
    e = max(dx.values()) if dx else 0
    cap = (((n - wstar) * e) // floor_c2) if floor_c2 > 0 else None
    return dict(wstar=wstar, W=sorted(W), floor=floor_c2, T1=t1, T2=t2,
                spends=spends, e=e, cap=cap, dxmax=e)


# ---------------- cells ----------------
# rate-half separating shapes: n = 2R, k = R, rho, r = R-rho, a = R+rho
SHAPES = [
    # (n, R, rho, [q list])
    (20, 10, 2, [23, 101, 349, 1009, 10007, 65537]),
    (22, 11, 2, [23, 701, 10007]),
]


def run_shape(n, R, rho, qs):
    k = n - R
    r = R - rho
    a = n - r
    Cnr = comb(n, r)
    emit("SHAPE n=%d k=%d R=%d rho=%d r=%d a=%d | rate=%s | 4rho=%d<R=%d:%s"
         " | a>R+1:%s (a-(R+1)=%d) | a-1>r:%s | C(n,r)=%d"
         % (n, k, R, rho, r, a, "1/2" if 2 * k == n else "?",
            4 * rho, R, 4 * rho < R, a > R + 1, a - (R + 1), a - 1 > r, Cnr))
    emit("   2rho=%d  floor(R/2)=%d  intermediate band (2rho, R/2] = %s"
         % (2 * rho, R // 2, list(range(2 * rho + 1, R // 2 + 1))))
    for q in qs:
        p = q
        D = list(range(n))
        v = dual_mults(D, p)
        mu1 = Cnr / (q ** rho)
        mu2 = Cnr / (q ** (2 * rho))
        emit("  --- q=%d   mu_1=C(n,r)/q^rho=%.6g   mu_2=%.6g   "
             "Poisson envelope 1-exp(-mu_1)=%.6f ---"
             % (q, mu1, mu2, 1 - exp(-min(mu1, 700))))
        # FG witness-B replica
        P1 = find_irred(rho, p)
        P2 = poly_from_roots(list(range(rho)), p)
        Pstar = pmul(P1, P2, p)
        y0, y1 = impulse(P1, R, p), impulse(P2, R, p)
        # LB1 replica
        T = list(range(r + 1))
        z1 = syn({t: 1 for t in T}, D, v, R, p)
        z0 = syn({t: (-t) % p for t in T}, D, v, R, p)
        for name, (u0, u1) in (("FG(witness B)", (y0, y1)), ("LB1", (z0, z1))):
            ps, hr, K0, dg, princ = pstar_and_K0(u0, u1, R, r, p)
            A = hankel(u0, r, R, p)
            B = hankel(u1, r, R, p)
            bm, univ = bad_slopes(A, B, D, r, p)
            Tcount = len(bm)
            sizes = sorted(len(x) for x in bm.values())
            lg = ledger(bm, n, R, r, D) if Tcount >= 2 else None
            isFG = princ and ps is not None and ps <= 2 * rho and hr == ps
            emit("    [%s] p*=%s h_r=%d dimK0=%d deggcd=%d principal=%s FG=%s"
                 "  colclose-locators=%d (column-far=%s)"
                 % (name, ps, hr, len(K0), dg, princ, isFG, univ, univ == 0))
            emit("       T=%d of q=%d  (T/q=%.6f)   r+1=%d   list sizes"
                 " min/med/max = %s/%s/%s   sum=%d  [predicted mean list"
                 " mu_1=%.4g]"
                 % (Tcount, q, Tcount / q, r + 1,
                    sizes[0] if sizes else 0,
                    sizes[len(sizes) // 2] if sizes else 0,
                    sizes[-1] if sizes else 0, sum(sizes), mu1))
            if lg:
                emit("       ledger: w*=%d  (R+1)-w*=%d  T1=%d T2=%d  "
                     "max spend=%s  d_x max=e=%d  CAP=floor((n-w*)e/((R+1)-w*))"
                     "=%s   T2<=CAP:%s"
                     % (lg["wstar"], lg["floor"], lg["T1"], lg["T2"],
                        (max(lg["spends"]) if lg["spends"] else "-"),
                        lg["e"], lg["cap"],
                        (lg["T2"] <= lg["cap"]) if lg["cap"] is not None
                        else "vacuous(floor<=0)"))
        emit("")


def main():
    emit("=== r35_fg_razor  e2_budget  (D2: rate-half replicas) ===")
    emit("")
    for (n, R, rho, qs) in SHAPES:
        run_shape(n, R, rho, qs)
    with open("notes/pilots_20260811/r35_fg_razor/e2_results.txt", "w") as fh:
        fh.write("\n".join(OUT) + "\n")


main()
