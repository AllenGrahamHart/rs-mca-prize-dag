#!/usr/bin/env python3
"""d5_minindex.py -- rh_farca_upper (round 32).

Measures the RIGHT MINIMAL INDICES of the syndrome Hankel pencil
M(Z) = M_r(y_0) + Z M_r(y_1) in the WIDE regime r > R/2, i.e. inside the
open bracket [k+2^34, 3n/4).

Why: rate_half_ca_hankel_minimal_index_budget/proof.md:61-72 asserts that
the rational kernel is spanned by the shifts of ONE apolar form, hence
"all nu_R right and nu_L left minimal indices equal e"; that step is what
carries (3) delta = rho - A e, hence (MI1) and (MI2).  If the measured
minimal indices are NOT all equal, the step -- and with it the entire
(MI1)/(MI2) budget -- has no content in the wide regime.

N(d) = dim {v(Z) of degree <= d : M(Z) v(Z) = 0} = sum_i max(0, d-eps_i+1),
so #{i : eps_i <= d} = N(d) - N(d-1), which recovers the multiset.
N(0) = dim (ker M_0 cap ker M_1) = dim K_0, and (HK1) of
rate_half_ca_hankel_fixed_kernel_branch holds iff every eps_i = 0.

Stdlib only.  Run under: tools/ramguard local -- python3 <this>
"""
import itertools
import random
import time

T0 = time.time()
OUT = "notes/pilots_20260810/rh_farca_upper/d5_minindex_results.txt"
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


def rank(M, q):
    if not M or not M[0]:
        return 0
    M = [row[:] for row in M]
    rows, cols = len(M), len(M[0])
    rk = 0
    for c in range(cols):
        piv = None
        for i in range(rk, rows):
            if M[i][c]:
                piv = i
                break
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        iv = inv(M[rk][c], q)
        M[rk] = [x * iv % q for x in M[rk]]
        for i in range(rows):
            if i != rk and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[rk][j]) % q for j in range(cols)]
        rk += 1
        if rk == rows:
            break
    return rk


def hankel(w, R, r):
    return [[w[i + j] for j in range(r + 1)] for i in range(R - r)]


def nullity_deg(M0, M1, d, q):
    """dim {v(Z) = sum_{t<=d} v_t Z^t : (M0 + Z M1) v(Z) = 0}."""
    m = len(M0)
    nc = len(M0[0])
    nv = nc * (d + 1)          # unknowns v_t[j]
    rows = []
    for t in range(d + 2):     # coefficient of Z^t
        for i in range(m):
            row = [0] * nv
            if t <= d:
                for j in range(nc):
                    row[t * nc + j] = M0[i][j]
            if t >= 1:
                for j in range(nc):
                    row[(t - 1) * nc + j] = (row[(t - 1) * nc + j]
                                             + M1[i][j]) % q
            rows.append(row)
    return nv - rank(rows, q)


def min_indices(M0, M1, q, dmax=6):
    N = [nullity_deg(M0, M1, d, q) for d in range(dmax + 1)]
    cum = [N[0]] + [N[d] - N[d - 1] for d in range(1, dmax + 1)]
    eps = []
    prev = 0
    for d in range(dmax + 1):
        for _ in range(cum[d] - prev):
            eps.append(d)
        prev = cum[d]
    return eps, N


def report(tag, n, k, r, q, s0, s1, H=None):
    R = n - k
    M0 = hankel(s0, R, r)
    M1 = hankel(s1, R, r)
    rho = 0
    for g in list(range(q)) + [None]:
        w = s1[:] if g is None else [(s0[m] + g * s1[m]) % q for m in range(R)]
        if any(w):
            rho = max(rho, rank(hankel(w, R, r), q))
        if rho == min(R - r, r + 1):
            break
    eps, N = min_indices(M0, M1, q)
    nuR = (r + 1) - rho
    nuL = (R - r) - rho
    allsame = len(set(eps)) <= 1
    emit(f"  {tag}: rho={rho} nu_R={nuR} nu_L={nuL} A=R+1-2rho={R+1-2*rho}")
    emit(f"    N(d) = {N}")
    emit(f"    right minimal indices = {eps}   (count {len(eps)}, "
         f"expected nu_R = {nuR})")
    emit(f"    dim K_0 = {N[0]}   (HK1 holds iff = nu_R : {N[0] == nuR})")
    emit(f"    ALL RIGHT MINIMAL INDICES EQUAL ? {allsame}   "
         f"sum(eps) = {sum(eps)} (Kronecker: sum(eps)+sum(eta)+delta = rho "
         f"= {rho})")
    return eps, rho, N[0], nuR


def main():
    random.seed(20260810)
    emit("d5_minindex.py -- rh_farca_upper round 32")
    emit("wide-regime minimal-index structure (r > R/2)")

    emit("")
    emit("== census maximisers (from d3_wide / d4_deficient) ==")
    report("(7,2,a=4,r=3,q=7) exhaustive max T=7", 7, 2, 3, 7,
           [1, 0, 0, 0, 1], [0, 1, 0, 1, 0])
    report("(7,2,a=4,r=3,q=11) sampled max T=8", 7, 2, 3, 11,
           [5, 8, 7, 5, 4], [4, 10, 7, 4, 3])
    report("(8,3,a=5,r=3,q=11) sampled max T=10", 8, 3, 3, 11,
           [3, 2, 5, 10, 3], [2, 2, 10, 8, 4])
    report("(9,2,a=5,r=4,q=11) sampled max T=6", 9, 2, 4, 11,
           [6, 3, 1, 2, 2, 0, 9], [3, 3, 3, 2, 1, 6, 7])

    emit("")
    emit("== LB1 (round-31 extremiser) pencils ==")
    for (n, k, r, q) in ((7, 2, 3, 11), (8, 3, 3, 11), (9, 2, 4, 11),
                         (6, 3, 2, 17)):
        R, D, H = build(n, k, q)
        a = n - r
        Tset = list(range(a - 1, n))
        lams = random.sample(range(1, q), r + 1)
        d1 = [0] * n
        d2 = [0] * n
        for j, x in enumerate(Tset):
            d2[x] = 1
            d1[x] = (-lams[j]) % q
        s0 = [sum(d1[x] * H[m][x] for x in range(n)) % q for m in range(R)]
        s1 = [sum(d2[x] * H[m][x] for x in range(n)) % q for m in range(R)]
        report(f"LB1 n={n} k={k} a={a} r={r} q={q} lams={lams}", n, k, r, q,
               s0, s1)

    emit("")
    emit("== deficient (irreducible-P) planes: P = x^2+1 over F_11 ==")
    for (n, k, r) in ((9, 2, 4), (8, 1, 4)):
        R = n - k
        P = [1, 0, 1]
        B = []
        for b in range(2):
            y = [0] * R
            y[b] = 1
            for i in range(R - 2):
                y[i + 2] = (-(P[0] * y[i] + P[1] * y[i + 1])) % 11
            B.append(y)
        report(f"P-annihilated plane n={n} k={k} a={n-r} r={r} q=11",
               n, k, r, 11, B[0], B[1])

    emit("")
    emit("== how often is the (MI1) premise 'all minimal indices equal' "
         "true?  random column-far planes ==")
    for (n, k, r, q, ns) in ((7, 2, 3, 7, 500), (7, 2, 3, 11, 500),
                             (8, 3, 3, 11, 400), (9, 2, 4, 11, 300)):
        R, D, H = build(n, k, q)
        same = 0
        tot = 0
        hk1 = 0
        pat = {}
        while tot < ns:
            s0 = [random.randrange(q) for _ in range(R)]
            s1 = [random.randrange(q) for _ in range(R)]
            if rank([s0, s1], q) < 2:
                continue
            tot += 1
            M0 = hankel(s0, R, r)
            M1 = hankel(s1, R, r)
            rho = 0
            for g in list(range(q)) + [None]:
                w = (s1[:] if g is None
                     else [(s0[m] + g * s1[m]) % q for m in range(R)])
                if any(w):
                    rho = max(rho, rank(hankel(w, R, r), q))
                if rho == min(R - r, r + 1):
                    break
            eps, N = min_indices(M0, M1, q, dmax=4)
            key = tuple(eps)
            pat[key] = pat.get(key, 0) + 1
            if len(set(eps)) <= 1:
                same += 1
            if N[0] == (r + 1) - rho:
                hk1 += 1
        emit(f"  n={n} k={k} a={n-r} r={r} q={q}: {tot} random planes; "
             f"all-indices-equal in {same} ({same/tot:.3f}); "
             f"(HK1) fixed kernel in {hk1} ({hk1/tot:.3f})")
        emit(f"    index patterns = {dict(sorted(pat.items()))}")
    emit("")
    emit(f"elapsed {time.time()-T0:.1f}s")


main()
print("\n".join(LINES))
