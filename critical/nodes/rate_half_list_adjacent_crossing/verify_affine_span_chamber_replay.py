#!/usr/bin/env python3
"""Fail-closed replay of the GF affine-span / rank-flat list compilers against
this node (H1/S3, 2026-07-26).  Stdlib only, exact integers, no floats.

Upstream sources, read-only at przchojecki/rs-mca origin/main = b13de811:
  experimental/grande_finale.tex:498  thm:affine-span-list
  experimental/grande_finale.tex:583  thm:rank-flat-list
(Both are HIS theorems.  This script consumes them; it proves neither.  Note the
Convergence Ledger r1 cites these as ":498/:583" without naming the file -- they
live in grande_finale.tex, NOT proximity_prize_results_v4.tex, and the ledger's
third citation `thm:single-mds-circuit-ray ":421"` is RS_MCA_Paving_v9.2.tex:1514.)

What this pins:
  A. Official-scale caps (n=2^41, K=2^40) at m = 3n/4 and m = 3n/4 - 1.
  B. The s=1 exclusion -- no THREE list codewords at agreement >= 3n/4 - 1 are
     collinear -- proved directly here, independently of the compiler, with the
     exact agreement floor down to which the direct argument still fires.
  C. The exact F_17 four-codeword witness at agreement 3n/4 - 1 that
     statement.md cites but never banked as integers, and the measured slack of
     BOTH compilers on it.

Headline negative result (see notes/affine_span_chamber_replay_20260726.md):
the compilers kill NONE of the thirteen edge-degree chambers, so the ledger's
S3 promotion test does not fire and H1 stays ev-wired.
"""

from __future__ import annotations

import sys
from math import comb, prod

# ---------------------------------------------------------------- official row
N_OFF = 2**41
K_OFF = 2**40
R_OFF = N_OFF - K_OFF                      # redundancy n-K
D_OFF = R_OFF + 1                          # MDS distance

# Pinned caps, recomputed below (Q0-style: recompute, never trust).
EXPECTED_AFFINE_CAPS = {
    (3 * N_OFF // 4, 0): 1,
    (3 * N_OFF // 4, 1): 1,
    (3 * N_OFF // 4, 2): 3,
    (3 * N_OFF // 4, 3): 7,
    (3 * N_OFF // 4 - 1, 0): 1,
    (3 * N_OFF // 4 - 1, 1): 2,
    (3 * N_OFF // 4 - 1, 2): 4,
    (3 * N_OFF // 4 - 1, 3): 8,
}
# Lowest agreement at which the direct 3-collinear argument still fires.
EXPECTED_COLLINEAR_FLOOR = 1466015503701

# ------------------------------------------------------------- F_17 witness
P17, N17, K17 = 17, 16, 8
M17 = 3 * N17 // 4 - 1                     # 11
U17 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 15, 12, 7, 15)
WORDS17 = {
    "f0": (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "f1": (0, 0, 0, 0, 0, 10, 7, 0, 7, 3, 0, 12, 15, 12, 7, 15),
    "f2": (0, 0, 0, 2, 13, 0, 0, 0, 1, 0, 15, 6, 4, 12, 7, 15),
    "f3": (0, 4, 6, 0, 0, 0, 0, 0, 0, 10, 6, 6, 15, 13, 7, 15),
}
EXPECTED_WITNESS = {
    "s": 3, "d": {1: 9, 2: 12, 3: 14}, "z": 2, "g": 2, "b": 0,
    "list_size": 4, "affine_cap": 8, "rank_flat_cap": 8,
    "pairwise_agreement": 7,
}

INV17 = [0] + [pow(a, P17 - 2, P17) for a in range(1, P17)]
DOM17 = list(range(1, 17))                 # F_17^*

errors: list[str] = []


def check(cond: bool, msg: str) -> None:
    if not cond:
        errors.append(msg)


# ------------------------------------------------------------------ part A
def affine_span_cap(n: int, k: int, m: int, s: int) -> int:
    """GF thm:affine-span-list: floor( C(n-K+s, s) / C(w+s, s) ), w = m-K."""
    return comb(n - k + s, s) // comb(m - k + s, s)


for (m, s), want in sorted(EXPECTED_AFFINE_CAPS.items()):
    got = affine_span_cap(N_OFF, K_OFF, m, s)
    check(got == want, f"official affine-span cap drift at m={m}, s={s}: {got} != {want}")

# The two facts the rest of the node leans on.
check(affine_span_cap(N_OFF, K_OFF, 3 * N_OFF // 4, 1) == 1,
      "at m=3n/4 an affine line must carry at most ONE list member")
check(affine_span_cap(N_OFF, K_OFF, 3 * N_OFF // 4 - 1, 1) == 2,
      "at m=3n/4-1 an affine line must carry at most TWO list members")
check(affine_span_cap(N_OFF, K_OFF, 3 * N_OFF // 4 - 1, 2) == 4,
      "at m=3n/4-1 an affine plane cap must be exactly 4 (four codewords sit AT it)")

# ------------------------------------------------------------------ part B
# Three collinear list members c_0, c_0+L1 v, c_0+L2 v force one shared support
# supp(v).  On it the three values are pairwise distinct, so at most one agrees
# with u per position; off it all three coincide.  Hence
#     3m <= 3(n - wt(v)) + wt(v)   =>   wt(v) <= 3(n-m)/2,
# while MDS gives wt(v) >= n-K+1.  Contradiction iff n-K+1 > floor(3(n-m)/2).
def collinear_excluded(n: int, k: int, m: int) -> bool:
    return (n - k + 1) > 3 * (n - m) // 2


for m in (3 * N_OFF // 4, 3 * N_OFF // 4 - 1, 3 * N_OFF // 4 - 2):
    check(collinear_excluded(N_OFF, K_OFF, m),
          f"direct 3-collinear exclusion must fire at official m={m}")

# Closed form for the floor: fires iff 3(n-m) <= 2(n-K+1)-1.
t_max = (2 * D_OFF - 1) // 3
m_floor = N_OFF - t_max
check(m_floor == EXPECTED_COLLINEAR_FLOOR,
      f"collinear-exclusion floor drift: {m_floor} != {EXPECTED_COLLINEAR_FLOOR}")
check(collinear_excluded(N_OFF, K_OFF, m_floor), "exclusion must fire at its floor")
check(not collinear_excluded(N_OFF, K_OFF, m_floor - 1),
      "exclusion must NOT fire one step below its floor (else the floor is wrong)")
# It must also fire at the F_17 scale, where the witness lives.
check(collinear_excluded(N17, K17, M17), "3-collinear exclusion must fire on the F_17 row")

# ------------------------------------------------------------------ part C
def rref17(rows: list[list[int]]) -> list[list[int]]:
    rows = [list(x) for x in rows]
    r = 0
    for c in range(len(rows[0])):
        sel = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if sel is None:
            continue
        rows[r], rows[sel] = rows[sel], rows[r]
        iv = INV17[rows[r][c]]
        rows[r] = [x * iv % P17 for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                f = rows[i][c]
                rows[i] = [(a - f * b) % P17 for a, b in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return [x for x in rows if any(x)]


def interpolate_degree(word: tuple[int, ...]) -> int:
    """Degree of the unique interpolant of `word` on DOM17, or -1 for the zero word."""
    coeffs = [0] * N17
    for i, xi in enumerate(DOM17):
        if word[i] == 0:
            continue
        # Lagrange basis L_i(X) = prod_{j!=i} (X - x_j)/(x_i - x_j)
        num = [1] + [0] * N17
        deg = 0
        den = 1
        for j, xj in enumerate(DOM17):
            if j == i:
                continue
            new = [0] * (N17 + 1)
            for dd in range(deg + 1):
                new[dd + 1] = (new[dd + 1] + num[dd]) % P17
                new[dd] = (new[dd] - xj * num[dd]) % P17
            num, deg = new, deg + 1
            den = den * (xi - xj) % P17
        scale = word[i] * INV17[den % P17] % P17
        for dd in range(deg + 1):
            coeffs[dd] = (coeffs[dd] + scale * num[dd]) % P17
    for dd in range(N17 - 1, -1, -1):
        if coeffs[dd]:
            return dd
    return -1


def agreement(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    return sum(1 for x, y in zip(a, b) if x == y)


names17 = list(WORDS17)
for nm in names17:
    deg = interpolate_degree(WORDS17[nm])
    check(deg < K17, f"witness {nm} is not a codeword: interpolant degree {deg} >= {K17}")
    check(agreement(WORDS17[nm], U17) >= M17,
          f"witness {nm} agreement {agreement(WORDS17[nm], U17)} < {M17}")
for i in range(len(names17)):
    for j in range(i + 1, len(names17)):
        ag = agreement(WORDS17[names17[i]], WORDS17[names17[j]])
        check(ag <= K17 - 1,
              f"witness {names17[i]},{names17[j]} agree in {ag} > {K17-1} places")
        check(ag == EXPECTED_WITNESS["pairwise_agreement"],
              f"witness pairwise agreement drift {names17[i]},{names17[j]}: {ag}")

basis = rref17([[(WORDS17[nm][i] - WORDS17["f0"][i]) % P17 for i in range(N17)]
                for nm in names17[1:]])
s17 = len(basis)
check(s17 == EXPECTED_WITNESS["s"], f"witness affine rank drift: {s17}")
Bvec = [tuple(basis[k][i] for k in range(s17)) for i in range(N17)]


def proj_points(dim: int) -> list[tuple[int, ...]]:
    pts = []
    for lead in range(dim):
        for k in range(P17 ** (dim - lead - 1)):
            v, r = [0] * lead + [1], k
            for _ in range(dim - lead - 1):
                v.append(r % P17)
                r //= P17
            pts.append(tuple(v))
    return pts


PTS = proj_points(s17)
check(len(PTS) == (P17**s17 - 1) // (P17 - 1), "projective point count wrong")

d = {}
d[1] = min(sum(1 for i in range(N17)
               if sum(c[k] * Bvec[i][k] for k in range(s17)) % P17) for c in PTS)
d[s17] = sum(1 for i in range(N17) if any(Bvec[i]))
if s17 == 3:                                   # dim-2 subspaces = kernels of duals
    best = None
    for phi in PTS:
        lead = next(j for j in range(s17) if phi[j])
        cz = 0
        for i in range(N17):
            bi = Bvec[i]
            if not any(bi):
                cz += 1
                continue
            if bi[lead] == 0:
                continue
            lam = bi[lead] * INV17[phi[lead]] % P17
            if all(bi[j] == lam * phi[j] % P17 for j in range(s17)):
                cz += 1
        supp = N17 - cz
        best = supp if best is None else min(best, supp)
    d[2] = best
for j, want in EXPECTED_WITNESS["d"].items():
    check(d.get(j) == want, f"witness d_{j} drift: {d.get(j)} != {want}")
for j in range(1, s17 + 1):                    # MDS floor must hold
    check(d[j] >= (N17 - K17) + j, f"witness d_{j}={d[j]} below the MDS floor")

G = [i for i in range(N17) if not any(Bvec[i])]
z17, g17 = len(G), sum(1 for i in G if WORDS17["f0"][i] == U17[i])
b17 = z17 - g17
check(z17 == EXPECTED_WITNESS["z"] and g17 == EXPECTED_WITNESS["g"]
      and b17 == EXPECTED_WITNESS["b"], f"witness (z,g,b) drift: {(z17, g17, b17)}")
check(z17 == N17 - d[s17], "z must equal n - d_s")

L17 = sum(1 for nm in names17 if agreement(WORDS17[nm], U17) >= M17)
check(L17 == EXPECTED_WITNESS["list_size"], f"witness list size drift: {L17}")

asc17 = affine_span_cap(N17, K17, M17, s17)
t17 = N17 - M17
rf17 = prod(d[s17] - i for i in range(s17)) // prod(d[j] - t17 + b17
                                                    for j in range(1, s17 + 1))
check(asc17 == EXPECTED_WITNESS["affine_cap"], f"witness affine-span cap drift: {asc17}")
check(rf17 == EXPECTED_WITNESS["rank_flat_cap"], f"witness rank-flat cap drift: {rf17}")
# Both are theorems: they MUST hold on a real configuration.
check(asc17 >= L17, "affine-span compiler VIOLATED by the witness")
check(rf17 >= L17, "rank-flat compiler VIOLATED by the witness")
# ...and both are loose on it -- the finding that keeps H1 ev-wired.
check(asc17 > L17 and rf17 > L17,
      "compilers unexpectedly TIGHT on the witness -- rerun the chamber analysis")

if errors:
    for e in errors:
        print("FAIL:", e)
    sys.exit(1)

print(
    "AFFINE_SPAN_CHAMBER_REPLAY_PASS "
    f"official_caps={len(EXPECTED_AFFINE_CAPS)} "
    f"collinear_floor={m_floor} "
    f"witness=F_{P17}[n={N17},k={K17},m={M17}] s={s17} "
    f"d={tuple(d[j] for j in range(1, s17+1))} b={b17} "
    f"list={L17} affine_cap={asc17} rank_flat_cap={rf17} slack={asc17-L17}"
)
