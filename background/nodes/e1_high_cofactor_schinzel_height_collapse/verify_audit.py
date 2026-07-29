#!/usr/bin/env python3
"""Independent exact-rational audit of the E1 entropy-height separation."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256


F = Fraction
ORDER = 64
TERMS = 48
BISECTION_STEPS = 84
D_LIMIT = F(6845, 1000)
P_LIMIT = F(119, 10)
SCALE = 10**20
EXPECTED_AUDIT_DIGEST = (
    "0404fc4ac941d2a48453fac4d316b47f4c2538b7f3db47d0b6a5ea356c6f9e2f"
)


def atanh_log_core(value: F) -> tuple[F, F]:
    """Bound log(value) for 1<=value<=2 by an exact atanh series."""
    if not F(1) <= value <= F(2):
        raise RuntimeError(f"core log input outside [1,2]: {value}")
    z = (value - 1) / (value + 1)
    z2 = z * z
    power = z
    total = F(0)
    for index in range(TERMS):
        total += 2 * power / (2 * index + 1)
        power *= z2
    tail = 2 * power / ((2 * TERMS + 1) * (1 - z2))
    return total, total + tail


LOG_TWO_LO, LOG_TWO_HI = atanh_log_core(F(2))


def log_bounds(value: F) -> tuple[F, F]:
    if value <= 0:
        raise RuntimeError("log input must be positive")
    exponent = 0
    scaled = value
    while scaled >= 2:
        scaled /= 2
        exponent += 1
    while scaled < 1:
        scaled *= 2
        exponent -= 1
    lower, upper = atanh_log_core(scaled)
    if exponent >= 0:
        return lower + exponent * LOG_TWO_LO, upper + exponent * LOG_TWO_HI
    return lower + exponent * LOG_TWO_HI, upper + exponent * LOG_TWO_LO


def floor_fraction(value: F) -> int:
    return value.numerator // value.denominator


def entropy_audit() -> tuple[F, int, str, int, int]:
    rows: list[str] = []
    minimum: F | None = None
    minimum_index = -1
    active = 0
    skipped = 0

    for positive_count in range(1, ORDER):
        negative_count = ORDER - positive_count
        _maximum_lo, maximum_hi = log_bounds(F(ORDER, positive_count))
        if positive_count * maximum_hi < P_LIMIT:
            skipped += 1
            rows.append(f"{positive_count}:skip")
            continue

        active += 1
        lower_excess = F(0)
        upper_excess = F(negative_count)
        for _ in range(BISECTION_STEPS):
            midpoint = (lower_excess + upper_excess) / 2
            _candidate_lo, candidate_hi = log_bounds(
                1 + midpoint / positive_count
            )
            if positive_count * candidate_hi < P_LIMIT:
                lower_excess = midpoint
            else:
                upper_excess = midpoint

        positive_lo, positive_hi = log_bounds(
            1 + lower_excess / positive_count
        )
        negative_lo, negative_hi = log_bounds(
            1 - lower_excess / negative_count
        )
        if not positive_count * positive_hi < P_LIMIT:
            raise RuntimeError(f"invalid entropy bracket at {positive_count}")

        barrier_lower = (
            -positive_count * positive_hi - negative_count * negative_hi
        )
        if not barrier_lower > D_LIMIT:
            raise RuntimeError(
                f"rational entropy barrier failed at {positive_count}: "
                f"{float(barrier_lower)}"
            )
        if minimum is None or barrier_lower < minimum:
            minimum = barrier_lower
            minimum_index = positive_count
        rows.append(
            f"{positive_count}:{floor_fraction(lower_excess * SCALE)}:"
            f"{floor_fraction(barrier_lower * SCALE)}"
        )

    if minimum is None:
        raise RuntimeError("empty rational entropy audit")
    digest = sha256("\n".join(rows).encode("ascii")).hexdigest()
    return minimum, minimum_index, digest, active, skipped


def main() -> None:
    _log_eighteen_lo, log_eighteen_hi = log_bounds(F(18))
    deficit_upper = 64 * log_eighteen_hi - 257 * LOG_TWO_LO
    if not deficit_upper < D_LIMIT:
        raise RuntimeError(f"rational deficit bound failed: {float(deficit_upper)}")

    minimum, minimum_index, digest, active, skipped = entropy_audit()
    print(f"audit_digest={digest}")
    if digest != EXPECTED_AUDIT_DIGEST:
        raise RuntimeError(f"audit digest drift: {digest}")

    sqrt_five_lower = F(2236067977499789696409173668731276235, 10**36)
    if not sqrt_five_lower * sqrt_five_lower < 5:
        raise RuntimeError("invalid rational lower bound for sqrt(5)")
    phi_lower = (1 + sqrt_five_lower) / 2
    log_phi_lower, _log_phi_upper = log_bounds(phi_lower)
    pair_upper = 2 * (D_LIMIT + 2 * P_LIMIT)
    schinzel_lower = 128 * log_phi_lower
    if not pair_upper < schinzel_lower:
        raise RuntimeError("rational Schinzel separation failed")

    print(
        "E1_HIGH_COFACTOR_SCHINZEL_HEIGHT_COLLAPSE_AUDIT_PASS "
        f"active={active} skipped={skipped}"
    )
    print(
        f"minimum_barrier_lower={float(minimum):.15f} "
        f"positive_count={minimum_index}"
    )
    print(
        f"deficit_upper={float(deficit_upper):.15f} "
        f"pair_upper={float(pair_upper):.6f} "
        f"schinzel_lower={float(schinzel_lower):.15f}"
    )


if __name__ == "__main__":
    main()
