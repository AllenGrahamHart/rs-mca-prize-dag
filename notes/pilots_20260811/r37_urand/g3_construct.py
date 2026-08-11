#!/usr/bin/env python3
# r37_urand run 3: CAN THE ADVERSARY ENGINEER U-rand SLOPES TO ORDER?
#
# PREREG R2i predicts T_rand <~ 2(r+1)/rho by parameter counting:
#   unknowns  = e_0,e_1 on W (2(r+1)) + lambda_1..lambda_j
#   equations = j*(rho+1)   [ lambda_i Z_i(x) + e_0(x) + gamma_i e_1(x) = 0, x in A_i ]
#   solvable while  j*rho <= 2(r+1) - 1.
# We SOLVE that system, build the pencil, and then run the exhaustive census to
# see whether T = (r+1) + j really holds, i.e. whether Statement U is false by a
# constructible additive term.  Two domains: negation-closed integers AND the
# razor-faithful multiplicative subgroup mu_n of F_q^*.
# APPEND MODE.  Never piped through head.

import sys
import random
from math import comb
from itertools import combinations

OUT = "notes/pilots_20260811/r37_urand/g3_results.txt"
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


def subgroup(n, q):
    """the order-n multiplicative subgroup of F_q^*, q = 1 mod n."""
    e = (q - 1) // n
    for g in range(2, q):
        h = pow(g, e, q)
        if pow(h, n // 2, q) != 1 and pow(h, n, q) == 1:
            S = set()
            x = 1
            for _ in range(n):
                S.add(x)
                x = x * h % q
            if len(S) == n:
                return sorted(S), h
    return None, None


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
    basis = []
    for fc in free:
        vec = [0] * ncol
        vec[fc] = 1
        for i, c in enumerate(piv):
            vec[c] = (-M[i][fc]) % q
        basis.append(vec)
    return basis


def census(D, y0, y1, rho, r, q, Wset, negpair):
    n = len(D)
    y0s = [tuple(y0[i:i + r + 1]) for i in range(rho)]
    y1s = [tuple(y1[i:i + r + 1]) for i in range(rho)]
    slopes = {}
    close = [0]

    def rec(start, depth, poly, chosen):
        if depth == r:
            uv = [sum(a * b for a, b in zip(y0s[i], poly)) % q for i in range(rho)]
            wv = [sum(a * b for a, b in zip(y1s[i], poly)) % q for i in range(rho)]
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
            fib = S <= Wset
            ev = (negpair is not None) and all(negpair[i] in S for i in S)
            rc = slopes.get(g)
            if rc is None:
                slopes[g] = [fib, ev, len(S - Wset)]
            else:
                rc[0] = rc[0] or fib
                rc[1] = rc[1] or ev
                rc[2] = min(rc[2], len(S - Wset))
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
    return slopes, close[0]


def attempt(tag, D, negpair, k, rho, q, dom, jlist, docensus, tries=6, seed=1):
    n = len(D)
    R = n - k
    r = R - rho
    a = n - r
    faithful = (4 * rho < R) and (a > R + 1) and (a - 1 > r)
    emit("")
    emit("=" * 78)
    emit("CONSTRUCT %s  n=%d k=%d R=%d rho=%d r=%d a=%d q=%d domain=%s"
         % (tag, n, k, R, rho, r, a, q, dom))
    emit("FAITHFUL 4rho<R=%s a>R+1=%s a-1>r=%s -> %s"
         % (4 * rho < R, a > R + 1, a - 1 > r, "FAITHFUL" if faithful else "NOT FAITHFUL"))
    if not faithful:
        emit("SKIPPED (faithfulness gate)")
        return
    emit("parameter-counting cap  j <= (2(r+1)-1)/rho = %.3f  (razor form 2r/rho)"
         % ((2 * (r + 1) - 1) / rho))
    v = vvals(D, q)
    Widx = list(range(r + 1))
    Wset = set(Widx)
    offidx = [i for i in range(n) if i not in Wset]
    rng = random.Random(seed)
    best = 0
    for j in jlist:
        okrow = None
        for tr in range(tries):
            Ps, As, gams = [], [], []
            used = set()
            bad = False
            for i in range(j):
                for _ in range(50):
                    P = tuple(sorted(rng.sample(offidx, rho)))
                    if P not in used:
                        used.add(P)
                        break
                else:
                    bad = True
                    break
                Ps.append(P)
                As.append(tuple(sorted(rng.sample(Widx, rho + 1))))
                gams.append(rng.randrange(2, q))
            if bad or len(set(gams)) != j:
                continue
            # unknowns: e0(w) w in W  (0..r), e1(w) (r+1..2r+1), lambda_i (2r+2 ..)
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
            for _ in range(40):
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
                # chi injective on W ?
                chi = []
                degen = False
                for t in range(r + 1):
                    if e1[t] == 0:
                        chi.append(("inf", e0[t] != 0))
                    else:
                        chi.append((e0[t] * inv(e1[t], q) % q, True))
                if len(set(c[0] for c in chi)) != r + 1:
                    continue
                fibslopes = set()
                for t in range(r + 1):
                    if e1[t]:
                        fibslopes.add((-e0[t] * inv(e1[t], q)) % q)
                if any(g in fibslopes for g in gams):
                    continue
                okrow = (e0, e1, lam, Ps, As, gams)
                break
            if okrow:
                break
        if not okrow:
            emit("  j=%2d : NO valid pencil found in %d tries" % (j, tries))
            continue
        e0, e1, lam, Ps, As, gams = okrow
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
        # direct verification of each engineered slope
        nver = 0
        for i in range(j):
            S = sorted(set(Ps[i]) | (Wset - set(As[i])))
            if len(S) != r:
                continue
            sig = [1]
            for t in S:
                ns = [0] * (len(sig) + 1)
                for jj, cj in enumerate(sig):
                    ns[jj + 1] = (ns[jj + 1] + cj) % q
                    ns[jj] = (ns[jj] - D[t] * cj) % q
                sig = ns
            good = all(sum((y0[ii + jj] + gams[i] * y1[ii + jj]) * sig[jj]
                           for jj in range(r + 1)) % q == 0 for ii in range(rho))
            if good:
                nver += 1
        line = ("  j=%2d : engineered slopes VERIFIED by pencil test = %d/%d"
                % (j, nver, j))
        if docensus:
            slopes, close = census(D, y0, y1, rho, r, q, Wset, negpair)
            T = len(slopes)
            Tf = sum(1 for s in slopes.values() if s[0])
            Ts = sum(1 for s in slopes.values() if (not s[0]) and s[1])
            Tr = sum(1 for s in slopes.values() if (not s[0]) and not s[1])
            line += ("  | CENSUS T=%d T_fib=%d T_sym=%d T_rand=%d  r+1=%d  "
                     "excess=%+d  column-%s  null q*mu1=%.4g"
                     % (T, Tf, Ts, Tr, r + 1, T - (r + 1),
                        "FAR" if close == 0 else "CLOSE(%d)" % close,
                        comb(n, r) * q ** (1 - rho)))
        emit(line)
        if nver == j:
            best = max(best, j)
    emit("  --> LARGEST j with all engineered slopes verified: %d  "
         "(parameter cap %.2f)" % (best, (2 * (r + 1) - 1) / rho))


def main():
    emit("")
    emit("################ RUN g3_construct.py ################")
    # ---- negation-closed integer domains ----
    for (m, k, rho, jl, dc) in [(10, 10, 2, [1, 2, 4, 6, 8, 9, 10], True),
                                (12, 12, 2, [1, 4, 8, 10, 11, 12], False),
                                (13, 13, 3, [1, 2, 4, 6, 7, 8], False),
                                (17, 17, 4, [1, 2, 3, 6, 7, 8], False)]:
        n = 2 * m
        q = 999983
        D = []
        for i in range(1, m + 1):
            D.append(i % q)
            D.append((-i) % q)
        # reorder so that the first r+1 entries are the positive 1..r+1
        R = n - k
        r = R - rho
        pos = [i % q for i in range(1, m + 1)]
        neg = [(-i) % q for i in range(1, m + 1)]
        Dl = pos[:r + 1] + pos[r + 1:] + neg
        idx = {Dl[i]: i for i in range(n)}
        negpair = {}
        for i in range(n):
            val = Dl[i]
            partner = (-val) % q
            negpair[i] = idx.get(partner)
        if any(vv is None for vv in negpair.values()):
            negpair = None
        attempt("intZ n=%d rho=%d" % (n, rho), Dl, negpair, k, rho, q,
                "negclosed integers {+-1..+-%d}" % m, jl, dc)
    # ---- razor-faithful multiplicative subgroup mu_n ----
    for (n, k, rho, jl, dc) in [(20, 10, 2, [1, 2, 4, 6, 8, 9], True),
                                (26, 13, 3, [1, 2, 4, 6, 7], False),
                                (34, 17, 4, [1, 2, 3, 6, 7], False)]:
        q = find_prime_1modn(n, 500000)
        S, g = subgroup(n, q)
        if S is None:
            emit("no subgroup for n=%d q=%d" % (n, q))
            continue
        # order the subgroup as g^0, g^1, ... so that -1 = g^{n/2}
        Dl = []
        x = 1
        for _ in range(n):
            Dl.append(x)
            x = x * g % q
        idx = {Dl[i]: i for i in range(n)}
        negpair = {i: idx[(-Dl[i]) % q] for i in range(n)}
        attempt("mu_%d" % n, Dl, negpair, k, rho, q,
                "MULTIPLICATIVE SUBGROUP mu_%d < F_%d^*" % (n, q), jl, dc)
    emit("################ END RUN g3_construct.py ################")


main()
FH.close()
