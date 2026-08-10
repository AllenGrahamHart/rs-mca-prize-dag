"""D1: the cyclotomic candidate for the half-distance A=1 residual.

The design cap is attained field-independently by
    Q(U,V;X) = X^rho U^e - (c_0 U + c_1 V)^e ,     rho = e * r_0,
whose fibre over gamma is X^rho = c(gamma)^e, split over D = mu_N as
soon as rho | N and c(gamma)^e lies in mu_(N/rho); that happens for
about N/r_0 slopes, which is far above the residual target rho+1.

At the OFFICIAL half-distance budget B = 2^39+1 the A=1 profile has
rho = 2^39 which DOES divide N = 2^41, and the admissible parameter
window m+1 <= e <= rho contains e = 2^39 (r_0=1) and e = 2^38 (r_0=2).
So this family is a genuine structural threat there — unless the
Hankel/apolar origin kills it.

This script tests exactly that at the accessible analogues:
  N=16, R=8,  r=rho=4, A=1, e=2, r_0=2  (target T <= 5, design T = 8)
  N=16, R=8,  r=rho=4, A=1, e=4, r_0=1  (target T <= 5)
  N=12, R=6,  r=rho=3, A=1, e=1, r_0=3  (the realizable case already seen)
  N=24, R=12, r=rho=6, A=1, e=2, r_0=3  (target T <= 7)
  N=20, R=10, r=rho=5, A=1, e=1, r_0=5

Realizability = nonzero solution of M_r(y_0+Z y_1) . Q(Z) = 0.

Stdlib only.  Run under tools/ramguard.
"""
import itertools


def say(s=""):
    print(str(s), flush=True)


def subgroup(q, N):
    for cand in range(2, q):
        x, order = 1, 0
        while True:
            x = x * cand % q
            order += 1
            if x == 1:
                break
        if order == q - 1:
            g = cand
            break
    h = pow(g, (q - 1) // N, q)
    D, x = [], 1
    for _ in range(N):
        D.append(x)
        x = x * h % q
    return sorted(D)


def rref(M, q):
    M = [row[:] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    piv, r = [], 0
    for c in range(cols):
        p = None
        for i in range(r, rows):
            if M[i][c] % q:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        iv = pow(M[r][c], q - 2, q)
        M[r] = [v * iv % q for v in M[r]]
        for i in range(rows):
            if i != r and M[i][c] % q:
                f = M[i][c]
                M[i] = [(M[i][t] - f * M[r][t]) % q for t in range(cols)]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return M, piv


def kernel(M, q, cols):
    if not M:
        return [[1 if t == j else 0 for t in range(cols)] for j in range(cols)]
    Mr, piv = rref(M, q)
    free = [c for c in range(cols) if c not in piv]
    out = []
    for f in free:
        v = [0] * cols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-Mr[i][f]) % q
        out.append(v)
    return out


def realizability(Qcoeffs, Rv, rv, q):
    """Qcoeffs[t] = vector in F^(rv+1), the Z^t coefficient of Q(Z).

    Solve M_rv(y_0 + Z y_1) . Q(Z) = 0 for (y_0,y_1) in F^(2Rv)."""
    e = len(Qcoeffs) - 1
    m = Rv - rv
    rows = []
    for deg in range(e + 2):            # Z^0 .. Z^(e+1)
        for i in range(m):
            row = [0] * (2 * Rv)
            for j in range(rv + 1):
                if 0 <= deg < len(Qcoeffs):
                    row[i + j] = (row[i + j] + Qcoeffs[deg][j]) % q
                if 0 <= deg - 1 < len(Qcoeffs):
                    row[Rv + i + j] = (row[Rv + i + j] + Qcoeffs[deg - 1][j]) % q
            rows.append(row)
    return kernel(rows, q, 2 * Rv)


def split_count(Qcoeffs, D, q, rho):
    """number of finite slopes whose Q_gamma is a squarefree split
    degree-rho locator over D (the DESIGN count of this family)."""
    T = 0
    for g in range(q):
        vec = [0] * (rho + 1)
        for t, qc in enumerate(Qcoeffs):
            gt = pow(g, t, q)
            for j in range(rho + 1):
                vec[j] = (vec[j] + gt * qc[j]) % q
        if vec[rho] % q == 0:
            continue
        iv = pow(vec[rho], q - 2, q)
        c = [v * iv % q for v in vec]
        roots = [x for x in D
                 if sum(c[i] * pow(x, i, q) for i in range(rho + 1)) % q == 0]
        if len(roots) == rho:
            T += 1
    return T


def cyclo_family(rho, e, c0, c1, q):
    """Q = X^rho U^e - (c0 U + c1 V)^e  ->  ascending-coefficient
    vectors of the Z^t components (V=1, U=Z convention: Q_gamma(X) =
    X^rho - (c0 + c1 gamma)^e ... we use c(gamma)=c0+c1*gamma)."""
    # (c0 + c1 Z)^e expanded
    coef = [0] * (e + 1)
    for t in range(e + 1):
        # binomial(e,t) c0^(e-t) c1^t
        b = 1
        for i in range(t):
            b = b * (e - i) // (i + 1)
        coef[t] = b % q * pow(c0, e - t, q) % q * pow(c1, t, q) % q
    out = []
    for t in range(e + 1):
        v = [0] * (rho + 1)
        v[0] = (-coef[t]) % q
        if t == 0:
            v[rho] = 1
        out.append(v)
    return out


CASES = [
    ("N=16 rho=4 e=2 r0=2", 17, 16, 8, 4, 2),
    ("N=16 rho=4 e=4 r0=1", 17, 16, 8, 4, 4),
    ("N=12 rho=3 e=1 r0=3", 13, 12, 6, 3, 1),
    ("N=20 rho=5 e=1 r0=5", 41, 20, 10, 5, 1),
    ("N=24 rho=6 e=2 r0=3", 73, 24, 12, 6, 2),
    ("N=16 rho=4 e=2 r0=2", 97, 16, 8, 4, 2),
    ("N=16 rho=4 e=2 r0=2", 113, 16, 8, 4, 2),
]

say("=== cyclotomic candidate for the A=1 half-distance profile ===")
say("case                  q     A   target  best design T  realizable?")
for (name, q, N, Rv, rho, e) in CASES:
    if (q - 1) % N:
        say("%s q=%d SKIPPED (N does not divide q-1)" % (name, q))
        continue
    D = subgroup(q, N)
    A = Rv + 1 - 2 * rho
    bestT, bestreal, bestpair = 0, None, None
    for c0 in range(0, q):
        for c1 in range(1, q):
            Q = cyclo_family(rho, e, c0, c1, q)
            T = split_count(Q, D, q, rho)
            if T > bestT:
                sols = realizability(Q, Rv, rho, q)
                nz = [s for s in sols if any(v % q for v in s)]
                bestT, bestreal, bestpair = T, len(nz), (c0, c1)
    say("%-21s %-5d %-3d %-7d %-14d nullity=%s at (c0,c1)=%s"
        % (name, q, A, rho + 1, bestT, bestreal, bestpair))
    if bestT > rho + 1 and bestreal:
        say("   *** REALIZABLE OVER-TARGET FAMILY — check column-farness ***")
say("=== END ===")
