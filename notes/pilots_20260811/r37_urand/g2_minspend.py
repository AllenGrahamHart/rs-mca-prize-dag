#!/usr/bin/env python3
# r37_urand run 2: the MINIMAL-SPEND U-rand carrier, exactly.
#
# Derivation (PREREG R2g/R2h): at f = |W|-r = 1 and minimal spend t = rho the
# mediating codeword c must be a MINIMUM-weight codeword of the RS code
# C = {g|_D : deg g <= k-1}, wt(c) = R+1, supp(c) ⊇ W.  Hence
#     c = lambda * Z_Y ,  Z_Y(x) = prod_{y in Y}(x-y) ,  Y ⊂ D\W , |Y| = k-1 ,
# and the off-W part of the locator is exactly P := (D\W)\Y, |P| = rho.
# The slope condition is
#     lambda Z_Y(x) + e_0(x) + gamma e_1(x) = 0   for all x in A ⊆ W, |A| = rho+1
# i.e. the points chi_Y(x) = [Z_Y(x) : e_0(x) : e_1(x)] in P^2 have rho+1
# COLLINEAR members.  With e_0 = 1, e_1 = x^d this is plane collinearity of
# {(x^d, Z_Y(x)) : x in A}.
#
# We enumerate the carrier EXACTLY OVER THE INTEGERS (so a hit is field-size
# independent, i.e. STRUCTURAL) and separately verify each hit by the direct
# pencil test (M_0 + gamma M_1) sigma = 0 at TWO fields.
# APPEND MODE.  Never piped through head.

import sys
from math import comb, gcd
from itertools import combinations
from fractions import Fraction

OUT = "notes/pilots_20260811/r37_urand/g2_results.txt"
FH = open(OUT, "a")


def emit(s):
    FH.write(s + "\n")
    FH.flush()
    print(s)


def inv(a, q):
    return pow(a % q, q - 2, q)


def linekey(x1, y1, x2, y2):
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    g = gcd(gcd(abs(a), abs(b)), abs(c))
    if g:
        a //= g
        b //= g
        c //= g
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return (a, b, c)


def verify_at_field(Dz, Wz, Sz, gam_num, gam_den, dexp, R, rho, r, q):
    """direct pencil test at F_q: build y_0,y_1 from (e_0,e_1) on W and test
       (M_0 + gamma M_1) sigma_S = 0 for sigma_S = prod_{x in S}(X-x)."""
    n = len(Dz)
    D = [z % q for z in Dz]
    v = []
    for i in range(n):
        p = 1
        for j in range(n):
            if j != i:
                p = p * (D[i] - D[j]) % q
        v.append(inv(p, q))
    idx = {Dz[i]: i for i in range(n)}
    y0 = [0] * R
    y1 = [0] * R
    for w in Wz:
        i = idx[w]
        c0 = v[i] % q
        c1 = v[i] * pow(D[i], dexp, q) % q
        xp = 1
        for m in range(R):
            y0[m] = (y0[m] + c0 * xp) % q
            y1[m] = (y1[m] + c1 * xp) % q
            xp = xp * D[i] % q
    if gam_den % q == 0:
        return None
    gam = gam_num % q * inv(gam_den, q) % q
    sig = [1]
    for s in Sz:
        ns = [0] * (len(sig) + 1)
        for j, cj in enumerate(sig):
            ns[j + 1] = (ns[j + 1] + cj) % q
            ns[j] = (ns[j] - (s % q) * cj) % q
        sig = ns
    while len(sig) < r + 1:
        sig.append(0)
    ok = True
    for i in range(rho):
        s = sum((y0[i + j] + gam * y1[i + j]) * sig[j] for j in range(r + 1)) % q
        if s:
            ok = False
    # also confirm it is NOT realisable inside W (i.e. genuinely U-rand):
    return ok, gam


def run(tag, m, k, rho, dexp, negclosed, qs, maxreport=12):
    n = 2 * m
    R = n - k
    r = R - rho
    a = n - r
    faithful = (4 * rho < R) and (a > R + 1) and (a - 1 > r)
    if negclosed:
        Dz = []
        for i in range(1, m + 1):
            Dz.append(i)
            Dz.append(-i)
    else:
        Dz = list(range(1, n + 1))
    Wz = sorted([z for z in Dz if z > 0])[:r + 1]
    offW = [z for z in Dz if z not in set(Wz)]
    nY = comb(len(offW), rho)
    emit("")
    emit("=" * 78)
    emit("MINSPEND %s  n=%d k=%d R=%d rho=%d r=%d a=%d  D=%s  e1=x^%d"
         % (tag, n, k, R, rho, r, a,
            "negclosed{+-1..+-%d}" % m if negclosed else "{1..%d}" % n, dexp))
    emit("FAITHFUL 4rho<R=%s a>R+1=%s a-1>r=%s -> %s"
         % (4 * rho < R, a > R + 1, a - 1 > r, "FAITHFUL" if faithful else "NOT FAITHFUL"))
    if not faithful:
        emit("SKIPPED (faithfulness gate)")
        return
    emit("|W|=%d  |D\\W|=%d  #Y (=choose P, |P|=rho) = C(%d,%d) = %d ; need %d collinear"
         % (len(Wz), len(offW), len(offW), rho, nY, rho + 1))
    emit("carrier size = #Y * C(|W|,rho+1) = %d * %d = %d ; per-config null = q^-(rho-1)"
         % (nY, comb(len(Wz), rho + 1), nY * comb(len(Wz), rho + 1)))
    hits = []
    nlines = 0
    for P in combinations(offW, rho):
        Ps = set(P)
        Y = [z for z in offW if z not in Ps]
        pts = []
        for x in Wz:
            Z = 1
            for y in Y:
                Z *= (x - y)
            pts.append((x ** dexp, Z, x))
        cnt = {}
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                kk = linekey(pts[i][0], pts[i][1], pts[j][0], pts[j][1])
                cnt.setdefault(kk, set()).update((i, j))
        for kk, members in cnt.items():
            if len(members) >= rho + 1:
                nlines += 1
                A = sorted(members)
                aa, bb, cc = kk
                # line: aa*X + bb*Y + cc = 0 with X = x^d, Y = Z_Y(x)
                # i.e. bb*Z + aa*x^d + cc = 0 -> lambda=bb, gamma=aa, const=cc
                # normalise to lambda*Z + e_0 + gamma*e_1 = 0  (e_0=1):
                if cc == 0:
                    continue                       # degenerate: no e_0 component
                lam = Fraction(bb, cc)
                gam = Fraction(aa, cc)
                Aset = [Wz[i] for i in A]
                Sz = sorted(Ps) + [w for w in Wz if w not in set(Aset)]
                hits.append((tuple(sorted(Ps)), tuple(Aset), lam, gam, tuple(Sz), len(A)))
    emit("INTEGER-COLLINEAR CONFIGURATIONS FOUND: %d  (lines with >= rho+1 points, over Z)"
         % len(hits))
    gams = sorted(set(h[3] for h in hits))
    emit("DISTINCT RATIONAL SLOPES: %d   %s"
         % (len(gams), " ".join(str(g) for g in gams[:20])))
    for h in hits[:maxreport]:
        P, A, lam, gam, Sz, la = h
        emit("  P=%s A=%s |A|=%d lambda=%s gamma=%s |S|=%d S=%s"
             % (list(P), list(A), la, lam, gam, len(Sz), list(Sz)))
        if len(Sz) != r:
            emit("      (|S| != r : |A| > rho+1, locator under-full; padded check skipped)")
            continue
        for q in qs:
            res = verify_at_field(Dz, Wz, Sz, gam.numerator, gam.denominator,
                                  dexp, R, rho, r, q)
            if res is None:
                emit("      q=%d : gamma denominator divisible by q, skipped" % q)
            else:
                ok, gq = res
                emit("      q=%d : gamma=%d  PENCIL TEST (M_0+gamma M_1)sigma=0 : %s"
                     % (q, gq, ok))
    return len(hits), len(gams)


def main():
    emit("")
    emit("################ RUN g2_minspend.py ################")
    QS = [65537, 999983]
    # rho = 2, two shapes, two families, negation-closed
    run("C1/F1 rho=2 n=20", 10, 10, 2, 1, True, QS)
    run("C1/F2 rho=2 n=20", 10, 10, 2, 2, True, QS)
    run("C2/F1 rho=2 n=24", 12, 12, 2, 1, True, QS)
    run("C2/F2 rho=2 n=24", 12, 12, 2, 2, True, QS)
    # CONTROL: same shapes on a NON negation-closed domain
    run("K1/F1 rho=2 n=20 CONTROL D={1..20}", 10, 10, 2, 1, False, QS)
    run("K1/F2 rho=2 n=20 CONTROL D={1..20}", 10, 10, 2, 2, False, QS)
    run("K2/F1 rho=2 n=24 CONTROL D={1..24}", 12, 12, 2, 1, False, QS)
    # rho = 3
    run("C3/F1 rho=3 n=26", 13, 13, 3, 1, True, QS)
    run("C3/F2 rho=3 n=26", 13, 13, 3, 2, True, QS)
    run("K3/F1 rho=3 n=26 CONTROL D={1..26}", 13, 13, 3, 1, False, QS)
    # rho = 4
    run("C4/F1 rho=4 n=34", 17, 17, 4, 1, True, QS)
    run("C4/F2 rho=4 n=34", 17, 17, 4, 2, True, QS)
    emit("################ END RUN g2_minspend.py ################")


main()
FH.close()
