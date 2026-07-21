#!/usr/bin/env python3
"""Independent audit for the HGE4 Vandermonde-defect exclusion."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "background" / "nodes" / "f3_hge4_vandermonde_defect_band_exclusion"
EXPECTED_CAPS = {
    9: 2, 10: 4, 11: 9, 12: 17, 13: 33, 14: 61, 15: 115,
    16: 215, 17: 404, 18: 761, 19: 1437, 20: 2720, 21: 5164,
    22: 9827, 23: 18742, 24: 35824, 25: 68606, 26: 131623,
    27: 252943, 28: 486832, 29: 938320, 30: 1810906,
    31: 3499241, 32: 6769391, 33: 13109649, 34: 25413774,
    35: 49312552, 36: 95770531, 37: 186153140, 38: 362120147,
    39: 704953197, 40: 1373333614, 41: 2677220820,
}


def log_two_bounds(terms: int = 48) -> tuple[Fraction, Fraction]:
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


def certified_status(exponent: int, defect: int) -> bool:
    lower_log_two, upper_log_two = log_two_bounds()
    order = 1 << exponent
    width = order // 4 - defect
    if defect < 1 or width < 4:
        return False
    rank_floor = (width - 1) // 2 + 2
    radius = defect + 1

    def cubic_ceiling(logarithm: Fraction) -> Fraction:
        return (
            4 * (radius * exponent * logarithm - defect)
            - Fraction(8 * radius**2 * exponent**2, order) * logarithm**2
            + Fraction(32 * radius**3 * exponent**3, 3 * order**2)
            * logarithm**3
        )

    x_lower = Fraction(4 * radius * exponent, order) * lower_log_two
    x_upper = Fraction(4 * radius * exponent, order) * upper_log_two
    lower = cubic_ceiling(lower_log_two)
    upper = cubic_ceiling(upper_log_two)
    if x_lower > 1:
        return False
    if x_upper > 1:
        raise AssertionError("insufficient rational precision at guard boundary")
    if upper <= rank_floor:
        return True
    if lower > rank_floor:
        return False
    raise AssertionError("insufficient rational precision at band boundary")


def boundary_audit() -> None:
    for exponent in range(4, 9):
        assert not certified_status(exponent, 1)
    for exponent, cap in EXPECTED_CAPS.items():
        assert certified_status(exponent, cap)
        assert not certified_status(exponent, cap + 1)
    assert sum(EXPECTED_CAPS.values()) == 5_501_420_621


def vandermonde_audit() -> None:
    prime = 97
    generator = 8  # Exact order 16 in F_97.
    assert pow(generator, 16, prime) == 1 and pow(generator, 8, prime) != 1
    points = [pow(generator, index, prime) for index in range(16)]
    for size in range(1, 6):
        for indices in combinations(range(16), size):
            determinant = 1
            for left, right in combinations(indices, 2):
                determinant = determinant * (points[right] - points[left]) % prime
            assert determinant

    # Omitting the size equation loses one rank: one moment cannot determine
    # two supported coefficients.
    left, right = points[1], points[3]
    mutation = (right, -left)
    assert (mutation[0] * left + mutation[1] * right) % prime == 0
    assert any(value % prime for value in mutation)


def defect_energy_audit() -> None:
    for support_size in range(1, 7):
        for values in product((-2, -1, 1, 2), repeat=support_size):
            if sum(values):
                continue
            energy = sum(value * value for value in values)
            assert energy >= support_size
            assert energy % 2 == 0
            if support_size % 2:
                assert energy >= support_size + 1


def packet_language_audit() -> None:
    statement = (BASE / "statement.md").read_text()
    proof = (BASE / "proof.md").read_text()
    result = (BASE / "result.md").read_text()
    assert "consecutive" in statement and "even moments" in statement
    assert "exp(-x)>=1-x+x^2/2-x^3/6" in proof
    assert "determinant" in proof and "`p` is odd" in proof
    assert "HGE4 remains open" in result
    assert "HGE4 is proved" not in statement + proof + result


def main() -> None:
    boundary_audit()
    vandermonde_audit()
    defect_energy_audit()
    packet_language_audit()
    print("F3_HGE4_VANDERMONDE_DEFECT_BAND_EXCLUSION_AUDIT_PASS")


if __name__ == "__main__":
    main()
