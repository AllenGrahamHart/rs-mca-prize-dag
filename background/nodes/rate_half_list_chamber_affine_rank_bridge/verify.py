#!/usr/bin/env python3
"""Wired falsifier for rate_half_list_chamber_affine_rank_bridge (2026-07-26).

Re-derives EVERY four-codeword witness in the normalized branch of the banked
RS[F_17,F_17^*,8] row at agreement a = 3n/4 - 1 and pins the affine-invariant
census (s, d_1, d_s, z, g, b) over that branch.

The node conjectures the bridge returns s = 3, b = 0 always.  The falsifier is a
witness in this branch with s != 3 or b != 0 -- this script fails closed on one.

Stdlib only, exact integers over F_17, no floats.  Branch: f_0 = 0 (translate u),
Z = zero set of u with |Z| = 11, each other member c_i * P_{R_i} with R_i subset Z,
|R_i| = 7, agreeing with u on 4 of the 5 points of N = D \\ Z (the sigma(i) = i
pattern; see the statement's "Expected sign" section).
"""

from __future__ import annotations

import sys
from collections import Counter
from itertools import combinations

P, N_LEN, K = 17, 16, 8
M = 3 * N_LEN // 4 - 1                      # 11
R_RED = N_LEN - K                           # 8
DOM = list(range(1, 17))                    # F_17^*
INV = [0] + [pow(a, P - 2, P) for a in range(1, P)]
Z, NN = DOM[:11], DOM[11:]

# Pinned census over the branch: (s, d_1, d_s, z, g, b) -> multiplicity.
EXPECTED_CENSUS = {
    (3, 9, 14, 2, 2, 0): 9,
    (3, 9, 15, 1, 1, 0): 3,
}
EXPECTED_WITNESSES = 12
EXPECTED_PAIR_AGREEMENTS = {7: 71, 6: 1}

errors: list[str] = []


def check(cond: bool, msg: str) -> None:
    if not cond:
        errors.append(msg)


def pval(roots, x: int) -> int:
    v = 1
    for r in roots:
        v = v * (x - r) % P
    return v


def rref(rows):
    rows, r = [list(x) for x in rows], 0
    for c in range(len(rows[0])):
        sel = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if sel is None:
            continue
        rows[r], rows[sel] = rows[sel], rows[r]
        iv = INV[rows[r][c]]
        rows[r] = [x * iv % P for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                f = rows[i][c]
                rows[i] = [(a - f * b) % P for a, b in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return [x for x in rows if any(x)]


def proj_points(dim: int):
    pts = []
    for lead in range(dim):
        for k in range(P ** (dim - lead - 1)):
            v, rr = [0] * lead + [1], k
            for _ in range(dim - lead - 1):
                v.append(rr % P)
                rr //= P
            pts.append(tuple(v))
    return pts


RSETS = list(combinations(Z, 7))
check(len(RSETS) == 330, f"root-set count drift: {len(RSETS)}")
V = {R: tuple(pval(R, y) for y in NN) for R in RSETS}
for R in RSETS:
    check(all(v != 0 for v in V[R]), "P_R must not vanish on N")

# --- enumerate the branch -------------------------------------------------
sols = []
for R1 in RSETS:
    v1 = V[R1]
    for R2 in RSETS:
        if R2 == R1:
            continue
        v2 = V[R2]
        c2 = v1[3] * INV[v2[3]] % P
        if c2 * v2[4] % P != v1[4] or c2 * v2[2] % P != v1[2]:
            continue
        for R3 in RSETS:
            if R3 in (R1, R2):
                continue
            v3 = V[R3]
            c3 = v1[3] * INV[v3[3]] % P
            if c3 * v3[4] % P != v1[4] or c3 * v3[1] % P != v1[1]:
                continue
            if c2 * v2[0] % P != c3 * v3[0] % P:
                continue
            sols.append((R1, R2, R3, 1, c2, c3))

check(len(sols) == EXPECTED_WITNESSES,
      f"witness count drift: {len(sols)} != {EXPECTED_WITNESSES}")

# --- measure each witness -------------------------------------------------
census: Counter = Counter()
pair_agr: Counter = Counter()
for (R1, R2, R3, c1, c2, c3) in sols:
    u = [0] * N_LEN
    u[NN[3] - 1] = c1 * V[R1][3] % P
    u[NN[4] - 1] = c1 * V[R1][4] % P
    u[NN[0] - 1] = c2 * V[R2][0] % P
    u[NN[1] - 1] = c1 * V[R1][1] % P
    u[NN[2] - 1] = c1 * V[R1][2] % P

    words = [tuple([0] * N_LEN)]
    for R, c in ((R1, c1), (R2, c2), (R3, c3)):
        words.append(tuple(c * pval(R, x) % P for x in DOM))

    for w in words:
        agr = sum(1 for i in range(N_LEN) if w[i] == u[i])
        check(agr >= M, f"witness member below agreement {M}: {agr}")
    for a, b in combinations(range(4), 2):
        ag = sum(1 for i in range(N_LEN) if words[a][i] == words[b][i])
        check(ag <= K - 1, f"two members agree in {ag} > {K-1} places (not distinct codewords)")
        pair_agr[ag] += 1

    basis = rref([tuple((w[i] - words[0][i]) % P for i in range(N_LEN))
                  for w in words[1:]])
    s = len(basis)
    B = [tuple(basis[k][i] for k in range(s)) for i in range(N_LEN)]
    pts = proj_points(s)
    d1 = min(sum(1 for i in range(N_LEN)
                 if sum(c[k] * B[i][k] for k in range(s)) % P) for c in pts)
    ds = sum(1 for i in range(N_LEN) if any(B[i]))
    G = [i for i in range(N_LEN) if not any(B[i])]
    z = len(G)
    g = sum(1 for i in G if words[0][i] == u[i])
    check(d1 >= R_RED + 1, f"d_1 = {d1} below the MDS floor {R_RED+1}")
    check(ds >= R_RED + s, f"d_s = {ds} below the MDS floor {R_RED+s}")
    check(z == N_LEN - ds, "z must equal n - d_s")
    census[(s, d1, ds, z, g, z - g)] += 1

check(dict(census) == EXPECTED_CENSUS, f"affine-invariant census drift: {dict(census)}")
check(dict(pair_agr) == EXPECTED_PAIR_AGREEMENTS,
      f"pairwise-agreement census drift: {dict(pair_agr)}")

# --- THE FALSIFIER --------------------------------------------------------
ranks = {k[0] for k in census}
bs = {k[5] for k in census}
check(ranks == {3}, f"FALSIFIER FIRED: affine rank is not constant on the branch: {sorted(ranks)}")
check(bs == {0}, f"FALSIFIER FIRED: b is not identically 0 on the branch: {sorted(bs)}")

# s >= 2 must hold here too (the proved collinearity exclusion at this row).
check((N_LEN - K + 1) > 3 * (N_LEN - M) // 2,
      "the s>=2 exclusion must fire on the F_17 row")

if errors:
    for e in errors:
        print("FAIL:", e)
    sys.exit(1)

print(
    "CHAMBER_AFFINE_RANK_BRIDGE_FALSIFIER_PASS "
    f"witnesses={len(sols)} ranks={sorted(ranks)} b={sorted(bs)} "
    f"census={{{', '.join(f'{k}:{v}' for k, v in sorted(census.items()))}}} "
    "(bridge conjecture s=3,b=0 NOT falsified on this branch)"
)
