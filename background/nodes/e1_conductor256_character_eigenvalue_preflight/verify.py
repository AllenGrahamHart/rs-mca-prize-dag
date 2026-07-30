#!/usr/bin/env python3
"""Certified interval preflight for the conductor-256 unit-log spectrum.

Only Decimal arithmetic with directed rounding is used.  Pi is enclosed by
Machin's formula, and every sine, logarithm, and root of unity is enclosed by
an explicit convergent series with a proved remainder bound.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import (
    Context,
    Decimal,
    ROUND_CEILING,
    ROUND_FLOOR,
    localcontext,
)
from hashlib import sha256
from math import comb, isqrt


PRECISION = 96
GUARD_PRECISION = 112
ORDER = 64
SCALE_DIGITS = 30
SCALE = Decimal(10) ** SCALE_DIGITS
EPSILON = Decimal(10) ** (-(PRECISION - 16))
EXPECTED_SPECTRUM_DIGEST = "6ee33c37477a58c92a087cd7dcf3c128d148a2c8d08887141ff79367aa9efb8d"

DOWN = Context(prec=GUARD_PRECISION, rounding=ROUND_FLOOR)
UP = Context(prec=GUARD_PRECISION, rounding=ROUND_CEILING)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def down_add(a: Decimal, b: Decimal) -> Decimal:
    with localcontext(DOWN):
        return a + b


def up_add(a: Decimal, b: Decimal) -> Decimal:
    with localcontext(UP):
        return a + b


def down_sub(a: Decimal, b: Decimal) -> Decimal:
    with localcontext(DOWN):
        return a - b


def up_sub(a: Decimal, b: Decimal) -> Decimal:
    with localcontext(UP):
        return a - b


def down_mul(a: Decimal, b: Decimal) -> Decimal:
    with localcontext(DOWN):
        return a * b


def up_mul(a: Decimal, b: Decimal) -> Decimal:
    with localcontext(UP):
        return a * b


def down_div(a: Decimal, b: Decimal) -> Decimal:
    with localcontext(DOWN):
        return a / b


def up_div(a: Decimal, b: Decimal) -> Decimal:
    with localcontext(UP):
        return a / b


def down_sqrt(a: Decimal) -> Decimal:
    with localcontext(DOWN):
        return a.sqrt()


def up_sqrt(a: Decimal) -> Decimal:
    with localcontext(UP):
        return a.sqrt()


def floor_decimal(a: Decimal) -> int:
    return int(a.to_integral_value(rounding=ROUND_FLOOR))


def ceil_decimal(a: Decimal) -> int:
    return int(a.to_integral_value(rounding=ROUND_CEILING))


@dataclass(frozen=True)
class Interval:
    lo: Decimal
    hi: Decimal

    def __post_init__(self) -> None:
        require(self.lo <= self.hi, "reversed interval")

    @staticmethod
    def point(value: int | str | Decimal) -> "Interval":
        d = value if isinstance(value, Decimal) else Decimal(value)
        return Interval(d, d)

    def __add__(self, other: "Interval") -> "Interval":
        return Interval(down_add(self.lo, other.lo), up_add(self.hi, other.hi))

    def __neg__(self) -> "Interval":
        # Decimal unary minus obeys the ambient context and can silently round.
        return Interval(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other: "Interval") -> "Interval":
        return Interval(down_sub(self.lo, other.hi), up_sub(self.hi, other.lo))

    def __mul__(self, other: "Interval") -> "Interval":
        lows = [
            down_mul(self.lo, other.lo),
            down_mul(self.lo, other.hi),
            down_mul(self.hi, other.lo),
            down_mul(self.hi, other.hi),
        ]
        highs = [
            up_mul(self.lo, other.lo),
            up_mul(self.lo, other.hi),
            up_mul(self.hi, other.lo),
            up_mul(self.hi, other.hi),
        ]
        return Interval(min(lows), max(highs))

    def __truediv__(self, other: "Interval") -> "Interval":
        require(other.lo > 0, "division needs a positive denominator")
        reciprocal = Interval(down_div(Decimal(1), other.hi), up_div(Decimal(1), other.lo))
        return self * reciprocal

    def times_int(self, value: int) -> "Interval":
        return self * Interval.point(value)

    def width(self) -> Decimal:
        return up_sub(self.hi, self.lo)


ZERO = Interval.point(0)
ONE = Interval.point(1)
TWO = Interval.point(2)


def alternating_atan_inverse(denominator: int) -> Interval:
    """Enclose atan(1/denominator) by its alternating Taylor series."""
    x = ONE / Interval.point(denominator)
    x2 = x * x
    power = x
    total = ZERO
    sign = 1
    for index in range(100):
        term = power / Interval.point(2 * index + 1)
        total = total + (term if sign > 0 else -term)
        power = power * x2
        sign = -sign
    next_term = power / Interval.point(201)
    require(next_term.hi < EPSILON, "atan series did not converge")
    return Interval(
        down_sub(total.lo, next_term.hi),
        up_add(total.hi, next_term.hi),
    )


def pi_interval() -> Interval:
    return alternating_atan_inverse(5).times_int(16) - alternating_atan_inverse(239).times_int(4)


def sine_point(x: Decimal) -> Interval:
    """Enclose sin(x) for an exact Decimal 0 <= x <= pi/2."""
    point = Interval.point(x)
    x2 = point * point
    power = point
    total = ZERO
    sign = 1
    for index in range(50):
        total = total + (power if sign > 0 else -power)
        denominator = (2 * index + 2) * (2 * index + 3)
        power = power * x2 / Interval.point(denominator)
        sign = -sign
    require(power.hi < EPSILON, "sine series did not converge")
    return Interval(
        down_sub(total.lo, power.hi),
        up_add(total.hi, power.hi),
    )


def cosine_point(x: Decimal) -> Interval:
    """Enclose cos(x) for an exact Decimal 0 <= x <= pi/2."""
    point = Interval.point(x)
    x2 = point * point
    power = ONE
    total = ZERO
    sign = 1
    for index in range(50):
        total = total + (power if sign > 0 else -power)
        denominator = (2 * index + 1) * (2 * index + 2)
        power = power * x2 / Interval.point(denominator)
        sign = -sign
    require(power.hi < EPSILON, "cosine series did not converge")
    return Interval(
        down_sub(total.lo, power.hi),
        up_add(total.hi, power.hi),
    )


def sine_monotone(angle: Interval) -> Interval:
    lower = sine_point(angle.lo)
    upper = sine_point(angle.hi)
    return Interval(min(lower.lo, upper.lo), max(lower.hi, upper.hi))


def cosine_monotone(angle: Interval) -> Interval:
    lower_at_upper = cosine_point(angle.hi)
    upper_at_lower = cosine_point(angle.lo)
    return Interval(
        min(lower_at_upper.lo, upper_at_lower.lo),
        max(lower_at_upper.hi, upper_at_lower.hi),
    )


def atanh_nonnegative(z: Interval) -> Interval:
    require(z.lo >= 0 and z.hi < 1, "atanh interval outside [0,1)")
    z2 = z * z
    power = z
    total = ZERO
    for index in range(110):
        total = total + power / Interval.point(2 * index + 1)
        power = power * z2
    next_term_upper = up_div(power.hi, Decimal(221))
    require(next_term_upper < EPSILON, "atanh series did not converge")
    one_minus = down_sub(Decimal(1), z2.hi)
    require(one_minus > 0, "invalid atanh remainder denominator")
    remainder = up_div(next_term_upper, one_minus)
    return Interval(total.lo, up_add(total.hi, remainder))


LOG_TWO = atanh_nonnegative(ONE / Interval.point(3)).times_int(2)


def log_positive(value: Interval) -> Interval:
    """Enclose log(value) for a positive interval with upper endpoint <= 1."""
    require(value.lo > 0 and value.hi <= 1, "log reducer expects (0,1]")
    scaled = value
    exponent = 0
    while scaled.lo < 1:
        scaled = scaled.times_int(2)
        exponent += 1
    require(scaled.lo >= 1 and scaled.hi < 2, "log interval crossed a power-of-two boundary")
    z = (scaled - ONE) / (scaled + ONE)
    return atanh_nonnegative(z).times_int(2) - LOG_TWO.times_int(exponent)


def canonical(value: int) -> int:
    value %= 256
    return min(value, 256 - value)


@dataclass(frozen=True)
class ComplexInterval:
    real: Interval
    imag: Interval

    def __add__(self, other: "ComplexInterval") -> "ComplexInterval":
        return ComplexInterval(self.real + other.real, self.imag + other.imag)

    def conjugate(self) -> "ComplexInterval":
        return ComplexInterval(self.real, -self.imag)


COMPLEX_ZERO = ComplexInterval(ZERO, ZERO)


def root_table(pi: Interval) -> list[ComplexInterval]:
    sine: list[Interval] = [ZERO]
    cosine: list[Interval] = [ONE]
    for residue in range(1, 17):
        angle = pi.times_int(residue) / Interval.point(32)
        sine.append(sine_monotone(angle))
        cosine.append(cosine_monotone(angle))

    roots: list[ComplexInterval] = []
    for index in range(ORDER):
        quadrant, residue = divmod(index, 16)
        c = cosine[residue]
        s = sine[residue]
        if quadrant == 0:
            roots.append(ComplexInterval(c, s))
        elif quadrant == 1:
            roots.append(ComplexInterval(-s, c))
        elif quadrant == 2:
            roots.append(ComplexInterval(-c, -s))
        else:
            roots.append(ComplexInterval(s, -c))
    return roots


def interval_overlap(left: Interval, right: Interval) -> bool:
    return max(left.lo, right.lo) <= min(left.hi, right.hi)


def magnitude_bounds(value: ComplexInterval) -> tuple[Decimal, Decimal]:
    def min_abs(part: Interval) -> Decimal:
        if part.lo <= 0 <= part.hi:
            return Decimal(0)
        return min(part.lo.copy_abs(), part.hi.copy_abs())

    real_min = min_abs(value.real)
    imag_min = min_abs(value.imag)
    real_max = max(value.real.lo.copy_abs(), value.real.hi.copy_abs())
    imag_max = max(value.imag.lo.copy_abs(), value.imag.hi.copy_abs())
    lower_square = down_add(down_mul(real_min, real_min), down_mul(imag_min, imag_min))
    upper_square = up_add(up_mul(real_max, real_max), up_mul(imag_max, imag_max))
    return down_sqrt(lower_square), up_sqrt(upper_square)


def spectrum() -> tuple[Interval, list[ComplexInterval], list[tuple[Decimal, Decimal]]]:
    pi = pi_interval()
    require(
        pi.lo > Decimal("3.141592653589793238462643383279")
        and pi.hi < Decimal("3.141592653589793238462643383280"),
        f"pi enclosure failed: {pi}",
    )
    roots = root_table(pi)

    representatives = [canonical(pow(5, index, 256)) for index in range(ORDER)]
    require(set(representatives) == set(range(1, 128, 2)), "wrong powers of 5")
    logs: list[Interval] = []
    for representative in representatives:
        angle = pi.times_int(representative) / Interval.point(256)
        sine_value = sine_monotone(angle)
        logs.append(log_positive(sine_value).times_int(2))

    kappas: list[ComplexInterval] = []
    for frequency in range(ORDER):
        total = COMPLEX_ZERO
        for index, log_value in enumerate(logs):
            # exp(-2*pi*i*frequency*index/64) is the conjugate root.
            root = roots[(frequency * index) % ORDER].conjugate()
            total = total + ComplexInterval(log_value * root.real, log_value * root.imag)
        kappas.append(total)

    magnitudes = [magnitude_bounds(value) for value in kappas]
    for frequency in range(1, ORDER):
        require(magnitudes[frequency][0] > 0, f"kappa_{frequency} interval meets zero")
        conjugate = kappas[-frequency % ORDER].conjugate()
        require(
            interval_overlap(kappas[frequency].real, conjugate.real),
            f"real conjugacy mismatch at {frequency}: {kappas[frequency].real} {conjugate.real}",
        )
        require(
            interval_overlap(kappas[frequency].imag, conjugate.imag),
            f"imaginary conjugacy mismatch at {frequency}: {kappas[frequency].imag} {conjugate.imag}",
        )
    require(kappas[32].imag.lo <= 0 <= kappas[32].imag.hi, "kappa_32 is not real")
    return pi, kappas, magnitudes


def count_zero_sum_l2_envelope(coordinate_bound: int, l2_bound: int) -> int:
    """Count the exact coarse integer envelope without storing its vectors."""
    states: dict[tuple[int, int], int] = {(0, 0): 1}
    choices = [(value, value * value) for value in range(-coordinate_bound, coordinate_bound + 1)]
    for _coordinate in range(ORDER):
        next_states: dict[tuple[int, int], int] = {}
        for (total, energy), multiplicity in states.items():
            for value, square in choices:
                new_energy = energy + square
                if new_energy > l2_bound:
                    continue
                key = (total + value, new_energy)
                next_states[key] = next_states.get(key, 0) + multiplicity
        states = next_states
    return sum(
        multiplicity
        for (total, _energy), multiplicity in states.items()
        if total == 0
    )


def main() -> None:
    pi, _kappas, magnitudes = spectrum()
    nontrivial = magnitudes[1:]
    minimum_index = min(range(1, ORDER), key=lambda j: magnitudes[j][0])
    maximum_index = max(range(1, ORDER), key=lambda j: magnitudes[j][1])
    minimum_lower = magnitudes[minimum_index][0]
    maximum_upper = magnitudes[maximum_index][1]
    require(minimum_index == 32, "minimum-frequency index drift")
    require(maximum_index in (11, 53), "maximum-frequency index drift")
    require(
        all(magnitudes[32][1] < magnitudes[j][0] for j in range(1, ORDER) if j != 32),
        "minimum eigenvalue is not strictly isolated at frequency 32",
    )
    require(
        all(
            magnitudes[11][0] > magnitudes[j][1]
            for j in range(1, ORDER)
            if j not in (11, 53)
        ),
        "maximum eigenvalue pair is not strictly isolated at frequencies 11 and 53",
    )
    require(
        interval_overlap(Interval(*magnitudes[11]), Interval(*magnitudes[53])),
        "conjugate maximum-frequency magnitudes do not overlap",
    )

    inverse_sum_upper = Decimal(0)
    inverse_square_sum_upper = Decimal(0)
    brackets: list[str] = []
    for frequency, (lower, upper) in enumerate(nontrivial, start=1):
        inverse_sum_upper = up_add(inverse_sum_upper, up_div(Decimal(1), lower))
        inverse_square_sum_upper = up_add(
            inverse_square_sum_upper,
            up_div(Decimal(1), down_mul(lower, lower)),
        )
        lower_scaled = floor_decimal(down_mul(lower, SCALE))
        upper_scaled = ceil_decimal(up_mul(upper, SCALE))
        require(lower_scaled > 0, "scaled spectral lower bound vanished")
        brackets.append(f"{frequency}:{lower_scaled}:{upper_scaled}")

    log_nine_sixteenths = log_positive(Interval.point(Decimal(9) / Decimal(16)))
    log_eighteen = log_nine_sixteenths + LOG_TWO.times_int(5)
    d_upper_interval = log_eighteen.times_int(64) - LOG_TWO.times_int(256)
    d_upper = d_upper_interval.hi
    require(d_upper > 0, "empty worst-case cofactor body")
    r_upper = up_mul(
        Decimal(2),
        up_add(d_upper, up_sqrt(up_mul(Decimal(128), d_upper))),
    )

    coordinate_upper = up_div(up_mul(r_upper, inverse_sum_upper), Decimal(64))
    l2_upper = up_div(
        up_mul(up_mul(r_upper, r_upper), inverse_square_sum_upper),
        Decimal(64),
    )
    coordinate_bound = floor_decimal(coordinate_upper)
    l2_bound = floor_decimal(l2_upper)
    require(coordinate_bound > 0 and l2_bound > 0, "degenerate exponent bounds")

    box_count = pow(2 * coordinate_bound + 1, 63)
    box_bits_floor = box_count.bit_length() - 1
    box_digits = len(str(box_count))
    l2_radius = isqrt(l2_bound)
    require(l2_radius <= coordinate_bound * 8, "unexpected L2/coordinate mismatch")
    coarse_envelope_count = count_zero_sum_l2_envelope(coordinate_bound, l2_bound)
    coarse_envelope_bits_floor = coarse_envelope_count.bit_length() - 1
    coarse_envelope_digits = len(str(coarse_envelope_count))
    require(
        coarse_envelope_count == 16_616_854_517_524_950_208_619_690_062_355_423_946_568_371,
        "coarse Fourier envelope count drift",
    )

    # Every vector with k entries +1, k entries -1, and all other entries
    # zero has norm squared 2k.  Bounding every spectral weight by max|kappa|
    # proves that the universal weighted ellipsoid itself contains this family.
    sparse_inside_max = floor_decimal(
        down_div(
            down_mul(r_upper, r_upper),
            up_mul(Decimal(2), up_mul(maximum_upper, maximum_upper)),
        )
    )
    sparse_inside_max = min(sparse_inside_max, ORDER // 2)
    sparse_inside_count = sum(
        comb(ORDER, count) * comb(ORDER - count, count)
        for count in range(sparse_inside_max + 1)
    )
    require(sparse_inside_max >= 5, "weighted-ellipsoid lower family regressed")
    require(sparse_inside_max == 5, "weighted-ellipsoid sparse radius drift")
    require(sparse_inside_count == 38_482_585_013_041, "weighted-ellipsoid family count drift")

    digest = sha256("\n".join(brackets).encode("ascii")).hexdigest()
    require(digest == EXPECTED_SPECTRUM_DIGEST, "spectrum bracket digest drift")

    require(pi.width() < Decimal("1e-80"), "pi interval too wide")
    require(max(upper - lower for lower, upper in nontrivial) < Decimal("1e-70"), "spectrum interval too wide")
    require(minimum_lower > Decimal("1.7627"), "minimum eigenvalue headline drift")
    require(maximum_upper < Decimal("24.292"), "maximum eigenvalue headline drift")
    require(inverse_sum_upper < Decimal("6.556"), "inverse-sum headline drift")
    require(inverse_square_sum_upper < Decimal("1.090"), "inverse-square headline drift")
    require(d_upper < Decimal("7.539") and r_upper < Decimal("77.202"), "log-body headline drift")
    require(coordinate_bound == 7 and l2_bound == 101, "integer exponent bound drift")

    print("E1_CONDUCTOR256_CHARACTER_EIGENVALUE_PREFLIGHT_PASS checks=71")
    print(f"spectrum_digest={digest}")
    print(f"minimum_index={minimum_index} minimum_lower={minimum_lower}")
    print(f"maximum_index={maximum_index} maximum_upper={maximum_upper}")
    print(f"inverse_sum_upper={inverse_sum_upper}")
    print(f"inverse_square_sum_upper={inverse_square_sum_upper}")
    print(f"D_upper={d_upper} R_upper={r_upper}")
    print(f"coordinate_bound={coordinate_bound} l2_bound={l2_bound}")
    print(f"coordinate_box_bits_floor={box_bits_floor} coordinate_box_digits={box_digits}")
    print(
        "coarse_zero_sum_l2_count="
        f"{coarse_envelope_count} bits_floor={coarse_envelope_bits_floor} "
        f"digits={coarse_envelope_digits}"
    )
    print(
        f"weighted_ellipsoid_sparse_inside_k={sparse_inside_max} "
        f"count={sparse_inside_count}"
    )


if __name__ == "__main__":
    main()
