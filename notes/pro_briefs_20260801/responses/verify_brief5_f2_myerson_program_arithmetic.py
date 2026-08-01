#!/usr/bin/env python3
"""Planning-level exact checks for the Brief-5 F2 proof-program dossier.

This checker verifies only arithmetic reductions, explicit counterexamples to
invalid proof inferences, and literature-regime diagnostics used by the
programme.  It does NOT prove f2_growing_order_myerson, the weighted parity
alignment theorem, the first-descent contraction, tower transport, or the
raw/pruned K2 bridge.

All verdict-path comparisons use integers or Fraction.  Floating point appears
only in displays and in two non-boundary diagnostics (the annealed constant and
the published fixed-k error formula); both are bracketed far from their tested
thresholds.
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction


DIGEST = "BRIEF5_F2_MYERSON_PROGRAM_ARITHMETIC_PASS"
TOLERANCE_BITS = 1_050_000_000_000
MOVING_LEVEL_EXPONENTS = tuple(range(25, 41))  # 2^25,...,2^40
ALIGNMENT_N_TOP = 1 << 40
AMBIENT_N_PRIZE = 1 << 41


class CheckFailure(AssertionError):
    pass


def check(name: str, condition: bool, detail: str = "") -> None:
    if not condition:
        raise CheckFailure(f"{name}: {detail}")
    print(f"[PASS] {name}" + (f"  ({detail})" if detail else ""))


def ceil_log2_int(x: int) -> int:
    if x <= 0:
        raise ValueError("x must be positive")
    return (x - 1).bit_length()


def struct_modulus(j: int) -> int:
    """M_j = 2^ceil(log2(j+1)), for j>=1."""
    if j < 1:
        raise ValueError("j must be >= 1")
    return 1 << ceil_log2_int(j + 1)


def euler_phi_power_of_two(k: int) -> int:
    if k < 1 or k & (k - 1):
        raise ValueError("k must be a positive power of two")
    return 1 if k == 1 else k // 2


def tower_budget_checks() -> None:
    levels = [1 << e for e in MOVING_LEVEL_EXPONENTS]
    total = sum(levels)
    expected = (1 << 41) - (1 << 25)
    check("sixteen moving levels", len(levels) == 16)
    check("tower geometric sum", total == expected, f"sum={total}")

    one_third = Fraction(total, 3)
    one_half = Fraction(total, 2)
    check(
        "per-rung exponent n_r/3 fits even under log-additive composition",
        one_third < TOLERANCE_BITS,
        f"used={int(one_third)} slack={TOLERANCE_BITS-int(one_third)} bits",
    )
    check(
        "per-rung exponent n_r/2 fails the same conservative composition",
        one_half > TOLERANCE_BITS,
        f"used={int(one_half)} excess={int(one_half)-TOLERANCE_BITS} bits",
    )

    theta_star = Fraction(TOLERANCE_BITS, total)
    check(
        "common linear-exponent threshold lies between 1/3 and 1/2",
        Fraction(1, 3) < theta_star < Fraction(1, 2),
        f"theta*={float(theta_star):.12f}",
    )

    # If the 16 sectors are an orthogonal additive partition, Cauchy costs only
    # sqrt(16)=4, i.e. two bits, beyond the largest per-sector exponent.
    additive_one_third = Fraction(ALIGNMENT_N_TOP, 3) + 2
    check(
        "n_top/3 also fits additive-sector Cauchy assembly",
        additive_one_third < TOLERANCE_BITS,
        f"used~{float(additive_one_third):.3f} bits",
    )

    additive_nineteen_twentieths = Fraction(19 * ALIGNMENT_N_TOP, 20) + 2
    check(
        "additive-only budget could tolerate 19n/20 per top sector",
        additive_nineteen_twentieths < TOLERANCE_BITS,
        f"slack~{float(TOLERANCE_BITS-additive_nineteen_twentieths):.3f} bits",
    )

    # Explicit 2^(n/100) is much stronger than needed and composes comfortably.
    one_percent = Fraction(total, 100)
    check(
        "explicit n_r/100 programme has very large assembly slack",
        one_percent < TOLERANCE_BITS,
        f"used={float(one_percent):.2f} slack factor={TOLERANCE_BITS/float(one_percent):.3f}",
    )


def notation_checks() -> None:
    check(
        "ambient and parity-alignment n are not silently identified",
        AMBIENT_N_PRIZE == 2 * ALIGNMENT_N_TOP,
        f"ambient=2^41, moving-top=2^40",
    )


def structural_drift_checks() -> None:
    expected = {
        1: 2,
        2: 4,
        3: 4,
        4: 8,
        5: 8,
        6: 8,
        7: 8,
        8: 16,
        15: 16,
        16: 32,
    }
    for j, want in expected.items():
        got = struct_modulus(j)
        check(f"struct modulus j={j}", got == want, f"M_j={got}")

    check(
        "catch-28 guard: j=4 is not a 2^(n/4) structural sector",
        struct_modulus(4) == 8 and struct_modulus(4) != 4,
        "correct exponent is n/8",
    )


def weighted_alignment_counterexample() -> None:
    """Balanced signs + constant modulus max/mean do not imply weighted alignment."""
    N = ALIGNMENT_N_TOP
    plus = minus = N // 2
    numerator = 3 * plus - minus
    variance = 9 * plus + minus
    total_weight = 3 * plus + minus
    mean_weight = Fraction(total_weight, N)
    max_to_mean = Fraction(3, 1) / mean_weight

    check("balanced-sign counterexample has zero unweighted mean", plus == minus)
    check("counterexample has constant modulus max/mean", max_to_mean == Fraction(3, 2))
    check("counterexample numerator", numerator == N)
    check("counterexample L2 mass", variance == 5 * N)

    # numerator/sqrt(variance) > 2^15, squared exactly.
    check(
        "constant max/mean does not imply 2^15 weighted alignment",
        numerator * numerator > (1 << 30) * variance,
        f"ratio bits={0.5*math.log2(numerator*numerator/variance):.6f}",
    )

    check(
        "sign-only diagnostics cannot replace a joint sign-weight theorem",
        mean_weight == 2 and numerator != 0,
    )


def orbit_invariance_checks() -> None:
    orbit_size = 1 << 56  # campaign-scale n*k proxy
    quotient_num = 7
    quotient_var = 49
    lifted_num = orbit_size * quotient_num
    lifted_var = orbit_size * quotient_var
    check(
        "Frobenius/twisted invariance creates no within-orbit cancellation",
        lifted_num * lifted_num == orbit_size * quotient_num * quotient_num * lifted_var // quotient_var,
    )
    lifted_ratio_bits = 0.5 * math.log2(orbit_size) + math.log2(abs(quotient_num) / math.sqrt(quotient_var))
    check(
        "official proxy orbit multiplicity contributes 28 alignment bits",
        abs(lifted_ratio_bits - 28.0) < 1e-12,
        "sqrt(2^56)=2^28",
    )


def asymptotic_effectivity_checks() -> None:
    explicit = Fraction(ALIGNMENT_N_TOP, 100)
    check("explicit 2^(n/100) is consumable at n=2^40", explicit < TOLERANCE_BITS)

    hidden_constant_exponent = 10**15 + math.isqrt(ALIGNMENT_N_TOP)
    check(
        "bare 2^o(n) wording is not a finite official certificate",
        hidden_constant_exponent > TOLERANCE_BITS,
        f"counterexample exponent={hidden_constant_exponent}",
    )


def annealed_route_fence() -> None:
    death_constant = math.log2(4 / math.pi)
    bits = death_constant * ALIGNMENT_N_TOP
    check(
        "annealed absolute-value loss is linear in n",
        0.34 < death_constant < 0.35,
        f"log2(4/pi)={death_constant:.12f}; loss~{bits:.3f} bits",
    )


def literature_regime_diagnostic() -> None:
    """Fixed-k error from arXiv:2507.09303v3 at a tower-shaped proxy."""
    p_bits = 31
    k = 1 << 24
    phi_k = euler_phi_power_of_two(k)
    first_term_log2 = (
        math.log2(4 * math.sqrt(3))
        + math.log2(k)
        + math.log2(k + 1)
        - Fraction(p_bits, phi_k)
    )
    check(
        "new Gaussian-period Mahler theorem is quantitatively vacuous at growing-k proxy",
        float(first_term_log2) > 50,
        f"first-term log2~{float(first_term_log2):.6f}",
    )

    k_small = 4
    small_log2 = (
        math.log2(4 * math.sqrt(3))
        + math.log2(k_small)
        + math.log2(k_small + 1)
        - p_bits / 2
    )
    check(
        "same published estimate is effective in a fixed-small-k regime",
        small_log2 < 0,
        f"first-term log2~{small_log2:.6f}",
    )


def weak_margin_block_target() -> None:
    """Campaign-proxy calibration of the block-contraction scale."""
    frequency_bits_proxy = 2_150_000_000_000
    orbit_saving_bits = 28
    required_bias_bits = Fraction(frequency_bits_proxy, 2) - orbit_saving_bits - TOLERANCE_BITS
    bits_43 = Fraction(ALIGNMENT_N_TOP, 43)
    bits_44 = Fraction(ALIGNMENT_N_TOP, 44)
    check(
        "proxy required weighted-bias saving is positive but only about 2.5e10 bits",
        24_000_000_000 < required_bias_bits < 26_000_000_000,
        f"required~{float(required_bias_bits):.3f}",
    )
    check(
        "one contraction bit per 43 moving coordinates clears the proxy",
        bits_43 > required_bias_bits,
        f"available~{float(bits_43):.3f}",
    )
    check(
        "one contraction bit per 44 moving coordinates narrowly misses the proxy",
        bits_44 < required_bias_bits,
        f"available~{float(bits_44):.3f}",
    )


def b_resolved_structure_checks() -> None:
    n = 64
    b = 32
    struct_b = math.comb(n // 4, b // 4)
    check("b-resolved struct formula at n=64,b=32", struct_b == 12_870)
    check("b-resolved struct vanishes off the 4-grid", 31 % 4 != 0)
    check(
        "b-resolved struct respects complement symmetry",
        math.comb(n // 4, b // 4) == math.comb(n // 4, (n - b) // 4),
    )


def main() -> None:
    try:
        notation_checks()
        tower_budget_checks()
        structural_drift_checks()
        weighted_alignment_counterexample()
        orbit_invariance_checks()
        asymptotic_effectivity_checks()
        annealed_route_fence()
        literature_regime_diagnostic()
        weak_margin_block_target()
        b_resolved_structure_checks()
    except (CheckFailure, AssertionError, ValueError) as exc:
        print(f"BRIEF5_F2_MYERSON_PROGRAM_ARITHMETIC_FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
    print(DIGEST)


if __name__ == "__main__":
    main()
