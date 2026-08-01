#!/usr/bin/env python3
"""Exact/replayable checks for the Brief-1 C1'-r3 proof-program dossier.

This is not a proof of C1'-r3.  It checks the algebraic rewrites, official
schedule arithmetic, finite-census route size, the 256-block basis
factorization on representative exact fields, the current ten-slot
zero-window decomposition, and selected banked exact fractions.

All verdicts use integers or fractions.  Floating point is display-only.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import gcd


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def v2(n: int) -> int:
    out = 0
    while n % 2 == 0:
        out += 1
        n //= 2
    return out


def factor_distinct(n: int) -> list[int]:
    out: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.append(n)
    return out


def primitive_root_prime(q: int) -> int:
    factors = factor_distinct(q - 1)
    for g in range(2, q):
        if all(pow(g, (q - 1) // p, q) != 1 for p in factors):
            return g
    raise RuntimeError(f"no primitive root found mod {q}")


def exact_order(x: int, modulus: int, order: int) -> bool:
    if pow(x, order, modulus) != 1:
        return False
    return all(pow(x, order // p, modulus) != 1 for p in factor_distinct(order))


def det_mod(matrix: list[list[int]], q: int) -> int:
    a = [row[:] for row in matrix]
    n = len(a)
    det = 1
    for col in range(n):
        pivot = next((row for row in range(col, n) if a[row][col] % q), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[pivot], a[col] = a[col], a[pivot]
            det = -det
        pv = a[col][col] % q
        det = det * pv % q
        inv = pow(pv, -1, q)
        for row in range(col + 1, n):
            if not a[row][col] % q:
                continue
            scale = a[row][col] * inv % q
            for j in range(col, n):
                a[row][j] = (a[row][j] - scale * a[col][j]) % q
    return det % q


def official_schedule() -> list[int]:
    t = 1 << 33
    return [((t // (1 << j)) + 1) // 2 for j in range(34)]


def verify_schedule_and_scope() -> None:
    levels = official_schedule()
    expected = [1 << e for e in range(32, -1, -1)] + [1]
    require(levels == expected, "official level schedule mismatch")
    require(len(levels) == 34, "official level count")
    require(sum(levels) == 1 << 33, "official level sum")
    require(levels.count(1) == 2, "duplicate terminal ell=1")
    require(max(256 * ell for ell in levels) == 1 << 40, "maximum N")
    require(2 * max(256 * ell for ell in levels) == 1 << 41, "maximum root order")

    # Even under the q<2^256 cap, q=1+k*2^41 has this many possible k values.
    k_max = ((1 << 256) - 2) // (1 << 41)
    require(k_max == (1 << 215) - 1, "progression candidate count")

    # An O(q) uint64 DP would already require at least 16 TiB at q>2^41.
    min_array_bytes = 8 * (1 << 41)
    require(min_array_bytes == 1 << 44, "minimum official uint64 array size")

    print(
        "SCOPE_SCHEDULE_PASS",
        f"levels={len(levels)} distinct={len(set(levels))}",
        f"sum_ell=2^33 max_N=2^40",
        f"candidate_k=2^215-1 digits={len(str(k_max))}",
        f"min_O(q)_uint64_bytes=2^44",
    )


def relation_weight(row: tuple[int, ...]) -> int:
    return sum(value != 0 for value in row)


def is_relation(row: tuple[int, ...], values: list[int], q: int) -> bool:
    return sum(c * v for c, v in zip(row, values)) % q == 0


def is_primitive_relation(row: tuple[int, ...], values: list[int], q: int) -> bool:
    support = [i for i, value in enumerate(row) if value]
    if not support or not is_relation(row, values, q):
        return False
    # A proper signed support restriction must retain the signs of row.
    for mask in range(1, (1 << len(support)) - 1):
        restricted = [0] * len(row)
        for j, index in enumerate(support):
            if (mask >> j) & 1:
                restricted[index] = row[index]
        if is_relation(tuple(restricted), values, q):
            return False
    return True


def signed_shift(row: tuple[int, ...], shift: int) -> tuple[int, ...]:
    n = len(row)
    out = [0] * n
    for exponent, coefficient in enumerate(row):
        if not coefficient:
            continue
        target = (exponent + shift) % (2 * n)
        if target >= n:
            out[target - n] -= coefficient
        else:
            out[target] += coefficient
    return tuple(out)


def orbit_key(row: tuple[int, ...]) -> tuple[int, ...]:
    n = len(row)
    candidates = []
    for shift in range(2 * n):
        moved = signed_shift(row, shift)
        candidates.append(moved)
        candidates.append(tuple(-x for x in moved))
    return min(candidates)


def verify_equivalent_forms_toy() -> None:
    # A full-half-section L=1 analogue: q=97, N=8, exact order 16.
    q, n, ell = 97, 8, 1
    g = primitive_root_prime(q)
    omega = pow(g, (q - 1) // (2 * n), q)
    require(exact_order(omega, q, 2 * n), "toy root order")
    values = [pow(omega, i, q) for i in range(n)]

    fibers = [0] * q
    subset_sums = [0] * (1 << n)
    for mask in range(1, 1 << n):
        low = mask & -mask
        index = low.bit_length() - 1
        subset_sums[mask] = (subset_sums[mask ^ low] + values[index]) % q
    for syndrome in subset_sums:
        fibers[syndrome] += 1

    collision_pairs = sum(size * size for size in fibers)
    relation_rows = []
    z = Fraction(0)
    primitives = []
    for row in product((-1, 0, 1), repeat=n):
        if is_relation(row, values, q):
            relation_rows.append(row)
            z += Fraction(1, 1 << relation_weight(row))
            if is_primitive_relation(row, values, q):
                primitives.append(row)

    require(collision_pairs == (1 << n) * z, "fiber/relation collision identity")
    r = Fraction(q, 1 << n)
    e = Fraction(q * collision_pairs, 1 << (2 * n))
    require(e == r * z, "E=rZ")

    mean = Fraction(1 << n, q)
    variance = sum((Fraction(size) - mean) ** 2 for size in fibers)
    require(variance == (1 << n) * (z - 1 / r), "fiber variance identity")
    require(e - 1 == r * variance / (1 << n), "C1 variance normalization")

    primitive_orbits: dict[tuple[int, ...], int] = {}
    for row in primitives:
        key = orbit_key(row)
        primitive_orbits[key] = relation_weight(row)
    w_ext = sum(Fraction(2 * n, 1 << w) for w in primitive_orbits.values() if 2 <= w <= 8)
    require(e - 1 <= 4 * r * (1 + w_ext), "toy C1-r3 check")

    print(
        "EQUIVALENCE_TOY_PASS",
        f"q={q} N={n} fibers={sum(size > 0 for size in fibers)}",
        f"relations={len(relation_rows)} primitive_orbits={len(primitive_orbits)}",
        f"E={e} r={r} W_ext={w_ext}",
        f"variance={variance}",
    )


def verify_block_factorization(ell: int, q: int) -> None:
    n = 256 * ell
    order = 2 * n
    require((q - 1) % order == 0, f"q={q} does not split order {order}")
    g = primitive_root_prime(q)
    omega = pow(g, (q - 1) // order, q)
    require(exact_order(omega, q, order), f"root order ell={ell}")
    theta = pow(omega, 256, q)
    require(exact_order(theta, q, 2 * ell), f"theta order ell={ell}")

    # F_{j,b}=theta^((2j+1)b), j,b=0..ell-1.
    f = [
        [pow(theta, (2 * j + 1) * b, q) for b in range(ell)]
        for j in range(ell)
    ]
    require(det_mod(f, q) != 0, f"base Fourier block singular ell={ell}")

    for a in range(256):
        d = [pow(omega, (2 * j + 1) * a, q) for j in range(ell)]
        block = [
            [pow(omega, (2 * j + 1) * (a + 256 * b), q) for b in range(ell)]
            for j in range(ell)
        ]
        reconstructed = [[d[j] * f[j][b] % q for b in range(ell)] for j in range(ell)]
        require(block == reconstructed, f"block identity ell={ell}, a={a}")
        require(det_mod(block, q) != 0, f"block basis ell={ell}, a={a}")

    print("BLOCK_FACTOR_PASS", f"ell={ell} q={q} blocks=256 rank={ell}")


def verify_slot_decomposition() -> None:
    open_cells = set()
    for ell in sorted(set(official_schedule())):
        for weight in range(ell + 1, ell + 8):
            if weight <= 2 * ell:
                continue  # Newton short-window exclusion.
            if ell == 1 and weight in {3, 4}:
                continue  # exact ambient exclusions.
            if ell == 2 and weight in {5, 6}:
                continue  # banked exact certificates.
            open_cells.add((ell, weight))

    expected = {
        (1, 5), (1, 6), (1, 7), (1, 8),
        (2, 7), (2, 8), (2, 9),
        (4, 9), (4, 10), (4, 11),
    }
    require(open_cells == expected, f"ten-slot decomposition drift: {sorted(open_cells)}")
    require(all(ell < 8 for ell, _ in open_cells), "deep-level residual")
    print("TEN_SLOT_DECOMPOSITION_PASS", sorted(open_cells))


def verify_banked_exact_arithmetic() -> None:
    require(41**34 < 2**202, "baseline assembly inequality")
    require((1 + Fraction(6 * 33, 32)) ** 34 < 2**100, "allowance-six headroom")
    require(not ((1 + Fraction(7 * 33, 32)) ** 34 < 2**100), "allowance-seven fence")

    accident_env = Fraction(46233153981711603, 15410754991685632)
    accident_w = Fraction(5, 4)
    accident_k = accident_env / (1 + accident_w)
    require(
        accident_k == Fraction(5137017109079067, 3852688747921408),
        "accident-row repricing fraction",
    )
    require(accident_env > 3 and accident_k < 2, "accident-row qualitative read")

    worst_k = Fraction(35507502101438673, 25332747971067904)
    require(1 < worst_k < 2 < 4, "round-two worst ratio ordering")

    print(
        "BANKED_ARITHMETIC_PASS",
        f"assembly_slack_numerator={2**202-41**34}",
        f"accident_env={accident_env} accident_K={accident_k}",
        f"round2_worst_K={worst_k}",
    )


def main() -> None:
    verify_schedule_and_scope()
    verify_equivalent_forms_toy()
    verify_block_factorization(1, 7681)   # 512 | q-1
    verify_block_factorization(2, 12289) # 1024 | q-1
    verify_block_factorization(4, 12289) # 2048 | q-1
    verify_slot_decomposition()
    verify_banked_exact_arithmetic()
    print("BRIEF1_C1R3_PROGRAM_ARITHMETIC_PASS")


if __name__ == "__main__":
    main()
