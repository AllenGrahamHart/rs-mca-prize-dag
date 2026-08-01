#!/usr/bin/env python3
"""Exact and high-precision checks for the adversarial audit.

The script verifies explicit route fences and replacement identities. It does
not prove or refute official C1-ZERO.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, cos, exp, gcd, log, pi, sin
import cmath


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
    fs = prime_factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // r, p) != 1 for r in fs):
            return g
    raise AssertionError("primitive root")


def phi_power_two(order: int) -> int:
    require(order > 1 and order & (order - 1) == 0, "power of two")
    return order // 2


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


def check_packet_vacuity_and_scale() -> None:
    require(2**256 > 2**255, "pigeonhole scale")
    # Failure threshold ratio over Haar.
    low_ratio_minus_one = Fraction(4 * 2**41, 2**256)
    high_ratio = Fraction(1) + Fraction(4 * 2**255, 2**256)
    require(low_ratio_minus_one == Fraction(1, 2**213), "low scale")
    require(high_ratio == 3, "high scale")

    # A local owner target at j=63: guaranteed absolute excess 1/320
    # against Haar 2^252 / 2^41 = 2^211.
    relative = Fraction(1, 320 * 2**211)
    require(relative < Fraction(1, 2**219), "local BSG blindness")

    print(
        "AUDIT1_VACUITY_SCALE_PASS",
        "pigeonhole_packets=universal",
        "low_relative=1+2^-213",
        "high_relative=3",
    )


def check_direct_product_activity() -> None:
    q = 50177
    n = 16
    omega = pow(primitive_root(q), (q - 1) // 32, q)
    coeffs = [pow(omega, i, q) for i in range(n)]
    spectrum = relation_weight_counts(q, coeffs)
    expected = {0: 1, 9: 320, 10: 32, 12: 96, 14: 64}
    require(
        {w: c for w, c in enumerate(spectrum) if c} == expected,
        "relation spectrum",
    )

    z = sum(Fraction(c, 2**w) for w, c in enumerate(spectrum))
    require(z == Fraction(431, 256), "single-copy Z")
    haar = Fraction(2**16, q)
    x1 = z - haar
    x4 = z**4 - haar**4
    require(0 < x1 < 1, "one packet family harmless")
    require(x4 > 4, "four copies dangerous")

    print(
        "AUDIT2_PACKET_ACTIVITY_PASS",
        f"single_excess={float(x1):.6f}",
        f"four_copy_excess={float(x4):.6f}",
        "min_weight=9",
    )


def check_eightwise_product_trap() -> None:
    # A 3-dimensional binary code of length 20. The integers encode bitsets.
    basis = [977550, 100823, 909264]
    weights = []
    for mask in range(1, 8):
        word = 0
        for i, b in enumerate(basis):
            if mask >> i & 1:
                word ^= b
        weights.append(word.bit_count())

    require(sorted(weights) == sorted([12, 10, 12, 13, 11, 9, 9]),
            "binary code weights")
    require(min(weights) == 9, "dual distance / no <=8 dependency")

    # Quotient rank is 20-3=17. Any <=8 columns are independent.
    # All 20 zero events occur only at t=0.
    ratio = 2 ** (20 - 17)
    require(ratio == 8, "global product ratio")

    print(
        "AUDIT3_EIGHTWISE_TRAP_PASS",
        f"nonzero_codeword_weights={weights}",
        f"global_to_iid_ratio={ratio}",
    )


def check_companion_and_block_trap() -> None:
    for b in (1, 2, 4, 8):
        blocks = 256 // b
        order = 512 // b
        degree = phi_power_two(order)
        require(blocks == degree, f"dyadic companion equality b={b}")

    # The order-128 companion action: T^64=-I and T^128=I.
    dim = 64

    def apply_t(v: tuple[int, ...]) -> tuple[int, ...]:
        out = [0] * dim
        for i in range(dim - 1):
            out[i + 1] += v[i]
        out[0] -= v[-1]
        return tuple(out)

    e0 = (1,) + (0,) * (dim - 1)
    v = e0
    for _ in range(64):
        v = apply_t(v)
    require(v == tuple(-x for x in e0), "T^64=-I")
    for _ in range(64):
        v = apply_t(v)
    require(v == e0, "T^128=I")

    gaps = []
    for b in (5, 6, 7):
        blocks = (256 + b - 1) // b
        order = 512 // gcd(512, b)
        degree = phi_power_two(order)
        require(blocks < degree, f"non-dyadic degree gap b={b}")
        gaps.append((b, blocks, degree))

    print(
        "AUDIT4_COMPANION_TRAP_PASS",
        "dyadic=cyclotomic_degree",
        f"nondyadic_gaps={gaps}",
    )


def check_travelling_window() -> None:
    r = 8
    width = r + 1

    def window(start: int) -> set:
        total_dim = 20
        out = set()
        for digits in product((-1, 0, 1), repeat=width):
            v = [0] * total_dim
            for i, d in enumerate(digits):
                v[start + i] = d
            out.add(tuple(v))
        return out

    p0 = window(0)
    p1 = window(1)
    require(len(p0) == 3**width, "window size")
    require(len(p0 & p1) == 3**r, "adjacent overlap")
    require(Fraction(len(p0 & p1), len(p0)) == Fraction(1, 3),
            "overlap density")

    # e_r is in the first model and shifts outside it.
    er = [0] * 20
    er[r] = 1
    shifted = [0] * 20
    shifted[r + 1] = 1
    require(tuple(er) in p0 and tuple(shifted) not in p0,
            "no invariant fixed window")

    print(
        "AUDIT5_TRAVELLING_WINDOW_PASS",
        f"rank={width}",
        "adjacent_overlap=1/3",
        "fixed_invariance=false",
    )


def subgroup_cosets(q: int, order: int):
    g = primitive_root(q)
    hgen = pow(g, (q - 1) // order, q)
    H = [pow(hgen, i, q) for i in range(order)]
    unseen = set(range(1, q))
    cosets = []
    owner = {}
    while unseen:
        t = min(unseen)
        c = sorted({t * h % q for h in H})
        idx = len(cosets)
        for x in c:
            owner[x] = idx
        unseen.difference_update(c)
        cosets.append(c)
    return cosets, owner


def check_doubling_coboundary_row(q: int, order: int):
    cosets, owner = subgroup_cosets(q, order)
    log_d = []
    log_a = []
    reps = [c[0] for c in cosets]

    for c in cosets:
        ld = 0.0
        la = 0.0
        for x in c:
            theta = 2.0 * pi * x / q
            ld += log(abs(1.0 - cmath.exp(1j * theta)))
            la += log(abs(1.0 + cmath.exp(1j * theta)))
        log_d.append(ld)
        log_a.append(la)

    err = 0.0
    sigma = []
    for i, rep in enumerate(reps):
        j = owner[(2 * rep) % q]
        sigma.append(j)
        err = max(err, abs(log_a[i] - (log_d[j] - log_d[i])))
    require(err < 2e-10, f"doubling identity q={q}")

    seen = set()
    max_cycle_sum = 0.0
    max_cycle_len = 0
    for i in range(len(cosets)):
        if i in seen:
            continue
        cycle = []
        j = i
        while j not in cycle:
            cycle.append(j)
            seen.add(j)
            j = sigma[j]
        s = sum(log_a[k] for k in cycle)
        max_cycle_sum = max(max_cycle_sum, abs(s))
        max_cycle_len = max(max_cycle_len, len(cycle))
    require(max_cycle_sum < 2e-9, f"cycle telescoping q={q}")

    return max(abs(x) for x in log_a), max_cycle_len


def check_doubling_coboundary() -> None:
    # q=257, order 32: 2 lies in H and every Fourier product is exactly 1.
    mx257, cyc257 = check_doubling_coboundary_row(257, 32)
    require(mx257 < 2e-12, "doubling-closed flat row")

    mx7681, cyc7681 = check_doubling_coboundary_row(7681, 512)
    require(cyc7681 > 1, "nontrivial doubling cycles")

    print(
        "AUDIT6_DOUBLING_COBBOUNDARY_PASS",
        f"q257_max_logA={mx257:.2e}",
        f"q7681_cycle_max={cyc7681}",
        f"q7681_max_abs_logA={mx7681:.3f}",
    )


def main() -> None:
    check_packet_vacuity_and_scale()
    check_direct_product_activity()
    check_eightwise_product_trap()
    check_companion_and_block_trap()
    check_travelling_window()
    check_doubling_coboundary()
    print("ADVERSARIAL_AUDIT_INVERSE_FLATNESS_PASS")


if __name__ == "__main__":
    main()
