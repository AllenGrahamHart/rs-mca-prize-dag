#!/usr/bin/env python3
"""d6_kernel_structure.py -- rh_farca_upper (round 32).

The (MI1)/(MI2) budget of rate_half_ca_hankel_minimal_index_budget rests
on ONE structural step (proof.md:56-72, 147): the generic kernel of the
pencil is the SHIFT FAMILY of a single apolar form Q_Z of degree rho, so
that any domain-split locator in the kernel of a generic-rank slope is
DIVISIBLE by Q_gamma.

This script tests that step directly in the wide regime r > R/2 by
computing, at every slope gamma, a basis of ker M_r(y_0 + gamma y_1) as
polynomials of degree <= r and taking the gcd of the basis.  Shift-family
<=> gcd has degree rho.  It also lists the actual split locators.

Stdlib only.  Run under: tools/ramguard tiny -- python3 <this>
"""
import itertools
import time

T0 = time.time()
OUT = "notes/pilots_20260810/rh_farca_upper/d6_kernel_results.txt"
LINES = []


def emit(s):
    LINES.append(s)
    with open(OUT, "w") as fh:
        fh.write("\n".join(LINES) + "\n")


def inv(x, q):
    return pow(x, q - 2, q)


def build(n, k, q):
    R = n - k
    D = list(range(n))
    v = []
    for x in D:
        p = 1
        for y in D:
            if y != x:
                p = p * (x - y) % q
        v.append(inv(p, q))
    H = [[v[x] * pow(x, m, q) % q for x in range(n)] for m in range(R)]
    return R, D, H


def rref(M, q):
    M = [row[:] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    piv = []
    rk = 0
    for c in range(cols):
        p = None
        for i in range(rk, rows):
            if M[i][c]:
                p = i
                break
        if p is None:
            continue
        M[rk], M[p] = M[p], M[rk]
        iv = inv(M[rk][c], q)
        M[rk] = [x * iv % q for x in M[rk]]
        for i in range(rows):
            if i != rk and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[rk][j]) % q for j in range(cols)]
        piv.append(c)
        rk += 1
    return M[:rk], piv


def nullspace(M, q):
    Rm, piv = rref(M, q)
    cols = len(M[0])
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        v = [0] * cols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-Rm[i][f]) % q
        basis.append(v)
    return basis


def trim(p):
    while p and p[-1] == 0:
        p.pop()
    return p


def polydiv(a, b, q):
    a = a[:]
    db = len(b) - 1
    ivb = inv(b[db], q)
    while len(a) - 1 >= db and any(a):
        da = len(a) - 1
        c = a[da] * ivb % q
        for i in range(db + 1):
            a[da - db + i] = (a[da - db + i] - c * b[i]) % q
        trim(a)
    return a


def polygcd(a, b, q):
    a = trim(a[:])
    b = trim(b[:])
    while b:
        a, b = b, polydiv(a, b, q)
    if a:
        iv = inv(a[-1], q)
        a = [x * iv % q for x in a]
    return a


def hankel(w, R, r):
    return [[w[i + j] for j in range(r + 1)] for i in range(R - r)]


def split_locators(ker, n, r, D, q):
    """which squarefree degree-r D-split locators lie in span(ker)?"""
    if not ker:
        return []
    K, piv = rref([v[:] for v in ker], q)
    out = []
    for X in itertools.combinations(range(n), r):
        # coefficients of prod (x - D[j]) for j in X
        c = [1]
        for j in X:
            c = [0] + c
            for i in range(len(c) - 1):
                c[i] = (c[i] - D[j] * c[i + 1]) % q
        v = c[:] + [0] * (r + 1 - len(c))
        w = v[:]
        for i, p in enumerate(piv):
            if w[p]:
                f = w[p]
                w = [(w[t] - f * K[i][t]) % q for t in range(r + 1)]
        if not any(w):
            out.append(X)
    return out


def examine(tag, n, k, r, q, s0, s1):
    R, D, H = build(n, k, q)
    emit("")
    emit("=" * 72)
    emit(f"{tag}  n={n} k={k} a={n-r} r={r} R={R} q={q}  "
         f"pencil {R-r} x {r+1} (wide: {R-r < r+1})")
    rows = []
    rhos = []
    for g in range(q):
        w = [(s0[m] + g * s1[m]) % q for m in range(R)]
        M = hankel(w, R, r)
        ker = nullspace(M, q)
        rk = (r + 1) - len(ker)
        rhos.append(rk)
        g0 = []
        for v in ker:
            g0 = polygcd(g0, v[:], q) if g0 else trim(v[:])
        locs = split_locators(ker, n, r, D, q)
        rows.append((g, rk, len(ker), len(g0) - 1 if g0 else -1, locs))
    rho = max(rhos)
    emit(f"  generic rank rho = {rho}; kernel dim at generic rank = "
         f"{r+1-rho}; theory expects gcd degree = rho if the kernel is the "
         f"shift family of ONE apolar form")
    nbad = 0
    for (g, rk, kd, gd, locs) in rows:
        flag = "BAD" if locs else "   "
        if locs:
            nbad += 1
        emit(f"   gamma={g:3d} rank={rk} kerdim={kd} gcd_deg={gd} {flag} "
             f"split locators={locs if len(locs) <= 4 else str(locs[:4])+'...'}")
    emit(f"  #finite CA-bad slopes T = {nbad}")
    gds = set(row[3] for row in rows if row[1] == rho)
    emit(f"  gcd degrees at generic-rank slopes = {sorted(gds)}  "
         f"(single-apolar-generator step requires all = rho = {rho})")
    e_guess = 1
    A = R + 1 - 2 * rho
    d_ = rho
    mi2 = rho - A * e_guess + (n * e_guess) // d_ if d_ else None
    emit(f"  (MI2) instantiated at s=0, e=1: rho - A e + floor(N e/d) = "
         f"{rho} - {A} + floor({n}/{d_}) = {mi2}   vs measured T = {nbad}")
    return nbad, rho, sorted(gds)


def main():
    emit("d6_kernel_structure.py -- rh_farca_upper round 32")
    examine("census maximiser (q=11)", 7, 2, 3, 11, [5, 8, 7, 5, 4],
            [4, 10, 7, 4, 3])
    examine("census maximiser (q=7)", 7, 2, 3, 7, [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0])
    examine("census maximiser (8,3,a=5,q=11)", 8, 3, 3, 11, [3, 2, 5, 10, 3],
            [2, 2, 10, 8, 4])
    # LB1 at (7,2,a=4,r=3,q=11) with a fixed lam-assignment
    n, k, r, q = 7, 2, 3, 11
    R, D, H = build(n, k, q)
    Tset = [2, 3, 4, 5, 6]
    Tset = list(range(n - r - 1 + 1 - 1, n))[-(r + 1):]
    lams = [6, 1, 10, 9]
    d1 = [0] * n
    d2 = [0] * n
    for j, x in enumerate(Tset):
        d2[x] = 1
        d1[x] = (-lams[j]) % q
    s0 = [sum(d1[x] * H[m][x] for x in range(n)) % q for m in range(R)]
    s1 = [sum(d2[x] * H[m][x] for x in range(n)) % q for m in range(R)]
    examine(f"LB1 extremiser (T={Tset}, lams={lams})", n, k, r, q, s0, s1)
    emit("")
    emit(f"elapsed {time.time()-T0:.1f}s")


main()
print("\n".join(LINES))
