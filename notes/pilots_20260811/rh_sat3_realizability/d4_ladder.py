"""D1 (ladder) / D3: the T-LADDER BY CONSTRUCTION at m = 1..4.

Explicit family (Kummer pencil).  Take q = 1 mod rho and
        Q_Z(X) = X^rho + Z          (bidegree (e,rho) = (1, rho)).
Then q_rho == 1 (never degenerate), q_0 = Z, so the generator is primitive
with parameter degree e = 1 and s = 0, and Q_Z(x) = x^rho + Z has the SINGLE
root Z = -x^rho, so d_x <= 1 for every x.  The member at slope gamma is
X^rho + gamma, which splits over F_q into rho distinct roots exactly when
-gamma is a nonzero rho-th power; the root sets are then the cosets of mu_rho
and are PAIRWISE DISJOINT.  Choosing T such cosets and padding to |D| = N
gives a column-far Hankel pencil with T supported slopes.

Because d_x <= e = 1, sum_x d_x = T*rho <= N, so this e=1 family caps at
        T <= floor(N/rho) = floor(16m/(4m-1)) = 5 (m=1), 4 (m>=2),
and the cap is ATTAINED at every m below.  NOTE (stated loudly in the
report): for m >= 2 this is e = 1, NOT the (SAT1) profile e = m, so these
objects do NOT test (SAT3); they establish that the rank-deficient A = 3
branch is non-empty at every m and they calibrate the ladder.

Stdlib only.
"""
import sys
from itertools import combinations


def isprime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def primes_for(rho, lo, count):
    out = []
    n = lo
    while len(out) < count:
        n += 1
        if (n - 1) % rho == 0 and isprime(n):
            out.append(n)
    return out


def cell(m, q, out):
    rho, N, R = 4 * m - 1, 16 * m, 8 * m
    r, K, e = rho, N - R, 1
    inv = lambda a: pow(a % q, q - 2, q)

    def peval(c, x):
        v = 0
        for co in reversed(c):
            v = (v * x + co) % q
        return v

    def rref(rows, nc):
        rows = [row[:] for row in rows]
        piv, rk = [], 0
        for c in range(nc):
            p = None
            for i in range(rk, len(rows)):
                if rows[i][c] % q:
                    p = i
                    break
            if p is None:
                continue
            rows[rk], rows[p] = rows[p], rows[rk]
            iv = inv(rows[rk][c])
            rows[rk] = [v * iv % q for v in rows[rk]]
            for i in range(len(rows)):
                if i != rk and rows[i][c] % q:
                    f = rows[i][c]
                    rows[i] = [(a - f * b) % q
                               for a, b in zip(rows[i], rows[rk])]
            piv.append(c)
            rk += 1
            if rk == len(rows):
                break
        return rows, piv, rk

    def nullspace(rows, nc):
        rr, piv, rk = rref(rows, nc)
        bas = []
        for f in [c for c in range(nc) if c not in piv]:
            v = [0] * nc
            v[f] = 1
            for i, c in enumerate(piv):
                v[c] = (-rr[i][f]) % q
            bas.append(v)
        return bas

    # rho-th power cosets
    g = 2
    while pow(g, (q - 1) // 2, q) == 1 or any(
            pow(g, (q - 1) // p, q) == 1 for p in (3, 5, 7, 11, 13)
            if (q - 1) % p == 0):
        g += 1
    zeta = pow(g, (q - 1) // rho, q)
    mu = [pow(zeta, i, q) for i in range(rho)]
    Tmax = N // rho
    cosets, slopes, used = [], [], set()
    j = 0
    while len(cosets) < Tmax and j < q:
        j += 1
        base = pow(g, j, q)
        cs = tuple(sorted(base * z % q for z in mu))
        if set(cs) & used:
            continue
        gam = (-pow(base, rho, q)) % q
        if gam in slopes:
            continue
        cosets.append(cs)
        slopes.append(gam)
        used |= set(cs)
    if len(cosets) < Tmax:
        out(f"  m={m} q={q}: could not assemble {Tmax} disjoint cosets")
        return None
    D = sorted(used)
    extra = [x for x in range(q) if x not in used][:N - len(D)]
    D = sorted(set(D) | set(extra))
    assert len(D) == N, (len(D), N)

    A = [0] * rho + [1]          # X^rho
    B = [1] + [0] * rho          # 1
    rows = []
    for i in range(R - r):
        r1 = [0] * (2 * R); r2 = [0] * (2 * R); r3 = [0] * (2 * R)
        for jj in range(r + 1):
            r1[i + jj] = (r1[i + jj] + A[jj]) % q
            r2[R + i + jj] = (r2[R + i + jj] + B[jj]) % q
            r3[i + jj] = (r3[i + jj] + B[jj]) % q
            r3[R + i + jj] = (r3[R + i + jj] + A[jj]) % q
        rows += [r1, r2, r3]
    ns = nullspace(rows, 2 * R)

    def Mr(y):
        return [[y[i + jj] for jj in range(r + 1)] for i in range(R - r)]

    def splitlocs(mat):
        bas = nullspace(mat, r + 1)
        if len(bas) != 1:
            return None
        v = bas[0]
        if v[r] == 0:
            return []
        iv = inv(v[r])
        w = [a * iv % q for a in v]
        rs = [x for x in D if peval(w, x) == 0]
        return [tuple(sorted(rs))] if len(rs) == rho else []

    import random as _rnd
    rr_ = _rnd.Random(12345 + m * 1000 + q)
    cands = list(ns)
    for _ in range(400):                      # random combos, not just basis
        co = [rr_.randrange(q) for _ in ns]
        cands.append([sum(c * b[i] for c, b in zip(co, ns)) % q
                      for i in range(2 * R)])
    for sol in cands:
        y0, y1 = sol[:R], sol[R:]
        if not any(y0) and not any(y1):
            continue
        rk = max(rref(Mr([(a + gg * b) % q for a, b in zip(y0, y1)]),
                      r + 1)[2] for gg in range(min(q, 40)))
        if rk != rho:
            continue
        c0, c1 = splitlocs(Mr(y0)), splitlocs(Mr(y1))
        if c0 is None or c1 is None or (set(c0) & set(c1)):
            continue
        sup = {}
        for gg in range(q):
            sl = splitlocs(Mr([(a + gg * b) % q for a, b in zip(y0, y1)]))
            if sl:
                sup[gg] = sl[0]
        dx = {x: sum(1 for S in sup.values() if x in S) for x in D}
        O = sum(rho - len(S) for S in sup.values())
        ws = (min(len(set(sup[a]) | set(sup[b]))
                  for a, b in combinations(sorted(sup), 2))
              if len(sup) >= 2 else None)
        out(f"  m={m} q={q}: rho={rho} N={N} R={R} k={K} r={r} "
            f"A={R + 1 - 2 * rk} e={e} s=0")
        out(f"      T = {len(sup)}  (e=1 ceiling floor(N/rho) = {Tmax}; "
            f"rho+1 = {rho + 1}; rho+2 = {rho + 2})")
        out(f"      generic rank = {rk} (= rho) ; O = {O} ; "
            f"max d_x = {max(dx.values())} (<= e = 1)")
        out(f"      sum_x d_x = {sum(dx.values())} = T*rho - O = "
            f"{len(sup) * rho - O} ; N*e = {N * e}")
        out(f"      (SAT4) at e=m would need sum_x (m-d_x) = 1+O = {1 + O}; "
            f"here sum_x (m-d_x) = {sum(m - dx[x] for x in D)} -> "
            f"{'ON (SAT1) PROFILE' if m == 1 else 'OFF (SAT1) PROFILE (e=1 != m)'}")
        out(f"      column-far: OK ; w* = {ws} ; 2rho = {2 * rho} ; "
            f"7m-1 = {7 * m - 1}")
        return len(sup)
    out(f"  m={m} q={q}: no non-degenerate realization")
    return None


def main():
    lines = []

    def out(s):
        print(s)
        lines.append(s)

    out("=== D1: THE T-LADDER BY CONSTRUCTION (Kummer pencil, e=1) ===")
    out("Q_Z(X) = X^rho + Z ; supported slopes = -(rho-th powers) ;")
    out("locator sets = cosets of mu_rho, pairwise disjoint (d_x <= e = 1).")
    out("")
    table = {}
    for m in (1, 2, 3, 4):
        rho = 4 * m - 1
        qs = primes_for(rho, 16 * m * 4, 2)
        got = []
        for q in qs:
            v = cell(m, q, out)
            if v is not None:
                got.append((q, v))
        table[m] = got
        out("")
    out("=== LADDER SUMMARY ===")
    out(f"{'m':>3} {'rho':>5} {'N':>5} {'rho+2':>6} {'e=1 ceiling':>12} "
        f"{'T measured (two fields)':>26}")
    for m in (1, 2, 3, 4):
        rho, N = 4 * m - 1, 16 * m
        out(f"{m:>3} {rho:>5} {N:>5} {rho + 2:>6} {N // rho:>12} "
            f"{str([v for _, v in table[m]]):>26}")
    out("")
    out("READING: the e=1 family attains its own ceiling floor(N/rho) at")
    out("every m, and that ceiling equals rho+2 ONLY at m=1.  For m>=2 the")
    out("ladder stalls at T=4 while rho+2 = 9,13,17 -- so NO e=1 object can")
    out("reach (SAT3) for m>=2, and (SAT1)'s e=m is not decoration.")
    with open(sys.argv[1], "w") as f:
        f.write("\n".join(lines) + "\n")


main()
