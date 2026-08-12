#!/usr/bin/env python3
# r37_urand run 4:
#  PART A  the rho = 3 / rho = 4 SYMMETRIC-T secondary (anchor 1's parity
#          prediction: survival at rho=3, death at rho>=4).
#          Carrier derived here: T symmetric + e_1 = x^2 e_0 on a negation-closed
#          D makes every EVEN syndrome moment vanish (v_{-x} = -v_x for n even),
#          so row i of the pencil couples only sigma_j with i+j odd.  Rows 2s and
#          2s+1 carry the SAME y-vector Z^(s) = (y_{2s+1}, y_{2s+3}, ...), acting
#          on sigma^o and sigma^e respectively.  For the carrier
#              sigma = (X - x_0) * P(X^2)     (root set (A u -A) u {x_0}, deg r)
#          one has sigma^o = p and sigma^e = -x_0 p, so BOTH blocks reduce to the
#          same conditions on p and the count of independent conditions is
#          ceil(rho/2), i.e. ceil(rho/2) - 1 over-determination on gamma.
#          => survives at rho = 2 (count = C(m,(r-1)/2), x_0-INDEPENDENT),
#             dies at rho >= 3.   ANCHOR 1 PREDICTED SURVIVAL AT rho = 3.
#  PART B  fill the j = 4,5 gap my run-3 ladder skipped at rho = 4, and add a
#          THIRD field to the mu_n construction census.
# APPEND MODE.  Never piped through head.

import sys
import random
from math import comb
from itertools import combinations

OUT = "notes/pilots_20260811/r37_urand/g4_results.txt"
FH = open(OUT, "a")


def emit(s):
    FH.write(s + "\n")
    FH.flush()
    print(s)


def inv(a, q):
    return pow(a % q, q - 2, q)


def isprime(x):
    if x < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if x % p == 0:
            return x == p
    d = x - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        y = pow(a, d, x)
        if y in (1, x - 1):
            continue
        for _ in range(s - 1):
            y = y * y % x
            if y == x - 1:
                break
        else:
            return False
    return True


def find_prime_1modn(n, lo):
    x = lo + (1 - lo) % n
    while True:
        if x > lo and isprime(x):
            return x
        x += n


def subgroup_ordered(n, q):
    e = (q - 1) // n
    for g in range(2, q):
        h = pow(g, e, q)
        if pow(h, n // 2, q) != 1 and pow(h, n, q) == 1:
            D = []
            x = 1
            for _ in range(n):
                D.append(x)
                x = x * h % q
            if len(set(D)) == n:
                return D
    return None


def vvals(D, q):
    n = len(D)
    v = []
    for i in range(n):
        p = 1
        for j in range(n):
            if j != i:
                p = p * (D[i] - D[j]) % q
        v.append(inv(p, q))
    return v


def sigma_of(roots, q):
    sig = [1]
    for x in roots:
        ns = [0] * (len(sig) + 1)
        for j, c in enumerate(sig):
            ns[j + 1] = (ns[j + 1] + c) % q
            ns[j] = (ns[j] - x * c) % q
        sig = ns
    return sig


def slope_of(sig, y0, y1, rho, r, q):
    while len(sig) < r + 1:
        sig.append(0)
    uv = [sum(y0[i + j] * sig[j] for j in range(r + 1)) % q for i in range(rho)]
    wv = [sum(y1[i + j] * sig[j] for j in range(r + 1)) % q for i in range(rho)]
    if not any(uv) and not any(wv):
        return "CLOSE"
    if not any(wv):
        return None
    p = next(i for i in range(rho) if wv[i])
    g = (-uv[p] * inv(wv[p], q)) % q
    for i in range(rho):
        if (uv[i] + g * wv[i]) % q:
            return None
    return g


def symT_cell(tag, D, negof, k, rho, q, dom, fullcensus):
    n = len(D)
    R = n - k
    r = R - rho
    a = n - r
    faithful = (4 * rho < R) and (a > R + 1) and (a - 1 > r)
    emit("")
    emit("=" * 78)
    emit("SYM-T %s  n=%d k=%d R=%d rho=%d r=%d a=%d q=%d  %s" %
         (tag, n, k, R, rho, r, a, q, dom))
    emit("FAITHFUL 4rho<R=%s a>R+1=%s a-1>r=%s -> %s"
         % (4 * rho < R, a > R + 1, a - 1 > r, "FAITHFUL" if faithful else "NOT FAITHFUL"))
    if not faithful:
        emit("SKIPPED (faithfulness gate)")
        return
    if (r + 1) % 2:
        emit("SKIPPED: r+1 = %d is ODD, no symmetric T of size r+1 exists" % (r + 1))
        return
    # pick a symmetric T of size r+1 : (r+1)/2 elements and their negatives
    reps = []
    seen = set()
    for i in range(n):
        if D[i] in seen:
            continue
        seen.add(D[i])
        seen.add(D[negof[i]])
        reps.append(i)
    Tidx = []
    for i in reps[:(r + 1) // 2]:
        Tidx.append(i)
        Tidx.append(negof[i])
    Tset = set(Tidx)
    v = vvals(D, q)
    e0 = {i: 1 for i in Tidx}
    e1 = {i: D[i] * D[i] % q for i in Tidx}
    y0 = [0] * R
    y1 = [0] * R
    for i in Tidx:
        c0 = e0[i] * v[i] % q
        c1 = e1[i] * v[i] % q
        xp = 1
        for m in range(R):
            y0[m] = (y0[m] + c0 * xp) % q
            y1[m] = (y1[m] + c1 * xp) % q
            xp = xp * D[i] % q
    evenzero = all(y0[m] == 0 and y1[m] == 0 for m in range(0, R, 2))
    emit("  |T|=%d symmetric=%s ; PARITY STRUCTURE y_m = 0 for all EVEN m : %s"
         % (len(Tidx), all(negof[i] in Tset for i in Tidx), evenzero))
    emit("  predicted independent conditions on p = ceil(rho/2) = %d  -> "
         "over-determination on gamma = %d  (anchor-1 parity derivation said "
         "floor(rho/2) = %d)" % (-(-rho // 2), -(-rho // 2) - 1, rho // 2))
    # --- carrier sweep: sigma = (X - x_0) * P(X^2), root set (A u -A) u {x_0}
    half = (r - 1) // 2
    car_slopes = {}
    ncar = 0
    x0dep = []
    for A in combinations(reps, half):
        Aall = set()
        for i in A:
            Aall.add(i)
            Aall.add(negof[i])
        roots_sym = [D[i] for i in Aall]
        gset = set()
        for x0 in range(n):
            if x0 in Aall:
                continue
            ncar += 1
            sig = sigma_of(roots_sym + [D[x0]], q)
            g = slope_of(sig, y0, y1, rho, r, q)
            if g is not None and g != "CLOSE":
                car_slopes.setdefault(g, set()).add(tuple(sorted(Aall)))
                gset.add(g)
        if len(gset) == 1:
            x0dep.append(1)
        elif len(gset) > 1:
            x0dep.append(len(gset))
    emit("  CARRIER (X-x_0)P(X^2): #A = C(%d,%d) = %d ; locators swept = %d ; "
         "DISTINCT SLOPES = %d   [prediction at rho=2 : C(m,(r-1)/2) = %d]"
         % (len(reps), half, comb(len(reps), half), ncar, len(car_slopes),
            comb(len(reps), half)))
    emit("  A-blocks yielding exactly one x_0-INDEPENDENT slope: %d ; "
         "yielding >1 slope: %d" % (sum(1 for z in x0dep if z == 1),
                                    sum(1 for z in x0dep if z > 1)))
    emit("  VERDICT rho=%d : symmetric-T carrier %s"
         % (rho, "SURVIVES (%d slopes)" % len(car_slopes) if car_slopes else "DEAD (0 slopes)"))
    if fullcensus:
        y0s = [tuple(y0[i:i + r + 1]) for i in range(rho)]
        y1s = [tuple(y1[i:i + r + 1]) for i in range(rho)]
        slopes = {}
        close = [0]

        def rec(start, depth, poly, chosen):
            if depth == r:
                uv = [sum(x * y for x, y in zip(y0s[i], poly)) % q for i in range(rho)]
                wv = [sum(x * y for x, y in zip(y1s[i], poly)) % q for i in range(rho)]
                if not any(uv) and not any(wv):
                    close[0] += 1
                    return
                if not any(wv):
                    return
                p = next(i for i in range(rho) if wv[i])
                g = (-uv[p] * inv(wv[p], q)) % q
                for i in range(rho):
                    if (uv[i] + g * wv[i]) % q:
                        return
                S = set(chosen)
                fib = S <= Tset
                sym = all(negof[i] in S for i in S)
                rc = slopes.get(g)
                if rc is None:
                    slopes[g] = [fib, sym]
                else:
                    rc[0] = rc[0] or fib
                    rc[1] = rc[1] or sym
                return
            hi = n - (r - depth)
            for i in range(start, hi + 1):
                x = D[i]
                np_ = [0] * (depth + 2)
                for j in range(depth + 1):
                    c = poly[j]
                    if c:
                        np_[j + 1] = (np_[j + 1] + c) % q
                        np_[j] = (np_[j] - x * c) % q
                chosen.append(i)
                rec(i + 1, depth + 1, np_, chosen)
                chosen.pop()

        rec(0, 0, [1], [])
        T = len(slopes)
        Tf = sum(1 for s in slopes.values() if s[0])
        carrier_hits = sum(1 for g in slopes if g in car_slopes)
        emit("  FULL CENSUS C(%d,%d)=%d : T=%d  T_fib=%d  column-%s  "
             "slopes explained by the carrier = %d  residual = %d  "
             "null q*mu_1 = %.4g"
             % (n, r, comb(n, r), T, Tf, "FAR" if close[0] == 0 else "CLOSE(%d)" % close[0],
                carrier_hits, T - Tf - carrier_hits, comb(n, r) * q ** (1 - rho)))


# ---------------- PART B : construction j-gap ----------------
def kernel(rows, ncol, q):
    M = [r[:] for r in rows]
    piv = []
    rr = 0
    for c in range(ncol):
        p = None
        for i in range(rr, len(M)):
            if M[i][c]:
                p = i
                break
        if p is None:
            continue
        M[rr], M[p] = M[p], M[rr]
        iv = inv(M[rr][c], q)
        M[rr] = [a * iv % q for a in M[rr]]
        for i in range(len(M)):
            if i != rr and M[i][c]:
                f = M[i][c]
                M[i] = [(a - f * b) % q for a, b in zip(M[i], M[rr])]
        piv.append(c)
        rr += 1
    free = [c for c in range(ncol) if c not in piv]
    out = []
    for fc in free:
        vec = [0] * ncol
        vec[fc] = 1
        for i, c in enumerate(piv):
            vec[c] = (-M[i][fc]) % q
        out.append(vec)
    return out


def construct(tag, D, k, rho, q, jlist, tries=25, seed=7):
    n = len(D)
    R = n - k
    r = R - rho
    a = n - r
    emit("")
    emit("-" * 74)
    emit("CONSTRUCT-FILL %s n=%d k=%d R=%d rho=%d r=%d a=%d q=%d  FAITHFUL %s%s%s"
         % (tag, n, k, R, rho, r, a, q, 4 * rho < R, a > R + 1, a - 1 > r))
    emit("  parameter cap j <= (2(r+1)-1)/rho = %.3f" % ((2 * (r + 1) - 1) / rho))
    v = vvals(D, q)
    Widx = list(range(r + 1))
    Wset = set(Widx)
    offidx = [i for i in range(n) if i not in Wset]
    rng = random.Random(seed)
    for j in jlist:
        found = 0
        for tr in range(tries):
            Ps, As, gams = [], [], []
            used = set()
            ok = True
            for i in range(j):
                for _ in range(60):
                    P = tuple(sorted(rng.sample(offidx, rho)))
                    if P not in used:
                        used.add(P)
                        break
                else:
                    ok = False
                Ps.append(P)
                As.append(tuple(sorted(rng.sample(Widx, rho + 1))))
                gams.append(rng.randrange(2, q))
            if not ok or len(set(gams)) != j:
                continue
            ncol = 2 * (r + 1) + j
            rows = []
            for i in range(j):
                Y = [t for t in offidx if t not in set(Ps[i])]
                for xi in As[i]:
                    Z = 1
                    for t in Y:
                        Z = Z * (D[xi] - D[t]) % q
                    row = [0] * ncol
                    row[xi] = 1
                    row[r + 1 + xi] = gams[i] % q
                    row[2 * (r + 1) + i] = Z
                    rows.append(row)
            bas = kernel(rows, ncol, q)
            if not bas:
                continue
            for _ in range(60):
                coef = [rng.randrange(q) for _ in bas]
                sol = [0] * ncol
                for cc, bv in zip(coef, bas):
                    if cc:
                        for t in range(ncol):
                            sol[t] = (sol[t] + cc * bv[t]) % q
                e0 = sol[:r + 1]
                e1 = sol[r + 1:2 * (r + 1)]
                lam = sol[2 * (r + 1):]
                if any(l == 0 for l in lam):
                    continue
                if any(e0[t] == 0 and e1[t] == 0 for t in range(r + 1)):
                    continue
                ch = []
                for t in range(r + 1):
                    ch.append("inf" if e1[t] == 0 else e0[t] * inv(e1[t], q) % q)
                if len(set(ch)) != r + 1:
                    continue
                fib = set((-e0[t] * inv(e1[t], q)) % q for t in range(r + 1) if e1[t])
                if any(g in fib for g in gams):
                    continue
                y0 = [0] * R
                y1 = [0] * R
                for t in range(r + 1):
                    c0 = e0[t] * v[t] % q
                    c1 = e1[t] * v[t] % q
                    xp = 1
                    for m in range(R):
                        y0[m] = (y0[m] + c0 * xp) % q
                        y1[m] = (y1[m] + c1 * xp) % q
                        xp = xp * D[t] % q
                nver = 0
                for i in range(j):
                    S = sorted(set(Ps[i]) | (Wset - set(As[i])))
                    if len(S) != r:
                        continue
                    sig = sigma_of([D[t] for t in S], q)
                    if slope_of(sig[:], y0, y1, rho, r, q) == gams[i]:
                        nver += 1
                found = nver
                break
            if found:
                break
        emit("  j=%2d : engineered slopes verified = %d/%d %s"
             % (j, found, j, "OK" if found == j else "(FAILED)"))


def main():
    emit("")
    emit("################ RUN g4_sym.py ################")
    # ---------- PART A ----------
    QS = [65537, 999983]
    specs = [
        # (m, k, rho, fullcensus)  negation-closed integer domain {+-1..+-m}
        (11, 11, 2, True),    # S2 n=22 r=9  ANCHOR-1's rho=2 positive control
        (13, 13, 2, False),   # S5 n=26 r=11 second rho=2 shape
        (14, 14, 3, False),   # S3 n=28 r=11 rho=3   <-- THE DECIDING CELL
        (17, 17, 4, False),   # S4 n=34 r=13 rho=4
    ]
    for (m, k, rho, fc) in specs:
        n = 2 * m
        for q in QS:
            D = []
            for i in range(1, m + 1):
                D.append(i % q)
                D.append((-i) % q)
            negof = {i: (i ^ 1) for i in range(n)}
            symT_cell("intZ n=%d rho=%d" % (n, rho), D, negof, k, rho, q,
                      "D=negclosed{+-1..+-%d}" % m, fc and q == QS[0])
    # razor-faithful multiplicative-subgroup cross-checks
    for (n, k, rho, fc) in [(22, 11, 2, True), (28, 14, 3, False)]:
        q = find_prime_1modn(n, 300000)
        D = subgroup_ordered(n, q)
        if D is None:
            emit("no subgroup n=%d q=%d" % (n, q))
            continue
        idx = {D[i]: i for i in range(n)}
        negof = {i: idx[(-D[i]) % q] for i in range(n)}
        symT_cell("mu_%d rho=%d" % (n, rho), D, negof, k, rho, q,
                  "D=MULTIPLICATIVE SUBGROUP mu_%d < F_%d^*" % (n, q), fc)
    # ---------- PART B ----------
    emit("")
    emit("################ PART B : the j = 4,5 gap at rho = 4 ################")
    q = 999983
    m = 17
    D = [i % q for i in range(1, 14)] + [i % q for i in range(14, 18)] + \
        [(-i) % q for i in range(1, 18)]
    construct("intZ n=34 rho=4", D, 17, 4, q, [4, 5, 6])
    qq = find_prime_1modn(34, 500000)
    Dm = subgroup_ordered(34, qq)
    construct("mu_34 rho=4", Dm, 17, 4, qq, [4, 5, 6])
    qq2 = find_prime_1modn(20, 900000)
    Dm2 = subgroup_ordered(20, qq2)
    construct("mu_20 rho=2 THIRD FIELD", Dm2, 10, 2, qq2, [4, 8, 9])
    emit("################ END RUN g4_sym.py ################")


main()
FH.close()
