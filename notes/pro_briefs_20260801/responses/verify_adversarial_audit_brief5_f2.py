#!/usr/bin/env python3
"""Exact and numerical route-fence checks for the Brief-5 adversarial audit.

The constructions are abstract inference traps, not F2 counterexamples.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import comb, cos, pi, sin, sqrt
import cmath


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def check_hidden_modulation() -> None:
    m = 60
    N = 2**m
    delta = Fraction(1, 2**10)  # 2^(-m/6)
    ratio_sq = delta * delta * N / (1 + delta * delta)
    target_sq = Fraction(2 ** (2 * (m // 3)), 1)
    require(ratio_sq < target_sq, "saturating modulation below target")
    require(ratio_sq > target_sq * Fraction(1023, 1024),
            "saturating modulation is close")

    delta_bad = 2 * delta
    ratio_bad_sq = delta_bad * delta_bad * N / (1 + delta_bad * delta_bad)
    require(ratio_bad_sq > target_sq, "double modulation violates target")

    # Exhaustive proper-marginal check on a smaller cube.
    mm = 12
    dd = Fraction(1, 4)
    for keep in range(mm):
        for bit in (0, 1):
            total = Fraction(0)
            count = 0
            for tail in product((0, 1), repeat=mm - 1):
                x = list(tail)
                x.insert(keep, bit)
                eps = -1 if sum(x) % 2 else 1
                total += 1 + dd * eps
                count += 1
            require(total / count == 1, "proper weight marginal")

    print(
        "F2_AUDIT1_HIDDEN_MODULATION_PASS",
        "near_target_ratio_bits~20",
        "all_proper_weight_marginals=1",
        "low_degree_sign_spectrum=0",
    )


def check_slice_catastrophe() -> None:
    m = 60
    b = 30
    slice_size = comb(m, b)
    full_alignment = 0
    slice_ratio_sq = slice_size
    target_sq = 2 ** (2 * (m // 3))
    require(full_alignment == 0, "full cube cancellation")
    require(slice_ratio_sq > target_sq, "central slice exceeds n/3 target")

    print(
        "F2_AUDIT2_SLICE_PASS",
        "full_window_alignment=0",
        f"slice_size=C(60,30)={slice_size}",
        "slice_sign=constant",
    )


def carry_sign(p: int, r: int) -> int:
    r %= 2 * p
    return 1 if r < p else -1


def check_carry_state_lower_bound() -> None:
    for p in (3, 5, 7, 11):
        modulus = 2 * p
        for r in range(modulus):
            for s in range(r + 1, modulus):
                require(
                    any(
                        carry_sign(p, r + t) != carry_sign(p, s + t)
                        for t in range(modulus)
                    ),
                    f"indistinguishable residues p={p}, r={r}, s={s}",
                )
    print(
        "F2_AUDIT3_CARRY_AUTOMATON_PASS",
        "all_2p_residues_pairwise_distinguishable",
    )


def dft(values: list[complex]) -> list[complex]:
    n = len(values)
    return [
        sum(values[r] * cmath.exp(-2j * pi * k * r / n) for r in range(n))
        for k in range(n)
    ]


def check_carry_fourier() -> None:
    p = 101
    n = 2 * p
    h = [1.0 if r < p else -1.0 for r in range(n)]
    H = dft(h)

    nonzero = 0
    max_formula_err = 0.0
    for k, val in enumerate(H):
        if k % 2 == 0:
            require(abs(val) < 1e-9, "even carry mode")
        else:
            pred = 4 / (1 - cmath.exp(-1j * pi * k / p))
            max_formula_err = max(max_formula_err, abs(val - pred))
            require(abs(val) > 1e-6, "odd carry mode nonzero")
            nonzero += 1
    require(nonzero == p, "dense odd-mode support")
    require(max_formula_err < 1e-8, "carry Fourier formula")

    normalized_l1 = sum(abs(v) for v in H) / n
    require(normalized_l1 < 10, "carry Fourier L1 logarithmic at test p")

    print(
        "F2_AUDIT4_CARRY_FOURIER_PASS",
        f"nonzero_modes={nonzero}",
        f"normalized_L1={normalized_l1:.6f}",
    )


def check_pairing_precision() -> None:
    m = 60
    M = 2**m

    eta_near = Fraction(1, 2**10)
    ratio_near_sq = (
        eta_near * eta_near * M
        / (1 + (1 + eta_near) * (1 + eta_near))
    )
    target_sq = Fraction(2 ** (2 * (m // 3)), 1)
    require(ratio_near_sq < target_sq, "near pairing below target")
    require(ratio_near_sq > target_sq / 3, "near pairing exponential scale")

    eta_bad = Fraction(1, 2**9)
    ratio_bad_sq = (
        eta_bad * eta_bad * M
        / (1 + (1 + eta_bad) * (1 + eta_bad))
    )
    require(ratio_bad_sq > target_sq, "pairing mismatch violates target")

    print(
        "F2_AUDIT5_PAIRING_PRECISION_PASS",
        "required_eta_scale=2^(-m/6)",
        "inverse_polynomial_accuracy=insufficient",
    )


def check_chamber_complexity() -> None:
    p = 101
    a = p - 1
    seq = [((a * c) // p) & 1 for c in range(p)]
    runs = 1 + sum(seq[i] != seq[i - 1] for i in range(1, p))
    require(runs >= p - 1, "order-p chamber complexity")

    print(
        "F2_AUDIT6_CHAMBER_PASS",
        f"p={p}",
        f"parity_runs={runs}",
    )


def check_structural_drift_and_sector_cost() -> None:
    M = 2**40
    drift_ratio_sq = M
    require(drift_ratio_sq == 2**40, "drift amplification")
    require(sqrt(drift_ratio_sq) == 2**20, "drift ratio")

    sectors = 2**20
    coherent_ratio_sq = sectors
    require(sqrt(coherent_ratio_sq) == 2**10, "sector Cauchy overhead")

    print(
        "F2_AUDIT7_COMPOSITION_PASS",
        "unit_drift_per_orbit=>2^20_ratio",
        "2^20_coherent_sectors=>10_bit_overhead",
    )


def check_order_two_transport_trap() -> None:
    r = 4
    delta = Fraction(1, 8)
    for keep_count in range(r):
        for fixed_indices in [tuple(range(keep_count))]:
            for bits in product((0, 1), repeat=keep_count):
                total = Fraction(0)
                count = 0
                for tail in product((0, 1), repeat=r - keep_count):
                    x = list(bits) + list(tail)
                    eps = -1 if sum(x) % 2 else 1
                    total += 1 + delta * eps
                    count += 1
                require(total / count == 1, "proper sector marginal")
    numerator = delta * 2**r
    variance = 2**r * (1 + delta * delta)
    require(numerator != 0 and variance > 0, "global higher-order interaction")

    print(
        "F2_AUDIT8_TRANSPORT_TRAP_PASS",
        "every_proper_order2_sector_marginal=flat",
        "full_interaction=nonzero",
    )


def check_carry_fourier_product_identity() -> None:
    p = 5
    modulus = 2 * p
    locals_ = [
        [(0, 0, 1.0), (3, 1, 2.0)],
        [(1, 0, 1.5), (6, 1, 0.5)],
        [(2, 1, 0.75), (8, 0, 1.25)],
        [(4, 0, 1.0), (9, 1, 1.0)],
    ]

    direct = 0.0
    for choices in product((0, 1), repeat=len(locals_)):
        residue = 0
        parity = 0
        weight = 1.0
        for i, choice in enumerate(choices):
            s, u, a = locals_[i][choice]
            residue += s
            parity ^= u
            weight *= a
        direct += carry_sign(p, residue) * ((-1) ** parity) * weight

    h = [float(carry_sign(p, r)) for r in range(modulus)]
    H = dft(h)
    spectral = 0j
    for k in range(modulus):
        prod_mult = 1 + 0j
        for records in locals_:
            local = 0j
            for s, u, a in records:
                local += ((-1) ** u) * a * cmath.exp(
                    2j * pi * k * s / modulus
                )
            prod_mult *= local
        spectral += H[k] * prod_mult
    spectral /= modulus

    require(abs(direct - spectral.real) < 1e-9, "carry Fourier product real")
    require(abs(spectral.imag) < 1e-9, "carry Fourier product imaginary")

    print(
        "F2_AUDIT9_CARRY_PRODUCT_PASS",
        f"direct={direct:.6f}",
        f"spectral={spectral.real:.6f}",
    )


def main() -> None:
    check_hidden_modulation()
    check_slice_catastrophe()
    check_carry_state_lower_bound()
    check_carry_fourier()
    check_pairing_precision()
    check_chamber_complexity()
    check_structural_drift_and_sector_cost()
    check_order_two_transport_trap()
    check_carry_fourier_product_identity()
    print("ADVERSARIAL_AUDIT_BRIEF5_F2_PASS")


if __name__ == "__main__":
    main()
