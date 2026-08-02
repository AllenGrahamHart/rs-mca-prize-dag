#!/usr/bin/env python3
"""Verifier for dli_c1_ternary_relation_norm_sandwich.

Exact integer replay of the four claims:
  A  doubling embedding squares the norm      (exhaustive M=2,4)
  B  AM-GM ceiling + positivity + weight-max  (exhaustive N=4,8)
  C  saturation propagation witnesses          (Bareiss at N=16,32)
  D  router threshold spot checks              (2N=8 empty; 2N=16 w3)

Pure python ints, fraction-free Bareiss determinants, no imports beyond
itertools. Run: tools/ramguard tiny -- python3 verify.py
"""
import itertools
import sys


def mult_matrix(f, N):
    """Multiplication-by-f matrix on Z[x]/(x^N+1); column j = f*x^j."""
    cols = []
    for j in range(N):
        col = [0] * N
        for i, c in enumerate(f):
            if c == 0:
                continue
            k = i + j
            if k < N:
                col[k] += c
            else:
                col[k - N] -= c
        cols.append(col)
    return [[cols[j][i] for j in range(N)] for i in range(N)]


def bareiss_det(m):
    """Fraction-free Bareiss determinant with row-swap pivoting."""
    a = [row[:] for row in m]
    n = len(a)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            for r in range(k + 1, n):
                if a[r][k] != 0:
                    a[k], a[r] = a[r], a[k]
                    sign = -sign
                    break
            else:
                return 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * a[k][k] - a[i][k] * a[k][j]) // prev
            a[i][k] = 0
        prev = a[k][k]
    return sign * a[n - 1][n - 1]


def norm(f, N):
    return bareiss_det(mult_matrix(f, N))


def ternary_vectors(N):
    return itertools.product((-1, 0, 1), repeat=N)


def iota(g):
    """g(y) -> g(x^2): spread coefficients onto even indices."""
    f = [0] * (2 * len(g))
    for i, c in enumerate(g):
        f[2 * i] = c
    return f


def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    if not ok:
        sys.exit(1)


def main():
    # A: Norm_{2M}(iota g) == Norm_M(g)^2, exhaustive at M=2,4
    for M in (2, 4):
        bad = 0
        cnt = 0
        for g in ternary_vectors(M):
            cnt += 1
            if norm(iota(list(g)), 2 * M) != norm(list(g), M) ** 2:
                bad += 1
        check(f"A: doubling embedding squares Norm (M={M})", bad == 0,
              f"{cnt} vectors, {bad} violations")

    # B: 1 <= Norm <= w^(N/2) for nonzero f; per-weight maxima tables
    expected_max = {
        4: {0: 0, 1: 1, 2: 4, 3: 9, 4: 8},
        8: {0: 0, 1: 1, 2: 16, 3: 81, 4: 196, 5: 529, 6: 1154,
            7: 2401, 8: 2176},
    }
    saturating = {4: {1, 2, 3}, 8: {1, 2, 3, 7}}
    for N in (4, 8):
        maxima = {w: 0 for w in range(N + 1)}
        viol = 0
        for f in ternary_vectors(N):
            w = sum(1 for c in f if c)
            d = norm(list(f), N)
            if w and not (1 <= d <= w ** (N // 2)):
                viol += 1
            if w == 0 and d != 0:
                viol += 1
            if d > maxima[w]:
                maxima[w] = d
        check(f"B: ceiling/positivity exhaustive (N={N})", viol == 0,
              f"3^{N} vectors")
        check(f"B: per-weight maxima table (N={N})",
              maxima == expected_max[N], str(maxima))
        sat = {w for w in range(1, N + 1) if maxima[w] == w ** (N // 2)}
        check(f"B: saturating weights exactly {sorted(saturating[N])} (N={N})",
              sat == saturating[N], str(sorted(sat)))

    # C: saturation propagation witnesses via iterated iota
    w7 = [1, 1, 1, -1, -1, 1, -1, 0]          # N=8 argmax, norm 7^4
    check("C: w=7 base witness at N=8", norm(w7, 8) == 7 ** 4)
    w7_16 = iota(w7)
    check("C: w=7 sandwich witness at N=16", norm(w7_16, 16) == 7 ** 8)
    check("C: w=7 sandwich witness at N=32", norm(iota(w7_16), 32) == 7 ** 16)
    w2_32 = [0] * 32
    w2_32[0] = w2_32[16] = 1                   # iota^3 of 1+x^2
    check("C: w=2 sandwich witness at N=32", norm(w2_32, 32) == 2 ** 16)
    w3 = [1, 1, -1, 0]                          # N=4 argmax, norm 9
    check("C: w=3 base witness at N=4", norm(w3, 4) == 9)
    check("C: w=3 sandwich witness at N=16",
          norm(iota(iota(w3)), 16) == 3 ** 8)

    # D: router thresholds
    def is_prime(n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    smallest_adm_8 = next(q for q in itertools.count(2)
                          if is_prime(q) and q % 8 == 1)
    check("D: smallest admissible prime at 2N=8 is 17 > maxnorm 9",
          smallest_adm_8 == 17 and 17 > 9)
    w3_16 = [1, 1, 0, 1, 0, 0, 0, 0]           # 2N=16 census witness for 17
    check("D: q=17 exceptional witness at 2N=16 (w=3, Norm=17 <= 81)",
          norm(w3_16, 8) == 17 and 17 <= 3 ** 4)
    check("D: thresholds w^(N/2) monotone in w (N=16)",
          all((w + 1) ** 8 > w ** 8 for w in range(1, 16)))

    print("DLI_C1_TERNARY_RELATION_NORM_SANDWICH_ALL_PASS")


if __name__ == "__main__":
    main()
