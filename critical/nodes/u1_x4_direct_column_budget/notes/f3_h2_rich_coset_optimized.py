#!/usr/bin/env python3
"""Exact checks for the optimized h=2 rich-coset Stepanov constant."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt


K_RICH = 66
TRIVIAL_X_MAX = 65 * 65
ENERGY_CONSTANT = 1 + 5 * (K_RICH * K_RICH + K_RICH)


def floor_nth_root(n: int, k: int) -> int:
    if n < 0:
        raise ValueError(n)
    if n < 2:
        return n
    lo, hi = 1, 1
    while hi**k <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**k <= n:
            lo = mid
        else:
            hi = mid
    return lo


def floor_scaled_cuberoot(num: int, den: int, scale: int) -> int:
    """Return floor((num/den)^(1/3) / scale), exactly."""

    if num <= 0 or den <= 0 or scale <= 0:
        raise ValueError((num, den, scale))
    lo, hi = 0, 1
    while (scale * hi) ** 3 * den <= num:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if (scale * mid) ** 3 * den <= num:
            lo = mid
        else:
            hi = mid
    return lo


def min_p_for_h4t(h: int, t: int) -> int:
    """Smallest integer p satisfying p^3 > h^4 t."""

    value = h**4 * t
    p = floor_nth_root(value, 3)
    while p**3 <= value:
        p += 1
    return p


@dataclass(frozen=True)
class ParameterRow:
    h: int
    t: int
    branch: str
    a: int
    b: int
    d: int
    linear_slack: int
    nonvanishing_slack: int


def parameter_row(h: int, t: int) -> ParameterRow:
    if h < 1 or t < 1:
        raise ValueError((h, t))

    # X <= TRIVIAL_X_MAX is equivalent to h^2 <= TRIVIAL_X_MAX^3 * t.
    if h * h <= TRIVIAL_X_MAX**3 * t:
        # Verify h <= K*(hT)^(2/3), cubed to avoid real arithmetic.
        if h**3 > K_RICH**3 * (h * t) ** 2:
            raise AssertionError((h, t, "trivial branch bound"))
        return ParameterRow(h, t, "trivial", 0, 0, 0, 0, 0)

    a = floor_scaled_cuberoot(h * h, t, 4)
    b = floor_scaled_cuberoot(h * t, 1, 2)
    d = floor_scaled_cuberoot(h * h, t, 64)
    if min(a, b, d) < 1:
        raise AssertionError((h, t, a, b, d))

    # Linear-system inequality: D(A+D)T < AB^2.
    linear_slack = a * b * b - d * (a + d) * t
    if linear_slack <= 0:
        raise AssertionError((h, t, a, b, d, linear_slack))

    # Nonvanishing inequalities under the extremal allowed p^3 > h^4 T.
    p_min = min_p_for_h4t(h, t)
    nonvanishing_slack = p_min - (a + h * b)
    if a * b > h or nonvanishing_slack <= 0:
        raise AssertionError((h, t, a, b, d, a * b, p_min, nonvanishing_slack))

    # Degree bound: ((A+2hB)/D)^3 <= K^3 (hT)^2.
    degree_num = a + 2 * h * b
    if degree_num**3 > K_RICH**3 * (h * t) ** 2 * d**3:
        raise AssertionError((h, t, a, b, d, degree_num))

    return ParameterRow(h, t, "stepanov", a, b, d, linear_slack, nonvanishing_slack)


def selected_t_values(h: int) -> list[int]:
    values = {1, 2, 3, h, h * h}
    transition = max(1, h * h // TRIVIAL_X_MAX**3)
    for delta in range(-8, 9):
        values.add(max(1, transition + delta))
    root = isqrt(h)
    values.update({max(1, root - 1), root, root + 1})
    return sorted(values)


def main() -> None:
    rows: list[ParameterRow] = []
    h_values = list(range(1, 1025))
    h_values += [
        1536,
        2048,
        4096,
        8192,
        16384,
        65536,
        10**6,
        7_639_006,
        2**23,
        2**32,
        2**41,
    ]
    for h in h_values:
        for t in selected_t_values(h):
            rows.append(parameter_row(h, t))

    # Deterministic active-branch stress rows with prescribed X scale.
    for x in (TRIVIAL_X_MAX + 1, 5000, 8192, 16384, 65536):
        h = x * x
        for t in (1, 2, 7, 31, 257):
            rows.append(parameter_row(h, t))

    trivial = sum(1 for row in rows if row.branch == "trivial")
    stepanov = len(rows) - trivial
    min_linear = min((row.linear_slack for row in rows if row.branch == "stepanov"), default=0)
    min_nonvanishing = min(
        (row.nonvanishing_slack for row in rows if row.branch == "stepanov"),
        default=0,
    )
    h2_threshold = Fraction(ENERGY_CONSTANT, 8) ** 2

    official_powers = []
    for exponent in range(13, 42):
        n = 2**exponent
        covered = Fraction(n, 1) > h2_threshold
        official_powers.append((exponent, n, covered))

    first_power = next(exp for exp, _, covered in official_powers if covered)
    last_uncovered = max(exp for exp, _, covered in official_powers if not covered)

    print(f"K_RICH_OPTIMIZED = {K_RICH}")
    print(f"ENERGY_CONSTANT_OPTIMIZED = {ENERGY_CONSTANT}")
    print(f"T2 floor threshold = {h2_threshold}")
    print("integer coverage starts at h >= 7639006")
    print(f"official powers covered from 2^{first_power}; last uncovered power 2^{last_uncovered}")
    print(f"parameter rows checked = {len(rows)}")
    print(f"branches: trivial={trivial}, stepanov={stepanov}")
    print(f"minimum linear-system slack = {min_linear}")
    print(f"minimum nonvanishing slack = {min_nonvanishing}")
    if first_power != 23 or last_uncovered != 22:
        raise AssertionError((first_power, last_uncovered))
    if min_linear <= 0 or min_nonvanishing <= 0:
        raise AssertionError((min_linear, min_nonvanishing))
    print("H2_RICH_COSET_OPTIMIZED_PASS")


if __name__ == "__main__":
    main()
