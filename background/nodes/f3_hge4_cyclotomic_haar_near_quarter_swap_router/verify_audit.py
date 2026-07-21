#!/usr/bin/env python3
"""Independent audit for the cyclotomic-Haar swap router."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "background" / "nodes" / "f3_hge4_cyclotomic_haar_near_quarter_swap_router"


def log_two_bounds(terms: int = 40) -> tuple[Fraction, Fraction]:
    # log(2)=2 atanh(1/3); the positive tail has an elementary geometric bound.
    x = Fraction(1, 3)
    partial = 2 * sum(
        (x ** (2 * index + 1) / (2 * index + 1) for index in range(terms)),
        Fraction(0),
    )
    tail = (
        2 * x ** (2 * terms + 1)
        / Fraction(2 * terms + 1)
        / (1 - x * x)
    )
    return partial, partial + tail


def band_expression(exponent: int, defect: int, log_bound: Fraction) -> Fraction:
    return 64 * (defect + 1) ** 2 * (exponent * log_bound) ** 2


def log_fraction_bounds(
    value: Fraction,
    lower_log_two: Fraction,
    upper_log_two: Fraction,
    terms: int = 50,
) -> tuple[Fraction, Fraction]:
    assert value > 0
    shift = 0
    while value >= 2:
        value /= 2
        shift += 1
    while value < 1:
        value *= 2
        shift -= 1
    y = (value - 1) / (value + 1)
    partial = 2 * sum(
        (y ** (2 * index + 1) / (2 * index + 1) for index in range(terms)),
        Fraction(0),
    )
    tail = Fraction(0)
    if y:
        tail = (
            2 * y ** (2 * terms + 1)
            / Fraction(2 * terms + 1)
            / (1 - y * y)
        )
    if shift >= 0:
        return (
            shift * lower_log_two + partial,
            shift * upper_log_two + partial + tail,
        )
    return (
        shift * upper_log_two + partial,
        shift * lower_log_two + partial + tail,
    )


def certified_exact_status(exponent: int, defect: int) -> bool:
    lower_log_two, upper_log_two = log_two_bounds()
    order = 1 << exponent
    width = order // 4 - defect
    x_lower = 4 * (defect + 1) * exponent * lower_log_two
    x_upper = 4 * (defect + 1) * exponent * upper_log_two

    tower_depth = 0
    while Fraction(1 << tower_depth) < x_upper:
        tower_depth += 1
    block_count = 1 << tower_depth
    assert x_lower > Fraction(block_count, 2)
    assert x_upper < block_count
    if block_count >= width:
        return False

    log_x_lower, _ = log_fraction_bounds(
        x_lower, lower_log_two, upper_log_two
    )
    _, log_x_upper = log_fraction_bounds(
        x_upper, lower_log_two, upper_log_two
    )
    lhs_lower = tower_depth * lower_log_two + log_x_lower
    lhs_upper = tower_depth * upper_log_two + log_x_upper
    exponent_factor = Fraction(
        exponent * (order - 4 * defect - 8 * block_count), order
    )
    if exponent_factor <= 0:
        return False
    rhs_lower = exponent_factor * lower_log_two
    rhs_upper = exponent_factor * upper_log_two
    if lhs_upper < rhs_lower:
        return True
    if lhs_lower >= rhs_upper:
        return False
    raise AssertionError("insufficient rational precision at exact-band boundary")


def exact_boundary_audit() -> None:
    exact_caps = {
        15: 2, 16: 3, 17: 4, 18: 7, 19: 8, 20: 15, 21: 16,
        22: 30, 23: 31, 24: 58, 25: 58, 26: 110, 27: 108,
        28: 208, 29: 202, 30: 390, 31: 380, 32: 735, 33: 715,
        34: 1387, 35: 1349, 36: 2623, 37: 2554, 38: 4973,
        39: 4847, 40: 9451, 41: 9223,
    }
    for exponent in range(4, 15):
        assert not certified_exact_status(exponent, 1)
    for exponent, cap in exact_caps.items():
        assert certified_exact_status(exponent, cap)
        assert not certified_exact_status(exponent, cap + 1)
    assert sum(exact_caps.values()) == 39_487


def clean_boundary_audit() -> None:
    lower_log_two, upper_log_two = log_two_bounds()
    first = None
    for exponent in range(4, 42):
        order = 1 << exponent
        if band_expression(exponent, 1, upper_log_two) < order:
            first = exponent
            break
    assert first == 15
    assert band_expression(14, 1, lower_log_two) >= 1 << 14

    assert band_expression(41, 6521, upper_log_two) < 1 << 41
    assert band_expression(41, 6522, lower_log_two) >= 1 << 41


def mutation_audit() -> None:
    # Odd widths use floor(h/2), so replacing d+1 by d in the first defect
    # estimate is an invalid strengthening at the first admitted cell.
    order = 1 << 15
    defect = 1
    width = order // 4 - defect
    assert width % 2 == 1
    exact_exponent = 8 * (width // 2) / order
    assert exact_exponent == 1 - 4 * (defect + 1) / order
    assert exact_exponent < 1 - 4 * defect / order

    # Strict p>m^2 is needed to turn norm equality into the strict defect
    # bound used by the repetition argument.
    quarter = order // 4
    rank = quarter // 2
    assert (order * order) ** rank == order ** quarter
    assert (order * order + 1) ** rank > order ** quarter


def repetition_audit() -> None:
    base = [1, 0, -1]
    for depth in range(1, 8):
        repeated = base * (1 << depth)
        norm = sum(value * value for value in repeated)
        assert norm % (1 << depth) == 0
        assert norm >= (1 << depth)


def packet_language_audit() -> None:
    statement = (BASE / "statement.md").read_text()
    proof = (BASE / "proof.md").read_text()
    result = (BASE / "result.md").read_text()
    assert "every primitive exact-level top" in statement
    assert "when `h` is even" in statement
    assert "D_v>m^(1-(4d+8B)/m)>BX" in proof and "D_v<=2^v L" in proof
    assert "(CHQ2-exact)" in statement and "closed-form" in result
    assert "odd swap" in result
    assert "HGE4 is proved" not in statement + proof + result


def main() -> None:
    exact_boundary_audit()
    clean_boundary_audit()
    mutation_audit()
    repetition_audit()
    packet_language_audit()
    print("F3_HGE4_CYCLOTOMIC_HAAR_NEAR_QUARTER_SWAP_ROUTER_AUDIT_PASS")


if __name__ == "__main__":
    main()
