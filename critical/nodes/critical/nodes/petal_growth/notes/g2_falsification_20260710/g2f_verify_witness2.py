#!/usr/bin/env python3
"""g2f_verify_witness2: fully self-contained re-verification of the GENERIC
(shuffled-layout) fixed-M hybrid witness at n=32.  All data hardcoded from
the run's dump; nothing imported.

Witness tuple:
  p=97, n=32, k=12, sigma=1, M in {4, 8}
  D = order-32 subgroup of F_97^* (listed explicitly below, x_j = 9^j? --
      irrelevant: D is verified directly to be the order-32 subgroup)
  U : listed explicitly below (a G4/sunflower auxiliary word: 0 on an
      11-point core + background, c_i * L_core on ten 2-point petals)
  f(X) = 92 + 95X + 18X^2 + 0X^3 + 83X^4 + 72X^5 + 47X^6 + 36X^7 + 35X^8
         + 14X^9 + 49X^10 + 10X^11   (degree 11 < k = 12)

Claims checked from scratch:
  1. D is exactly the order-32 multiplicative subgroup; x_{j+1} = g0*x_j.
  2. f agrees with U exactly on S = {0,4,5,9,12,13,15,16,20,21,25,28,29,31}
     (exponent indices), |S| = 14 >= k+sigma = 13: a list member.
  3. |S| = 14 lies in the fixed-M top defect band [13, 13+M-1] for M=4 and M=8.
  4. S is NOT of tail-plus-full-M-fibers form at M=4 (residual 10 >= 4) nor
     at M=8 (residual 14 >= 8) -- fails both lax and strict staircase at M.
  5. The order-M subgroup stabilizer of S is nontrivial for M=4 and M=8
     (the involution shift +16 fixes S).
  => f is neither staircase-at-M nor stabilizer-primitive: fixed-M hybrid.
  6. Closure-form charge: S IS a union of full 2-fibers (staircase at scale 2,
     empty tail) -- consistent with the G2 closure dichotomy.
"""
P = 97
N = 32
K = 12
SIGMA = 1
DOM = [1, 28, 8, 30, 64, 46, 27, 77, 22, 34, 79, 78, 50, 42, 12, 45, 96, 69,
       89, 67, 33, 51, 70, 20, 75, 63, 18, 19, 47, 55, 85, 52]
VALUES = [66, 0, 24, 91, 0, 0, 85, 0, 0, 0, 0, 0, 81, 28, 30, 51, 0, 0, 84,
          60, 95, 83, 28, 54, 63, 34, 0, 31, 0, 34, 78, 62]
POLY = [92, 95, 18, 0, 83, 72, 47, 36, 35, 14, 49, 10]
S_CLAIM = [0, 4, 5, 9, 12, 13, 15, 16, 20, 21, 25, 28, 29, 31]
CORE = [1, 4, 5, 7, 9, 10, 11, 16, 17, 26, 28]
PETALS = [[19, 30], [13, 22], [0, 21], [6, 29], [12, 20], [14, 23], [3, 15],
          [2, 31], [24, 25], [18, 27]]
SCALARS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
BACKGROUND = [8]


def ev(poly, x):
    v = 0
    for c in reversed(poly):
        v = (v * x + c) % P
    return v


def main():
    # 1. D is the order-32 subgroup, cyclically ordered
    assert all(pow(x, 32, P) == 1 for x in DOM)
    assert len(set(DOM)) == 32
    assert any(all(pow(g, e, P) != 1 for e in (1, 2, 4, 8, 16)) for g in DOM)
    g0 = DOM[1]
    assert all(DOM[(j + 1) % 32] == g0 * DOM[j] % P for j in range(32))
    # 1b. U is a sunflower word: 0 on core+background, c_i*L_core on petals
    lc = [1]
    for j in CORE:
        r = DOM[j]
        new = [0] * (len(lc) + 1)
        for i, c in enumerate(lc):
            new[i] = (new[i] - r * c) % P
            new[i + 1] = (new[i + 1] + c) % P
        lc = new
    for j in CORE + BACKGROUND:
        assert VALUES[j] == 0
    for ci, petal in zip(SCALARS, PETALS):
        for j in petal:
            assert VALUES[j] == ci * ev(lc, DOM[j]) % P, (ci, j)
    # 2. agreement set of f
    S = sorted(j for j in range(32) if ev(POLY, DOM[j]) == VALUES[j])
    assert S == S_CLAIM, S
    assert len(S) == 14 >= K + SIGMA
    Sset = set(S)
    for M in (4, 8):
        # 3. band
        assert K + SIGMA <= len(S) <= K + SIGMA + M - 1, M
        # 4. staircase at M fails (fibers of x->x^M = exponent cosets mod 32/M)
        step = N // M
        full = [r for r in range(step)
                if all((r + step * i) in Sset for i in range(M))]
        residual = len(S) - M * len(full)
        assert residual >= M, (M, residual)
        # 5. order-M-subgroup stabilizer nontrivial
        stab = [a for a in range(0, N, step)
                if all(((x + a) % N) in Sset for x in S)]
        assert len(stab) >= 2, (M, stab)
        print(f"M={M}: band [{K+SIGMA},{K+SIGMA+M-1}] contains |S|=14; "
              f"full {M}-fibers in S: {len(full)}, residual {residual} >= {M} "
              f"(NOT staircase, lax or strict); stabilizer shifts {stab} "
              f"(NONTRIVIAL) => FIXED-M HYBRID CONFIRMED")
    # 6. closure charge at scale 2
    pairs = [r for r in range(16) if r in Sset and (r + 16) in Sset]
    assert 2 * len(pairs) == len(S)
    print(f"closure form: S = union of {len(pairs)} full 2-fibers, tail 0 "
          f"=> STAIRCASE at scale 2 (closure dichotomy holds for this witness)")
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
