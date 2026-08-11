"""D1 controls: (i) the packed rank engine against a naive dense rank;
(ii) the ANALYTIC control on the realizability system.

Analytic control.  If A_x = B (one fixed m-set) for every x in W, then

  sum_x x^i (alpha_x Z + beta_x) prod_B(Z-g) = prod_B(Z-g) * ( Z*sum_x x^i alpha_x
                                                              + sum_x x^i beta_x )

so S2 is EXACTLY "alpha in K'|_W and beta in K'|_W", i.e.

  nullity(S2) = 2 * dim K'|_W = 2 * (a - (4m+1)) = 6m-4   at a = 7m-1.

Any deviation means the builder is wrong.  (This configuration is NOT
incidence-admissible -- it needs |S_g ^ W| = a = 7m-1 > rho -- it is a
code test, nothing else.)
"""

import random
import sys

sys.path.insert(0, "notes/pilots_20260811/rh_bivariate_system")
from biv_core import (PackedRank, build_S1, build_S2, mu_N, poly_from_roots,
                      primes_one_mod)


def naive_rank(rows, ncols, q):
    rows = [r[:] for r in rows]
    piv = 0
    for c in range(ncols):
        sel = None
        for r in range(piv, len(rows)):
            if rows[r][c] % q:
                sel = r
                break
        if sel is None:
            continue
        rows[piv], rows[sel] = rows[sel], rows[piv]
        inv = pow(rows[piv][c], q - 2, q)
        rows[piv] = [v * inv % q for v in rows[piv]]
        for r in range(len(rows)):
            if r != piv and rows[r][c] % q:
                f = rows[r][c]
                rows[r] = [(a - f * b) % q for a, b in zip(rows[r], rows[piv])]
        piv += 1
        if piv == len(rows):
            break
    return piv


out = []
P = out.append

P("=" * 72)
P("D1 CONTROLS -- rh_bivariate_system (round 33)")
P("=" * 72)

# ---------------------------------------------------------------- engine test
rnd = random.Random(11)
P("")
P("[C0] packed rank engine vs naive dense rank, random matrices")
ok = True
for trial in range(12):
    q = rnd.choice([97, 193, 257, 12289])
    nr = rnd.randint(3, 25)
    nc = rnd.randint(3, 20)
    rk_forced = rnd.randint(0, min(nr, nc))
    # build a matrix of exactly rank rk_forced
    U = [[rnd.randrange(q) for _ in range(rk_forced)] for _ in range(nr)]
    V = [[rnd.randrange(q) for _ in range(nc)] for _ in range(rk_forced)]
    M = [[sum(U[i][k] * V[k][j] for k in range(rk_forced)) % q for j in range(nc)]
         for i in range(nr)]
    pr = PackedRank(nc, q)
    for row in M:
        pr.add_row(row)
    nv = naive_rank(M, nc, q)
    if pr.rank != nv:
        ok = False
        P("    MISMATCH q=%d %dx%d packed=%d naive=%d" % (q, nr, nc, pr.rank, nv))
P("    12 random matrices, packed == naive : %s" % ("PASS" if ok else "FAIL"))

# kernel basis test
P("")
P("[C0b] kernel_basis: M * v == 0 for every basis vector, and count == nullity")
ok2 = True
for trial in range(8):
    q = rnd.choice([97, 193, 257])
    nr, nc = rnd.randint(3, 14), rnd.randint(3, 12)
    rk = rnd.randint(0, min(nr, nc))
    U = [[rnd.randrange(q) for _ in range(rk)] for _ in range(nr)]
    V = [[rnd.randrange(q) for _ in range(nc)] for _ in range(rk)]
    M = [[sum(U[i][k] * V[k][j] for k in range(rk)) % q for j in range(nc)]
         for i in range(nr)]
    pr = PackedRank(nc, q)
    for row in M:
        pr.add_row(row)
    kb = pr.kernel_basis()
    if len(kb) != nc - pr.rank:
        ok2 = False
    for v in kb:
        for row in M:
            if sum(a * b for a, b in zip(row, v)) % q:
                ok2 = False
P("    8 random matrices, kernel verified : %s" % ("PASS" if ok2 else "FAIL"))

# ---------------------------------------------- analytic control on the system
P("")
P("[C1] ANALYTIC CONTROL: A_x = B for all x  =>  nullity(S2) = 2(a-(4m+1)) = 6m-4")
P("     (a = 7m-1; this is a CODE test, the configuration is not admissible)")
P("")
P("      m   q     a   T   equations  unknowns  rank  nullity  predicted")
for m in (2, 3, 4):
    N = 16 * m
    for q in primes_one_mod(N, count=2, limit=4000)[:2]:
        D = mu_N(q, N)
        a = 7 * m - 1
        rnd2 = random.Random(1000 + m)
        Wvals = rnd2.sample(D, a)
        slopes = rnd2.sample(range(1, q), 4 * m + 1)
        B = slopes[:m]
        Amap = {x: B for x in Wvals}
        pr, cols, ncols, nrows, T, aa = build_S2(m, q, Wvals, Amap)
        nul = ncols - pr.rank
        pred = 2 * (a - (4 * m + 1))
        P("     %2d  %4d  %3d  %2d  %9d  %8d  %4d  %7d  %9d  %s"
          % (m, q, a, T, (m + 2) * (4 * m + 1), ncols, pr.rank, nul, pred,
             "PASS" if nul == pred else "FAIL"))

# ------------------------------------------ control 2: perturb one point of W
P("")
P("[C2] perturb: change A_x at ONE point of W to a different m-set")
P("      m   q    nullity(all equal)  nullity(one changed)")
for m in (2, 3, 4):
    N = 16 * m
    q = primes_one_mod(N, count=1, limit=4000)[0]
    D = mu_N(q, N)
    a = 7 * m - 1
    rnd2 = random.Random(2000 + m)
    Wvals = rnd2.sample(D, a)
    slopes = rnd2.sample(range(1, q), 4 * m + 1)
    B = slopes[:m]
    B2 = slopes[1:m + 1]
    Amap = {x: B for x in Wvals}
    pr0, _, nc0, _, _, _ = build_S2(m, q, Wvals, Amap)
    Amap2 = dict(Amap)
    Amap2[Wvals[0]] = B2
    pr1, _, nc1, _, _, _ = build_S2(m, q, Wvals, Amap2)
    P("     %2d  %4d  %18d  %20d" % (m, q, nc0 - pr0.rank, nc1 - pr1.rank))

# ----------------------------------------------- control 3: the S1 slice of S2
P("")
P("[C3] S1 (mu given) is the mu-slice of S2: nullity(S1) <= nullity(S2)")
P("     and S1 with a CONSTANT mu on the all-equal control should be 3m-2")
for m in (2, 3, 4):
    N = 16 * m
    q = primes_one_mod(N, count=1, limit=4000)[0]
    D = mu_N(q, N)
    a = 7 * m - 1
    rnd2 = random.Random(3000 + m)
    Wvals = rnd2.sample(D, a)
    slopes = rnd2.sample(range(1, q), 4 * m + 1)
    B = slopes[:m]
    Amap = {x: B for x in Wvals}
    mu0 = slopes[m]
    mumap = {x: mu0 for x in Wvals}
    pr, _, aa, _ = build_S1(m, q, Wvals, Amap, mumap)
    P("     m=%d q=%d  nullity(S1, constant mu) = %d   predicted %d  %s"
      % (m, q, aa - pr.rank, 3 * m - 2,
         "PASS" if aa - pr.rank == 3 * m - 2 else "FAIL"))

P("")
P("=" * 72)
print("\n".join(out))
with open("notes/pilots_20260811/rh_bivariate_system/d1_control_results.txt", "w") as f:
    f.write("\n".join(out) + "\n")
