#!/usr/bin/env python3
"""Agreement-budget bound on the common-zero set (2026-07-26).  Exact integers.

THEOREM.  Let C = RS[F,D,K] with n = 2K (rate 1/2), let c_0..c_3 be four distinct
codewords with agr(c_i,u) >= m for a common received word u, let C' = span{c_i-c_0}
with common-zero set G, z = |G|, and let b be the number of points of G at which the
common value differs from u.  Then

        4(m - g) <= (n - z) + 6(K - 1 - z),      g = z - b,

and at the razor agreement m = 3n/4 - 1 this collapses to

        3z + 4b <= n - 2.                                            (CZB)

Proof.
 1. c_i - c_j is a nonzero codeword, so wt >= n-K+1 and agr(c_i,c_j) <= K-1.
 2. Sum_{i<j} agr(c_i,c_j) = sum_x sum_k C(n_k(x),2) over value-class sizes n_k(x).
    On G all four values coincide, contributing C(4,2) = 6 per point.  Off G they
    do not all coincide, so P(x) := sum_k C(n_k(x),2) lies in {0,1,2,3}.  Hence
        6z + sum_{x off G} P(x) <= 6(K-1),  i.e.  sum_{off G} P(x) <= 6(K-1-z).
 3. With a_x = #{i : c_i(x) = u(x)}, off G one has a_x <= 1 + P(x):
        a_x=2 forces an agreeing pair, so P(x) >= 1;
        a_x=3 forces C(3,2)=3 agreeing pairs, so P(x) >= 3;
        a_x=4 is impossible off G.
 4. On G, a_x = 4 at the g agreeing points and 0 at the other b, so
        sum_i agr(c_i,u) = 4g + sum_{off G} a_x >= 4m.
 5. Combining, 4(m-g) <= (n-z) + 6(K-1-z).  Put K = n/2 and 4m = 3n-4.  []

CONSEQUENCES at the razor:
  (a) z <= (n-2)/3   -- the common-zero set is at most a third of the block, well
      below the trivial pairwise bound z <= K-1 = n/2 - 1;
  (b) d_s = n - z >= (2n+2)/3;  in particular the MINIMUM-SUPPORT case d_s = R+2
      (= n/2+2) is IMPOSSIBLE for n > 8 -- and that was exactly the case in which
      GF thm:rank-flat-list appeared to force b = 0;
  (c) b = 0 is forced whenever z > (n-6)/3.

This is a bound, not a closure: it does not by itself decide s = 2 vs s = 3.
"""

from __future__ import annotations

import sys
from itertools import combinations

errors: list[str] = []


def check(c: bool, m: str) -> None:
    if not c:
        errors.append(m)


def czb_rhs(n: int, K: int, m: int, z: int) -> int:
    """Upper bound for 4(m-g) from steps 2-3, as an inequality on 4b."""
    return n + 6 * K - 6 - 4 * m - 3 * z          # >= 4b


# ---- official row -------------------------------------------------------
n, K = 2**41, 2**40
m = 3 * n // 4 - 1
check(4 * m == 3 * n - 4, "razor agreement identity 4m = 3n-4")
# (CZB): 4b <= n - 2 - 3z
for z in (0, 1, 10**6, (n - 2) // 3):
    check(czb_rhs(n, K, m, z) == n - 2 - 3 * z, f"(CZB) reduction failed at z={z}")

z_max = (n - 2) // 3
check(czb_rhs(n, K, m, z_max) >= 0, "z_max must be admissible")
check(czb_rhs(n, K, m, z_max + 1) < 0, "z_max+1 must be inadmissible")
print(f"official: z <= {z_max}  (= (n-2)/3 = {z_max/n:.6f} n);  "
      f"trivial pairwise bound was z <= K-1 = {K-1} ({(K-1)/n:.6f} n)")
check(z_max < K - 1, "(CZB) must beat the trivial pairwise bound")

# (b) minimum support d_s = R+2 is killed
R = n - K
d_min = R + 2
z_at_dmin = n - d_min
check(czb_rhs(n, K, m, z_at_dmin) < 0,
      "minimum-support case d_s = R+2 should be excluded by (CZB)")
print(f"minimum support d_s = R+2 = {d_min}: z = {z_at_dmin}, "
      f"4b <= {czb_rhs(n,K,m,z_at_dmin)} < 0  => EXCLUDED")
d_s_min = -(-(2 * n + 2) // 3)                    # ceil((2n+2)/3)
check(czb_rhs(n, K, m, n - d_s_min) >= 0, "d_s floor must be admissible")
check(czb_rhs(n, K, m, n - d_s_min + 1) < 0, "d_s floor must be sharp")
print(f"forced: d_s >= {d_s_min} (= {d_s_min/n:.6f} n)")

# (c) b = 0 forced for large z
z_b0 = (n - 6) // 3 + 1
check(czb_rhs(n, K, m, z_b0) < 4, "b=0 threshold must force b=0")
print(f"b = 0 forced once z > (n-6)/3, i.e. z >= {z_b0}")

# ---- exhaustive check on the banked F_17 witnesses ----------------------
P17, n17, K17 = 17, 16, 8
m17 = 3 * n17 // 4 - 1
INV = [0] + [pow(a, P17 - 2, P17) for a in range(1, P17)]
DOM = list(range(1, 17))
Z17, N17 = DOM[:11], DOM[11:]


def pval(rts, x):
    v = 1
    for r in rts:
        v = v * (x - r) % P17
    return v


RS = list(combinations(Z17, 7))
V = {R_: tuple(pval(R_, y) for y in N17) for R_ in RS}
sols = []
for R1 in RS:
    v1 = V[R1]
    for R2 in RS:
        if R2 == R1:
            continue
        v2 = V[R2]
        c2 = v1[3] * INV[v2[3]] % P17
        if c2 * v2[4] % P17 != v1[4] or c2 * v2[2] % P17 != v1[2]:
            continue
        for R3 in RS:
            if R3 in (R1, R2):
                continue
            v3 = V[R3]
            c3 = v1[3] * INV[v3[3]] % P17
            if c3 * v3[4] % P17 != v1[4] or c3 * v3[1] % P17 != v1[1]:
                continue
            if c2 * v2[0] % P17 != c3 * v3[0] % P17:
                continue
            sols.append((R1, R2, R3, 1, c2, c3))
check(len(sols) == 12, f"expected 12 F_17 witnesses, got {len(sols)}")

tight = 0
for (R1, R2, R3, c1, c2, c3) in sols:
    u = [0] * n17
    u[N17[3] - 1] = c1 * V[R1][3] % P17
    u[N17[4] - 1] = c1 * V[R1][4] % P17
    u[N17[0] - 1] = c2 * V[R2][0] % P17
    u[N17[1] - 1] = c1 * V[R1][1] % P17
    u[N17[2] - 1] = c1 * V[R1][2] % P17
    W = [tuple([0] * n17)] + [tuple(c * pval(R_, x) % P17 for x in DOM)
                              for R_, c in ((R1, c1), (R2, c2), (R3, c3))]
    G = [x for x in range(n17) if len({W[i][x] for i in range(4)}) == 1]
    z = len(G)
    g = sum(1 for x in G if W[0][x] == u[x])
    b = z - g
    # the theorem, verbatim
    check(4 * b <= n17 - 2 - 3 * z, f"(CZB) VIOLATED on an F_17 witness: z={z} b={b}")
    # and the step-2 inequality it rests on
    pairsum = sum(sum(1 for x in range(n17) if W[i][x] == W[j][x])
                  for i, j in combinations(range(4), 2))
    offP = pairsum - 6 * z
    check(offP <= 6 * (K17 - 1 - z), f"step-2 bound violated: {offP} > {6*(K17-1-z)}")
    if offP == 6 * (K17 - 1 - z):
        tight += 1
    # step-3 pointwise bound
    for x in range(n17):
        if x in G:
            continue
        a_x = sum(1 for i in range(4) if W[i][x] == u[x])
        classes: dict[int, int] = {}
        for i in range(4):
            classes[W[i][x]] = classes.get(W[i][x], 0) + 1
        Px = sum(v * (v - 1) // 2 for v in classes.values())
        check(a_x <= 1 + Px, f"step-3 bound a_x <= 1+P(x) violated at x={x}")
        check(a_x <= 3, "a_x = 4 must be impossible off G")

if errors:
    for e in errors[:10]:
        print("FAIL:", e)
    sys.exit(1)

print(f"F_17: all 12 witnesses satisfy (CZB); step-2 bound TIGHT on {tight}/12")
print(
    "COMMON_ZERO_BUDGET_PASS "
    f"official_z_max={z_max} d_s_min={d_s_min} "
    f"min_support_excluded=yes b0_threshold={z_b0} f17_witnesses=12"
)
