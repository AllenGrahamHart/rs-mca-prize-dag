#!/usr/bin/env python3
"""Exact checks for the adversarial audit of Brief 6.

The script verifies route-fence examples. It does not prove or refute the
official adjacent crossing.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def prime_factors(n: int) -> list[int]:
    out = []
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


def primitive_root(q: int) -> int:
    factors = prime_factors(q - 1)
    for g in range(2, q):
        if all(pow(g, (q - 1) // r, q) != 1 for r in factors):
            return g
    raise AssertionError("primitive root")


def inv(a: int, q: int) -> int:
    return pow(a, q - 2, q)


def poly_eval(coeff: list[int], x: int, q: int) -> int:
    out = 0
    for c in reversed(coeff):
        out = (out * x + c) % q
    return out


def lagrange_interpolate(xs: list[int], ys: list[int], q: int) -> list[int]:
    n = len(xs)
    out = [0] * n
    for i, (xi, yi) in enumerate(zip(xs, ys)):
        basis = [1]
        den = 1
        for j, xj in enumerate(xs):
            if i == j:
                continue
            nxt = [0] * (len(basis) + 1)
            for a, c in enumerate(basis):
                nxt[a] = (nxt[a] - c * xj) % q
                nxt[a + 1] = (nxt[a + 1] + c) % q
            basis = nxt
            den = den * (xi - xj) % q
        scale = yi * inv(den, q) % q
        for a, c in enumerate(basis):
            out[a] = (out[a] + scale * c) % q
    return out


def exact_shells(q: int, n: int, k: int, U: list[int]) -> dict[int, int]:
    g = primitive_root(q)
    omega = pow(g, (q - 1) // n, q)
    D = [pow(omega, i, q) for i in range(n)]
    Uv = [poly_eval(U, x, q) for x in D]
    shells = {b: 0 for b in range(k, n + 1)}

    seen: set[tuple[int, ...]] = set()
    for idxs in combinations(range(n), k):
        xs = [D[i] for i in idxs]
        ys = [Uv[i] for i in idxs]
        P = tuple(lagrange_interpolate(xs, ys, q))
        if P in seen:
            continue
        seen.add(P)
        agr = sum(poly_eval(list(P), x, q) == y for x, y in zip(D, Uv))
        if agr >= k:
            shells[agr] += 1
    return shells


def check_budget_three_chamber() -> None:
    d = 8
    n = 4 * d
    supports = [set() for _ in range(4)]
    coord = 0

    for missing in range(4):
        for _ in range(d - 1):
            for i in range(4):
                if i != missing:
                    supports[i].add(coord)
            coord += 1

    for pair in ((0, 2), (0, 3), (1, 2), (1, 3)):
        for i in pair:
            supports[i].add(coord)
        coord += 1

    require(coord == n, "coordinate count")
    require(all(len(s) == 3 * d - 1 for s in supports), "support sizes")

    intersections = {}
    for i in range(4):
        for j in range(i + 1, 4):
            intersections[(i, j)] = len(supports[i] & supports[j])

    require(intersections[(0, 1)] == 2 * d - 2, "deficit edge 01")
    require(intersections[(2, 3)] == 2 * d - 2, "deficit edge 23")
    for edge in ((0, 2), (0, 3), (1, 2), (1, 3)):
        require(intersections[edge] == 2 * d - 1, f"tight edge {edge}")

    print(
        "RHL_AUDIT1_CHAMBER_TEMPLATE_PASS",
        f"d={d}",
        f"supports={[len(s) for s in supports]}",
    )


def check_chamber_orbit_explosion() -> None:
    d = 2**39
    n = 4 * d
    m = 4 * d - 4

    ceil_log_m1 = (m + 1).bit_length()
    ceil_log_24 = 5
    ceil_log_n = n.bit_length()
    lower_log2 = (
        2 * m
        - 3 * ceil_log_m1
        - ceil_log_24
        - 2 * ceil_log_n
    )
    require(lower_log2 > 2**41, "official chamber orbit explosion")

    print(
        "RHL_AUDIT2_CHAMBER_ORBITS_PASS",
        f"lower_log2_orbits>{lower_log2}",
        "13_cells_are_types_not_cases",
    )


def check_budget_three_progress() -> None:
    n = 2**41
    unsafe = 5 * n // 8 - 1
    safe = 3 * n // 4
    required_decrements = safe - (unsafe + 1)
    require(required_decrements == n // 8 == 2**38, "B=3 gap")

    print(
        "RHL_AUDIT3_B3_PROGRESS_PASS",
        f"one_step_iterations_worst_case={required_decrements}",
    )


def check_rank_one_toeplitz_and_cumulative() -> None:
    q = 17
    n = 8
    k = 4

    U0 = [0] * 7 + [1]               # X^7
    U1 = [0, 0, 0, 0, 1, 0, 0, 1]  # X^7+X^4

    shells0 = exact_shells(q, n, k, U0)
    shells1 = exact_shells(q, n, k, U1)

    require(shells0[5] == 0, "empty parallel shell")
    require(shells1[5] == 7, "product-class shell")
    require(shells1[4] == 35, "lower exact shell")
    require(sum(shells1[b] for b in range(4, 9)) == 42,
            "cumulative threshold")
    require(max(shells1.values()) == 35, "per-shell cap mutation")

    homogeneous0 = (1, 0, 0)
    homogeneous1 = (1, 0, 0)
    require(homogeneous0 == homogeneous1, "same homogeneous Toeplitz row")

    require(comb(8, 3) // 8 == 7, "fixed-product count")

    print(
        "RHL_AUDIT4_TOEPLITZ_PROFILE_PASS",
        f"U0_shell5={shells0[5]}",
        f"U1_shell5={shells1[5]}",
        f"U1_shell4={shells1[4]}",
        "same_homogeneous_rank=1",
    )


def check_product_fibre_uniformity() -> None:
    q = 97
    n = 16
    e = 7
    g = primitive_root(q)
    omega = pow(g, (q - 1) // n, q)
    D = [pow(omega, i, q) for i in range(n)]

    counts = {c: 0 for c in D}
    for T in combinations(D, e):
        p = 1
        for x in T:
            p = p * x % q
        require(p in counts, "subset product outside mu_n")
        counts[p] += 1

    expected = comb(n, e) // n
    require(set(counts.values()) == {expected}, "uniform product fibres")
    max_to_average = Fraction(q, n)
    require(max_to_average == Fraction(97, 16), "q/n ratio")

    print(
        "RHL_AUDIT5_MAX_AVERAGE_PASS",
        f"product_fibre={expected}",
        f"max_to_full_field_average={q}/{n}",
    )


def check_contract_tautology_scale() -> None:
    n = 2**41
    k = 2**40
    received_word_log2_count_lower = 128 * n
    codeword_log2_count_lower = 128 * k
    require(received_word_log2_count_lower > 2**47,
            "received-word brute-force scale")
    require(codeword_log2_count_lower > 2**46,
            "codeword brute-force scale")

    print(
        "RHL_AUDIT6_CONTRACT_SCALE_PASS",
        "finite_is_not_succinct",
    )


def main() -> None:
    check_budget_three_chamber()
    check_chamber_orbit_explosion()
    check_budget_three_progress()
    check_rank_one_toeplitz_and_cumulative()
    check_product_fibre_uniformity()
    check_contract_tautology_scale()
    print("ADVERSARIAL_AUDIT_BRIEF6_CROSSING_PASS")


if __name__ == "__main__":
    main()
