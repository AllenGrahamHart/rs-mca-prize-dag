#!/usr/bin/env python3
# r37_urand run 5 (closing run):
#  (A) are the 6 / 7 surviving symmetric-T carrier slopes at rho = 3,4 exactly
#      the FIBRE slopes {-1/t^2 : t in T} ?  (decides D3b)
#  (B) a rho = 3 engineered pencil, FULL census C(26,10) = 5,311,735 :
#      column-farness + exact T = (r+1) + j ?   (the construction at rho > 2)
#  (C) razor closed forms, incl. C(128,63) vs C(127,64).
# APPEND MODE.  Never piped through head.

import sys
import random
from math import comb, log2
from itertools import combinations

OUT = "notes/pilots_20260811/r37_urand/g5_results.txt"
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
    sig = sig[:]
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


# ------------------------------------------------------------------ (A)
def symT_fibcheck(m, k, rho, q):
    n = 2 * m
    R = n - k
    r = R - rho
    a = n - r
    D = []
    for i in range(1, m + 1):
        D.append(i % q)
        D.append((-i) % q)
    negof = {i: i ^ 1 for i in range(n)}
    reps = [2 * i for i in range(m)]
    Tidx = []
    for i in reps[:(r + 1) // 2]:
        Tidx.append(i)
        Tidx.append(negof[i])
    v = vvals(D, q)
    y0 = [0] * R
    y1 = [0] * R
    for i in Tidx:
        c0 = v[i] % q
        c1 = v[i] * D[i] % q * D[i] % q
        xp = 1
        for mm in range(R):
            y0[mm] = (y0[mm] + c0 * xp) % q
            y1[mm] = (y1[mm] + c1 * xp) % q
            xp = xp * D[i] % q
    fib = set()
    for i in Tidx:
        fib.add((-inv(D[i] * D[i] % q, q)) % q)
    half = (r - 1) // 2
    car = set()
    for A in combinations(reps, half):
        Aall = set()
        for i in A:
            Aall.add(i)
            Aall.add(negof[i])
        rs = [D[i] for i in Aall]
        for x0 in range(n):
            if x0 in Aall:
                continue
            g = slope_of(sigma_of(rs + [D[x0]], q), y0, y1, rho, r, q)
            if g is not None and g != "CLOSE":
                car.add(g)
    emit("  n=%d k=%d R=%d rho=%d r=%d a=%d q=%d FAITHFUL(%s,%s,%s)"
         % (n, k, R, rho, r, a, q, 4 * rho < R, a > R + 1, a - 1 > r))
    emit("    fibre slopes {-1/t^2 : t in T} : %d   carrier slopes : %d   "
         "carrier SUBSET of fibre : %s   fibre SUBSET of carrier : %s   "
         "EXCESS (carrier \\ fibre) = %d"
         % (len(fib), len(car), car <= fib, fib <= car, len(car - fib)))


# ------------------------------------------------------------------ (B)
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
        M[rr] = [x * iv % q for x in M[rr]]
        for i in range(len(M)):
            if i != rr and M[i][c]:
                f = M[i][c]
                M[i] = [(x - f * y) % q for x, y in zip(M[i], M[rr])]
        piv.append(c)
        rr += 1
    out = []
    for fc in [c for c in range(ncol) if c not in piv]:
        vec = [0] * ncol
        vec[fc] = 1
        for i, c in enumerate(piv):
            vec[c] = (-M[i][fc]) % q
        out.append(vec)
    return out


def construct_and_census(n, k, rho, q, j, seed=11):
    D = subgroup_ordered(n, q)
    R = n - k
    r = R - rho
    a = n - r
    v = vvals(D, q)
    Widx = list(range(r + 1))
    Wset = set(Widx)
    off = [i for i in range(n) if i not in Wset]
    rng = random.Random(seed)
    for tr in range(40):
        Ps, As, gams, used = [], [], [], set()
        for i in range(j):
            for _ in range(60):
                P = tuple(sorted(rng.sample(off, rho)))
                if P not in used:
                    used.add(P)
                    break
            Ps.append(P)
            As.append(tuple(sorted(rng.sample(Widx, rho + 1))))
            gams.append(rng.randrange(2, q))
        if len(set(gams)) != j:
            continue
        ncol = 2 * (r + 1) + j
        rows = []
        for i in range(j):
            Y = [t for t in off if t not in set(Ps[i])]
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
            ch = ["inf" if e1[t] == 0 else e0[t] * inv(e1[t], q) % q
                  for t in range(r + 1)]
            if len(set(ch)) != r + 1:
                continue
            fibs = set((-e0[t] * inv(e1[t], q)) % q for t in range(r + 1) if e1[t])
            if any(g in fibs for g in gams):
                continue
            y0 = [0] * R
            y1 = [0] * R
            for t in range(r + 1):
                c0 = e0[t] * v[t] % q
                c1 = e1[t] * v[t] % q
                xp = 1
                for mm in range(R):
                    y0[mm] = (y0[mm] + c0 * xp) % q
                    y1[mm] = (y1[mm] + c1 * xp) % q
                    xp = xp * D[t] % q
            y0s = [tuple(y0[i:i + r + 1]) for i in range(rho)]
            y1s = [tuple(y1[i:i + r + 1]) for i in range(rho)]
            slopes = {}
            close = [0]

            def rec(start, depth, poly, chosen):
                if depth == r:
                    uv = [sum(x * y for x, y in zip(y0s[i], poly)) % q
                          for i in range(rho)]
                    wv = [sum(x * y for x, y in zip(y1s[i], poly)) % q
                          for i in range(rho)]
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
                    rc = slopes.get(g)
                    fb = S <= Wset
                    if rc is None:
                        slopes[g] = fb
                    else:
                        slopes[g] = rc or fb
                    return
                hi = n - (r - depth)
                for i in range(start, hi + 1):
                    x = D[i]
                    np_ = [0] * (depth + 2)
                    for jj in range(depth + 1):
                        c = poly[jj]
                        if c:
                            np_[jj + 1] = (np_[jj + 1] + c) % q
                            np_[jj] = (np_[jj] - x * c) % q
                    chosen.append(i)
                    rec(i + 1, depth + 1, np_, chosen)
                    chosen.pop()

            rec(0, 0, [1], [])
            T = len(slopes)
            Tf = sum(1 for b in slopes.values() if b)
            hit = sum(1 for g in gams if g in slopes)
            emit("  mu_%d k=%d R=%d rho=%d r=%d a=%d q=%d j=%d FAITHFUL(%s,%s,%s)"
                 % (n, k, R, rho, r, a, q, j, 4 * rho < R, a > R + 1, a - 1 > r))
            emit("    FULL CENSUS C(%d,%d)=%d : T=%d  T_fib=%d  T_rand=%d  "
                 "r+1=%d  excess=%+d  engineered slopes present=%d/%d  "
                 "column-%s  null q*mu_1=%.4g"
                 % (n, r, comb(n, r), T, Tf, T - Tf, r + 1, T - (r + 1), hit, j,
                    "FAR" if close[0] == 0 else "CLOSE(%d)" % close[0],
                    comb(n, r) * q ** (1 - rho)))
            return
    emit("  no valid pencil found")


# ------------------------------------------------------------------ (C)
def razor():
    n = 2 ** 41
    k = 2 ** 40
    R = n - k
    rho = 2 ** 34
    r = R - rho
    a = k + rho
    emit("")
    emit("RAZOR CLOSED FORMS  n=2^41=%d  k=R=2^40=%d  rho=2^34=%d  r=%d  a=%d"
         % (n, k, rho, r, a))
    emit("  FAITHFUL 4rho<R=%s  a>R+1=%s  a-1>r=%s"
         % (4 * rho < R, a > R + 1, a - 1 > r))
    emit("  r+1 = %d = 2^%.6f" % (r + 1, log2(r + 1)))
    emit("  n/rho = %d   r/rho = %d   k/rho = %d" % (n // rho, r // rho, k // rho))
    cap_a = (2 * (r + 1) - 1) / rho
    cap_b = 2 * (r + 1) / (rho - 1)
    emit("  U-RAND PARAMETER CAP  j <= (2(r+1)-1)/rho = %.10f  -> floor = %d"
         % (cap_a, int(cap_a)))
    emit("  (registered variant 2(r+1)/(rho-1) = %.10f -> floor = %d ; 2r/rho = %d)"
         % (cap_b, int(cap_b), 2 * r // rho))
    Tmax = r + 1 + int(cap_a)
    emit("  => heuristic B_ca^far(k+2^34) <= r+1+%d = %d = 2^%.6f"
         % (int(cap_a), Tmax, log2(Tmax)))
    emit("  => PROVED-BY-CONSTRUCTION floor (if the construction transports):"
         " B_ca^far >= r+1+j for j up to %d" % int(cap_a))
    emit("  over-determination per U-rand slope = rho-1 = %d" % (rho - 1))
    emit("  over-determination per U-sym slope  = ceil(rho/2)-1 = %d" % (rho // 2 - 1 + rho % 2))
    emit("  f-optimisation: T(f) <= r/f+1 + (2(r+f)-1)/rho")
    for f in (1, 2, 4, 2 ** 17, 2 ** 34):
        val = r // f + 1 + int((2 * (r + f) - 1) / rho)
        emit("      f=%-12d  T <= %d = 2^%.6f" % (f, val, log2(val)))
    emit("  B*(q) = floor(q/2^128) at q=2^167 : %d = 2^39 ; (r+1)/2^39 = %.6f "
         "= 2^%.6f" % (2 ** 39, (r + 1) / 2 ** 39, log2((r + 1) / 2 ** 39)))
    emit("  (r+1+%d)/2^39 = %.9f = 2^%.9f" % (int(cap_a), Tmax / 2 ** 39,
                                              log2(Tmax / 2 ** 39)))
    c12863 = comb(128, 63)
    c12764 = comb(127, 64)
    c12763 = comb(127, 63)
    emit("")
    emit("  C(128,63) = %d = 2^%.6f" % (c12863, log2(c12863)))
    emit("  C(127,64) = %d = 2^%.6f" % (c12764, log2(c12764)))
    emit("  C(127,63) = C(127,64) : %s" % (c12763 == c12764))
    emit("  C(128,63)/C(127,64) = 128/65 exactly : %s   value %.10f = 2^%.6f"
         % (c12863 * 65 == c12764 * 128, c12863 / c12764, log2(c12863 / c12764)))
    emit("  C(128,63) - C(127,64) = C(127,62) : %s"
         % (c12863 - c12764 == comb(127, 62)))
    emit("  NEAR-COINCIDENCE CHECK (registered A-1): log2(128/65) = %.6f  vs  "
         "log2((r+1)/2^39) = %.6f  -> EQUAL? %s"
         % (log2(128 / 65), log2((r + 1) / 2 ** 39),
            abs(log2(128 / 65) - log2((r + 1) / 2 ** 39)) < 1e-9))
    emit("  T_sym carrier at M=rho : C(n/rho, r/rho) = C(128,63) ; banked qcore "
         "plateau at sigma=M-1 : C(n/M-1, k/M) = C(127,64)")
    for lq in (128, 167, 256):
        lm = log2(comb(n, r)) - rho * lq if False else None
    from math import lgamma
    lgC = (lgamma(n + 1) - lgamma(r + 1) - lgamma(n - r + 1)) / 0.6931471805599453
    emit("  log2 C(n,r) = %.2f ; log2 mu_1 at q=2^128/2^167/2^256 = %.6e / %.6e / %.6e"
         % (lgC, lgC - 128 * rho, lgC - 167 * rho, lgC - 256 * rho))


def main():
    emit("")
    emit("################ RUN g5_close.py ################")
    emit("(A) SYMMETRIC-T at rho>=3 : are the surviving carrier slopes the FIBRE slopes?")
    symT_fibcheck(14, 14, 3, 65537)
    symT_fibcheck(14, 14, 3, 999983)
    symT_fibcheck(17, 17, 4, 65537)
    symT_fibcheck(17, 17, 4, 999983)
    symT_fibcheck(11, 11, 2, 999983)      # rho=2 positive control
    emit("")
    emit("(B) rho=3 ENGINEERED PENCIL, FULL CENSUS (column-farness + exact T)")
    q26 = find_prime_1modn(26, 200000)
    construct_and_census(26, 13, 3, q26, 6)
    razor()
    emit("################ END RUN g5_close.py ################")


main()
FH.close()
