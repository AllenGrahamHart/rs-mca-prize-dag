#!/usr/bin/env python3
"""Independent exact-rational audit of the cofactor-2 Smyth separation."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256


F = Fraction
ORDER = 64
TERMS = 48
BISECTION_STEPS = 84
D_LIMIT = F(7539, 1000)
P_LIMIT = F(61, 5)
SCALE = 10**20
EXPECTED_AUDIT_DIGEST = (
    "ee3e59acdfed6536189c3ff18476a7c657e279729e0c906ef627c4224c245cb8"
)


def atanh_log_core(value: F) -> tuple[F, F]:
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

        _positive_lo, positive_hi = log_bounds(
            1 + lower_excess / positive_count
        )
        _negative_lo, negative_hi = log_bounds(
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


def smyth_polynomial(value: F) -> F:
    return value**4 - value**3 - 3 * value**2 + value + 1


def main() -> None:
    _log_eighteen_lo, log_eighteen_hi = log_bounds(F(18))
    deficit_upper = 64 * log_eighteen_hi - 256 * LOG_TWO_LO
    if not deficit_upper < D_LIMIT:
        raise RuntimeError(f"rational deficit bound failed: {float(deficit_upper)}")

    minimum, index, digest, active, skipped = entropy_audit()
    print(f"audit_digest={digest}")
    if digest != EXPECTED_AUDIT_DIGEST:
        raise RuntimeError(f"audit digest drift: {digest}")

    if not smyth_polynomial(F(209, 100)) < 0 < smyth_polynomial(F(3)):
        raise RuntimeError("positive beta_2 root bracket failed")
    if not smyth_polynomial(F(-2)) > 0 > smyth_polynomial(F(-133, 100)):
        raise RuntimeError("negative beta_2 root bracket failed")
    if not F(209, 100) * F(133, 100) > F(129, 100) ** 4:
        raise RuntimeError("beta_2 Mahler lower bound failed")

    log_129_lower, _log_129_upper = log_bounds(F(129, 100))
    pair_upper = 2 * (D_LIMIT + 2 * P_LIMIT)
    smyth_lower = 256 * log_129_lower
    if not pair_upper < smyth_lower:
        raise RuntimeError("rational Smyth separation failed")

    print(
        "E1_COFACTOR2_SMYTH_HEIGHT_COLLAPSE_AUDIT_PASS "
        f"active={active} skipped={skipped}"
    )
    print(
        f"minimum_barrier_lower={float(minimum):.15f} "
        f"positive_count={index}"
    )
    print(
        f"deficit_upper={float(deficit_upper):.15f} "
        f"pair_upper={float(pair_upper):.6f} "
        f"smyth_lower={float(smyth_lower):.15f}"
    )


if __name__ == "__main__":
    main()
