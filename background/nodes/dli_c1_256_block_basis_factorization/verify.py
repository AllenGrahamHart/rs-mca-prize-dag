#!/usr/bin/env python3
"""Exact verifier for dli_c1_256_block_basis_factorization.

Checks, over exact split prime fields at L in {1, 2, 4} (and the orbit
identity additionally at L = 8):
  (i)   theta = omega^256 has exact order 2L; block identity A_a = D_a F;
        every one of the 256 blocks is invertible;
  (ii)  |A_a {0,1}^L| = 2^L for representative blocks (parallelepipeds);
  (iii) {A_a^T lambda : lambda in F_q^L} = F_q^L for representative blocks
        at L = 1, 2 (exact marginal bijectivity);
  (iv)  C_a = M^a C_0 with M = F^T D_1 F^(-T), on random exact lambda.

All arithmetic is exact modular integer arithmetic.
"""
from __future__ import annotations

import random
from itertools import product


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def factor_distinct(n: int) -> list[int]:
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.append(n)
    return out


def primitive_root(q: int) -> int:
    fs = factor_distinct(q - 1)
    for g in range(2, q):
        if all(pow(g, (q - 1) // p, q) != 1 for p in fs):
            return g
    raise RuntimeError(f"no primitive root mod {q}")


def exact_order(x: int, q: int, order: int) -> bool:
    return pow(x, order, q) == 1 and all(
        pow(x, order // p, q) != 1 for p in factor_distinct(order)
    )


def mat_mul(a, b, q):
    n, m, k = len(a), len(b[0]), len(b)
    return [
        [sum(a[i][t] * b[t][j] for t in range(k)) % q for j in range(m)]
        for i in range(n)
    ]


def mat_inv(a, q):
    n = len(a)
    aug = [row[:] + [int(i == j) for j in range(n)] for i, row in enumerate(a)]
    for col in range(n):
        piv = next(r for r in range(col, n) if aug[r][col] % q)
        aug[col], aug[piv] = aug[piv], aug[col]
        inv = pow(aug[col][col], -1, q)
        aug[col] = [x * inv % q for x in aug[col]]
        for r in range(n):
            if r != col and aug[r][col] % q:
                s = aug[r][col]
                aug[r] = [(x - s * y) % q for x, y in zip(aug[r], aug[col])]
    return [row[n:] for row in aug]


def det_mod(matrix, q):
    a = [row[:] for row in matrix]
    n, det = len(a), 1
    for col in range(n):
        piv = next((r for r in range(col, n) if a[r][col] % q), None)
        if piv is None:
            return 0
        if piv != col:
            a[piv], a[col] = a[col], a[piv]
            det = -det
        pv = a[col][col] % q
        det = det * pv % q
        inv = pow(pv, -1, q)
        for r in range(col + 1, n):
            if a[r][col] % q:
                s = a[r][col] * inv % q
                for j in range(col, n):
                    a[r][j] = (a[r][j] - s * a[col][j]) % q
    return det % q


def transpose(a):
    return [list(row) for row in zip(*a)]


def check_level(ell: int, q: int, check_marginal: bool, check_cube: bool) -> None:
    n = 256 * ell
    order = 2 * n
    require((q - 1) % order == 0, f"q={q} does not split order {order}")
    g = primitive_root(q)
    omega = pow(g, (q - 1) // order, q)
    require(exact_order(omega, q, order), f"omega order, ell={ell}")
    theta = pow(omega, 256, q)
    require(exact_order(theta, q, 2 * ell), f"theta order 2L, ell={ell}")

    F = [[pow(theta, (2 * j + 1) * b, q) for b in range(ell)] for j in range(ell)]
    require(det_mod(F, q) != 0, f"F singular, ell={ell}")

    d1 = [pow(omega, 2 * j + 1, q) for j in range(ell)]
    blocks = []
    for a in range(256):
        da = [pow(x, a, q) for x in d1]
        block = [
            [pow(omega, (2 * j + 1) * (a + 256 * b), q) for b in range(ell)]
            for j in range(ell)
        ]
        rebuilt = [[da[j] * F[j][b] % q for b in range(ell)] for j in range(ell)]
        require(block == rebuilt, f"(KBB-1) fails, ell={ell}, a={a}")
        require(det_mod(block, q) != 0, f"block singular, ell={ell}, a={a}")
        blocks.append(block)

    if check_cube:
        for a in (0, 1, 255):
            images = {
                tuple(sum(blocks[a][i][j] * bit[j] for j in range(ell)) % q
                      for i in range(ell))
                for bit in product((0, 1), repeat=ell)
            }
            require(len(images) == 1 << ell, f"parallelepiped defect, a={a}")

    if check_marginal:
        for a in (0, 7, 255):
            at = transpose(blocks[a])
            images = {
                tuple(sum(at[i][j] * lam[j] for j in range(ell)) % q
                      for i in range(ell))
                for lam in product(range(q), repeat=ell)
            }
            require(len(images) == q**ell, f"marginal not bijective, a={a}")

    # (iv) companion orbit on random exact lambda.
    ft = transpose(F)
    m = mat_mul(mat_mul(ft, [[d1[i] * int(i == j) for j in range(ell)]
                             for i in range(ell)], q), mat_inv(ft, q), q)
    rng = random.Random(20260801 + ell)
    for _ in range(3):
        lam = [rng.randrange(q) for _ in range(ell)]
        c = [sum(ft[i][j] * lam[j] for j in range(ell)) % q for i in range(ell)]
        power = [[int(i == j) for j in range(ell)] for i in range(ell)]
        for a in range(256):
            expect = [sum(transpose(blocks[a])[i][j] * lam[j]
                          for j in range(ell)) % q for i in range(ell)]
            mc = [sum(power[i][j] * c[j] for j in range(ell)) % q
                  for i in range(ell)]
            require(mc == expect, f"(KBB-2) fails, ell={ell}, a={a}")
            power = mat_mul(m, power, q)

    print(f"LEVEL_PASS ell={ell} q={q} blocks=256")


def main() -> None:
    check_level(1, 7681, check_marginal=True, check_cube=True)
    check_level(2, 12289, check_marginal=False, check_cube=True)
    check_level(4, 12289, check_marginal=False, check_cube=True)
    check_level(8, 12289, check_marginal=False, check_cube=False)
    print("DLI_C1_256_BLOCK_BASIS_FACTORIZATION_PASS")


if __name__ == "__main__":
    main()
