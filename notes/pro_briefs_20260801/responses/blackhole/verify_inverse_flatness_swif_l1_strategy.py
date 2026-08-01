#!/usr/bin/env python3
"""Exact planning checks for the inverse-flatness / SWIF-L1 strategy.

This script verifies:
  * the exact L=1 variance / collision / ternary relation identities;
  * the full order-512 subgroup zero-subset identity;
  * the four-coordinate first-owner decomposition;
  * exact N=16 analogue rows with and without <=8 relations;
  * a weight-9 cyclotomic resultant example;
  * a synthetic minimum-weight-9 system showing ideal local contraction is false.

It does NOT prove C1-ZERO, SWIF-4, CERP-512, a relative inverse
Littlewood-Offord theorem, lambda-rigidity, Booleanisation, or the official
2-adic packet sieve.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import gcd


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def prime_factors(n: int) -> list[int]:
    out: list[int] = []
    d = 2
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
    factors = prime_factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // r, p) != 1 for r in factors):
            return g
    raise AssertionError("no primitive root found")


def v2(n: int) -> int:
    c = 0
    while n % 2 == 0:
        c += 1
        n //= 2
    return c


def subset_counts_mod(q: int, coeffs: list[int],
                      checkpoints: set[int] | None = None
                      ) -> tuple[list[int], dict[int, list[int]]]:
    counts = [0] * q
    counts[0] = 1
    saved: dict[int, list[int]] = {}
    for idx, a in enumerate(coeffs, 1):
        new = counts.copy()
        for s, c in enumerate(counts):
            if c:
                new[(s + a) % q] += c
        counts = new
        if checkpoints and idx in checkpoints:
            saved[idx] = counts.copy()
    return counts, saved


def min_signed_relation(q: int, coeffs: list[int]) -> tuple[int, tuple[int, ...]]:
    n = len(coeffs)
    h = n // 2
    left: dict[int, tuple[int, tuple[int, ...]]] = {}
    for ds in product((-1, 0, 1), repeat=h):
        s = sum(d * a for d, a in zip(ds, coeffs[:h])) % q
        w = sum(d != 0 for d in ds)
        old = left.get(s)
        if old is None or w < old[0]:
            left[s] = (w, ds)

    best: tuple[int, tuple[int, ...]] | None = None
    for ds in product((-1, 0, 1), repeat=n - h):
        s = sum(d * a for d, a in zip(ds, coeffs[h:])) % q
        hit = left.get((-s) % q)
        if hit is None:
            continue
        w = hit[0] + sum(d != 0 for d in ds)
        if w and (best is None or w < best[0]):
            best = (w, hit[1] + ds)

    if best is None:
        raise AssertionError("no signed relation found")
    return best


def relation_weight_counts(q: int, coeffs: list[int]) -> list[int]:
    n = len(coeffs)
    h = n // 2
    left: dict[int, list[int]] = defaultdict(lambda: [0] * (h + 1))
    right: dict[int, list[int]] = defaultdict(lambda: [0] * (n - h + 1))

    for ds in product((-1, 0, 1), repeat=h):
        s = sum(d * a for d, a in zip(ds, coeffs[:h])) % q
        left[s][sum(d != 0 for d in ds)] += 1

    for ds in product((-1, 0, 1), repeat=n - h):
        s = sum(d * a for d, a in zip(ds, coeffs[h:])) % q
        right[s][sum(d != 0 for d in ds)] += 1

    counts = [0] * (n + 1)
    for s, ls in left.items():
        rs = right.get((-s) % q)
        if rs is None:
            continue
        for i, a in enumerate(ls):
            if not a:
                continue
            for j, b in enumerate(rs):
                if b:
                    counts[i + j] += a * b
    return counts


def trim(poly: list[int]) -> list[int]:
    p = poly[:]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def bareiss_det(matrix: list[list[int]]) -> int:
    a = [row[:] for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    previous = 1

    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1

        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (
                    a[i][j] * pivot - a[i][k] * a[k][j]
                ) // previous
        previous = pivot
        for i in range(k + 1, n):
            a[i][k] = 0

    return sign * a[-1][-1]


def resultant(f: list[int], g: list[int]) -> int:
    f = trim(f)
    g = trim(g)
    m = len(f) - 1
    n = len(g) - 1
    fd = f[::-1]
    gd = g[::-1]
    size = m + n
    sylvester: list[list[int]] = []

    for i in range(n):
        sylvester.append([0] * i + fd + [0] * (n - 1 - i))
    for i in range(m):
        sylvester.append([0] * i + gd + [0] * (m - 1 - i))

    require(all(len(row) == size for row in sylvester),
            "Sylvester sizing error")
    return bareiss_det(sylvester)


def subset_counts_integer(coeffs: list[int]) -> dict[int, int]:
    counts = {0: 1}
    for a in coeffs:
        new = counts.copy()
        for s, c in counts.items():
            new[s + a] = new.get(s + a, 0) + c
        counts = new
    return counts


def min_signed_weight_integer(coeffs: list[int]) -> int:
    n = len(coeffs)
    h = n // 2
    left: dict[int, int] = {}

    for ds in product((-1, 0, 1), repeat=h):
        s = sum(d * a for d, a in zip(ds, coeffs[:h]))
        w = sum(d != 0 for d in ds)
        if s not in left or w < left[s]:
            left[s] = w

    best = n + 1
    for ds in product((-1, 0, 1), repeat=n - h):
        s = sum(d * a for d, a in zip(ds, coeffs[h:]))
        w = sum(d != 0 for d in ds)
        lw = left.get(-s)
        if lw is not None and 0 < lw + w < best:
            best = lw + w

    require(best <= n, "integer gadget has no relation")
    return best


def check_official_shape_identity() -> None:
    q = 7681
    n = 256
    g = primitive_root(q)
    omega = pow(g, (q - 1) // 512, q)
    require(pow(omega, 512, q) == 1, "omega^512")
    require(pow(omega, 256, q) == q - 1, "omega^256=-1")

    coeffs = [pow(omega, i, q) for i in range(n)]
    checkpoints = set(range(4, n + 1, 4))
    counts, saved = subset_counts_mod(q, coeffs, checkpoints)
    require(sum(counts) == 2**n, "Boolean mass")

    collision_numerator = sum(c * c for c in counts)
    cp = Fraction(collision_numerator, 2 ** (2 * n))
    excess_l2 = cp - Fraction(1, q)
    variance = sum(
        (Fraction(c) - Fraction(2**n, q)) ** 2
        for c in counts
    )
    z = Fraction(collision_numerator, 2**n)

    require(variance == 2 ** (2 * n) * excess_l2,
            "variance / collision identity")
    require(variance == 2**n * (z - Fraction(2**n, q)),
            "variance / relation identity")

    # Full order-512 subset-zero count equals the Boolean collision numerator.
    full_h = [pow(omega, i, q) for i in range(512)]
    full_counts, _ = subset_counts_mod(q, full_h)
    require(full_counts[0] == collision_numerator,
            "full subgroup zero-subset identity")

    # Four-coordinate owner decomposition.
    z_values = [Fraction(1)]
    for j in range(1, 65):
        cts = saved[4 * j]
        cp_j = Fraction(sum(c * c for c in cts), 2 ** (8 * j))
        z_values.append(2 ** (4 * j) * cp_j)

    owner_sum = Fraction(0)
    for j in range(64):
        actual_increment = z_values[j + 1] - z_values[j]
        haar_increment = Fraction(15 * 2 ** (4 * j), q)
        owner_sum += actual_increment - haar_increment

    terminal = z_values[-1] - Fraction(2**256, q)
    require(
        terminal == Fraction(1) - Fraction(1, q) + owner_sum,
        "block-owner telescoping identity",
    )

    print(
        "CHECK1_L1_IDENTITIES_PASS",
        f"q={q}",
        f"zero_subset_bits={full_counts[0].bit_length()}",
        f"owner_terms=64",
    )


def check_analogue_rows_and_resultants() -> None:
    # A no-<=8-relation analogue row.
    q = 50177
    n = 16
    omega = pow(primitive_root(q), (q - 1) // 32, q)
    coeffs = [pow(omega, i, q) for i in range(n)]
    weight, relation = min_signed_relation(q, coeffs)
    require(weight == 9, "q=50177 minimum relation should be 9")

    spectrum = relation_weight_counts(q, coeffs)
    expected = {0: 1, 9: 320, 10: 32, 12: 96, 14: 64}
    require(
        {w: c for w, c in enumerate(spectrum) if c} == expected,
        "q=50177 exact relation spectrum",
    )

    counts, checkpoints = subset_counts_mod(
        q, coeffs, checkpoints={4, 8, 12, 16}
    )
    collision_numerator = sum(c * c for c in counts)
    z = Fraction(collision_numerator, 2**n)
    terminal = z - Fraction(2**n, q)
    require(0 < terminal < 1, "q=50177 analogue excess range")

    # Every four-block scaled centred-L2 ratio is <=1 on this row.
    e = [Fraction(1) - Fraction(1, q)]
    for depth in (4, 8, 12, 16):
        cts = checkpoints[depth]
        cp = Fraction(sum(c * c for c in cts), 2 ** (2 * depth))
        e.append(cp - Fraction(1, q))
    ratios = [Fraction(16) * e[j + 1] / e[j] for j in range(4)]
    require(all(r <= 1 for r in ratios),
            "q=50177 four-block contraction profile")

    phi_32 = [1] + [0] * 15 + [1]  # X^16+1
    res = resultant(list(relation), phi_32)
    require(abs(res) == q, "q=50177 weight-9 resultant")
    require(v2(q - 1) == 10, "q=50177 v2")

    # A contrasting short-relation analogue row.
    q2 = 353
    omega2 = pow(primitive_root(q2), (q2 - 1) // 32, q2)
    coeffs2 = [pow(omega2, i, q2) for i in range(n)]
    weight2, relation2 = min_signed_relation(q2, coeffs2)
    require(weight2 == 3, "q=353 minimum relation should be 3")
    res2 = resultant(list(relation2), phi_32)
    require(abs(res2) == q2, "q=353 weight-3 resultant")

    _, checkpoints2 = subset_counts_mod(
        q2, coeffs2, checkpoints={4, 8, 12, 16}
    )
    e2 = [Fraction(1) - Fraction(1, q2)]
    for depth in (4, 8, 12, 16):
        cts = checkpoints2[depth]
        cp = Fraction(sum(c * c for c in cts), 2 ** (2 * depth))
        e2.append(cp - Fraction(1, q2))
    ratios2 = [Fraction(16) * e2[j + 1] / e2[j] for j in range(4)]
    require(any(r > 2 for r in ratios2),
            "q=353 should exhibit a strong local spike")

    print(
        "CHECK2_ANALOGUE_RESONANCE_PASS",
        f"q50177_minwt={weight}",
        f"q50177_v2={v2(q-1)}",
        f"q353_minwt={weight2}",
    )


def check_weight9_local_contraction_fence() -> None:
    previous = [3**i for i in range(8)]
    ninth = sum(previous)
    big = 10 * ninth
    current = [ninth, big, big**2, big**3]
    coeffs = previous + current

    require(min_signed_weight_integer(coeffs) == 9,
            "synthetic gadget minimum relation")

    prev_counts = subset_counts_integer(previous)
    cur_counts = subset_counts_integer(current)
    full_counts = subset_counts_integer(coeffs)

    cp_prev = Fraction(sum(c * c for c in prev_counts.values()), 2**16)
    cp_cur = Fraction(sum(c * c for c in cur_counts.values()), 2**8)
    cp_full = Fraction(sum(c * c for c in full_counts.values()), 2**24)

    require(cp_prev == Fraction(1, 256), "previous injective")
    require(cp_cur == Fraction(1, 16), "current block injective")

    scaled_ratio = Fraction(16) * cp_full / cp_prev
    require(scaled_ratio == Fraction(257, 256),
            "weight-9 local contraction ratio")
    require(scaled_ratio > 1,
            "ideal local contraction must fail")

    print(
        "CHECK3_WEIGHT9_LOCAL_FENCE_PASS",
        f"scaled_ratio={scaled_ratio.numerator}/{scaled_ratio.denominator}",
    )


def main() -> None:
    check_official_shape_identity()
    check_analogue_rows_and_resultants()
    check_weight9_local_contraction_fence()
    print("INVERSE_FLATNESS_SWIF_L1_STRATEGY_CHECK_PASS")


if __name__ == "__main__":
    main()
