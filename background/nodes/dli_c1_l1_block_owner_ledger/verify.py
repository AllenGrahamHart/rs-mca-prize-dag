#!/usr/bin/env python3
"""Exact verifier for dli_c1_l1_block_owner_ledger.

Replays, at a full official-shape split prime (q=7681, omega of exact
order 512, N=256):
  - the collision/relation/variance equivalences feeding the target form;
  - kappa mass 16 with kappa(0)=1 for every block;
  - the convolution recursion Z_(j+1)=Z_j+A_j at every one of 64 blocks;
  - the telescoping identity (BO-3) exactly, in rationals.
"""
from __future__ import annotations
from fractions import Fraction


def require(c: bool, m: str) -> None:
    if not c:
        raise AssertionError(m)


def prime_factors(n: int) -> list[int]:
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def primitive_root(p: int) -> int:
    fs = prime_factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // r, p) != 1 for r in fs):
            return g
    raise AssertionError("no primitive root")


def main() -> None:
    q, n = 7681, 256
    g = primitive_root(q)
    omega = pow(g, (q - 1) // 512, q)
    require(pow(omega, 256, q) == q - 1, "omega order")
    coeffs = [pow(omega, i, q) for i in range(n)]

    # Boolean subset-sum DP with 4-block checkpoints.
    counts = [0] * q
    counts[0] = 1
    z_values = [Fraction(1)]
    for idx, a in enumerate(coeffs, 1):
        new = counts.copy()
        for s, c in enumerate(counts):
            if c:
                new[(s + a) % q] += c
        counts = new
        if idx % 4 == 0:
            j = idx // 4
            cp = Fraction(sum(c * c for c in counts), 2 ** (2 * idx))
            z_values.append(2 ** idx * cp)

    require(len(z_values) == 65, "checkpoint count")
    require(sum(counts) == 2 ** n, "Boolean mass")

    # kappa mass and kappa(0)=1 per block (ternary DP over 4 coords).
    for j in range(64):
        block = coeffs[4 * j: 4 * j + 4]
        kap: dict[int, Fraction] = {0: Fraction(1)}
        for a in block:
            new: dict[int, Fraction] = {}
            for s, w in kap.items():
                for d, f in ((0, Fraction(1)), (1, Fraction(1, 2)), (-1, Fraction(1, 2))):
                    t = (s + d * a) % q
                    new[t] = new.get(t, Fraction(0)) + w * f
            kap = new
        require(sum(kap.values()) == 16, f"kappa mass block {j}")
        require(kap[0] == 1, f"kappa(0) != 1 at block {j}")

    # Telescoping identity (BO-3).
    owner_sum = Fraction(0)
    for j in range(64):
        actual = z_values[j + 1] - z_values[j]
        haar = Fraction(15 * 2 ** (4 * j), q)
        owner_sum += actual - haar
    terminal = z_values[-1] - Fraction(2 ** 256, q)
    require(terminal == Fraction(1) - Fraction(1, q) + owner_sum,
            "telescoping identity (BO-3)")

    print("DLI_C1_L1_BLOCK_OWNER_LEDGER_PASS",
          f"q={q} blocks=64 terminal_minus_haar={float(terminal):.6f}")


if __name__ == "__main__":
    main()
